---
name: kiwa-motion-graphics
description: "Kiwa de motion graphics: tipografía cinética en After Effects, easing, animación 2D en Blender, ritmo de transiciones, zonas seguras para reels y motion en código (HTML, Remotion, HyperFrames) con render determinista, springs, motion blur, beats y videos de lanzamiento. Úsalo al animar, hacer reels, intros, lanzamientos o explainers."
metadata:
  nicho: motion-graphics
  herramientas: "After Effects, Blender, Remotion, HyperFrames, código HTML"
  lecciones: 16
  actualizado: "2026-10-31"
---

# Kiwa · Motion graphics
> Anima con criterio: planea la composición final, una capa por bloque con Animators, curvas siempre suavizadas y el color para dirigir la mirada. Hoy domina la tipografía cinética en After Effects; el resto de áreas crece con cada video. Tiene **2 lecciones propias** ([1] tipografía cinética, [3] cartoon en Blender) y **6 complementarias** de composición, edición y cámara ([2] reel de composición, [4] edición, [5] composición, [6] overlays, [7] movimientos, [8] soportes).

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Todo lo animado vive aquí, en su área. El diseño estático va a `kiwa-diseno-grafico`.

## Cómo trabajar (cualquier animación)
1. **Planea el cuadro final antes de animar**: en papel o Photoshop, cómo encajan los elementos al terminar [1].
2. **Pocas capas, mucha animación**: una capa por bloque o frase, animada con Animators, no una capa por letra [1].
3. **Nunca keyframes lineales**: Easy Ease (F9) y ajuste en el Graph Editor [1].
4. **Agrupa con un control (null)** para mover conjuntos sin romper la animación [1].
5. **El color va al final** y marca el foco: qué debe mirar el espectador en cada momento [1].

## Áreas
### Tipografía cinética
- **Aparición por palabra o letra**: capa de texto → *Animate* → **Opacity** = 0% → *Range Selector*: keyframe **Start** 0% y, ≈12 frames después, 100% → *Advanced* → **Based On: Words** (o *Characters*) [1].
- **Entrada desde abajo**: Animator con **Position + Opacity** y el mismo Range Selector [1].
- **Bloques rotados que forman una composición**: una capa por bloque, rotación 90° / −90°, cada bloque alineado al borde del anterior, con keyframes de posición y rotación suavizados [1].
- **Ola de color por palabras**: *Animate* → **Fill Color** con el color de acento → anima **End** 0→100% y luego **Start** 0→100%; *Advanced* → **Shape: Ramp Up** o **Wiggly** [1].
- **Foco por bloque**: Fill Color de blanco al acento en el bloque que habla; el resto en blanco o grises [1].
- **Profundidad sin capas extra**: un gris distinto por línea, de claro a oscuro [1].

### Easing y timing
- Selecciona keyframes → **F9** → Graph Editor. Más ease al final hace que el último elemento "retenga" [1].

### Animación de logos, transiciones, lower thirds, elementos para reels
- **Guía que se dibuja y luego revela la foto** (reel de composición): línea blanca fina que se traza sobre negro (≈ 0,7 s), entra la imagen con la línea encima (≈ 1 s) y la línea se desvanece; etiqueta de texto integrada en la geometría. Cada bloque dura ≈ 2–3 s [2]. Valores de easing y trazo: no visibles, solo ≈.

### Animación 2D de personajes (cartoon clásico)
- **Orden de trabajo**: boceto tosco cuadro a cuadro → segunda pasada más clara (expresión, forma, diseño) → tinta → color plano → ajustes → escenario → ajuste de velocidad [3].
- **Boceto**: círculos y líneas para torso, cabeza y piernas, con la piel de cebolla del cuadro anterior; la sombra al suelo como trazo aparte [3].
- **Tinta**: una capa por parte del cuerpo (se mueve una sin tocar las demás); línea limpia que no tiembla, en marrón oscuro y no negro puro; color plano debajo de la línea [3].
- **Escenario 3D con aire de dibujo animado**: fondo en banda curva (arena que sube a mar y cielo) y objetos 3D como sombrillas; el personaje, un plano que recorre una trayectoria; el paralaje da el efecto Popeye [3].
- **Pies que no patinan**: ajusta la velocidad del avance del personaje hasta que el paso coincida con el suelo [3] (valor no visto).
- **Cierre para reels**: un objeto pasa a ras de cámara y tapa al personaje antes del corte [3].

