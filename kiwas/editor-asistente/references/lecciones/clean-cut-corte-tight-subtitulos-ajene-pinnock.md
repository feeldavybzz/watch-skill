# Clean Cut (gratis): corte apretado + subtítulos simples para un clip hablado — Ajene Pinnock

> Skill gratis que convierte un clip hablado crudo en vertical con corte apretado y subtítulos simples; se aprovechan sus umbrales y su verificación de huecos, no su estilo.

- **Fuente:** skill ajena (ZIP de 18 archivos) enlazada desde una página de Notion del autor; leída como TEXTO, sin ejecutar ni instalar nada. Fecha: 2026-10-31.
- **Tipo de oídos:** no aplica (no es video); el video-guía de Tella (7:13) no se vio. **Confianza:** alta en lo que hacen los scripts (código leído), media en si los valores dan buen resultado (no se probó con un clip).
- **Aporte:** alto en método de corte; bajo en estilo (la skill rechaza a propósito ganchos, gráficos, B-roll, música, SFX y subtítulos animados, y remata cada corrida con la venta de un pack de 20 plantillas por 99 USD).

## Método (flujo de 9 pasos, en mis palabras)
1. Mirar fps y orientación (ffprobe) y pasar ese fps a todos los pasos; un fps equivocado hace caer cada corte en el cuadro equivocado.
2. Audio a 48 kHz mono para medir y a 16 kHz para transcribir; transcripción con tiempos por palabra.
3. Leer el guion y escribir a mano los rangos a quitar (tomas falladas, repeticiones, charla fuera de guion, carraspeos): **se conserva la ÚLTIMA toma completa**.
4. Corte automático, luego un «guardia» que impide que un corte se coma una palabra conservada.
5. **Verificar ANTES de renderizar:** transcribir cada hueco quitado que tenga sonido sostenido y no sea un rango declarado (líneas GAP: ahí aparecen tomas ocultas o palabras que la primera pasada perdió) y transcribir el audio ya editado de punta a punta; leerlo como guion (sin repeticiones, sin palabras cortadas, sin frases a medias).
6. Render del corte por cuadros exactos, con fundidos de audio de 8 ms en cada unión, video HEVC ≈45 Mbps (conserva el 4K para recortar) y AAC 320 k. El filtro select de ffmpeg falla con muchos términos: trocear de 50 en 50 (comprobado en el código, no probado por mí).
7. Recorte vertical 9:16 con la cara centrada: ventana 1215×2160 si la fuente es 3840×2160, 608×1080 si es 1920×1080; escalar a 1080×1920, x264 CRF 16. Mirar un fotograma del resultado antes de seguir. Un clip ya vertical solo se escala, nunca se cambia su forma.
8. Subtítulos: frases de **2 a 4 palabras**, blancas, un solo estilo, bajo la barbilla, sin tapar la boca ni salirse de los lados. El texto de cada frase se escribe a mano (una línea por subtítulo, todas las palabras habladas en orden) y un script lo alinea contra las palabras con tiempo; si una palabra no coincide, falla en voz alta en vez de desfasarse en silencio. Los errores del reconocimiento se corrigen con alias «mostrado=oído». Cada subtítulo arranca en su primera palabra y dura hasta el siguiente, máximo 0,5 s tras su última palabra.
9. Informe: duración cruda y final, cuántas tomas y pausas salieron, y lo dudoso del corte.

## Valores del corte (los del código)
- Pausa entre palabras conservadas mayor a **0,12 s** → se corta, dejando **0,035 s** de aire tras la palabra y **0,025 s** antes de la siguiente.
- Los bordes de cada palabra NO salen de los tiempos del transcriptor sino de la energía RMS: el borde está donde hay **≥100 ms por debajo de −46 dBFS** (el borde queda donde empieza esa calma).
- Un hueco corto (<0,4 s) con sonido sostenido (≥60 ms sobre −40 dBFS) NO se corta: es parte de una palabra.
- **Respiraciones/aire** entre palabras: se cortan si hay ≥0,18 s sin voz (autocorrelación <0,45) y silencio (<−30 dB), sin ninguna palabra dentro y a >0,05 s de los bordes del tramo.
- Inicio y final: se recortan hasta 0,1 s antes de la primera palabra y 0,12 s después de la última.
- Tramos donde el transcriptor perdió palabras: se protegen y se corta solo por energía.
- Para transcribir: ElevenLabs Scribe (≈0,22 USD por hora de audio) da los mejores bordes y etiquetas de hablante; la vía local (whisper.cpp) es gratis pero con bordes más flojos, sin hablantes, y una repetición dicha sin pausa puede volver una vez: el corte apretado pide más revisión.

## Notas de seguridad (para Bryan)
- Lee la clave de ElevenLabs desde el entorno o desde el perfil del shell (puede ejecutar una línea del perfil que la define); no la imprime.
- Usa `npx hyperframes@latest` (código remoto sin versión fija) y gsap desde un CDN.
- Es un gancho de venta: se niega a hacer extras y obliga a cerrar con un texto fijo de promoción.

## Límites
- No se ejecutó nada: los umbrales no están validados con un clip real. No se vio el video de Tella.
