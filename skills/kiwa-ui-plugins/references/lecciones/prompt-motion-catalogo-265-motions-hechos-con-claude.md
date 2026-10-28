# Prompt Motion: catálogo de 265 motions hechos con Claude en código
> Qué hay en la biblioteca promptsmotion.com, qué entradas traen método de verdad y cuáles solo muestran el resultado.

- **Fuente**: https://www.promptsmotion.com/ (biblioteca en francés/inglés, 265 entradas, cada una con video, prompt y a veces stack) · leída el 2026-10-28
- **Fecha**: 2026-10-28
- **Tipo de "oídos"**: texto de las 265 páginas (el prompt de cada una). Sin audio.
- **Tipo de "ojos"**: hoja de fotogramas (6 por video) de 11 videos escogidos, no de todos. Lo demás es solo texto.
- **Confianza**: alta en el texto de los prompts; media en lo visual (muestra pequeña); los parámetros son «según el prompt», no medidos en el video.

## Qué es
Galería de videos de motion generados por Claude (Opus 5.5 en las fechas vistas, sep–oct 2026) a partir de un prompt, casi siempre como HTML/JS o Remotion renderizado a MP4. Cada entrada: video, autor de X, prompt, modelo/esfuerzo/fecha. Un generador de prompts y un curso son de pago (no se vio ni se usó).

## Teoría (lo que dicen los prompts)
- **Dos familias de prompt**:
  - **Cortos (≈240 de 265)**: «haz un showreel dinámico de 15 s que demuestre lo gran motion designer que eres, ve a por todo» (≈95 entradas son variantes de este) o «haz un video de lanzamiento de [producto]». Dan resultado variado: el método lo pone el modelo.
  - **Largos con dirección (≈24 con más de 900 caracteres)**: traen entradas a pedir, dirección de arte, estructura por compases, instrucciones de construcción, trampas conocidas y arranque. Son las únicas con técnica transferible (ver lecciones 2 y 3).
- **Categorías de la web** (una entrada puede tener varias): Charts 155, Kinetic type 126, Product UI 86, Music 56, Code 52, Characters 51, Diagrams 38, Photos 36, Shapes 30, Particles 21, Phone 8, HyperFrames 5.
- **Herramientas que aparecen**: Remotion (15 entradas), HyperFrames (5), GSAP (3), Blender y Blender MCP (6), Three.js (5), Lottie (2), Manim, Playwright + ffmpeg (render), ElevenLabs (voz), Mixkit (música y SFX libres), Suno, Magnific MCP (imágenes y video de IA).
- **Skills/plugins de terceros nombrados** (solo referencia; no se instaló nada): `remotion-dev/skills`, `greensock/gsap-skills`, `LottieFiles/motion-design-skill`, `heygen-com/hyperframes` y `hyperframes-community-skills` (p. ej. `session-story`), `Leonxlnx/cinetic`, `Rieranthony/product-film-skill`, `lemomo-ai/lemo-opuscar`, `Nova0x2/ai-film-producer-skill`, 21st.dev (componentes UI reales), whatships.com (videos de referencia).
- **Flujo profesional de una entrada (N54)**: 1) elegir 1–2 videos de referencia y pedir que los iguale («nombrar un estilo funciona mejor que describirlo»; sin referencia el modelo cae en texto centrado, fondo degradado y todo con fade); 2) instalar HyperFrames o Remotion para que cada escena sea código; 3) usar componentes UI reales (21st.dev) en vez de los inventados; 4) volcar contexto (logo, colores, fuentes, capturas del producto, referencia, ideas) y pedir 3 storyboards; 5) elegir uno y pedir **un fotograma fijo por escena antes de animar**; 6) dar notas como director («baja todos los zooms a 0,7×», «corte seco aquí», «empuja sobre el botón»): las palabras de cámara dan exactamente el cambio.
- **Otro flujo (Remotion)**: definir duración y fps primero (20 s a 30 fps = 600 fotogramas), mapear cada momento clave a un fotograma y pedir cambios **por rango de fotogramas** para no romper el resto (entradas de Remotion).
- **Otro flujo (en pasos)**: en vez de un prompt largo, dividir en desglose de referencia → especificación escrita → datos → cada escena; si una parte falla se corrige ese paso (entrada de Lottie + Remotion).

