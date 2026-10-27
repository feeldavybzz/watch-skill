# Watch en Claude Code: cómo hacer que Claude "vea" un video
> Skill /watch (bradautomates/claude-video): yt-dlp descarga, ffmpeg saca fotogramas, subtítulos nativos o Whisper (Groq/OpenAI) ponen el texto, y Claude lee ambos con tiempos. Útil para auditar hooks, entender charlas largas y documentar sesiones grabadas.

- **Fuente**: https://youtu.be/sLOj0YS1KVg · canal Nexum AI · 11:25 (685 s)
- **Fecha**: 2026-10-10
- **Tipo de "oídos"**: transcripción de subtítulos automáticos de YouTube (.srt es, con duplicación "rolling" y errores: "Cloud Code" = Claude Code, "Grock" = Groq, "WTDLP" = yt-dlp, "Caparzy" = Karpathy)
- **Confianza**: media-alta. Transcripción completa con tiempos + 45 fotogramas de muestra + ampliaciones a 1280 px en los tramos con texto en pantalla. El método se describe y se ve, pero no se validó corriendo la skill /watch original.

## Teoría (lo que se dijo)
- [0:02–0:40] Promesa: Claude Code puede "ver" cualquier video (YouTube, reels, TikTok, Loom, archivos locales) gratis. No solo audio/transcripción, también lo que hay en pantalla, fotograma a fotograma.
- [1:25] La skill se llama **watch** ("ver"). Se invoca pasando el link y una pregunta.
- [1:45–2:05] Si la plataforma ya da transcripción (YouTube), la usa de forma nativa. Además extrae fotogramas, también en videos largos (ejemplo: charla de ~1 h).
- [2:45–3:20] Se puede preguntar por un minuto concreto ("explica el diagrama del 13:11") y la skill extrae fotogramas justo de ese momento.
- [4:06–4:47] Instalación: copiar el link del repo de GitHub de **Brad Automates** (claude-video) y pedirle a Claude Code que instale la skill. Funciona igual en VS Code, otro IDE o la app de escritorio.
- [5:08–5:50] Necesita una API key para transcribir audio cuando no hay subtítulos. Recomienda **Groq** (gratis, ~500.000 tokens/día según él; sin tarjeta) o la de OpenAI de pago.
- [6:31–7:53] Funcionamiento en 4 pasos: 1) yt-dlp descarga; 2) ffmpeg corta el video en fotogramas; 3) usa subtítulos nativos si existen, si no manda el audio a Whisper (Groq/OpenAI); 4) une fotogramas + texto y Claude responde.
- [7:53–9:55] Caso 1: analizar el **hook** de un reel de Instagram (propio o de la competencia). La primera vez pregunta cómo acceder al reel y él elige **cookies del navegador**.
- [10:16–11:19] Caso 2: video de **Loom** de una clase de Airtable. Devuelve tablas, columnas y campos trabajados.

## Práctica (lo que se ve)
- [0:28–0:29] SKILL.md de /watch en VS Code: "Step 0 – Setup preflight (runs every /watch invocation, silent on success)", configuración en `~/.config/watch/.env` con permisos `0600`, variables `GROQ_API_KEY` u `OPENAI_API_KEY` y opción `--no-whisper` (sin claves solo saca fotogramas).
- [6:05–6:20] La misma SKILL.md muestra el **dial de detalle** que se pregunta en el primer uso: `transcript` (sin fotogramas; no descarga video si hay subtítulos), `efficient` (pasada rápida de keyframes, tope 50), `balanced` (recomendado: fotogramas por cambio de escena, tope 100) y `token-burner` (por escena, sin tope). Se guarda como clave en el `.env`.
- [3:08–3:30] En la terminal, Claude responde: "El frame se descartó por ser casi idéntico al anterior. Voy a forzar la captura exacta en el segundo 13:11". O sea, **deduplica fotogramas parecidos** y tiene un modo de **captura forzada en un tiempo exacto**.
- [3:30–3:50] La respuesta sobre el diagrama separa partes ("1. Diagrama de la izquierda… 2. Texto 'Little is known in full detail'…"), citando texto visible de la slide.
- [6:42–7:34] Explicación "como un cuento": "No sube tu video a ningún lado — solo el audio va a Groq/OpenAI, y solo si hace falta transcribir".
- [9:16–10:08] Salida del análisis del reel con estructura fija: **Qué se muestra (visual)** con encuadre, texto overlay y progresión con tiempos (0:00–0:02, ~0:02, ~0:04…), **Qué se dice (audio, transcripción Whisper)** con citas fechadas, y **Lectura del hook** (diagnóstico: "prueba + curiosidad").
- [~6:00] En pantalla se pega la API key en texto plano en el chat y se graba (riesgo: la clave queda publicada en el video).

