#!/usr/bin/env python3
"""Buzón de links de MUKIWA. Mandas un link desde el iPhone (o lo pegas en un archivo) y la Mac lo
descarga, lo prepara y deja la evidencia lista para que Claude lo analice y alimente a los profesores.

Carpeta del buzón (por defecto en Google Drive: «Mi unidad/MUKIWA · Aprender»; cambia con MUKIWA_INBOX o --dir):
  links-pendientes.md   un link por línea, solo se AÑADE (no se borra nada: el estado va aparte)
  Para analizar/        videos o audios guardados desde el celular: plan B cuando un link no se deja bajar
  estado.md             informe legible de qué se hizo con cada cosa (lo escribe este script)
  _estado.json          la cuenta interna

  inbox.py init                     crea la carpeta y los archivos
  inbox.py run [--limit 5]          escanea, descarga y prepara lo pendiente; lista lo que Claude debe analizar
  inbox.py ready [--json]           lo que ya está preparado y espera análisis
  inbox.py done --url U [--profes diseno-grafico,motion-graphics] [--leccion ruta]   marca como aprendido
  inbox.py requeue --url U          vuelve a ponerlo en pendiente
  inbox.py status                   reescribe estado.md y muestra el resumen

No usa cookies por su cuenta: solo grab.py puede usar la sesión del navegador, y únicamente para los sitios que
Bryan autorizó en ~/.config/mukiwa/permisos.json (hoy: instagram.com), cuando el link falla por pedir sesión. Si no hay
permiso o falla, queda como fallo con la causa y lo que hacer (plan B: guardar el video en «Para analizar»). El análisis visual y la lección los hace Claude, no este script."""
import argparse, datetime, fcntl, glob, json, os, re, subprocess, sys, tempfile, urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
WORK = (REPO if (REPO / "CLAUDE.md").exists() else Path.cwd()) / "work"
WATCH = HERE / "watch.py"
VENV_PY = Path.home() / ".venvs" / "watch-skill" / "bin" / "python"
FOLDER, LINKS, VIDEOS, ESTADO_MD, STATE = "MUKIWA · Aprender", "links-pendientes.md", "Para analizar", "estado.md", "_estado.json"
MEDIA_EXT = (".mp4", ".mov", ".m4v", ".mkv", ".webm", ".mp3", ".m4a", ".wav", ".aac")
RETRY_CODES = {"429", "red", "5xx", "403"}      # fallos que pueden arreglarse solos con el tiempo
MAX_TRIES = 3
TRACK = {"si", "igsh", "igshid", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "feature",
         "ref", "pp", "gclid", "mc_cid", "mc_eid", "_r", "_t", "is_from_webapp", "sender_device", "share_app_id",
         "share_link_id", "share_item_id", "web_id"}
URL_RE = re.compile(r"https?://[^\s<>\[\]\"']+")


def now():
    return datetime.datetime.now().replace(microsecond=0).isoformat(sep=" ")


def default_dir():
    if os.environ.get("MUKIWA_INBOX"): return Path(os.environ["MUKIWA_INBOX"]).expanduser()
    roots = glob.glob(str(Path.home() / "Library/CloudStorage/GoogleDrive-*"))
    for r in roots:
        for mine in ("Mi unidad", "My Drive"):
            if (Path(r) / mine).is_dir(): return Path(r) / mine / FOLDER
    return Path.home() / FOLDER


def extract_urls(text):
    seen, out = set(), []
    for m in URL_RE.findall(text or ""):
        u = m.rstrip(".,;:!?)»”")
        if u not in seen: seen.add(u); out.append(u)
    return out


