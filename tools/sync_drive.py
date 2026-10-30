#!/usr/bin/env python3
"""Sube cada semana las skills de MUKIWA a Google Drive (vía Google Drive para escritorio).

  python3 tools/sync_drive.py [--dest CARPETA] [--no-git]

1. Trae lo último de GitHub (solo si estás en main sin cambios pendientes; nunca fuerza nada).
2. Empaqueta kiwa-watch-learn y cada profesor (tools/build_skills.py), incluyendo lo
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


CREADAS, AJENAS = "Skills by Mukiwa", "Global Skills"
GLOBAL_SRC = ROOT.parent / "Global Skills"   # .skill descargados de otros o que Claude trae por defecto (junto a watch-skill)


def default_icloud():
    base = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs"
    return base / FOLDER if base.exists() else None


def ajenas():
    f = ROOT / "tools" / "skills-de-otros.txt"
    if not f.exists(): return set()
    return {l.strip() for l in f.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")}


def sync_dest(dest, groups, text):
    """Copia a dest/<grupo>/ solo lo que cambió; lo que ya no existe va a _retiradas/ (no se borra)."""
    dest.mkdir(parents=True, exist_ok=True)
    changed, retired = [], []
    for folder, files in groups.items():
        sub = dest / folder; sub.mkdir(exist_ok=True)
        for src in files:
            dst = sub / src.name
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                shutil.copyfile(src, dst); changed.append(f"{folder}/{src.name}")
        names = {f.name for f in files}
        for old in sorted(sub.glob("*.skill")):
            if old.name not in names:
                (dest / "_retiradas").mkdir(exist_ok=True)
                shutil.move(str(old), str(dest / "_retiradas" / old.name)); retired.append(old.name)
    for old in sorted(dest.glob("*.skill")):      # archivos sueltos de la versión anterior (sin subcarpetas)
        (dest / "_retiradas").mkdir(exist_ok=True)
        shutil.move(str(old), str(dest / "_retiradas" / old.name)); retired.append(old.name)
    readme = dest / "LEEME.md"
    if not readme.exists() or readme.read_text(encoding="utf-8") != text: readme.write_text(text, encoding="utf-8")
    return changed, retired


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", help="carpeta de Google Drive (por defecto la detecta)")
    ap.add_argument("--icloud", nargs="?", const="auto", help="carpeta de iCloud Drive (sin valor: la detecta)")
    ap.add_argument("--no-git", action="store_true")
    a = ap.parse_args()
    dests = []
    gd = Path(a.dest) if a.dest else default_dest()
    if gd and gd.parent.exists(): dests.append(("Google Drive", gd))
    else: log("AVISO: no encuentro la carpeta de Google Drive (¿está abierta la app Google Drive para escritorio?).")
    ic = default_icloud() if a.icloud == "auto" or (a.icloud is None and not a.dest) else (Path(a.icloud) if a.icloud else None)
    if ic and ic.parent.exists(): dests.append(("iCloud Drive", ic))
    elif a.icloud: log("AVISO: no encuentro iCloud Drive.")
    if not dests:
        log("ERROR: no hay ninguna carpeta de destino."); return 2
    if not a.no_git: update_repo()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        r = subprocess.run([sys.executable, "-I", str(ROOT / "tools/build_skills.py"), "--out", str(tmp), "--allow-dirty"],
                           capture_output=True, text=True)
        if r.returncode: log("ERROR al empaquetar: " + (r.stderr or r.stdout).strip()[-400:]); return 1
        otras = ajenas(); own = []
        for d in sorted(USER_SKILLS.iterdir()) if USER_SKILLS.exists() else []:
            if d.is_dir() and not d.is_symlink() and (d / "SKILL.md").exists():
                zip_skill_dir(d, tmp / f"{d.name}.skill"); own.append(d.name)
        glob_src = {f.stem: f for f in sorted(GLOBAL_SRC.glob("*.skill")) if not f.name.startswith(".")} if GLOBAL_SRC.exists() else {}
        otras |= set(glob_src)
        allf = sorted(tmp.glob("*.skill"))
        propias = [f for f in allf if f.stem not in otras]
        ajenas_f = {f.stem: f for f in allf if f.stem in otras}
        for k, f in glob_src.items(): ajenas_f.setdefault(k, f)        # lo de ~/.claude/skills manda; si falta, el .skill ya hecho
        groups = {CREADAS: propias, AJENAS: [ajenas_f[k] for k in sorted(ajenas_f)]}
        allf = propias + groups[AJENAS]
        profes = (ROOT / "profes" / "INDEX.md").read_text(encoding="utf-8") if (ROOT / "profes" / "INDEX.md").exists() else ""
        lines = ["# Skills de Claude · MUKIWA", "", f"Actualizado: {datetime.date.today().isoformat()} (cada lunes, automático).", ""]
        for folder, files in groups.items():
            lines += [f"## {folder}", ""] + [f"- `{f.name}`" for f in files] + [""]
        lines += ["## Cómo instalarlas", "",
                  "- **claude.ai (app de Claude):** Configuración → Capacidades → Skills → Subir el `.skill`.",
                  "- **Claude Code:** descomprimir el `.skill` dentro de `~/.claude/skills/`.", "",
                  "Los profesores (`kiwa-<nicho>`) crecen con cada video que se analiza con kiwa-watch-learn.", ""]
        if profes: lines += ["## Estado de los profesores", ""] + profes.splitlines()[2:]
        text = "\n".join(lines) + "\n"
        for nombre, dest in dests:
            changed, retired = sync_dest(dest, groups, text)
            log(f"OK {nombre}: {len(allf)} skills en {dest} · cambiadas: {', '.join(changed) or 'ninguna'}"
                + (f" · retiradas: {', '.join(retired)}" if retired else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
