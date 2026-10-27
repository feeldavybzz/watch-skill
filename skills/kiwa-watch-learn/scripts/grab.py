#!/usr/bin/env python3
"""kiwa-watch-learn (bajar): descarga video / audio / fotos desde casi cualquier link.
Corre en la compu de Bryan (internet normal, Python 3.9+, sin Homebrew).
Guarda en ../../_descargas/<fecha>-<titulo>/

Uso:
  python3 grab.py URL [URL2 ...] [--out DIR] [--cookies chrome|safari|firefox] [--audio-only]
                  [--photos-only] [--max-height 1080] [--no-subs] [--frames]
Genera: video.mp4, audio.mp3, subs *.srt, miniatura, fotos/ (carruseles), info.json, LEEME.md
"""
import argparse, datetime, glob, json, os, re, shutil, subprocess, sys, time, urllib.parse, urllib.request

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

def find_js_runtime(which=shutil.which, home=None):
    """Runtime de JavaScript que YouTube exige a yt-dlp para resolver sus desafíos.
    Orden: deno propio (bin/), deno, node, bun. Node casi nunca está en el PATH: se busca también en
    ~/nodejs/node-v*/bin (la versión más alta) y en las rutas de Homebrew. Devuelve (nombre, ruta) o None."""
    home = home or os.path.expanduser("~")
    own = os.path.join(BIN_DIR, "deno")
    if os.path.exists(own): return ("deno", own)
    for name in ("deno", "node", "bun"):
        p = which(name)
        if p: return (name, p)
        if name == "node":
            ver = lambda c: [int(x) for x in re.findall(r"\d+", os.path.basename(os.path.dirname(os.path.dirname(c))))]
            found = sorted(glob.glob(os.path.join(home, "nodejs", "node-v*", "bin", "node")), key=ver, reverse=True)
            for c in found + ["/opt/homebrew/bin/node", "/usr/local/bin/node"]:
                if os.path.isfile(c) and os.access(c, os.X_OK): return ("node", c)
    return None

def ensure_tools():
    global YT, GDL, FF
    YT = find_cmd("yt-dlp", "yt_dlp"); rt = find_js_runtime()
    if rt:
        # El runtime ejecuta el solucionador oficial de desafíos de YouTube (yt-dlp/ejs): yt-dlp lo descarga una vez a
        # ~/.cache/yt-dlp y lo reutiliza. Sin él, algunos videos fallan con «This video is not available».
        JS[:] = ["--js-runtimes", "%s:%s" % rt, "--remote-components", "ejs:github"]
    GDL = find_cmd("gallery-dl", "gallery_dl"); FF = find_ffmpeg()
    if not YT or not FF:
        print("Faltan herramientas (yt-dlp / ffmpeg). Corre una vez:\n  bash \"%s\"" % os.path.join(HERE, "setup.sh"))
        sys.exit(2)

def slug(s, n=60):
    s = re.sub(r"[^\w\s-]", "", s, flags=re.U).strip().lower()
    return re.sub(r"[\s_-]+", "-", s)[:n] or "descarga"

