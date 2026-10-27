#!/usr/bin/env python3
"""Los 'ojos': extrae frames clave con timestamp y arma contact sheets para leerlos con Read.

Uso:
  python extract_frames.py VIDEO --out DIR [--mode scene|uniform|both] [--max 60]
                           [--every 5] [--threshold 0.30] [--width 960]
                           [--start 0] [--end SEG] [--sheet-cols 3]
                           [--at 13:11,4:32] [--at-width 1280] [--no-dedup]
  --at      capturas fijas en segundos exactos, a resolución alta para leer texto/código.
  --max 0   solo las capturas de --at.
  Las capturas casi idénticas se descartan (salvo las fijas); manifest.json informa cuántas
  y el hueco máximo entre capturas, para saber qué tanto del video quedó sin mirar.
Genera:
  DIR/frames/f_0001_t00-12.40.jpg ...   (un frame por momento clave)
  DIR/sheets/sheet_01.jpg ...           (cuadrículas con timestamp grabado, 9 frames c/u)
  DIR/manifest.json                     (lista frame -> segundo)
Modos:
  scene   = cambios de plano/corte (ffmpeg select scene) -> ideal para ediciones rápidas
  uniform = un frame cada N seg  -> ideal para tutoriales de pantalla/lentos
  both    = unión de ambos (default), repartida por tramos de tiempo hasta --max
"""
import argparse, json, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

import sys, shutil
def _ffmpeg():
    w = shutil.which("ffmpeg")
    if w: return w
    try:
        import imageio_ffmpeg; return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("NO_FFMPEG: instala ffmpeg o `pip install imageio-ffmpeg` (en la Mac: mukiwa-ver-videos/scripts/setup.sh)")
FFMPEG = None
def sh(cmd):
    global FFMPEG
    if FFMPEG is None: FFMPEG = _ffmpeg()
    if cmd[0] in ("ffmpeg","ffprobe"): cmd = [FFMPEG] + cmd[1:] if cmd[0]=="ffmpeg" else cmd
    try:
        return subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        class R: stdout=""; stderr=""; returncode=127
        return R()

