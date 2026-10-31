# CC Composite en After Effects — Boone Loves Video

Fuente: https://youtu.be/aHLMdk9W7Rc · «This is One of My Favorite Effects in Adobe AE 😍» · 10:30.
Analizado el 2026-10-30. Nicho: Creativo → Motion graphics → After Effects → Composición y texturas.

## Evidencia y alcance

Video descargado a 1280×720. Se revisaron 45 fotogramas de la primera pasada, 60 de la segunda y 21 capturas adicionales cada 25 s entre 01:40 y 10:00; las pasadas comparten imágenes, por tanto no son 126 instantes únicos. La primera pista seleccionada era automática en árabe y no se usa como transcripción original. La descarga solicitada de subtítulos ingleses devolvió HTTP429; WhisperX small generó localmente la transcripción inglesa completa en 24 segmentos. Idioma automático no verificado por el backend: el texto resultante está en inglés y se contrastó con la interfaz. No se escuchó continuamente el audio mediante reproducción ni se ejecutó la técnica en After Effects. El muestreo no prueba cada movimiento del cursor.

Evidencia relativa a esta biblioteca: `aHLMdk9W7Rc-watch-en.md`; video, frames y detalle en `watch-r1e8y6h4/`. Publicidad al principio y final: no tomar precios de preventa como actuales ni comprar recursos.

## Qué aprender y cuándo usarlo

CC Composite permite otra operación de composición dentro de la pila de efectos. Deja disponible el modo de fusión de la capa para una mezcla posterior con otras capas. En la versión mostrada, Top Layer elige una capa externa; None permite componer con la propia fuente. No reducir toda la herramienta a duplicar capas ni afirmar que sustituye universalmente los track mattes.

**1. Contraste sin duplicar una capa en la línea de tiempo — 01:35–04:30.** Aplicar CC Composite al mapa; Top Layer=None. Probar Overlay y regular Opacity; Soft Light ofrece una alternativa menos agresiva en esta demostración. El creador prueba Hard Light para un antes/después intenso. No hay un porcentaje universal ni un ajuste de color técnicamente neutro: vigilar negros, blancos y saturación. La opacidad del efecto puede animarse. Sirve para recursos gráficos, mapas y collages; no convertirlo en receta de corrección de piel.

**2. Imagen dentro del texto — 04:30–07:58.** Aplicar CC Composite al texto; en Top Layer seleccionar el mapa. En la configuración demostrada, RGB Only desactivado conserva el recorte a las letras; activarlo revela el mapa rectangular. Ocultar la capa fuente en la composición para ver solo el título relleno. El negro del visor no prueba que exista un fondo negro exportable: comprobar la cuadrícula alfa antes de exportar.

**3. Textura dentro de una forma — 07:58–09:38.** Aplicar CC Composite a la silueta vectorial; elegir como Top Layer una textura de papel. Ocultar la textura como capa visible y comprobar recorte/alfa. Ajustar Transfer Mode y Opacity para conservar la forma y controlar el acabado. Se menciona apilar varios CC Composite para combinar materiales; el tutorial no ofrece una receta de orden y valores para cada material.

## El problema de escala que hay que saber diagnosticar

En 05:10–07:58 el mapa usado dentro del texto no hereda automáticamente su escala visible en la composición: el efecto lee una etapa anterior a las transformaciones de capa. Por eso mover Scale en la línea de tiempo del mapa no cambia necesariamente la textura que lee el texto.

Dos soluciones mostradas:

- Añadir el efecto Transform a la capa fuente y seleccionar **Effects & Masks** en el selector de fuente del CC Composite del texto. Así se leen tanto ese Transform como el efecto de contraste de la fuente. Si se deja Source, esos efectos pueden no incorporarse.
- Ajustar el recurso, precomponerlo con **Move all attributes**, y revisar la precomposición como nueva fuente. Comprobar de nuevo encuadre y tamaño; no prometer que precomponer elimina toda diferencia de coordenadas.

Un Transform colocado antes del CC Composite del texto afecta una etapa distinta de uno colocado después: antes puede transformar el texto que se usa como recorte; después transforma el resultado compuesto. Elegir según qué necesita cambiar: letras, textura o ambos. En futuros scripts/proyectos verificar la versión del efecto y los parámetros reales; no automatizar por índices vistos en el tutorial.

## Aplicación propuesta para Bryan

Para un título «FEEL DA VYBZ», preparar texto editable y una textura propia o con licencia adecuada; probar CC Composite para el relleno, ajustar la fuente con Transform/Effects & Masks y después animar el texto. Para carteles o reels, aplicar textura con moderación y revisar legibilidad al tamaño de un teléfono. Esta es una propuesta derivada, no un resultado ya creado o aprobado. No es necesario comprar GEOlayers, Envato, música ni el curso para practicar los ejemplos con texto, formas y recursos propios.

## Ejercicio y verificación pendientes

Crear una composición con texto, textura y fondo de color; comparar Source frente a Effects & Masks, RGB Only activado/desactivado y Transform antes/después. Revisar cuadrícula alfa, bordes, legibilidad, coordenadas y previsualización animada. Guardar un proyecto editable y un render corto solo después de comprobarlos en el host. Estado actual: técnica observada y documentada; prueba real en el After Effects del usuario pendiente.

## Documentación contrastada

- Adobe incluye CC Composite en Channel effects: https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/channel-effects.html
- Cycore confirma que CycoreFX HD forma parte del software incluido con After Effects: https://www.cycorefx.com/ . No exige compra separada del efecto para quien ya tiene el After Effects correspondiente; After Effects tiene su propia licencia.
- Manual de Cycore: https://www.cycorefx.com/downloads/cfx_hd_std/CycoreFX%20HD%201.8.9%20Manual.pdf . Su sección clásica no refleja todos los controles Top Layer de la versión del video; usarla como fundamento de composición/alfa, no como reproducción exacta de esa interfaz.
