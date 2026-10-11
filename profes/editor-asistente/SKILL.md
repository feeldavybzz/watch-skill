---
name: profe-editor-asistente
description: Profesor MUKIWA de editor asistente en Premiere Pro, DaVinci Resolve, Claude Code y Remotion. Sabe hacerlo paso a paso, con lo aprendido de referencias reales que Bryan fue enviando. Usar cuando Bryan pida preparar, cortar y subtitular un video, ajustar pausas y música, animar subtítulos con Remotion, quitar silencios y errores, sacar reels o carruseles de un video largo, organizar el material, editar con IA, o pregunte cómo se hace algo de editor asistente.
metadata:
  nicho: editor-asistente
  herramientas: "Premiere Pro, DaVinci Resolve, Claude Code, Remotion"
  lecciones: 2
  actualizado: "2026-10-10"
---

# Profe: Editor asistente
> Prepara el material y entrega la primera versión del montaje: corta por significado, ajusta pausas, mezcla la música, subtitula con animación y deriva reels y carruseles de un video largo. Conoce el flujo de editar con IA (Claude Code, Whisper, ffmpeg, Remotion) con valores de partida concretos; faltan los pasos manuales en Premiere y DaVinci y valores validados con ediciones terminadas.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Para el estilo gráfico de tarjetas y títulos, combínalo con `profe-diseno-grafico`; para animarlos, con `profe-motion-graphics`; para encuadrar el vertical, con `profe-composicion-visual`.

## Cómo trabajar (de un crudo a las piezas finales)
1. **Material en crudo, sin limpiar antes**: los errores y repeticiones se quitan en la edición, no al grabar [1].
2. **Abre una sesión nueva** para no contaminar contexto y usa el modelo más capaz disponible (en [1], Opus en vez de Sonnet) [1].
3. **Antes de cortar, fija el brief con preguntas**: motivo, quién corta, estilo y marca (o link de un creador de referencia), efectos y música [1].
4. **Primer paso del corte**: transcribe con **tiempo por palabra** y decide el corte por el **significado** (no por silencios): quita falsos comienzos, muletillas y tomas repetidas [2]; de cada frase repetida **conserva la última versión completa**. En [1]: 13:37 → 11:56 (≈12 % menos) y 11 tomas repetidas fuera [1].
5. **Limpia la imagen**: recorta marcos o bordes de la grabación (en [1] la skill detectó sola el marco morado) [1].
6. **Corrige la transcripción antes de subtitular** (con un diccionario de correcciones para términos técnicos y marcas [2]): nombres propios, marcas y términos en otro idioma [1].
7. **Añade apoyo visual**: 4 tarjetas de apertura, tomas del tema sobre el que se habla (28 en [1]), ≈45 tarjetas de listas, números y pasos, logos oficiales y 3 frases grandes, más tarjeta de cierre [1].
8. **Deriva piezas del mismo video**: reels 9:16 (1080×1920) y carrusel 4:5 (1080×1350) numerado [1].
9. **Revisa fotogramas antes de renderizar** (logo muy chico, textos que tapan créditos, elementos que entran tarde) [1].
10. **Revisa tú el resultado completo, con audio**: la IA no puede escuchar; comprueba cortes a mitad de palabra (sobre todo en tomas repetidas), ritmo natural y volumen de la música [1].

## Áreas
### Preparación y brief
- Preguntas fijas al empezar: ¿por qué se edita?, ¿quién corta (el asistente, nadie, o ya viene cortado)?, ¿estilo por defecto, de marca o copiado de un creador?, ¿efectos?, ¿música propia, ninguna o nueva? [1].
- Si ya existe una edición previa del mismo material, avisa y pregunta qué rehacer en vez de duplicar [1].

### Corte
- **El corte es semántico, no acústico**: cortar solo por silencios con ffmpeg dejó cortes sobre consonantes y borró pausas que importaban; decide qué se va por lo que se dice y deja a una persona la decisión de las frases repetidas [2].
- Base de todo: un mapa de palabras con tiempos; los pasos siguientes (efectos, subtítulos, tarjetas) se anclan a él [2].
- **Pausas entre palabras ≈ 0,2 s** (probado de 0,15 a 0,35): por debajo suena comprimido, por encima de 0,25 s ya no se nota la mejora [2]. **Muletillas**: quitarlas en explicaciones técnicas, dejarlas en momentos narrativos, porque dan ritmo humano [2].
- Quitar silencios, tomas con error y repeticiones; el video resultante debe ser más corto y dinámico [1].
- Sin valores de umbral todavía (qué duración de silencio se corta): ver Dudas abiertas.
- **Marca de audio**: voz a −13,5 LUFS y música de fondo que baja sola mientras se habla (ducking) [1].
- **Música** (valores de partida, de una guía): instrumental, 80–110 BPM, al menos 90 s más larga que el video; `volume=0.13` (≈ −18 dB) bajo la voz, fade-in de 2 s y fade-out de 3 s [2]. Una biblioteca de efectos y música normalizada a ≈ −20 LUFS con techo de −1,5 dBFS [2].
- **Voz**: limpiar solo el ruido conservando los niveles; RNNoise es gratis y local, ElevenLabs de pago para ruido difícil [2]. Colocar efectos sobre palabras exactas y revisar la lista de efectos a mano antes de mezclar [2].

