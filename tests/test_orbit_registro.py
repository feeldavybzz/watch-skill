import os, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "kiwa-orbit" / "scripts" / "orbit_registro.py"

class OrbitRegistro(unittest.TestCase):
    def run_cli(self, reg, *args):
        env = dict(os.environ, ORBIT_REGISTRO=str(reg))
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, env=env).stdout.strip()

    def test_nuevo_agregar_y_ver(self):
        with tempfile.TemporaryDirectory() as d:
            reg = Path(d) / "sub" / "r.jsonl"
            self.assertEqual(self.run_cli(reg, "seen", "--id", "a1"), "NUEVO")
            self.run_cli(reg, "add", "--id", "a1", "--antes", "x", "--despues", "Y · Z", "--estado", "verificado")
            self.assertIn('"estado": "verificado"', self.run_cli(reg, "seen", "--id", "a1"))
            self.assertIn("Y · Z", self.run_cli(reg, "list", "--estado", "verificado"))
            self.assertEqual(self.run_cli(reg, "list", "--estado", "pendiente"), "")

if __name__ == "__main__":
    unittest.main()
