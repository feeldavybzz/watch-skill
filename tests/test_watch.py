import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from urllib.error import HTTPError

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/mukiwa-learn/scripts'
sys.path.insert(0, str(SCRIPTS))
import cues  # noqa: E402
import extract_frames as ef  # noqa: E402
import gemini  # noqa: E402
import metrics  # noqa: E402
import watch  # noqa: E402


def make_video(path, seconds=6):
    subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i', f'testsrc2=size=160x90:rate=10', '-f', 'lavfi',
                    '-i', 'sine=frequency=440', '-t', str(seconds), '-c:v', 'mpeg4', '-c:a', 'aac', '-shortest', str(path)],
                   check=True)


class FramesTests(unittest.TestCase):
    def test_spread_covers_range_despite_clustered_cuts(self):
        cuts = [i * 0.5 for i in range(1, 41)] + [100.0]    # 40 cortes en la intro y uno más tarde
        picked = ef.spread(cuts + [0.05, 299.9], 0, 300, 10)
        self.assertIn(0.05, picked)                         # el primer instante (gancho) siempre
        self.assertIn(299.9, picked)
        self.assertLessEqual(ef.max_gap(picked, 0, 300), 2 * 300 / 8)
        self.assertLess(sum(1 for t in picked if t < 20), 4)

    def test_parse_at(self):
        self.assertEqual(ef.parse_at('13:11, 95,1:00:00.5'), [95.0, 791.0, 3600.5])
        with self.assertRaises(ValueError):
            ef.parse_at('13m11s')

    def test_dedupe_respects_pinned_and_max_hole(self):
        with tempfile.TemporaryDirectory() as d:
            frames = []
            for i, t in enumerate([0, 10, 20, 30, 40, 50]):
                p = Path(d) / f'f{i}.jpg'
                Image.new('RGB', (64, 36), (200, 30, 30)).save(p)
                frames.append({'file': str(p), 't': t, 'reason': 'pinned' if t == 30 else 'detail'})
            kept, dropped = ef.dedupe([dict(f) for f in frames], max_hole=25)
            times = [f['t'] for f in kept]
            self.assertIn(30, times)                        # fija: nunca se descarta
            self.assertIn(50, times)                        # última: nunca se descarta
            self.assertLessEqual(ef.max_gap(times, 0, 50), 25)
            self.assertGreater(dropped, 0)

    def test_dedupe_keeps_different_frames(self):
        with tempfile.TemporaryDirectory() as d:
            frames = []
            for i, color in enumerate([(0, 0, 0), (255, 255, 255), (0, 0, 0)]):
                p = Path(d) / f'f{i}.jpg'
                Image.new('RGB', (64, 36), color).save(p)
                frames.append({'file': str(p), 't': i, 'reason': 'detail'})
            self.assertEqual(ef.dedupe(frames)[1], 0)


class CuesTests(unittest.TestCase):
    def test_detects_pointing_phrases_with_spacing(self):
        lines = ['[00:00:01.00] Hola a todos', '[00:00:05.00] y si te fijas acá arriba',
                 '[00:00:07.00] como ves, cambia', '[00:01:00.00] look at this diagram', '[00:01:30.00] nada aquí']
        hits = cues.find_cues(lines)
        self.assertEqual([h['t'] for h in hits], [5.5, 60.5])   # 7 s queda a menos de 8 s del anterior

    def test_ignores_plain_speech(self):
        self.assertEqual(cues.find_cues(['[00:00:01.00] Mirá que hoy hablamos de color']), [])


class MetricsTests(unittest.TestCase):
    def test_rhythm(self):
        r = metrics.rhythm([1, 2, 3, 50, 70, 80, 90, 95, 98], 0, 100)
        self.assertEqual(r['cortes'], 9)
        self.assertEqual(r['gancho'], {'cortes_0_3s': 2, 'cortes_0_10s': 3, 'primer_corte_s': 1})
        self.assertEqual(r['tendencia'], 'acelera')

    def test_palette_reports_measured_hex(self):
        with tempfile.TemporaryDirectory() as d:
            files = []
            for i, color in enumerate([(0, 104, 251), (197, 237, 46)]):
                p = Path(d) / f'{i}.png'
                Image.new('RGB', (32, 32), color).save(p)
                files.append(str(p))
            pal = metrics.palette(files, n=2)
            self.assertEqual(sorted(c['hex'] for c in pal), ['#0068FB', '#C5ED2E'])
            self.assertEqual(sum(c['porcentaje'] for c in pal), 100.0)


