# El curso de diseño web más corto del mundo: sitio vs. página, layout, responsive, breakpoints, tipografía, color y Atomic Design (Eze Cichello)
> Un video de 10:14 explica cómo se organiza un sitio web: grillas de 12 columnas, responsive y breakpoints (1440 / 768 / 320), un viewport de ≈800 px, jerarquías H1–H6, color de marca y semántico con contraste, y la metodología Atomic Design (átomos → moléculas → organismos → páginas).

- **Fuente**: https://youtu.be/VKdx96GitYA · «el curso de DISEÑO WEB más CORTO del mundo» · Eze Cichello · 10:14 · español rioplatense.
- **Fecha**: 2026-10-11
- **Tipo de "oídos"**: audio transcrito con faster-whisper (≈2 070 palabras) y cotejado con los subtítulos automáticos. Los **números** salen distintos en cada fuente: whisper «7.680» (tablet) y «10000/1.200»; los subtítulos dicen «**tablet 768**» y «1440 … otros 1200». Se usan los subtítulos.
- **Aporte del creador**: ALTO. Sin promoción; la descripción enlaza **dos recursos abiertos**: el verificador de contraste de **WebAIM** y el artículo de **Atomic Design** de Brad Frost (abrí ambos).
- **Confianza**: alta (las 12 hojas vistas; la primera redacción de «lo que se ve» se corrigió el 2026-10-11); las cifras se leen de voz y subtítulos, y «1920x1080» sale en pantalla.

## Qué NO es este video
- No habla de tendencias, plugins, herramientas ni efectos (lo dice al empezar).
- No muestra el diseño de una web real paso a paso ni Figma: son rótulos y ejemplos.
- No da márgenes, medianiles ni tamaños de tipografía.

## Teoría (lo que se dice)
- [0:00–1:19] Una **web es un sistema de decisiones** que debe funcionar en distintos dispositivos, con contenidos distintos y con usuarios que no dan segundas oportunidades. **Sitio web** = la totalidad; **página web** = una página puntual (como un libro y sus páginas): «estoy haciendo mi **sitio** web».
- [1:19–2:10] **Layout**: una web no es un collage; se usan **grillas** (como en editorial), respetadas, para mantener orden y consistencia visual y para que el programador **sepa qué hacer y mantenga tamaños y proporciones** (no tiene un Figma donde ir arrastrando). Generalmente en desktop **12 columnas**; se pueden sumar líneas horizontales.
- [2:10–3:05] **Responsive**: adaptarse automáticamente a **desktop, tablet y mobile**; las composiciones de desktop suelen ser horizontales, las de mobile 100 % verticales y las de tablet mezcla. **No es opcional ni solo achicar: es reorganizar** (recortar textos, cambiar alineaciones y escalas, ajustes tipográficos). Hay que **presentar una versión mobile**; si no, el desarrollador hará mil preguntas.
- [3:05–4:33] **Breakpoints**: el ancho de pantalla a partir del cual la web reordena el contenido. Para saber los *viewports*, usa el panel **Inspeccionar** de Chrome y emula dispositivos. Valores tradicionales: **desktop 1440** (hay quien usa 1200), **tablet 768**, **mobile 320 px de ancho**. **Un canvas de 1920 × 1080 es un error**: el **viewport** (la parte visible) suele ser de **≈800 px**; los otros ≈200–280 los ocupa la interfaz del navegador; si pones cosas muy abajo, quedan fuera. **Se diseña en 320** (la pantalla más chica), aunque muchos usan 390: así entra todo (título no demasiado grande; en alemán, «no entraba ni un solo título»).
- [4:33–5:39] **Tipografía**: pocas, bien usadas, con **jerarquía H1–H6**, tamaños de **body, caption y botones**; cada nivel tiene importancia **visual y semántica** (le dice al navegador, ayuda al SEO). Las jerarquías deben **funcionar con cualquier título**, sobre todo con contenido dinámico (un diario no puede reajustar el tamaño por cada nota). Vale también para un proyecto pequeño: «uno tiene que trabajar bien siempre».
- [5:39–7:21] **Color**: no es decoración, es un sistema con **tres funciones: dar identidad, informar y guiar**. **Colores de marca** (si tu marca es roja y amarilla, no estás limitado a esos dos: se puede ampliar la paleta, «branding digital»). **Colores semánticos**: verde (formulario completado), rojo (campo incompleto), amarillo (advertencia, contraseña débil): **tono alineado a la marca pero reconocible**. **Accesibilidad = contraste**: usa el **verificador de contraste de WebAIM**. Tipografías y colores son la **base del sistema visual**.
- [7:22–8:29] **Atomic Design**: «para diseñar una web, lo último que hay que hacer es diseñar una web». Metodología (de Brad Frost): **átomos** (tipografías, colores, imágenes, iconos, inputs) → **moléculas** (botones, barra de navegación, encabezados de texto) → **organismos** (módulos completos de ancho total: texto con imagen, formularios, carruseles) → **páginas** → **sistemas**. Ejemplo con YouTube.
- [8:29–10:00] **De sistema a sitio**: primero se define **qué páginas existen** (la home con un **hero** —el primer componente—, un bloque de texto con imagen y un llamado a la acción); **los bloques no se rediseñan cada vez**: de ahí nacen **consistencia y escalabilidad**. Si el cliente pide 10 productos más, cambias foto y texto y las páginas «se hacen solas». «Si cada página es una excepción, el diseño no es un sistema.» Cambiar algo en un lugar y que se replique en todo el sitio es «totalmente satisfactorio».