## Cruce teoría ↔ práctica
- Coincide: los 4 pasos dichos (7:13) se ven en la SKILL.md y en las respuestas de la terminal.
- Lo dicho sin demostrar: "completamente gratis" depende de la cuota gratuita de Groq y del dial elegido. El modo `token-burner` consume muchos tokens del propio Claude.
- Lo mostrado sin explicar: el dial de 4 niveles, la deduplicación de fotogramas casi iguales y el preflight silencioso. Son las piezas de diseño más valiosas y el video no las comenta.
- Contradicción leve: dice "fotograma por fotograma", pero la skill **muestrea** (tope 50/100 o por escena). No ve cada fotograma.
- Omite: cómo maneja videos de 1 h dentro del contexto (presumiblemente tope de fotogramas + saltos a tiempos concretos) y qué pasa cuando YouTube bloquea o pide verificación.

## Receta paso a paso
1. Preflight silencioso: comprobar yt-dlp, ffmpeg y claves. Solo hablar si falta algo.
2. Descargar con yt-dlp (o usar archivo local). Para Instagram/TikTok privados, cookies del navegador con permiso del usuario.
3. Texto: subtítulos nativos primero; si no hay, extraer audio y transcribir con Whisper (Groq u OpenAI). Si no hay clave: modo solo visual.
4. Fotogramas según un dial de detalle (transcript / efficient / balanced / token-burner), con deduplicación de fotogramas casi idénticos.
5. Para preguntas sobre un momento: extraer fotogramas forzados en ese segundo exacto.
6. Responder en bloques fijos: visual con tiempos / lo que se dice con citas fechadas / lectura o diagnóstico.

## Para MUKIWA
- Comparado con `kiwa-watch-learn` + `kiwa-watch-learn`, ya cubrimos los pasos 1–3 y 5 (extract_frames con --start/--end). Nos faltan: dial de detalle, deduplicación de fotogramas, preflight silencioso y una plantilla de salida para "hook/estructura" de reels (la de motion/diseño no cubre hook).
- Caso directo para Visual Edits y Creative Direction: auditar hooks (0–3 s y 0–10 s) de reels propios y de referencias antes de editar.
- Nuestras ventajas que conviene conservar: separar evidencia preparada / análisis / validación, registrar tramos revisados y guardar lecciones en biblioteca.

## Límites
- Revisado de verdad: transcripción completa (deduplicada a mano); 5 hojas de contacto (45 fotogramas de 0:00 a 11:25); ampliaciones a 1280 px en 0:28–0:30, 3:06–3:52, 6:05–7:36 y 9:16–10:10. No se escuchó el audio: solo se leyó el texto de los subtítulos.
- Huecos de muestreo de 15–35 s entre 0:54 y 11:25 (p. ej. 2:28→2:59, 4:59→5:17). Pudo haber pasos en pantalla no vistos.
- No se instaló ni se ejecutó /watch. Los topes (50/100) y opciones se leyeron de la SKILL.md mostrada en el video y pueden haber cambiado en el repo actual.
- La cuota de Groq (500.000 tokens/día) es lo que dice el autor; no está verificada.

## Conecta con
- [[tipografia-cinetica-after-effects-3-tecnicas]] (ejemplo de lección generada con este mismo flujo)
