---
name: kiwa-orbit
description: Organiza chats, sesiones y proyectos en ChatGPT, Claude o Codex por marca, tema o actividad, adaptando la estructura al rubro del usuario, con títulos cortos en mayúsculas y emojis.
---

# ORBIT (kiwa-orbit)

> Origen: skill `organizar-chats` de Bryan (ChatGPT/Codex), copia de iCloud del 2026-10-30, integrada tal cual, más el índice maestro en `references/` y, el 2026-10-31, ruta de ejecución, nota para Claude y registro (`scripts/orbit_registro.py`). Si la versión mejorada en ChatGPT difiere, fusionar (no sobrescribir).

Organiza las conversaciones accesibles dentro de la plataforma autorizada. Adapta la estructura a la persona; no importes marcas, nombres, relaciones personales ni categorías de cuentas anteriores.

## Conocer el contexto

Para la cuenta de Bryan (MUKIWA), parte de `references/indice-maestro-bryan.md` (nueve áreas y reglas aprobadas), y confírmalo contra los proyectos reales.

Antes de clasificar, pregunta brevemente por el rubro o actividad principal, el uso profesional/personal de la cuenta y cualquier agrupación importante que el contenido no permita deducir. Usa las respuestas ya dadas; no repitas preguntas resueltas. Mientras esperas, puedes revisar títulos, proyectos y capacidades sin hacer movimientos que dependan de la respuesta.

Inspecciona proyectos existentes, títulos, resúmenes y contenido cuando sea ambiguo. Confirma equivalencias entre nombres o marcas con el usuario cuando no haya evidencia suficiente. No supongas que toda referencia genérica pertenece a un cliente ni asignes personas por edad o tipo de tarea.

## Estructura adaptable

- Cuando existan secciones, usa ÁREA → PROYECTO → CONVERSACIONES: el área agrupa un ámbito amplio y cada proyecto una marca, tema o actividad concreta. Si solo hay proyectos planos, usa esos proyectos reales y nombres claros; no inventes carpetas anidadas.
- Para trabajo recurrente con clientes, suele servir un área de MARCAS Y MARKETING con proyectos por cliente. Para otros rubros, adapta las áreas a sus actividades reales: investigación, operaciones, docencia, desarrollo o vida personal, por ejemplo. Son ejemplos, no una plantilla obligatoria.
- Reutiliza proyectos adecuados. Crea agrupaciones distintas cuando haya contenido que las justifique o el usuario solicite expresamente un espacio futuro; no inventes conversaciones ni declares pendientes por entidades solo mencionadas de pasada.
- Define la prioridad entre marca y actividad con el usuario cuando ambas encajen. Una marca puede reunir su campaña completa; un departamento compartido puede reunir generación de imágenes/video/motion, diseño/branding o desarrollo. Mantén disciplinas separadas si tienen contextos distintos; agrúpalas cuando formen el mismo flujo de trabajo solicitado. Evita duplicar chats para mostrar ambas rutas.
- Distingue COTIZACIONES (propuestas y presupuestos previos) de FACTURACIÓN (facturas, registros y automatización contable). En una estructura por marca, las de un cliente concreto permanecen con ese cliente; los proyectos generales de negocio reúnen plantillas, procesos, DGI o registros transversales sin un cliente predominante. Un presupuesto dentro de una campaña no obliga a trasladar toda la campaña. Respeta excepciones explícitas y no conviertas la organización en trámites o transacciones.
- Reúne conversaciones de un mismo servicio personal en un proyecto comprensible, como ENTRENAMIENTO Y NUTRICIÓN, preservando sesiones con enfoques distintos. Reunir en un proyecto no fusiona historiales.
- Conserva o reutiliza 💡 STUPID GALLERY · PREGUNTAS Y CURIOSIDADES para consultas variadas que no tengan otra categoría útil. No sirve como criterio para descartar contenido.

## Reunir conversaciones del mismo trabajo

Busca grupos de conversaciones relacionadas tanto entre los chats sueltos de una sección como dentro de proyectos amplios. Compara marca/cliente, objetivo, entregable, referencias y continuidad de decisiones. Compartir una herramienta o la palabra imagen no basta: dos clientes distintos no deben fusionarse por usar Photoshop.

Para cada grupo, identifica un proyecto existente adecuado y reúne allí las conversaciones cuyo contexto coincida, manteniendo títulos breves que distingan sus aportes. Si el usuario elige organización por marca, TODO encargo concreto de esa marca va a su proyecto: imágenes, video, motion, color, estrategia, cotizaciones y facturas relacionadas. Los departamentos generales quedan para técnicas, recursos o administración transversal sin un cliente predominante. No repartas una marca por herramienta. Solo una excepción explícita del usuario puede cambiar esta prioridad. Las consultas generales permanecen en su disciplina: color, motion, retoque, recursos o plugins. Una foto restaurada puede convivir con su tarea de restauración sin duplicar o borrar historiales.

