---
name: kiwa-editor-asistente
description: "Kiwa de editor asistente: corte por significado, pausas, música, subtítulos, Remotion, reels y carruseles, criterio de edición y flujo con Claude Code."
metadata:
  nicho: editor-asistente
  herramientas: "Premiere Pro, DaVinci Resolve, Claude Code, Remotion"
  lecciones: 12
  actualizado: "2026-10-31"
---

# Kiwa · Editor asistente
> Prepara el material y entrega la primera versión del montaje: corta por significado y con intención (eyeline match, cross cutting, eye trace, J/L cut, montaje intelectual, corte en acción), cubre con B-roll, respeta la línea de 180° y usa la velocidad como recurso, ajusta pausas, mezcla la música, subtitula con animación y deriva reels y carruseles de un video largo. Incluye valores de partida de corte apretado y verificación de huecos ([12], sin validar con un clip). Conoce el flujo de editar con IA (Claude Code, Whisper, ffmpeg, Remotion) con valores de partida concretos; faltan los pasos manuales en Premiere y DaVinci y valores validados con ediciones terminadas. Tiene **6 lecciones propias** y **3 complementarias** ([7] whip pan, [8] match cut en video de IA, [9] overlays en Premiere).

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Para el estilo gráfico de tarjetas y títulos, combínalo con `kiwa-diseno-grafico`; para animarlos, con `kiwa-motion-graphics`; para encuadrar el vertical, con `kiwa-composicion-visual`.

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

### Criterio de corte (cómo decidir cada corte) [3]
- **Todo el trabajo se reduce a tres decisiones: qué mostrar, cuándo cortar y a qué cortar.** Cada corte debe ser pensado y con propósito [3].
- **Regla de los seis de Walter Murch** (pesos leídos del gráfico del video; coinciden con los publicados): **Emoción 51 %**, **Historia 23 %**, **Ritmo 10 %**, **Eye trace 7 %**, **Plano bidimensional de la pantalla 5 %**, **Espacio tridimensional 4 %**. Cuando dos criterios chocan, gana el de más peso: la emoción primero [3].
- **Ritmo según el tono**: escena contemplativa o luctuosa = mantén los planos más tiempo; acción frenética = cortes rápidos [3].
- **A qué cortar**: a lo que mira el personaje (eyeline match: a menudo un POV; se puede retrasar la revelación o no mostrarla nunca para crear intriga), a un **inserto** (detalle de un objeto), a un **cutaway** (lo que el personaje piensa) [3].
- **Conversaciones**: **plano-contraplano** (sujeto A y sujeto B desde un ángulo inverso y composición parecida) para mantener la geografía y la claridad de la escena [3].
- **Cross cutting (montaje paralelo)**: alterna dos o más escenas simultáneas en lugares distintos; da ironía (bautizo de *El padrino*) o mantiene varios frentes avanzando (*Rogue One*) [3].
- **Eye trace**: en planos rápidos, deja el punto de interés **en la misma zona del cuadro** de un plano al siguiente para que el ojo no tenga que rastrear; con ≈ 1,8 s entre cortes (dato del director de fotografía de *Mad Max: Fury Road*), algunos planos duran menos de 1 s [3].
- **J cut y L cut (split edit)**: **J** = el audio del siguiente plano empieza antes de verlo; **L** = el audio del plano anterior continúa sobre el siguiente. Úsalos en diálogos (más naturales; captan reacciones del que escucha) y para explicar un plan mientras se muestra la acción [3].
- **Montaje intelectual** (efecto Kuleshov): yuxtapón planos sin relación aparente para crear una idea o emoción (un ratón y una trampa = «cae en una trampa»); hace el corte más notorio [3].
- **Corte en acción**: corta **durante el movimiento**; la salida del plano A coincide con la entrada del B; en peleas, **corta en el impacto** [3].
- **B-roll (el material al que cortas)** [4]: es lo que cubre los huecos del A-roll: **tapa saltos (jump cuts) y errores**, da **cobertura** a un hablante largo y puede **simbolizar** lo que se dice (en *Her*, el polvo en la pared mientras ella explica su conciencia). Corta a él en la frase clave y **elige su ángulo, lente y movimiento por el significado que quieres** (la misma línea cambia de sentido según el plano). Al rodarlo se planifica y se agrupa; esta parte la ejecuta `kiwa-cinematografia` [4].
- **No cruces la línea sin querer (regla de los 180°)** [5]: en un diálogo mantén cada personaje mirando al **mismo lado de pantalla** corte tras corte (uno a la derecha, otro a la izquierda); si el material quedó cruzado, repáralo con un **plano neutral** (sobre la línea o detrás de un sujeto) o con un movimiento de cámara que cruce dentro del plano. Cruzarla a propósito sirve para **caos** o para **cambiar poco a poco el poder** entre personajes [5].
- **Velocidad como recurso de montaje** [6]: la **rampa de velocidad** (pasar entre velocidades dentro de un mismo plano) da peso a un golpe o acento (*300*); la cámara lenta enfatiza la emoción o la acción que muestra; **no mezcles velocidades** dentro de un movimiento que debe verse normal. Material grabado a alta tasa (60, 120 o más) se reproduce a 24 para que sea lento y suave; el audio se estira con él [6].
- **Whip pan como transición** [7]: un paneo rápido puede **transicionar entre personajes o escenas** y sincronizarse con el ritmo de la música (*Whiplash*); si el material trae un whip pan, corta dentro del giro [7]. Reproducirlo en edición con un empuje o zoom digital es una idea (≈), sin fuente de valores [7].
- **Match cut entre locaciones** [8]: corta en una acción (el toque en un teléfono), **conserva el encuadre y el movimiento de cámara** y cambia solo la locación; así se hizo el salto a otra ciudad en el anuncio de video de IA [8].
- Pendientes (sin fuente): freeze frame, cortes invisibles, fotogramas subliminales, cortes dobles y jump cut [3].

