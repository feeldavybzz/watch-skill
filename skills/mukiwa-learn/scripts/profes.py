#!/usr/bin/env python3
"""Profesores MUKIWA: mini skills por nicho que crecen con cada video analizado.

Cada lección guardada se clasifica en uno o varios nichos (color grading, diseño de logos,
tipografía cinética...). Si el profesor del nicho existe, aprende más; si no, se crea. Si el
nicho ya lo cubre una skill propia de Bryan (p. ej. portfolio-marca-personal), se le añade
el conocimiento en vez de duplicarla.

  python3 profes.py list                         # profesores y skills existentes (para clasificar)
  python3 profes.py ensure --nicho color-grading --nombre "Color grading" \\
          --herramientas "DaVinci Resolve,Premiere Pro" --cuando "corregir color, gradear, crear un look, LUTs"
  python3 profes.py attach --nicho color-grading --leccion library/motion-edicion/x.md
  python3 profes.py attach --skill ~/.claude/skills/portfolio-marca-personal --leccion ...
  python3 profes.py install                      # enlaza profes/* en ~/.claude/skills/profe-*
  python3 profes.py check                        # valida formato y fuentes

El script arma la estructura, copia lecciones, lleva la cuenta y el índice. Fusionar el
conocimiento en las secciones del SKILL.md (en forma de instrucciones, sin repetir) lo hace el
agente siguiendo references/profesores.md."""
import argparse, datetime, os, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEARN = HERE.parent
REPO = LEARN.parents[1]
PROFES = Path(os.environ["MUKIWA_PROFES"]) if os.environ.get("MUKIWA_PROFES") else (
    REPO / "profes" if (REPO / "CLAUDE.md").exists() else Path.cwd() / "profes")
USER_SKILLS = Path.home() / ".claude" / "skills"
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
APRENDIDO = "## Aprendido de referencias (MUKIWA)"

TEMPLATE = """---
name: profe-{nicho}
description: Profesor MUKIWA de {nombre_l}{en_herr}. Sabe hacerlo paso a paso, con lo aprendido de referencias reales que Bryan fue enviando. Usar cuando Bryan pida {cuando}, o pregunte cómo se hace algo de {nombre_l}.
metadata:
  nicho: {nicho}
  herramientas: "{herramientas}"
  lecciones: 0
  actualizado: "{hoy}"
---

# Profe: {nombre}
> Qué sabe hacer este profesor, en una línea (se reescribe a medida que aprende).

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".

## Cómo trabajar
1. (procedimiento general, del primer paso a la entrega)

## Áreas
- (subtemas del oficio; cada técnica en su área)

## Por herramienta
{secciones}
## Recetas
- (técnicas concretas: objetivo → pasos → valores → cómo se ve bien)

## Errores comunes
- (error → por qué pasa → cómo evitarlo)

## Checklist antes de entregar
- [ ] …

## Para MUKIWA
- Cómo aplicarlo en Graphic Design / Visual Edits / Creative Direction.

## Dudas abiertas
- (contradicciones entre fuentes, cosas sin verificar)

## Fuentes
"""


def today():
    return datetime.date.today().isoformat()


def read(p):
    return Path(p).read_text(encoding="utf-8")


def write(p, text):
    Path(p).write_text(text, encoding="utf-8")


def meta(text, key):
    m = re.search(rf"^  {key}:\s*\"?(.*?)\"?\s*$", text, re.M)
    return m.group(1) if m else ""


def set_meta(text, key, value):
    val = f'"{value}"' if isinstance(value, str) else str(value)
    return re.sub(rf"^(  {key}:).*$", rf"\g<1> {val}", text, count=1, flags=re.M)