Si conviven un chat de ChatGPT y una tarea local derivados del mismo encargo, vincúlalos conceptualmente por proyecto y prefijo; conserva la diferencia entre conversación inicial y ejecución. No deduzcas duplicidad por compartir título. Para una consolidación de contexto autorizada, crea una referencia con fuentes y decisiones actuales; separa lo vigente de lo sustituido. No mezcles fases o aprobaciones de versiones antiguas.

Distingue los tres resultados: mover a un proyecto, agrupar visualmente en una sección y reunir contexto en un documento. Verifica y comunica cuál se realizó. Si la app exige consentimiento para que una tarea local mantenga acceso a carpetas originales, deja ese traslado pendiente de la confirmación nativa; no edites rutas ni índices para forzarlo. Continúa con títulos y cambios independientes permitidos. No crear un proyecto duplicado para evitar ese requisito.

## Orden por uso y revisión incremental

Prioriza el chat actual y las conversaciones con mensajes nuevos desde la última revisión; después revisa pendientes y antiguos. Usa fecha del último mensaje del usuario cuando esté disponible. Una modificación de título puede cambiar updated_at: no la interpretes como actividad real ni vuelvas a procesar la misma tanda por eso.

Si el usuario pide ordenar por uso, configura Recientes y chats de proyectos por última actividad con las opciones reales de la app, preservando secciones y fijados manuales. No simules una clasificación automática de toda la cuenta ni cambies fijados sin petición. Si updated_at incluye cambios de metadatos, explica que los renombrados pueden subir temporalmente en Recientes.

Mantén un registro privado mínimo por ID: título anterior/nuevo, proyecto confirmado, última actividad observada, motivo y estado de verificación. Revisa primero lo cambiado; conserva un título correcto y estable aunque aparezcan palabras nuevas en el último mensaje. Renombra de nuevo solo si cambia el tema predominante o el título pierde precisión.

La skill actúa cuando se invoca o dentro de una programación autorizada. No vigila todas las conversaciones continuamente ni garantiza ejecución inmediata después de cada mensaje. En un chat que estés atendiendo y cuyo renombrado esté autorizado, revisa el título al cerrar una tarea o cuando cambie claramente su tema, sin interrumpir el trabajo principal.

## Nichos y títulos condensados

Usa MAYÚSCULAS con tildes. Usa un emoji al inicio del título cuando el usuario lo solicite; elige uno consistente por marca o nicho para facilitar el reconocimiento. Mantén el resto del título corto y en mayúsculas. Los emojis de los proyectos deben seguir el mismo criterio.

1. Identifica el contexto estable: marca/cliente si define el encargo; en otro caso, rubro, herramienta o actividad específica. Evita prefijos genéricos como IA o DISEÑO cuando uno concreto permita reconocer mejor el chat.
2. Identifica el objetivo o resultado predominante leyendo mensajes y resultados. Si la conversación evolucionó, conserva lo relevante del historial y distingue el estado actual del brief antiguo. No titules solo por la última frase ni por una marca mencionada de pasada.
3. Elige **NICHO · TEMA**, normalmente **2–5 palabras y unos 20–36 caracteres**, sin truncar nombres propios ni perder diferencias necesarias. Es un objetivo de lectura en la barra, no un límite rígido. Ejemplos genéricos: `MARCA · FEED`, `PLUGIN · LICENCIAS`, `MAC · BATERÍA`, `COCINA · TOSTADAS`.
4. Quita verbos de trámite (crear, revisar, ayudar), muletillas y detalles que ya se entiendan. Usa abreviaturas reconocibles y evita siglas inventadas. No impongas un nombre de marca tomado de otra cuenta.
5. Si dos chats quedarían iguales, añade el mínimo distintivo útil: actividad, entregable, variante o fecha. Para informes recurrentes, usa `BRIEFING · AAAA-MM-DD` con la fecha del informe, no la de importación; diferencia un intento fallido de un informe entregado. Para un chat vacío, no inventes tema.
6. Comprueba que el título permita reconocer nicho y asunto sin abrirlo. Si la categoría es ambigua, conserva el título útil o marca el caso para revisar; no fuerces una etiqueta.

Clasifica chats sueltos de Recientes, pero no prometas quitar ese panel. Si se solicitó acceso por proyectos en la izquierda, fija los útiles y desfija categorías vacías redundantes o chats sueltos que estorben, comprobando el resultado. Unificar la ubicación no fusiona historiales.

## Traslados y verificación

Prefiere herramientas propias de la app y usa su interfaz autorizada para funciones faltantes. Distingue asignación a una sección, pertenencia real a un proyecto y proyecto local vinculado a un directorio. Organizar chats no autoriza mover archivos locales ni cambiar rutas.

Revisa las páginas accesibles, incluidos chats antiguos y sesiones de trabajo, no solo recientes. Si un listado está limitado, usa su paginación cuando exista. Un índice local autorizado puede servir para descubrir IDs antiguos: sus títulos pueden estar desactualizados; consulta el estado actual mediante la herramienta de lectura antes de mutar. Excluye sesiones internas de revisión del sistema y no alteres índices o bases de datos a mano. Conserva archivos, instrucciones y memoria del proyecto al renombrarlo. Antes de retirar una agrupación, comprueba que sus elementos se trasladaron y revisa su contexto restante; no borres un proyecto porque la lista visible parezca vacía.

