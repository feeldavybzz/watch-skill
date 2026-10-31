# Archivar solo el material usado, con margen (handles), en DaVinci Resolve
> Cómo copiar a un archivo solo lo que usan las timelines elegidas, conservando margen para revisiones, y qué probar antes de borrar originales.

- **Fuente**: https://www.instagram.com/p/De82N99A-a8/ · reel de Instagram (autor no recuperado en la ficha)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local (WhisperX small) + descripción abierta en Chrome + 10 fotogramas muestreados
- **Confianza**: media — descripción, transcripción y fotogramas coinciden en la ruta del menú; es muestreo visual, no escucha humana

## Teoría (lo que se dijo)
- Se puede copiar solo el material usado por las timelines seleccionadas y recortarlo conservando unos fotogramas de margen (handles).
- El autor avisa: guardar el proyecto y probar el archivo antes de eliminar los originales.

## Práctica (lo que se ve)
- Ruta del menú: File → Media Management → Timelines → Copy → **Used media and trim**, con *keeping frame handles*.
- El ejemplo usa 50 fotogramas de margen. El autor muestra un archivo que pasó de 166 a 21 GB.

## Cruce teoría ↔ práctica
- Coinciden. El ahorro (166 → 21 GB) es **un caso del creador, no una garantía**: depende de cuánto material sin usar tenía el proyecto.

## Receta paso a paso
1. Selecciona **todas** las timelines que deben sobrevivir (las que falten dejan de tener material).
2. File → Media Management → Timelines → Copy → Used media and trim, con handles.
3. Elige el margen en fotogramas y conviértelo a segundos con los fps de la timeline: 50 fotogramas ≈ 2 s a 25 fps, ≈ 1,67 s a 30 fps y ≈ 2,08 s a 24 fps (cálculo nuestro).
4. Guarda el proyecto.
5. Abre la copia y comprueba: relink de los clips, audio, efectos y reproducción completa.
6. Solo entonces considera retirar fuentes. **Conserva los originales** hasta que la copia pase la prueba.

## Para MUKIWA
- Visual Edits: archivar proyectos de entrega cerrados sin perder la posibilidad de rehacer una revisión; el margen decide cuánto se puede alargar un corte después.
- No se ejecutó consolidación sobre ningún proyecto de Bryan: **pendiente de probar en su Resolve** con una copia.

## Límites
- No se vio el resultado de la consolidación ni el relink real. No se sabe si los handles se aplican igual a clips compuestos, Fusion o audio.
- Los gigas del ejemplo no se extrapolan.

## Conecta con
- [[evaluar-edicion-automatica-y-subtitulos-con-claude]]