def normalize(url):
    """-> (clave para no repetir, link limpio sin rastreadores). El mismo video compartido de dos formas = una clave."""
    u = urllib.parse.urlparse(url.strip())
    host = re.sub(r"^www\.", "", u.netloc.lower())
    path = u.path.rstrip("/")
    q = urllib.parse.parse_qs(u.query)
    if host in ("youtu.be",) or host.endswith("youtube.com"):
        vid = None
        if host == "youtu.be": vid = path.lstrip("/").split("/")[0]
        elif "v" in q: vid = q["v"][0]
        else:
            m = re.match(r"^/(shorts|live|embed)/([\w-]+)", path)
            vid = m.group(2) if m else None
        if vid:
            kind = "shorts" if path.startswith("/shorts/") else "watch"
            return "youtube:" + vid, ("https://www.youtube.com/shorts/%s" % vid) if kind == "shorts" else ("https://www.youtube.com/watch?v=%s" % vid)
    if host.endswith("instagram.com"):
        m = re.match(r"^/(?:[\w.]+/)?(reels?|p|tv)/([\w-]+)", path)
        if m: return "instagram:" + m.group(2), "https://www.instagram.com/%s/%s/" % ("reel" if m.group(1).startswith("reel") else m.group(1), m.group(2))
    if host.endswith("tiktok.com"):
        m = re.search(r"/video/(\d+)", path)
        if m: return "tiktok:" + m.group(1), "https://www.tiktok.com%s" % path
    keep = sorted((k, v) for k, vs in q.items() if k not in TRACK and not k.startswith("utm_") for v in vs)
    query = urllib.parse.urlencode(keep)
    clean = urllib.parse.urlunparse((u.scheme or "https", u.netloc, u.path, "", query, ""))
    return "%s%s%s" % (host, path, ("?" + query) if query else ""), clean


# ---------- estado ----------
def load_state(inbox):
    p = Path(inbox) / STATE
    try: return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError): return {"items": {}}


def save_state(inbox, state):
    p = Path(inbox) / STATE
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), prefix=".estado-", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f: json.dump(state, f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)


def init(inbox):
    inbox = Path(inbox); (inbox / VIDEOS).mkdir(parents=True, exist_ok=True)
    links = inbox / LINKS
    if not links.exists():
        links.write_text("# Links pendientes\n\nUn link por línea (o usa el atajo del iPhone «Aprender con MUKIWA»). "
                         "Solo añade líneas: el estado de cada uno está en estado.md.\n\n", encoding="utf-8")
    readme = inbox / "LEEME.md"
    if not readme.exists():
        readme.write_text("# Buzón de aprendizaje · MUKIWA\n\n"
                          "- **links-pendientes.md**: añade un link por línea (YouTube, Instagram, TikTok, Loom…). Cada noche la Mac los descarga, "
                          "los analiza y alimenta a los profesores.\n"
                          "- **Para analizar/**: si un link no se deja bajar, guarda aquí el video desde el celular (Archivos → esta carpeta).\n"
                          "- **estado.md**: qué pasó con cada cosa y qué hacer si algo falló.\n\n"
                          "No borres líneas de links-pendientes.md ni archivos de aquí: la Mac lleva la cuenta sola.\n", encoding="utf-8")
    if not (inbox / STATE).exists(): save_state(inbox, {"items": {}})
    return inbox


def scan(inbox, state, min_age=60, clock=None):
    """Añade como pendientes los links nuevos y los videos nuevos de «Para analizar». Devuelve las claves nuevas."""
    inbox = Path(inbox); items = state["items"]; new = []
    links = inbox / LINKS
    if links.exists():
        for url in extract_urls(links.read_text(encoding="utf-8", errors="replace")):
            key, clean = normalize(url)
            if key not in items:
                items[key] = {"url": clean, "origen": "link", "estado": "pendiente", "desde": now(), "intentos": 0}; new.append(key)
    vdir = inbox / VIDEOS
    t = clock if clock is not None else datetime.datetime.now().timestamp()
    for f in sorted(vdir.glob("*")) if vdir.is_dir() else []:
        if f.name.startswith(".") or f.suffix.lower() not in MEDIA_EXT or not f.is_file(): continue
        st = f.stat()
        if st.st_size == 0 or t - st.st_mtime < min_age: continue          # todavía sincronizando
        key = "archivo:%s:%d" % (f.name, st.st_size)
        if key not in items:
            items[key] = {"url": str(f), "origen": "archivo", "estado": "pendiente", "desde": now(), "intentos": 0}; new.append(key)
    return new


