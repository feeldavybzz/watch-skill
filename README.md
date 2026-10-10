# watch-skill · MUKIWA

Skills de referencia y aprendizaje audiovisual para Claude Code: `mukiwa-grab` obtiene medios y `mukiwa-learn` relaciona transcripción con fotogramas y guarda lecciones.

## Instalar en Claude Code

Dentro de una sesión de Claude Code:

```text
/plugin marketplace add feeldavybzz/watch-skill
/plugin install mukiwa-video@watch-skill
```

Seguir la indicación de activación del cliente. Los nombres de las skills pueden aparecer con el prefijo del plugin. También se puede abrir este repositorio en Claude Code y pedir que lea `CLAUDE.md` y las skills directamente, antes de instalar globalmente.

## Dependencias

Python 3.9+ y ffmpeg/ffprobe en PATH son la ruta principal. Para extraer fotogramas sin ffmpeg del sistema se admite imageio-ffmpeg. Instalar las dependencias Python en un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Whisper es opcional: `python3 -m pip install faster-whisper`. Su primera ejecución puede descargar un modelo. No se necesita para usar subtítulos existentes. `probe.py` y la transcripción Whisper heredados necesitan ffprobe/ffmpeg del sistema.

## Flujo

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

`python3 -m unittest discover -s tests -v` prueba subtítulos y el flujo con un video sintético local. Requiere ffmpeg y Pillow. Descargas de redes, Whisper e instalación real del plugin en Claude Code requieren validación adicional en el entorno destino.

## Origen

Base: paquetes `mukiwa-learn.skill` y `mukiwa-grab.skill` proporcionados por Bryan el 10 de octubre de 2026. La arquitectura de fotogramas + transcripción también toma como referencia conceptual [Watch](https://github.com/bradautomates/claude-video). Esta versión no incorpora ni instala su código.

Conservar las lecciones al actualizar. No subir cookies, claves ni medios privados. `_descargas`, `work` y binarios descargados quedan fuera de Git.
