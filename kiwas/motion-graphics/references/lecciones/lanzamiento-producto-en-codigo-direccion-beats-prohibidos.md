# Lanzamiento de producto en código: dirección, estructura por beats y lista de prohibidos
> Cómo se pide un video de producto de nivel Apple/Stripe: un solo plano continuo, objetos que se transforman, UI real y reglas negativas explícitas.

- **Fuente**: entradas largas de https://www.promptsmotion.com/ (Frame by Frame, Photo print, Food craving, UGC ad, UI morph, Orange dot, Ora 2, TechHalla, Spotify, Taxtello y paper-style film)
- **Fecha**: 2026-10-28
- **Tipo de "oídos"**: texto de los prompts
- **Tipo de "ojos"**: hojas de 6 fotogramas de 8 de ellos
- **Confianza**: media

## Teoría (la fórmula que repiten los prompts)
- **Bloques del prompt**: `<inputs>` (qué pedir al usuario y valores por defecto si los omite) → `<direction>` (formato, sensación, paleta, tipografía, cámara, lista de prohibidos) → `<structure>` (compases y beats con qué pasa en cada uno) → `<build>` (técnica) → `<gotchas>` → `<start>` (preguntar entradas y mostrar mapa de beats + 4 fotogramas antes de escribir todo).
- **Dirección**:
  - **Un plano continuo**: cada escena sale de la anterior; «nada se desvanece, desenfoca ni corta»: los objetos cambian de forma (texto que sube desde una línea de máscara, iconos que saltan con un spring desde cero, barras que se dibujan, una forma negra que inunda el cuadro y se contrae a la siguiente escena).
  - **Cursor protagonista** con clics, arrastres y pulsaciones largas reales; la cámara hace zoom «tipo Screen Studio» y el cursor escala con ella.
  - **UI real** del producto (capturas, componentes, logo vectorial), no inventada; no inventar funciones, números ni citas.
  - **Un acento** (naranja #F0442C en una entrada, lima en otra, oro #E8B84B en Taxtello) y una o dos tipografías (Geist/Inter; Archivo para wordmark; Anton/Caveat en el estilo papel).
  - **Cristal líquido** (iOS 26): congelar y desplazar el fondo detrás del control, borde brillante, sombra de elevación; en blanco desaparece, así que añadir un aura pastel o lavado de la foto detrás.
  - **Ritmo**: algo en cada beat; 120–130 BPM; el drop de la música cae en el clímax (el zoom, el cristal, el verbo); el respiro en el breakdown; el último fotograma = el primero.
- **Prohibidos que aparecen una y otra vez**: fundidos cruzados, borrosos de entrada, destellos blancos, voltear en 3D, partículas, glows en el texto de UI, neón, rejillas de suelo, cámara temblorosa, anillos de onda de choque, división RGB, easing rebotón, degradados en la UI, glassmorphism en todo, plantillas, párrafos largos, clichés de IA (cerebros, robots, redes neuronales, destellos), «bounce», retenciones de más de 1 s, texto en las esquinas (típico de IA). Una entrada permite un solo corte seco y lo declara.
- **Tipografía cinética con estructura** (TechHalla, discurso): sistema de tres fuentes (display ultra condensada, grotesca urbana, mono para etiquetas); tracking display −40 a −80, mono +20; mensaje bloqueado palabra por palabra («sin slogans extra»); desalineación de impresión de 2–4 px en magenta y verde ácido solo en fotogramas de impacto; revelado por máscara usando el contorno de la palabra que sale; revoltijo con Fisher–Yates con semilla por glifo; micro-respiración 1,000→1,012→1,000 para el loop.
- **Palabras con rol arquitectónico** (discurso «BUILD THE FLOOR»): WAIT es un dintel, WAITING una carga suspendida, VOICE un soporte, ROOM una abertura, FLOOR una plataforma; los roles salen de las letras reales; mantener 400 ms de quietud absoluta una vez; el final se apoya en lo que construyeron las palabras anteriores; debajo del todo el cuadro vuelve al inicio tras una oclusión total.

## Práctica (lo que se ve)
- Spotify: escenario negro redondeado ≈80 % del ancho, fondo verde esmeralda atmosférico, barra de reproductor persistente «secundaria».
- Orange dot: lienzo hueso → círculo naranja que llena el cuadro → cuadrado negro rotando → anillo de texto → cierre oscuro.
- TechHalla: tipografía enorme; palabras cambiando por máscara; cierre con barra magenta y regla verde en L.
- Ora 2: lienzo blanco, un solo tipo de letra, tarjeta de resultado que cambia por beat, rejilla 3×3, nube de 120 imágenes que forma el logo.

## Método
1. Escribir el prompt con los 6 bloques.
2. Antes de animar: mapa de beats y 4 fotogramas (apertura, momento «cristal», escenario, cierre).
3. Una forma que se transforma como hilo conductor (punto naranja, pill negra, wok, logo).
4. Revisar la lista de prohibidos y, al entregar, el último fotograma contra el primero.

## Para MUKIWA
- Hilo conductor posible: el punto de la I (pupila/ojo) que pasa de UI a letra, gráfica y forma; acentos lime y blue sobre negro, sin degradados en UI.
- Glass: solo en controles, con borde cromático azul/lima (según las reglas de la marca); no cubrir el fondo entero.
- Para los reels de MUKIWA: prohibir de antemano los clichés de IA y el texto en las esquinas.

## Límites
- No se vieron los prompts completos de las entradas truncadas por la web en nivel de código (solo el texto mostrado).
- Los nombres de los efectos de cristal vienen del prompt; no se vio su implementación.
- Sin audio: lo dicho sobre sonido es lo escrito en los prompts.

## Conecta con
- [[motion-en-codigo-render-determinista-seek-springs-y-motion-blur]]
