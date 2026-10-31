# Distribución entre entornos

Una misma fuente puede alimentar varias instalaciones; cada anfitrión mantiene su copia y permisos.

| Entorno | Entrada | Verificación |
|---|---|---|
| ChatGPT Work | Skill personal guardada mediante su flujo de skills | Comprobar archivo remoto persistido; refrescar Skills si no aparece |
| Claude Code local | `skills/kiwa-control` del repositorio; instalar con el plugin existente o copia/enlace revisado | Abrir nueva sesión y solicitar la skill; comprobar ruta y lectura |
| Claude web | Importación de paquete generado por la herramienta del repo | Confirmar aceptación del paquete y probar una tarea |
| Codex local | Carpeta de skills admitida por su versión o lectura explícita del SKILL.md | Consultar configuración/documentación local; no asumir la ruta de ChatGPT Work |
| Nube con repositorio | Leer fuente/version fija y usar herramientas disponibles | No asumir hooks ni procesos locales permanentes |

Ruta histórica en Mac: `/Volumes/MUKIWA 2TB/CLAUDE DATA/CLAUDE PERSONAL SKILLS/`. Verificar que existe y comparar con el checkout de watch-skill antes de enlazar o copiar. No reemplazarla entera. Conservar el venv en disco interno cuando el externo sea exFAT.

GitHub verificado el 29-10-2026: feeldavybzz/watch-skill tiene skills, Kiwas, biblioteca y empaquetador; feeldavybzz/design-skills solo tenía README en la consulta. Mantener esta fecha como instantánea, no estado perpetuo.

Sincronización deliberada: leer versión origen y destino → comparar → fusionar → validar → guardar → releer. Un cambio en GitHub no actualiza automáticamente una skill ya instalada en ChatGPT o Claude web. No crear tareas recurrentes si no fueron solicitadas.
