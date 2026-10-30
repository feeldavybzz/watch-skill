#!/usr/bin/env python3
"""Transcribe audio/video con faster-whisper. REANUDABLE: sirve en entornos con límite de tiempo por llamada
(la VM del dispositivo corta a 180 s por comando).

Uso: python transcribe.py ARCHIVO --out transcript.md [--model small] [--lang es] [--budget 150]

- Escribe cada segmento al terminar y guarda el avance en OUT.progreso.json.
- Con --budget SEGUNDOS se detiene limpio al pasar ese tiempo: sale con código 3 y dice
  "PARCIAL ... repetir el MISMO comando". Al repetirlo continúa donde quedó (no reinicia).
- Códigos: 0 completo · 3 parcial (repetir) · 1 error · mensaje NO_WHISPER / NO_MODEL si falta algo
  (en ese caso NO insistir por otras rutas: pedir transcript o correr en otra máquina).
"""
import argparse, json, os, subprocess, sys, tempfile, time

SR = 16000


def ts(s):
    return f"{int(s//3600):02d}:{int(s%3600//60):02d}:{s%60:05.2f}"


def load_progress(path):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def resume_point(out, prog_path, model, lang):
    """Segundo desde el que continuar. 0 si no hay avance válido (otro modelo/idioma o salida borrada)."""
    d = load_progress(prog_path)
    if not d or not os.path.exists(out) or d.get("model") != model:
        return 0.0, d if d.get("model") == model else {}
    if lang and d.get("lang") and d["lang"] != lang:
        return 0.0, {}
    return float(d.get("hecho_hasta", 0.0)), d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="small"); ap.add_argument("--lang", default=None)
    ap.add_argument("--budget", type=float, default=0, help="segundos máximos de esta corrida (0 = sin límite)")
    ap.add_argument("--threads", type=int, default=0)
    a = ap.parse_args()
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("NO_WHISPER: pip install --user --break-system-packages faster-whisper (o usar un transcript externo)")
    t0 = time.time()
    wav = tempfile.mktemp(suffix=".wav")
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.file, "-vn", "-ac", "1", "-ar", str(SR), wav])
    if r.returncode:
        sys.exit("ERROR: ffmpeg no pudo leer el audio de " + a.file)
    try:
        import numpy as np, wave
        with wave.open(wav) as w:
            audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    except Exception as e:
        sys.exit(f"ERROR: no se pudo leer el wav ({e})")
    finally:
        try: os.remove(wav)
        except OSError: pass
    dur = len(audio) / SR
    prog_path = a.out + ".progreso.json"
    start, prev = resume_point(a.out, prog_path, a.model, a.lang)
    if start >= dur - 1:
        print("OK (ya estaba completo) ->", a.out); return 0
    try:
        m = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=a.threads or (os.cpu_count() or 2))
    except Exception as e:
        sys.exit(f"NO_MODEL: no se pudo cargar/descargar el modelo '{a.model}' ({type(e).__name__}). "
                 "Pedir transcript externo (Sider/YouTube/SpeakApp) o correr en otra máquina.")
    lang = prev.get("lang") or a.lang
    segs, info = m.transcribe(audio[int(start * SR):], language=lang, vad_filter=True)
    lang = lang or info.language
    prob = prev.get("prob", getattr(info, "language_probability", 1))
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    mode = "a" if start > 0 else "w"
    done = start; partial = False
    with open(a.out, mode, encoding="utf-8") as f:
        if mode == "w":
            f.write(f"<!-- fuente: whisper-{a.model} | tipo: captions | tiempos: si | idioma: {lang} | prob: {prob:.2f} -->\n")
            f.flush()
        for s in segs:
            f.write(f"[{ts(start + s.start)}] {s.text.strip()}\n"); f.flush()
            done = start + s.end
            json.dump({"model": a.model, "lang": lang, "prob": prob, "hecho_hasta": done, "duracion": dur},
                      open(prog_path, "w", encoding="utf-8"))
            if a.budget and time.time() - t0 > a.budget and done < dur - 2:
                partial = True; break
    if prob < 0.8:
        print("AVISO: idioma poco seguro (%.2f) -> probablemente música/ruido; no usar como teoría." % prob)
    if partial:
        print(f"PARCIAL: {ts(done)} de {ts(dur)} ({done/dur:.0%}). Repetir el MISMO comando para continuar.")
        return 3
    try: os.remove(prog_path)
    except OSError: pass
    print("OK ->", a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
