#!/usr/bin/env python3
"""Motor opcional Gemini: Google ve el video completo (imagen + audio) y responde.

Solo se usa con `watch.py --engine gemini`. Los links de YouTube se mandan a Google tal cual;
los archivos locales se suben a la Files API de Google y se borran después de la respuesta
(si no se pueden borrar, Google los elimina solo en 48 h).

La clave GEMINI_API_KEY se lee del entorno o de ~/.config/mukiwa/.env (permisos 0600).
Se manda solo en la cabecera x-goog-api-key y se tacha de cualquier mensaje de error.
Clave gratis: https://aistudio.google.com/apikey

Adaptado de Watch (https://github.com/bradautomates/claude-video, gemini.py),
Copyright (c) 2026 Bradley Bonanno, licencia MIT. Cambios: Python 3.9, mensajes en español,
configuración MUKIWA. Solo biblioteca estándar."""
from __future__ import annotations

import json, math, mimetypes, os, re, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = "https://generativelanguage.googleapis.com"
INTERACTIONS = f"{API}/v1beta/interactions"
DEFAULT_MODEL = "gemini-3.7-flash"
CONFIG = Path.home() / ".config" / "mukiwa" / ".env"
YOUTUBE = re.compile(r"^https?://(?:(?:www\.|m\.|music\.)?youtube\.com/(?:watch\?\S*\bv=|shorts/|live/)|youtu\.be/)\S+$", re.I)
HINTS = {
    "auth": "revisa GEMINI_API_KEY (se crea gratis en https://aistudio.google.com/apikey)",
    "quota": "la clave llegó a su límite de uso; espera o revisa su plan",
    "rejected": "Gemini rechazó el pedido; el video puede ser privado, no compatible o muy largo",
    "service": "error del servidor de Gemini; reintenta en un rato",
    "network": "no se pudo conectar con generativelanguage.googleapis.com; revisa la red",
    "response": "Gemini devolvió algo que esta versión no sabe leer",
    "upload": "el video no se pudo subir o procesar en la Files API de Gemini",
}
DEFAULT_QUESTION = ("Resume a fondo este video en orden cronológico: qué se muestra, el texto o código que "
                    "aparece en pantalla y qué se dice.")
PROMPT_SUFFIX = ("\n\nCita un tiempo MM:SS (o H:MM:SS) en cada afirmación sobre un momento concreto. "
                 "Separa lo que se ve de lo que se escucha cuando importe. Si el video no muestra o no dice "
                 "algo necesario para responder, dilo claramente en vez de adivinar. Responde en español.")


def config_value(name, default=None, path=CONFIG):
    """Entorno -> ~/.config/mukiwa/.env -> default. Nunca imprime el valor."""
    if os.environ.get(name): return os.environ[name].strip()
    try:
        for line in Path(path).read_text(encoding="utf-8-sig").splitlines():
            k, sep, v = line.partition("=")
            if sep and k.strip() == name and v.strip() and not line.lstrip().startswith("#"):
                return v.strip().strip('"').strip("'")
    except OSError:
        pass
    return default


def ensure_config(path=CONFIG):
    """Crea el archivo de configuración privado con la línea vacía para la clave."""
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Configuración MUKIWA (privada, no subir a Git)\nGEMINI_API_KEY=\n", encoding="utf-8")
    os.chmod(path, 0o600)
    return path


def is_youtube(source):
    return bool(YOUTUBE.match(source or ""))


def build_prompt(question):
    return ((question or "").strip() or DEFAULT_QUESTION) + PROMPT_SUFFIX


def fail(category, detail, key):
    detail = (detail or "ninguno")[:600]
    if key: detail = detail.replace(key, "[clave oculta]")
    return SystemExit(f"Gemini {category}: {HINTS[category]}. Detalle: {detail}. "
                      "No se intentó el modo local; vuelve a correr con --engine local para capturas + transcripción.")


def error_message(body):
    text = body.decode("utf-8", errors="replace")
    try:
        data = json.loads(text)
        if isinstance(data, list) and data: data = data[0]
        return str(data["error"]["message"])
    except (ValueError, KeyError, TypeError):
        return text


def call(method, url, key, data=None, headers=None, timeout=60.0, opener=urlopen):
    request = Request(url, data=data, method=method, headers={"x-goog-api-key": key, **(headers or {})})
    try:
        with opener(request, timeout=timeout) as response:
            return response.status, dict(response.headers), response.read()
    except HTTPError as exc:
        message = error_message(exc.read())
        category = ("auth" if exc.code in (401, 403) or "api key" in message.lower() else "quota" if exc.code == 429
                    else "service" if exc.code >= 500 else "rejected")
        raise fail(category, f"HTTP {exc.code}: {message}", key) from None
    except (URLError, TimeoutError, OSError) as exc:
        raise fail("network", f"{type(exc).__name__}: {getattr(exc, 'reason', exc)}", key) from None


