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
- [9:24–10:50] Resumen que devolvió Claude: 13:37 → 11:56 (quitó silencios y tomas con error); **recortó el marco morado** de la grabación (lo detectó solo); **corrigió a mano la transcripción** antes de subtitular; 4 tarjetas de apertura, 28 tomas del evento sobre el que habla, logos oficiales (OpenAI, Slack, Teams, Drive, Notion, WhatsApp), frases destacadas y tarjeta final.
- [11:43–13:30] Reels: pide solo 2 por tiempo; Claude detecta que ya hizo 6 el día anterior y pregunta cuáles hacer; pregunta **qué palabra va en el llamado a la acción** final («Comenta DEVDAY»). Aviso: la palabra debe existir también en la automatización de mensajes de Instagram.
- [12:13–12:44] Consumo: la sesión de edición usó ≈ la mitad del cupo de la ventana de 5 horas en el plan de 20 USD (57 % marcado, con otras tareas en paralelo).

## Práctica (lo que se ve)
- [2:47–3:15] Instagram: dos de los reels publicados; los otros cuatro se dejan como «trial reels».
- [6:44–7:00] En Claude Code (app de escritorio): carpeta «rrss», modelo Opus 5.5, esfuerzo «Medio», el video adjunto y la skill invocada como `/editor-video-ia`.
- [13:35–14:30] Salida en Descargas: `Reels - DevDay (prueba)` y `Carrusel - DevDay (prueba)`. Según el resumen en pantalla: reels **1080×1920** de 39 s y 40 s; carrusel **4:5, 1080×1350**, 12 diapositivas numeradas 01–12 con portada con su foto. Reel 1: frase sobre su cara, tomas del evento arriba y su cara abajo, dos tarjetas de texto. Reel 2: error de la demo en vivo y tarjetas. Ambos terminan con el llamado «Comenta DEVDAY y te envío el video completo».
- Dato honesto: Claude escribe que **revisó fotogramas y vistas previas, pero no vio los reels completos ni escuchó el audio**. Ella los revisa rápido (los adelanta).
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
- Para aprender los criterios de edición (cuánto silencio cortar, tipografía de subtítulos, animación de logos) hay que ver el resultado terminado, no este tutorial. Mandar un video editado de referencia o un tutorial de Premiere/DaVinci.
- Idea para MUKIWA: la pregunta «copia a un creador» es lo que ya hace esta skill de análisis: un reel de referencia → estilo.

## Límites
- Evidencia: transcripción completa del audio (whisper local) y 87 capturas de 0:00 a 20:26 (hueco máximo 30,7 s); vi 2 capturas completas y leí el resumen de Claude en pantalla. No vi cada segundo.
- La skill y el prompt no aparecen: no se pueden extraer sus reglas.
- Tiempos y consumo de tokens son lo que dice ella, en su cuenta.
