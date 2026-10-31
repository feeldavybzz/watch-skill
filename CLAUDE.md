# MUKIWA video skills

Usar skills/kiwa-watch-learn (una sola skill) para obtener archivos, analizar evidencia y guardar lecciones. Leer su SKILL.md antes de trabajar.

Conservar las lecciones existentes. No borrar ni reemplazar toda la carpeta para actualizar código. No publicar videos descargados, cookies, claves, audio privado ni archivos de trabajo en Git.

Antes de cambiar algo, revisar git status y conservar cambios ajenos. Usar ramas para las mejoras. No decir que se vio todo el video si solo se revisaron muestras. Distinguir preparación de evidencia, análisis del agente y validación del método.

Pruebas: python3 -m unittest discover -s tests -v

Disco externo (exFAT): macOS crea archivos ocultos "._nombre" junto a cada archivo. Git los ignora y los scripts los saltan. El entorno de Python (venv) va en el disco interno, por ejemplo ~/.venvs/watch-skill: dentro del disco externo Python intenta leer esos ._*.pth y no arranca.

Para ver un video en un paso: python3 skills/kiwa-watch-learn/scripts/watch.py "LINK-O-ARCHIVO" --question "..." (detalle en skills/kiwa-watch-learn/SKILL.md). Gemini solo con --engine gemini y si Bryan lo pide.

Oídos (texto del audio) fuera del Mac: python3 skills/kiwa-watch-learn/scripts/oir.py "LINK-O-ARCHIVO" --out work/oidos [--whisper] [--budget 100]. Escalera y fallos en skills/kiwa-watch-learn/references/oidos.md. Sin transcript = «voz no verificada», nunca «sin voz». Permiso permanente de Bryan (2026-10-30): bajar subtítulos, transcripciones y el audio necesario para transcribir (yt-dlp, Whisper, instalar yt-dlp/faster-whisper) sin preguntar; borrar mis propios archivos de trabajo. NO incluye cookies de sitios fuera de permisos.json, contraseñas ni inicios de sesión.

Después de cada lección: clasificar en nichos y alimentar los Kiwas de kiwas/ (skills/kiwa-watch-learn/references/kiwas.md). No borrar ni reescribir Kiwas enteros: fusionar.

Descargas: si fallan, retransmitir CAUSA/HAZ de grab.py; plan B = «Para analizar» del buzón. Cookies del navegador: solo para los sitios de ~/.config/mukiwa/permisos.json (hoy instagram.com, Chrome) y solo ante un fallo por sesión; para otros sitios, permiso explícito de Bryan en esa descarga. Nunca imprimir ni guardar valores de cookies. Buzón: skills/kiwa-watch-learn/scripts/inbox.py.

## Centro de control de skills
Para inventario, instalación, fusión, continuidad o mejoras por correcciones, leer `skills/kiwa-control/SKILL.md` (viene de ChatGPT/Codex, PR #10 original, ya con los nombres actuales). Diferenciar una guía de integración de un servicio instalado y probado. La memoria privada queda fuera de este repositorio público. Los cambios entre ChatGPT, Claude web y el Mac requieren instalación/verificación en cada destino; no asumir sincronización automática. Nombres vigentes: kiwa-watch-learn (única skill de ver/bajar/aprender), kiwas/<nicho>; no quedan mukiwa-learn, mukiwa-grab ni profes/.
