#!/usr/bin/env python3
"""mukiwa-grab: descarga video / audio / fotos desde casi cualquier link.
Corre en la compu de Bryan (internet normal, Python 3.9+, sin Homebrew).
Guarda en ../../_descargas/<fecha>-<titulo>/

Uso:
  python3 grab.py URL [URL2 ...] [--out DIR] [--cookies chrome|safari|firefox] [--audio-only]
                  [--photos-only] [--max-height 1080] [--no-subs] [--frames]
Genera: video.mp4, audio.mp3, subs *.srt, miniatura, fotos/ (carruseles), info.json, LEEME.md
"""
import argparse, datetime, glob, os, re, shutil, subprocess, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.abspath(os.path.join(HERE, "..", "..", "_descargas"))
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")
AV_EXT = (".mp4", ".mov", ".webm", ".mkv", ".mp3", ".m4a", ".wav", ".aac", ".ogg")
VIDEO_ONLY = ("youtube.", "youtu.be", "vimeo.", "tiktok.")
PHOTO_SITES = ("pinterest.", "pin.it", "behance.net", "flickr.com", "unsplash.com", "pexels.com",
               "dribbble.com", "artstation.com", "imgur.com")
YT = GDL = None; FF = None; JS = []

BIN_DIR = os.path.abspath(os.path.join(HERE, "..", "bin"))

def find_cmd(exe, module):
    own = os.path.join(BIN_DIR, exe)
    if os.path.exists(own): return [own]
    p = shutil.which(exe)
    if p: return [p]
    dirs = glob.glob(os.path.expanduser("~/Library/Python/*/bin")) + [os.path.expanduser("~/.local/bin")]
    for d in dirs:
        c = os.path.join(d, exe)
        if os.path.exists(c): return [c]
    r = subprocess.run([sys.executable, "-c", f"import {module}"], capture_output=True)
    return [sys.executable, "-m", module] if r.returncode == 0 else None

def find_ffmpeg():
    p = shutil.which("ffmpeg")
    if p: return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None

def ensure_tools():
    global YT, GDL, FF
    YT = find_cmd("yt-dlp", "yt_dlp"); deno = os.path.join(BIN_DIR, "deno")
    if os.path.exists(deno): JS[:] = ["--js-runtimes", "deno:" + deno, "--remote-components", "ejs:github"]
    GDL = find_cmd("gallery-dl", "gallery_dl"); FF = find_ffmpeg()
    if not YT or not FF:
        print("Faltan herramientas (yt-dlp / ffmpeg). Corre una vez:\n  bash \"%s\"" % os.path.join(HERE, "setup.sh"))
        sys.exit(2)

def slug(s, n=60):
    s = re.sub(r"[^\w\s-]", "", s, flags=re.U).strip().lower()
    return re.sub(r"[\s_-]+", "-", s)[:n] or "descarga"

def run(cmd):
    print("$", " ".join(cmd)); return subprocess.run(cmd).returncode

def direct(url, outdir):
    name = os.path.basename(urllib.parse.urlparse(url).path) or "archivo"
    dst = os.path.join(outdir, name)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r, open(dst, "wb") as f: shutil.copyfileobj(r, f)
    return dst

