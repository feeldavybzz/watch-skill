# Kiwas: cómo clasificar y hacer crecer las mini skills

Bryan no necesita resúmenes de cada video: necesita Kiwas por tema que sepan **hacer** el
trabajo y que mejoren con cada link. Este paso va siempre después de guardar la lección.

## 1. Clasificar (sin preguntar, salvo duda real)
1. `python3 scripts/kiwas.py list`: ver Kiwas existentes y otras skills de Bryan.
2. **Kiwas paraguas (decisión de Bryan, 2026-10-10).** Si el video encaja, va SIEMPRE a uno de estos, dentro del área correspondiente:

   | Kiwa | Abarca (todo esto va aquí, en su área) |
   |---|---|
   | `diseno-grafico` | briefing y estrategia visual, logos, identidad y branding visual, tipografía, color, composición y retícula, piezas para redes, carteles, editorial, mockups, presentación al cliente |
   | `motion-graphics` | toda animación: tipografía cinética, animación de logos y títulos, transiciones gráficas, lower thirds, elementos para reels, easing y timing |
   | `composicion-visual` | composición de la imagen en foto, video, cine, reels y piezas: tercios, rejilla áurea, diagonales, triángulos, V, radial, curva S, pirámide, espiral, guías por formato (16:9, 5:4, 1:1, 4:5, 9:16) y guías o plantillas superpuestas para el plugin |
| `editor-asistente` | preparar y montar el material: cortar silencios y errores, subtitular, sacar reels y carruseles de un video largo, organizar el material, editar con IA (Premiere, DaVinci, Claude Code) |
| `cinematografia` | cámara: movimientos (estático, paneo, whip pan, tilt, push in, pull out, zoom, dolly zoom, roll, tracking, trucking, arc, boom, aleatorio), ángulos, los 12 soportes (en mano, trípode, pedestal, grúa, cenital, dolly, estabilizador, Snorricam, vehículo, dron, motion control, submarina), frame rate y cámara lenta o rápida, regla de los 180°, B-roll, lista de planos; después lentes y foco |
| `efectos-visuales` | efectos especiales de rodaje (SFX), efectos visuales (VFX: composición, croma, rotoscopia, producción virtual) y CGI; supervisores y departamentos; planear efectos desde el guion |
| `narrativa-y-direccion` | estructura de historias (círculo de Harmon), arco del personaje, blocking de escenas (espacio, formas, líneas), subtexto, storyboard |
| `iluminacion` | luz de cine y video: tipos de luz (natural, artificial, ambiente, práctica, motivada), medición (lux, kelvin, cuadrado inverso), clave alta y baja, claroscuro, luz dura y suave, equipo (tungsteno, HMI, LED, Kino Flo, geles, difusión, banderas) |
| `video-con-ia` | dirigir video y anuncios con IA (Seedance, Seedream, Higgsfield con Claude): personajes y locaciones de referencia, prompts cronometrados por planos, anclas, mapas de blocking, cortes ocultos |

3. Para temas fuera de los paraguas, crear un Kiwa nuevo con un nicho **igual de amplio** (un oficio, no una técnica ni una herramienta). Ejemplos: `color-grading`, `edicion-de-video`, `fotografia`, `sound-design`, `direccion-creativa`. DaVinci, Premiere o After Effects son secciones dentro del Kiwa, nunca un Kiwa.
4. Reusar antes que crear. Si una skill propia de Bryan (no `kiwa-<nicho>`) ya cubre exactamente el tema, como `portfolio-marca-personal`, usar `attach --skill`.
5. Un video puede alimentar varios Kiwas: por ejemplo, un reel con diseño de carteles y su animación va a `diseno-grafico` y a `motion-graphics`. Hacerlo solo si enseña algo real de cada uno.
6. No crear Kiwas de temas sin oficio para MUKIWA (noticias, opiniones). Herramientas internas como esta skill no llevan Kiwa.
7. Aprender **teoría y práctica**: lo que se explica en la voz y lo que se ve hacer en pantalla (paneles, valores, pasos). Si algo solo se dijo y no se vio, o al revés, anotarlo.

## 2. Crear o alimentar
```bash
python3 scripts/kiwas.py ensure --nicho color-grading --nombre "Color grading" \
  --herramientas "DaVinci Resolve,Premiere Pro" --cuando "corregir color, gradear, crear un look, igualar planos, usar LUTs"
python3 scripts/kiwas.py attach --nicho color-grading --leccion library/<topic>/<slug>.md
# o, si ya existe una skill de Bryan para eso:
python3 scripts/kiwas.py attach --skill ~/.claude/skills/<skill> --leccion library/<topic>/<slug>.md
```
`--cuando` son las frases con las que Bryan pediría ese trabajo: es lo que hace que la skill se active sola.

## 3. Fusionar lo aprendido (lo hace el agente, editando el SKILL.md del Kiwa)
- Escribir **instrucciones para hacerlo**, en imperativo: "Equilibra blancos con el gotero en una zona neutra antes de crear el look [3]". Nunca "en el video dice…".
- Cada técnica una sola vez. Si ya estaba, mejorarla (más precisa, con valores) y sumar la fuente: [2][5].
- Lo que depende de la herramienta va en **Por herramienta → DaVinci Resolve / Premiere Pro / …**: nombre exacto del panel, menú o control. Si aparece una herramienta nueva, añadir su sección y actualizar `herramientas` y la `description`.
- Valores (grados, %, frames, hex) solo si se vieron o dijeron; si son estimados, con ≈.
- Contradicciones entre fuentes → "Dudas abiertas", con ambas fuentes. No elegir en silencio.
- Reescribir la línea `>` del principio y la `description` cuando el Kiwa aprenda algo que cambie su alcance (más disparadores en "Usar cuando…").
- Mantener el SKILL.md por debajo de ~400 líneas: las recetas largas van a `references/recetas-<tema>.md`, enlazadas desde Recetas.
- Para una skill existente de Bryan: escribir en su `references/aprendido-mukiwa.md`, por tema, con el mismo estilo. No reescribir la skill original.

## 4. Instalar y verificar
```bash
python3 scripts/kiwas.py install   # enlaza kiwas/* en ~/.claude/skills/kiwa-<nicho> (una vez por Kiwa nuevo)
python3 scripts/kiwas.py check
```
Los enlaces apuntan al repo en el disco externo: si el disco no está conectado, los Kiwas no se cargan.

## 5. Contarle a Bryan
Una línea por nicho: "Kiwa color-grading: aprendió X (ahora 4 lecciones)" o "Nuevo Kiwa: diseño de logos".
