# MUKIWA video skills

Usar skills/mukiwa-grab para obtener archivos y skills/mukiwa-learn para analizar evidencia y guardar lecciones. Leer su SKILL.md antes de trabajar.

Conservar las lecciones existentes. No borrar ni reemplazar toda la carpeta para actualizar código. No publicar videos descargados, cookies, claves, audio privado ni archivos de trabajo en Git.

Antes de cambiar algo, revisar git status y conservar cambios ajenos. Usar ramas para las mejoras. No decir que se vio todo el video si solo se revisaron muestras. Distinguir preparación de evidencia, análisis del agente y validación del método.

Pruebas: python3 -m unittest discover -s tests -v

Disco externo (exFAT): macOS crea archivos ocultos "._nombre" junto a cada archivo. Git los ignora y los scripts los saltan. El entorno de Python (venv) va en el disco interno, por ejemplo ~/.venvs/watch-skill: dentro del disco externo Python intenta leer esos ._*.pth y no arranca.

Para ver un video en un paso: python3 skills/mukiwa-learn/scripts/watch.py "LINK-O-ARCHIVO" --question "..." (detalle en skills/mukiwa-learn/SKILL.md). Gemini solo con --engine gemini y si Bryan lo pide.

Después de cada lección: clasificar en nichos y alimentar los profesores de profes/ (skills/mukiwa-learn/references/profesores.md). No borrar ni reescribir profesores enteros: fusionar.

Descargas: si fallan, retransmitir CAUSA/HAZ de mukiwa-grab; plan B = «Para analizar» del buzón. Cookies del navegador: solo para los sitios de ~/.config/mukiwa/permisos.json (hoy instagram.com, Chrome) y solo ante un fallo por sesión; para otros sitios, permiso explícito de Bryan en esa descarga. Nunca imprimir ni guardar valores de cookies. Buzón: skills/mukiwa-learn/scripts/inbox.py.
