import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


grab = load('grab_t', ROOT / 'skills/mukiwa-grab/scripts/grab.py')
doctor = load('doctor_t', ROOT / 'skills/mukiwa-grab/scripts/doctor.py')
inbox = load('inbox_t', ROOT / 'skills/mukiwa-learn/scripts/inbox.py')


class ErrorExplanationTests(unittest.TestCase):
    def code(self, text, js_ok=True):
        return grab.explain(text, js_ok)['code']

    def test_known_causes(self):
        self.assertEqual(self.code('ERROR: unable to download: HTTP Error 429: Too Many Requests'), '429')
        self.assertEqual(self.code("ERROR: [youtube] x: Sign in to confirm you're not a bot"), 'login')
        self.assertEqual(self.code('ERROR: [instagram] x: Instagram sent an empty media response. Check if this post is accessible'), 'login')
        self.assertEqual(self.code('ERROR: [youtube] x: Private video. Sign in if you\'ve been granted access'), 'privado')
        self.assertEqual(self.code('ERROR: [youtube] zzz: This video is unavailable'), 'no-existe')
        self.assertEqual(self.code('ERROR: unable to download video data: HTTP Error 403: Forbidden'), '403')
        self.assertEqual(self.code('ERROR: Unsupported URL: https://example.com/x'), 'no-soportado')
        self.assertEqual(self.code('ERROR: <urlopen error [Errno 8] nodename nor servname provided, or not known>'), 'red')
        self.assertEqual(self.code('ERROR: HTTP Error 503: Service Unavailable'), '5xx')

    def test_missing_js_runtime_explains_format_error(self):
        text = 'WARNING: No supported JavaScript runtime\nERROR: [youtube] x: Requested format is not available'
        self.assertEqual(self.code(text, js_ok=False), 'js')
        self.assertEqual(self.code(text, js_ok=True), 'formato')

    def test_warning_alone_is_not_a_failure_cause(self):
        # sin línea de error, una advertencia suelta no debe clasificar como "js" si hay un 429 real
        text = 'WARNING: No supported JavaScript runtime\nERROR: HTTP Error 429: Too Many Requests'
        self.assertEqual(self.code(text), '429')

    def test_unknown_gives_last_line_and_next_step(self):
        info = grab.explain('ERROR: algo rarísimo pasó')
        self.assertEqual(info['code'], 'desconocido')
        self.assertIn('rarísimo', info['causa'])
        self.assertTrue(info['haz'])

    def test_every_known_cause_has_action(self):
        for code, _pat, causa, haz, _retry in grab.ERRORES:
            self.assertTrue(causa and haz, code)


class RetryTests(unittest.TestCase):
    def test_retries_only_what_deserves_it(self):
        calls, sleeps = [], []

        def flaky():
            calls.append(1)
            return (0, 'ok') if len(calls) == 3 else (1, 'ERROR: HTTP Error 429: Too Many Requests')
        code, _ = grab.with_retries(flaky, sleep=sleeps.append, waits=(1, 2, 3), log=lambda *_: None)
        self.assertEqual((code, len(calls), sleeps), (0, 3, [1, 2]))

    def test_does_not_retry_login_or_private(self):
        calls = []

        def once():
            calls.append(1)
            return 1, "ERROR: Sign in to confirm you're not a bot"
        code, _ = grab.with_retries(once, sleep=lambda s: self.fail('no debe esperar'), log=lambda *_: None)
        self.assertEqual((code, len(calls)), (1, 1))

    def test_gives_up_after_all_waits(self):
        calls = []

        def once():
            calls.append(1)
            return 1, 'ERROR: HTTP Error 429: Too Many Requests'
        grab.with_retries(once, sleep=lambda s: None, waits=(1, 2), log=lambda *_: None)
        self.assertEqual(len(calls), 3)


class JsRuntimeTests(unittest.TestCase):
    def fake_node(self, home, version):
        p = Path(home) / 'nodejs' / f'node-v{version}-darwin-arm64' / 'bin' / 'node'
        p.parent.mkdir(parents=True)
        p.write_text('#!/bin/sh\n')
        p.chmod(0o755)
        return str(p)

    def test_finds_highest_node_outside_path(self):
        with tempfile.TemporaryDirectory() as d:
            self.fake_node(d, '20.1.0')
            newest = self.fake_node(d, '22.14.0')
            old_bin = grab.BIN_DIR
            grab.BIN_DIR = str(Path(d) / 'sin-bin')
            try:
                self.assertEqual(grab.find_js_runtime(which=lambda n: None, home=d), ('node', newest))
            finally:
                grab.BIN_DIR = old_bin

    def test_prefers_deno_then_node_in_path(self):
        old_bin = grab.BIN_DIR
        grab.BIN_DIR = '/no/existe'
        try:
            self.assertEqual(grab.find_js_runtime(which=lambda n: {'deno': '/x/deno', 'node': '/x/node'}.get(n), home='/vacio'), ('deno', '/x/deno'))
            self.assertEqual(grab.find_js_runtime(which=lambda n: {'node': '/x/node'}.get(n), home='/vacio'), ('node', '/x/node'))
            self.assertIsNone(grab.find_js_runtime(which=lambda n: None, home='/vacio'))
        finally:
            grab.BIN_DIR = old_bin