class FakeResponse(io.BytesIO):
    def __init__(self, body, status=200, headers=None):
        super().__init__(body)
        self.status, self.headers = status, headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class GeminiTests(unittest.TestCase):
    KEY = 'AIza-clave-de-prueba'

    def test_youtube_detection(self):
        self.assertTrue(gemini.is_youtube('https://youtu.be/sLOj0YS1KVg'))
        self.assertTrue(gemini.is_youtube('https://www.youtube.com/watch?v=abc&t=3'))
        self.assertFalse(gemini.is_youtube('https://www.instagram.com/reel/abc/'))

    def test_config_reads_file_and_env(self):
        with tempfile.TemporaryDirectory() as d:
            cfg = Path(d) / '.env'
            gemini.ensure_config(cfg)
            self.assertEqual(oct(cfg.stat().st_mode & 0o777), '0o600')
            self.assertIsNone(gemini.config_value('GEMINI_API_KEY_TEST', path=cfg))
            cfg.write_text('# x\nGEMINI_API_KEY_TEST="abc"\n', encoding='utf-8')
            self.assertEqual(gemini.config_value('GEMINI_API_KEY_TEST', path=cfg), 'abc')

    def test_ask_parses_answer_and_sends_key_in_header(self):
        seen = {}

        def opener(req, timeout):
            seen['key'] = req.get_header('X-goog-api-key')
            seen['payload'] = json.loads(req.data)
            body = {'steps': [{'type': 'model_output', 'content': [{'type': 'text', 'text': '[00:05] Un gráfico'}]}],
                    'usage': {'total_tokens': 1234}}
            return FakeResponse(json.dumps(body).encode())
        res = gemini.ask({'uri': 'https://youtu.be/x'}, '¿Qué se ve?', 'gemini-test', self.KEY, opener=opener)
        self.assertEqual(res['text'], '[00:05] Un gráfico')
        self.assertEqual(res['total_tokens'], 1234)
        self.assertEqual(seen['key'], self.KEY)
        self.assertNotIn(self.KEY, json.dumps(seen['payload']))
        self.assertIn('¿Qué se ve?', seen['payload']['input'][1]['text'])

    def test_http_errors_are_categorized_and_key_redacted(self):
        def opener(req, timeout):
            raise HTTPError(req.full_url, 429, 'quota', {}, io.BytesIO(
                json.dumps({'error': {'message': 'limit for key ' + GeminiTests.KEY}}).encode()))
        with self.assertRaises(SystemExit) as ctx:
            gemini.ask({'uri': 'u'}, None, 'm', self.KEY, opener=opener)
        self.assertIn('Gemini quota', str(ctx.exception))
        self.assertNotIn(self.KEY, str(ctx.exception))

    def test_upload_then_delete(self):
        calls = []

        def opener(req, timeout):
            calls.append(req.get_method() + ' ' + req.full_url)
            if 'upload/v1beta/files' in req.full_url:
                return FakeResponse(b'{}', headers={'X-Goog-Upload-URL': 'https://upload.example/s'})
            if req.full_url.startswith('https://upload.example'):
                return FakeResponse(json.dumps({'file': {'name': 'files/1', 'uri': 'gs://1', 'state': 'ACTIVE'}}).encode())
            return FakeResponse(b'{}')
        with tempfile.TemporaryDirectory() as d:
            video = Path(d) / 'v.mp4'
            video.write_bytes(b'0' * 100)
            up = gemini.upload_file(video, self.KEY, opener=opener)
        self.assertEqual(up['uri'], 'gs://1')
        self.assertIsNone(gemini.delete_file(up['name'], self.KEY, opener=opener))
        self.assertTrue(calls[-1].startswith('DELETE '))


