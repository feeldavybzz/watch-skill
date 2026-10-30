# Estilo MUKIWA por defecto

Úsalo cuando el sitio sea de **MUKIWA DEPARTMENT** o Bryan lo pida. Para un cliente, mandan su marca y el arquetipo de `02-archetypes.md`.

## Marca
- **MUKIWA DEPARTMENT**: departamento creativo para gente que ve el mundo distinto. La palabra "DEPARTMENT" se queda.
- Firma recurrente: **FEEL DA VYBZ**. Frases: VIBES NEVER LIE. VIBES NEVER DIE. WE MOVE OUR LIFE BY VIBES.
- Quien trabaja ahí es un **VIBE STAR**.
- Tono: directo, creativo, seguro, humano, contemporáneo, con conciencia cultural. Sin clichés corporativos ni formalidad innecesaria.
- Nunca se define a nadie por color de piel, origen ni clase social.

## Color
| Rol | Valor |
|---|---|
| Lima | `#C5ED2E` |
| Azul | `#0068FB` |
| Blanco | `#FFFFFF` |
| Oscuro | `#232323` |
| Morado | acento atmosférico secundario, nunca el color principal |

Combinación base: **negro + azul eléctrico + lima**, con acentos morados ocasionales.

## Fondo
- Base de **negro sólido**; el color entra como luz difusa, no como relleno.
- Formas luminosas suaves y dispersas en azul, lima y un poco de morado: fluidas, brillantes, atmosféricas, cinematográficas.
- **El centro se mantiene más oscuro** para tipografía y navegación. El fondo nunca debe competir con el contenido.
- Evita: ruido excesivo, formas agresivas, degradados saturados a pantalla completa, desorden visual.
- Para el fondo animado, el arquetipo más cercano de `02-archetypes.md` es 05 Mouse-Reactive Gradient o el mesh gradient en CSS (`03-effects-catalog.md` §4.3, sin WebGL).

## Vidrio (glass UI): selectivo
- **Se usa en**: botones, divisiones de navegación, tarjetas y elementos interactivos.
- **No** convertir toda la web en vidrio.
- Botones con relleno oscuro translúcido, desenfoque de fondo, bordes finos luminosos con bordes cromáticos azul/lima, brillo controlado. Debe sentirse como la interfaz de iOS de gama alta, no como cyberpunk genérico.
- Recuerda B.12 de `04-critical-gotchas.md`: `backdrop-filter` necesita un **fondo sólido de respaldo**.

## Navegación
HOME · PORTFOLIO · DESIGN DEPT. · ABOUT US · CONTACT. Igual en todas las páginas.

Departamentos: GRAPHIC DESIGN DEPT. (identidad, colecciones y campañas gráficas) · VISUAL EDITS DEPT. (filmación, foto, edición, postproducción) · CREATIVE DIRECTION DEPT. (concepto, guion, dirección de campaña).

## Portfolio
- Los proyectos son visualmente dominantes: evita miniaturas pequeñas o mucho texto antes de mostrar el trabajo.
- Prioridad en las páginas de proyecto: 1) contenido visual, 2) composición fuerte, 3) movimiento y video, 4) información.
- Video horizontal para héroes; **reels en vertical 9:16**; videos ordenados, autoplay solo donde corresponda, empezando en silencio o a volumen bajo. Evita el aspecto de reproductor por defecto del navegador. Cuida la velocidad de carga.

## Principios
Jerarquía visual fuerte, espaciado limpio, alineación óptica, tipografía, consistencia de marca, espacio negativo, movimiento con propósito, rendimiento, móvil, ejecución premium. **Cada efecto debe tener una razón.**

No debe sentirse como una agencia genérica, una consultora, una plantilla ni un sitio cyberpunk o de grafiti infantil. Debe sentirse **creativo + cultural + premium + poco convencional**, con ejecución profesional.

## Regla de trabajo
Al modificar un diseño existente, **no lo rediseñes entero**. Si piden cambiar el fondo, cambia solo el fondo; si piden cambiar los botones, conserva el resto de la composición, las proporciones, la jerarquía, la tipografía, el contenido y la estructura. Iteración controlada, no rediseño innecesario.
