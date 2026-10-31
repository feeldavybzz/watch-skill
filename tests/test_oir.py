import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/kiwa-watch-learn/scripts'
sys.path.insert(0, str(SCRIPTS))
import oir  # noqa: E402
import transcribe  # noqa: E402


class OirTests(unittest.TestCase):
    def test_classify(self):
        with tempfile.TemporaryDirectory() as d:
            srt = Path(d) / 'a.srt'; srt.write_text('x')
            mp4 = Path(d) / 'a.mp4'; mp4.write_text('x')
            self.assertEqual(oir.classify('https://youtu.be/abc'), 'url')
            self.assertEqual(oir.classify(str(srt)), 'texto')
            self.assertEqual(oir.classify(str(mp4)), 'media')
            self.assertEqual(oir.classify(str(Path(d) / 'no.mp4')), 'nada')

    def test_fail_cause_never_says_mute(self):
        self.assertIn('acceso', oir.fail_cause('ERROR: HTTP Error 429: Too Many Requests'))
        self.assertIn('sesión', oir.fail_cause('Sign in to confirm you are not a bot'))
        self.assertNotIn('mudo', oir.fail_cause('lo que sea').lower())

    def test_numbers_ignore_header_and_timestamps(self):
        t = '<!-- fuente: whisper | prob: 1.00 -->\n[00:01:02.00] el gain es 0.528 y 45 minutos\n'
        self.assertEqual(oir.numbers(t), {'0.528', '45'})

    def test_cotejo_lists_differences(self):
        with tempfile.TemporaryDirectory() as d:
            a = Path(d) / 'w.md'; b = Path(d) / 's.md'
            a.write_text('[00:00:01.00] gain 0.528 y 8\n'); b.write_text('[00:00:01.00] gain 0.6 y 8\n')
            c = oir.cotejo(str(a), str(b))
            self.assertEqual(c['solo_whisper'], ['0.528'])
            self.assertEqual(c['solo_subtitulos'], ['0.6'])
            self.assertEqual(c['comunes'], 1)

    def test_key_line_skips_warnings(self):
        msg = 'onnxruntime cpuid_info warning\nPARCIAL: 00:03:21 de 00:44:45'
        self.assertTrue(oir.key_line(msg, 'PARCIAL').startswith('PARCIAL'))

    def test_transcript_file_gives_complete_and_report(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / 't.srt'
            lines = []
            for i in range(12):
                lines.append(f'{i+1}\n00:00:{i*2:02d},000 --> 00:00:{i*2+1:02d},500\npalabra{i} otra{i} tercera{i}\n')
            src.write_text('\n'.join(lines))
            out = Path(d) / 'o'
            r = subprocess.run([sys.executable, str(SCRIPTS / 'oir.py'), str(src), '--out', str(out)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            rep = json.loads((out / 'oidos.json').read_text())
            self.assertEqual(rep['estado'], 'completo')
            self.assertEqual(rep['peldano'], 'transcript-existente')
            self.assertTrue((out / 'transcript.md').exists())

    def test_empty_transcript_is_sin_oidos_not_mute(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / 't.txt'; src.write_text('')
            out = Path(d) / 'o'
            r = subprocess.run([sys.executable, str(SCRIPTS / 'oir.py'), str(src), '--out', str(out)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 2)
            rep = json.loads((out / 'oidos.json').read_text())
            self.assertEqual(rep['estado'], 'sin-oidos')
            self.assertIn('no verificado', rep['regla2'])


class ResumeTests(unittest.TestCase):
    def test_resume_point(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / 't.md'; prog = Path(d) / 't.md.progreso.json'
            self.assertEqual(transcribe.resume_point(str(out), str(prog), 'small', None)[0], 0.0)
            out.write_text('x'); prog.write_text(json.dumps({'model': 'small', 'lang': 'es', 'hecho_hasta': 201.6}))
            self.assertEqual(transcribe.resume_point(str(out), str(prog), 'small', 'es')[0], 201.6)
            self.assertEqual(transcribe.resume_point(str(out), str(prog), 'base', 'es')[0], 0.0)   # otro modelo: reinicia
            self.assertEqual(transcribe.resume_point(str(out), str(prog), 'small', 'en')[0], 0.0)  # otro idioma: reinicia
            out.unlink()
            self.assertEqual(transcribe.resume_point(str(out), str(prog), 'small', 'es')[0], 0.0)  # salida borrada


if __name__ == '__main__':
    unittest.main()