class WatchTests(unittest.TestCase):
    def test_pick_captions_prefers_original_language(self):
        with tempfile.TemporaryDirectory() as d:
            for name in ('video.en.srt', 'video.es.srt', 'video.pt-orig.srt'):
                (Path(d) / name).write_text('1\n00:00:00,000 --> 00:00:01,000\nx\n')
            (Path(d) / 'video.info.json').write_text(json.dumps({'language': 'pt'}))
            path, why = watch.pick_captions(d)
            self.assertTrue(path.endswith('video.pt-orig.srt'))
            self.assertIn('original', why)
            self.assertTrue(watch.pick_captions(d, lang='en')[0].endswith('video.en.srt'))

    def test_end_to_end_local_file_with_captions(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            video = d / 'clip.mp4'
            make_video(video)
            (d / 'clip.es.srt').write_text('1\n00:00:00,500 --> 00:00:02,000\nHola, como ves acá está el menú\n\n'
                                           '2\n00:00:04,000 --> 00:00:05,500\nY eso es todo\n', encoding='utf-8')
            out = d / 'work'
            r = subprocess.run([sys.executable, str(SCRIPTS / 'watch.py'), str(video), '--out', str(out),
                                '--detail', 'efficient', '--at', '4'], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
            ev = json.loads((out / 'evidence.json').read_text())
            self.assertEqual(ev['status'], 'ready')
            self.assertEqual(len(ev['cues']), 1)
            report = (out / 'informe.md').read_text()
            self.assertIn('gancho', report)
            self.assertIn('señal en la voz', report)
            self.assertIn('pedida con --at', report)
            self.assertIn('Ritmo de edición', report)
            manifest = json.loads((out / 'visual/manifest.json').read_text())
            fixed = [f for f in manifest['frames'] if f['reason'] == 'pinned']
            with Image.open(fixed[0]['file']) as im:
                self.assertEqual(im.width, 160)                  # 1280 es un máximo: no se agranda

    def test_partial_without_text(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            video = d / 'mudo.mp4'
            make_video(video, 3)
            r = subprocess.run([sys.executable, str(SCRIPTS / 'watch.py'), str(video), '--out', str(d / 'w'),
                                '--no-whisper', '--detail', 'efficient'], capture_output=True, text=True)
            self.assertEqual(r.returncode, 2, r.stderr)
            self.assertIn('PARCIAL', (d / 'w/informe.md').read_text())


if __name__ == '__main__':
    unittest.main()


import importlib.util  # noqa: E402
import zipfile  # noqa: E402
_spec = importlib.util.spec_from_file_location('grab', ROOT / 'skills/mukiwa-grab/scripts/grab.py')
grab = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(grab)


class CaptionTrackTests(unittest.TestCase):
    T = [{'ext': 'vtt'}]

    def test_original_auto_track_beats_translations(self):
        info = {'automatic_captions': {'en-orig': self.T, 'en': self.T, 'es': self.T}, 'language': None}
        self.assertEqual(grab.pick_track(info), {'key': 'en-orig', 'kind': 'automatic', 'provenance': 'original'})

    def test_manual_in_original_language_first(self):
        info = {'language': 'es', 'subtitles': {'es': self.T, 'en': self.T}, 'automatic_captions': {'es-orig': self.T}}
        self.assertEqual(grab.pick_track(info)['key'], 'es')
        self.assertEqual(grab.pick_track(info)['kind'], 'manual')

    def test_requested_language_and_missing(self):
        info = {'automatic_captions': {'pt-orig': self.T, 'es': self.T}}
        self.assertEqual(grab.pick_track(info, 'es'), {'key': 'es', 'kind': 'automatic', 'provenance': 'traducción pedida'})
        self.assertIsNone(grab.pick_track(info, 'fr'))
        self.assertIsNone(grab.pick_track({}))

    def test_unknown_language_prefers_spanish(self):
        info = {'subtitles': {'en': self.T, 'es': self.T, 'live_chat': self.T}}
        self.assertEqual(grab.pick_track(info)['key'], 'es')


class PackageTests(unittest.TestCase):
    def test_skill_packages(self):
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, str(ROOT / 'tools/build_skills.py'), '--out', d, '--allow-dirty'],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            for name in ('mukiwa-grab', 'mukiwa-learn'):
                with zipfile.ZipFile(Path(d) / f'{name}.skill') as z:
                    names = z.namelist()
                self.assertTrue(all(n.startswith(name + '/') for n in names))
                self.assertEqual([n for n in names if n.endswith('SKILL.md')], [f'{name}/SKILL.md'])
                self.assertFalse([n for n in names if '/._' in n or '_descargas' in n or '/work/' in n])
                self.assertLess(len(names), 200)
            with zipfile.ZipFile(Path(d) / 'mukiwa-learn.skill') as z:
                names = z.namelist()
            self.assertIn('mukiwa-learn/scripts/grab.py', names)
            self.assertIn('mukiwa-learn/library/INDEX.md', names)
            self.assertIn('mukiwa-learn/scripts/watch.py', names)
            self.assertTrue((Path(d) / 'profe-diseno-grafico.skill').exists())


class ProfesTests(unittest.TestCase):
    def run_profes(self, env, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / 'profes.py'), *args], capture_output=True, text=True, env=env)

    def test_create_feed_install_and_existing_skill(self):
        import os
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            env = dict(os.environ, MUKIWA_PROFES=str(d / 'profes'), HOME=str(d / 'home'))
            lesson = d / 'grading-basico.md'
            lesson.write_text('# Grading básico en DaVinci\n> x\n\n- **Fuente**: https://youtu.be/abc · canal\n', encoding='utf-8')
            r = self.run_profes(env, 'ensure', '--nicho', 'color-grading', '--nombre', 'Color grading',
                                '--herramientas', 'DaVinci Resolve,Premiere Pro', '--cuando', 'gradear o crear un look')
            self.assertEqual(r.returncode, 0, r.stderr)
            skill = d / 'profes/color-grading/SKILL.md'
            text = skill.read_text(encoding='utf-8')
            self.assertIn('name: profe-color-grading', text)
            self.assertIn('### DaVinci Resolve', text)
            self.assertIn('### Premiere Pro', text)
            self.assertIn('gradear o crear un look', text)
            for _ in range(2):   # alimentar dos veces la misma lección no la duplica
                self.assertEqual(self.run_profes(env, 'attach', '--nicho', 'color-grading', '--leccion', str(lesson)).returncode, 0)
            text = skill.read_text(encoding='utf-8')
            self.assertEqual(text.count('- [1] Grading básico en DaVinci'), 1)
            self.assertIn('  lecciones: 1', text)
            self.assertTrue((d / 'profes/color-grading/references/lecciones/grading-basico.md').exists())
            self.assertIn('1 lección', (d / 'profes/INDEX.md').read_text(encoding='utf-8'))
            self.assertEqual(self.run_profes(env, 'install').returncode, 0)
            link = d / 'home/.claude/skills/profe-color-grading'
            self.assertTrue(link.is_symlink())
            self.assertEqual(self.run_profes(env, 'check').returncode, 0)
            # Skill propia existente: se añade una línea y el conocimiento va a references/
            own = d / 'home/.claude/skills/mi-skill'
            own.mkdir(parents=True)
            (own / 'SKILL.md').write_text('---\nname: mi-skill\ndescription: algo\n---\n\n# Mi skill\n', encoding='utf-8')
            for _ in range(2):
                self.assertEqual(self.run_profes(env, 'attach', '--skill', str(own), '--leccion', str(lesson)).returncode, 0)
            self.assertEqual((own / 'SKILL.md').read_text(encoding='utf-8').count('Aprendido de referencias'), 1)
            self.assertEqual((own / 'references/aprendido-mukiwa.md').read_text(encoding='utf-8').count('- [1]'), 1)
            r = self.run_profes(env, 'list')
            self.assertIn('color-grading', r.stdout)
            self.assertIn('mi-skill', r.stdout)

    def test_rejects_bad_niche(self):
        import os
        with tempfile.TemporaryDirectory() as d:
            env = dict(os.environ, MUKIWA_PROFES=str(Path(d) / 'p'), HOME=d)
            r = self.run_profes(env, 'ensure', '--nicho', 'Color Grading', '--nombre', 'x')
            self.assertNotEqual(r.returncode, 0)