# Causas de fallo conocidas: (código, patrón sobre las líneas de error, qué pasó, qué hacer, ¿vale reintentar?)
ARCHIVO = "Opción A: guarda el video en la carpeta «Para analizar» del buzón (o dame el archivo) y se analiza igual."
ERRORES = [
    ("429", r"HTTP Error 429|Too Many Requests", "La plataforma limitó las peticiones (demasiadas seguidas).",
     "Espera 10–15 minutos y reintenta una vez; no lo repitas en bucle. " + ARCHIVO, True),
    ("cookies", r"could not find .{0,20}cookies|cookies database|Failed to decrypt|cookies.{0,40}(Operation not permitted|not permitted)|Chrome Safe Storage",
     "No se pudieron leer las cookies de Chrome (sesión).",
     "Abre Chrome con tu sesión iniciada. Si macOS pide permiso al llavero («Chrome Safe Storage»), elige «Permitir siempre»; si dice «Operation not permitted», "
     "dale «Acceso total al disco» a la app desde la que corres esto (Ajustes → Privacidad y seguridad). " + ARCHIVO, False),
    ("login", r"Sign in to confirm|confirm you.re not a bot|login required|requiring login|rate-limit reached or login|"
              r"Please log in|empty media response|age-restricted|confirm your age|inappropriate for some users",
     "Este contenido pide sesión iniciada (o la plataforma sospecha que es un bot).",
     ARCHIVO + " Opción B: --cookies chrome usa tu sesión de Chrome en esta Mac (solo con tu permiso).", False),
    ("privado", r"Private video|video is private|account is private|This video is only available",
     "Es privado o solo para ciertas personas.", "Pide el archivo a su dueño o súbelo a «Para analizar».", False),
    ("no-existe", r"[Vv]ideo (is )?(no longer )?unavailable|video is not available|has been removed|no longer available|does not exist|Video not found|HTTP Error 404",
     "El video ya no existe o fue eliminado.", "Revisa que el link esté completo y siga publicado.", False),
    ("region", r"not available in your country|blocked it in your country|geo.?restrict",
     "Está bloqueado en tu región.", ARCHIVO, False),
    ("403", r"HTTP Error 403|Forbidden",
     "La plataforma rechazó la descarga (403).",
     "Suele pasar con yt-dlp viejo o una conexión marcada. Corre doctor.py --online; si está al día, espera y reintenta. " + ARCHIVO, False),
    ("no-soportado", r"Unsupported URL", "Ese enlace no es de un video o foto descargable.", "Copia el link directo del post o video.", False),
    ("js", r"JavaScript runtime|n challenge|Signature solving failed",
     "YouTube exige un runtime de JavaScript para resolver sus desafíos y no se encontró ninguno.",
     "Instala Node.js o deno (se busca en el PATH, en ~/nodejs y en Homebrew). doctor.py muestra qué falta.", False),
    ("ffmpeg", r"ffmpeg.*(not found|not installed)|ffprobe and ffmpeg not found", "Falta ffmpeg.",
     "Instala ffmpeg o `pip install imageio-ffmpeg` en el venv.", False),
    ("red", r"Temporary failure in name resolution|timed out|Connection reset|Network is unreachable|getaddrinfo failed|"
            r"Connection refused|Name or service not known|nodename nor servname|Remote end closed|IncompleteRead|URLError",
     "Sin conexión o conexión inestable.", "Revisa tu internet y reintenta.", True),
    ("5xx", r"HTTP Error 5\d\d", "El servidor de la plataforma falló (error 5xx).", "Reintenta en unos minutos.", True),
]

def explain(text, js_ok=True):
    """Traduce el texto de error de yt-dlp/gallery-dl a {code, causa, haz, retry}. Mira solo las líneas de error."""
    lines = [l for l in (text or "").splitlines() if re.search(r"error", l, re.I)] or (text or "").splitlines()
    blob = "\n".join(lines)
    if re.search(r"n challenge solving failed|challenge solver script|Remote component challenge", text or "", re.I) \
            and re.search(r"not available|Only images|Requested format", blob, re.I):
        return {"code": "js", "retry": False,
                "causa": "YouTube pidió resolver un desafío y no se pudo (falta el runtime de JavaScript o su solucionador oficial).",
                "haz": "Corre doctor.py. Con Node o deno instalados, yt-dlp baja el solucionador oficial (--remote-components ejs:github) la primera vez; "
                       "si no hay red a GitHub o bloqueaste la descarga, instala `yt-dlp-ejs` con pip. " + ARCHIVO}
    for code, pat, causa, haz, retry in ERRORES:
        if re.search(pat, blob, re.I): return {"code": code, "causa": causa, "haz": haz, "retry": retry}
    if re.search(r"Requested format is not available|Only images are available", blob, re.I):
        if not js_ok: return explain("JavaScript runtime", True)
        return {"code": "formato", "causa": "No hay un formato que cumpla lo pedido.",
                "haz": "Prueba otra calidad (--max-height 1080 o 480). " + ARCHIVO, "retry": False}
    last = (lines[-1] if lines else "sin detalle").strip()[:200]
    return {"code": "desconocido", "causa": "Fallo no reconocido: " + last,
            "haz": "Corre doctor.py para revisar las herramientas. " + ARCHIVO, "retry": False}

def with_retries(once, sleep=time.sleep, waits=(8, 25, 75), log=print):
    """once() -> (código, texto de error). Reintenta con espera solo lo que lo merece (429, red, 5xx)."""
    n = 0
    while True:
        code, text = once()
        if code == 0: return code, text
        info = explain(text)
        if not info["retry"] or n >= len(waits): return code, text
        log("Reintento %d/%d en %d s (%s)" % (n + 1, len(waits), waits[n], info["causa"]))
        sleep(waits[n]); n += 1