### Transiciones y ritmo (criterio de edición aplicado a gráficos) [4]
(Las lecciones de edición no enseñan After Effects; lo que sigue es criterio de corte que aplico a las animaciones, ≈, sin probar.)
- **Decide el ritmo por el tono**: una pieza contemplativa pide bloques que se queden más tiempo; una de acción, cambios rápidos [4]. Cada cambio de bloque debe tener propósito [4].
- **Corte en acción**: haz que la transición ocurra en mitad de un movimiento (el bloque que sale arrastra al que entra) para que se sienta fluida; el punto de salida de uno coincide con el de entrada del otro [4].
- **Match cut**: un elemento (forma, línea, color) pasa de una escena a la siguiente; la guía escrita de [4] solo lo define, no enseña a animarlo [4].
- **Eye trace**: en cambios muy rápidos (≈1–2 s) deja el punto de interés en la misma zona del cuadro de un bloque al siguiente [4].
- **Audio por delante o por detrás (J/L cut)**: en lyric videos o textos con voz, adelanta o prolonga el sonido sobre el cambio para que el ritmo sea natural [4] (aplicación mía).

### Composición del cuadro para gráficos y texto [5]
- **Líneas y formas guían la mirada**: verticales = fuerza, horizontales = calma, diagonales = energía; ordena los bloques de texto con esa intención [5].
- **Espacio negativo y equilibrio**: un bloque grande sin contrapeso desequilibra; el vacío da importancia al texto [5]. El 9:16 de reels no lo trata el video: solo habla horizontal [5].
- **Color y tono**: el color puede imponerse a otros métodos de composición; el ojo va a lo más brillante, así que la palabra de foco lleva el tono más claro (el lima #C5ED2E sobre #232323 cumple eso, aplicación mía) [5].
- **Tercios, triángulo áureo y razón áurea 1:1,618** sirven de guía para colocar el título; el nivel de la línea áurea cae a ≈ 0,382 de la altura [5].

### Overlays y guías sobre el cuadro [6]
- En Premiere un overlay (interfaz social o guías: cuadrícula, tercios, cruz, márgenes, zona segura de acción 90 % y de título 80 %) se coloca como **clip en una pista de video superior** de la duración de la secuencia; no se dibuja sobre el monitor [6].
- Usa esas zonas seguras al diseñar texto para reels; no olvides quitar el overlay antes de exportar (el video no lo explica) [6].

### Cámara virtual (3D / Blender / AE) [7]
- Vocabulario de movimientos para animar una cámara: push in, pull out, arc, tracking, boom, whip pan, dolly zoom, etc. [7] (el uso en 3D es aplicación mía, ≈).
- **Control de movimiento**: repetir exactamente el mismo movimiento de cámara en dos tomas sirve para componer elementos después; con cámara virtual es el equivalente a duplicar la curva [8] (≈).

### Explainers en collage de papel con Claude Motion [9]
- Conectar el conector de video en Claude (Settings → Connectors), pedir 30 s con el tema y un estilo con nombre («paper collage estilo Vox»), abrir el proyecto en el editor y retocar a mano o pedir cambios a Claude sobre la misma línea de tiempo. El primer resultado es un borrador: se itera.

### Radial blur animado con la persona nítida (Premiere) [10]
- Plugin gratuito Any Radial Blur (al instalar pide un monto: poner 0). Aplicarlo al clip; valores vistos: Type Spin, Amount ≈ 70–73, Quality 20–50, Distance to center 2,00 / 1,00 / 0,80, Effect center 960/540; animar con keyframes.
- Para que quede natural: duplicar el clip arriba, quitarle el efecto y hacerle una máscara de objeto a la persona; Expansion ≈ 8 y feather; se ve blend mode Add y Scale 114 en esa capa (sin explicación).

### Micro-interacciones de UI [11]
- Un botón elástico («let's collaborate») tirado por una mano dibujada con hilos se usa como gancho humorístico. Solo referencia visual: sin método.
### Motion en código (HTML, Remotion, HyperFrames): render determinista [12][13][14]
- **Cuándo**: videos de lanzamiento, explainers, reels y fondos animados que quieres editar y volver a renderizar cambiando una línea. El proyecto vive como código; cada escena es un bloque.
- **Antes de pedir nada** [12]: elige 1 o 2 videos de referencia y pide que los iguale (nombrar un estilo funciona mejor que describirlo; sin referencia sale texto centrado, fondo degradado y todo con fade). Vuelca el contexto (logo, colores, fuentes, capturas reales del producto, ideas), pide **3 storyboards**, elige uno y pide **un fotograma fijo por escena antes de animar**. Da notas como director, con palabras de cámara y fotogramas: «baja todos los zooms a 0,7×», «corte seco aquí», «empuja sobre el botón».
- **Define el tiempo primero** [12]: duración y fps (20 s a 30 fps = 600 fotogramas), qué pasa en cada fotograma o beat, y pide los cambios **por rango de fotogramas** para no romper el resto.
- **Construcción** [13]: una función `seek(t)` que calcula todos los estilos a partir del tiempo (sin transiciones CSS, timers, estado entre fotogramas ni `Math.random`; aleatoriedad con semilla); **springs en forma cerrada** (un spring por cada cambio de objetivo, sumados); cámara única en un contenedor con pistas `[tiempo, zoom, x, y]` y zoom en escala logarítmica; último fotograma igual al primero si hay loop (incluido el cursor).
- **Render** [13]: Playwright a 60 fps con 4 u 8 subfotogramas por fotograma, mezclados con `ffmpeg tmix` (8 si ves copias fantasma en movimientos rápidos). Antes del render final: un fotograma por beat, búsqueda de «pops» de un solo fotograma y legibilidad.
- **Ritmo y sonido** [13]: analiza la canción (tempo, drop) y pon algo en cada beat; cortes duros 2 fotogramas antes del beat; un SFX por evento colocado por su pico medido; música con ducking bajo la voz; masterizar a −14 LUFS.
- **Dirección de un lanzamiento** [14]: un plano continuo donde cada escena sale de la anterior (los objetos cambian de forma en vez de fundirse); cursor con clics reales; UI real del producto (nada inventado); un solo acento y una o dos tipografías; una forma como hilo conductor (en MUKIWA, el punto de la I).
- **Lista de prohibidos** [14]: fundidos cruzados, entradas borrosas, destellos blancos, volteos 3D, partículas, glows en el texto de UI, neón, cámara temblorosa, easing rebotón, degradados en la UI, glassmorphism en todo, clichés de IA (cerebros, robots, destellos), texto en las esquinas, retenciones de más de 1 s.
- **Plugins y skills de terceros que aparecen** [12] (solo referencia, no instalar sin permiso de Bryan): Remotion (`remotion-dev/skills`), HyperFrames (`heygen-com/hyperframes`), GSAP (`greensock/gsap-skills`), Lottie (`LottieFiles/motion-design-skill`), componentes de 21st.dev.

### Cámara 3D de After Effects: crear, mover y enfocar [15]
- **Crear**: Layer → New → Camera, el botón de capa nueva o **Ctrl+Alt+Shift+C**. Tipo **Two-Node** (orbita alrededor de un punto de interés) o **One-Node** (orienta sobre sí misma). Preset 50 mm de partida (Film Size 36 mm, ángulo 39.6°); lista de presets: 15, 20, 24, 28, 35, 50, 80, 135 y 200 mm. **Marca Enable Depth of Field** antes de aceptar; todo se puede editar después en Camera Options [15].
- **Qué hace la focal** (dicho por el autor): corta (15 mm) = ángulo muy amplio; larga (200 mm) = ángulo estrecho, sujeto más grande y más desenfoque [15].
- **Mover**: herramientas **Orbit**, **Pan** y **Dolly**. Dolly ≠ zoom: dolly desplaza la cámara hacia el sujeto; zoom cambia la lente con la cámara quieta. Para movimientos repetibles, keyframea **Position / Point of Interest / Orientation / Rotation (X, Y, Z)** en Transform; en el ejemplo, cronómetro en Position, dolly hacia el centro del logo, dolly de salida más adelante, **Easy Ease**, y **Z Rotation** para sumar giro [15].
- **Valores base vistos** (comp de 1920 px, 50 mm): Point of Interest 960, 540, 0; Position 960, 540, **−2666.7**; Orientation 0, 0, 0; Zoom 2666.7 px (39.6° H) [15]. La relación es ≈ focal × ancho de comp ÷ 36 mm (cálculo mío que coincide con lo visto).
- **Profundidad de campo**: Focus Distance (qué distancia queda nítida), Aperture (más abertura, más desenfoque; visto 25.3 px con Focus Distance 2666.7 px), Blur Level 100 % = natural. **Iris Shape = Fast Rectangle** (renderiza más rápido; otras formas: Triangle a Decagon); Highlight Gain 0, Threshold 255, Saturation 0 por defecto [15].
- **Foco automático**: Layer → Camera → **Link Focus Distance to Layer** (elegida por el autor): el foco se queda en la capa (por ejemplo el logo) mientras la cámara hace dolly. También: Link to Point of Interest y Set Focus Distance to Layer (esta última no se probó) [15].
- Vistas: Active Camera para ver lo que ve la cámara; vistas Top/Front/Right/Left para ver dónde está; en AE 2023 el menú de vistas, en versiones anteriores un icono de cámara [15].

## Por herramienta
### After Effects
- Atajos: **R** rotación, **P** posición, **S** escala, **U** ver keyframes, **F9** easy ease [1].
- Emparentar a un null con **Pick Whip** [1].
- Cámara 3D: Ctrl+Alt+Shift+C; las capas deben ser 3D para reaccionar a la cámara (≈, no se vio el interruptor) [15].

### Blender
- Dibujo 2D cuadro a cuadro con capas, piel de cebolla y barra de pinceles, línea de tiempo con un keyframe por cuadro, y vista 3D con cámara vertical 9:16 [3]. Nombres de menús y valores: no vistos; el creador no los dice.

### Composición y texturas con CC Composite (After Effects) [16]
- CC Composite hace otra operación de composición dentro de la pila de efectos. **Contraste sin duplicar capa**: aplícalo al mapa con Top Layer = None y prueba Overlay (Soft Light es más suave, Hard Light más agresivo) bajando Opacity; la opacidad se puede animar [16].
- **Imagen dentro del texto**: CC Composite en el texto, Top Layer = el mapa; con RGB Only desactivado se conserva el recorte a las letras. Oculta la capa fuente y revisa la cuadrícula alfa antes de exportar [16].
- **Textura dentro de una forma**: CC Composite en la silueta con una textura de papel como Top Layer; ajusta Transfer Mode y Opacity [16].
- **Escala**: el mapa no hereda su escala visible porque el efecto lee una etapa anterior a las transformaciones. Arréglalo con un Transform en la capa fuente y eligiendo **Effects & Masks** en el selector de fuente, o precomponiendo con Move all attributes [16].
- Técnica vista en video, aún sin probar en el After Effects de Bryan; no automatizar por índices de parámetros [16].

## Errores comunes
- Crear la cámara 3D sin marcar **Enable Depth of Field** y luego no ver desenfoque: viene desmarcado por defecto, actívalo en el diálogo o en Camera Options [15].
- Confundir zoom con dolly: el zoom no cambia la perspectiva; el dolly sí [15].
- Una capa por palabra → proyecto pesado y difícil de reeditar [1].
- Animar sin saber el cuadro final → los elementos no encajan al terminar [1].
- Keyframes lineales → movimiento robótico [1].
- Todo el cuerpo en una sola capa de dibujo → cualquier ajuste obliga a redibujar [3].
- Velocidad de avance que no coincide con el paso → los pies patinan [3].
- Cortes de bloque sin motivo ni ritmo → la pieza se siente arbitraria [4].
- Poner texto fuera de las zonas seguras de reels → lo tapa la interfaz [6].
- **En código** [13]: `backdrop-filter: url()` falla en Chromium (clona la escena detrás del cristal); una inundación de color debe pasar los 4 bordes y durar ≈0,35 s; `will-change` en lo que escala la cámara deja el texto borroso; `opacity` o `filter` en un elemento `preserve-3d` lo aplana; un fade de 0,05 s parece aparición instantánea; si la cámara se reinicia a 1,0 al cambiar de escena, el zoom salta.
## Checklist antes de entregar
- [ ] Cuadro final planeado y respetado.
- [ ] Capas mínimas, con Animators.
- [ ] Easing revisado en el Graph Editor.
- [ ] Un solo color de foco, sincronizado con lo que se dice.
- [ ] Legible en móvil (9:16) si va a reels, dentro de zonas seguras [6].
- [ ] Cada cambio de bloque tiene propósito y ritmo acorde al tono [4].
- **Motion en código**: ¿el último fotograma es igual al primero (loop)? ¿Revisé un fotograma por beat y los pops de un fotograma? ¿Cada SFX cae en su pico? ¿Masterizado a −14 LUFS? ¿Cero prohibidos de la lista [14]?
## Para MUKIWA
- Logo MUKIWA / el «I» con ojo: dolly lento sobre capas 3D con foco enlazado al logo (Link Focus Distance to Layer) y Aperture moderada [15] (≈, idea mía).
- Color de foco lima #C5ED2E sobre blanco y #232323; azul #0068FB como segunda ola [1].
- Frases de marca ("FEEL DA VYBZ" / "VIBES NEVER LIE.") como bloques: uno a 90° y otro horizontal, formando un solo bloque [1].
- Mascota o personaje retro animado: método de [3], a 9:16 nativo.
- Reels 9:16: ola de Fill Color lima barriendo las palabras clave.
- **Motion en código**: usa lime #C5ED2E y blue #0068FB sobre negro/#232323, sin degradados neón ni glassmorphism en el cuerpo; glass solo en controles; el punto de la I (pupila) como hilo entre escenas [14].
## Dudas abiertas
- Valores de easing/bezier no visibles en [1]; los ≈12 frames son lo que se dijo.
- De [3] no hay fps, pinceles ni cómo se arma el fondo curvo; falta un tutorial completo de animación 2D en Blender.
- [4][5][6][7][8] Son lecciones de cine y edición real, no de motion: dan criterio, no pasos de After Effects ni valores.
- Animación de logos, transiciones, lower thirds y herramientas fuera de After Effects: sin fuentes todavía; de [2] solo se ve el resultado, no el método.
- [9] No se vio el explainer completo (solo stills) ni el nombre exacto del conector (se lee «invideo» en un tile).
- [10] No se explica por qué la máscara va en Add ni el Scale 114; los keyframes que animan el efecto no se ven. El link del plugin va por comentario.
- [11] Sin voz y 7 s: no se sabe con qué se hizo la física del botón (código, Rive, After Effects).
- [12][13][14] Todo viene de prompts de terceros: no se midieron los springs (constantes), duraciones ni easings en los videos, y no se ejecutó ninguna receta aquí; 11 de 265 videos vistos con fotogramas, el resto por texto.
- [13] Falta una lección con código real (un `seek(t)` probado en un video de MUKIWA) para validar el método.

- [15] Tutorial de principiante con un solo ejemplo animado (logo sobre anillos); subtítulos automáticos sin Whisper. No muestra atajos de las herramientas de cámara, animar Focus Distance/Aperture con keyframes, Create Orbit Null ni Stereo 3D Rig, ni el render final; el efecto de Highlight no se cambia.

## Referencias incorporadas — Instagram 2026-10-30
Notas de evidencia y criterio de la tanda de Instagram del 30-oct (rescatadas del disco; sin análisis nuevo). Consúltalas al evaluar referencias o una revisión de video por planos.
- [criterios-motion.md](references/instagram-2026-10-30/criterios-motion.md)
- [revision-por-planos-claude.md](references/instagram-2026-10-30/revision-por-planos-claude.md)

## Fuentes
- [1] Tipografía cinética en After Effects: 3 técnicas con una sola capa — https://www.youtube.com/watch?v=f3nb-MQyshQ · `references/lecciones/tipografia-cinetica-after-effects-3-tecnicas.md`
- [2] Reel de 24 s con 8 recursos de composición dibujados sobre fotos — archivo local · `references/lecciones/reel-8-recursos-composicion-guias-sobre-fotos.md`
- [3] Cartoon clásico en Blender (Youpie Toons, short de 61 s) — https://youtube.com/shorts/DCzXpBqt558 · `references/lecciones/dibujo-animado-clasico-blender-youpie-toons.md`
- [4] Seis formas de editar una escena (StudioBinder, Shot List ep. 10) — https://youtu.be/FVR8zz8ci2k · `references/lecciones/seis-formas-de-editar-una-escena-studiobinder.md`
- [5] Los 9 elementos de la composición en cine (StudioBinder, ep. 11) — https://youtu.be/hUmZldt0DTg · `references/lecciones/nueve-elementos-composicion-cine-studiobinder.md`
- [6] Guideify 2: overlay social y guías en Premiere — https://youtu.be/ZcDtrjVuR5k · `references/lecciones/guideify-2-overlay-social-y-guias-en-premiere.md`
- [7] Los 15 movimientos de cámara (StudioBinder, ep. 6) — https://youtu.be/IiyBo-qLDeM · `references/lecciones/movimientos-de-camara-15-studiobinder.md`
- [8] Los 12 soportes de cámara, sección de control de movimiento (StudioBinder, ep. 5) — https://youtu.be/heJ9hWNb10g · `references/lecciones/soportes-de-camara-12-rigs-studiobinder.md`
- [9] Explainer de motion graphics con Claude Motion y un conector de editor de video (@aangel) — reel de Instagram, archivo local · `references/lecciones/claude-motion-explainer-papel-collage-aangel.md`
- [10] Radial blur en Premiere con el plugin gratuito Any Radial Blur y máscara (@colo.sparta) — reel de Instagram, archivo local · `references/lecciones/radial-blur-premiere-con-mascara-colo-sparta.md`
- [11] Botón «let's collaborate» tirado con una mano dibujada (@xitij) — reel de Instagram, archivo local · `references/lecciones/boton-collaborate-con-cuerdas-xitij.md`
- [12] Prompt Motion: catálogo de 265 motions hechos con Claude (promptsmotion.com) — https://www.promptsmotion.com/ · `references/lecciones/prompt-motion-catalogo-265-motions-hechos-con-claude.md`
- [13] Motion en código: render determinista con seek(t), springs y motion blur (promptsmotion.com) — https://www.promptsmotion.com/ · `references/lecciones/motion-en-codigo-render-determinista-seek-springs-y-motion-blur.md`
- [14] Lanzamiento de producto en código: dirección, beats y prohibidos (promptsmotion.com) — https://www.promptsmotion.com/ · `references/lecciones/lanzamiento-producto-en-codigo-direccion-beats-prohibidos.md`
- [15] Cámara 3D de After Effects: crear, controlar, profundidad de campo y mover con keyframes — https://youtu.be/qO3_WBYCe-E · `references/lecciones/camara-3d-after-effects-controles-peter-kasilo.md`
- [16] CC Composite: contraste, relleno de texto y texturas — Boone Loves Video · https://youtu.be/aHLMdk9W7Rc · `references/lecciones/cc-composite-after-effects-boone.md`
