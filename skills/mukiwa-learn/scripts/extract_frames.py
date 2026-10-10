#!/usr/bin/env python3
"""Los 'ojos': extrae frames clave con timestamp y arma contact sheets para leerlos con Read.

Uso:
  python extract_frames.py VIDEO --out DIR [--mode scene|uniform|both] [--max 60]
                           [--every 5] [--threshold 0.30] [--width 960]
                           [--start 0] [--end SEG] [--sheet-cols 3]
Genera:
  DIR/frames/f_0001_t00-12.40.jpg ...   (un frame por momento clave)
  DIR/sheets/sheet_01.jpg ...           (cuadrículas con timestamp grabado, 9 frames c/u)
  DIR/manifest.json                     (lista frame -> segundo)
Modos:
  scene   = cambios de plano/corte (ffmpeg select scene) -> ideal para ediciones rápidas
  uniform = un frame cada N seg  -> ideal para tutoriales de pantalla/lentos
  both    = unión de ambos (default), recortada a --max
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
        sys.exit("NO_FFMPEG: instala ffmpeg o `pip install imageio-ffmpeg` (en la Mac: mukiwa-grab/scripts/setup.sh)")
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

def grab(p, t, outp, width):
    sh(["ffmpeg","-y","-hide_banner","-loglevel","error","-ss",f"{t:.2f}","-i",p,
        "-frames:v","1","-vf",f"scale={width}:-2","-q:v","3",outp])
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
    a = ap.parse_args()
    if a.max < 1 or a.every < 0 or a.width < 2 or a.sheet_cols < 1 or a.start < 0:
        ap.error("Parámetros de muestreo inválidos")
    fdir = os.path.join(a.out,"frames"); os.makedirs(fdir, exist_ok=True)
    dur = duration(a.video); end = min(a.end or dur, dur)
    if dur <= 0 or a.start >= end:
        ap.error("Archivo sin duración válida o rango vacío")
    times = []
    if a.mode in ("scene","both"):
        times += scene_times(a.video, a.threshold, a.start, a.end or None)
        if len(times) < 4 and a.mode == "scene":      # pocos cortes -> bajar umbral
            times = scene_times(a.video, a.threshold/2, a.start, a.end or None)
    if a.mode in ("uniform","both") or len(times) < 4:
        every = a.every or max(2.0, (end-a.start)/min(a.max, 40))
        t = a.start + every/2
        while t < end: times.append(t); t += every
    times = [a.start+0.05] + times if (a.start+0.05) not in times else times
    times.append(max(a.start, end - 0.1))
    times = thin([t for t in times if a.start <= t < end], a.max)
    frames = []
    for i,t in enumerate(times,1):
        fp = os.path.join(fdir, f"f_{i:04d}_t{t:08.2f}.jpg")
        if grab(a.video, t, fp, a.width): frames.append({"file":fp,"t":t})
    if not frames: sys.exit("NO_FRAMES: no se extrajo ninguna imagen")
    sh_paths = sheets(frames, os.path.join(a.out,"sheets"), a.sheet_cols)
    man = {"video":a.video,"duration_s":dur,"n_frames":len(frames),"evidence_type":"sampled_frames","range_s":[a.start,end],"mode":a.mode,"frames":frames,"sheets":sh_paths}
    json.dump(man, open(os.path.join(a.out,"manifest.json"),"w"), indent=1)
    print(f"OK {len(frames)} frames, {len(sh_paths)} sheets -> {a.out}")
    for p in sh_paths: print(p)

if __name__ == "__main__":
    main()