class DoctorTests(unittest.TestCase):
    def test_version_age_and_upgrade_hint(self):
        import datetime
        self.assertEqual(doctor.version_age_days('2026.08.19', today=datetime.date(2026, 10, 10)), 52)
        self.assertIsNone(doctor.version_age_days('abc'))
        self.assertEqual(doctor.upgrade_hint('/Users/x/.local/share/uv/tools/yt-dlp/bin/yt-dlp'), 'uv tool upgrade yt-dlp')
        self.assertIn('pip install -U yt-dlp', doctor.upgrade_hint('/usr/bin/yt-dlp'))

    def test_latest_version_parsing(self):
        self.assertEqual(doctor.latest_ytdlp(fetch=lambda url: json.dumps({'tag_name': '2026.09.01'}).encode()), '2026.09.01')


class UrlTests(unittest.TestCase):
    def test_same_video_any_shape_is_one_key(self):
        keys = {inbox.normalize(u)[0] for u in (
            'https://youtu.be/sLOj0YS1KVg?si=abc', 'https://www.youtube.com/watch?v=sLOj0YS1KVg&feature=share&t=30',
            'https://m.youtube.com/watch?v=sLOj0YS1KVg')}
        self.assertEqual(keys, {'youtube:sLOj0YS1KVg'})
        self.assertEqual(inbox.normalize('https://youtu.be/sLOj0YS1KVg?si=abc')[1], 'https://www.youtube.com/watch?v=sLOj0YS1KVg')

    def test_shorts_instagram_tiktok(self):
        self.assertEqual(inbox.normalize('https://www.youtube.com/shorts/AbC123xyz_-?feature=share')[0], 'youtube:AbC123xyz_-')
        self.assertEqual(inbox.normalize('https://www.instagram.com/reel/DaRiZYuCKJb/?igsh=abc')[0], 'instagram:DaRiZYuCKJb')
        self.assertEqual(inbox.normalize('https://www.instagram.com/agustinbadt/reel/DaRiZYuCKJb/')[0], 'instagram:DaRiZYuCKJb')
        self.assertEqual(inbox.normalize('https://www.tiktok.com/@user/video/7300000000000000000?is_from_webapp=1')[0], 'tiktok:7300000000000000000')

    def test_other_sites_drop_tracking_only(self):
        key, clean = inbox.normalize('https://www.loom.com/share/abc123?utm_source=x&sid=9')
        self.assertEqual(clean, 'https://www.loom.com/share/abc123?sid=9')
        self.assertNotIn('utm', key)

    def test_extract_urls(self):
        text = 'mira esto: https://youtu.be/abc, y también (https://x.com/p?a=1). https://youtu.be/abc'
        self.assertEqual(inbox.extract_urls(text), ['https://youtu.be/abc', 'https://x.com/p?a=1'])


class InboxFlowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / 'buzon'
        inbox.init(self.dir)

    def tearDown(self):
        self.tmp.cleanup()

    def test_init_is_idempotent_and_keeps_user_links(self):
        (self.dir / inbox.LINKS).write_text('https://youtu.be/abc\n', encoding='utf-8')
        inbox.init(self.dir)
        self.assertEqual((self.dir / inbox.LINKS).read_text(encoding='utf-8'), 'https://youtu.be/abc\n')
        self.assertTrue((self.dir / inbox.VIDEOS).is_dir())

    def test_scan_dedupes_and_waits_for_synced_files(self):
        (self.dir / inbox.LINKS).write_text('https://youtu.be/AAA?si=1\nhttps://www.youtube.com/watch?v=AAA\nhttps://youtu.be/BBB\n', encoding='utf-8')
        video = self.dir / inbox.VIDEOS / 'clip.mp4'
        video.write_bytes(b'x' * 10)
        (self.dir / inbox.VIDEOS / '.oculto.mp4').write_bytes(b'x')
        (self.dir / inbox.VIDEOS / 'notas.txt').write_text('no es video')
        state = inbox.load_state(self.dir)
        new = inbox.scan(self.dir, state)                      # el archivo es muy reciente: aún no
        self.assertEqual(sorted(new), ['youtube:AAA', 'youtube:BBB'])
        later = os.path.getmtime(video) + 120
        new2 = inbox.scan(self.dir, state, clock=later)
        self.assertEqual(len(new2), 1)
        self.assertTrue(new2[0].startswith('archivo:clip.mp4:'))
        self.assertEqual(inbox.scan(self.dir, state, clock=later), [])      # nada se repite

    def test_prepare_marks_ready_partial_and_failed_with_cause(self):
        state = {'items': {
            'a': {'url': 'u-ok', 'estado': 'pendiente', 'desde': '1', 'intentos': 0},
            'b': {'url': 'u-parcial', 'estado': 'pendiente', 'desde': '2', 'intentos': 0},
            'c': {'url': 'u-login', 'estado': 'pendiente', 'desde': '3', 'intentos': 0}}}
        answers = {
            'u-ok': {'code': 0, 'text': 'INFORME: /w/a/informe.md'},
            'u-parcial': {'code': 2, 'text': 'INFORME: /w/b/informe.md'},
            'u-login': {'code': 1, 'text': 'No se pudo descargar.\nCAUSA[login]: Pide sesión.\nHAZ: Guárdalo en Para analizar.'}}
        inbox.prepare(state, runner=lambda s: answers[s], log=lambda *_: None)
        it = state['items']
        self.assertEqual((it['a']['estado'], it['a']['carpeta']), ('listo', '/w/a'))
        self.assertEqual(it['b']['estado'], 'parcial')
        self.assertEqual((it['c']['estado'], it['c']['codigo'], it['c']['haz']), ('fallo', 'login', 'Guárdalo en Para analizar.'))

    def test_only_transient_failures_are_retried_and_not_forever(self):
        fail429 = {'url': 'u', 'estado': 'fallo', 'codigo': '429', 'intentos': 1}
        self.assertTrue(inbox.eligible(fail429))
        self.assertFalse(inbox.eligible(dict(fail429, intentos=3)))
        self.assertFalse(inbox.eligible({'url': 'u', 'estado': 'fallo', 'codigo': 'login', 'intentos': 1}))
        self.assertFalse(inbox.eligible({'url': 'u', 'estado': 'aprendido'}))
        self.assertFalse(inbox.eligible({'url': 'u', 'estado': 'listo'}))

    def test_limit_and_timeout_and_unknown_failure(self):
        state = {'items': {str(i): {'url': 'u%d' % i, 'estado': 'pendiente', 'desde': str(i), 'intentos': 0} for i in range(4)}}
        done = inbox.prepare(state, limit=2, runner=lambda s: {'code': 1, 'text': 'algo\nextraño'}, log=lambda *_: None)
        self.assertEqual(done, ['0', '1'])
        self.assertEqual(state['items']['0']['codigo'], 'desconocido')
        self.assertIn('extraño', state['items']['0']['causa'])
        self.assertEqual(state['items']['3']['estado'], 'pendiente')

    def test_done_requeue_and_estado_md(self):
        state = {'items': {'youtube:AAA': {'url': 'https://www.youtube.com/watch?v=AAA', 'estado': 'listo', 'desde': '1', 'intentos': 1, 'informe': '/w/i.md'},
                           'youtube:BBB': {'url': 'https://www.youtube.com/watch?v=BBB', 'estado': 'fallo', 'desde': '2', 'intentos': 1,
                                           'codigo': 'login', 'causa': 'Pide sesión.', 'haz': 'Guárdalo.'}}}
        self.assertEqual(inbox.mark_done(state, 'https://youtu.be/AAA?si=zzz', ['diseno-grafico'], 'library/x.md'), 'youtube:AAA')
        self.assertEqual(state['items']['youtube:AAA']['estado'], 'aprendido')
        self.assertIsNone(inbox.mark_done(state, 'https://youtu.be/NOEXISTE'))
        md = inbox.estado_md(state)
        self.assertIn('Profesores: diseno-grafico', md)
        self.assertIn('Pide sesión. Qué hacer: Guárdalo.', md)
        self.assertEqual(inbox.requeue(state, 'https://youtu.be/BBB'), 'youtube:BBB')
        self.assertEqual((state['items']['youtube:BBB']['estado'], 'causa' in state['items']['youtube:BBB']), ('pendiente', False))

    def test_state_roundtrip_is_atomic_and_readable(self):
        state = {'items': {'k': {'url': 'u', 'estado': 'pendiente'}}}
        inbox.save_state(self.dir, state)
        self.assertEqual(inbox.load_state(self.dir), state)
        self.assertEqual([p.name for p in self.dir.iterdir() if p.name.endswith('.tmp')], [])

    def test_cli_run_and_ready(self):
        import subprocess
        (self.dir / inbox.LINKS).write_text('https://youtu.be/AAA\n', encoding='utf-8')
        state = inbox.load_state(self.dir)
        inbox.scan(self.dir, state)
        state['items']['youtube:AAA'].update(estado='listo', informe='/w/informe.md')
        inbox.save_state(self.dir, state)
        r = subprocess.run([sys.executable, str(ROOT / 'skills/mukiwa-learn/scripts/inbox.py'), '--dir', str(self.dir), 'ready', '--json'],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual([d['clave'] for d in data], ['youtube:AAA'])


if __name__ == '__main__':
    unittest.main()
