# KIWA Control

Centro de coordinación portable en `skills/kiwa-control`. Incluye inventario, captura explícita de notas privadas, mejora por observaciones y guías para los cinco proyectos de CDIA. Su adaptación de Task Observer no es el bundle original; Claude-Mem, Headroom, Setup y OmniRoute aún requieren instalación y pruebas en el entorno destino.

## Claude Code

Actualizar el checkout a una versión que incluya este cambio. El plugin del repositorio descubre skills/; comprobar disponibilidad de kiwa-control en el cliente y leer su SKILL.md. No borrar la carpeta histórica de skills del disco externo. Comparar antes de enlazar o reemplazar copias.

## Claude web

Ejecutar `python3 tools/build_skills.py` en un checkout limpio con esta versión; el empaquetador ahora incluye `kiwa-control.skill`. Importarlo mediante Capacidades/Skills y verificar con una petición de inventario. La importación no arranca servicios ni sincroniza memoria con el Mac.

## ChatGPT Work

La copia personal se instala mediante el flujo de skills de ChatGPT; enlazar el repo no la actualiza automáticamente. Para futuras actualizaciones comparar ambas versiones y guardar por el mecanismo de cada anfitrión.

## Utilidades

`python3 skills/kiwa-control/scripts/control.py inventory --root skills` lista nombres, rutas y hashes.

Las notas requieren `--store` explícito fuera de cualquier repositorio. Ejemplo local: `python3 skills/kiwa-control/scripts/control.py note --store "$HOME/.local/share/kiwa-control/notes" --kind decision --text 'Decisión de prueba' --source 'Prueba local'`. Consultar con `notes --store` y la misma ruta. Esta es memoria explícita, no hooks automáticos.

## Pendiente en el Mac

Verificar ruta actual del checkout y skills instaladas. Leer references/integrations.md; instalar y probar cada servicio por separado, sin cambiar endpoints de todos los clientes a la vez. No activar pagos o sincronización remota por defecto. Conservar versiones y bibliotecas. No hay proceso de sincronización automática configurado por este cambio.
