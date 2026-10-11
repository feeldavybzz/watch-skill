# Editar un video en crudo con Claude Code: flujo de editor asistente (video largo, reels y carrusel)
> Una creadora le pasa a Claude Code un video grabado en crudo y una skill empaquetada; Claude responde unas preguntas de estilo y devuelve el MP4 editado, reels verticales y un carrusel. Sirve como flujo de trabajo, no como receta de cortes: la skill en sí no se muestra.

- **Fuente**: https://youtu.be/viztypMn7D0 · «Cómo editar videos con Claude Opus 5.5 | Skill Gratis» · canal Melina Blanco | Agentes IA y Automatizaciones · 20:26
- **Fecha**: 2026-10-10
- **Tipo de "oídos"**: audio transcrito en la Mac con faster-whisper (small, 4601 palabras) y cotejado con los subtítulos automáticos de YouTube (4689). Coinciden en el contenido; ambos escriben «Cloud» donde ella dice Claude (así suena en su voz) y «Day de» por DevDay. No es una escucha humana: no capta tono ni música.
- **Confianza**: media en el flujo (se ve en pantalla); baja en los criterios de edición, porque nunca se abre la skill ni se enseñan parámetros.

## Qué NO es este video
- Es en buena parte una **demostración comercial**: la skill («editor-video-ia») se entrega gratis a cambio de unirse a una lista de espera de su comunidad de pago [14:38–19:00]. No se ve su contenido ni el prompt completo.
- No hay valores de edición (umbrales de silencio, duraciones, easing, fuentes, colores): solo el resumen que Claude escribe al final.
- Se habla de precio de servicio («desde 400–500 USD al mes por reels») [19:24]; es una afirmación de ella, sin evidencia.

## Teoría (lo que se dijo)
- [0:00–0:24] Resultado declarado: animaciones de logos, títulos, cortes por errores y subtítulos palabra por palabra, hechos por Claude en minutos; de un mismo video salieron 6 reels y un carrusel.
- [1:45–2:31] Flujo: (1) grabarse en crudo, sin cortes, con errores y repeticiones; (2) pasarle el video a Claude con un prompt de edición; (3) Claude devuelve el video editado; (4) pedirle reels del mismo video; (5) pedirle el carrusel.
- [3:36–4:37] Ventaja que plantea: ofrecer edición a clientes sin saber edición; a mano un video de 10+ minutos «llevaría un día entero». Requisitos: Claude Code en plan de pago de 20 USD, un ordenador y la grabación.
- [4:39–6:30] Instalación: el kit (un zip con guía y skill) se descomprime, se le pasa la carpeta a Claude y se le dice «instálame esta skill»; Claude instala por su cuenta las herramientas que faltan.
- [6:37–6:48] Recomienda cambiar a **Opus** para editar video (dice que Sonnet no rinde igual).
- [7:26–8:50] La skill **pregunta antes de editar**: motivo de la edición, quién hace los cortes (la skill, sin cortes, o un video ya cortado), estilo y marca (el de siempre, por defecto, o **copiar a un creador pasando su link**), efectos, y música (la de siempre, ninguna, o elegir una nueva). Detectó que el mismo video ya se había editado el día anterior.
- [8:51–9:15] Tiempo: unos 3–5 minutos para un crudo de 13:38.
- [9:24–10:50] Resumen que devolvió Claude (leído en pantalla a 10:28 y 12:00): 13:37 → 11:56; quitó las pausas y **11 tomas repetidas** dejando la **última versión completa** de cada frase; **recortó el marco morado**; **corrigió a mano la transcripción** (ej. «Death Day»→DevDay, «Hasbot»→HubSpot, «cloud»→Claude); **4 tarjetas de apertura**, **28 tomas del evento**, **≈45 tarjetas** con listas, números que suben, flujos de pasos y opciones, logos oficiales (OpenAI, Slack, Teams, Drive, Notion, WhatsApp), **3 frases grandes** y tarjeta final.
- [11:43–13:30] Reels: pide solo 2 por tiempo; Claude detecta que ya hizo 6 el día anterior y pregunta cuáles hacer; pregunta **qué palabra va en el llamado a la acción** final («Comenta DEVDAY»). Aviso: la palabra debe existir también en la automatización de mensajes de Instagram.
- Audio de salida (leído en pantalla): voz a **−13,5 LUFS**, que dice ser el volumen que usa YouTube; música lo-fi que **baja sola cuando hablas**. Marca de agua con el usuario (en la prueba salió el marcador @TU_USUARIO por usar el estilo por defecto). La skill crea una carpeta de edición con el nombre del video y, si se edita dos veces, sobrescribiría: conviene avisar o numerar.
- [12:13–12:44] Consumo: la sesión de edición usó ≈ la mitad del cupo de la ventana de 5 horas en el plan de 20 USD (57 % marcado, con otras tareas en paralelo).

