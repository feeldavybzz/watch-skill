#!/usr/bin/env python3
"""Empaqueta las skills como archivos .skill listos para subir a claude.ai
(Configuración → Capacidades → Skills → Subir).

Uso: python3 tools/build_skills.py [--out dist] [--allow-dirty]
Genera dist/mukiwa-grab.skill y dist/mukiwa-learn.skill.

- Solo entra lo que Git conoce (git ls-files): nada de _descargas/, work/, ._*, venv ni claves.
- mukiwa-learn lleva una copia de grab.py en scripts/ para descargar aunque se suba sola.
- La biblioteca de lecciones viaja dentro de mukiwa-learn.
- Se comprueba: una sola carpeta raíz, un solo SKILL.md, frontmatter válido y menos de 200 archivos.

En claude.ai el entorno suele bloquear YouTube/Instagram: ahí conviene subir el archivo de video.
Idea tomada de Watch (bradautomates/claude-video, build-skill.sh, MIT)."""
import argparse, os, re, subprocess, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ["mukiwa-grab", "mukiwa-learn"]
EXTRA = {"mukiwa-learn": {"scripts/grab.py": "skills/mukiwa-grab/scripts/grab.py"}}
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
MAX_FILES = 200


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def frontmatter_keys(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: raise SystemExit("SKILL.md sin frontmatter (--- ... ---)")
    return {line.split(":", 1)[0].strip() for line in m.group(1).splitlines() if re.match(r"^[\w-]+:", line)}


def build(name, out):
    files = [f for f in git("ls-files", "-z", f"skills/{name}").split("\0") if f]
    files = [f for f in files if not Path(f).name.startswith(".")]
    entries = {f[len(f"skills/{name}/"):]: ROOT / f for f in files}
    for arc, src in EXTRA.get(name, {}).items(): entries[arc] = ROOT / src
    if list(entries).count("SKILL.md") != 1 or sum(1 for a in entries if a.endswith("SKILL.md")) != 1:
        raise SystemExit(f"{name}: debe haber exactamente un SKILL.md")
    keys = frontmatter_keys((ROOT / f"skills/{name}/SKILL.md").read_text(encoding="utf-8"))
    if not {"name", "description"} <= keys or keys - ALLOWED_KEYS:
        raise SystemExit(f"{name}: frontmatter con claves no válidas para claude.ai: {sorted(keys - ALLOWED_KEYS)}")
    if len(entries) > MAX_FILES:
        raise SystemExit(f"{name}: {len(entries)} archivos (máximo {MAX_FILES})")
    out.mkdir(parents=True, exist_ok=True)
    dst = out / f"{name}.skill"
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, src in sorted(entries.items()):
            info = zipfile.ZipInfo(f"{name}/{arc}", date_time=(2026, 1, 1, 0, 0, 0))
            info.external_attr = (0o755 if os.access(src, os.X_OK) else 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, src.read_bytes())
    return dst, len(entries)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--allow-dirty", action="store_true", help="empaquetar aunque haya cambios sin commit")
    a = ap.parse_args()
    dirty = git("status", "--porcelain", "--untracked-files=no", "skills/").strip()
    if dirty and not a.allow_dirty:
        sys.exit("Hay cambios sin commit en skills/: haz commit antes de empaquetar (o usa --allow-dirty).\n" + dirty)
    for name in SKILLS:
        dst, n = build(name, Path(a.out))
        print(f"OK {dst} — {n} archivos, {dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