### Corte
- **El corte es semántico, no acústico**: cortar solo por silencios con ffmpeg dejó cortes sobre consonantes y borró pausas que importaban; decide qué se va por lo que se dice y deja a una persona la decisión de las frases repetidas [2].
- Base de todo: un mapa de palabras con tiempos; los pasos siguientes (efectos, subtítulos, tarjetas) se anclan a él [2].
- **Pausas entre palabras ≈ 0,2 s** (probado de 0,15 a 0,35): por debajo suena comprimido, por encima de 0,25 s ya no se nota la mejora [2]. **Muletillas**: quitarlas en explicaciones técnicas, dejarlas en momentos narrativos, porque dan ritmo humano [2].
- Quitar silencios, tomas con error y repeticiones; el video resultante debe ser más corto y dinámico [1].
- **Corte apretado de un clip hablado: valores de partida** [12] (de un código leído, sin validar con un clip; el estilo humano de [2] con pausas ≈0,2 s es más suave):
  - Pausa entre palabras conservadas **> 0,12 s** → cortar, dejando **0,035 s** tras la palabra y **0,025 s** antes de la siguiente.
  - Los bordes de palabra se miden por energía, no por los tiempos del transcriptor: el borde es donde hay **≥100 ms bajo −46 dBFS**. Un hueco corto (<0,4 s) con sonido sostenido (≥60 ms sobre −40 dBFS) es parte de una palabra: no se corta.
  - **Respiraciones**: cortar si hay ≥0,18 s sin voz (autocorrelación <0,45) y silencio (<−30 dB) entre palabras. Recortar el inicio hasta 0,1 s antes de la primera palabra y el final 0,12 s tras la última.
  - **Tomas falladas: conserva la ÚLTIMA toma completa**; escribe a mano los rangos a quitar y deja que un guardia impida que un corte se coma una palabra conservada [12].
  - **Verifica antes de renderizar** [12]: transcribe cada hueco quitado que tenga sonido sostenido (si aparece una palabra real, protégela o corrige el rango) y transcribe el audio ya editado entero; léelo como guion: sin repeticiones, sin palabras cortadas, sin frases a medias.
  - Pasa el fps real del clip a cada paso (un fps equivocado hace caer los cortes en el cuadro equivocado) y une cada corte con un fundido de audio de ≈8 ms [12].
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

### Transición «frame flash» en DaVinci Resolve [10]
- Es una transición de Fusion de 4 fotogramas por defecto (más fotogramas con las pestañas «before 3…»): se pone entre dos clips y se elige el **tratamiento de cada fotograma** (invertir, desenfoque direccional, desenfoque + invertir). En direccional: dirección y longitud del desenfoque. Luces altas, sombras, contraste y saturación se ajustan en el mismo Inspector, sin pasar por Color. Se remata con diseño de sonido.
- Inspector visto: «Transition – RAM Frame Flash Four», duración ≈ 0,6 s (15 fotogramas), secuencia Before 4 / 3 / 2 / 1 / After 1.

