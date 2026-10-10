# watch-skill · MUKIWA

Skills de referencia y aprendizaje audiovisual para Claude Code: `mukiwa-grab` obtiene medios y `mukiwa-learn` relaciona transcripción con fotogramas y guarda lecciones.

## Instalar en Claude Code

Dentro de una sesión de Claude Code:

```text
/plugin marketplace add feeldavybzz/watch-skill
/plugin install mukiwa-video@watch-skill
```

Seguir la indicación de activación del cliente. Los nombres de las skills pueden aparecer con el prefijo del plugin. También se puede abrir este repositorio en Claude Code y pedir que lea `CLAUDE.md` y las skills directamente, antes de instalar globalmente.

## Profesores por nicho

Cada video analizado alimenta **mini skills por oficio** en `profes/<nicho>/` (color grading, diseño de logos, tipografía cinética…). Si el profesor no existe se crea; si existe, aprende más; si el tema ya lo cubre una skill propia de Bryan, se le añade el conocimiento en `references/aprendido-mukiwa.md`. Las herramientas (DaVinci, Premiere, After Effects…) son secciones dentro de cada profesor. Se escriben como instrucciones para hacer el trabajo, con fuente [n] por técnica.

```bash
python3 skills/mukiwa-learn/scripts/profes.py list      # profesores y skills existentes
python3 skills/mukiwa-learn/scripts/profes.py install   # enlaza profes/* en ~/.claude/skills/profe-*
```

Reglas de clasificación y fusión: `skills/mukiwa-learn/references/profesores.md`. Índice: `profes/INDEX.md`. Los enlaces apuntan al disco externo: sin el disco conectado, los profesores no se cargan.

## Copia semanal en Google Drive

Cada lunes, la tarea programada de la app de Claude `mukiwa-skills-drive-semanal` ejecuta `tools/sync_drive.py`, que empaqueta todas las skills (MUKIWA, profesores y las propias de `~/.claude/skills`) y las copia a `Mi unidad/MUKIWA · Skills de Claude` mediante Google Drive para escritorio. Solo copia lo que cambió; lo retirado va a `_retiradas/`. A mano: `python3 tools/sync_drive.py`.

## Usar en claude.ai (app de Claude)

```bash
python3 tools/build_skills.py
```

Genera `dist/mukiwa-grab.skill` y `dist/mukiwa-learn.skill` (solo archivos de Git: sin descargas, claves ni `._*`). Subirlos en claude.ai → Configuración → Capacidades → Skills. `mukiwa-learn` lleva su propia copia del descargador y la biblioteca de lecciones. En claude.ai el entorno suele bloquear YouTube e Instagram: subir el archivo de video en vez del link.

## Dependencias

Python 3.9+ y ffmpeg/ffprobe en PATH son la ruta principal. Para extraer fotogramas sin ffmpeg del sistema se admite imageio-ffmpeg. Instalar las dependencias Python en un entorno virtual:

```bash
python3 -m venv ~/.venvs/watch-skill
~/.venvs/watch-skill/bin/python -m pip install -r requirements.txt
```

En la Mac de Bryan el repo vive en un disco exFAT: el venv va en el disco interno (`~/.venvs/watch-skill`), porque dentro del disco externo los archivos `._*` de macOS impiden que Python arranque.

Whisper es opcional: `python3 -m pip install faster-whisper`. Su primera ejecución puede descargar un modelo. No se necesita para usar subtítulos existentes. `probe.py` y la transcripción Whisper heredados necesitan ffprobe/ffmpeg del sistema.

## Ver un video en un paso

```bash
python3 skills/mukiwa-learn/scripts/watch.py "https://youtu.be/ID" --question "¿Qué técnica usa en el minuto 2?"
```

Descarga (o reutiliza), saca subtítulos o transcribe en la Mac, extrae capturas repartidas por todo el video, fija capturas a 1280 px del gancho y de los momentos que el presentador señala, mide ritmo de edición y paleta, y escribe `work/watch-…/informe.md` + `evidence.json`. Niveles: `--detail transcript|efficient|balanced|full`. Enfoque: `--start/--end`, `--at 4:32,13:11`.

Motor opcional `--engine gemini`: Google ve el video completo y responde. Requiere `GEMINI_API_KEY` en `~/.config/mukiwa/.env` (gratis en https://aistudio.google.com/apikey); los links de YouTube se envían a Google y los archivos se suben y se borran al terminar. Nunca se usa sin pedirlo.

Comparado con Watch: funciona con el Python 3.9 de la Mac sin Homebrew; limpia subtítulos automáticos en cascada (Watch solo quita duplicados exactos); detecta y captura solas las señales del presentador; capturas fijas a 1280 px para leer texto; reparte capturas por tramos e informa el hueco máximo; mide ritmo de edición, gancho y paleta; guía de análisis de reels; y guarda lo aprendido en una biblioteca.

## Flujo por pasos

1. Descargar un enlace con `python3 skills/mukiwa-grab/scripts/grab.py URL --out _descargas --max-height 720`.
2. Preparar un archivo local:

```bash
python3 skills/mukiwa-learn/scripts/prepare.py VIDEO --out work/referencia --transcript SUBTITULOS.srt
```

Sin subtítulos se puede omitir `--transcript` (evidencia parcial) o usar `--whisper` cuando esté configurado. `evidence.json` informa el estado; salida 0 significa evidencia visual y textual lista, salida 2 significa parcial o bloqueada. Nunca significa que el agente ya analizó el video.

3. El agente abre las hojas de contacto, revisa la transcripción, amplía momentos relevantes y escribe una lección con tiempos y límites.
4. Guardar la lección usando `save_lesson.py`; al reemplazar una lección se conserva una copia en `library/_history`.

Los fotogramas son muestras. No se promete inspección de cada fotograma ni transcripción perfecta. Obtener un resumen no equivale a demostrar que el método funciona en otra tarea.

## Validación

`python3 -m unittest discover -s tests -v` prueba subtítulos, capturas, señales, ritmo, paleta, Gemini (con respuestas simuladas, sin red) y el flujo completo de `watch.py` con un video sintético local. Requiere ffmpeg y Pillow. Descargas de redes, Whisper e instalación real del plugin en Claude Code requieren validación adicional en el entorno destino.

## Origen

Base: paquetes `mukiwa-learn.skill` y `mukiwa-grab.skill` proporcionados por Bryan el 10 de octubre de 2026. La arquitectura de fotogramas + transcripción, el selector de detalle, el descarte de capturas casi idénticas y las capturas en tiempos exactos toman como referencia [Watch](https://github.com/bradautomates/claude-video) (MIT). `skills/mukiwa-learn/scripts/gemini.py` es una adaptación de su `gemini.py`: Copyright (c) 2026 Bradley Bonanno, licencia MIT (permite usar, copiar y modificar conservando este aviso). El resto es código propio.

Conservar las lecciones al actualizar. No subir cookies, claves ni medios privados. `_descargas`, `work` y binarios descargados quedan fuera de Git.
