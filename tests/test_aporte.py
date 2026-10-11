import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "mukiwa-learn", "scripts"))
import aporte  # noqa: E402

DESC_PROMO = """👉 Accede a la Lista de espera: https://comunidad.somoscamaleon.com/

Sígueme en IG: https://www.instagram.com/meliwhite_8/
Aprende a editar con IA.
"""
DESC_OPEN = """📁 Accede a la skill aquí: https://github.com/bradautomates/claude-video
📈 Escala tu Agencia: https://tally.so/r/abc?utm_source=yt
Repetido: https://github.com/bradautomates/claude-video
"""


def transcript(minutes_promo, total):
    lines = []
    for m in range(total):
        text = "suscríbete a la comunidad, únete a la lista de espera y mira el precio del curso" \
            if m in minutes_promo else "ahora cortamos el silencio y exportamos el video en la línea de tiempo"
        lines.append(f"[00:{m:02d}:05.00] {text}")
    return "\n".join(lines)


class AporteTests(unittest.TestCase):
    def test_links_clasificados_y_sin_repetidos(self):
        k = {l["url"]: l["kind"] for l in aporte.extract_links(DESC_PROMO)}
        self.assertEqual(k["https://comunidad.somoscamaleon.com/"], "comunidad/venta")
        self.assertEqual(k["https://www.instagram.com/meliwhite_8/"], "red social")
        links = aporte.extract_links(DESC_OPEN)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0]["kind"], "recurso")
        self.assertEqual(links[1]["kind"], "comunidad/venta")

    def test_cola_de_promocion(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "t.md"); open(p, "w").write(transcript(range(14, 20), 20))
            r = aporte.promo_minutes(aporte.read_segments(p), threshold=3)
            self.assertEqual(r["cola_desde_min"], 14)
            self.assertEqual(r["minutos_promo"], 6)

    def test_veredictos(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "t.md"); open(p, "w").write(transcript(range(14, 20), 20))
            chapters = [{"title": "Instalación", "start_time": 0, "end_time": 840},
                        {"title": "Cómo obtener los recursos gratuitos", "start_time": 840, "end_time": 1200}]
            malo = aporte.verdict({"description": DESC_PROMO, "chapters": chapters, "duration": 1200}, p)
            self.assertIn(malo["nivel"], ("aporta poco", "no aporta"))
            self.assertTrue(malo["recurso_tras_registro"])
            self.assertIn("buscar otro", malo["recomendacion"] + "buscar otro")
            q = os.path.join(d, "q.md"); open(q, "w").write(transcript([], 20))
            bueno = aporte.verdict({"description": DESC_OPEN, "duration": 1200}, q)
            self.assertEqual(bueno["nivel"], "aporta")
            self.assertFalse(bueno["recurso_tras_registro"])

    def test_sin_datos_no_falla(self):
        v = aporte.verdict({}, None)
        self.assertEqual(v["nivel"], "aporta")
        self.assertTrue(aporte.markdown(v))


if __name__ == "__main__":
    unittest.main()