### Vocabulario de recursos de un teaser de gira [11]
- Mezcla de planos limpios con «planos efecto»: zoom radial con bloom, latigazo, estática tipo VHS, fogonazos de color, un fotograma negro como golpe, espejo simétrico y cierre de espaldas. Ritmo ≈ 1 corte por segundo (≈). Solo visual: no se verificó el corte al beat.

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
- **Subtítulos simples (alternativa sin animación)** [12]: frases de **2 a 4 palabras**, blancas, un solo estilo, bajo la barbilla, sin tapar la boca ni salirse de los lados. Escribe el texto a mano (una línea por subtítulo, todas las palabras habladas en orden) y alinéalo con un script contra las palabras con tiempo: si una palabra no coincide debe fallar en voz alta, no desfasarse. Arreglos del reconocimiento con alias «mostrado=oído»; cada subtítulo dura hasta el siguiente, máximo 0,5 s tras su última palabra [12].
- Una vista previa que funciona no garantiza el render: fuentes y recursos externos pueden comportarse distinto [2].

### ffmpeg
- **Recorte a 9:16 con la cara centrada** [12]: desde 3840×2160 ventana 1215×2160; desde 1920×1080 ventana 608×1080; luego escalar a 1080×1920 (lanczos, x264 CRF 16, AAC 320 k). Mira un fotograma antes de seguir; un clip ya vertical solo se escala. Para cortar por cuadros exactos con muchos tramos, el filtro `select` de ffmpeg falla con muchos términos `between()`: trocear en grupos de ≈50 y unir [12].
- Extraer audio para transcribir: mono, 16 kHz, PCM s16le [2]. Mezclar música con `volume=0.13` y fades de 2 s y 3 s [2].

### Premiere Pro
- **Overlay de guías o zonas seguras como clip** [9]: un plugin real (Guideify 2) no dibuja sobre el Monitor de Programa; al pulsar **Apply** inserta el overlay como **clip en una pista de video nueva** que cubre toda la secuencia y avisa dónde quedó (p. ej. V7); **Remove** lo quita. Sirve para revisar zonas seguras de reels 9:16 (Action safe 90 %, Title safe 80 %, márgenes en %); comprueba que el clip no se exporte [9].
- Sin fuentes todavía para corte por silencios, secuencias para vertical y subtítulos de texto a voz.

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
- [ ] Cada hueco quitado con sonido sostenido transcrito y el audio editado leído como guion [12].
- [ ] Cortes a mitad de palabra revisados (minutos marcados por el asistente) y volumen de la música aprobado.
- [ ] Revisión final a 1,5x con audio por una persona (≈ 4–6 min por 10 min de video) [2].
- [ ] Video completo visto y escuchado por una persona.

## Para MUKIWA
- Visual Edits: usar el flujo como plantilla de «primera versión rápida» para clientes, siempre con revisión humana antes de entregar.
- Para aprender los criterios de corte, subtítulos y animación hace falta ver ediciones terminadas o tutoriales de Premiere/DaVinci.

