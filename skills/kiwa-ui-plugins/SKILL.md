---
name: kiwa-ui-plugins
description: "Cómo animar la interfaz de los plugins y consolas de MUKIWA (perillas, sticks, botones, toggles, pestañas, deslizadores, paletas de comandos, avisos) y cómo mostrarlos en un video de demo o lanzamiento: micro-interacciones con springs, arrastre directo, estados que se transforman, render determinista con seek(t) y lista de prohibidos. Úsala cuando Bryan pida animar un control o un plugin, hacer la demo o el reel de un plugin, definir cómo se mueve un botón o una perilla, o revisar si una animación de interfaz se siente física y no genérica. Complementa a mukiwa-ui-plugins (diseño del plugin), que vive en el Mac de Bryan."
---

# kiwa-ui-plugins — animar la UI de los plugins

Aquí vive **cómo se mueve** la interfaz de un plugin y cómo se enseña en video. El diseño del plugin (flujo, arquitectura, wireframe, sistema de componentes) está en `mukiwa-ui-plugins`, que solo existe en el Mac y en Drive de Bryan y **no se pudo leer** al crear esta skill: si Bryan sube esa skill, fusionar ambas en una sola (ver «Dudas abiertas»).

Fuente de todo lo de abajo: lecciones `motion-codigo/*` (Prompt Motion, 265 motions hechos con Claude; texto completo de todas, fotogramas de 11) y las lecciones de diseño UI ya guardadas (controles físicos sin neón ni glassmorphism). Los parámetros son los que daban los prompts de terceros, no medidos.

## Cuándo usarla
- Animar un control: perilla, stick, botón, toggle, slider, pestañas, selector, paleta de comandos (⌘K), aviso (toast), medidor.
- Hacer la **demo o el reel de un plugin**: un solo plano donde la misma forma pasa por todos los estados.
- Revisar una animación de UI que «se siente genérica» o rebotona.
- Pasar un prototipo de HTML a video renderizado.

Para animación general (texto cinético, logos, transiciones) usa `kiwa-motion-graphics`; para el diseño visual de una web, `kiwa-web` (carpeta `diseno/`).

## Principios (de los prompts largos de Prompt Motion)
1. **Una forma, nunca un corte**: cada estado es el mismo elemento que cambia de tamaño, radio y color mientras su contenido se cambia con un desenfoque corto. Recorrido visto: botón → cargador → check → isla dinámica → reproductor (play/pausa que se transforma) → barra de progreso → deslizador de volumen que se estira al arrastrarlo más allá del máximo → toggle → indicador de pestaña líquido → gráfica que se dibuja con tooltip al pasar el cursor → ⌘K → filtrar al escribir → enter → aviso → vuelve al botón.
2. **Springs con overshoot mínimo, sin rebote cartoon**: «springs everywhere, a tiny overshoot at most». Si el spring es fuerte, parece juguete.
3. **Dos bordes, dos springs**: en un indicador de pestaña, el borde delantero va antes que el trasero y la forma se estira; igual con la perilla de un toggle.
4. **Manipulación directa**: mientras el cursor está presionado, el valor sale de su posición; al soltar, un spring lo devuelve desde donde estaba (así se siente físico).
5. **Objeto sólido y físico**: una insignia o un control 3D se inclina hacia el cursor siguiendo la física; rápido y suave, no rebotón.
6. **Cada evento tiene su sonido**: un efecto por clic, tecla o aterrizaje, colocado por su pico medido, no por el inicio del archivo.
7. **Cursor protagonista**: clics, arrastres y pulsaciones largas reales sobre controles que existen; la cámara hace zoom y el cursor escala con ella.
8. **Loop limpio**: el último fotograma = el primero, con la posición y velocidad del cursor incluidas; si no, el bucle tartamudea.

## Cómo construirlo (receta)
1. Lista de estados del plugin (8–12) **sobre la rejilla de beats** (p. ej. 120 BPM, 7 compases, algo en cada beat) antes de escribir código.
2. Un HTML de tamaño fijo (p. ej. 1440×1440) con `seek(t)`: todo se calcula del tiempo, sin transiciones CSS, timers ni estado entre fotogramas.
3. Springs en forma cerrada; un valor con varios objetivos = suma de un spring por cambio.
4. Texto que cambia dentro de un contenedor que se transforma: máscara propia y tiempos de entrada y salida separados.
5. La cámara hace zoom para que cada estado llene el cuadro; nunca `will-change` sobre lo que se escala (texto borroso).
6. Render con Playwright a 60 fps, 4 subfotogramas mezclados con `ffmpeg tmix` (8 si hay fantasmas); un fotograma por beat antes del render completo; buscar «pops» de un fotograma.
7. Música ≈120 BPM con un tiempo fuerte al inicio; SFX por pico; masterizar a −14 LUFS.

## Estilo MUKIWA para plugins
- Controles **físicos**, no neón ni glassmorphism genérico; el stick con sombra dinámica y el «bendy button» (ver lecciones de diseño) son la referencia.
- Paleta: negro/#232323, lime #C5ED2E y blue #0068FB; morado solo atmosférico. Un acento por pantalla.
- Glass solo en botones y tarjetas, con borde cromático azul/lima, no en toda la consola.
- El punto de la I (pupila) puede ser el cursor o el indicador que conecta los estados.

## Prohibidos
Easing rebotón, partículas, glows en el texto de UI, degradados en la UI, destellos blancos, volteos 3D, fundidos cruzados, cámara temblorosa, mezclar estilos de trazo en los iconos, tiempos muertos, cualquier cosa que parezca plantilla.

## Checklist antes de entregar
- [ ] ¿Cada estado es la misma forma transformada, sin cortes?
- [ ] ¿Springs sin rebote cartoon y arrastres con retorno desde la posición real?
- [ ] ¿Un sonido por evento y todo cae en un beat?
- [ ] ¿Último fotograma = primero?
- [ ] ¿Revisé un fotograma por beat y los pops de un fotograma?
- [ ] ¿Solo controles que el plugin realmente tiene?

## Dudas abiertas
- No se leyó `mukiwa-ui-plugins` (solo en el Mac/Drive): falta fusionar su sistema de componentes, nombres de controles y reglas de la consola (p. ej. VYBZ-64).
- Constantes de springs, duraciones y curvas no aparecen en la fuente.
- No hay una animación de plugin real de MUKIWA probada con este método; validarla con un control (p. ej. el stick) antes de dar el método por bueno.
- Voz y sonido de los videos no se evaluaron: solo texto y fotogramas.

## Fuentes
- Lecciones en `references/lecciones/`: `motion-en-codigo-render-determinista-seek-springs-y-motion-blur.md`, `lanzamiento-producto-en-codigo-direccion-beats-prohibidos.md`, `prompt-motion-catalogo-265-motions-hechos-con-claude.md` (promptsmotion.com).
- Lecciones de diseño UI relacionadas en la biblioteca: `diseno-grafico/tendencias-ui-material-squircle-bendy-trazo-a-mano-malewicz.md`, `diseno-grafico/ux-ui-curso-mas-corto-eze-cichello.md`.
