# Profesores: cómo clasificar y hacer crecer las mini skills

Bryan no necesita resúmenes de cada video: necesita profesores por tema que sepan **hacer** el
trabajo y que mejoren con cada link. Este paso va siempre después de guardar la lección.

## 1. Clasificar (sin preguntar, salvo duda real)
1. `python3 scripts/profes.py list`: ver profesores existentes y otras skills de Bryan.
2. Elegir el o los nichos del video. Un nicho es **un oficio o resultado**, no una herramienta:
   - Bien: `color-grading`, `diseno-de-logos`, `tipografia-cinetica`, `ritmo-de-edicion`, `ganchos-de-reels`, `sound-design`, `retoque-de-retrato`.
   - Mal: `davinci`, `premiere`, `after-effects` (eso va como sección dentro del nicho: color grading → DaVinci Resolve y Premiere Pro).
   - Ni demasiado amplio (`diseno`) ni demasiado estrecho (`curvas-en-davinci-18`).
3. Reusar antes que crear: si un profesor existente cubre el oficio, alimentar ese. Si lo cubre una skill propia de Bryan (no `profe-*`), usar `attach --skill`.
4. Un video puede alimentar varios nichos (ej. un tutorial de reel con color y ritmo → `color-grading` y `ritmo-de-edicion`), pero solo si enseña algo real de cada uno.
5. No crear profesores de temas sin oficio para MUKIWA (noticias, opiniones). Herramientas internas como esta skill no llevan profesor.

## 2. Crear o alimentar
```bash
python3 scripts/profes.py ensure --nicho color-grading --nombre "Color grading" \
  --herramientas "DaVinci Resolve,Premiere Pro" --cuando "corregir color, gradear, crear un look, igualar planos, usar LUTs"
python3 scripts/profes.py attach --nicho color-grading --leccion library/<topic>/<slug>.md
# o, si ya existe una skill de Bryan para eso:
python3 scripts/profes.py attach --skill ~/.claude/skills/<skill> --leccion library/<topic>/<slug>.md
```
`--cuando` son las frases con las que Bryan pediría ese trabajo: es lo que hace que la skill se active sola.

## 3. Fusionar lo aprendido (lo hace el agente, editando el SKILL.md del profesor)
- Escribir **instrucciones para hacerlo**, en imperativo: "Equilibra blancos con el gotero en una zona neutra antes de crear el look [3]". Nunca "en el video dice…".
- Cada técnica una sola vez. Si ya estaba, mejorarla (más precisa, con valores) y sumar la fuente: [2][5].
- Lo que depende de la herramienta va en **Por herramienta → DaVinci Resolve / Premiere Pro / …**: nombre exacto del panel, menú o control. Si aparece una herramienta nueva, añadir su sección y actualizar `herramientas` y la `description`.
- Valores (grados, %, frames, hex) solo si se vieron o dijeron; si son estimados, con ≈.
- Contradicciones entre fuentes → "Dudas abiertas", con ambas fuentes. No elegir en silencio.
- Reescribir la línea `>` del principio y la `description` cuando el profesor aprenda algo que cambie su alcance (más disparadores en "Usar cuando…").
- Mantener el SKILL.md por debajo de ~400 líneas: las recetas largas van a `references/recetas-<tema>.md`, enlazadas desde Recetas.
- Para una skill existente de Bryan: escribir en su `references/aprendido-mukiwa.md`, por tema, con el mismo estilo. No reescribir la skill original.

## 4. Instalar y verificar
```bash
python3 scripts/profes.py install   # enlaza profes/* en ~/.claude/skills/profe-* (una vez por profesor nuevo)
python3 scripts/profes.py check
```
Los enlaces apuntan al repo en el disco externo: si el disco no está conectado, los profesores no se cargan.

## 5. Contarle a Bryan
Una línea por nicho: "Profe color-grading: aprendió X (ahora 4 lecciones)" o "Nuevo profe: diseño de logos".
