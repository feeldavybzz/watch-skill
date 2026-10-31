# Escenas consistentes con Seedance 2.5: referencias, audio primero y dirección de escena (AiLendra Labs)
> Una guía pública enseña a dirigir una escena de video IA decidiendo primero qué no puede cambiar, preparando hojas de referencia y el audio antes de gastar en el video.

- **Fuente**: https://ailendra.com/ailab/lite/seedance-25-escenas/ · AiLendra Labs (guía escrita con audio y video de ejemplo) · página pública gratuita
- **Fecha**: 2026-10-15
- **Tipo de "oídos"**: ninguno (guía escrita; el MP3 y el video de ejemplo de la página no se abrieron)
- **Aporte del creador**: MEDIO. Método claro y transferible; la página también promociona su comunidad y su skill, y dice que el prompt original completo de la toma «queda pendiente de incorporar».
- **Confianza**: media-baja. Es un resumen de la página, sin ver el resultado ni probar nada en Higgsfield o Seedance.

## Qué NO es esta fuente
- No trae el prompt original completo del video (la propia página lo dice); los bloques de cámara y estética son ejemplos para adaptar.
- No enseña a montar ni a corregir fallos de una toma; para eso, la lección de Higgsfield.

## Teoría (lo que dice la guía)
- Idea clave: **no empieces por un prompt de video**. Decide qué no puede cambiar (caras, vestuario, lugar, objetos, sonido) y después dirige lo que sucede dentro de ese mundo.
- **Tres pasos**: referencias visuales (con GPT Image 2.5) → dirección sonora (con Seed Audio) → dirección de escena (con Seedance 2.5).
- **Referencias**: una hoja por función, no solo imágenes bonitas. Identidad (rostro legible, varios ángulos), cuerpo y vestuario (proporciones, ropa, accesorios), mundo (luz, materiales, paleta) y objetos importantes (cada uno en su referencia).
- **No dejes detalles importantes a la interpretación**: si el personaje debe tener objetos concretos sobre la mesa, ponlos en una referencia. Adjunta solo las hojas que intervienen y explica la función de cada una. Una referencia de estética no tiene que ser el primer fotograma.
- **Sonido antes que video**: generar e iterar audio cuesta menos que repetir una escena completa. El prompt de audio separa tres decisiones: **textura** (micrófono, ruido, proximidad), **voces** (quién, acento, actitud, cómo dice cada frase) y **eventos** (qué se oye, cuándo entra, qué queda de fondo). Se pueden plantear varios interlocutores y combinar diálogo, ambiente y efectos.
- El ejemplo de prompt de audio tiene duración exacta (16 s), «cero música, cero narrador», una sección de estética y otra de ejecución con etiquetas por evento (ambiente, diálogo, evento, transición) y tiempos sueltos (un clic de mechero a 2,2 s, corte duro a 16,0 s).
- **Escucha el audio entero** (frases, interlocutores, pausas, sonidos) y corrígelo antes de pasar al video.
- **Dirección de escena**: adjunta las imágenes relevantes y el audio aprobado; explica qué mantiene cada referencia, quién actúa, cómo se mueve la cámara y qué textura tiene la imagen.
  - Actuación: quién habla, qué mira, qué gesto acompaña cada frase; quien escucha respira, cambia de postura, reacciona (no una cara congelada). La referencia fija la identidad; el prompt define la interpretación.
  - Cámara: no basta «handheld»; describe a una persona grabando (pequeñas oscilaciones de mano, microajustes imperfectos, paneo que llega ligeramente tarde). Intensidad contenida: nada de gimbal flotante, órbitas ni sacudidas exageradas.
  - Estética: textura de camcorder doméstica de los 2000 (CCD), imagen algo suave, color de cámara de consumo, pequeños ajustes de exposición, conservando la luz de la referencia del entorno; y define lo que **no** buscas (piel pulida, nitidez artificial, HDR sintético, iluminación de anuncio).
- **Revisión antes de generar**: hojas que no se contradicen, función explícita de cada referencia, audio con las palabras y el ambiente correctos, prompt que dirige actuación y cámara, orden de archivos que coincide con lo que pides, y revisión final de caras, manos, objetos y sincronía.
- Las referencias y el prompt ayudan a controlar, pero no garantizan identidad ni sincronía perfectas. Trabaja por escenas y cambia una variable cada vez.
- Aparte, la página enlaza un video suyo sobre cómo reducir un 80 % el coste de Seedance 2.5 (no se vio).

## Práctica (lo que se ve)
- No aplica: no se abrió el video de ejemplo (16 s, formato 4:3) ni el MP3.

## Cruce teoría ↔ práctica
- Sin cruce posible. Coincide con la lección de Higgsfield en referencias con función clara y dirección de actuación y cámara; solo esta añade el audio como primer paso y la lista de lo que no se busca.

## Receta paso a paso
1. Escribe qué no puede cambiar (caras, vestuario, lugar, objetos, sonido).
2. Crea una hoja por función y revisa que no se contradigan.
3. Diseña y genera el audio (textura, voces, eventos); escúchalo entero y corrígelo.
4. Escribe el prompt de video asignando el rol de cada referencia según el orden real de los archivos, con actuación, cámara y estética (y lo que no se busca).
5. Una escena a la vez, una variable por iteración; revisa caras, manos, objetos y sincronía.

## Para MUKIWA
- Personajes recurrentes de la marca (p. ej. Arenio) como hojas de referencia fijas; paleta lime #C5ED2E / blue #0068FB / dark #232323 como referencia de mundo.
- Sirve igual para anuncios y reels de Creative Direction: decidir sonido antes del video ahorra créditos.

## Límites
- Resumen de una página, sin ver ni oír los ejemplos. Sin prompts completos ni valores de Seedance (duración máxima, resolución) ni costes.
- La página de recursos gratuitos de AiLendra (https://ailendra.com/ailab/lite/) lista «Character Sheets Prompts» (dos variantes) y tres plantillas editables de GPT Image 2.5; de ellas solo se leyeron los títulos y descripciones, no los prompts.

## Conecta con
- [[dirigir-anuncio-con-video-ia-higgsfield-seedance]]
