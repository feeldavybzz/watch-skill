# watch-skill · MUKIWA

Skills de referencia y aprendizaje audiovisual para Claude Code: `kiwa-watch-learn` baja medios, relaciona transcripción con fotogramas, guarda lecciones y se las pasa al Kiwa del oficio.

## Skills del repositorio

Todas llevan el prefijo **kiwa** y viven en `skills/` (las de oficio, en `kiwas/`):

| Skill | Para qué |
|---|---|
| `kiwa-watch-learn` | Bajar, ver, escuchar, analizar y aprender de videos; pasa lo aprendido al Kiwa del oficio. Fusiona `mukiwa-grab`, `mukiwa-learn` y `mukiwa-ver-videos`. |
| `kiwa-web` | Construir, conectar y publicar sitios completos en Hostinger: portfolio, web para cliente, SaaS y afiliados. Incluye lo visual (antes `kiwa-web-ui`): arquetipos, animación y efectos, estructura, qué conviene y qué no. Fusiona las cuatro `crear-web-*` y la de diseño premium. |
| `kiwa-marca-mascota` | Dirección de marca, dibujo retro cartoon y mascota MUKIWA. Fusiona `direccion-de-marca-y-mascota`, `retro-cartoon` y `retro-cartoon-mascota`. |
| `kiwa-instagram` | Carruseles y estudio de feed. Fusiona `slide-maker` e `instagram-feed-studio`. |
| `kiwa-ui-plugins` | Cómo animar la interfaz de los plugins de MUKIWA y mostrarla en video (springs, arrastre directo, render con `seek(t)`). Nace de promptsmotion.com; falta fusionar `mukiwa-ui-plugins` (solo en el Mac). |
| `kiwa-<nicho>` (`kiwas/<nicho>/`) | Un Kiwa por oficio (cinematografía, color grading, iluminación…). Antes se llamaban `profe-<nicho>`. |

`kiwa-watch-learn` está además enlazada como skill de proyecto en `.claude/skills/`, así que queda activa en cualquier sesión de Claude Code que abra este repositorio.

## Instalar en Claude Code

Dentro de una sesión de Claude Code:

```text
/plugin marketplace add feeldavybzz/watch-skill
/plugin install mukiwa-video@watch-skill
```

Seguir la indicación de activación del cliente. Los nombres de las skills pueden aparecer con el prefijo del plugin. También se puede abrir este repositorio en Claude Code y pedir que lea `CLAUDE.md` y las skills directamente, antes de instalar globalmente.

## Kiwas por nicho

Cada video analizado alimenta **mini skills por oficio** en `kiwas/<nicho>/` (color grading, diseño de logos, tipografía cinética…). Si el Kiwa no existe se crea; si existe, aprende más; si el tema ya lo cubre una skill propia de Bryan, se le añade el conocimiento en `references/aprendido-mukiwa.md`. Las herramientas (DaVinci, Premiere, After Effects…) son secciones dentro de cada Kiwa. Se escriben como instrucciones para hacer el trabajo, con fuente [n] por técnica.

```bash
python3 skills/kiwa-watch-learn/scripts/kiwas.py list      # Kiwas y skills existentes
python3 skills/kiwa-watch-learn/scripts/kiwas.py install   # enlaza kiwas/* en ~/.claude/skills/kiwa-<nicho>
```

Reglas de clasificación y fusión: `skills/kiwa-watch-learn/references/kiwas.md`. Índice: `kiwas/INDEX.md`. Los enlaces apuntan al disco externo: sin el disco conectado, los Kiwas no se cargan.

## Descarga robusta y buzón de links

- `skills/kiwa-watch-learn/scripts/doctor.py [--online]` revisa yt-dlp (y si hay versión nueva), el runtime de JavaScript que YouTube exige (detecta Node aunque no esté en el PATH), ffmpeg, gallery-dl, whisper y espacio, con el comando exacto de lo que falte.
- Los fallos se explican (`CAUSA[...]` / `HAZ:`): 429, login, privado, no existe, región, 403, JavaScript, red, 5xx. Reintenta con espera solo lo que lo merece.
- **Buzón** (`skills/kiwa-watch-learn/scripts/inbox.py`): Google Drive → `MUKIWA · Aprender` con `links-pendientes.md` (un link por línea; el atajo del iPhone lo llena, ver `docs/atajo-iphone.md`) y `Para analizar/` (videos guardados desde el celular, plan B cuando un link no se deja bajar). Cada noche la tarea programada `mukiwa-aprender-buzon` descarga, prepara y analiza lo pendiente, guarda las lecciones y alimenta a los Kiwas. `estado.md` dice qué pasó con cada cosa. Usa la sesión de Chrome solo para sitios que autorizaste en `~/.config/mukiwa/permisos.json` (hoy: instagram.com) y solo si el link falla por pedir sesión; `estado.md` lo anota.

## Copia semanal en Google Drive

