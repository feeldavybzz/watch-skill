#!/usr/bin/env python3
"""Sube cada semana las skills de MUKIWA a Google Drive (vía Google Drive para escritorio).

  python3 tools/sync_drive.py [--dest CARPETA] [--no-git]

1. Trae lo último de GitHub (solo si estás en main sin cambios pendientes; nunca fuerza nada).
2. Empaqueta mukiwa-grab, mukiwa-learn y cada profesor (tools/build_skills.py), incluyendo lo
   aprendido esta semana aunque no esté en un commit.
3. Empaqueta también las skills propias de ~/.claude/skills (carpetas reales, no enlaces).
4. Copia los .skill a la carpeta de Drive solo si cambiaron; los que ya no existen (p. ej. un
   profesor renombrado) se mueven a _retiradas/ en vez de borrarse.
5. Escribe LEEME.md con la fecha, la lista y cómo instalarlas.
Lo ejecuta cada lunes a las 9:08 la tarea programada de la app de Claude
"mukiwa-skills-drive-semanal" (necesita la app abierta; si estaba cerrada, corre al abrirla).
No usa launchd: macOS no deja a procesos en segundo plano leer el disco externo sin darle
"Acceso total al disco" a Python."""
import argparse, datetime, glob, io, os, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
USER_SKILLS = Path.home() / ".claude" / "skills"
FOLDER = "MUKIWA · Skills de Claude"


def log(msg):
    print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M}] {msg}", flush=True)


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


def default_dest():
    found = glob.glob(str(Path.home() / "Library/CloudStorage/GoogleDrive-*" / "Mi unidad" / FOLDER)) + \
            glob.glob(str(Path.home() / "Library/CloudStorage/GoogleDrive-*" / "My Drive" / FOLDER))
    return Path(found[0]) if found else None


def update_repo():
    if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != "main":
        log("git: no estás en main; se empaqueta lo que hay sin actualizar."); return
    if git("status", "--porcelain", "--untracked-files=no").stdout.strip():
        log("git: hay cambios sin commit; se empaqueta lo que hay sin actualizar."); return
    if git("fetch", "-q", "origin").returncode != 0:
        log("git: sin conexión con GitHub; se empaqueta la copia local."); return
    r = git("merge", "-q", "--ff-only", "origin/main")
    log("git: main actualizado desde GitHub." if r.returncode == 0 else "git: no se pudo avanzar main (" + r.stderr.strip()[:200] + ")")


def zip_skill_dir(src, dst):
    """Skill propia (carpeta real) -> .skill con una sola carpeta raíz, sin ocultos ni ._*."""
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src.rglob("*")):
            rel = p.relative_to(src)
            if p.is_dir() or any(part.startswith(".") or part == "__pycache__" for part in rel.parts): continue
            info = zipfile.ZipInfo(f"{src.name}/{rel.as_posix()}", date_time=(2026, 1, 1, 0, 0, 0))
            info.external_attr = (0o755 if os.access(p, os.X_OK) else 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, p.read_bytes())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dest"); ap.add_argument("--no-git", action="store_true")
    a = ap.parse_args()
    dest = Path(a.dest) if a.dest else default_dest()
    if not dest or not dest.parent.exists():
        log("ERROR: no encuentro la carpeta de Google Drive. ¿Está abierta la app Google Drive para escritorio?"); return 2
    dest.mkdir(exist_ok=True)
    if not a.no_git: update_repo()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        r = subprocess.run([sys.executable, "-I", str(ROOT / "tools/build_skills.py"), "--out", str(tmp), "--allow-dirty"],
                           capture_output=True, text=True)
        if r.returncode: log("ERROR al empaquetar: " + (r.stderr or r.stdout).strip()[-400:]); return 1
        own = []
        for d in sorted(USER_SKILLS.iterdir()) if USER_SKILLS.exists() else []:
            if d.is_dir() and not d.is_symlink() and (d / "SKILL.md").exists():
                zip_skill_dir(d, tmp / f"{d.name}.skill"); own.append(d.name)
        new = sorted(p.name for p in tmp.glob("*.skill"))
        changed = []
        for name in new:
            src, dst = tmp / name, dest / name
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                shutil.copyfile(src, dst); changed.append(name)
        retired = []
        for old in sorted(dest.glob("*.skill")):
            if old.name not in new:
                (dest / "_retiradas").mkdir(exist_ok=True)
                shutil.move(str(old), str(dest / "_retiradas" / old.name)); retired.append(old.name)
    profes = (ROOT / "profes" / "INDEX.md").read_text(encoding="utf-8") if (ROOT / "profes" / "INDEX.md").exists() else ""
    lines = [f"# Skills de Claude · MUKIWA", "", f"Actualizado: {datetime.date.today().isoformat()} (cada lunes, automático).", "",
             "## Archivos", ""] + [f"- `{n}`" + (" — skill propia" if n[:-6] in own else "") for n in new] + [
             "", "## Cómo instalarlas", "",
             "- **claude.ai (app de Claude):** Configuración → Capacidades → Skills → Subir el `.skill`.",
             "- **Claude Code:** descomprimir el `.skill` dentro de `~/.claude/skills/`.", "",
             "Los profesores (`profe-*`) crecen con cada video que se analiza con mukiwa-learn.", ""]
    if profes: lines += ["## Estado de los profesores", ""] + profes.splitlines()[2:]
    text = "\n".join(lines) + "\n"
    readme = dest / "LEEME.md"
    if not readme.exists() or readme.read_text(encoding="utf-8") != text: readme.write_text(text, encoding="utf-8")
    log(f"OK {len(new)} skills en {dest} · cambiadas: {', '.join(changed) or 'ninguna'}"
        + (f" · retiradas: {', '.join(retired)}" if retired else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