def run_capture(cmd):
    """Ejecuta mostrando la salida en vivo y devuelve (código, salida completa)."""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, errors="replace")
    out = []
    for line in p.stdout:
        sys.stdout.write(line); sys.stdout.flush(); out.append(line)
    p.wait(); return p.returncode, "".join(out)

LAST_FAIL = {}   # última causa explicada (código), para decidir si vale reintentar con sesión
PERMISOS = os.path.expanduser("~/.config/mukiwa/permisos.json")

def cookies_permitidas(url, path=None):
    """Navegador cuya sesión Bryan autorizó por escrito para este sitio, o None.
    Permiso explícito, acotado por sitio y revocable: borrar ~/.config/mukiwa/permisos.json lo quita."""
    try:
        with open(path or PERMISOS, encoding="utf-8") as f: cfg = json.load(f)["cookies_navegador"]
    except (OSError, ValueError, KeyError, TypeError): return None
    host = urllib.parse.urlparse(url).netloc.lower().split(":")[0]
    for s in cfg.get("sitios", []):
        if host == s or host.endswith("." + s): return cfg.get("navegador", "chrome")
    return None

ERR_LOG = []   # textos de los intentos fallidos de esta descarga, para explicar la causa al final

def run(cmd, retry=False):
    print("$", " ".join(cmd))
    code, text = with_retries(lambda: run_capture(cmd)) if retry else run_capture(cmd)
    if code: ERR_LOG.append(text)
    return code

def report_failure(texts, folder=None):
    info = explain("\n".join(texts), js_ok=bool(JS)); LAST_FAIL["code"] = info["code"]
    print("CAUSA[%s]: %s\nHAZ: %s" % (info["code"], info["causa"], info["haz"]))
    if folder:
        with open(os.path.join(folder, "error.json"), "w", encoding="utf-8") as f: json.dump(info, f, ensure_ascii=False)
    return info

def direct(url, outdir):
    name = os.path.basename(urllib.parse.urlparse(url).path) or "archivo"
    dst = os.path.join(outdir, name)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r, open(dst, "wb") as f: shutil.copyfileobj(r, f)
    return dst

def pick_track(info, lang="auto"):
    """Elige UNA pista de subtítulos desde info.json, sin pedir nada a YouTube.
    Orden: manuales antes que automáticos; idioma original del video (YouTube lo marca como
    'xx-orig' en los automáticos) antes que traducciones automáticas; si el idioma es
    desconocido, español y luego inglés. Devuelve {key, kind, provenance} o None.
    Adaptado de Watch (bradautomates/claude-video, download.py, MIT)."""
    manual = {k: v for k, v in (info.get("subtitles") or {}).items() if v and k != "live_chat"}
    auto = {k: v for k, v in (info.get("automatic_captions") or {}).items() if v and k != "live_chat"}
    origs = sorted(k for k in auto if k.endswith("-orig"))
    original = origs[0][:-5] if len(origs) == 1 else (info.get("language") or None)
    base = lambda k: k[:-5] if k.endswith("-orig") else k
    root = lambda k: base(k).split("-")[0]
    want = original if lang == "auto" else lang
    for kind, tracks in (("manual", manual), ("automatic", auto)):
        if want:
            hits = sorted((k for k in tracks if base(k) == want or root(k) == want.split("-")[0]),
                          key=lambda k: (not k.endswith("-orig"), k != want, k))
            if hits:
                prov = "original" if original and root(hits[0]) == original.split("-")[0] else "traducción pedida"
                return {"key": hits[0], "kind": kind, "provenance": prov}
    if lang != "auto": return None
    for kind, tracks in (("manual", manual), ("automatic", auto)):
        keys = sorted(tracks, key=lambda k: ({"es": 0, "en": 1}.get(root(k), 2), not k.endswith("-orig"), k))
        if keys:
            return {"key": keys[0], "kind": kind,
                    "provenance": "original" if keys[0].endswith("-orig") else "desconocida (puede ser traducción automática)"}
    return None

