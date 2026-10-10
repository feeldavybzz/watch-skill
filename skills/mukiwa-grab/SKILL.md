---
name: mukiwa-grab
description: Obtener videos, audio, subtítulos, imágenes o carruseles desde enlaces para referencia y análisis con mukiwa-learn. Usar cuando Bryan pida descargar, bajar o guardar contenido o cuando el análisis necesite el archivo.
---

# MUKIWA Grab

1. Comprobar terminal, red y herramientas disponibles en el entorno actual. Claude Code local puede ejecutar en el Mac; un contenedor remoto no equivale al Mac.
2. Reutilizar archivos ya descargados. Ejecutar `python3 scripts/grab.py URL --max-height 720 --out DIR` usando argumentos seguros.
3. Dependencias: yt-dlp, ffmpeg o imageio-ffmpeg; gallery-dl para fotos. Instalar desde fuentes oficiales cuando falten. No actualizar paquetes silenciosamente en cada descarga. scripts/setup.sh es el instalador heredado para macOS: revisarlo antes de usarlo y no ejecutarlo en Linux.
4. Verificar que existen archivos de medios reproducibles; miniatura, metadata o subtítulos no prueban que se descargó el video. Usar probe.py de mukiwa-learn sobre el archivo.
5. Para analizar, continuar con mukiwa-learn. Opciones: --audio-only, --photos-only, --no-subs, --subs-only (solo subtítulos e info, sin video), --frames. Subtítulos: una sola petición, eligiendo desde info.json una pista (manual antes que automática; idioma original antes que traducciones automáticas; `--sub-lang es` para forzar otro). La procedencia queda en subtitulos.json. Si video.mp4 o los subtítulos ya están en la carpeta, no se vuelven a pedir. Para ver y analizar en un paso, usar ../mukiwa-learn/scripts/watch.py, que llama a este script.

## Si falla
mukiwa-grab explica el fallo con dos líneas: `CAUSA[código]: qué pasó` y `HAZ: qué hacer` (429, login, privado, no-existe, región, 403, js, red, 5xx...). Retransmitirlas a Bryan tal cual; no inventar otra causa. Reintenta solo con espera lo que lo merece (429, red, 5xx); nunca en bucle. Si pide sesión, privado o está bloqueado: plan B = que Bryan guarde el video en «Para analizar» del buzón o te dé el archivo.

`python3 scripts/doctor.py [--online]` revisa yt-dlp (y si hay una versión más nueva), el runtime de JavaScript que YouTube exige (se detecta Node en el PATH, en ~/nodejs y en Homebrew), ffmpeg, gallery-dl, whisper y el espacio libre, y da el comando exacto de lo que falte. Correrlo con `~/.venvs/watch-skill/bin/python`. Actualizar yt-dlp solo con permiso de Bryan y con el comando que indique doctor.

Usar --cookies solo con una sesión autorizada y cuando sea necesario. No guardar cookies o claves en Git, no imprimir secretos y no cambiar permisos de seguridad del sistema automáticamente. No evadir DRM ni bloqueos de verificación. Ante un fallo persistente, conservar evidencia útil y reportar la causa; pedir archivo local si no hay una ruta disponible.