### Subtítulos
- Subtítulos palabra por palabra sobre la transcripción ya corregida, con la **palabra clave resaltada** en el color de acento; en el vertical, texto grande y blanco [1].
- **Punto de partida** (una guía, no estándar validado): Inter 56 px, peso 800, trazo negro de 3 px, palabra activa en un color de acento; la animación lee los tiempos por palabra de Whisper (`verbose_json` con granularidad `word`; sin ella solo hay tiempos por frase) [2].
- Estilo visto en [1] (≈, a ojo): fondo oscuro, texto blanco, acento lima, tarjetas con etiqueta en píldora. Fuente y tamaños exactos: sin fuentes todavía.

### Piezas derivadas (reels y carrusel)
- **Reels**: elige tú los mejores momentos (2 a 6 por video largo); cada reel abre con la frase gancho sobre el rostro, con tomas del tema arriba y la cara abajo (pantalla dividida), subtítulo grande y dura ≈ 40 s [1].
- **Imagen en imagen** para grabaciones de pantalla: la cara en un recuadro vertical a un lado [1].
- **Llamado a la acción** al final del reel con una palabra para comentar («Comenta DEVDAY y te envío…»); la misma palabra debe estar dada de alta en la automatización de mensajes de Instagram [1].
- **Carrusel**: 4:5 (1080×1350), 12 diapositivas numeradas, portada con foto de la persona, copy propio y no copiado del reel [1].
- Si reutilizas el mismo video para varias tandas, no repitas los reels ya publicados [1].

### Entrega y control de calidad
- Pide al asistente un resumen: duración antes y después, tomas repetidas quitadas, qué recortó, cuántas tarjetas y tomas, qué logos añadió y qué dudas tiene (minutos a revisar) [1].
- Si se edita dos veces el mismo video, no sobrescribas la carpeta de salida: avisa o numera [1].
- Los reels pueden guardarse como «trial reels» antes de publicar [1].

## Por herramienta
### Claude Code
- Piezas que usa [1]: ffmpeg (cortar y mezclar), Whisper en Python (transcribir y apoyar la detección de la cara) y **Remotion** con Node 18+ (dibuja las animaciones); pide 16 GB de RAM y grabación en 4K o 1080p [1].
- Flujo de [1]: carpeta de trabajo propia, skill instalada pasando la carpeta del kit y pidiendo «instálame esta skill»; se invoca con `/<nombre-de-la-skill>` y el archivo adjunto; modelo Opus, esfuerzo medio [1].
- Una edición de ≈ 13 min tardó 3–5 min y un lote de 2 reels + carrusel ≈ la mitad del cupo de la ventana de 5 h en el plan de 20 USD (dato de la autora) [1].

### Remotion (animaciones y subtítulos desde código)
- **No edita metraje grabado**: genera tarjetas, subtítulos y gráficos desde React; los cortes los hace otra herramienta (ffmpeg, Descript o el flujo de transcripción) [2].
- Instalar las skills oficiales: `claude plugin marketplace add remotion-dev/claude-code-plugin` y `claude plugin install remotion@remotion`, o `npx remotion skills add` (usar una vía, no las dos); reiniciar Claude Code [2]. Skills útiles: `/remotion-captions`, `/remotion-markup`, `/remotion-studio`, `/remotion-render` [2].
- **Cómo pedir**: duración, dimensiones, fps, orden y tiempos de escenas, texto literal, rutas de recursos permitidas, colores, fuentes y estilo de movimiento; **un cambio por vez**; movimiento contenido; revisar en Remotion Studio y no renderizar a cada paso; pedir que preserve lo existente y revisar el diff [2].
- Si la vista previa va lenta en videos largos, renderiza segmentos cortos y no decidas el ritmo con el scrubber [2]. Si se añaden o renombran tomas hay que regenerar el registro (`npm run gen` en una guía); el texto de marca, los colores y las fuentes deben coincidir en todos los archivos o falla en silencio [2].
- Una vista previa que funciona no garantiza el render: fuentes y recursos externos pueden comportarse distinto [2].

