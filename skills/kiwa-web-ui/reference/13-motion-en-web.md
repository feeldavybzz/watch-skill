# 13 · Motion en la web (lo aprendido de Prompt Motion)

Fuente: lecciones `motion-codigo/*` de la biblioteca (promptsmotion.com, 265 motions hechos con Claude en código; texto de todos y fotogramas de 11). Lo marcado **[criterio propio]** es ingeniería web general añadida aquí, no viene de esa fuente. Para videos renderizados, usa `kiwa-motion-graphics`.

## Cuándo aplicar esto
Cuando una página necesita una **animación dirigida** (hero que cuenta una historia, secciones por scroll, un producto que se transforma) y no solo efectos sueltos. Si basta un efecto del catálogo (`03-effects-catalog.md`), usa ese.

## Principios que se repiten en los prompts
1. **Todo es función del tiempo (o del scroll)**: cada estilo se calcula a partir de un valor `t`; sin estado que se acumule entre fotogramas ni aleatoriedad suelta (usa semilla). En web, `t` puede ser el progreso del scroll **[criterio propio]**: así la animación se puede rebobinar, probar por fotograma y no se rompe si el usuario scrollea rápido.
2. **Un objeto que se transforma, no que aparece**: la forma pasa de botón a cargador a reproductor; el texto sube desde una línea de máscara; una forma negra inunda y se contrae a la siguiente escena. Evita fundidos cruzados entre secciones.
3. **Springs con overshoot mínimo y sin rebote cartoon** para botones, toggles y tarjetas; el indicador de una pestaña puede estirarse (el borde delantero va antes que el trasero).
4. **Una sola «cámara»**: un contenedor al que se le aplica el zoom y el desplazamiento; nunca dos movimientos a la vez; los empujes van de 1,0 a ≈1,04–1,08; al cambiar de escena, empezar donde terminó la anterior (si se reinicia a 1,0, salta).
5. **Cursor y estados reales**: si muestras una interacción, que el cursor haga clic de verdad sobre un control que existe; no inventes funciones que el producto no tiene.
6. **Un acento, una o dos fuentes, mucho espacio**; un hilo visual recurrente (en MUKIWA: el punto de la I / pupila).
7. **Cristal líquido solo en controles** y con algo detrás que lo haga visible (aura o foto desenfocada); sobre blanco liso desaparece. Para el cristal no uses `backdrop-filter: url()`: clona la escena detrás.

## Lista de prohibidos en piezas «premium» (la repiten los prompts)
Fundidos cruzados, entradas borrosas, destellos blancos, volteos 3D, partículas, glows en el texto de UI, neón, rejillas de suelo, cámara temblorosa, easing rebotón, degradados en la UI, glassmorphism en todo, párrafos largos, clichés de IA (cerebros, robots, destellos), texto en las esquinas, retenciones de más de 1 s, cualquier cosa que parezca plantilla.

## Receta para una sección animada dirigida
1. Escribe el **mapa de beats** (qué cambia en cada paso) y haz **un fotograma fijo por escena** antes de animar.
2. Define las pistas de cámara como `[progreso, zoom, x, y]` con zoom en escala logarítmica **[criterio propio]** y tramos suavizados.
3. Cada cambio de objetivo de un elemento = un spring; suma los springs en vez de reiniciar uno.
4. Texto que cambia dentro de una forma: máscara propia y tiempos de entrada y salida separados.
5. Una inundación de color debe pasar los 4 bordes y durar ≈0,35 s; un fade de 0,05 s parece una aparición instantánea.
6. No pongas `will-change` en lo que la cámara escala (el texto se ve borroso); no pongas `opacity` ni `filter` en un elemento `preserve-3d` (se aplana): desvanece el contenedor.
7. Revisa el último estado contra el primero si hay loop, y busca saltos de un fotograma al grabar la pantalla.

## Reglas de robustez (siguen mandando las de este skill)
- Respeta `prefers-reduced-motion` y lee `07-windows-troubleshooting.md` (Windows lo trae activado).
- Mantén cada efecto con una razón; 4 o 5 por página y una firma (ver SKILL.md).
- Si el hero es un video renderizado desde código: exporta MP4/WebM ligero, con póster y sin sonido por defecto; el peso importa **[criterio propio]**.

## Para MUKIWA
Fondo negro, lime #C5ED2E y blue #0068FB como únicos acentos, #232323 para superficies; glass solo en botones y tarjetas con borde cromático azul/lima; el centro del fondo queda oscuro para la tipografía.

## Límites
- Los valores de springs y los easings exactos no aparecen en la fuente.
- No se probó ninguna receta construyendo una página real.
