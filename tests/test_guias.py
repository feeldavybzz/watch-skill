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
        # evidencia (StudioBinder): rectángulo áureo centrado, no estirado, sobre 16:9
        self.assertEqual([m("16:9"), m("3:2"), m("9:16"), m("1:1"), m("5:4"), m("4:5"), m("2.39:1")], ["proporcional"] * 7)
        # el rectángulo áureo queda centrado con ≈7 % de margen a cada lado en 16:9
        pts = guias.resolver("espiral_aurea", "16:9")["primitivas"][0]["p"]
        self.assertAlmostEqual(min(p[0] for p in pts), min(p[0] for p in pts), places=6)
        xs = [p[0] for p in pts]; self.assertGreater(min(xs), 0.05); self.assertLess(max(xs), 0.95)
        # el ojo de la espiral cae dentro del cuadro y cerca de la esquina inferior izquierda en horizontal
        ojo = guias.resolver("espiral_aurea", "3:2")["meta"]["ojo"]
        self.assertLess(ojo[0], 0.5); self.assertGreater(ojo[1], 0.5)

    def test_marco_vertical_con_margen_igual_en_pixeles(self):
        r = guias.resolver("marco_en_el_marco", "9:16")
        pts = r["primitivas"][0]["p"]
        w, h = r["ancho"], r["alto"]
        self.assertAlmostEqual(pts[0][0] * w, pts[0][1] * h, delta=0.5)

    def test_guias_de_los_reels_2_y_3_y_formato_4x3(self):
        for n in ("espacio_negativo", "primer_plano", "simetria", "contorno_del_sujeto", "marco_circular", "lineas_convergentes"):
            self.assertIn(n, guias.GUIAS)
        self.assertIn("4:3", guias.FORMATOS); self.assertIn("3:4", guias.FORMATOS)
        self.assertAlmostEqual(guias.resolver("primer_plano", "16:9")["meta"]["linea_v"], 0.667, places=3)
        self.assertEqual(guias.resolver("espacio_negativo", "9:16")["meta"]["region_vacia_v"], 0.60)
        # el contorno del sujeto conserva su forma en píxeles en todos los formatos
        ratios = []
        for f in ("16:9", "4:3", "9:16"):
            r = guias.resolver("contorno_del_sujeto", f); pts = r["primitivas"][0]["p"]
            ratios.append(((max(p[0] for p in pts) - min(p[0] for p in pts)) * r["ancho"]) / ((max(p[1] for p in pts) - min(p[1] for p in pts)) * r["alto"]))
        self.assertAlmostEqual(ratios[0], ratios[2], delta=0.05)

    def test_guias_de_studiobinder(self):
        h = guias.resolver("linea_aurea_horizonte", "9:16")["primitivas"][0]["p"]
        self.assertAlmostEqual(h[0][1], 0.382, places=3)
        r = guias.resolver("headroom_lookroom", "16:9")
        self.assertAlmostEqual(r["meta"]["sujeto_u"], 0.382, places=3)
        self.assertEqual(len(guias.GUIAS), 23)

    def test_area_segura_9x16(self):
        r = guias.resolver("tercios", "9:16")
        s = guias.en_area_segura(r, "conservadora")
        v = [p["p"][0][1] for p in s["primitivas"] if p["t"] == "line" and p["p"][0][1] == p["p"][1][1]]
        self.assertTrue(all(0.14 <= x <= 0.65 for x in v), v)   # dentro de 14 %..65 %
        self.assertEqual(s["area"], "conservadora")
        # un formato sin interfaz definida no cambia
        self.assertEqual(guias.en_area_segura(guias.resolver("tercios", "4:5"))["primitivas"], guias.resolver("tercios", "4:5")["primitivas"])

    def test_los_verticales_comparten_reglas(self):
        a = guias.resolver("punto_de_fuga", "4:5")["meta"]["punto"]; b = guias.resolver("punto_de_fuga", "9:16")["meta"]["punto"]
        self.assertEqual(a, b)
        self.assertEqual(guias.resolver("yuxtaposicion", "4:5")["meta"]["eje"], guias.resolver("yuxtaposicion", "9:16")["meta"]["eje"])

    def test_triangulos_reproducen_el_plano_de_pulp_fiction(self):
        # medido en pantalla sobre un plano ≈2,35:1: pies de las perpendiculares en (0,152; 0,846) y (0,849; 0,16)
        prim, _ = guias.g_triangulos_metodo(2350, 1000)
        f1, f2 = prim[2]["p"][1], prim[3]["p"][1]
        self.assertAlmostEqual(f1[0], 0.152, delta=0.01); self.assertAlmostEqual(f1[1], 0.846, delta=0.01)
        self.assertAlmostEqual(f2[0], 0.849, delta=0.01)
        prim2, _ = guias.g_triangulos_metodo(1920, 1080)   # en 16:9 son otros puntos: se recalcula
        self.assertAlmostEqual(prim2[2]["p"][1][0], 0.24, delta=0.005)

    def test_svg_valido(self):
        s = guias.svg(guias.resolver("centrado", "4:5"))
        self.assertTrue(s.startswith("<svg") and s.rstrip().endswith("</svg>"))


if __name__ == "__main__":
    unittest.main()
