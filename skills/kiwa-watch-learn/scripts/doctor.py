#!/usr/bin/env python3
"""Revisa si todo lo necesario para ver, descargar y analizar videos está listo, y dice qué hacer si no.

  python3 doctor.py [--online] [--downloads DIR]

--online compara yt-dlp con la última versión publicada en GitHub (una petición de solo lectura).
Código de salida: 0 todo bien (puede haber avisos), 1 si falta algo imprescindible.
Importante: correrlo con el Python del venv (~/.venvs/watch-skill/bin/python) para que vea Pillow y whisper."""
import argparse, datetime, glob, importlib.util, json, os, re, shutil, subprocess, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import grab  # noqa: E402

OK, AVISO, FALTA = "ok", "aviso", "falta"
ICON = {OK: "✅", AVISO: "⚠️ ", FALTA: "❌"}


def version_age_days(version, today=None):
    """'2026.08.19' -> días desde esa fecha; None si no tiene ese formato."""
    m = re.match(r"^(\d{4})\.(\d{2})\.(\d{2})", version or "")
    if not m: return None
    today = today or datetime.date.today()
    return (today - datetime.date(*map(int, m.groups()))).days


def upgrade_hint(path):
    """Cómo se actualiza yt-dlp según dónde esté instalado."""
    p = path or ""
    if "/uv/tools/" in p: return "uv tool upgrade yt-dlp"
    if p.startswith(grab.BIN_DIR): return 'bash "%s/setup.sh"' % HERE
    return "python3 -m pip install -U yt-dlp"


def latest_ytdlp(fetch=None):
    fetch = fetch or (lambda u: urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "mukiwa-doctor"}), timeout=15).read())
    return json.loads(fetch("https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"))["tag_name"]


def check(online=False, downloads=None):
    rows = []
    add = lambda state, name, detail, fix="": rows.append((state, name, detail, fix))

    py = sys.version_info
    add(OK if py >= (3, 9) else FALTA, "Python", "%d.%d.%d · %s" % (py[0], py[1], py[2], sys.executable), "" if py >= (3, 9) else "Instala Python 3.9 o superior.")

    yt = grab.find_cmd("yt-dlp", "yt_dlp")
    if not yt:
        add(FALTA, "yt-dlp", "no encontrado", 'bash "%s/setup.sh"' % HERE)
    else:
        v = subprocess.run(yt + ["--version"], capture_output=True, text=True).stdout.strip()
        age = version_age_days(v)
        detail = "%s · %s%s" % (v, yt[0], (" · de hace %d días" % age) if age is not None else "")
        if online:
            try:
                last = latest_ytdlp()
                if last == v: add(OK, "yt-dlp", detail + " · es la última versión")
                else: add(AVISO, "yt-dlp", detail + " · hay una más nueva (%s)" % last, upgrade_hint(yt[0]))
            except Exception as e:
                add(AVISO, "yt-dlp", detail + " · no se pudo comparar con GitHub (%s)" % type(e).__name__)
        else:
            add(AVISO if age is not None and age > 120 else OK, "yt-dlp", detail,
                upgrade_hint(yt[0]) if age is not None and age > 120 else "")

    rt = grab.find_js_runtime()
    add(OK if rt else FALTA, "Runtime de JavaScript (YouTube)", ("%s · %s" % rt) if rt else "ninguno (YouTube fallará)",
        "" if rt else "Instala Node.js (nodejs.org) o deno; se detecta solo en el PATH, ~/nodejs y Homebrew.")

    solver_cache = glob.glob(os.path.expanduser("~/.cache/yt-dlp/challenge-solver*"))
    solver = bool(solver_cache) or importlib.util.find_spec("yt_dlp_ejs") is not None
    add(OK if solver else AVISO, "Solucionador de desafíos de YouTube (EJS)",
        "listo" if solver else "aún no descargado: yt-dlp lo baja solo la primera vez que YouTube lo pida",
        "" if solver else "Si tu red bloquea GitHub: pip install yt-dlp-ejs (en el venv).")

    ff = grab.find_ffmpeg()
    add(OK if ff else FALTA, "ffmpeg", ff or "no encontrado", "" if ff else "pip install imageio-ffmpeg (en el venv) o instala ffmpeg.")

    gdl = grab.find_cmd("gallery-dl", "gallery_dl")
    add(OK if gdl else AVISO, "gallery-dl", gdl[0] if gdl else "no encontrado (solo afecta a fotos y carruseles)",
        "" if gdl else "pip install gallery-dl (en el venv).")

    pil = importlib.util.find_spec("PIL") is not None
    add(OK if pil else FALTA, "Pillow (capturas)", "disponible" if pil else "no disponible en este Python",
        "" if pil else "Corre este chequeo con ~/.venvs/watch-skill/bin/python o: pip install Pillow")

    fw = importlib.util.find_spec("faster_whisper") is not None
    add(OK if fw else AVISO, "faster-whisper (voz a texto)", "disponible" if fw else "no disponible en este Python",
        "" if fw else "Sin él, los videos sin subtítulos quedan solo-visual. pip install faster-whisper (en el venv).")

    target = downloads or grab.DEFAULT_OUT
    probe = target if os.path.exists(target) else os.path.dirname(target)
    try:
        free = shutil.disk_usage(probe).free / 1e9
        add(OK if free >= 10 else AVISO, "Espacio libre en descargas", "%.0f GB · %s" % (free, target),
            "" if free >= 10 else "Menos de 10 GB: libera espacio antes de bajar videos largos.")
    except OSError:
        add(AVISO, "Espacio libre en descargas", "no se pudo leer " + probe)

    inbox = os.environ.get("MUKIWA_INBOX") or next(iter(glob.glob(os.path.expanduser("~/Library/CloudStorage/GoogleDrive-*/Mi unidad/MUKIWA · Aprender"))), "")
    add(OK if inbox and os.path.isdir(inbox) else AVISO, "Buzón de links", inbox if inbox and os.path.isdir(inbox) else "no creado todavía",
        "" if inbox and os.path.isdir(inbox) else "python3 skills/kiwa-watch-learn/scripts/inbox.py init")
    return rows


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--online", action="store_true"); ap.add_argument("--downloads")
    a = ap.parse_args()
    rows = check(a.online, a.downloads)
    for state, name, detail, fix in rows:
        print("%s %s — %s" % (ICON[state], name, detail))
        if fix: print("     → " + fix)
    missing = [r for r in rows if r[0] == FALTA]
    print("\n" + ("Falta algo imprescindible: arregla lo marcado con ❌." if missing else "Todo listo para ver, descargar y analizar."))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
