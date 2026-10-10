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

Usar --cookies solo con una sesión autorizada y cuando sea necesario. No guardar cookies o claves en Git, no imprimir secretos y no cambiar permisos de seguridad del sistema automáticamente. No evadir DRM ni bloqueos de verificación. Ante un fallo persistente, conservar evidencia útil y reportar la causa; pedir archivo local si no hay una ruta disponible.