def grab(url, a):
    u = urllib.parse.urlparse(url); host = u.netloc.lower(); path = u.path.lower()
    os.makedirs(a.out, exist_ok=True)
    ck = ["--cookies-from-browser", a.cookies] if a.cookies else []
    title = "descarga"
    if not path.endswith(IMG_EXT + AV_EXT):
        r = subprocess.run(YT + ["--no-warnings", "--ffmpeg-location", FF] + JS + [ "--skip-download", "--playlist-items", "1",
                                 "--print", "%(title)s"] + ck + [url], capture_output=True, text=True)
        if r.stdout.strip(): title = r.stdout.strip().splitlines()[0]
        else: title = (host.split(".")[-2] if "." in host else host) + "-" + path.strip("/").replace("/", "-")
    d = os.path.join(a.out, "%s-%s" % (datetime.date.today().isoformat(), slug(title)))
    os.makedirs(d, exist_ok=True)
    if path.endswith(IMG_EXT + AV_EXT):
        direct(url, d)
    else:
        photo_first = any(s in host for s in PHOTO_SITES)
        ok = False
        if not photo_first and not a.photos_only:
            if a.audio_only:
                cmd = YT + ["-o", os.path.join(d, "audio.%(ext)s"), "-x", "--audio-format", "mp3", "--write-info-json", "--no-playlist"]
            else:
                fmt = "bv*[height<=%d]+ba/b[height<=%d]/b" % (a.max_height, a.max_height)
                cmd = YT + ["-o", os.path.join(d, "video.%(ext)s"), "-f", fmt, "--merge-output-format", "mp4",
                            "--write-thumbnail", "--convert-thumbnails", "jpg", "--write-info-json", "--no-playlist"]
            have = os.path.join(d, "audio.mp3" if a.audio_only else "video.mp4")
            if a.subs_only:                                 # solo subtítulos + info: no bajar el video
                ok = os.path.exists(os.path.join(d, "video.info.json")) or run(YT + ["-o", os.path.join(d, "video.%(ext)s"),
                    "--skip-download", "--write-info-json", "--no-playlist"] + JS + ck + [url]) == 0
            elif os.path.exists(have): print("Ya descargado, se reutiliza:", have); ok = True
            else: ok = run(cmd + ["--ffmpeg-location", FF] + JS + ck + [url]) == 0
            if not a.no_subs:  # subtítulos aparte y NO fatales (YouTube da 429 a veces); se borran los .vtt sueltos si hay .srt
                for langs in ("es.*", "en.*"):
                    if glob.glob(os.path.join(d, "video.%s.srt" % langs)): continue   # ya están: no pedir de nuevo (evita 429)
                    run(YT + ["-o", os.path.join(d, "video.%(ext)s"), "--skip-download", "--write-subs", "--write-auto-subs",
                              "--sub-langs", langs, "--convert-subs", "srt", "--sleep-subtitles", "2", "--no-playlist",
                              "--ffmpeg-location", FF] + JS + ck + [url])
            if ok and not a.audio_only and os.path.exists(os.path.join(d, "video.mp4")) and not os.path.exists(os.path.join(d, "audio.mp3")):
                run([FF, "-y", "-loglevel", "error", "-i", os.path.join(d, "video.mp4"), "-vn", "-q:a", "2",
                     os.path.join(d, "audio.mp3")])
        if (not ok or photo_first or a.photos_only):
            if any(v in host for v in VIDEO_ONLY) and not a.photos_only: print("yt-dlp falló en un sitio de video; revisa el error de arriba.")
            elif GDL: run(GDL + ["-d", os.path.join(d, "fotos"), "-o", "directory=[]"] + ck + [url])
            else: print("yt-dlp no pudo y gallery-dl no está disponible (corre setup.sh).")
    files = sorted(os.path.relpath(os.path.join(r, f), d) for r, _, fs in os.walk(d) for f in fs if f != "LEEME.md" and not f.startswith("._"))  # ._x = metadatos macOS en exFAT
    with open(os.path.join(d, "LEEME.md"), "w") as f:
        f.write("# %s\n\n- Fuente: %s\n- Fecha: %s\n- Archivos:\n%s\n" % (
            title, url, datetime.date.today().isoformat(), "\n".join("  - " + x for x in files)))
    got = any(x.lower().endswith(IMG_EXT + AV_EXT + ((".srt",) if a.subs_only else ())) for x in files)
    print(("\nOK -> %s" if got else "\nFALLO (no se bajó nada; revisa el error de arriba) -> %s") % d); [print("  " + x) for x in files]
    if not files and "instagram" in host:
        print("\nPISTA Instagram: necesita sesión. Si viste 'Operation not permitted' o 'could not find chrome cookies':\n  Ajustes del Sistema > Privacidad y seguridad > Acceso total al disco > activa Terminal, cierra Terminal (Cmd+Q) y reábrela.")
    if a.frames and os.path.exists(os.path.join(d, "video.mp4")):
        ef = os.path.abspath(os.path.join(HERE, "..", "..", "mukiwa-learn", "scripts", "extract_frames.py"))
        if os.path.exists(ef): run([sys.executable, ef, os.path.join(d, "video.mp4"), "--out", os.path.join(d, "frames_work")])
    return d if got else None

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*"); ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--cookies", default=None, help="chrome|safari|firefox|edge para links privados/login")
    ap.add_argument("--audio-only", action="store_true"); ap.add_argument("--photos-only", action="store_true")
    ap.add_argument("--max-height", type=int, default=1080); ap.add_argument("--no-subs", action="store_true")
    ap.add_argument("--frames", action="store_true")
    ap.add_argument("--subs-only", action="store_true", help="solo subtítulos + info, sin bajar el video (nivel transcript)")
    a = ap.parse_args()
    urls = a.urls
    if not urls:  # modo interactivo: pegar el link cuando lo pida
        raw = input("Pega el link (o varios separados por espacio) y Enter: ").strip()
        urls = raw.split()
    bad = [u for u in urls if not re.match(r"^https?://", u)]
    if not urls or bad:
        print("Eso no es un link v\u00e1lido: %s\nDebe empezar con https:// (c\u00f3pialo desde Instagram/YouTube/TikTok)." % (" ".join(bad) or "(vac\u00edo)"))
        sys.exit(1)
    ensure_tools()
    results = [grab(url, a) for url in urls]
    sys.exit(0 if all(results) else 1)
