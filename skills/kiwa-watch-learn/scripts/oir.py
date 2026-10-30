#!/usr/bin/env python3
"""OÍDOS en un solo comando: escalera de texto con tiempos para un link o un archivo, y un
informe honesto (oidos.json) de qué se verificó y qué no (Regla #2 de la skill).

Uso:
  python oir.py FUENTE --out DIR [--lang es] [--model small] [--budget 150] [--whisper | --no-whisper]
FUENTE = link (YouTube, etc.) | video/audio local | transcript (.srt .vtt .json3 .json .txt .md)

Escalera (se detiene en el primer peldaño que da texto, salvo --whisper):
  1  transcript que ya existe (FUENTE es texto, o --transcript ARCHIVO)
  2  subtítulos del link con yt-dlp: primero los hechos por el autor, luego los automáticos
  3  Whisper sobre el audio (se baja si es link). Reanudable: con --budget se detiene limpio y
     se repite el MISMO comando hasta terminar (la VM del dispositivo corta a 180 s por llamada)
  4  nada funcionó -> "sin-oidos": NO es prueba de que el video sea mudo.
Chrome + Sider (peldaño extra para YouTube) lo hace el agente a mano; ver references/oidos.md.

Salida en DIR: transcript.md, oidos.json y, si hubo subtítulos Y Whisper, transcript_subtitulos.md
(para cotejar números y términos). Códigos: 0 completo · 3 parcial (repetir) · 2 sin oídos.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT_EXT = (".srt", ".vtt", ".json3", ".json", ".txt", ".md")
REGLA2 = ("Sin transcript NO se puede decir que el video no habla: es «no verificado». "
          "Un fallo de descarga (429, bloqueo) es un fallo de acceso, no un video mudo.")


def is_url(s):
    return bool(re.match(r"^https?://", s.strip(), re.I))


def classify(src):
    """'url' | 'texto' | 'media' | 'nada'"""
    if is_url(src): return "url"
    if not os.path.isfile(src): return "nada"
    return "texto" if src.lower().endswith(TEXT_EXT) else "media"


def fail_cause(stderr):
    """Causa legible de un fallo de yt-dlp (para retransmitir tal cual, sin adivinar)."""
    s = (stderr or "").lower()
    if "429" in s or "too many requests" in s: return "HTTP 429 (límite de peticiones): acceso, no ausencia de voz"
    if "sign in" in s or "confirm you" in s or "bot" in s: return "YouTube pide sesión/verificación: acceso bloqueado"
    if "private" in s or "unavailable" in s: return "video privado o no disponible"
    if "no subtitles" in s or "there are no subtitles" in s: return "el video no tiene subtítulos publicados"
    if "unable to download" in s or "urlopen error" in s or "name resolution" in s: return "sin red hacia el sitio"
    return "sin detalle: " + (stderr or "").strip()[-160:]


def count_words(path):
    with open(path, encoding="utf-8") as f:
        return sum(len(l.split()) for l in f if not l.startswith("<!--"))


def key_line(msg, *starts):
    """Línea útil de la salida de transcribe.py (ignora avisos de onnxruntime y similares)."""
    for l in msg.splitlines():
        if l.startswith(starts): return l
    return msg.splitlines()[-1] if msg else "falló sin mensaje"


def numbers(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)          # encabezado (prob: 1.00) no es habla
    return set(re.findall(r"\b\d+(?:[.,]\d+)?\b", re.sub(r"^\[[^\]]*\]", "", text, flags=re.M)))


def cotejo(path_a, path_b):
    """Números que aparecen en un transcript y no en el otro (cifras y valores = lo que más se corrompe)."""
    with open(path_a, encoding="utf-8") as fa, open(path_b, encoding="utf-8") as fb:
        a, b = fa.read(), fb.read()
    na, nb = numbers(a), numbers(b)
    return {"comunes": len(na & nb), "solo_whisper": sorted(na - nb)[:20], "solo_subtitulos": sorted(nb - na)[:20]}


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def ingest(src, out_md, kind="auto"):
    r = run([sys.executable, os.path.join(HERE, "ingest_transcript.py"), src, "--out", out_md, "--kind", kind])
    ok = r.returncode == 0 and os.path.exists(out_md) and os.path.getsize(out_md) > 0
    words = 0
    if ok:
        words = count_words(out_md)
    return ok and words >= 15, words, (r.stdout + r.stderr).strip()


def subs_from_url(url, work, lang):
    """Devuelve (archivo|None, tipo, intentos). Primero subtítulos del autor, luego automáticos."""
    ytdlp = shutil.which("yt-dlp") or os.path.expanduser("~/.local/bin/yt-dlp")
    if not os.path.exists(ytdlp):
        return None, None, [{"peldano": "subs", "ok": False, "causa": "yt-dlp no está instalado: pip install --user --break-system-packages yt-dlp"}]
    langs = ",".join(x for l in ([lang] if lang else ["es", "en"]) for x in (l, l + "-orig"))
    tries = []
    for tipo, flag in (("subtitulos-del-autor", "--write-subs"), ("subtitulos-automaticos", "--write-auto-subs")):
        for old in glob.glob(os.path.join(work, "subs.*")): os.remove(old)
        r = run([ytdlp, "--skip-download", flag, "--sub-langs", langs, "--convert-subs", "srt",
                 "-o", os.path.join(work, "subs.%(ext)s"), url])
        files = sorted(f for f in glob.glob(os.path.join(work, "subs.*.srt")) if not os.path.basename(f).startswith("._"))
        if files:
            # preferir el idioma pedido y, en automáticos, la pista -orig (la hablada, no la traducida)
            files.sort(key=lambda f: (0 if "-orig" in f else 1, 0 if lang and f".{lang}" in f else 1))
            tries.append({"peldano": tipo, "ok": True, "archivo": os.path.basename(files[0])})
            return files[0], tipo, tries
        tries.append({"peldano": tipo, "ok": False, "causa": fail_cause(r.stderr) if r.returncode else "no hay pista en el idioma pedido"})
    return None, None, tries


def get_audio(src, work):
    if classify(src) == "media": return src, None
    ytdlp = shutil.which("yt-dlp") or os.path.expanduser("~/.local/bin/yt-dlp")
    mp3 = os.path.join(work, "audio.mp3")
    if os.path.exists(mp3) and os.path.getsize(mp3) > 10000: return mp3, None
    if not os.path.exists(ytdlp): return None, "yt-dlp no está instalado"
    r = run([ytdlp, "-q", "--no-warnings", "-f", "ba/b", "-x", "--audio-format", "mp3", "--audio-quality", "5",
             "-o", os.path.join(work, "audio.%(ext)s"), src])
    if os.path.exists(mp3): return mp3, None
    return None, fail_cause(r.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fuente"); ap.add_argument("--out", required=True)
    ap.add_argument("--lang"); ap.add_argument("--model", default="small")
    ap.add_argument("--budget", type=float, default=0, help="segundos máximos de Whisper por corrida (VM: 150)")
    ap.add_argument("--whisper", action="store_true", help="correr Whisper aunque haya subtítulos (el audio manda)")
    ap.add_argument("--no-whisper", action="store_true")
    ap.add_argument("--transcript", help="archivo de transcript que Bryan ya tiene")
    a = ap.parse_args()
    out = os.path.abspath(a.out); os.makedirs(out, exist_ok=True)
    md = os.path.join(out, "transcript.md")
    rep = {"fuente": a.fuente, "estado": "sin-oidos", "peldano": None, "tipo": None, "idioma": a.lang,
           "palabras": 0, "intentos": [], "regla2": REGLA2}
    kind = classify(a.fuente)
    if kind == "nada":
        sys.exit("ERROR: la fuente no es un link ni un archivo que exista: " + a.fuente)

    # Si Whisper quedó a medias en una corrida anterior, se continúa SIN tocar transcript.md.
    resuming = os.path.exists(md + ".progreso.json")
    keep = os.path.join(out, "transcript_subtitulos.md")

    # 1 · transcript que ya existe
    txt = None if resuming else (a.transcript or (a.fuente if kind == "texto" else None))
    if txt:
        ok, words, msg = ingest(txt, md)
        rep["intentos"].append({"peldano": "transcript-existente", "ok": ok, "causa": None if ok else (msg or "vacío o muy corto")})
        if ok:
            rep.update(estado="completo", peldano="transcript-existente", tipo="segun-archivo", palabras=words)

    # 2 · subtítulos del link
    subs_md = None
    if rep["estado"] != "completo" and kind == "url" and not resuming:
        f, tipo, tries = subs_from_url(a.fuente, out, a.lang)
        rep["intentos"] += tries
        if f:
            ok, words, msg = ingest(f, md, "captions")   # subtítulos reales, no resumen
            if ok:
                rep.update(estado="completo", peldano=tipo, tipo=tipo, palabras=words)
                subs_md = md
            else:
                rep["intentos"].append({"peldano": "ingest-subs", "ok": False, "causa": msg or "subtítulos casi vacíos"})

    # 3 · Whisper (si faltó texto, o si piden que el audio mande)
    if not a.no_whisper and (rep["estado"] != "completo" or a.whisper) and kind in ("url", "media"):
        if subs_md:   # conservar los subtítulos aparte para cotejar
            shutil.copy(subs_md, keep)
        if os.path.exists(keep): subs_md = keep
        audio, why = get_audio(a.fuente, out)
        if not audio:
            rep["intentos"].append({"peldano": "audio", "ok": False, "causa": why})
        else:
            cmd = [sys.executable, os.path.join(HERE, "transcribe.py"), audio, "--out", md, "--model", a.model]
            if a.lang: cmd += ["--lang", a.lang]
            if a.budget: cmd += ["--budget", str(a.budget)]
            r = run(cmd)
            msg = (r.stdout + r.stderr).strip()
            if r.returncode == 0:
                words = count_words(md)
                low = "AVISO: idioma poco seguro" in msg
                rep.update(estado="completo", peldano="whisper", tipo="whisper-" + a.model, palabras=words)
                rep["intentos"].append({"peldano": "whisper", "ok": True, "aviso": "música/voz no verificada" if low else None})
                if words == 0: rep["estado"] = "sin-voz-detectada"   # Whisper recorrió todo el audio y no halló habla
                elif low: rep["estado"] = "dudoso"
            elif r.returncode == 3:
                rep.update(estado="parcial", peldano="whisper", tipo="whisper-" + a.model, palabras=count_words(md))
                rep["siguiente"] = "repetir el MISMO comando: " + " ".join(sys.argv)
                rep["intentos"].append({"peldano": "whisper", "ok": False, "causa": key_line(msg, "PARCIAL")})
            else:
                rep["intentos"].append({"peldano": "whisper", "ok": False, "causa": key_line(msg, "NO_WHISPER", "NO_MODEL", "ERROR")})
                if subs_md and os.path.exists(subs_md):   # Whisper falló: quedan los subtítulos
                    shutil.copy(subs_md, md)
        if rep["estado"] == "completo" and subs_md and os.path.exists(subs_md):
            rep["cotejo"] = cotejo(md, subs_md)

    # 4 · informe
    rep["confianza"] = {"completo": "alta" if rep["peldano"] == "whisper" else "media-alta (subtítulos: términos y cifras a cotejar con pantalla)",
                        "dudoso": "baja: Whisper no reconoció idioma con seguridad (¿música?)",
                        "parcial": "incompleta: falta transcribir el resto", "sin-oidos": "ninguna: voz NO verificada",
                        "sin-voz-detectada": "Whisper recorrió todo el audio y no detectó habla (evidencia propia; decir «Whisper no detectó voz», no «no habla»)"}[rep["estado"]]
    json.dump(rep, open(os.path.join(out, "oidos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"[oir] estado: {rep['estado']} · peldaño: {rep['peldano']} · ~{rep['palabras']} palabras · confianza: {rep['confianza']}")
    for t in rep["intentos"]:
        print(f"[oir]  - {t['peldano']}: {'OK' if t['ok'] else 'falló: ' + str(t.get('causa'))}")
    if rep.get("cotejo"): print("[oir] cotejo de números:", json.dumps(rep["cotejo"], ensure_ascii=False))
    if rep.get("siguiente"): print("[oir] SIGUIENTE:", rep["siguiente"])
    if rep["estado"] == "sin-oidos": print("[oir] " + REGLA2)
    return {"completo": 0, "dudoso": 0, "sin-voz-detectada": 0, "parcial": 3}.get(rep["estado"], 2)


if __name__ == "__main__":
    sys.exit(main())
