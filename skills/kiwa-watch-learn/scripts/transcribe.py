#!/usr/bin/env python3
"""Transcribe audio/video con faster-whisper si el modelo está disponible. Si no, falla CLARO
(para que Claude pida a Bryan un transcript de Sider/subs/SpeakApp en vez de insistir).

Uso: python transcribe.py ARCHIVO --out transcript.md [--model small] [--lang es]
Sugerencia: correrlo en la compu de Bryan (device_bash) si el contenedor no puede bajar el modelo.
"""
import argparse, subprocess, sys, tempfile, os
ap=argparse.ArgumentParser(); ap.add_argument("file"); ap.add_argument("--out",required=True)
ap.add_argument("--model",default="small"); ap.add_argument("--lang",default=None); a=ap.parse_args()
try:
    from faster_whisper import WhisperModel
except ImportError:
    sys.exit("NO_WHISPER: pip install faster-whisper (o usar un transcript externo)")
wav=tempfile.mktemp(suffix=".wav")
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",a.file,"-vn","-ac","1","-ar","16000",wav],check=True)
try:
    m=WhisperModel(a.model,device="cpu",compute_type="int8")
except Exception as e:
    sys.exit(f"NO_MODEL: no se pudo cargar/descargar el modelo '{a.model}' ({type(e).__name__}). "
             "Pedir transcript externo (Sider/YouTube/SpeakApp) o correr en la compu del usuario.")
# Audio como arreglo numpy: con `av` nuevo (>=17) faster-whisper falla al abrir el archivo (metadata_errors).
try:
    import numpy as np, wave
    with wave.open(wav) as w:
        audio=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
except Exception:
    audio=wav
segs,info=m.transcribe(audio,language=a.lang,vad_filter=True)
# En música Whisper inventa letra: idioma poco seguro => tratar como música, voz no verificada.
if getattr(info,"language_probability",1)<0.8:
    print("AVISO: idioma poco seguro (%.2f) -> probablemente música/ruido; no usar como teoría."%info.language_probability)
def ts(s): return f"{int(s//3600):02d}:{int(s%3600//60):02d}:{s%60:05.2f}"
with open(a.out,"w",encoding="utf-8") as f:
    f.write(f"<!-- fuente: whisper-{a.model} | tipo: captions | tiempos: si | idioma: {info.language} -->\n")
    for s in segs: f.write(f"[{ts(s.start)}] {s.text.strip()}\n")
os.remove(wav); print("OK ->",a.out)