def default_runner(source):
    py = str(VENV_PY) if VENV_PY.exists() else sys.executable
    r = subprocess.run([py, str(WATCH), source, "--detail", "balanced"], capture_output=True, text=True, errors="replace", timeout=2400)
    return {"code": r.returncode, "text": r.stdout + "\n" + r.stderr}


def apply_result(item, res):
    text = res.get("text", ""); item["intentos"] = item.get("intentos", 0) + 1; item["actualizado"] = now()
    if re.search(r"^SESION\[", text, re.M): item["sesion"] = True      # grab.py usó la sesión autorizada del navegador
    m = re.search(r"^INFORME: (.+)$", text, re.M)
    if m and res["code"] in (0, 2):
        item.update(estado="listo" if res["code"] == 0 else "parcial", informe=m.group(1).strip(), carpeta=str(Path(m.group(1).strip()).parent))
        item.pop("causa", None); item.pop("haz", None); item.pop("codigo", None)
        return
    c = re.search(r"^CAUSA\[([^\]]+)\]: (.*)$", text, re.M); h = re.search(r"^HAZ: (.*)$", text, re.M)
    if c: item.update(estado="fallo", codigo=c.group(1), causa=c.group(2), haz=h.group(1) if h else "")
    else:
        tail = [l for l in text.strip().splitlines() if l.strip()][-1:] or ["sin detalle"]
        item.update(estado="fallo", codigo="desconocido", causa="Fallo no reconocido: " + tail[0][:200],
                    haz="Corre doctor.py; si sigue, guarda el video en «Para analizar».")


def eligible(item):
    if item["estado"] == "pendiente": return True
    return item["estado"] == "fallo" and item.get("codigo") in RETRY_CODES and item.get("intentos", 0) < MAX_TRIES


def prepare(state, limit=5, runner=default_runner, log=print):
    todo = [(k, v) for k, v in sorted(state["items"].items(), key=lambda kv: kv[1].get("desde", "")) if eligible(v)][:limit]
    for key, item in todo:
        log("→ %s" % item["url"])
        try: res = runner(item["url"])
        except subprocess.TimeoutExpired: res = {"code": 1, "text": "CAUSA[timeout]: Tardó demasiado (más de 40 min).\nHAZ: Prueba con un video más corto o guárdalo en «Para analizar»."}
        apply_result(item, res)
        log("   %s%s" % (item["estado"], (" — " + item["causa"]) if item["estado"] == "fallo" else ""))
    return [k for k, _ in todo]


def find_key(state, ident):
    if ident in state["items"]: return ident
    key = normalize(ident)[0] if re.match(r"https?://", ident) else ident
    if key in state["items"]: return key
    for k, v in state["items"].items():
        if v["url"] == ident: return k
    return None


def mark_done(state, ident, profes=None, leccion=None):
    key = find_key(state, ident)
    if not key: return None
    it = state["items"][key]; it.update(estado="aprendido", actualizado=now())
    if profes: it["profes"] = list(profes)
    if leccion: it["leccion"] = leccion
    return key


def requeue(state, ident):
    key = find_key(state, ident)
    if key: state["items"][key].update(estado="pendiente", intentos=0); [state["items"][key].pop(x, None) for x in ("causa", "haz", "codigo")]
    return key