def fetch_subs(url, d, ck, lang="auto"):
    """Una sola petición de subtítulos (antes eran dos, es.* y en.*, y YouTube respondía 429).
    Deja video.<pista>.srt y subtitulos.json con la procedencia."""
    if glob.glob(os.path.join(d, "video.*.srt")): return             # ya están: no pedir de nuevo
    info_path = os.path.join(d, "video.info.json")
    if not os.path.exists(info_path):
        run(YT + ["-o", os.path.join(d, "video.%(ext)s"), "--skip-download", "--write-info-json", "--no-playlist"] + JS + ck + [url], retry=True)
    try:
        with open(info_path, encoding="utf-8") as f: track = pick_track(json.load(f), lang)
    except (OSError, ValueError):
        print("Sin info.json: no se pudieron elegir subtítulos."); return
    if not track:
        print("Este video no tiene subtítulos" + ("" if lang == "auto" else " en '%s'" % lang) + "."); return
    run(YT + ["-o", os.path.join(d, "video.%(ext)s"), "--load-info-json", info_path, "--skip-download", "--no-write-info-json",
              "--write-subs" if track["kind"] == "manual" else "--no-write-subs",
              "--write-auto-subs" if track["kind"] == "automatic" else "--no-write-auto-subs",
              "--sub-langs", "-all,^" + re.escape(track["key"]) + "$", "--convert-subs", "srt",
              "--ffmpeg-location", FF] + JS + ck, retry=True)
    with open(os.path.join(d, "subtitulos.json"), "w", encoding="utf-8") as f: json.dump(track, f, ensure_ascii=False)

def grab(url, a):
    u = urllib.parse.urlparse(url); host = u.netloc.lower(); path = u.path.lower()
    os.makedirs(a.out, exist_ok=True)
    ck = ["--cookies-from-browser", a.cookies] if a.cookies else []
    title = "descarga"; del ERR_LOG[:]
    if not path.endswith(IMG_EXT + AV_EXT):
        probe = YT + ["--ffmpeg-location", FF] + JS + ["--skip-download", "--playlist-items", "1",
                                 "--print", "%(title)s"] + ck + [url]
        box = {}
        def once():
            r = subprocess.run(probe, capture_output=True, text=True, errors="replace")
            box["out"] = r.stdout; return r.returncode, r.stderr
        code, err = with_retries(once)
        if box["out"].strip(): title = box["out"].strip().splitlines()[0]
        else:
            title = (host.split(".")[-2] if "." in host else host) + "-" + path.strip("/").replace("/", "-")
            if code and any(v in host for v in VIDEO_ONLY) and not a.photos_only:   # ni el título se pudo leer: bajar no servirá
                print("No se pudo leer el video: " + (err.strip().splitlines() or ["sin detalle"])[-1][:200])
                report_failure([err]); return None
    d = os.path.join(a.out, "%s-%s" % (datetime.date.today().isoformat(), slug(title)))
    os.makedirs(d, exist_ok=True)
    photo_first = False
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
            have = os.path.join(d, "audio.mp3") if a.audio_only else (video_en(d) or os.path.join(d, "video.mp4"))
            if a.subs_only:                                 # solo subtítulos + info: no bajar el video
                ok = os.path.exists(os.path.join(d, "video.info.json")) or run(YT + ["-o", os.path.join(d, "video.%(ext)s"),
                    "--skip-download", "--write-info-json", "--no-playlist"] + JS + ck + [url]) == 0
            elif os.path.exists(have): print("Ya descargado, se reutiliza:", have); ok = True
            else:
                ok = run(cmd + ["--newline", "--progress-delta", "5", "--ffmpeg-location", FF] + JS + ck + [url], retry=True) == 0
                if not a.audio_only and not video_en(d):   # fallo transitorio (visto con YouTube): un reintento
                    print("[grab] el video no quedó en disco; se reintenta una vez en 10 s", file=sys.stderr); time.sleep(10)
                    ok = run(cmd + ["--newline", "--progress-delta", "5", "--ffmpeg-location", FF] + JS + ck + [url], retry=True) == 0
            if not a.no_subs: fetch_subs(url, d, ck, a.sub_lang)   # NO fatal: un video sin subtítulos sigue siendo útil
            if ok and not a.audio_only and video_en(d) and not os.path.exists(os.path.join(d, "audio.mp3")):
                run([FF, "-y", "-loglevel", "error", "-i", video_en(d), "-vn", "-q:a", "2",
                     os.path.join(d, "audio.mp3")])
        if (not ok or photo_first or a.photos_only):
            if any(v in host for v in VIDEO_ONLY) and not a.photos_only: print("yt-dlp falló en un sitio de video; revisa el error de arriba.")
            elif GDL: run(GDL + ["-d", os.path.join(d, "fotos"), "-o", "directory=[]"] + ck + [url])
            else: print("yt-dlp no pudo y gallery-dl no está disponible (corre setup.sh).")
    files = sorted(os.path.relpath(os.path.join(r, f), d) for r, _, fs in os.walk(d) for f in fs if f != "LEEME.md" and not f.startswith("._"))  # ._x = metadatos macOS en exFAT
    with open(os.path.join(d, "LEEME.md"), "w") as f:
        f.write("# %s\n\n- Fuente: %s\n- Fecha: %s\n- Archivos:\n%s\n" % (
            title, url, datetime.date.today().isoformat(), "\n".join("  - " + x for x in files)))
    video_esperado = not (a.subs_only or a.audio_only or a.photos_only or photo_first or path.endswith(IMG_EXT + AV_EXT))
    got = descarga_ok(files, a.subs_only, video_esperado)
    print(("\nOK -> %s" if got else "\nFALLO (no se bajó nada) -> %s") % d); [print("  " + x) for x in files]
    if not got:
        if a.subs_only and os.path.exists(os.path.join(d, "video.info.json")) and not ERR_LOG:   # el video existe, solo que sin subtítulos
            print("CAUSA[sin-subtitulos]: El video no tiene subtítulos.\nHAZ: Se transcribe el audio en la Mac con faster-whisper.")
        else: report_failure(ERR_LOG or ["sin detalle"], d)
    if not files and "instagram" in host:
        print("\nPISTA Instagram: necesita sesión. Si viste 'Operation not permitted' o 'could not find chrome cookies':\n  Ajustes del Sistema > Privacidad y seguridad > Acceso total al disco > activa Terminal, cierra Terminal (Cmd+Q) y reábrela.")
    if a.frames and video_en(d):
        ef = os.path.abspath(os.path.join(HERE, "extract_frames.py"))
        if os.path.exists(ef): run([sys.executable, ef, video_en(d), "--out", os.path.join(d, "frames_work")])
    return d if got else None