Verifica cada traslado por ID/enlace del chat o sesión en el destino, y cada renombrado por un listado o estado actualizado. Un nombre antiguo en la barra puede ser caché: recarga antes de repetir una acción. Mantén un registro local de cambios verificados y pendientes cuando el trabajo sea largo, sin incluirlo en la skill compartible.

Detén la tanda al primer límite de solicitudes o restricción de acceso; guarda lo confirmado y no eludas controles ni repitas operaciones sin comprobar su estado actual. No declares completa toda la cuenta si el inventario o la paginación son limitados.

## Limpieza y límites

Títulos iguales o temas parecidos no demuestran duplicidad. Compara contenido, archivos y resultados; conserva versiones con contexto distinto. Presenta candidatos concretos con sus diferencias y la conversación que se conservaría. Un chat mal clasificado se reclasifica; uno vacío o de poco aporte no se borra automáticamente.

No borres ni archives por defecto. Aplica archivo solo con autorización concreta suficiente y pide confirmación en el momento para eliminaciones permanentes. Si faltan herramientas, informa la limitación sin afirmar que eliminaste nada.

La skill no concede acceso a otras cuentas ni autoriza enviar mensajes, subir inventarios privados a otro asistente o programar ejecuciones. Esas acciones requieren un pedido separado. Al organizar varias plataformas, conserva sus inventarios privados separados.

## Entrega

Muestra la estructura final, algunos títulos representativos, cambios verificados, proyectos fijados si se solicitaron y pendientes reales. Distingue resultados observados de reportes de otro asistente. Adjunta evidencia visual cuando uses la interfaz. No confundas una solicitud aceptada con un cambio guardado ni prometas continuidad automática sin una programación expresamente solicitada.

## Ruta de ejecución (paso a paso)

1. **Contexto**: lee `references/indice-maestro-bryan.md` si es la cuenta de Bryan; si no, pregunta rubro y agrupaciones (una sola ronda).
2. **Inventario**: lista los chats con la herramienta de la plataforma (en Claude: búsqueda y chats recientes, solo lectura). Di cuántos viste y cuántos faltan; nunca declares la cuenta completa si el listado está limitado.
3. **Filtro incremental**: consulta `scripts/orbit_registro.py seen --id ID`. Si ya está `verificado` y el tema no cambió, sáltalo.
4. **Clasificación**: para cada chat da título propuesto (NICHO · TEMA) y destino, con una línea de motivo. Marca **confianza alta** solo si el contexto del chat decide el destino; el resto es **«revisar»**.
5. **Propuesta**: muestra una tabla `chat → título nuevo → proyecto`. Lo ambiguo va aparte, sin tocar. Espera aprobación del lote.
6. **Aplicar por lotes de ≤10**, solo lo aprobado. Tras cada lote, recarga y verifica por ID/enlace; registra con `orbit_registro.py add --estado verificado` (o `pendiente` si no se pudo comprobar).
7. **Detente** al primer límite de solicitudes, error de acceso o pantalla que pida permiso nativo. Reporta lo confirmado y lo pendiente.

## En Claude (claude.ai y la app)

- Las herramientas de chat (conversaciones recientes, búsqueda, leer un chat) son **solo lectura**: sirven para el inventario y para entender el contexto, no para cambiar nada.
- Renombrar o mover un chat se hace desde la interfaz con el navegador autorizado, un chat a la vez, verificando en la lista. Ruta probada el 2026-10-31 en claude.ai: abrir el chat → flecha junto al título → **Añadir al proyecto** (abrir el submenú con flecha derecha, escribir parte del nombre del proyecto y elegir el existente, no «Crear») → aparece «Movido a …»; luego flecha del título → **Cambiar nombre** → Cmd+A, escribir, Enter. Cuidado: el mismo menú tiene **Eliminar** y **Archivar**; no los uses.
- Los enlaces `claude.ai/chat/ID` que devuelven las herramientas de lectura pueden pertenecer a otra cuenta o sesión y abrir «Esa sesión ya no está disponible»; para actuar, abre el chat desde la barra lateral de la cuenta activa y usa el ID de la URL real.
- Los proyectos ya existentes y sus emojis mandan: reutiliza el emoji del proyecto o del nicho que Bryan ya usa en esa cuenta.
- Pide acceso al sitio antes de abrir la interfaz y no uses sesiones de otra cuenta.
- Los chats de Claude Code o tareas locales no se mueven de carpeta ni se editan por archivo: solo se les sugiere título.
- Un proyecto nuevo solo se crea con aprobación; si ya existe uno parecido, reutilízalo.

## Registro de correcciones (privado)

`scripts/orbit_registro.py` guarda en `~/.mukiwa/orbit-registro.jsonl` (fuera del repo) ID, título anterior y nuevo, proyecto, motivo y estado. Si Bryan corrige un destino, regístralo con `--estado verificado` y el título corregido: esa decisión gana sobre cualquier clasificación futura. No se guarda contenido de los chats.
