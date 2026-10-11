import math, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "profes", "composicion-visual", "scripts"))
import guias  # noqa: E402


class GuiasTests(unittest.TestCase):
    def test_todo_dentro_del_cuadro_en_todos_los_formatos(self):
        for n in guias.GUIAS:
            for f in guias.FORMATOS:
                r = guias.resolver(n, f)
                self.assertTrue(r["primitivas"], (n, f))
                for p in r["primitivas"]:
                    for q in ([p["p"]] if p["t"] == "dot" else p["p"]):
                        self.assertTrue(-0.001 <= q[0] <= 1.001 and -0.001 <= q[1] <= 1.001, (n, f, q))

    def test_tercios_y_aurea(self):
        r = guias.resolver("tercios", "9:16")["primitivas"]
        self.assertAlmostEqual(r[0]["p"][0][0], 1 / 3)
        a = guias.resolver("rejilla_aurea", "16:9")["primitivas"]
        self.assertAlmostEqual(a[0]["p"][0][0], 0.382, places=3)

    def test_reglas_de_vertical(self):
        self.assertEqual(guias.resolver("yuxtaposicion", "16:9")["meta"]["eje"], "vertical")
        self.assertEqual(guias.resolver("yuxtaposicion", "9:16")["meta"]["eje"], "horizontal")
        self.assertAlmostEqual(guias.resolver("punto_de_fuga", "9:16")["meta"]["punto"][1], 0.382, places=3)
        self.assertEqual(guias.resolver("punto_de_fuga", "16:9")["meta"]["punto"][1], 0.5)
        # el ángulo de la diagonal cambia con la proporción
        a169 = guias.resolver("triangulos", "16:9")["meta"]["angulo_diagonal_grados"]
        a916 = guias.resolver("triangulos", "9:16")["meta"]["angulo_diagonal_grados"]
        self.assertAlmostEqual(a169, 29.4, delta=0.2); self.assertAlmostEqual(a916, 60.6, delta=0.2)

    def test_espiral_modo_y_orientacion(self):
        m = lambda f: guias.resolver("espiral_aurea", f)["meta"]["modo"]
        self.assertEqual([m("16:9"), m("3:2"), m("9:16")], ["estirada"] * 3)
        self.assertEqual([m("1:1"), m("5:4"), m("4:5")], ["proporcional"] * 3)
        # el ojo de la espiral cae dentro del cuadro y cerca de la esquina inferior izquierda en horizontal
        ojo = guias.resolver("espiral_aurea", "3:2")["meta"]["ojo"]
        self.assertLess(ojo[0], 0.5); self.assertGreater(ojo[1], 0.5)

    def test_marco_vertical_con_margen_igual_en_pixeles(self):
        r = guias.resolver("marco_en_el_marco", "9:16")
        pts = r["primitivas"][0]["p"]
        w, h = r["ancho"], r["alto"]
        self.assertAlmostEqual(pts[0][0] * w, pts[0][1] * h, delta=0.5)

    def test_svg_valido(self):
        s = guias.svg(guias.resolver("centrado", "4:5"))
        self.assertTrue(s.startswith("<svg") and s.rstrip().endswith("</svg>"))


if __name__ == "__main__":
    unittest.main()