## Dudas abiertas
- [3] Los porcentajes de la regla de los seis salen de un gráfico a baja resolución del video; coinciden con los valores publicados de Murch pero el narrador no los recita. Faltan duraciones recomendadas por tipo de plano y los pasos de J/L cut y de corte en acción en Premiere o DaVinci.
- [2] Valores de pausas, música y subtítulos salen de guías escritas (autores con herramientas y afiliados propios) y no se han comprobado con una edición terminada de referencia: validar antes de fijarlos como estándar MUKIWA.
- [2] AssemblyAI frente a Whisper: una guía prefiere AssemblyAI, otra usa Whisper; ambas dan tiempos por palabra. Aquí se usa Whisper local.
- Umbral de silencio y relleno de cortes: ya hay valores de partida en [12] (−46/−30 dBFS, 0,12 s, 0,035/0,025 s) pero salen de un código leído, sin probar con un clip ni comparar con [2]; siguen sin valor la lista de muletillas y la tolerancia de desfase.
- [12] La skill de origen es un gancho de venta (rechaza ganchos, gráficos, música y subtítulos animados): solo se aprovecha su método de corte, no su estilo. Su video-guía no se vio.
- La guía escrita de [3] añade técnicas que el video no desarrolla: continuity editing, disolvencia, fundido, jump cut, match cut y montaje; la **regla de los 180°** ya tiene fuente propia [5]. No hay fuente para ejecutarlas en software.
- Sin fuente para Premiere y DaVinci (ya hay un oficio de corte por transcripción en ambos, pero no se ha aprendido de un video real).
- [1] es una demostración comercial: la skill y su prompt no se muestran, así que faltan umbrales de silencio, tipografía y tamaños de subtítulos y reglas de animación (solo se ve el estilo general).
- La calidad real de los cortes y subtítulos no se pudo comprobar: solo se vieron segundos de los reels, adelantados.
- [7][8][9] Las tres lecciones complementarias no son de edición como tema: [7] es teoría de cámara, [8] un flujo de video de IA y [9] una demo de 39 s sin voz; aportan criterios y un método para Premiere, sin valores.
- Precio de servicio (desde 400–500 USD al mes) y consumo de tokens son afirmaciones de la autora, sin evidencia.
- [10] No se leen los valores numéricos por fotograma y el preset no se obtuvo (se entrega por comentario).
- [11] Sin voz: no se sabe con qué efectos se hizo cada recurso ni si los cortes caen en el beat.

## Fuentes
- [1] Editar un video en crudo con Claude: video largo, reels y carrusel — https://youtu.be/viztypMn7D0 · `references/lecciones/editor-asistente-claude-flujo-reels-carrusel.md`
- [2] Editar video con Claude Code: tres guías escritas (cortes, pausas, música, subtítulos, Remotion) — https://learnwithhasan.com/guide/claude-code-video-editing/ · https://www.mejba.me/es/blog/claude-code-video-editing-workflow · https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code.md · `references/lecciones/guias-claude-code-cortes-pausas-musica-subtitulos.md`
- [3] Seis formas de editar una escena: eyeline match, cross cutting, eye trace, split edit, montaje intelectual y corte en acción (StudioBinder, Shot List ep. 10) — https://youtu.be/FVR8zz8ci2k · `references/lecciones/seis-formas-de-editar-una-escena-studiobinder.md`
- [4] B-roll: qué es y tres consejos para rodarlo (StudioBinder, Elliot Rosen) — https://youtu.be/MJnT1TwQFdU · `references/lecciones/b-roll-que-es-y-como-rodarlo-studiobinder.md`
- [5] La regla de los 180°: seguirla, romperla y doblarla (StudioBinder) — https://youtu.be/iW0bKUfvH2c · `references/lecciones/regla-de-los-180-grados-studiobinder.md`
- [6] Frame rate: capturar y presentar a distintas velocidades (StudioBinder, Shot List ep. 8) — https://youtu.be/7lUFluLOh-s · `references/lecciones/frame-rate-captura-presentacion-camara-lenta-studiobinder.md`
- [7] Los 15 movimientos de cámara (StudioBinder, Shot List ep. 6), sección «whip pan» — https://youtu.be/IiyBo-qLDeM · `references/lecciones/movimientos-de-camara-15-studiobinder.md`
- [8] Dirigir un anuncio de 30 s con video de IA (Higgsfield, Seedance), sección «dirigir» — https://youtu.be/kFKpcCHkuPI · `references/lecciones/dirigir-anuncio-con-video-ia-higgsfield-seedance.md`
- [9] Guideify 2: cómo un plugin de Premiere muestra interfaz social y guías — https://youtu.be/ZcDtrjVuR5k · `references/lecciones/guideify-2-overlay-social-y-guias-en-premiere.md`
- [10] Transición «frame flash» en DaVinci Resolve (@ramrylie) — reel de Instagram, archivo local · `references/lecciones/flash-transition-davinci-ramrylie.md`
- [11] Edit de concierto: flashes, latigazos, zoom radial, glitch y espejo (@acreyyyyy) — reel de Instagram, archivo local · `references/lecciones/edit-concierto-flashes-zoom-glitch-acreyyyyy.md`
- [12] Clean Cut (gratis): corte apretado y subtítulos simples para un clip hablado (Ajene Pinnock) — skill ajena leída como texto; página de Notion del autor · `references/lecciones/clean-cut-corte-tight-subtitulos-ajene-pinnock.md`