## Práctica (lo que se ve)
- **Estructura**: el presentador (camiseta blanca) a cámara en tres escenarios, con **tarjetas de capítulo** en negro grande sobre gris claro: «**Diseño Web**» (0:00) y «**UI**» (0:05, sobre un collage de elementos de iOS), «**Herramientas**» (0:23, sobre su rostro), «**¿Qué es una Web?**» (0:34), «**Layout**» (1:19), «**Responsive**» (2:14), «**Breakpoints**» (3:05), «**Tipografía**» (4:34) y «**Diseñar una web**» (7:23); y la cifra «**1920x1080**» en blanco sobre su rostro (3:42).
- **Layout** (1:32, 2:09): la web de una estudio de interiores («**Annie Downing Interiors**»: fondo rosado claro, tres imágenes dispersas y el texto «Annie Downing Interiors crafts spaces that are thoroughly modern and utterly timeless») para mostrar un layout con grilla.
- **Responsive** (2:21–2:25): un recuadro naranja liso que se convierte en tres versiones rotuladas «**Desktop**», «**Tablet**» y «**Mobile**» (una web de un edificio con vista al mar en desktop, una de muebles en tablet y una de moda en mobile).
- **Breakpoints** (3:11–3:27): la web roja «**Op/Intelligence**» (SHIFT) y el menú contextual de Chrome con «**Inspect**» resaltado (3:17); después un recuadro naranja liso otra vez (3:27).
- **Tipografía** (4:43 y 7:51): la pantalla oscura con la **escala Material** en dos columnas («Baseline» y «Emphasized») y, en fondo claro, la lista **DisplayLarge, DisplayMedium, Display Small, Headline Large, Headline Medium, Headline Small** con sus etiquetas pequeñas.
- **Color** (6:08–7:16): el logo de **McDonald's** sobre rojo y su web («McDonald's · Más que una hamburguesa», con «Post Dubai», «Frappés» y «Mi McDonald's»); la herramienta de **WebAIM** con un fondo magenta y un texto rosa, **Current Ratio 3.7:1** y los cuatro resultados «**Fail AA Normal · Fail AAA Normal · Pass AA Large · Fail AAA Large**» (7:09–7:16).
- **Atomic Design** (8:05–9:01): una tarjeta de web de viajes («**¿Estás planeando tu próxima escapada?**» con una ilustración de ciudad y un botón «Río de Janeiro»), un lienzo con elementos de la interfaz de YouTube y su logo (8:18, con la miniatura «Logos» y «El curso de TIPOGRAFÍA más corto del mundo») y una web de productos de limpieza con un hero naranja y azul, productos y logos de marcas (9:01).
- Cierra a 10:12 con pantalla negra.

## Cruce teoría ↔ práctica
- El video no da el **número de columnas** de tablet y mobile (solo 12 en desktop).
- **Solo se ve**: el ejemplo de contraste de **3.7:1** (pasa AA solo en texto grande); el creador no dice el umbral. Según WebAIM: **texto normal AA 4.5:1, AAA 7:1; texto grande AA 3:1, AAA 4.5:1; componentes UI 3:1**.
- **Solo se dice**: 12 columnas, 1440/768/320, 800 px de viewport.
- La cifra de **800 px de viewport** coincide con la de su video de brief web (donde aparece «800 px Desktop» en el boceto).

## Receta paso a paso
1. Define las **páginas** del sitio y los **bloques** que se repiten (hero, texto + imagen, CTA).
2. Elige **grilla de 12 columnas** en desktop (**1440 px**), **768** en tablet y **320** en mobile; diseña **primero en 320**.
3. Recuerda el **viewport ≈800 px**: lo importante tiene que verse sin hacer scroll.
4. Define jerarquías **H1–H6** y tamaños de body, caption y botón; que funcionen con cualquier título.
5. Define **color de marca ampliado** + **colores semánticos** y **verifica el contraste** (≥4.5:1 en texto normal).
6. Construye con **Atomic Design**: átomos → moléculas → organismos → páginas, sin rediseñar bloques.
7. Presenta las tres versiones (desktop, tablet y mobile).

## Para MUKIWA
- Landing de plugins y portfolio: grilla de 12 columnas, diseño primero en 320, jerarquía H1–H6 con la tipografía de marca (Satoshi) y botones consistentes.
- Verifica el contraste del lima #C5ED2E sobre #232323 con WebAIM antes de usarlo en texto pequeño.

## Límites
- No da márgenes ni tamaños de texto; el desktop de 1440 y el de 1200 son valores citados, no demostrados.
- No abrí la guía de pago.

## Conecta con
- [[antes-de-figma-mapa-cinco-preguntas-eze-cichello]]
- [[ux-ui-curso-mas-corto-eze-cichello]]