## Práctica (lo que se ve)
- [0:00–0:24] **El propio inicio del video es el resultado editado** (se ve en la hoja 1): fondo negro, su cámara dentro de un marco inclinado con borde lima neón; luego plano a pantalla completa con **subtítulos de una palabra o pocas por vez** que aparecen escribiéndose («Los títu|»); tarjeta «DEL MISMO VIDEO · Contenido listo para Instagram» con ella a la izquierda; marca de agua de usuario abajo a la derecha. Más adelante: grabación de pantalla con su cara en un **recuadro vertical a la derecha** (imagen en imagen) y subtítulo inferior con la **palabra clave resaltada** («Un **dot** que cuando»).
- [2:17–3:35] Miro: tablero con Claude arriba y tres ramas: Video largo → YouTube, Reels y Carrusel → Instagram. Es el esquema del flujo.
- [3:49–5:52] La guía PDF (13 páginas, «Edita videos y reels con IA — Guía + Skill»): promete transcribir palabra por palabra, quitar pausas, muletillas y tomas repetidas, subtítulos con palabras clave resaltadas, **tarjetas animadas (listas, números, procesos)**, zooms, recuadros y pantalla dividida. Índice: lo que necesitas, instalación, cómo grabar para que quede bien, primer video largo, reels y Shorts, copiar el estilo de otro creador. Antes/después en la guía: fondo oscuro, subtítulo blanco con palabra en lima.
- [4:51] Herramientas que pide: **ffmpeg** (cortar y mezclar), **Node 18+ con Remotion** (dibuja las animaciones), **Python 3.9+** (Whisper para transcribir y detección de la cara para los reels), 16 GB de RAM y 10 GB libres; grabación ideal en 4K o 1080p. Comandos: Mac `brew install ffmpeg node python`.
- [14:03–14:20] Reels vistos: formato 9:16 con **toma del evento arriba y su cara abajo** y subtítulo grande blanco («Presentaron un agente»); cierre con tarjeta negra «Comenta **DEVDAY**» (palabra en caja lima).
- [2:47–3:15] Instagram: dos de los reels publicados; los otros cuatro se dejan como «trial reels».
- [6:44–7:00] En Claude Code (app de escritorio): carpeta «rrss», modelo Opus 5.5, esfuerzo «Medio», el video adjunto y la skill invocada como `/editor-video-ia`.
- [13:35–14:30] Salida en Descargas: `Reels - DevDay (prueba)` y `Carrusel - DevDay (prueba)`. Según el resumen en pantalla: reels **1080×1920** de 39 s y 40 s; carrusel **4:5, 1080×1350**, 12 diapositivas numeradas 01–12 con portada con su foto. Reel 1: frase sobre su cara, tomas del evento arriba y su cara abajo, dos tarjetas de texto. Reel 2: error de la demo en vivo y tarjetas. Ambos terminan con el llamado «Comenta DEVDAY y te envío el video completo».
- **Control de calidad que hace la skill** (12:00): «revisé fotogramas de todo el video antes de renderizar» y corrigió tres cosas (logo de OpenAI muy chico, una fila de logos tapaba el crédito de las imágenes, un check aparecía tarde). Aun así avisa: «**no puedo escuchar el audio**; revisa que no haya quedado ningún corte a mitad de palabra en las tomas repetidas (minutos 5:06, 5:25, 5:48, 7:41 y 11:21) y que el volumen de la música te guste». También dice que los cortes son automáticos y que mires si el ritmo se siente natural o cortado. Ella los revisa rápido (los adelanta).
- Ritmo de este video (≈, medido): 33 cortes, 1,6 por minuto; es una grabación de pantalla, no el resultado editado.

## Cruce teoría ↔ práctica
- Coincide: el video largo se acorta (13:37→11:56), los reels salen en vertical 9:16 y el carrusel en 4:5, y las preguntas previas son las que describe.
- No se puede comprobar: la calidad de los cortes, de los subtítulos palabra por palabra y de las animaciones (solo se ven unos segundos de reels, a velocidad rápida).
- Se dijo «reels y carrusel con la misma información», pero se ve que el carrusel se reescribe en copy aparte (Claude pide el copy).

## Receta paso a paso (flujo de editor asistente con IA)
1. Graba en crudo y deja los errores: se corrigen en la edición.
2. Abre una **sesión nueva**, con el modelo más capaz, y llama a la skill de edición con el archivo adjunto.
3. Responde las preguntas de estilo: quién corta, estilo/marca (o link de un creador de referencia), efectos, música.
4. Revisa el resumen (duración antes/después, qué recortó, tarjetas, logos) y abre el MP4 **tú**: la IA no ve el video entero.
5. Pide los reels: elige tú cuáles, define el **llamado a la acción** final y verifica que la automatización lo reconozca.
6. Pide el carrusel en 4:5 (1080×1350) numerado y revisa el copy.
7. Antes de entregar, revisa subtítulos, nombres propios y datos.

## Para MUKIWA
- Esto es un **flujo de asistente**: sirve de plantilla para el trabajo de editor asistente (preparar, cortar silencios y errores, subtitular, derivar reels y carruseles) y para un servicio a clientes.
- Para aprender los criterios de edición (cuánto silencio cortar, tipografía de subtítulos, animación de logos) hay que ver el resultado terminado; aquí solo se ve el estilo general (fondo oscuro, acento lima, palabra clave resaltada, imagen en imagen). Mandar un video editado de referencia o un tutorial de Premiere/DaVinci.
- Idea para MUKIWA: la pregunta «copia a un creador» es lo que ya hace esta skill de análisis: un reel de referencia → estilo.

## Límites
- Evidencia: transcripción completa del audio (whisper local) y 87 capturas de 0:00 a 20:26 (hueco máximo 30,7 s). Abrí las 10 hojas de contacto y 6 capturas a tamaño completo (guía, instalación, resúmenes de Claude); los tramos de la comunidad y WhatsApp (14:38–19:00) los vi solo en hojas. No vi cada segundo.
- La skill y el prompt no aparecen: no se pueden extraer sus reglas.
- Tiempos y consumo de tokens son lo que dice ella, en su cuenta.
