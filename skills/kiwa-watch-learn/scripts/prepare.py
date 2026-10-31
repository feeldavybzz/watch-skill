#!/usr/bin/env python3
"""Preparar evidencia local. No sustituye la inspección visual del agente."""
import argparse
import json
from pathlib import Path
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('video')
    ap.add_argument('--out', required=True)
    ap.add_argument('--transcript')
    ap.add_argument('--whisper', action='store_true')
    ap.add_argument('--max', type=int, default=45)
    a = ap.parse_args()
    source = Path(a.video).resolve()
    if not source.is_file():
        ap.error('No existe el archivo de medios')
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    scripts = Path(__file__).resolve().parent
    def run(name, *args):
        return subprocess.run([sys.executable, str(scripts / name), *map(str, args)],
                              capture_output=True, text=True)
    frames = run('extract_frames.py', source, '--out', out / 'visual', '--max', a.max)
    transcript = out / 'transcript.md'
    audio = None
    if a.transcript:
        audio = run('ingest_transcript.py', a.transcript, '--out', transcript)
    elif a.whisper:
        audio = run('transcribe.py', source, '--out', transcript)
    has_frames = frames.returncode == 0 and (out / 'visual/manifest.json').exists()
    has_text = audio is not None and audio.returncode == 0 and transcript.exists() and transcript.stat().st_size > 0
    evidence = {
        'source': str(source),
        'status': 'ready' if has_frames and has_text else 'partial' if has_frames or has_text else 'blocked',
        'visual_manifest': str(out / 'visual/manifest.json') if has_frames else None,
        'transcript': str(transcript) if has_text else None,
        'visual_error': frames.stderr.strip() if not has_frames else None,
        'transcript_error': audio.stderr.strip() if audio and not has_text else None,
        'transcript_requested': bool(a.transcript or a.whisper),
        'agent_analysis_completed': False,
        'visual_coverage': 'sampled_frames' if has_frames else 'none',
    }
    (out / 'evidence.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(evidence, ensure_ascii=False, indent=2))
    return 0 if evidence['status'] == 'ready' else 2


if __name__ == '__main__':
    sys.exit(main())