Cada lunes, la tarea programada de la app de Claude `mukiwa-skills-drive-semanal` ejecuta `tools/sync_drive.py`, que empaqueta todas las skills (MUKIWA, Kiwas y las propias de `~/.claude/skills`) y las copia a `Mi unidad/MUKIWA · Skills de Claude` mediante Google Drive para escritorio. Solo copia lo que cambió; lo retirado va a `_retiradas/`. A mano: `python3 tools/sync_drive.py`.

## Usar en claude.ai (app de Claude)

```bash
python3 tools/build_skills.py
```

Genera un `.skill` por skill (`kiwa-watch-learn`, `kiwa-web`, `kiwa-marca-mascota`, `kiwa-instagram`, `kiwa-ui-plugins` y uno `kiwa-<nicho>` por Kiwa), con solo archivos de Git: sin descargas, claves ni `._*`. Subirlos en claude.ai → Configuración → Capacidades → Skills. `kiwa-watch-learn` ya lleva el descargador y la biblioteca de lecciones. En claude.ai el entorno suele bloquear YouTube e Instagram: subir el archivo de video en vez del link.

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
python3 skills/kiwa-watch-learn/scripts/watch.py "https://youtu.be/ID" --question "¿Qué técnica usa en el minuto 2?"
```

Descarga (o reutiliza), saca subtítulos o transcribe en la Mac, extrae capturas repartidas por todo el video, fija capturas a 1280 px del gancho y de los momentos que el presentador señala, mide ritmo de edición y paleta, y escribe `work/watch-…/informe.md` + `evidence.json`. Niveles: `--detail transcript|efficient|balanced|full`. Enfoque: `--start/--end`, `--at 4:32,13:11`.

Motor opcional `--engine gemini`: Google ve el video completo y responde. Requiere `GEMINI_API_KEY` en `~/.config/mukiwa/.env` (gratis en https://aistudio.google.com/apikey); los links de YouTube se envían a Google y los archivos se suben y se borran al terminar. Nunca se usa sin pedirlo.

Comparado con Watch: funciona con el Python 3.9 de la Mac sin Homebrew; limpia subtítulos automáticos en cascada (Watch solo quita duplicados exactos); detecta y captura solas las señales del presentador; capturas fijas a 1280 px para leer texto; reparte capturas por tramos e informa el hueco máximo; mide ritmo de edición, gancho y paleta; guía de análisis de reels; y guarda lo aprendido en una biblioteca.

## Flujo por pasos

1. Descargar un enlace con `python3 skills/kiwa-watch-learn/scripts/grab.py URL --out _descargas --max-height 720`.
2. Preparar un archivo local:

```bash
python3 skills/kiwa-watch-learn/scripts/prepare.py VIDEO --out work/referencia --transcript SUBTITULOS.srt
```

Sin subtítulos se puede omitir `--transcript` (evidencia parcial) o usar `--whisper` cuando esté configurado. `evidence.json` informa el estado; salida 0 significa evidencia visual y textual lista, salida 2 significa parcial o bloqueada. Nunca significa que el agente ya analizó el video.

3. El agente abre las hojas de contacto, revisa la transcripción, amplía momentos relevantes y escribe una lección con tiempos y límites.
4. Guardar la lección usando `save_lesson.py`; al reemplazar una lección se conserva una copia en `library/_history`.

Los fotogramas son muestras. No se promete inspección de cada fotograma ni transcripción perfecta. Obtener un resumen no equivale a demostrar que el método funciona en otra tarea.

## Validación

`python3 -m unittest discover -s tests -v` prueba subtítulos, capturas, señales, ritmo, paleta, Gemini (con respuestas simuladas, sin red) y el flujo completo de `watch.py` con un video sintético local. Requiere ffmpeg y Pillow. Descargas de redes, Whisper e instalación real del plugin en Claude Code requieren validación adicional en el entorno destino.

## Origen

Base: paquetes `mukiwa-learn.skill` y `mukiwa-grab.skill` proporcionados por Bryan el 10 de octubre de 2026 (hoy fusionados en `kiwa-watch-learn`). La arquitectura de fotogramas + transcripción, el selector de detalle, el descarte de capturas casi idénticas y las capturas en tiempos exactos toman como referencia [Watch](https://github.com/bradautomates/claude-video) (MIT). `skills/kiwa-watch-learn/scripts/gemini.py` es una adaptación de su `gemini.py`: Copyright (c) 2026 Bradley Bonanno, licencia MIT (permite usar, copiar y modificar conservando este aviso). El resto es código propio.

Conservar las lecciones al actualizar. No subir cookies, claves ni medios privados. `_descargas`, `work` y binarios descargados quedan fuera de Git.

## Copias en la nube (Drive e iCloud)
`python3 tools/sync_drive.py` (cada lunes lo corre la tarea programada del Mac) deja los `.skill` en la carpeta «MUKIWA · Skills de Claude» de Google Drive y de iCloud Drive, separados en **Skills by Mukiwa** (hechas por Bryan) y **Global Skills** (descargadas de otros o que Claude trae por defecto). Las de otros se declaran en `tools/skills-de-otros.txt` y los `.skill` ya hechos viven en `Global Skills/` junto a este repo; lo que lo retira de la lista pasa a `_retiradas/`, nunca se borra.