### ffmpeg
- Extraer audio para transcribir: mono, 16 kHz, PCM s16le [2]. Mezclar música con `volume=0.13` y fades de 2 s y 3 s [2].

### Premiere Pro
- Sin fuentes todavía (corte por silencios, secuencias para vertical, subtítulos de texto a voz).

### DaVinci Resolve
- Sin fuentes todavía (corte rápido, subtítulos, reencuadre a vertical).

## Recetas
### De un crudo largo a video + reels + carrusel
Objetivo: tener la primera versión publicable en minutos y revisarla tú.
1. Brief con las cinco preguntas → 2. corte de silencios y errores → 3. recorte del marco → 4. transcripción corregida → 5. tarjetas, tomas y logos → 6. MP4 largo → 7. elegir reels y llamado a la acción → 8. reels 9:16 → 9. carrusel 4:5 → 10. revisión humana completa [1].

## Errores comunes
- Dar por bueno el resultado sin abrirlo → el asistente solo vio fotogramas y dice que no puede escuchar el audio [1].
- Poner una palabra de llamado a la acción que la automatización no reconoce → no llega el mensaje; configúrala antes [1].
- Cortar solo por silencios → cortes sobre consonantes y pausas importantes borradas; corta por significado [2].
- Dejar pasar una frase repetida porque una pausa larga engañó al detector → revisión humana obligatoria [2].
- Pausa menor de 0,2 s → el audio suena comprimido [2].
- Rehacer reels ya publicados → pregunta cuáles hay y elige otros [1].
- Subtitular antes de corregir la transcripción → errores en nombres y marcas (en [1]: «Death Day» por DevDay, «Hasbot» por HubSpot) [1].
- Logos pequeños o filas de logos que tapan los créditos de las imágenes → corrígelos antes de renderizar [1].

## Checklist antes de entregar
- [ ] Brief respondido (cortes, estilo, efectos, música).
- [ ] Silencios y errores fuera; duración final comprobada.
- [ ] Transcripción corregida y subtítulos revisados.
- [ ] Reels en 1080×1920 y carrusel en 1080×1350, numerado.
- [ ] Llamado a la acción y su automatización coinciden.
- [ ] Verificación técnica: palabras cortadas por la mitad y desfase de audio (una guía cita un desfase de 200 ms como problema; tolerancia sin definir) [2].
- [ ] Cortes a mitad de palabra revisados (minutos marcados por el asistente) y volumen de la música aprobado.
- [ ] Revisión final a 1,5x con audio por una persona (≈ 4–6 min por 10 min de video) [2].
- [ ] Video completo visto y escuchado por una persona.

## Para MUKIWA
- Visual Edits: usar el flujo como plantilla de «primera versión rápida» para clientes, siempre con revisión humana antes de entregar.
- Para aprender los criterios de corte, subtítulos y animación hace falta ver ediciones terminadas o tutoriales de Premiere/DaVinci.

## Dudas abiertas
- [2] Valores de pausas, música y subtítulos salen de guías escritas (autores con herramientas y afiliados propios) y no se han comprobado con una edición terminada de referencia: validar antes de fijarlos como estándar MUKIWA.
- [2] AssemblyAI frente a Whisper: una guía prefiere AssemblyAI, otra usa Whisper; ambas dan tiempos por palabra. Aquí se usa Whisper local.
- Siguen sin valor: umbral de silencio en dB, relleno de los cortes (padding), lista de muletillas y tolerancia de desfase.
- Sin fuente para Premiere y DaVinci (ya hay un oficio de corte por transcripción en ambos, pero no se ha aprendido de un video real).
- [1] es una demostración comercial: la skill y su prompt no se muestran, así que faltan umbrales de silencio, tipografía y tamaños de subtítulos y reglas de animación (solo se ve el estilo general).
- La calidad real de los cortes y subtítulos no se pudo comprobar: solo se vieron segundos de los reels, adelantados.
- Precio de servicio (desde 400–500 USD al mes) y consumo de tokens son afirmaciones de la autora, sin evidencia.

## Fuentes
- [1] Editar un video en crudo con Claude: video largo, reels y carrusel — https://youtu.be/viztypMn7D0 · `references/lecciones/editor-asistente-claude-flujo-reels-carrusel.md`
- [2] Editar video con Claude Code: tres guías escritas (cortes, pausas, música, subtítulos, Remotion) — https://learnwithhasan.com/guide/claude-code-video-editing/ · https://www.mejba.me/es/blog/claude-code-video-editing-workflow · https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code.md · `references/lecciones/guias-claude-code-cortes-pausas-musica-subtitulos.md`