def description(text):
    m = re.search(r"^description:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def cmd_list(a):
    print("# Profesores MUKIWA\n")
    rows = sorted(PROFES.glob("*/SKILL.md")) if PROFES.exists() else []
    if not rows: print("(ninguno todavía)")
    for s in rows:
        t = read(s)
        print(f"- {s.parent.name} · herramientas: {meta(t, 'herramientas') or '—'} · lecciones: {meta(t, 'lecciones')} · "
              f"actualizado: {meta(t, 'actualizado')}\n  {description(t)[:220]}")
    print("\n# Otras skills de Bryan (si el nicho ya está cubierto, alimentar esa con attach --skill)\n")
    for s in sorted(USER_SKILLS.glob("*/SKILL.md")) if USER_SKILLS.exists() else []:
        if s.parent.name.startswith("profe-"): continue
        print(f"- {s.parent} \n  {description(read(s))[:220]}")


def cmd_ensure(a):
    if not SLUG.fullmatch(a.nicho): sys.exit("--nicho: minúsculas, números y guiones (ej. color-grading)")
    d = PROFES / a.nicho
    if (d / "SKILL.md").exists():
        print("Ya existe:", d / "SKILL.md"); return
    herr = [h.strip() for h in (a.herramientas or "").split(",") if h.strip()]
    secciones = "".join(f"### {h}\n- (pasos y ubicación de controles en {h})\n\n" for h in herr) or "- (general)\n\n"
    (d / "references" / "lecciones").mkdir(parents=True, exist_ok=True)
    write(d / "SKILL.md", TEMPLATE.format(
        nicho=a.nicho, nombre=a.nombre, nombre_l=a.nombre[0].lower() + a.nombre[1:],
        en_herr=(" en " + " y ".join(herr)) if herr else "", herramientas=", ".join(herr),
        cuando=a.cuando or a.nombre.lower(), hoy=today(), secciones=secciones))
    write_index()
    print("Creado:", d / "SKILL.md")


def lesson_info(path):
    t = read(path)
    title = (re.search(r"^# (.+)$", t, re.M) or [None, Path(path).stem])[1]
    src = re.search(r"\*\*Fuente\*\*:\s*(\S+)", t)
    return title, (src.group(1) if src else "")


def attach_to_profe(nicho, leccion):
    d = PROFES / nicho; skill = d / "SKILL.md"
    if not skill.exists(): sys.exit(f"No existe el profesor '{nicho}': créalo con ensure.")
    dst = d / "references" / "lecciones" / Path(leccion).name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(leccion, dst)
    t = read(skill)
    rel = f"references/lecciones/{dst.name}"
    if rel in t:
        print("La lección ya estaba en Fuentes; se actualizó la copia."); return skill
    n = len(re.findall(r"^- \[\d+\]", t, re.M)) + 1
    title, src = lesson_info(leccion)
    t = t.rstrip("\n") + f"\n- [{n}] {title} — {src} · `{rel}`\n"
    t = set_meta(set_meta(t, "lecciones", n), "actualizado", today())
    write(skill, t); write_index()
    print(f"OK [{n}] añadida a {skill}\nAhora fusiona lo aprendido en las secciones (references/profesores.md).")
    return skill


def attach_to_skill(skill_dir, leccion):
    skill_dir = Path(skill_dir).expanduser(); skill = skill_dir / "SKILL.md"
    if not skill.exists(): sys.exit(f"No hay SKILL.md en {skill_dir}")
    ref = skill_dir / "references" / "aprendido-mukiwa.md"
    ref.parent.mkdir(parents=True, exist_ok=True)
    title, src = lesson_info(leccion)
    body = ref.read_text(encoding="utf-8") if ref.exists() else (
        "# Aprendido de referencias (MUKIWA)\n\nConocimiento añadido desde videos analizados con mukiwa-learn. "
        "Instrucciones accionables por tema; fuente entre corchetes.\n\n## Fuentes\n")
    if src and src in body:
        print("Esta fuente ya estaba registrada en", ref); return skill
    n = len(re.findall(r"^- \[\d+\]", body, re.M)) + 1
    write(ref, body.rstrip("\n") + f"\n- [{n}] {title} — {src}\n")
    t = read(skill)
    if APRENDIDO not in t:   # una sola línea en la skill original; el contenido vive en references/
        write(skill, t.rstrip("\n") + f"\n\n{APRENDIDO}\nAntes de trabajar, leer `references/aprendido-mukiwa.md`: "
              "técnicas añadidas desde referencias en video que Bryan fue enviando.\n")
    print(f"OK [{n}] registrada en {ref}\nAhora escribe ahí lo aprendido como instrucciones (no reescribir la skill original).")
    return skill


def cmd_attach(a):
    if not Path(a.leccion).is_file(): sys.exit("No existe la lección: " + a.leccion)
    if bool(a.nicho) == bool(a.skill): sys.exit("Usa --nicho (profesor) o --skill (skill existente), uno de los dos.")
    attach_to_profe(a.nicho, a.leccion) if a.nicho else attach_to_skill(a.skill, a.leccion)


def cmd_install(a):
    USER_SKILLS.mkdir(parents=True, exist_ok=True); write_index()
    for d in sorted(p for p in PROFES.iterdir() if (p / "SKILL.md").exists()) if PROFES.exists() else []:
        link = USER_SKILLS / f"profe-{d.name}"
        if link.is_symlink():
            if link.resolve() == d.resolve(): print("ya instalado:", link); continue
            link.unlink()
        elif link.exists():
            print("OJO: existe una carpeta real en", link, "— no se toca"); continue
        link.symlink_to(d, target_is_directory=True)
        print("instalado:", link, "->", d)


def cmd_check(a):
    bad = 0
    for s in sorted(PROFES.glob("*/SKILL.md")) if PROFES.exists() else []:
        t = read(s); errs = []
        if not re.match(r"^---\nname: profe-[a-z0-9-]+\ndescription: .+\n", t): errs.append("frontmatter")
        if f"name: profe-{s.parent.name}\n" not in t: errs.append("name distinto a la carpeta")
        for rel in re.findall(r"`(references/[^`]+)`", t):
            if not (s.parent / rel).exists(): errs.append("falta " + rel)
        if len(t.splitlines()) > 500: errs.append("más de 500 líneas: mover recetas largas a references/")
        print(("OK " if not errs else "ERROR ") + s.parent.name + ("" if not errs else ": " + "; ".join(errs)))
        bad += bool(errs)
    sys.exit(1 if bad else 0)


def write_index():
    lines = ["# Profesores MUKIWA\n", "Mini skills por nicho que crecen con cada video analizado (ver "
             "skills/mukiwa-learn/references/profesores.md).\n"]
    for s in sorted(PROFES.glob("*/SKILL.md")):
        t = read(s)
        n = meta(t, "lecciones")
        lines.append(f"- **{s.parent.name}** — {n} {'lección' if n == '1' else 'lecciones'} · {meta(t, 'herramientas') or 'general'} · "
                     f"actualizado {meta(t, 'actualizado')}")
    write(PROFES / "INDEX.md", "\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list"); sub.add_parser("install"); sub.add_parser("check")
    e = sub.add_parser("ensure"); e.add_argument("--nicho", required=True); e.add_argument("--nombre", required=True)
    e.add_argument("--herramientas", default=""); e.add_argument("--cuando", default="")
    t = sub.add_parser("attach"); t.add_argument("--leccion", required=True)
    t.add_argument("--nicho"); t.add_argument("--skill")
    a = ap.parse_args()
    PROFES.mkdir(parents=True, exist_ok=True)
    {"list": cmd_list, "ensure": cmd_ensure, "attach": cmd_attach, "install": cmd_install, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    main()
