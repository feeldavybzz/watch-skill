# MUKIWA video skills

Usar skills/mukiwa-grab para obtener archivos y skills/mukiwa-learn para analizar evidencia y guardar lecciones. Leer su SKILL.md antes de trabajar.

Conservar las lecciones existentes. No borrar ni reemplazar toda la carpeta para actualizar código. No publicar videos descargados, cookies, claves, audio privado ni archivos de trabajo en Git.

Antes de cambiar algo, revisar git status y conservar cambios ajenos. Usar ramas para las mejoras. No decir que se vio todo el video si solo se revisaron muestras. Distinguir preparación de evidencia, análisis del agente y validación del método.

Pruebas: python3 -m unittest discover -s tests -v

Disco externo (exFAT): macOS crea archivos ocultos "._nombre" junto a cada archivo. Git los ignora y los scripts los saltan. El entorno de Python (venv) va en el disco interno, por ejemplo ~/.venvs/watch-skill: dentro del disco externo Python intenta leer esos ._*.pth y no arranca.
