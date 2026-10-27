# Guideify 2: cómo un plugin de Premiere muestra interfaz social y guías
> Demo de 39 s del competidor de KOMFRAK: el overlay no se dibuja sobre el monitor, se coloca como clip en una pista de video nueva; el panel solo tiene una vista previa pequeña.

- **Fuente**: https://youtu.be/ZcDtrjVuR5k · Guga dodashvili · 0:39
- **Fecha**: 2026-10-11
- **Tipo de "oídos"**: ninguno (solo-visual). Whisper no detectó voz; puede haber solo música.
- **Confianza**: media — 25 capturas, hueco máximo 2 s, un solo plano de grabación de pantalla; sin explicación hablada.

## Teoría (lo que se dijo)
- Nada: sin voz detectada ni subtítulos.

## Práctica (lo que se ve)
- [00:01–00:03] Se abre desde **Window > Extensions > Guideify**, no desde «UXP Plugins»: es una extensión CEP. En la misma lista: BadFX, Film Impact Dashboard, Premiere Composer, YouTube Downloader.
- [00:01] En Controles de efectos hay un clip `IMG-1920.png` seleccionado (posición 974/2039, escala 181): hay imágenes PNG en la secuencia. No se ve si ese PNG es del plugin.
- [00:05] Panel acoplado junto a Lumetri y Essential Sound. Cabecera con la secuencia: `2160x3840 · 30.01 fps · 9:16`. Dos pestañas: **Platform** y **Custom**. A la izquierda, una columna **PREVIEW** con un teléfono pequeño sobre fondo de cuadros (transparencia) y un botón de refrescar.
- [00:05] «Choose platform»: Saved Presets, TikTok 9:16, Instagram Reels, YouTube Shorts 9:16. Casilla «Also include custom guide». Sección «Saved presets» vacía con texto de ayuda.
- [00:07–00:13] Instagram Reels → Profile: interruptor **Verified**, foto circular con «Change photo» (abre selector de archivos y un modal «Crop photo · drag to move · slider to zoom» con Cancel / Use photo), **Username**, **Caption**.
- [00:17–00:25] **Engagement**: Likes, Comments, Repost, Shares; **Liked by**; **Other likes**; botón **Save preset**.
- [00:27] Tras **Apply**: mensaje verde «Overlay applied on V7 · 00:00–00:10» y la interfaz de Reels aparece en el Monitor de Programa. El overlay es un clip en la pista V7 con la duración de la secuencia (10 s).
- [00:27] Pie fijo del panel: casilla «Replace existing guide on apply», botones **Apply** y **Remove**, y una sección «Active Guides on Timeline» con refrescar.
- [00:29–00:35] Pestaña Custom: **My presets** (desplegable, Save, Delete); **Grid** rows/columns con Reset; **Margins (%)** top/bottom/left/right con candado e interruptor; **Gutter (%)**; **Overlays**: Margin box, Rule of thirds, Center cross, Action safe (90%), Title safe (80%), Diagonals; **Appearance**: Opacity 80, Line thickness 1, Guide color en hex más 8 muestras.
- [00:37–00:39] Segundo Apply: mensaje «…V8 · 00:00–00:10»; la cuadrícula verde aparece en el monitor encima de la interfaz de Reels. Se apilan en pistas distintas cuando no se marca «Replace».
- La vista previa del panel muestra solo el overlay sobre negro, no el cuadro del video.

## Cruce teoría ↔ práctica
- Sin teoría. Lo mostrado sin explicar: de qué tipo es el clip que se inserta (PNG, MOGRT u otro), si se desactiva al exportar y cómo se actualizan las plantillas.

## Receta paso a paso
1. Leer formato de la secuencia activa y mostrarlo en la cabecera.
2. Elegir plataforma o guía; editar datos; ver el resultado en la vista previa del panel.
3. Apply: generar el overlay e insertarlo como clip en una pista de video nueva, de principio a fin de la secuencia.
4. Informar en qué pista y en qué rango quedó.
5. Remove quita los overlays del plugin; «Replace» evita apilar.

## Para MUKIWA
- KOMFRAK: confirma que el método «capa en pista superior» es el que usa el competidor, y que un panel con vista previa pequeña más Apply/Remove es un flujo aceptado.
- Diferenciación posible: guías de composición (solo tiene cuadrícula, tercios, cruz, diagonales y márgenes), vista previa con el cuadro real, aviso para no exportar el overlay, y UXP.

## Límites
- No se vio el tipo de clip insertado, la exportación ni la instalación. La pista V7/V8 no aparece en la línea de tiempo visible (está fuera de cuadro).
- Demo de producto, no tutorial: sin valores de zonas seguras.

## Conecta con
- [[reel-8-recursos-composicion-guias-sobre-fotos]]
