# Integraciones externas

Consulta de fuentes primarias: 29-10-2026. Revalidar comandos y requisitos al instalar. Este centro contiene adaptaciones de flujos y guías; no incluye binarios, hooks ni servicios de terceros.

## Task Observer

Fuente: https://github.com/rebelytics/one-skill-to-rule-them-all
Usar la adaptación en observation.md para capturar y fusionar mejoras. Si se solicita el original, descargar el bundle completo con sus references/scripts y preservar CC BY 4.0; no instalar solo SKILL.md. No activar simultáneamente dos escritores sobre la misma cola.

## Claude-Mem

Fuente: https://github.com/thedotmack/claude-mem
En Claude Code, comandos documentados:

```text
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

Alternativa documentada: `npx claude-mem install`. Revisar el asistente antes de aceptar sincronización o proveedor. No tratar `npm install -g claude-mem` como instalación de hooks. Verificar Node y requisitos actuales del README. Comprobar trabajador, escritura de una nota de prueba no sensible y recuperación en otra sesión. El README anuncia otras integraciones, pero probarlas por separado; no implica compatibilidad con el chat alojado. Consultar LICENSE antes de incorporar o redistribuir su código.

## Headroom

Fuente: https://github.com/headroomlabs-ai/headroom
Instalación documentada: `uv tool install --python 3.13 "headroom-ai[all]"`, o entorno Python aislado con pip. El paquete npm es SDK, no CLI.
Prueba: `headroom doctor`; después `headroom wrap claude` o `headroom wrap codex` cuando esos clientes estén presentes. Revisar efectos de wrap: su README indica configuración de proxy y Serena; usar opciones actuales para controlar ese comportamiento. Consultar `--help` antes de activar.
Validar recuperación de originales, logs con errores, JSON con campos importantes y transcripciones con tiempos. Comparar calidad y consumo en la misma tarea. No prometer porcentajes ni limitar ventana de contexto por una configuración desactualizada. Licencia indicada por el proyecto: Apache 2.0; preservar avisos si se redistribuye código.

## Claude Code Setup

Fuente: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup
Comando de la guía CDIA: `/plugin install claude-code-setup@claude-plugins-official`; verificar catálogo del cliente al instalar.
Skill primaria revisada: `plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`. Su diagnóstico es de solo lectura. Adaptar aquí el procedimiento: inventariar stack, pruebas, herramientas y fricciones; recomendar 1–2 mejoras justificadas por necesidad. No habilitar conectores o automatizaciones solo por recomendarlos. No copiar referencias no leídas ni afirmar que el plugin está instalado al replicar este procedimiento.

## OmniRoute

Fuente actual: https://github.com/cheaper-inference/OmniRoute (la URL diegosouzapw/OmniRoute redirige allí).
Instalación citada en CDIA: `npm i -g omniroute`; consultar README/CLI actual antes de lanzar o conectar cuentas. Verificar el paquete y versión, proveedor, modelo, ruta, cuota y coste. Es una pasarela real, no una skill; no cambia el modelo interno de ChatGPT Work. Proveedores gratuitos requieren sus propias cuentas y cuotas. El traspaso a otros proveedores cambia a quién se envía el contenido. No guardar credenciales en el registro público. No encadenar proxies Headroom/OmniRoute hasta probar cada uno por separado. Licencia indicada: MIT; conservar avisos si se copia código.
