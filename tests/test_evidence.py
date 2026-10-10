import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import json

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/mukiwa-learn/scripts'
spec = importlib.util.spec_from_file_location('ingest', SCRIPTS / 'ingest_transcript.py')
ingest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ingest)


class EvidenceTests(unittest.TestCase):
    def test_vtt_without_cue_id_keeps_first_line(self):
        value = 'WEBVTT\n\n00:00:00.000 --> 00:00:02.000\nPrimera frase\nSegunda línea\n'
        self.assertEqual(ingest.from_srt_vtt(value), [(0.0, 'Primera frase Segunda línea')])

    def test_srt_repetition(self):
        value = '1\n00:00:01,000 --> 00:00:02,000\nMover el plano Mover el plano\n'
        self.assertEqual(ingest.from_srt_vtt(value), [(1.0, 'Mover el plano')])

    def test_fractional_timestamp(self):
        self.assertEqual(ingest.from_plain('[00:00:01.25] Paso uno'), [(1.25, 'Paso uno')])

    def test_partial_without_transcript_and_ready_with_text(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            video = d / 'fixture.mp4'
            subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i', 'testsrc2=size=160x90:rate=10', '-t', '2', '-c:v', 'mpeg4', str(video)], check=True)
            args = [sys.executable, str(SCRIPTS / 'prepare.py'), str(video), '--max', '3']
            partial = subprocess.run(args + ['--out', str(d / 'partial')], capture_output=True, text=True)
            self.assertEqual(partial.returncode, 2, partial.stderr)
            evidence = json.loads((d / 'partial/evidence.json').read_text())
            self.assertEqual(evidence['status'], 'partial')
            self.assertFalse(evidence['agent_analysis_completed'])
            captions = d / 'subs.vtt'
            captions.write_text('WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nPaso uno\n')
            ready = subprocess.run(args + ['--out', str(d / 'ready'), '--transcript', str(captions)], capture_output=True, text=True)
            self.assertEqual(ready.returncode, 0, ready.stderr)
            manifest = json.loads((d / 'ready/visual/manifest.json').read_text())
            self.assertEqual(manifest['evidence_type'], 'sampled_frames')
            self.assertGreater(manifest['frames'][-1]['t'], 1.8)


if __name__ == '__main__':
    unittest.main()
