---
name: kiwa-control
description: Coordinar el centro de control de skills MUKIWA entre ChatGPT Work, Codex, Claude Code y Claude web. Usar al instalar, fusionar, actualizar, inventariar o sincronizar skills, revisar correcciones repetidas, recuperar decisiones de trabajo o configurar memoria, compresión y proveedores. Conectar con kiwa-watch-learn sin reemplazar sus bibliotecas.
---

# KIWA Control

Gestionar capacidades, versiones, observaciones y continuidad. Tratar esta skill como instrucciones y utilidades portables, nunca como entrenamiento del modelo ni instalación automática de servicios.

## Identificar el entorno y la fuente

1. Detectar herramientas realmente disponibles. No inferir acceso al Mac desde una terminal remota.
2. Leer [registry.json](references/registry.json). Resolver las skills instaladas por el `name` de su frontmatter: sus carpetas pueden cambiar de nombre.
3. En GitHub usar `feeldavybzz/watch-skill` como fuente compartida para este centro. Conservar `skills/`, `kiwas/`, lecciones y herramientas existentes. No migrar ni borrar `design-skills` sin necesidad.
4. Inventariar antes de fusionar. Comparar contenido y hashes; nunca asumir que la versión más reciente de una plataforma reemplaza todos los cambios de otra.
5. Leer [environments.md](references/environments.md) antes de instalar o distribuir. No prometer sincronización en segundo plano. La copia local histórica es una pista, no un montaje comprobado.

## Observar y mejorar

Leer [observation.md](references/observation.md) cuando haya correcciones, decisiones reutilizables o revisiones. Registrar problema → mejora → principio, fuente, alcance y estado. Distinguir preferencia contextual de regla general. Buscar duplicados y habilidades relacionadas.

Fusionar con la skill especializada correspondiente: diseño con diseño, movimiento con motion, evidencia audiovisual con kiwa-watch-learn. Mantener aquí solo coordinación transversal. Preservar reglas existentes, excepciones y atribución; resolver contradicciones explícitamente. La autorización de Bryan para mejorar sus skills permite cambios pertinentes; respetar el alcance y las reglas del entorno anfitrión.

## Conservar continuidad

Guardar un resumen acotado con objetivo, decisiones, archivos/versiones, evidencia, pendientes y siguiente paso. Mantener memoria privada fuera de repositorios públicos. Usar el almacenamiento persistente real del anfitrión y verificar relectura; nunca decir “guardado” si solo quedó en una respuesta. Recuperar solo contexto relevante, no cargar todos los Kiwas ni toda la historia.

Para notas locales usar:

```bash
python3 scripts/control.py note --store RUTA_PRIVADA_PERSISTENTE --kind decision --text 'Decisión verificable' --source 'Origen concreto'
python3 scripts/control.py notes --store RUTA_PRIVADA_PERSISTENTE
python3 scripts/control.py inventory --root RUTA_SKILLS
```

El almacén debe ser explícito, fuera de repositorios públicos. Estas notas no sustituyen la memoria automática de Claude-Mem. En ChatGPT persistir archivos de la skill mediante el flujo de guardado personal; para memoria privada usar un destino persistente privado disponible. En ausencia de destino, comunicar la limitación sin fabricar persistencia.

## Integrar los cinco proyectos

Leer [integrations.md](references/integrations.md) antes de instalar servicios. Task Observer aporta observación; Claude-Mem aporta almacenamiento con hooks; Headroom aporta compresión; Setup aporta diagnóstico; OmniRoute aporta enrutamiento. No confundir una guía con el servicio operativo.

- Comprobar versiones, dependencias, licencia, configuración y autenticación en destino.
- Separar `documentado`, `instalado`, `configurado` y `verificado`; respaldar cada estado con evidencia.
- No copiar claves, cookies, bases de memoria ni material privado al repositorio público.
- Conservar originales de evidencia: la compresión es una vista recuperable. No resumir destructivamente transcripciones, timestamps o instrucciones críticas.
- No cambiar modelos, endpoints ni proveedores de una sesión por deducción. No habilitar servicios pagos o compartición adicional sin autorización aplicable.

## Cerrar un cambio

Validar scripts modificados y el paquete; guardar mediante el mecanismo real de cada anfitrión. Para mejoras del repositorio usar rama y conservar cambios ajenos. Informar qué quedó instalado, dónde se verificó y qué requiere el Mac o importación en Claude web. Nunca presentar un enlace a GitHub como instalación en todas las plataformas.