def estado_md(state):
    esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
    order = {"listo": 0, "parcial": 0, "pendiente": 1, "fallo": 2, "aprendido": 3}
    rows = sorted(state["items"].values(), key=lambda v: (order.get(v["estado"], 9), v.get("actualizado", v.get("desde", ""))), reverse=False)
    counts = {}
    for v in rows: counts[v["estado"]] = counts.get(v["estado"], 0) + 1
    L = ["# Estado del buzón", "", "Actualizado: %s" % now(), "",
         " · ".join("%s: %d" % (k, counts[k]) for k in ("listo", "parcial", "pendiente", "fallo", "aprendido") if k in counts) or "(vacío)", "",
         "| Estado | Link o archivo | Detalle |", "|---|---|---|"]
    for v in rows:
        if v["estado"] == "fallo": det = "%s. Qué hacer: %s" % (v.get("causa", "").rstrip("."), v.get("haz", ""))
        elif v["estado"] == "aprendido": det = "Profesores: %s" % (", ".join(v.get("profes", [])) or "—")
        elif v["estado"] in ("listo", "parcial"): det = "Preparado; falta que Claude lo analice" + (" (se usó tu sesión de Chrome)" if v.get("sesion") else "")
        else: det = "En espera"
        L.append("| %s | %s | %s |" % (v["estado"], esc(v["url"]), esc(det)))
    return "\n".join(L) + "\n"


def write_estado(inbox, state):
    (Path(inbox) / ESTADO_MD).write_text(estado_md(state), encoding="utf-8")


def ready_items(state):
    return [(k, v) for k, v in state["items"].items() if v["estado"] in ("listo", "parcial")]


def summary(state):
    lines = []
    ready = ready_items(state)
    lines.append("LISTOS PARA ANALIZAR (%d):" % len(ready))
    lines += ["  - %s [%s]\n    informe: %s" % (v["url"], v["estado"], v.get("informe", "")) for _, v in ready] or ["  (ninguno)"]
    fails = [v for v in state["items"].values() if v["estado"] == "fallo"]
    lines.append("CON PROBLEMAS (%d):" % len(fails))
    lines += ["  - %s\n    %s\n    Qué hacer: %s" % (v["url"], v.get("causa", ""), v.get("haz", "")) for v in fails] or ["  (ninguno)"]
    return "\n".join(lines)


class Lock:
    def __init__(self): WORK.mkdir(parents=True, exist_ok=True); self.f = open(WORK / "inbox.lock", "w")
    def __enter__(self):
        try: fcntl.flock(self.f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError: sys.exit("Ya hay otra ejecución del buzón en curso; intenta más tarde.")
        return self
    def __exit__(self, *a): self.f.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0]); ap.add_argument("--dir")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init"); sub.add_parser("status")
    r = sub.add_parser("run"); r.add_argument("--limit", type=int, default=5)
    y = sub.add_parser("ready"); y.add_argument("--json", action="store_true")
    d = sub.add_parser("done"); d.add_argument("--url", required=True); d.add_argument("--profes", default=""); d.add_argument("--leccion")
    q = sub.add_parser("requeue"); q.add_argument("--url", required=True)
    a = ap.parse_args()
    inbox = Path(a.dir).expanduser() if a.dir else default_dir()
    if a.cmd == "init":
        print("Buzón listo en:", init(inbox)); return 0
    if not inbox.is_dir():
        sys.exit("No existe el buzón (%s). Créalo con: inbox.py init" % inbox)
    if a.cmd == "run":
        with Lock():
            init(inbox); state = load_state(inbox)
            new = scan(inbox, state); save_state(inbox, state)
            print("Buzón: %s\nNuevos: %d" % (inbox, len(new)))
            done = prepare(state, a.limit); save_state(inbox, state)
            write_estado(inbox, state); print("Preparados en esta vuelta: %d\n" % len(done)); print(summary(state))
        return 0
    state = load_state(inbox)
    if a.cmd == "ready":
        ready = ready_items(state)
        print(json.dumps([dict(v, clave=k) for k, v in ready], ensure_ascii=False, indent=1) if a.json else summary(state)); return 0
    if a.cmd == "done":
        k = mark_done(state, a.url, [p for p in a.profes.split(",") if p], a.leccion)
        if not k: sys.exit("No encuentro ese link en el buzón: " + a.url)
    elif a.cmd == "requeue":
        if not requeue(state, a.url): sys.exit("No encuentro ese link en el buzón: " + a.url)
    if a.cmd in ("done", "requeue"): save_state(inbox, state)
    write_estado(inbox, state); print(summary(state)); return 0


if __name__ == "__main__":
    sys.exit(main())