def processing(clip):
    """Sin rango: modo 'agentic' (Gemini decide cómo mirar). Con --start/--end: recorte estático."""
    if not clip or (clip[0] is None and clip[1] is None):
        return "agentic", "agentic"
    start, end = clip
    config = {"type": "static"}
    if start is not None: config["start_offset"] = f"{int(math.floor(start))}s"
    if end is not None: config["end_offset"] = f"{int(math.ceil(end))}s"
    return config, f"recorte {int(start or 0)}s–{int(math.ceil(end)) if end is not None else 'final'}"


def ask(video, question, model, key, clip=None, timeout=600.0, opener=urlopen):
    proc, label = processing(clip)
    payload = {"model": model, "input": [{"type": "video", **video, "processing": proc},
                                         {"type": "text", "text": build_prompt(question)}]}
    _, _, body = call("POST", INTERACTIONS, key, data=json.dumps(payload).encode("utf-8"),
                      headers={"Content-Type": "application/json"}, timeout=timeout, opener=opener)
    try:
        data = json.loads(body)
        parts = [p["text"] for step in data["steps"] if step.get("type") == "model_output"
                 for p in step.get("content", []) if p.get("type") == "text" and p.get("text")]
        tokens = (data.get("usage") or {}).get("total_tokens")
    except (ValueError, KeyError, TypeError, AttributeError):
        raise fail("response", body[:300].decode("utf-8", errors="replace"), key) from None
    if not parts:
        raise fail("response", f"sin texto de respuesta (estado {data.get('status')})", key)
    return {"text": "\n".join(parts).strip(), "model": model, "processing": label,
            "total_tokens": tokens if isinstance(tokens, int) else None}


def upload_file(path, key, poll_seconds=2.0, max_wait=900.0, sleep=time.sleep, opener=urlopen):
    path = Path(path); size = path.stat().st_size
    if size == 0: raise fail("upload", f"{path.name} está vacío", key)
    guessed = mimetypes.guess_type(path.name)[0] or ""
    mime = guessed if guessed.startswith("video/") else "video/mp4"
    _, headers, _ = call("POST", f"{API}/upload/v1beta/files", key,
                         data=json.dumps({"file": {"display_name": "mukiwa-watch"}}).encode("utf-8"),
                         headers={"X-Goog-Upload-Protocol": "resumable", "X-Goog-Upload-Command": "start",
                                  "X-Goog-Upload-Header-Content-Length": str(size),
                                  "X-Goog-Upload-Header-Content-Type": mime, "Content-Type": "application/json"},
                         opener=opener)
    session = {k.lower(): v for k, v in headers.items()}.get("x-goog-upload-url")
    if not session: raise fail("upload", "la Files API no devolvió URL de subida", key)
    with path.open("rb") as stream:   # por bloques, sin cargar el video en memoria
        _, _, body = call("POST", session, key, data=stream,
                          headers={"Content-Length": str(size), "X-Goog-Upload-Offset": "0",
                                   "X-Goog-Upload-Command": "upload, finalize"}, timeout=3600.0, opener=opener)
    try:
        info = json.loads(body)["file"]; waited = 0.0
        while info.get("state") == "PROCESSING":
            if waited >= max_wait:
                delete_file(info["name"], key, opener=opener)
                raise fail("upload", f"sigue procesando tras {int(max_wait)} s", key)
            sleep(poll_seconds); waited += poll_seconds
            info = json.loads(call("GET", f"{API}/v1beta/{info['name']}", key, opener=opener)[2])
        if info.get("state") != "ACTIVE":
            delete_file(info["name"], key, opener=opener)
            raise fail("upload", f"estado del archivo {info.get('state')}", key)
        return {"name": info["name"], "uri": info["uri"], "mime_type": info.get("mimeType") or mime}
    except (ValueError, KeyError, TypeError):
        raise fail("upload", "respuesta ilegible de la Files API", key) from None


def delete_file(name, key, opener=urlopen):
    try:
        call("DELETE", f"{API}/v1beta/{name}", key, opener=opener); return None
    except (SystemExit, Exception) as exc:   # limpiar nunca debe tapar el resultado real
        return f"No se pudo borrar {name} de Google ({str(exc).split('. Detalle:')[0]}); expira solo en 48 h."