def duration(p):
    r = sh(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",p])
    try:
        if r.stdout.strip(): return float(r.stdout.strip())
    except ValueError: pass
    r = sh(["ffmpeg","-hide_banner","-i",p])   # sin ffprobe: leer "Duration: HH:MM:SS.xx" de ffmpeg
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", r.stderr)
    return int(m.group(1))*3600+int(m.group(2))*60+float(m.group(3)) if m else 0.0

def scene_times(p, thr, start, end):
    cmd = ["ffmpeg","-hide_banner","-nostats"]
    if start: cmd += ["-ss", str(start)]
    if end: cmd += ["-to", str(end)]
    cmd += ["-i",p,"-vf",f"select='gt(scene,{thr})',showinfo","-an","-f","null","-"]
    r = sh(cmd)
    ts = [float(m.group(1)) + (start or 0) for m in re.finditer(r"pts_time:([\d.]+)", r.stderr)]
    return ts

def thin(times, max_n):
    times = sorted(set(round(t,2) for t in times))
    if len(times) <= max_n: return times
    if max_n == 1: return [times[0]]
    return [times[round(i*(len(times)-1)/(max_n-1))] for i in range(max_n)]

def spread(times, start, end, max_n):
    """Reparte el presupuesto por tramos iguales de tiempo: en cada tramo, el candidato
    (corte de escena) más cercano a su centro, o el centro si el tramo no tiene cortes.
    Evita que una intro con muchos cortes se coma todas las capturas (thin las amontonaba)."""
    times = sorted(set(round(t,2) for t in times))
    if len(times) <= max_n: return times
    if max_n <= 2: return thin(times, max_n)
    first, last = times[0], times[-1]                 # primer y último instante siempre (el hook vive en el 0)
    start, end, max_n = first, last, max_n-2
    times = [t for t in times if first < t < last]
    step = (end-start)/max_n; out = [first, last]
    for i in range(max_n):
        a, b = start+i*step, start+(i+1)*step; mid = (a+b)/2
        inside = [t for t in times if a <= t < b]
        out.append(min(inside, key=lambda t: abs(t-mid)) if inside else round(mid,2))
    return sorted(set(out))

def max_gap(times, start, end):
    pts = [start] + sorted(times) + [end]
    return round(max(b-a for a,b in zip(pts, pts[1:])), 2)

DEDUP_THUMB, DEDUP_THRESHOLD = 16, 2.0   # mismos valores que Watch (bradautomates/claude-video)

def thumb(path):
    try: return Image.open(path).convert("RGB").resize((DEDUP_THUMB,DEDUP_THUMB)).tobytes()
    except Exception: return b""

def dedupe(frames, threshold=DEDUP_THRESHOLD, max_hole=None):
    """Descarta capturas casi idénticas a la última conservada (diferencia media por píxel
    en miniaturas de 16x16). Las fijadas con --at, la primera y la última nunca se descartan.
    max_hole: no descartar si eso deja más de N s sin captura (Watch muestrea denso; aquí las
    capturas están espaciadas y descartar sin tope abría huecos de minutos).
    Cambios sutiles de código/texto pueden perderse: para eso --no-dedup o --at."""
    kept, last, last_t, dropped = [], b"", None, 0
    for i,f in enumerate(frames):
        th = thumb(f["file"])
        protect = f.get("reason") != "detail" or i == len(frames)-1 or not last or not th or len(th) != len(last)
        if not protect and max_hole is not None and i+1 < len(frames) and frames[i+1]["t"]-last_t > max_hole:
            protect = True
        if not protect and sum(abs(x-y) for x,y in zip(th,last))/len(th) <= threshold:
            os.remove(f["file"]); dropped += 1
        else:
            kept.append(f); last = th or last; last_t = f["t"]
    return kept, dropped

def parse_at(value):
    """'13:11,4:32.5,95' -> [791.0, 272.5, 95.0]"""
    out = []
    for part in (value or "").split(","):
        part = part.strip()
        if not part: continue
        if not re.fullmatch(r"\d+(?::\d{1,2}){0,2}(?:\.\d+)?", part):
            raise ValueError("tiempo inválido en --at: %r (usar SS, MM:SS o HH:MM:SS)" % part)
        secs = 0.0
        for p in part.split(":"): secs = secs*60 + float(p)
        out.append(secs)
    return sorted(set(out))

def grab(p, t, outp, width):
    sh(["ffmpeg","-y","-hide_banner","-loglevel","error","-ss",f"{t:.2f}","-i",p,
        "-frames:v","1","-vf",f"scale='min({width},iw)':-2","-q:v","3",outp])   # nunca agrandar: no agrega detalle
    return os.path.exists(outp)

def sheets(frames, out, cols, tile_w=480):
    os.makedirs(out, exist_ok=True)
    per = cols*3
    try: font = ImageFont.truetype("DejaVuSans-Bold.ttf", 22)
    except Exception: font = ImageFont.load_default()
    paths = []
    for si in range(0, len(frames), per):
        chunk = frames[si:si+per]
        ims = []
        for f in chunk:
            im = Image.open(f["file"]).convert("RGB")
            h = int(im.height*tile_w/im.width)
            im = im.resize((tile_w,h))
            d = ImageDraw.Draw(im)
            lab = f"{int(f['t']//60):02d}:{f['t']%60:05.2f}"
            d.rectangle([0,0,110,28], fill=(0,0,0))
            d.text((6,2), lab, fill=(197,237,46), font=font)
            ims.append(im)
        th = max(i.height for i in ims)
        rows = (len(ims)+cols-1)//cols
        sheet = Image.new("RGB",(cols*tile_w, rows*th),(20,20,20))
        for i,im in enumerate(ims):
            sheet.paste(im, ((i%cols)*tile_w, (i//cols)*th))
        pth = os.path.join(out, f"sheet_{si//per+1:02d}.jpg")
        sheet.save(pth, quality=85); paths.append(pth)
    return paths

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--out", required=True)
    ap.add_argument("--mode", default="both", choices=["scene","uniform","both"])
    ap.add_argument("--max", type=int, default=60)
    ap.add_argument("--every", type=float, default=0, help="seg entre frames uniformes (0=auto)")
    ap.add_argument("--threshold", type=float, default=0.30)
    ap.add_argument("--width", type=int, default=960)
    ap.add_argument("--start", type=float, default=0); ap.add_argument("--end", type=float, default=0)
    ap.add_argument("--sheet-cols", type=int, default=3)
    ap.add_argument("--at", default="", help="tiempos fijos SS, MM:SS o HH:MM:SS separados por coma (capturas a --at-width)")
    ap.add_argument("--at-width", type=int, default=1280, help="ancho de las capturas fijas, para leer texto")
    ap.add_argument("--no-dedup", action="store_true", help="conservar capturas casi idénticas")
    a = ap.parse_args()
    if a.max < 0 or a.every < 0 or a.width < 2 or a.at_width < 2 or a.sheet_cols < 1 or a.start < 0:
        ap.error("Parámetros de muestreo inválidos")
    try: pinned = parse_at(a.at)
    except ValueError as e: ap.error(str(e))
    fdir = os.path.join(a.out,"frames"); os.makedirs(fdir, exist_ok=True)
    dur = duration(a.video); end = min(a.end or dur, dur)
    if dur <= 0 or a.start >= end:
        ap.error("Archivo sin duración válida o rango vacío")
    outside = [t for t in pinned if not (a.start <= t < end)]
    pinned = [t for t in pinned if a.start <= t < end]
    times = []; cuts = None
    if a.max == 0: pass                                   # solo capturas fijas (--at)
    elif a.mode in ("scene","both"):
        cuts = scene_times(a.video, a.threshold, a.start, a.end or None)
        times += cuts
        if len(times) < 4 and a.mode == "scene":      # pocos cortes -> bajar umbral
            times = scene_times(a.video, a.threshold/2, a.start, a.end or None)
    if a.max and (a.mode in ("uniform","both") or len(times) < 4):
        every = a.every or max(2.0, (end-a.start)/min(a.max, 40))
        t = a.start + every/2
        while t < end: times.append(t); t += every
    if a.max:
        times = [a.start+0.05] + times if (a.start+0.05) not in times else times
        times.append(max(a.start, end - 0.1))
        times = [t for t in times if a.start <= t < end]
        times = thin(times, a.max) if a.mode == "uniform" else spread(times, a.start, end, a.max)
    plan = sorted([(t,"detail") for t in times if round(t,2) not in [round(p,2) for p in pinned]] +
                  [(t,"pinned") for t in pinned])
    frames = []
    for i,(t,reason) in enumerate(plan,1):
        fp = os.path.join(fdir, f"f_{i:04d}_t{t:08.2f}{'_fija' if reason=='pinned' else ''}.jpg")
        if grab(a.video, t, fp, a.at_width if reason=="pinned" else a.width): frames.append({"file":fp,"t":round(t,2),"reason":reason})
    if not frames: sys.exit("NO_FRAMES: no se extrajo ninguna imagen")
    dropped = 0
    if not a.no_dedup: frames, dropped = dedupe(frames, max_hole=2*(end-a.start)/max(a.max, 1))
    sh_paths = sheets(frames, os.path.join(a.out,"sheets"), a.sheet_cols)
    man = {"video":a.video,"duration_s":dur,"n_frames":len(frames),"evidence_type":"sampled_frames","range_s":[a.start,end],"mode":a.mode,
           "max_gap_s":max_gap([f["t"] for f in frames], a.start, end),"dedup_dropped":dropped,
           "scene_cuts":None if cuts is None else sorted(round(t,2) for t in cuts),"scene_threshold":a.threshold,
           "pinned":[f["file"] for f in frames if f["reason"]=="pinned"],"pinned_outside_range":outside,
           "frames":frames,"sheets":sh_paths}
    json.dump(man, open(os.path.join(a.out,"manifest.json"),"w"), indent=1)
    print(f"OK {len(frames)} frames ({dropped} casi idénticos descartados, hueco máx {man['max_gap_s']} s), {len(sh_paths)} sheets -> {a.out}")
    for p in sh_paths: print(p)

if __name__ == "__main__":
    main()