## Práctica (lo que se ve)
Muestra de 11 videos (6 fotogramas c/u), coinciden con su prompt:
- **Comparativa «remake»** (notdwd, 12 s, 1920×1080): cada fotograma muestra dos paneles lado a lado (original y rehecho): app clara, icono con cuatro cuadrados orbitando, barra de menú, tarjetas, y cierre en negro con wordmark brillante.
- **Spotify** (brainextends, 18 s): escenario negro redondeado sobre fondo verde atmosférico, portadas de colores, barra de reproducción fija abajo, cierre con wordmark.
- **TechHalla** (20 s, 1080×1080): tipografía gigante negra/blanca/verde ácido/magenta, marcos de esquina en mono, barra de «registro» desplazada.
- **Orange dot** (ultimaxbt, 15 s): «Reduce Motion» → «Motion» con letras que se curvan, gráfica con el punto naranja, cuadrado negro que gira dentro de un círculo naranja, anillo de texto en órbita.
- **Print app** (twoclipping, 29 s, 1440²): botón «Develop» negro, foto de paisaje, pantalla de bloqueo con reloj, página web, iris negro que cubre el cuadro.
- **Ora 2** (rossaxbt, 22 s): lienzo blanco, subtítulo que se escribe, barra de prompt con tarjeta de resultado, rejilla 3×3 de imágenes, deslizadores, nube de imágenes que forma el logo.
- **Showreel de técnicas** (lukasersil, 15 s): onda en rejilla de puntos, formas 3D con reflejo, tinta fluida «FLUID», «MOTION» con textura, cierre «SHOWREEL ’26».
- **Discurso como arquitectura** (gdgtify, 20 s): fondo verde oscuro, WAIT enorme como dintel, VOICE girada como soporte, línea base dorada que se deforma.
- **Tráiler de juego** (theparuchh, 38 s, 1280×720, 2,39:1): paisaje procedural con anillo luminoso, criatura, título «CINDERWAKE».
- **UI morph** (twoclipping, 4 s de vista previa): botón «Generate» → cargador → reproductor «motion study 02».

## Cruce teoría ↔ práctica
Los videos largos con dirección se ven mucho más cuidados que los de prompt corto de la misma galería (se alcanza a ver en los 11). Lo único que NO se puede comprobar desde los fotogramas: el timing exacto, los easings y el sonido.

## Método
1. Para un motion propio, usar el patrón de dirección de la lección «Motion en código: render determinista» y el de «Lanzamiento de producto».
2. Antes de pedir nada: referencia (video), contexto de marca, 3 storyboards, un fotograma por escena, y recién entonces animar.
3. Notas de director en palabras de cámara y fotogramas, no en adjetivos.

## Para MUKIWA
- Los prompts largos sirven de plantilla para videos de lanzamiento y para los plugins de MUKIWA; sustituir paleta por lime #C5ED2E / blue #0068FB / dark #232323 y prohibir los degradados neón y el glassmorphism en el cuerpo (ver reglas de glass de la marca).
- «Un fotograma fijo por escena antes de animar» encaja con el flujo de storyboard del departamento de dirección creativa.

## Límites
- 11 de 265 videos vistos con hoja de fotogramas; los otros 254 solo por su texto.
- Muchas entradas cortas son repeticiones del mismo prompt de showreel con otro tema: no aportan técnica nueva.
- Las vistas previas duran segundos; no se midieron duraciones ni easings.
- No se probó ningún prompt ni se instaló ninguna skill de las listadas.
- Algunos prompts mencionan claves o rutas privadas del autor: se ignoraron; ninguna se copió.
