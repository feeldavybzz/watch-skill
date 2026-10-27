#!/usr/bin/env python3
"""Inspecciona un video/audio: duración, resolución, ¿tiene audio?, ¿audio con contenido real?
Uso: python probe.py <archivo>   -> imprime JSON"""
import json, subprocess, sys, re

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def main(path):
    r = run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", path])
    if r.returncode:
        print(json.dumps({"error": r.stderr.strip()})); sys.exit(1)
    d = json.loads(r.stdout)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in d["streams"] if s["codec_type"] == "audio"), None)
    out = {
        "duration_s": float(d["format"].get("duration", 0)),
        "has_video": bool(v), "has_audio_stream": bool(a),
        "width": v and v.get("width"), "height": v and v.get("height"),
        "fps": v and v.get("avg_frame_rate"),
    }
    out["audio_has_content"] = False
    if a:
        # volumedetect: si max_volume ~ -91 dB el audio es silencio
        r = run(["ffmpeg", "-hide_banner", "-t", "120", "-i", path, "-vn", "-af", "volumedetect", "-f", "null", "-"])
        m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
        if m:
            out["max_volume_db"] = float(m.group(1))
            out["audio_has_content"] = float(m.group(1)) > -60
    out["recommendation"] = (
        "audio con contenido: obtener transcripción (Sider/subs/Whisper) + frames"
        if out["audio_has_content"] else
        "sin audio útil: modo SOLO-VISUAL (frames + texto en pantalla)")
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1])