VIDEO_EXT = (".mp4", ".mov", ".m4v", ".webm", ".mkv")


def video_en(d):
    """Ruta del video real en la carpeta (cualquier extensión de video), o None. Una imagen (miniatura) NUNCA cuenta."""
    try: names = sorted(os.listdir(d))
    except OSError: return None
    mp4 = [n for n in names if n.lower() == "video.mp4"]
    otros = [n for n in names if n.lower().startswith("video.") and n.lower().endswith(VIDEO_EXT) and not n.startswith("._")]
    pick = (mp4 or otros or [None])[0]
    return os.path.join(d, pick) if pick else None


def descarga_ok(files, subs_only, video_esperado):
    """¿Se bajó lo que se pidió? La miniatura o los subtítulos solos NO cuentan como éxito si se pidió el video
    (antes una descarga que solo trajo la miniatura se daba por buena y el análisis seguía sin imagen)."""
    fl = [x.lower() for x in files]
    got = any(x.endswith(IMG_EXT + AV_EXT + ((".srt",) if subs_only else ())) for x in fl)
    if video_esperado and not subs_only:
        tiene_video = any(x.endswith(VIDEO_EXT) and "/" not in x for x in fl)
        tiene_fotos = any(x.startswith("fotos/") and x.endswith(IMG_EXT) for x in fl)
        return got and (tiene_video or tiene_fotos)
    return got


def grab_con_permiso(url, a, grab_fn=None, perms_path=None):
    """Descarga; si falla por pedir sesión y Bryan autorizó la de su navegador para ESE sitio, reintenta una vez con ella."""
    grab_fn = grab_fn or grab
    LAST_FAIL.clear()
    res = grab_fn(url, a)
    if res or a.cookies or LAST_FAIL.get("code") != "login": return res
    browser = cookies_permitidas(url, perms_path)
    if not browser: return res
    print("SESION[%s]: el link pide sesión; se usa tu sesión de %s (permiso tuyo para %s)." % (browser, browser, urllib.parse.urlparse(url).netloc))
    a.cookies = browser
    try: return grab_fn(url, a)
    finally: a.cookies = None

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*"); ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--cookies", default=None, help="chrome|safari|firefox|edge para links privados/login")
    ap.add_argument("--audio-only", action="store_true"); ap.add_argument("--photos-only", action="store_true")
    ap.add_argument("--max-height", type=int, default=1080); ap.add_argument("--no-subs", action="store_true")
    ap.add_argument("--frames", action="store_true")
    ap.add_argument("--subs-only", action="store_true", help="solo subtítulos + info, sin bajar el video (nivel transcript)")
    ap.add_argument("--sub-lang", default="auto", help="auto = idioma original del video; o un código: es, en, pt...")
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
    results = [grab_con_permiso(url, a) for url in urls]
    sys.exit(0 if all(results) else 1)
