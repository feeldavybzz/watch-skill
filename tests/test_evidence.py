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

    def test_youtube_rolling_captions(self):
        # Formato real de los .srt automáticos de YouTube: renglón en cascada, bloques de 10 ms
        # que sostienen el texto y una línea en blanco tras el tiempo en el primer bloque.
        value = ('1\n00:00:00,040 --> 00:00:02,030\n\nParecía que ya no\n\n'
                 '2\n00:00:02,030 --> 00:00:02,040\nParecía que ya no\n \n\n'
                 '3\n00:00:02,040 --> 00:00:03,350\nParecía que ya no\nnos podía sorprender\n\n'
                 '4\n00:00:03,350 --> 00:00:03,360\nnos podía sorprender\n \n\n'
                 '5\n00:00:03,360 --> 00:00:05,309\nnos podía sorprender\npero ahora sí\n')
        self.assertEqual(ingest.from_srt_vtt(value), [
            (0.04, 'Parecía que ya no'), (2.04, 'nos podía sorprender'), (3.36, 'pero ahora sí')])

    def test_rolling_keeps_single_word_repetition(self):
        value = ('00:00:01.000 --> 00:00:02.000\nDijo que sí\n\n'
                 '00:00:02.000 --> 00:00:03.000\nsí, claro\n')
        self.assertEqual(ingest.from_srt_vtt(value), [(1.0, 'Dijo que sí'), (2.0, 'sí, claro')])

    def test_vtt_cue_id_not_merged_into_previous_text(self):
        value = 'WEBVTT\n\nintro\n00:00:00.000 --> 00:00:01.000\nHola\n\nsegundo\n00:00:01.000 --> 00:00:02.000\nmundo\n'
        self.assertEqual(ingest.from_srt_vtt(value), [(0.0, 'Hola'), (1.0, 'mundo')])

    def test_save_lesson_ignores_macos_metadata_files(self):
        with tempfile.TemporaryDirectory() as d:
            lib = Path(d) / 'library'
            (lib / 'motion-edicion').mkdir(parents=True)
            (lib / 'motion-edicion/._vieja.md').write_bytes(b'\x00\x05\x16\x07\x00\x02\xb0\x00')
            (lib / '._motion-edicion').write_bytes(b'\x00\x05\x16\x07')
            lesson = Path(d) / 'nueva.md'
            lesson.write_text('# Nueva\n> Una línea\n', encoding='utf-8')
            r = subprocess.run([sys.executable, str(SCRIPTS / 'save_lesson.py'), '--library', str(lib),
                                '--topic', 'motion-edicion', '--slug', 'nueva', '--file', str(lesson)],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            index = (lib / 'INDEX.md').read_text(encoding='utf-8')
            self.assertIn('[Nueva](motion-edicion/nueva.md) — Una línea', index)
            self.assertNotIn('._', index)

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


class DescargaOkTests(unittest.TestCase):
    def setUp(self):
        import os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "mukiwa-grab", "scripts"))
        import grab
        self.g = grab

    def test_miniatura_y_subtitulos_solos_no_son_exito_si_se_pidio_video(self):
        files = ["video.jpg", "video.en-US.srt", "video.info.json", "subtitulos.json"]
        self.assertFalse(self.g.descarga_ok(files, subs_only=False, video_esperado=True))

    def test_con_video_es_exito(self):
        self.assertTrue(self.g.descarga_ok(["video.mp4", "video.jpg"], False, True))

    def test_carrusel_de_fotos_es_exito(self):
        self.assertTrue(self.g.descarga_ok(["fotos/a.jpg", "fotos/b.jpg"], False, True))

    def test_solo_subtitulos_es_exito_en_su_modo(self):
        self.assertTrue(self.g.descarga_ok(["video.en.srt", "video.info.json"], True, False))

    def test_foto_directa_sin_video_esperado(self):
        self.assertTrue(self.g.descarga_ok(["foto.jpg"], False, False))


class VideoRealTests(unittest.TestCase):
    def _carpeta(self, nombres):
        import os, tempfile
        d = tempfile.mkdtemp()
        for n in nombres: open(os.path.join(d, n), "w").write("x")
        return d

    def test_la_miniatura_nunca_es_video(self):
        import os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "mukiwa-grab", "scripts"))
        import grab
        d = self._carpeta(["video.jpg", "video.webp", "video.png", "video.en.srt", "video.info.json"])
        self.assertIsNone(grab.video_en(d))

    def test_reconoce_cualquier_extension_de_video(self):
        import os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "mukiwa-grab", "scripts"))
        import grab
        for ext in (".mp4", ".mkv", ".webm", ".mov", ".m4v"):
            d = self._carpeta(["video" + ext, "video.jpg"])
            self.assertTrue(grab.video_en(d).endswith("video" + ext), ext)

    def test_prefiere_mp4_e_ignora_appledouble(self):
        import os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "mukiwa-grab", "scripts"))
        import grab
        d = self._carpeta(["._video.mp4", "video.mkv", "video.mp4", "video.jpg"])
        self.assertTrue(grab.video_en(d).endswith("video.mp4"))
        d2 = self._carpeta(["._video.mkv", "video.jpg"])
        self.assertIsNone(grab.video_en(d2))

    def test_watch_usa_el_mismo_criterio(self):
        import os, importlib.util
        spec = importlib.util.spec_from_file_location("watch_t", os.path.join(os.path.dirname(__file__), "..", "skills", "mukiwa-learn", "scripts", "watch.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        d = self._carpeta(["video.jpg", "video.info.json"]); self.assertIsNone(m.find_video(d))
        d = self._carpeta(["video.webm", "video.jpg"]); self.assertTrue(m.find_video(d).endswith("video.webm"))
