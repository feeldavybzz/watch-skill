# Motion en código: render determinista con seek(t), springs y motion blur
> El método que se repite en los prompts largos: toda la animación es una función pura del tiempo y se renderiza por subfotogramas.

- **Fuente**: 14 entradas largas de https://www.promptsmotion.com/ (Frame by Frame, Photo print, Ora 2, UGC ad, UI morph, Orange dot, Food craving, TechHalla, Spotify, discurso como arquitectura, glitter sticker, Remotion SaaS, tráiler de juego y paper-style film)
- **Fecha**: 2026-10-28
- **Tipo de "oídos"**: texto de los prompts
- **Tipo de "ojos"**: 6 fotogramas de 9 de esos videos (resultado, no proceso)
- **Confianza**: media — son instrucciones que el autor dio a Claude; la técnica es coherente entre entradas, pero no se ejecutó aquí.

## Teoría (lo que dicen los prompts, siempre con la misma base)
1. **Un solo HTML, una función `seek(t)`**: cada estilo se calcula a partir del tiempo; sin transiciones CSS, sin timers, sin estado entre fotogramas, sin `Math.random` (aleatoriedad con semilla). El último fotograma = el primero si debe hacer loop (incluida la posición y velocidad del cursor).
2. **Springs en forma cerrada (respuesta al escalón)**, no simulación acumulada. Un valor con varios objetivos = suma de un spring por cada cambio, así sigue siendo función pura del tiempo. Los bordes de un indicador de pestaña (o la perilla de un toggle) van en springs distintos: el borde delantero se estira antes que el trasero.
3. **Arrastres como manipulación directa**: mientras el cursor está presionado el valor sale de su posición; al soltar, el spring vuelve desde donde estaba.
4. **Cámara única en un contenedor**, con pistas `[tiempo, zoom, x, y]`, zoom interpolado en escala logarítmica y tramos suavizados; el empuje va de 1,0 a 1,04–1,08. Nunca dos movimientos de cámara a la vez ni deriva aleatoria. Al pasar de escena, comenzar en el zoom donde terminó la anterior (si se reinicia a 1,0 el zoom salta).
5. **Motion blur por subfotogramas**: render con Playwright a 60 fps, con 3, 4 u 8 subfotogramas por fotograma, mezclados con `tmix` de ffmpeg (3 subfotogramas en t−, t y t+1/240 s). Con 4 quedan copias fantasma en movimientos rápidos: usar 8 y ralentizar el movimiento.
6. **Beat grid**: analizar la canción con numpy (tempo, rejilla de beats, energía por compás, el drop); calibrar con los golpes reales del bombo; empezar en un tiempo fuerte; algo debe pasar en cada beat (en 120 BPM, un dieciseisavo = 125 ms). Los cortes duros caen 2 fotogramas antes del beat (≈ el prompt de «Frame by Frame»: beat k = 0,048 + 0,4838·k s a 124 BPM).
7. **Sonido**: un efecto descargado de Mixkit por cada evento (nunca sintetizado), colocado por su **pico medido**, no por el inicio del archivo; acortar los risers de 4 s; música con ducking bajo la voz (3 bandas, p. ej. graves 30 %, medios 85 %, aire 55 %; retención 0,3 s, anticipo 50 ms, release 0,5 s); locución ≈9 dB sobre la música entre 300 Hz y 4 kHz; masterizar a −14 LUFS (−2 dBTP, re-medido tras el AAC en una entrada).
8. **Verificación antes del render final**: hoja de contacto con un fotograma por beat (o 8 fotogramas clave), buscar «pops» de un solo fotograma (picos de diferencia entre fotogramas ≥3× los vecinos; solo los dieciseisavos pueden saltar) y revisar legibilidad; en una entrada, un revisor externo que no construyó la pieza.
9. **Vídeo real dentro del HTML**: extraer clips a secuencias JPEG a 30 fps (o recodificar all-intra con `-g 1`), cargar como blob y esperar `seeked` antes de dibujar. `python -m http.server` no hace seek por rangos.
10. **Estructura de archivos de producción** (Remotion): todas las señales en `timeline.ts` (en beats) y todos los textos en `copy.ts`; las escenas no llevan números mágicos. Renders por fotograma de prueba antes del completo.

## Práctica (lo que se ve)
Los videos de la muestra cumplen el patrón de «una forma que se transforma» y de cámara limpia: p. ej. el punto naranja pasa de UI a letra, gráfica y círculo que llena el cuadro (ultimaxbt); en el de impresión, un círculo negro cubre todo y se contrae al siguiente escenario (twoclipping, fotograma 22 s).

## Cruce teoría ↔ práctica
Coinciden las formas de transición; no se pudo verificar con fotogramas el motion blur ni el spring (se ven en movimiento).

## Receta paso a paso
1. Fijar tamaño, fps y duración (p. ej. 1920×1080 a 60 fps, 15 s; o 1440² para cuadrado) y la rejilla de beats.
2. Escribir `seek(t)`: capas con estilos computados desde `t`; un spring cerrado por cada cambio de objetivo; cámara en pistas.
3. Poner a mano las 8 imágenes clave (una por beat) y revisar antes de animar.
4. Renderizar con Playwright con N subfotogramas y mezclar con `ffmpeg tmix`; subir a 8 si hay fantasmas.
5. Colocar SFX por pico; masterizar a −14 LUFS.
6. Revisar pops de un fotograma y legibilidad; recién entonces entregar.

## Trampas conocidas que dan los prompts
- `backdrop-filter: url()` lee mal los mapas de desplazamiento en Chromium: clonar la escena detrás del cristal.
- Una inundación de color debe sobreescalar pasados los 4 bordes y durar ≈0,35 s; si no, parece un destello.
- Un hijo con `visibility: visible` se ve aunque el padre esté oculto: usar `inherit`.
- Texto que cambia dentro de una forma que se transforma necesita su propia máscara y tiempos de entrada/salida (si no se solapa).
- Nunca poner `will-change` en lo que la cámara escala (texto borroso); no poner `opacity` ni `filter` en un elemento `preserve-3d` (se aplana y se ven ambas caras): desvanecer el contenedor.
- Declarar todas las variables antes de la primera llamada a `seek()`.
- Medir posiciones de elementos en tiempo de ejecución para los match cuts.
- Un fade de 0,05 s parece una aparición instantánea; un resaltado detrás de la palabra parece selección de Windows (lo dice el prompt de Ora 2).

## Para MUKIWA
- Convertir esto en una plantilla de prompt MUKIWA: lienzo oscuro, lime y blue como únicos acentos, sin neón ni degradados en la UI, un punto/«pupila» recurrente (como el punto de la I) que conecta escenas.
- Útil para los plugins: la misma función `seek(t)` sirve para las animaciones de perillas y botones (ver skill de UI de plugins).

## Límites
- No se probó ninguna receta aquí; son instrucciones de terceros.
- Los números de springs (constantes) no aparecen: solo «pequeño overshoot» y «sin rebote».
- Música y SFX de Mixkit: confirmar licencia antes de usar comercialmente.

## Conecta con
- [[prompt-motion-catalogo-265-motions-hechos-con-claude]]
