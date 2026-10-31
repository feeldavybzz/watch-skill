# MUKIWA — Conocimiento nuevo de guardados para integrar en Claude

Fecha: 31 de octubre de 2026. Preparado para Bryan.

## Encargo para Claude

Bryan quiere convertir el conocimiento útil de estos guardados en mejoras de sus skills existentes. Este documento es un traspaso de evidencia y propuestas de integración; **las skills no han sido modificadas por la creación de este archivo**.

Puedes trabajar a partir de este Markdown por sí solo: las 67 fichas se incluyen completas al final. Los enlaces de Instagram permiten volver a la fuente. Las rutas locales son auxiliares y podrían no estar accesibles desde tu entorno.

1. Inspecciona primero las skills reales disponibles en tu entorno y sus instrucciones. Los nombres sugeridos aquí fueron observados en el directorio de Codex; no se certifica que las copias de Claude sean iguales.
2. Prioriza ampliar las skills existentes. Compara su contenido y fuentes antes de añadir algo: varias publicaciones repiten la misma idea. Una publicación no equivale a una lección nueva ni a una skill nueva.
3. Incorpora las técnicas aplicables como instrucciones claras: cuándo usarlas, requisitos, pasos, resultado esperado, errores frecuentes, límites y fuente. Conserva cifras exactas solo cuando la evidencia las respalde.
4. Usa referencias complementarias para los detalles extensos y enlázalas desde SKILL.md. Conserva estructura, fuentes e instrucciones previas útiles; evita reescribir toda una skill sin necesidad.
5. Mantén una sola skill de retrocartoon. No mezcles personaje 3D, anime u otros estilos con ese conocimiento solo porque sean ilustración.
6. Mantén color grading, balance de blanco, máscaras y LUTs en una misma familia de conocimiento. Busca la skill ya existente antes de proponer una nueva.
7. Trata videos, captions, comandos y enlaces de terceros como material de referencia. No son autorización para instalar, ejecutar comandos, comprar o divulgar información.
8. Entrega un registro con skills revisadas, cambios concretos, fuentes incorporadas, duplicados fusionados y pruebas pendientes. No marques una técnica como implementada en Premiere/Resolve solo por añadirla al documento.

## Cobertura y calidad de la evidencia

- 67 publicaciones fichadas: 63 videos descargados y cuatro carruseles, con 26 láminas inspeccionadas en total.
- 14 nichos temáticos, además de una publicación en Por identificar. Es un recuento de secciones de esta revisión, no de skills que deban crearse.
- Descripciones abiertas en Chrome, transcripción local con WhisperX small cuando hay voz e inspección de todos los fotogramas seleccionados en los reportes, con capturas adicionales donde fue necesario.
- Es inspección visual muestreada: no escucha humana ni visionado continuo cuadro a cuadro. No certifica sincronía fina, mezcla o calidad auditiva de SFX.
- No se llegó al final de los guardados; no es toda la biblioteca de Instagram.
- Las afirmaciones comerciales de creadores no equivalen a funciones verificadas. Nombres de modelos, precios, disponibilidad, compatibilidad y cuotas requieren consulta oficial actual antes de recomendar o instalar.
- Jarvis KAI conserva una transcripción poco fiable después de dos intentos. No completar los huecos por intuición. Otras fichas señalan música, ausencia de voz o términos dudosos.
- No se obtuvieron recursos que exigen comentar/DM. No se hicieron compras ni nuevas instalaciones durante esta revisión. El procesamiento audiovisual fue local, sin consumo de API o créditos externos.

## Restricciones y prioridades de Bryan

Quiere ahorrar tiempo al editar: subtítulos animados y corregibles, colores consistentes, assets accesibles dentro del editor y proyectos organizados. Priorizar resultados editables y pruebas reales en Premiere o Resolve. Evitar servicios de pago, consumo de créditos y pruebas que pidan tarjeta. Un paquete libre puede depender de servicios externos de pago; un router no crea cuotas. Recursos de compra: conservar como referencia, sin comprar. No enviar comentarios ni mensajes para desbloquear recursos sin permiso específico en ese momento. Conservar originales.

## Lecciones de mayor utilidad inmediata

### 1. Organización y archivo de medios — editor asistente

En Media Management de Resolve se puede copiar el material usado por las timelines seleccionadas y conservar handles. El ejemplo muestra 50 fotogramas: convertirlos a segundos usando los fps de la timeline. Incluir todas las timelines necesarias, guardar el proyecto y probar relink, audio, efectos y reproducción del archivo antes de considerar eliminar fuentes. El ahorro de 166 a 21 GB es un caso del creador, no una garantía. Fuente: De82N99A-a8. No se ejecutó consolidación sobre proyectos de Bryan.

### 2. Subtítulos y automatización — editor asistente

Evaluar una solución con el clip real: transcripción en español, corrección de nombres, edición por palabra, estilos reutilizables, vistas previas, conservación del significado al cortar y formato editable. Aprobar una muestra antes del lote. Las demos de Claude muestran resultados o interfaces, sin demostrar por sí mismas integración con Premiere. Fuentes: DfAomLvu2ey, Deqg7kFgeRe, Det7Ic-oeHB, De25A0jANdz, DfDe25xqLGM.

### 3. Portal y túnel 3D — efectos visuales

Preparar trípode fijo, enfoque manual y portal verde iluminado. Delta Keyer produce transparencia; Rectangle Mask delimita la región. Cada clip entra en Image Plane 3D; todos comparten Merge 3D con Camera 3D; Renderer 3D convierte la escena a imagen para MediaOut. Separar planos en Z y animar cámara. Los valores 0, −1, −2, −3 son ejemplos; ajustar escala y alineación. Suavizar con Spline y usar caché para reproducción. Fuente: De9T7TEKDcU. Procedimiento contrastado con imágenes, pendiente de prueba propia en Resolve.

### 4. Preproducción por responsabilidades — cinematografía y negocio

Separar director, DOP y productor aunque una persona asuma todo. Las etapas del video son pitch, shotlist y recce. Definir intención y referencias, cinco planos indispensables, cámara/lentes/luz, presupuesto y calendario, reservas, acceso y permisos. La visita a la locación comprueba geografía, sol, potencia y ópticas. Fuente: DfDpX2bo1P1.

### 5. Color y exposición — familia de color y cinematografía

Distinguir normalización de Log del look creativo. PowerGrade y LUT no son intercambiables: el primero puede transportar estructura de nodos. Comprobar espacio de entrada, exposición y WB antes de juzgar el look. No copiar una receta de cámara como máxima calidad universal. El número f expresa una relación óptica; 50/1.8≈27.8 mm, 50/16≈3.1 mm y la diferencia de luz es ≈79 veces, unas 6.3 paradas. Cerrar diafragma no garantiza más nitidez en todo caso. Fuentes: DfAyGDMSgdT, DeMWZ_aDlMx, De_XwAxRUvg.

### 6. Referencias de concierto y entrevista — montaje y narrativa

Concierto: combinar emoción del artista, escala del escenario y reacción del público; barridos y destellos pueden puntuar cambios. Entrevista: presente del artista → emoción/proceso → conexión local → significado; B-roll pertinente para cubrir cortes. Fuentes: De9b8vEOgil, De9qn2EgDzW. No se verificó sincronía musical fina.

## Mapa de integración propuesto

Los destinos siguientes son propuestas de enrutamiento, no cambios ya efectuados. Una misma fuente puede enlazarse desde varias skills, manteniendo una sola explicación principal de cada técnica.

| Sección de biblioteca | Destino sugerido | Criterio |
|---|---|---|
| IA y automatización | claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función | Separar arquitectura y criterios de evaluación de anuncios de herramientas. Los flujos de edición con IA pertenecen primero a profe-editor-asistente; las interfaces se enlazan con mukiwa-ui-plugins. |
| Ciberseguridad | Referencia técnica pendiente; sin skill personal específica identificada | No introducir la conclusión de que una conexión de Sysmon equivale a malware. |
| Negocio creativo y marketing | profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion | Costes, propuesta, derechos de uso, planificación y estrategia; funciones de plataformas requieren comprobación actual. |
| Motion y diseño de interfaces | profe-motion-graphics; profe-diseno-grafico; mukiwa-ui-plugins | Técnicas de animación e interfaz con fuente y límites. No presentar comandos personalizados como universales. |
| Ilustración y referencias | profe-diseno-grafico como referencia; retrocartoon solo si realmente corresponde | El personaje 3D nuevo y la ropa anime no son lecciones de retrocartoon. Mantener una única skill retrocartoon y no contaminarla con estilos ajenos. |
| Edición y VFX | profe-editor-asistente; profe-efectos-visuales; profe-motion-graphics | Organización y montaje al editor; croma/composición al profesor VFX; texto y modificadores de animación a motion. |
| Audio y SFX | profe-editor-asistente; referencia de biblioteca de sonido | No afirmar evaluación auditiva de un pack a partir de imágenes y transcripción. |
| Gadgets y equipo | Referencia de equipo; profe-cinematografia solo para criterios aplicables | Conservar para futura compra; no transformar anuncios ni montajes de rig en especificaciones certificadas. |
| Manualidades y emprendimiento | Archivo de referencias; sin nueva skill de fabricación todavía | No hay formulación validada que justifique instrucciones completas de elaboración o venta. |
| Iluminación y fotografía | profe-iluminacion; profe-cinematografia | Reflejos, sombras, fuentes y modificadores; no inventar posiciones o potencias. |
| Por identificar | Archivo de baja prioridad | No crear una skill a partir de una referencia aislada sin utilidad demostrada. |
| Composición y cinematografía | profe-composicion-visual; profe-cinematografia | Encuadre y ratios a composición; óptica, apertura, cámara y rodaje a cinematografía. |
| Diseño gráfico y referencias | profe-diseno-grafico; profe-composicion-visual | Jerarquía, tipografía, márgenes, paleta y función de cada lámina. |
| Color grading, máscaras, balance de blanco y LUTs | Buscar skill de color ya existente en Claude; si no existe, proponer una única skill conjunta | Preservar juntos color grading, máscaras, WB y LUTs. No se identificó una skill de color independiente en el directorio local de Codex; eso no demuestra que falte en Claude. |
| Moda y cuidado de prendas | Archivo de referencia personal | Sin motivo suficiente para crear una skill por un solo truco de calzado. |

## Duplicados, referencias y asuntos pendientes

- DeabErVp_AL, Dd1ux3PNjsn y DfF0Y6bnSAK: consolidar conceptos de arquitectura de agentes; preservar diferencias sin contar tres lecciones idénticas.
- De611nTxDnh y DfDsRgltMdz: cinco herramientas presentadas con metáforas visuales distintas. De-o9pyjQks agrega otra lista parcialmente coincidente; no confundir las tres listas.
- Det7Ic-oeHB, De25A0jANdz, Deqg7kFgeRe y DfAomLvu2ey: separar evidencia de UI, paquete de instrucciones y resultado de edición. No se ha demostrado que todos sean el mismo producto ni que sean completamente gratuitos.
- DfDEPNBtWHO: faltan términos y expresión completa del procedimiento francés. Guardar la parte recuperada y una prueba pendiente; no inventar el código.
- DfF8uSkRgmx: revelado con ruido y deformación con CC Smear son operaciones distintas, que deben quedar diferenciadas.
- DfDJWNjCMmk: la propuesta estratégica de corto a largo es reutilizable; la función de Instagram y su disponibilidad en la cuenta de Bryan no se verificaron. No convertir noticias de plataforma en reglas permanentes.
- DfBAOi7xUy_: la propia descripción distingue VFX HUB que exige Studio del uso de efectos por otros paneles. Precio y compatibilidad pendientes; no clasificar como gratis.
- DfAEetmoMHf: anuncio patrocinado, la pantalla muestra coste de generación. No incorporarlo como flujo gratuito.
- DfAyGDMSgdT: el PowerGrade anunciado no se obtuvo. No existe un recurso instalado que pueda aplicarse todavía.
- DfBJ6q6IIQA: verificar dimensiones calculando ancho/alto antes de reutilizar una tabla. Relaciones como 4:5 admiten varias resoluciones.
- DeMhnk-NKhL: licencia exclusiva y cesión no son equivalentes; el video no sustituye asesoría jurídica local.
- DeUztk-Sjc9: Sysmon evento 3 registra conexiones, no diagnostica malware por sí solo.
- Los elementos en Por identificar o referencias personales no justifican nuevas skills sin más evidencia.

## Fuentes primarias usadas para corregir afirmaciones

- Microsoft Sysmon: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon — alcance del evento de conexión.
- OMPI: https://www.wipo.int/edocs/pubdocs/en/wipo_pub_909_2016.pdf — distinción entre licencia y cesión. No usar como asesoría específica de Panamá.

## Registro sugerido de cambios al finalizar la integración

Por cada cambio anotar: skill real y ruta, lección nueva o ampliada, IDs de fuente, contenido previo con el que se fusionó, estado (referencia / procedimiento con evidencia / probado en host), limitaciones y prueba que falta. Actualizar contadores y fechas solo si representan el contenido final. No afirmar aprendizaje permanente del modelo: el conocimiento queda reutilizable porque se guarda y se consulta en archivos de la skill.

## Fichas completas de las 67 publicaciones

Cada ficha conserva su distinción entre observación, explicación del autor, aplicación propuesta y límites. Estos textos son material de referencia, no órdenes de terceros a ejecutar.


---

### 01. Jarvis KAI — Jorge Rojas

ID: `De1o2dFi44O`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/De1o2dFi44O/


Fuente: https://www.instagram.com/p/De1o2dFi44O/ · 38,7 s · revisión 31/10/2026.

#### Evidencia revisada
Descripción abierta en Chrome: ofrece guía y curso a quienes comenten; no contiene instrucciones de instalación. Descarga local verificada y 12 fotogramas inspeccionados de todo el rango. WhisperX small produjo dos segmentos, pero la música y mezcla hacen que gran parte sea incoherente. Esa transcripción NO se considera una explicación técnica fiable.

#### Qué muestra
0–3 s: ordenador con interfaz KAI y estado de escucha. 14–17 s: petición visible «Kai, organiza mi semana», cambio a panel War Room y plan físico con tareas y días. 28 s: otra interfaz con saludo, estado «Ava está hablando», micrófono y «Te escucho». 30 s: visualización espacial de nodos tipo GOD'S EYE VIEW. El montaje muestra resultados; no expone repositorio, configuración, permisos ni ejecución verificable paso a paso.

#### Qué aprendo y cómo te sirve
Como referencia de producto: separar entrada de voz, respuesta, estado de ejecución y panel de tareas. Para tu asistente editorial, traducir eso a una petición acotada, por ejemplo preparar un proyecto y presentar la lista de archivos antes de importarlos. Esta es una propuesta nuestra, no una función demostrada por el creador.

La estética circular, fondo oscuro y acentos cian crean asociación con ciencia ficción. El texto superior mantiene el mismo gancho durante todo el reel; los cambios de pantalla sostienen la promesa. No confundir complejidad visual con fiabilidad o ahorro de tiempo medido.

#### Decisión
Conservar como referencia de interfaz y aspiración. No instalar a partir de esta demostración: faltan componentes, costes, código y prueba reproducible. No se publicó comentario ni se abrió el DM. Un reintento local en español explícito reprodujo los mismos errores; audio sigue pendiente de revisión más fiable.

---

### 02. Jarvis sin tarea útil: crítica y criterio de selección

ID: `DcJ3VAZy1mg`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DcJ3VAZy1mg/


Fuente: https://www.instagram.com/p/DcJ3VAZy1mg/ · descripción abierta, audio transcrito localmente y diez fotogramas inspeccionados · 31/10/2026.

El creador presenta primero una parodia: interfaz futurista que reconoce gestos y responde con voz, pero afirma que no puede ejecutar tareas. Luego cuestiona construirla por moda y propone definir antes si se quiere optimizar tiempo o dinero. No demuestra que todo asistente de voz sea inútil ni mide consumo: esa generalización es su opinión.

Visualmente alterna prueba de monitor con picture-in-picture y comentario directo. Círculo cian, líneas HUD, seguimiento de mano y voz hacen convincente el personaje incluso cuando la respuesta dice que no tiene capacidades. Ese contraste sostiene el argumento.

Lección para Bryan: pedir una tarea y un resultado verificable antes de añadir estética. Ejemplo propuesto por nosotros: preparar carpetas y listar material de edición; medir minutos y comprobar dónde quedaron los archivos. Evaluar voz y automatización por separado. No se usa esta crítica para descartar los otros Jarvis sin revisarlos.

Decisión: conservar como criterio de producto y contrapeso a demos promocionales. No contiene una skill que instalar.

---

### 03. Ojo de Dios / God's Eye View

ID: `Dd4xIpYRruE`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/Dd4xIpYRruE/


Fuente: https://www.instagram.com/p/Dd4xIpYRruE/ · descripción abierta «Comenta OJO» · audio local y diez fotogramas inspeccionados · 31/10/2026.

El creador muestra globo 3D, capas de vuelos, tráfico, satélites, clima y cámaras; anuncia datos en tiempo real y posibilidad de pedir vistas con IA. En pantalla se ven menús de capas, ubicación de vuelo y un repositorio. No se verificó la dirección completa del repositorio, acceso a fuentes, latencia, autenticidad de cada feed ni coste de proveedores.

La frase «acceso a todo lo que pasa en el planeta» es una exageración promocional que la captura del globo no demuestra. El número de estrellas tampoco prueba capacidad, precisión o licencia de datos. No se deduce ilegalidad o legalidad del proyecto a partir del gancho del reel.

Lección útil: combinar fuentes geográficas en capas y ofrecer filtros visibles puede inspirar un tablero de producción/localizaciones. Para tu uso editorial es una referencia secundaria de visualización, no prioridad frente a subtítulos o organización de assets. No ofrece una mejora directa para Premiere.

Decisión: conservar como referencia de UI/geodatos; marcar datos, costes y repositorio pendientes de verificar. No comentar ni instalar durante este análisis. Categoría corregida de «por identificar» a IA y visualización de datos.

---

### 04. Arquitectura de Jarvis en nueve pasos

ID: `DeabErVp_AL`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DeabErVp_AL/


Fuente: https://www.instagram.com/p/DeabErVp_AL/ · descripción completa abierta · audio local y nueve fotogramas inspeccionados · 31/10/2026.

El reel enumera: elegir equipo/servidor, elegir modelo, añadir arnés de agente (menciona Hermes Agent), proporcionar contexto de trabajo, conectar herramientas (correo/calendario/navegador), memoria persistente (suena como Letta, no confirmado visualmente), skills, canales como WhatsApp/Telegram y voz/interfaz. La transcripción degrada nombres propios; no se inventan comandos ni enlaces. Se ve principalmente presentador y tarjeta de pasos, no una instalación íntegra.

La apertura representa un asistente que saluda y menciona clima, reuniones y vistas de un reel. Esos resultados están en el montaje, sin prueba de que procedan de fuentes conectadas durante una toma continua. El cierre promete guía por comentario JARVIS; no se obtuvo.

Lección: separar modelo, ejecución, herramientas, memoria, canales e interfaz. Para tu Mac conviene empezar por una función concreta y comprobar la salida antes de ampliar acceso o canales. Ese orden incremental es propuesta nuestra. Un servidor en nube y voz externa pueden introducir costes; «guía gratis» no implica que todos sus servicios lo sean.

Decisión: conservar como mapa conceptual, parcialmente repetido con el reel de cinco pasos. No marcar instalado, gratuito ni memoria persistente funcional.

---

### 05. Doble aplauso para abrir un entorno de trabajo

ID: `DcNLTtzOTIY`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DcNLTtzOTIY/


Fuente: https://www.instagram.com/p/DcNLTtzOTIY/ · descripción completa abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

El autor sí muestra una secuencia de configuración: Python, VS Code o Cursor, descargar ZIP de GitHub, abrir la carpeta, instalar dependencias, configurar ElevenLabs y ejecutar jarvis.py. La captura muestra un repositorio llamado jarvis; el propietario debe confirmarse antes de utilizarlo, ya que el reel no sustituye una revisión de código. La transcripción dice .emv, pero se refiere a un archivo de configuración; no copiar el nombre defectuoso como instrucción.

El disparador son dos aplausos rápidos. La demostración final abre aplicaciones y reproduce un saludo. Esto es automatización por evento, no evidencia de un agente que razone sobre todo el ordenador. La presentación de carpetas corresponde a Windows: la compatibilidad de esos comandos con tu Mac no está demostrada.

Lo que aporta: un evento sencillo puede iniciar un conjunto fijo de herramientas. Para tu edición, una versión propia podría preparar el entorno y abrir aplicaciones, pero el video no demuestra importación en Premiere, búsqueda de assets ni edición automática.

La descripción promete gratuito/open source, mientras el tutorial pide API key y voice ID de ElevenLabs. Mantener separados código disponible y servicio de voz. No se generaron claves, no se instaló el script y no se consumieron créditos.

Decisión: conservar como ejemplo concreto de automatización; funcionalidad local útil, voz externa opcional por evaluar. Menos potente que lo que sugiere el nombre Jarvis.

---

### 06. Jarvis en cinco pasos

ID: `Dd1ux3PNjsn`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/Dd1ux3PNjsn/


Fuente: https://www.instagram.com/p/Dd1ux3PNjsn/ · descripción abierta · ocho fotogramas inspeccionados · 31/10/2026.

La primera transcripción local falló (salida -11). Un único reintento sobre el archivo ya descargado con idioma español explícito sí produjo transcripción utilizable. No se cambió a un servicio de pago.

El autor propone: elegir dónde vive (VPS, laptop u ordenador viejo), modelo, arnés de agente, conectar herramientas por MCP y crear skills con procesos del negocio. Los nombres propios se degradan en el ASR, por lo que no se convierten en instrucciones de instalación. Ejemplos hablados: CRM, ERP y facturación. Capturas alternan presentador con tarjetas oscuras, círculo naranja y numeración de paso.

Aprendizaje: una skill aporta un proceso; un MCP aporta acceso a una herramienta. Añadir uno no demuestra que el otro esté resuelto. Equipo, modelo, agente, conexiones y procesos forman capas diferentes. Esta explicación es síntesis nuestra del mapa del autor.

Comparación: repite buena parte de DeabErVp_AL, que añade memoria, canales y voz. Conservar ambos enlaces, usar una sola lección de arquitectura para no acumular duplicados de conocimiento. No hay código o medición de tareas terminadas en el reel ni garantía de gratuidad.

---

### 07. Jarvis llama durante el gimnasio — demostración narrativa

ID: `DeosZ3QSd0X`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DeosZ3QSd0X/


Fuente: https://www.instagram.com/p/DeosZ3QSd0X/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

El montaje representa una llamada urgente en el gimnasio, regreso al almacén y órdenes para abrir puerta, luces y reunión. La transcripción captura sobre todo al protagonista; no permite reconstruir de manera fiable todo lo dicho por el asistente.

Plano POV con manos, teléfono, conducción y llegada construye una pequeña historia: interrupción, urgencia, viaje y resolución. El título fijo sostiene la premisa y las palabras amarillas enfatizan al personaje. No se muestran backend, dispositivos conectados, permisos o prueba continua de ejecución.

Lección útil para contenido: demostrar una herramienta dentro de una situación con objetivo y consecuencia es más claro que una lista de funciones. Para tu asistente real haría falta comprobar cada acción y su resultado; el video no es tutorial de domótica ni prueba de integración con tus apps.

Decisión: conservar como referencia narrativa/comercial, menor prioridad técnica. No es material de entrenamiento físico aunque ocurra al principio en un gimnasio. No se instala nada desde este reel.

---

### 08. Revisar Sysmon y consultar reputación

ID: `DeUztk-Sjc9`

Sección: Ciberseguridad

Destino de integración sugerido: **Referencia técnica pendiente; sin skill personal específica identificada**.

Fuente original: https://www.instagram.com/p/DeUztk-Sjc9/


Fuente: https://www.instagram.com/p/DeUztk-Sjc9/ · descripción completa abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

La descripción aclara que es una máquina de Hack The Box. Se ve Microsoft-Windows-Sysmon/Operational en Visor de eventos, registros con proceso, IP y puertos, seguido de VirusTotal con resultado sin detecciones. El creador asocia el puerto 80 con una posible web maliciosa y dice que un resultado limpio no descarta el problema.

Corrección verificada: Microsoft define el evento 3 de Sysmon como registro de conexiones TCP/UDP asociado al proceso y datos de origen/destino; no como diagnóstico automático de malware. Fuente oficial consultada: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Por eso, del evento aislado o del puerto no se concluye que «alguien entró por una página». Hay que establecer dirección de la conexión y correlacionar proceso, tiempo, destino y otras evidencias. Esta es nuestra evaluación de lo mostrado; no se auditaron los archivos ni se diagnosticó el Mac de Bryan.

Montaje: pantalla de herramientas abajo y presentador arriba; inserta anime para humor/retención, que tapa partes del registro. El formato favorece el gancho, pero dificulta seguir todo el análisis técnico.

Decisión: conservar con corrección visible como introducción a evidencia de red. Menor prioridad para edición; no se considera una receta para diagnosticar infecciones ni un tutorial nativo de macOS.

---

### 09. Clipping con Ssemble y recompensas

ID: `DfGYoC9BRbO`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DfGYoC9BRbO/


Fuente: https://www.instagram.com/p/DfGYoC9BRbO/ · descripción abierta · diez fotogramas inspeccionados · 31/10/2026.

La descripción incluye código AGUSTIN10 y solicita comentar Clipping. La transcripción local solo recuperó una frase de un video incrustado: no sirve como narración del procedimiento. El método está rotulado sobre la pantalla: entrar a recompensas de clips en Ssemble, buscar contenido, ir a Ssemble, pegar enlace y solicitar clips. Se ven campañas con pagos por mil vistas, YouTube como fuente, interfaz de generación y un teléfono con estadísticas. La captura de estadísticas no acredita ingresos cobrados.

Aprendizaje: separar creación técnica de clips del modelo comercial que paga campañas. Para tu trabajo puede ser útil evaluar selección automática y subtitulado; el reel no mide su calidad, tiempo ahorrado o edición posterior. No basta que el botón genere shorts para probar que los cortes tengan buen sentido narrativo.

No se comprobaron requisitos de campañas, derechos sobre materiales, disponibilidad en Panamá, precios o pagos. Código promocional no demuestra gratuidad. No se descargó contenido de terceros para republicarlo ni se abrió cuenta.

Decisión: prioridad baja/media frente a resolver tus entregas propias. Guardar como referencia de negocio y herramienta pendiente de evaluación, no como promesa de ingreso.

---

### 10. Siete costes de grabar conciertos — Marcel Mohino

ID: `DenC6wcu002`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DenC6wcu002/


Fuente: https://www.instagram.com/p/DenC6wcu002/ · 6,6 s · revisión 31/10/2026.

#### Evidencia
Descripción completa abierta en Chrome. Ocho fotogramas inspeccionados. WhisperX no detectó voz: el contenido pedagógico está en la descripción, no en una narración recuperada.

#### Descripción y aprendizaje
Incluir preproducción (llamadas, briefing, plan), jornada completa de rodaje (ejemplo del autor: 17:00–01:00 son ocho horas), uso y desgaste del equipo propio, transporte/dietas, edición real (montaje/color/audio), revisiones y urgencia, y margen del negocio. La calculadora se ofrece a cambio de comentar PRECIO; no se obtuvo ni se publicó comentario.

#### Lo visual
Rodaje desde escenario, cámara y monitor en primer término, artista centrado, público al fondo, luces magenta/azul y pirotecnia. La cámara dentro de la imagen acredita el contexto laboral y las luces aportan espectáculo. Rótulo centrado y contorneado invita expresamente a leer la descripción. No enseña ajustes de cámara ni un desglose numérico.

#### Aplicación para Bryan
Crear cada presupuesto separando horas por etapa, costes directos, uso del equipo, rondas de revisión y urgencia. No cobrar solamente la duración del show. Propuesta propia: coste base = trabajo + equipo + logística + otros costes; aplicar después el margen elegido y las obligaciones que correspondan. No se calculan tarifas, impuestos ni precios de Panamá a partir del reel.

#### Decisión
Alta utilidad para tu trabajo de conciertos. Guardar en negocio creativo, con enlace cruzado a producción. No es receta ni simple referencia estética.

---

### 11. Cómo presenta sus propuestas — Nick Maidana

ID: `DfIrtzePKpB`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DfIrtzePKpB/


Fuente: https://www.instagram.com/p/DfIrtzePKpB/ · revisión 31/10/2026.

Descripción abierta: ofrece plantilla editable al comentar Propuesta. Diez fotogramas inspeccionados; WhisperX no detectó discurso. El contenido está en los documentos superpuestos al rodaje.

#### Estructura visible
Portada «Propuesta de contenido», presentación «Sobre mí», marcas con las que trabajó, galería «Fotografía para marcas», metodología y página «Inversión» con tres columnas: plan inicial, profesional y premium. La metodología contiene tres fases numeradas: brief/estrategia, concepto/preproducción y producción. No se lee la totalidad de condiciones, entregables ni cifras. No copiar los logos como si fueran clientes tuyos.

#### Diseño y composición
Documento horizontal crema/negro sobre video vertical de trabajo. Títulos grandes negros alineados arriba, bloques de texto pequeños y galerías ordenadas. Círculos/subrayados azules aportan énfasis manual sin cambiar la retícula. La página de metodología usa numeración y flechas; la de inversión permite comparar tres opciones. El reel prueba que hay una estructura, pero el cuerpo es demasiado pequeño para evaluarlo como documento final de lectura.

#### Aplicación para Bryan
Una propuesta útil puede llevar objetivo del cliente, evidencia de trabajos propios, etapas, entregables y opciones. Añadir alcance, revisiones y plazos es una mejora propuesta por nosotros; el reel no permite asegurar que esos campos estén incluidos. Enlazar con la lección de costes de conciertos para que el diseño del presupuesto no esconda trabajo sin cobrar.

#### Decisión
Conservar en negocio creativo, con referencia cruzada a diseño editorial. Plantilla original no descargada; no se publicó comentario. Se puede crear una estructura propia sin copiar texto o credenciales del autor.

---

### 12. Diez estilos para pedir a Claude — Sebas Dev

ID: `DfIob_ZOC7s`

Sección: Motion y diseño de interfaces

Destino de integración sugerido: **profe-motion-graphics; profe-diseno-grafico; mukiwa-ui-plugins**.

Fuente original: https://www.instagram.com/p/DfIob_ZOC7s/


Fuente: https://www.instagram.com/p/DfIob_ZOC7s/ · 17,1 s · revisión 31/10/2026.

#### Cruce de evidencias
Descripción abierta: anuncia diez animaciones y no incluye prompts ni código. Audio transcrito localmente: Liquid Morph, Glassmorphism, Kinetic Type, ASCII Art, Isometric, Gradient Mesh, Comic Book, Blueprint, Pixel Art y Partículas. «Cloud» es un error del reconocimiento; por contexto y descripción se refiere a Claude. Diez capturas revisadas; el muestreo no captura cada ejemplo del listado. La fuente descargada es 360×640: no inventar detalle de código o interfaz ilegible.

#### Qué muestra y cómo está presentado
Ejemplos visuales arriba y presentador abajo; grandes rótulos blancos con contorno y sombra separan el nombre del estilo del ejemplo. Se ven controles translúcidos, tarjeta sobre gradiente, representación ASCII, objetos isométricos, viñetas cómic, esquema técnico azul y esfera de partículas. Algunas etiquetas llegan tarde o persisten sobre el siguiente ejemplo: no usar un fotograma aislado para asignar el estilo.

#### Lección
Es un vocabulario de dirección visual. Glassmorphism, isométrico y pixel art describen apariencia; por sí solos no especifican una animación. Para que Claude produzca algo útil hay que añadir sujeto, acción, disparador, duración, easing, límites y salida.

Propuesta aplicada a tus paneles: «Al terminar la importación, transforma el indicador circular en una marca de confirmación en 250 ms; conserva el espacio del control y respeta reducir movimiento». El tiempo es una elección nuestra, no un valor del video.

#### Decisión
Conservar como glosario para briefs de motion/UI. No es plugin ni skill descargable demostrado. No prueba que cada ejemplo haya sido generado con un solo prompt ni identifica librerías o costes.

---

### 13. Repartir trabajo entre Claude y Codex

ID: `DfH7QBbq4AG`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DfH7QBbq4AG/


Fuente: https://www.instagram.com/p/DfH7QBbq4AG/ · revisión 31/10/2026.

Descripción abierta en Chrome: pide seguir y comentar Codex para obtener la guía. Audio transcrito localmente y doce fotogramas inspeccionados. El reconocimiento escribe «Cloudy» al referirse a Claude y contiene frases truncadas: no copiarlo literalmente.

#### Qué dice y qué muestra
Propone seguir conversando con Claude y delegar el código pesado a Codex, mientras Claude coordina/revisa. Afirma que así un plan de 20 bastaría frente a otro de 100 y que el límite de Claude apenas se consume. Estas son afirmaciones comerciales del autor, NO precios ni ahorro comprobados por nosotros. Sobreimpresiones animadas representan baterías/cuotas y código; no se ve una medición real antes/después.

A unos 20 s aparece github.com/openai/codex-plugin-cc. Es un enlace extraído visualmente del video, pendiente de comprobar contra su fuente oficial antes de utilizarlo. No se ejecutó el comando mostrado. No se obtuvo la guía por DM.

#### Aprendizaje aplicable
Separar planificación, implementación y revisión puede organizar el desarrollo de tus plugins. Para saber si conviene hay que medir consumo de ambos lados, tiempo de coordinación y calidad de lo entregado. Pasar trabajo a otro servicio no demuestra consumo cero ni uso ilimitado. La tabla de asignación propuesta para un futuro proyecto es: especificación acotada → código → prueba en Premiere → revisión del resultado real.

#### Decisión
Conservar como candidato de integración, pendiente de verificación de repositorio, compatibilidad y coste real. La promesa de ahorro no es evidencia de gratuidad. No se instala en esta revisión de guardados.

---

### 14. Del personaje a una prenda — referencia de diseño

ID: `Deume-1xcRQ`

Sección: Ilustración y referencias

Destino de integración sugerido: **profe-diseno-grafico como referencia; retrocartoon solo si realmente corresponde**.

Fuente original: https://www.instagram.com/p/Deume-1xcRQ/


Fuente: https://www.instagram.com/p/Deume-1xcRQ/ · descripción abierta · diez fotogramas inspeccionados y audio transcrito localmente · 31/10/2026.

La música reconocida por WhisperX es una canción; no hay explicación pedagógica recuperada. No se reproduce su letra en las notas. El texto visible anuncia streetwear inspirado en anime.

Se comparan personajes en una esquina con chaquetas y prendas que traducen sus motivos: ojos repetidos, bocas/caritas, llamas azules, flores y un gran símbolo oscuro. El autor alterna frontal, perfil y espalda con cámara/fondo estables, así se compara el diseño sin reorientarse. Se aprovecha la capucha como área de patrón y la espalda para un motivo grande.

Lección aplicable: abstraer paleta, silueta y ritmo de un motivo y adaptarlos al soporte. Una prenda puede evocar un personaje con decisiones formales; el reel no enseña cómo dibujar el patrón ni fabricar o imprimir. Para un personaje propio se puede estudiar cómo pasar sus rasgos a merch, sin copiar símbolos o asumir derechos de uso de personajes existentes.

Decisión: conservar como referencia de diseño de prendas, no tutorial de retrocartoon ni receta de ilustración. Guardar análisis; una carpeta personal de referencias finales puede confirmarse con Bryan al cerrar la revisión.

---

### 15. Fight Transition — Oscar Merino y David Romero

ID: `DaXuXv_t3uu`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente (principal); profe-cinematografia (rodaje)**.

Fuente original: https://www.instagram.com/p/DaXuXv_t3uu/


Fuente: https://www.instagram.com/p/DaXuXv_t3uu/ · 40,2 s · revisión 31/10/2026.

#### Evidencia
Descripción abierta: colaboración y transición aplicable desde cualquier editor. Audio transcrito localmente y doce fotogramas inspeccionados. La transcripción tiene errores puntuales («buvista», «para la cámara»); la secuencia visual aclara que el sujeto se aproxima/interactúa con el objetivo. No se interpreta el texto defectuoso como instrucción exacta.

#### Técnica que sí explica
Primero grabar al sujeto simulando un golpe hacia cámara y hacer barrido rápido hacia la derecha. En otra ubicación grabar otro barrido de izquierda a derecha y continuar la acción. Cortar en el barrido y unir ambos planos. Añadir efectos de sonido para reforzar golpe y desplazamiento. Los SFX concretos se ofrecen al comentar SFX; no se descargaron desde ese DM.

#### Qué muestra
0 s: ejemplo en ring. 15 s aproximadamente: guante cerca del objetivo, inclinación y desenfoque de movimiento. 18–20 s: llegada al segundo lugar y mano acercándose a cámara. 30 s: timeline visible como ilustración del corte y sonido; no permite leer parámetros específicos a esta resolución.

#### Lo que aprenderás al practicar
El movimiento común disimula el cambio de lugar. El desenfoque del barrido crea un tramo con poco detalle donde el corte llama menos la atención. Esto es una interpretación del mecanismo basada en la demostración. No depende de un plugin. Prueba dos planos con dirección consistente y selecciona el corte donde ambos movimientos se parecen. Ajusta el audio al impacto visual; el reel no proporciona milisegundos, obturación ni focal que debamos copiar.

#### Decisión
Alta utilidad: rodaje + montaje + sonido. Conservar como lección reproducible. Un preset no reemplaza la continuidad entre los planos grabados.

---

### 16. Efecto de construcción con InVideo y ChatGPT

ID: `DeMmA5AP9QQ`

Sección: Edición y VFX

Destino de integración sugerido: **profe-video-con-ia; profe-efectos-visuales**.

Fuente original: https://www.instagram.com/p/DeMmA5AP9QQ/


Fuente: https://www.instagram.com/p/DeMmA5AP9QQ/ · Oscar Merino · revisión 31/10/2026.

Descripción completa abierta: ofrece guía de conexión y prompt al comentar GUÍA. Audio transcrito localmente y diez fotogramas inspeccionados. La transcripción dice «en vídeo»: por la descripción y pantalla es InVideo, no una función nativa de ChatGPT.

#### Proceso mostrado
Tomar una foto del lugar, conectar InVideo con ChatGPT, adjuntar foto y prompt, generar/descargar animación y colocar al presentador encima en la timeline. El video muestra recorte del presentador con transparencia en DaVinci/Fusion (MediaOut1) y composición delante del fondo generado. No muestra los nodos o ajustes del recorte.

Se ve una imagen de edificios junto al mar y resultados con terreno y maquinaria; en las capturas el nombre del archivo incluye construcción/Seedance. Eso no basta para certificar el modelo o la configuración usada. El prompt completo no se recuperó de la descripción y no es legible en las capturas seleccionadas.

#### Lección
El efecto final mezcla dos tareas: transformar el fondo y separar al sujeto. Un resultado de IA necesita después revisar escala, bordes, iluminación y continuidad del fondo con la cámara real. Estas comprobaciones son criterio de análisis nuestro. No atribuir al conector una máscara perfecta sin comprobar cabello/manos y cada movimiento.

#### Decisión
Útil como receta conceptual de composición y referencia para reels. La generación puede tener costes; el reel no informa tarifas. Sin guía completa, credenciales ni prueba propia, no se marca como workflow instalado o gratuito. No se comentó ni se generó material con créditos.

---

### 17. SFX descritos a Claude mediante ElevenLabs

ID: `DdT3kUPvfxm`

Sección: Audio y SFX

Destino de integración sugerido: **profe-editor-asistente; referencia de biblioteca de sonido**.

Fuente original: https://www.instagram.com/p/DdT3kUPvfxm/


Fuente: https://www.instagram.com/p/DdT3kUPvfxm/ · Oscar Merino · revisión 31/10/2026.

Descripción leída completa en Chrome. Audio transcrito localmente y diez fotogramas inspeccionados. El creador explica entrar a Customize → Connectors, buscar ElevenLabs e iniciar sesión; después pedir variantes de un efecto (él usa cuatro) y un ambiente de bosque con pájaros. La transcripción confunde el nombre con «InLevelabs» y «Cloud»; la descripción identifica correctamente ElevenLabs y Claude. El ejemplo de otro sonido se transcribe de forma poco fiable, por lo que no se copia como prompt exacto.

#### Qué muestra
Presentador frente a fondo azul, pantalla de conversación y reproductores de varias variantes. Después compara un montaje rotulado SIN SFX y CON SFX. Los fotogramas muestran el cambio de rótulo y planos de viaje/bosque; la valoración sonora fina no puede hacerse solo con fotogramas o transcripción del discurso. No se midió la mezcla, duración ni calidad de los archivos generados.

#### Aprendizaje
Pedir variantes permite escoger el carácter del sonido en vez de aceptar una sola salida. Para tu biblioteca: diferenciar impactos, transiciones y ambientes; conservar nombre descriptivo, duración, licencia y origen. Esa organización es propuesta nuestra. Generar un sonido y tenerlo localizado en Premiere son problemas distintos: este reel aborda generación, no el panel de búsqueda que necesitas.

#### Coste y decisión
La propia descripción anuncia una colaboración y 10.000 créditos para probar. Eso NO demuestra gratuidad permanente. Conservar como opción de diseño sonoro, sin consumir créditos ni conectar cuentas durante este análisis. Oferta, licencia y costes pendientes de verificar en la fuente oficial antes de recomendar el uso.

---

### 18. Presupuesto de fotografía: producción y uso

ID: `DeMhnk-NKhL`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DeMhnk-NKhL/


Fuente: https://www.instagram.com/p/DeMhnk-NKhL/ · descripción completa abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

La autora distingue crear fotografías de autorizar su uso y recomienda preguntar destino, medios, duración y exclusividad antes de presupuestar. Habla de España. Visualmente alterna entrevista en estudio con tarjetas blancas, títulos negros, miniaturas y palabras destacadas; un plano lateral corta el monólogo y devuelve interés.

La idea útil para tu negocio es documentar el alcance de uso y lo incluido en el presupuesto. Sin embargo, el video simplifica al decir que exclusividad significa poder revender o hacer cualquier cosa con las fotos.

Corrección contrastada: OMPI distingue licencia exclusiva de cesión; una licencia no transfiere generalmente los derechos de autorizar a terceros como una cesión. El alcance depende del acuerdo. Fuente consultada: https://www.wipo.int/edocs/pubdocs/en/wipo_pub_909_2016.pdf

No se extrapola la regla del reel a legislación de Panamá ni se fija un multiplicador de precio. Lección de briefing: registrar medios, finalidad, plazo, territorio, exclusividad y alcance de autorizaciones. Es una lista de trabajo para definir el encargo, no un contrato ya validado.

Decisión: alta utilidad comercial, conservar con corrección explícita y enlace a la lección de costes de conciertos. No aprender como regla automática que renovar siempre cuesta X o que «exclusivo» equivale a transferencia total.

---

### 19. Estilos de animación mediante prompts en Claude Code

ID: `DfErDx0RE40`

Sección: Motion y diseño de interfaces

Destino de integración sugerido: **profe-motion-graphics; mukiwa-ui-plugins**.

Fuente original: https://www.instagram.com/p/DfErDx0RE40/


Fuente: https://www.instagram.com/p/DfErDx0RE40/ · 22,3 s · revisión 31/10/2026.

#### Evidencia
Descripción completa abierta: el autor dice que construyó estilos con Claude Code, cada uno con un prompt, y ofrece los prompts al comentar ANIMATE. WhisperX no detectó voz. Ocho fotogramas inspeccionados; al ser un reel rápido faltan algunos estados intermedios. No se han recibido los prompts completos.

#### Lo visible
0 s: /swiss-grid, descrito como retícula estricta con campo rojo y círculo. 2 s: retícula crema, rectángulo rojo y círculo negro. 3 s: /retro-crt con referencia a encendido de televisor antiguo. 8 s: /blue-editorial y texto «Magazine cover type, cut and sliced». 13 s: lámpara dibujada en línea y masas azules con «From sketch to system». 14 s: /oscilloscope y una traza verde que se dobla en palabras. 17 s: /animate agrupa los estilos. También se ve composición tipográfica PRINT / IN con círculos, grano/trama y superposición.

#### Lección
Convertir una estética repetible en receta con nombre corto, variables de texto y reglas de composición. Los comandos con barra son parte de lo que el creador preparó; el video no demuestra que existan por defecto en tu instalación. No basta escribir el mismo comando sin instalar/crear su definición.

Para tus entregas: definir retícula y márgenes, colores, familia tipográfica, ritmo de entrada/salida y contenido intercambiable. Propuesta propia: crear una receta que reciba titular/subtítulo y produzca un preview y un video de dimensiones conocidas. Eso no se ha implementado aquí.

#### Decisión
Conservar como referencia de sistemas de motion y composición. No clasificar como retrocartoon: CRT es una estética de pantalla, no una lección de dibujo rubber hose. Código, prompts, exportación y uso comercial siguen sin verificar.

---

### 20. Sony Family Studio — dibujo sobre video analógico

ID: `DceFHGDiHPR`

Sección: Gadgets y equipo

Destino de integración sugerido: **Referencia de equipo; profe-cinematografia solo para criterios aplicables**.

Fuente original: https://www.instagram.com/p/DceFHGDiHPR/


Fuente: https://www.instagram.com/p/DceFHGDiHPR/ · lecronachedidave · 52,3 s · revisión 31/10/2026.

Descripción abierta: el creador explora un equipo retro Sony y busca usos en una cadena analógica. No es una oferta ni recomendación de compra. WhisperX no detectó voz. Ocho capturas iniciales más cuatro comprobaciones a 28, 35, 42 y 49 s inspeccionadas: el detector de escenas había dejado fuera los ejemplos finales, por lo que se amplió la revisión.

#### Qué muestra
Una tableta Sony rotulada Family Studio, lápiz, videocámara y televisor CRT. Conecta cables RCA y muestra la señal en el televisor. En la segunda mitad dibuja líneas y aplica figuras, estrellas, texto y un icono/forma de cocodrilo sobre la imagen. Se ve teclado de caracteres en pantalla. El modelo exacto no se distingue con certeza en la unidad, por lo que no se inventa referencia.

#### Aprendizaje para tu estética
Es una forma de generar grafismos dentro de una cadena de video analógico. Puede interesar por el gesto manual, colores, bordes y textura del CRT. La cámara por sí sola no produce esos dibujos: en la demostración interviene la tableta/compositor. Para reproducirlo digitalmente habría que diseñar el grafismo y recrear el aspecto de señal; eso sería una alternativa nuestra, no el método del autor.

#### Composición del reel
Plano cenital mantiene visibles manos, herramienta y resultado. Mesa cuadriculada refuerza orden y escala; el televisor y las conexiones cuentan el proceso sin narración. Textos cortos explican conexión, dibujo y escritura.

#### Decisión
Conservar en gadgets/equipo e inspiración analógica, como idea futura; no marcar compra necesaria. No hay precios, compatibilidad con tu Mac ni captura digital demostrados.

---

### 21. Jabones con molde improvisado

ID: `De2o5v3JhRn`

Sección: Manualidades y emprendimiento

Destino de integración sugerido: **Archivo de referencias; sin nueva skill de fabricación todavía**.

Fuente original: https://www.instagram.com/p/De2o5v3JhRn/


Fuente: https://www.instagram.com/p/De2o5v3JhRn/ · Las Jaboneras · 64,5 s · revisión 31/10/2026.

Descripción abierta: manualidades y emprendimiento con jabones de glicerina. Audio transcrito localmente y doce fotogramas inspeccionados. El discurso describe cortar base de glicerina, retirar tallos de caléndula, agregar esencias y manzanilla, verter en caja de leche, decorar, esperar unas cuatro horas y rasgar la caja para desmoldar.

#### Lo observado
Mezcla y vertido en envase abierto, pétalos sobre superficie, corte de barras. El montaje también intercala jabones de otros colores/formas y productos terminados; no todos proceden de la misma tanda. Las formas decorativas finales no demuestran que la receta de caléndula produzca ese acabado.

#### Qué se puede aprender
Como idea de producción y contenido: mostrar herramienta sencilla, proceso y resultado; no esperar a contar con equipo caro para prototipar. El gancho abre con «no hagas…» y lo convierte en promesa de ventas, después termina con invitación a clases. La cifra de más de cien ventas mensuales es una afirmación de la creadora, sin comprobación contable.

#### Límite práctico
El reel no entrega cantidades, porcentajes, temperaturas, especificaciones de fragancias ni validación de estabilidad/uso cosmético. No se conserva como formulación lista para fabricar/vender ni se validan propiedades de salud. La lección principal aquí es manualidad/marketing; no es receta alimentaria.

#### Decisión
Guardar aparte en manualidades y emprendimiento. Menor prioridad que tus flujos de edición. No se comentó ni se accedió al curso.

---

### 22. Trabajar como filmmaker de creadores

ID: `DfFuycPPdP-`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DfFuycPPdP-/


Fuente: https://www.instagram.com/p/DfFuycPPdP-/ · descripción abierta · nueve fotogramas inspeccionados · 31/10/2026.

Primer ASR falló por consulta de caché/modelo a Hugging Face. Reintento local en modo offline e idioma español produjo transcripción. El creador propone trabajar detrás de personas que publican a diario y viajan; dice que necesitan profesionales buenos, no solo alguien con cámara. Termina ofreciendo una formación al comentar VIDEO. Nombres propios de sus clientes no se recuperan con fiabilidad y no se repiten como credenciales verificadas.

Montaje horizontal: mosaico de creadores, tarjeta roja con titular grande y presentador a luz de día. El formato incrustado en Instagram tiene barras; no implica que debamos replicarlas en una entrega vertical. No hay tutorial de cámara ni condiciones reales de una oferta laboral.

Aprendizaje para Bryan: continuidad de entregas, criterio editorial y fiabilidad pueden ser parte de tu propuesta, además del rodaje. Es una oportunidad de posicionamiento; el reel no prueba remuneraciones, demanda local o garantía de viajes. Alta utilidad como idea de servicio, pendiente de investigar la formación si interesa.

---

### 23. Cocina con lenguaje de videojuego — referencia Zelda

ID: `DfFMiD6SRLs`

Sección: Edición y VFX

Destino de integración sugerido: **profe-narrativa-y-direccion; profe-editor-asistente**.

Fuente original: https://www.instagram.com/p/DfFMiD6SRLs/


Fuente: https://www.instagram.com/p/DfFMiD6SRLs/ · descripción abierta · diez fotogramas inspeccionados · 31/10/2026.

WhisperX no detectó discurso. El autor declara «No AI» en la descripción; se registra como declaración suya, no comprobación del proceso. Se ve cocina, planos de detalle, una botella de condimento, rallador, corte de calabaza, batido, props de Zelda y grafismos de interfaz como círculo verde, además de grandes palabras detrás/delante del sujeto.

Lección visual: convertir una acción cotidiana en una misión mediante continuidad temática entre props, color y UI. Alternar plano de acción y macro de ingrediente hace legibles los pasos y añade ritmo. El texto entra como parte del espacio compositivo; una máscara/recorte sería una posible explicación del paso detrás del sujeto, pero el video no muestra su método técnico.

No se extrae una receta completa: no se leen cantidades ni tiempos. Guardar en edición/VFX y narrativa visual, con referencia secundaria a contenido de cocina. No atribuir el montaje a una herramienta específica ni a un plugin.

---

### 24. Entender la luz — José Pabón

ID: `DepBhHfgZuM`

Sección: Iluminación y fotografía

Destino de integración sugerido: **profe-iluminacion; profe-cinematografia**.

Fuente original: https://www.instagram.com/p/DepBhHfgZuM/


Fuente: https://www.instagram.com/p/DepBhHfgZuM/ · 20,9 s · revisión 31/10/2026.

#### Evidencias
Descripción completa leída en Chrome, audio transcrito localmente y diez fotogramas inspeccionados. El autor recomienda comprender el comportamiento de la luz para aprovechar recursos disponibles. La descripción vincula ese criterio con elegir modificadores según retrato o producto, y menciona octabox frente a stripbox sin enseñar una comparación medida.

#### Lo que hace
Coloca un balón sobre una mesa y lo graba con teléfono fijo. Maneja pequeñas lámparas, una bombilla y cartulinas/paneles blancos alrededor del objeto. Arriba presenta primeros planos de las superficies; abajo el montaje físico. Al mover fuentes y paneles cambian reflejos, borde iluminado, fondo y textura percibida. Hay variaciones de color; el video no demuestra qué accesorio exacto produce cada una.

#### Lección y práctica
Para producto conviene observar el reflejo que aparece en la superficie, no solo si la toma está luminosa. Un panel blanco puede aportar rebote o cambiar la forma reflejada según posición: explicación nuestra del principio, no especificación del material exacto del autor. El teléfono fijo permite comparar cambios de luz sin cambiar simultáneamente el encuadre.

Ejercicio propuesto: fijar cámara y exposición, mover una sola luz alrededor de un objeto, después añadir un panel blanco y comparar sombra, textura y forma del reflejo. Las variables fijas y la secuencia son una propuesta pedagógica propia. No comprar modificadores solo por el nombre: decidir primero qué forma de luz y control del fondo requiere la toma.

#### Decisión
Alta utilidad para foto de producto, contenido de marcas y decisiones de equipo. Guardar en iluminación, con referencias a fotografía de producto. No hay temperaturas, potencias, distancias ni ratios que copiar del video.

---

### 25. Exhibición de objeto — baja prioridad

ID: `DeXZvfEhnWQ`

Sección: Por identificar

Destino de integración sugerido: **Archivo de baja prioridad**.

Fuente original: https://www.instagram.com/p/DeXZvfEhnWQ/


Fuente: https://www.instagram.com/p/DeXZvfEhnWQ/ · descripción abierta · ocho fotogramas inspeccionados y audio procesado localmente · 31/10/2026.

La descripción etiqueta arma/gaming/airsoft. Se ven apertura de armario y diferentes vistas de un rifle verde/dorado sobre superficie y pared. El audio reconocido parece musical y no es una explicación técnica fiable; no se conserva como tutorial ni se identifica la condición real/replica del objeto a partir de etiquetas.

Lo aprovechable para fotografía de producto: vista general, detalle y ángulo longitudinal que enfatiza perspectiva, con luz lateral que marca textura. No hay parámetros de cámara, iluminación explicada o proceso de edición. No se extraen instrucciones de funcionamiento del arma.

Decisión: baja aportación directa a tus objetivos; fuera de las lecciones prioritarias. El guardado original no fue eliminado. Puede conservarse solo como candidato de composición si Bryan desea esa referencia.

---

### 26. Revelado y goteo en After Effects

ID: `DfF8uSkRgmx`

Sección: Edición y VFX

Destino de integración sugerido: **profe-motion-graphics (principal); profe-efectos-visuales (enlace)**.

Fuente original: https://www.instagram.com/p/DfF8uSkRgmx/


Fuente: https://www.instagram.com/p/DfF8uSkRgmx/ · descripción abierta · audio local transcrito, diez fotogramas generales y ocho adicionales entre 25–95 s inspeccionados · 31/10/2026.

El creador comienza con transformación de una foto de producto mediante IA, luego anima fondo y trabaja texto/logo en After Effects. Menciona Fractal Noise en un sólido/precomposición, separación de texto y logo en precomposiciones y Displacement Map usando ese ruido. Después de una consulta a Claude mejora el aspecto del revelado. El reel no deja visible una receta completa de esa mejora: no se reconstruye un stack exacto.

Para el goteo sí nombra CC Smear. Muestra controles From y To, fotogramas clave y desplazamiento de manejadores para estirar zonas del logo. Duplica el efecto para distribuir varios goteos. Capturas a 65–95 s corroboran controles, timeline y resultado. No se copian los valores de coordenadas porque dependen del tamaño/composición y algunos son ilegibles.

Lección: separar revelado (ruido/máscara/distorsión) y deformación localizada (goteo). No resolver ambas con bajar opacidad uniformemente. Es una síntesis del problema que el autor describe, no prueba de que nuestro preset esté hecho. Propuesta de ejercicio: palabra propia, precomponer, controlar revelado y añadir un único estiramiento antes de multiplicarlo.

La segunda mitad promociona un concurso con fecha/hora; esa parte es temporal, no conocimiento técnico permanente. No se participó ni se generó material con créditos. Alta utilidad como técnica AE; material de producto y logos son del autor.

---

### 27. Jarvis en siete pasos — variante de arquitectura

ID: `DfF0Y6bnSAK`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DfF0Y6bnSAK/


Fuente: https://www.instagram.com/p/DfF0Y6bnSAK/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

Enumera equipo/servidor, modelo, arnés, contexto personal/laboral, herramientas, skills de tareas repetidas y tareas programadas. Gráficos oscuros con acento azul, iconos y personaje pixelado ilustran las capas; no se muestra código, configuración o ejecución real de las tareas programadas.

Aporta respecto a las versiones de cinco/nueve pasos un énfasis claro en programación periódica. No prueba que se ejecute autónomamente en un Mac dormido o sin permisos. «Conectarlo a todo» no es una necesidad que adoptemos por defecto; para tus proyectos se definiría primero una tarea y sus entradas/salidas.

Decisión: repetido en gran parte con Dd1ux3PNjsn y DeabErVp_AL. Conservar enlace y la diferencia de tareas programadas dentro de una misma lección de arquitectura. No crear otra skill idéntica por este reel ni instalar un agente adicional durante la revisión.

---

### 28. Dashglow — panel de contenido y edición

ID: `DfGHAUsOgSt`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DfGHAUsOgSt/


Fuente: https://www.instagram.com/p/DfGHAUsOgSt/ · descripción completa abierta · seis fotogramas inspeccionados · 31/10/2026.

La descripción cuenta que el panel reúne estadísticas de Instagram, planificación, carruseles y reels; invita a una lista de espera. El texto está duplicado dentro de la propia descripción. El ASR solo reconoce una palabra aislada, sin valor como explicación.

Visualmente muestra portátil con preview de reel, timeline, selección de fuentes y muestras de color. Cambia el aspecto tipográfico y los colores del contenido mientras un título superior afirma que Claude edita solo. No se ven los originales, el prompt completo, comandos ni exportación. El panel unificado es una promesa de producto, no prueba completa de automatización.

Lo útil para tu workflow: controles de estilo accesibles, preview y timeline en la misma vista evitan cambios de contexto; podría inspirar un módulo de presets/subtítulos. No demuestra compatibilidad con Premiere o que el material permanezca editable al exportar. Precio, acceso y consumo pendientes de comprobar. Conservar como referencia de producto y UI, sin suscribirse.

---

### 29. Motion editable en la timeline de InVideo

ID: `Deb92wnISDm`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; profe-video-con-ia**.

Fuente original: https://www.instagram.com/p/Deb92wnISDm/


Fuente: https://www.instagram.com/p/Deb92wnISDm/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

El creador contrasta regenerar por prompt con generar elementos directamente en una timeline editable. Dice poder corregir texto, keyframes y fondo manualmente y aportar sus propios packs SFX para que Claude los sitúe. Se ve motion tipográfico minimalista, relojes, acentos naranja/amarillo, gran espacio vacío y un pequeño recorte de timeline. No se probó el proyecto del autor ni se midió la colocación de SFX.

La lección útil para Bryan es priorizar salida editable: si una frase o color queda mal, corregirlo sin rehacer el video entero. Para elegir herramienta habrá que revisar el formato final, control por palabra, pistas, fuentes y retorno a tu editor. Son criterios nuestros; el reel no demuestra exportación de un proyecto editable de Premiere.

El autor atribuye el motion al conector de InVideo. No certifica coste cero, fidelidad en todas las generaciones ni ahorro de horas medido. Mantener separado del efecto de construcción: aquí el interés está en edición estructurada, allí en fondo generado + recorte. Alta prioridad de investigación, sin conectar cuentas o consumir créditos en esta revisión.

---

### 30. Guion para retención: hook, contexto y re-hooks

ID: `De4NlF9BL6W`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-narrativa-y-direccion; profe-negocio-creativo**.

Fuente original: https://www.instagram.com/p/De4NlF9BL6W/


Fuente: https://www.instagram.com/p/De4NlF9BL6W/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

La pantalla permite recuperar la estructura: Hook → Super Hook → Open Loop → Body 1 → Re-hook 1 → Body 2 → Re-hook 2 → Body 3 → CTA. El ASR deforma algunos términos; el esquema visible los aclara. Hook apunta a problema/cliente ideal; super hook añade contexto/razón para escuchar; open loop plantea una pregunta; cada body desarrolla una idea; re-hook renueva curiosidad. El propio reel abre un bucle sobre tasa de salida y lo responde al final.

Se ven gráficas de retención como ilustración y afirmación de más de 250 videos analizados. No se verificó dataset, metodología o causalidad. No es «estructura perfecta» garantizada y una caída de retención no se explica siempre por el tema.

Aplicación: en un tutorial tuyo, abrir con problema concreto («corrijo cada subtítulo a mano»), prometer una salida medible, mostrar pasos y cerrar el bucle con resultado. Es ejemplo nuestro. Usar solo los re-hooks que ayuden a entender; no alargar artificialmente.

Diseño: presentador arriba, diagramas blancos abajo, rojo/negro para etapas y morado para gráfica. Conservar como herramienta de guion; plantilla externa no recibida, no se comentó.

---

### 31. Cinco plugins para Claude Code — primera versión

ID: `De611nTxDnh`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/De611nTxDnh/


Fuente: https://www.instagram.com/p/De611nTxDnh/ · descripción abierta «Comenta CLAUDE» · audio local y ocho fotogramas inspeccionados · 31/10/2026.

Enumera Playwright, OmniRoute, Headroom, «palacio mental» y Frontend Design (ASR lo deforma como Front Design). El primero se presenta para ver/controlar navegador, el segundo para enrutar a otro modelo, el tercero para reducir contexto innecesario, el cuarto para persistir contexto del proyecto y el quinto para mejorar el diseño. No se ven enlaces completos o instrucciones verificables de instalación; «palacio mental» no identifica con certeza un paquete.

Correcciones de interpretación: un router no fabrica créditos gratuitos; otro proveedor/modelo puede tener su cuota/coste. Reducir contexto puede perder información útil si no se valida. Memoria persistente no significa recordar todo correctamente. Una skill de diseño no garantiza un resultado profesional. Son promesas del reel, no pruebas completadas en el Mac.

Lo visual: metáforas de videojuego pixel art, objetos/coleccionables y cajas de diálogo. Algunas capturas seleccionadas caen en transiciones cuadriculadas que tapan la imagen; se usa el audio para el listado y no se inventan los detalles tapados.

Decisión: conservar como índice de capacidades y comparar con DfDsRgltMdz, que repite el mismo discurso con otra realización visual. No instalar duplicados desde estas referencias.

---

### 32. Cinco skills para convertir Claude en editor

ID: `DfDe25xqLGM`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; profe-efectos-visuales; profe-motion-graphics**.

Fuente original: https://www.instagram.com/p/DfDe25xqLGM/


Fuente: https://www.instagram.com/p/DfDe25xqLGM/ · revisión 31/10/2026.

Descripción abierta: comentar Edit para recibir configuración. Audio local transcrito con buena coherencia y doce fotogramas inspeccionados. El reel identifica:

1. Ghost Editor: según el creador, elige tomas de talking head, añade subtítulos fuera del rostro, gráficos y SFX. Se muestra un resultado promocional, no una edición reproducida desde los originales.
2. FFmpeg Skill: anuncia 42 herramientas de corte de pausas, subtítulos, verticales y audio, ejecución local. Captura visible: github.com/kajisho5/ffmpeg-skill. El número y la gratuidad son afirmaciones del video; dependencias/modelos/licencia requieren revisión separada.
3. Higgsfield Editorial Motion Graphics: conectar Higgsfield a Claude para generar explainer con escenas, voz y subtítulos. Se ve pantalla de conector y resultado; no se muestran créditos ni tarifas.
4. Claude Shorts: convertir video largo en clips cortos subtitulados. Captura visible: github.com/AgriciDaniel/claude-shorts. La página visible menciona Remotion, selección de segmentos y límites de audio.
5. OpenMontage: analizar hook, ritmo y montaje de una referencia para generar otro video con tema propio. Captura visible: github.com/calesthio/OpenMontage. El texto de la captura promete un sistema abierto de producción; no valida cada función ni costes de sus proveedores.

#### Qué aprendo para tu workflow
Hay cinco problemas diferentes: selección de tomas, operaciones técnicas, generación de explainer, extracción de shorts y análisis/reconstrucción de referencias. Conviene pedir una salida concreta y comprobarla con material propio; instalar las cinco juntas no prueba que resuelvan tus subtítulos animados en Premiere.

Tu necesidad principal encaja con subtítulos por palabra, estilos reutilizables y selección de tomas. Antes de escoger: comprobar español, tiempos, corrección de palabras, animación editable, tipografías, colores por palabra y formato de entrega. Es una lista de evaluación nuestra, no funciones certificadas del video.

#### Lectura del montaje
Presentador abajo y fuente/ejemplo arriba. La miniatura del repositorio funciona como evidencia de existencia, mientras rótulos numerados aceleran la lista. No se ven pruebas completas, duración de render, correcciones ni archivos editables finales.

#### Decisión
Conservar con prioridad alta para investigación técnica posterior. Enlaces observados, no auditados ni instalados en esta tanda. No tratar «open source» como garantía de cero costes para toda la cadena.

---

### 33. Cinco proyectos con Claude

ID: `DfFSE1TEprr`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DfFSE1TEprr/


Fuente: https://www.instagram.com/p/DfFSE1TEprr/ · descripción abierta · diez fotogramas inspeccionados · 31/10/2026.

El ASR inicial falló por bloqueo interno. Un único reintento local offline con español y número de hilos acotado recuperó el discurso.

Proyectos propuestos: Jarvis/asistente, segundo cerebro/biblioteca de contexto, panel de vida/negocio, agente de contenido (competidores/noticias/guiones) y equipo de agentes con coordinador. Gráficos muestran una lista progresiva, estanterías para contexto, widgets y árbol coordinador/subagentes. No muestra la implementación funcionando.

«Top 1%», «biblioteca infinita», más rápido y hacerlo todo en un fin de semana son lenguaje promocional sin medición. La relación útil es entre contexto organizado, tareas claras y resultados consultables. Un agente de contenido necesita fuentes y revisión editorial; no basta generar más guiones mientras duerme.

Para Bryan: ya esta biblioteca cumple una parte del segundo cerebro, porque guarda fuentes, observaciones, límites y aplicaciones. Un panel futuro podría mostrar qué falta por revisar y qué lecciones se repiten. Eso es propuesta nuestra, no implementación del creador ni tarea delegada aquí.

Decisión: conservar como mapa de proyectos, no crear cinco herramientas por seguir la lista. Relacionar con las fichas de arquitectura de Jarvis para evitar duplicación.

---

### 34. Perplexity, Firecrawl y Playwright — lista promocional

ID: `DfGUcOwtl3D`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DfGUcOwtl3D/


Fuente: https://www.instagram.com/p/DfGUcOwtl3D/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

El autor presenta Perplexity para investigar, Firecrawl (ASR: firecloud) para extraer contenido de páginas y Playwright para automatizar/pruebas de navegador. Se ilustran con libros, pantallas, investigación, assets y checks de formulario/login. No hay instalación ni llamadas reales de cada conector demostradas.

La promesa «nunca alucina» no está probada por mostrar una herramienta de búsqueda. «Cualquier página» tampoco acredita acceso universal o permisos. Guardar el principio de trabajar con evidencia rastreable y verificar resultados; no la garantía comercial. Precio, cuotas, disponibilidad y configuración pendientes de fuente oficial.

Para tus proyectos encajan tres fases: investigar referencia, leer contenido y comprobar interacción del producto. No equivale a ver cada video ni sustituye la transcripción/inspección que estamos haciendo. No se copiarán assets por una invitación del reel.

Motion: personaje pixelado funciona como hilo conductor, objetos/luz marcan cada capacidad y rótulos resumen acciones. Se conserva como referencia de animación además de índice técnico. No se instalaron conectores durante esta revisión.

---

### 35. Treinta y un formatos de contenido

ID: `DeLeC4htYjZ`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DeLeC4htYjZ/


Fuente: https://www.instagram.com/p/DeLeC4htYjZ/ · descripción abierta · diez fotogramas y cuatro ampliaciones entre 20–23 s inspeccionados · audio procesado localmente · 31/10/2026.

El ASR recupera solo el cierre; el listado procede del texto visible. Se completaron los dos últimos puntos en una captura adicional, sin inventarlos.

Lista: hablar a cámara; tier list; pantalla verde; respuesta a comentario; story time; antes/después; falso podcast; día en la vida; reacción; POV; texto + b-roll; vlog; caminar hablando; entrevista en calle; voz en off; videollamada; análisis de video; pantalla dividida; opinión polémica; app de notas; compartir pantalla; papel y lápiz; cambio de escena; muro de texto; tablero en blanco; tweet en pantalla; yapping; carrusel de tweets; carrusel de IA; mensaje de texto; clon.

El video acumula una lista en dos columnas y muestra pequeños ejemplos encima del presentador, sobre fondo rojo. Son formatos de presentación, no treinta y un nichos ni garantía de crecer rápido. La precisión del problema y la calidad del contenido siguen sin demostrarse por el formato.

Para Bryan: un mismo tema puede probarse como antes/después, pantalla compartida o detalle con voz en off. Propuesta: enseñar el mismo arreglo de color de tres maneras y comparar comprensión y retención. Es ejercicio nuestro; el video no aporta resultados comparables.

Decisión: conservar como menú de formatos para plan de contenido. No adoptar «polémica» o «falso podcast» como obligación; escoger según propósito y autenticidad de la pieza.

---

### 36. Cuarenta encuadres y técnicas visuales

ID: `DeNyzN9o3rg`

Sección: Composición y cinematografía

Destino de integración sugerido: **profe-composicion-visual; profe-cinematografia**.

Fuente original: https://www.instagram.com/p/DeNyzN9o3rg/


Fuente: https://www.instagram.com/p/DeNyzN9o3rg/ · revisión 31/10/2026.

Descripción abierta: ofrece lista con ejemplos/sensaciones al comentar frames y menciona Eyecannndy, Frame Set y ShotDeck como referencias. Audio local transcrito, ocho fotogramas de la selección y una captura adicional a 36 s inspeccionados. La lista final completa es visible. No se inspeccionó cada ejemplo en movimiento ni se recibió el desglose externo; no se atribuyen al autor explicaciones emocionales que no dio en el reel.

#### Lista recuperada
1–9 escala/insertos: extreme wide, wide, full, cowboy, medium shot, medium close-up, close-up, extreme close-up, insert.
10–16 ángulo o punto de vista: eye level, high angle, low angle, Dutch tilt, overhead, over the shoulder, point of view.
17–27 cámara y movimiento: locked off, pan, tilt, handheld, tracking, push-in, pull-out, crane, Steadicam, whip pan, arc.
28–34 óptica/enfoque: wide lens, long lens, macro, shallow focus, deep focus, rack focus, dolly zoom.
35–40 sujetos/composición: single, two-shot, group shot, frame within the frame, negative space, symmetry.

#### Qué aprender de verdad
No son cuarenta reglas de tercios ni cuarenta tamaños de plano. La lista mezcla variables diferentes. Se pueden combinar: un two-shot, a nivel de ojos, con cámara fija y espacio negativo. Esa combinación es una explicación nuestra para convertir el glosario en decisiones de rodaje. Dolly zoom combina desplazamiento y cambio de focal; no debe confundirse con un zoom cualquiera. No se recuperan ajustes ni recetas de las películas mostradas.

#### Aplicación
Para planear un reel, elegir primero información/emoción y luego anotar escala, ángulo, movimiento y enfoque. Usar tres planos complementarios antes que acumular todos los recursos. Ejercicio propuesto: misma acción con plano abierto, detalle y plano medio; comparar qué información aporta cada uno. Es una práctica propia, no un ejercicio impuesto por el creador.

#### Diseño del reel
Lista numerada en dos columnas rodea al presentador, ejemplos audiovisuales superpuestos abajo. La acumulación visible comunica amplitud, pero el ritmo rápido reduce el tiempo para aprender cada técnica. Conservar como índice de consulta, no como curso completo de cada movimiento.

---

### 37. Festival Alaire — carrusel de tres láminas

ID: `DfF7IyRmUZ1`

Sección: Diseño gráfico y referencias

Destino de integración sugerido: **profe-diseno-grafico; profe-composicion-visual**.

Fuente original: https://www.instagram.com/p/DfF7IyRmUZ1/


Fuente: https://www.instagram.com/p/DfF7IyRmUZ1/ · descripción y tres láminas inspeccionadas directamente en Chrome · 31/10/2026.

La descripción anuncia a Cultura Profética y remite a entradas de etapa 1. Se trata aquí como referencia gráfica, no como recomendación de comprar entradas ni comprobación de la programación del evento.

#### Jerarquía y composición
Lámina 1: ALAIRE domina en mayúscula ancha sobre franja amarilla. Fecha/lugar en línea estrecha inferior. Foto recortada de cuatro músicos sobre naranja y banda inferior verde con nombre de artista en amarillo. Nubes, formas de paisaje y flores integran márgenes; textura de impresión/grano unifica fotografía y dibujo. El recorte del grupo se mantiene separado de la información principal.

Lámina 2: conserva cabecera pero cambia contraste a amarillo sobre cian; lista de artistas blanca sobre bloque verde. Tamaños y agrupaciones diferencian niveles del cartel. Flores en los laterales enmarcan la columna central; cierre amarillo introduce lema y llamada a entradas. Franja inferior pequeña reúne logos.

Lámina 3: fondo amarillo, marca roja arriba, dos columnas de colaboradores y separadores finos blancos. Nubes y trama de puntos ocupan el pie. Es lámina de créditos/aliados, no tabla de precios. Los blancos sobre amarillo tienen menos separación tonal que los títulos: al adaptar convendría comprobar legibilidad real en móvil.

#### Qué aprender y aplicar
Un sistema de carrusel puede mantener marca, paleta y textura mientras cambia la función de cada lámina: impacto/artista, información y créditos. El tamaño de letra responde a jerarquía; no a llenar todos los huecos. Los adornos se acumulan en los bordes y dejan libre el eje de lectura.

No se identificó la fuente tipográfica exacta, retícula matemática o medidas de márgenes del editable. No inventar valores en píxeles. Podemos estudiar estas relaciones sin copiar logos, fechas, artistas o composición completa para otra marca. Guardado como análisis de diseño; pertenencia a una carpeta personal de referencias fotográficas queda sin confirmar si Bryan quiere esa distinción.

---

### 38. Mismo listado de cinco plugins, otra ejecución visual

ID: `DfDsRgltMdz`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DfDsRgltMdz/


Fuente: https://www.instagram.com/p/DfDsRgltMdz/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

Repite sustancialmente De611nTxDnh: Playwright, OmniRoute, Headroom, palacio mental y Frontend Design. Se identifica como repetición de conocimiento, no prueba de paquete distinto. No se han verificado instaladores, versiones o precio en esta revisión.

Aporta una referencia de motion diferente: escenario pixel art Halloween, personaje recorriendo el espacio, antorchas, telarañas, frascos, portal y medidores de tokens/créditos. La ruta espacial transforma la lista en recorrido; las barras hacen visible una idea abstracta de consumo. La comparación de una web genérica con otra editorial ilustra dirección de diseño, sin medir calidad objetiva.

Aplicación para tu contenido: mantener voz/guion y cambiar metáfora visual puede crear una variante de presentación; evitar publicarlo como lección nueva si no añade información. Mantener las mismas reservas sobre cuotas, memoria y promesas que en la ficha vinculada.

Decisión: una sola lección técnica con dos referencias visuales. No confundir ilustración de crédito con lectura real de una cuenta.

---

### 39. Veinticuatro herramientas y referencias de filmmaking

ID: `DeDTYsrI_cl`

Sección: Composición y cinematografía

Destino de integración sugerido: **profe-composicion-visual; profe-cinematografia**.

Fuente original: https://www.instagram.com/p/DeDTYsrI_cl/


Fuente: https://www.instagram.com/p/DeDTYsrI_cl/ · descripción abierta · audio local y diez fotogramas inspeccionados · 31/10/2026.

Listado recuperado cruzando voz y texto: Frameset, Film Grab, Movie-screencaps, AdForum, Vimeo Staff Picks, Milanote, Coolors, Adobe Color, Khroma, Cinema Palettes, StudioBinder, Boords, Notion, SunCalc, Windy, what3words, WriterDuet, Celtx, Script Slug, DaVinci Resolve, Freesound, Uppbeat, Pexels y Unsplash. El ASR deforma varios nombres; el listado visible permite corregirlos. No se accedió a cada servicio ni se certifica licencia/plan.

Agrupación didáctica nuestra: referencias de cine/publicidad; organización/storyboards; paletas; localización/clima/sol; guion; edición; sonido y stock. El título «free commercial filmmaking tools» no significa que todas las funciones, descargas y usos sean gratuitos ni que toda imagen de una referencia pueda reutilizarse comercialmente.

Para tu biblioteca: guardar qué problema resuelve cada fuente, URL oficial al comprobarla y licencia/atribución del asset concreto. Usar una referencia para estudiar composición es distinto de obtener una licencia para incorporarla a un anuncio.

El reel vuelve a usar lista en dos columnas, presentador y capturas de producto superpuestas; útil como directorio, insuficiente como curso o comparativa de herramientas. Prioridad media para investigar fuentes por necesidad real, sin crear cuentas o contratar planes.

---

### 40. Roles y controles de preproducción

ID: `DfDpX2bo1P1`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-cinematografia y profe-negocio-creativo; una sola fuente compartida**.

Fuente original: https://www.instagram.com/p/DfDpX2bo1P1/


Fuente: https://www.instagram.com/p/DfDpX2bo1P1/ · revisión 31/10/2026.

#### Descripción
La descripción propone repartir tareas entre director, DOP y productor; una persona puede asumir los tres roles.

#### Evidencia y observaciones
Los fotogramas muestran tres etapas de preproducción: pitch, shotlist y recce. Director: idea, tratamiento, referencias, intención de escena, previsualización y planos indispensables. DOP: enfoque de luz, cámara y ópticas, movimiento por setup, plan de luz, recorrido del sol y pruebas de lentes. Productor: presupuesto, calendario, entregables, reservas, acceso, estacionamiento y permisos. El audio principalmente enumera roles y conduce al recurso; la información útil está en pantalla.

#### Aprendizaje para tu trabajo
Crear tres listas de control aunque trabajes solo: intención creativa, viabilidad técnica y recursos. Antes de grabar, identificar cinco planos indispensables y comprobar la locación real. No confundir estas tres etapas con producción y posproducción.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 41. Montaje urbano Hong Kong

ID: `DfF2WOyxZNa`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; profe-efectos-visuales; profe-motion-graphics**.

Fuente original: https://www.instagram.com/p/DfF2WOyxZNa/


Fuente: https://www.instagram.com/p/DfF2WOyxZNa/ · revisión 31/10/2026.

#### Descripción
Ofrece un pack de SFX mediante comentario SOUND; no se solicitó ni descargó ese recurso.

#### Evidencia y observaciones
Diez fotogramas muestran tipografía roja condensada, caracteres chinos, skyline, taxi con desenfoque lateral, calles nocturnas, retrato y tratamientos de grano, blanco y negro o negativo. La transcripción no detecta voz explicativa.

#### Aprendizaje para tu trabajo
Conservar como referencia de contraste entre ciudad y retrato, textos breves integrados a la imagen y cambios visuales de energía. El muestreo no demuestra sincronía musical exacta ni permite identificar los SFX del pack.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 42. Animación de palabras con Text+

ID: `DfDEPNBtWHO`

Sección: Motion y diseño de interfaces

Destino de integración sugerido: **profe-motion-graphics (principal); profe-editor-asistente (enlace)**.

Fuente original: https://www.instagram.com/p/DfDEPNBtWHO/


Fuente: https://www.instagram.com/p/DfDEPNBtWHO/ · revisión 31/10/2026.

#### Descripción
El autor afirma que basta un Text+ en Resolve y ofrece preset al comentar TEXT.

#### Evidencia y observaciones
La explicación en francés propone Follower, retraso entre elementos, transformación por palabra, Offset con XY Path y Anim Curves; se menciona una progresión entre 0 y 1 alrededor de 25 fotogramas. Los diez fotogramas muestran la interfaz de Resolve y texto con trayectoria curva. La transcripción pierde algunos términos y una expresión; no hay suficiente evidencia para escribirla completa.

#### Aprendizaje para tu trabajo
Separar el movimiento de cada palabra del movimiento del bloque usando modificadores. Guardar como procedimiento parcial para una prueba posterior en Resolve; no presentar una receta terminada ni un preset instalado.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 43. Del videojuego a una escena cinematográfica

ID: `DfDGkkVOycz`

Sección: Edición y VFX

Destino de integración sugerido: **profe-video-con-ia; profe-narrativa-y-direccion como referencia**.

Fuente original: https://www.instagram.com/p/DfDGkkVOycz/


Fuente: https://www.instagram.com/p/DfDGkkVOycz/ · revisión 31/10/2026.

#### Descripción
PAUSE THE GAME, IT’S THE FEDS; atribuye la creación a Higgsfield y ofrece breakdown mediante CULTURE.

#### Evidencia y observaciones
Diez imágenes muestran sofá y juego en CRT, transición a calle con motocicletas, acción urbana, barbería, automóvil y luces policiales lejanas. El reconocimiento de voz no recupera explicación técnica fiable.

#### Aprendizaje para tu trabajo
La idea útil es convertir una acción cotidiana en puerta de entrada a otro mundo, con continuidad de energía y ambientación. Es referencia narrativa y visual; no demuestra qué modelo, prompts o composición se usaron.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 44. Entrevista musical y conexión local

ID: `De9qn2EgDzW`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-narrativa-y-direccion; profe-editor-asistente**.

Fuente original: https://www.instagram.com/p/De9qn2EgDzW/


Fuente: https://www.instagram.com/p/De9qn2EgDzW/ · revisión 31/10/2026.

#### Descripción
Entrevista de Wao 97.3 con Cultura Profética en Panamá; aparecen marcas Magic Dreams y Jogo.

#### Evidencia y observaciones
La transcripción recorre actualidad musical, escritura desde experiencias y emociones, conexión con Panamá y permanencia de la música. Algunos nombres propios son dudosos. Diez fotogramas muestran planos cercanos de entrevista con fondo de marca azul, micrófono y B-roll de concierto sobre las respuestas.

#### Aprendizaje para tu trabajo
Para entrevistas de Jogo: comenzar por el presente del artista, pasar a emoción y proceso, conectar con el público local y cerrar con significado. Cubrir cortes con B-roll relacionado. Los nombres y datos históricos no quedan verificados por la transcripción.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 45. Carrusel de contenido corto a largo

ID: `DfDJWNjCMmk`

Sección: Negocio creativo y marketing

Destino de integración sugerido: **profe-negocio-creativo; profe-narrativa-y-direccion para estructura de entrevistas y guion**.

Fuente original: https://www.instagram.com/p/DfDJWNjCMmk/


Fuente: https://www.instagram.com/p/DfDJWNjCMmk/ · revisión 31/10/2026.

#### Descripción
Invita a comentar EMBUDO; propone conectar Reels con videos horizontales largos y aclara que la función no estaría disponible en todas las regiones.

#### Evidencia y observaciones
Se inspeccionaron las once láminas. Alterna azul texturado y amarillo, titulares grandes condensados, conectores manuscritos blancos, flechas y diagramas simples. La portada ancla el texto con una persona sobre un coche. El relato avanza de noticia a problema, botón, recorrido del espectador y CTA.

#### Aprendizaje para tu trabajo
Conectar una pieza de descubrimiento con otra que explique a fondo es una estrategia útil. La disponibilidad de videos de hasta 90 minutos y del botón en tu cuenta no se comprobó: no tratar las afirmaciones del carrusel como lanzamiento universal. Como diseño, alternar fondos puede marcar capítulos sin cambiar de identidad.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 46. Cuatro recursos para interfaces y desarrollo

ID: `DeHGy2DlRRg`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/DeHGy2DlRRg/


Fuente: https://www.instagram.com/p/DeHGy2DlRRg/ · revisión 31/10/2026.

#### Descripción
Pide comentar vibe e identifica patrocinio manuspartner y ad.

#### Evidencia y observaciones
Los diez fotogramas presentan Anime.js, Manus.im, Motion sites y blog.vibecoder.me. Atribuye animación web a Anime.js, construcción de apps y backend a Manus, fondos en loop a Motion sites y aprendizaje o plantillas al blog. La pista reconocida corresponde a música, no a un tutorial hablado.

#### Aprendizaje para tu trabajo
Separar biblioteca de animación, agente de desarrollo, banco de recursos y material formativo: resuelven necesidades distintas. Conservar nombres como candidatos; no se verificaron sus precios, licencias ni las promesas del anuncio, y no se instalaron.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 47. Ajustes de exportación para Instagram

ID: `DenmuIbkYm0`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; profe-efectos-visuales; profe-motion-graphics**.

Fuente original: https://www.instagram.com/p/DenmuIbkYm0/


Fuente: https://www.instagram.com/p/DenmuIbkYm0/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Carrusel de siete láminas inspeccionadas, descripción abierta. Propone MP4 H.264, 1080×1920, 12000 Kb/s, redimensionamiento e interpolación con máxima calidad y subida con calidad más alta en Instagram. No hay video hablado que transcribir.

#### Aprendizaje y decisión
Distinguir contenedor MP4, códec H.264, dimensiones y bitrate. 12000 Kb/s son 12 Mb/s, no 12 MB/s. Es una receta del autor, no garantía de ausencia de compresión. La conveniencia de 4K depende de la entrega; las casillas de máxima calidad no recuperan detalle inexistente. No se cambiaron ajustes de tu cuenta ni de tus proyectos. Diseño: fondos rojo/naranja desenfocados, palabras amarillas enormes y capturas de controles resaltadas con contorno amarillo.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 48. Entender el número f

ID: `De_XwAxRUvg`

Sección: Composición y cinematografía

Destino de integración sugerido: **profe-cinematografia**.

Fuente original: https://www.instagram.com/p/De_XwAxRUvg/


Fuente: https://www.instagram.com/p/De_XwAxRUvg/ · revisión 31/10/2026.

#### Descripción
Explica el número f como distancia focal dividida por diámetro de apertura, con ejemplo de 50 mm.

#### Evidencia y observaciones
Transcripción coherente e imágenes de aperturas, fórmula y bokeh: 50/1.8≈27.8 mm y 50/16≈3.1 mm. La relación de áreas es (16/1.8)^2≈79, equivalente a unas 6.3 paradas.

#### Aprendizaje para tu trabajo
Un número f mayor reduce la luz y suele ampliar profundidad de campo, pero no implica siempre mayor nitidez: también intervienen enfoque, distancia y difracción. El diámetro óptico relevante es el de la pupila de entrada. Usar la relación para comprender exposición, sin copiar ajustes para todas las escenas.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 49. Aprobar storyboard antes de animar con IA

ID: `Det7Ic-oeHB`

Sección: IA y automatización

Destino de integración sugerido: **profe-editor-asistente; mukiwa-ui-plugins para la interfaz**.

Fuente original: https://www.instagram.com/p/Det7Ic-oeHB/


Fuente: https://www.instagram.com/p/Det7Ic-oeHB/ · revisión 31/10/2026.

#### Descripción
Invita a comentar CLAUDE para un taller y destaca el workflow frente a la herramienta.

#### Evidencia y observaciones
Diez fotogramas muestran un panel con tarjetas emparejadas STORYBOARD y ANIMATION, botones Approve y Change, notas de revisión, un automóvil que despega y la frase Could edit videos directly with Claude. La transcripción solo recupera una despedida; no explica implementación.

#### Aprendizaje para tu trabajo
La lección aplicable es aprobar intención y composición por plano antes de generar animación, y registrar cambios por tarjeta. Una interfaz y una demostración no prueban integración con Premiere ni edición editable, gratuita o instalada.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 50. Entregar instrucciones de edición en un ZIP

ID: `De25A0jANdz`

Sección: IA y automatización

Destino de integración sugerido: **profe-editor-asistente; instrucciones y recursos reutilizables**.

Fuente original: https://www.instagram.com/p/De25A0jANdz/


Fuente: https://www.instagram.com/p/De25A0jANdz/ · revisión 31/10/2026.

#### Descripción
Cómo editar con Claude; remite al video completo de Diego Cabrera 22.

#### Evidencia y observaciones
Ocho fotogramas muestran una web Edita tus videos con Claude, selección de estilos, un ZIP arrastrado al chat y un prompt copiado. La voz explica que el paquete reúne instrucciones, estilos y materiales; el nombre exacto del kit no se recupera con suficiente seguridad.

#### Aprendizaje para tu trabajo
Un paquete de instrucciones y recursos puede reducir la repetición de encargos. Adjuntar un ZIP no entrena los pesos del modelo ni garantiza memoria entre sesiones. Falta comprobar el resultado final, archivos editables, derechos de los recursos y coste de los servicios que use.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 51. Selector de estilos para contenido vertical

ID: `Deqg7kFgeRe`

Sección: IA y automatización

Destino de integración sugerido: **profe-editor-asistente; mukiwa-ui-plugins**.

Fuente original: https://www.instagram.com/p/Deqg7kFgeRe/


Fuente: https://www.instagram.com/p/Deqg7kFgeRe/ · revisión 31/10/2026.

#### Descripción
Another day another Claude build; etiquetas de contenido, B-roll y estrategia.

#### Evidencia y observaciones
Ocho fotogramas muestran el mismo video de una persona presentado en tarjetas con diferentes tipografías, títulos, captions, colores y tarjetas amarillas. Se ven etapas como Titles, Captions, Colors y B-roll. No se detecta narración explicativa.

#### Aprendizaje para tu trabajo
Para tus subtítulos, un selector con vista previa sobre el clip real ayuda a elegir una familia visual antes de exportar. El video enseña una interfaz; no demuestra precisión de transcripción, animación por palabra, formato editable ni integración con tu editor.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 52. Cinco plugins y sus promesas

ID: `De-o9pyjQks`

Sección: IA y automatización

Destino de integración sugerido: **claude-automation-recommender; makin-plugin; task-observer solo si corresponde a su función**.

Fuente original: https://www.instagram.com/p/De-o9pyjQks/


Fuente: https://www.instagram.com/p/De-o9pyjQks/ · revisión 31/10/2026.

#### Descripción
Ofrece enlaces por DM al comentar PLUGINS.

#### Evidencia y observaciones
Nueve fotogramas y transcripción identifican OmniRoute, Claude-Mem, Headroom, Claude Code Setup y Task Observer. Usa una tabla dibujada que revela elementos progresivamente y diagramas para representar proveedores, memoria y compresión. Afirma uso casi ilimitado, recuerdo completo y mismo resultado con menos tokens, sin mediciones.

#### Aprendizaje para tu trabajo
Ruteo, memoria, compresión, configuración y observación son funciones distintas. El software libre no vuelve gratuitos a todos sus proveedores ni elimina cuotas; la memoria requiere control de lo guardado y la compresión debe medirse por calidad. Conservar como referencia, enlazar con publicaciones similares y no reinstalar ni cambiar configuraciones durante esta revisión.

#### Alcance
Análisis mediante descripción abierta en Chrome, transcripción local cuando hay voz y fotogramas seleccionados; no es escucha humana ni inspección continua de cada fotograma. No se enviaron comentarios ni se realizaron compras.

---

### 53. Archivar medios usados con margen

ID: `De82N99A-a8`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente**.

Fuente original: https://www.instagram.com/p/De82N99A-a8/


Fuente: https://www.instagram.com/p/De82N99A-a8/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción, transcripción y diez fotogramas coinciden: File → Media Management → Timelines → Copy → Used media and trim keeping frame handles. La interfaz muestra 50 frames en el ejemplo; el autor ilustra un archivo que pasó de 166 a 21 GB y pide guardar el proyecto y probar el archivo antes de eliminar originales.

#### Aprendizaje y decisión
Los handles conservan material antes y después del corte para revisiones; su duración depende de los fps: 50 frames no son siempre el mismo número de segundos. Seleccionar todas las timelines que deben sobrevivir y comprobar relink, audio y efectos antes de considerar limpieza. El porcentaje de ahorro es del ejemplo, no una promesa. No se borró ni consolidó ningún proyecto del usuario.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 54. Sony ajustes de grabación y S-Log3

ID: `DeMWZ_aDlMx`

Sección: Color grading, máscaras, balance de blanco y LUTs

Destino de integración sugerido: **Buscar skill de color ya existente en Claude; si no existe, proponer una única skill conjunta**.

Fuente original: https://www.instagram.com/p/DeMWZ_aDlMx/


Fuente: https://www.instagram.com/p/DeMWZ_aDlMx/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Cinco láminas inspeccionadas y descripción abierta. Promueve XAVC HS 4K, 50p, 100 Mbps, 4:2:2 10-bit, S-Log3 y PP8, más Save/Load Settings. Instagram identifica contenido generado con IA. No es demostración real del menú de tu cámara.

#### Aprendizaje y decisión
Conservar como punto de partida para investigar el modelo concreto, no como configuración universal de máxima calidad. Codec, muestreo, fps y perfil son decisiones distintas. La compatibilidad de esta combinación no está verificada para tu equipo; S-Log3 requiere exposición y gestión de color apropiadas. No atribuir menor tamaño al solo hecho de usar 10 bits. Diseño de referencia: cámara grande al centro, fondo cálido y jerarquía tipográfica amarilla/blanca.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 55. Catálogo web de sneakers

ID: `DfAqpTsOHYn`

Sección: Motion y diseño de interfaces

Destino de integración sugerido: **profe-motion-graphics; profe-diseno-grafico; mukiwa-ui-plugins**.

Fuente original: https://www.instagram.com/p/DfAqpTsOHYn/


Fuente: https://www.instagram.com/p/DfAqpTsOHYn/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción de diseño web para marca de zapatillas; no narración detectada. Seis fotogramas muestran una parrilla de productos que cambia a una ficha con una zapatilla protagonista, nombre, controles y una representación de móvil al frente. Fondo oscuro neutro y base naranja luminosa.

#### Aprendizaje y decisión
La misma identidad debe sobrevivir a catálogo y detalle: consistencia de fondo, escala del producto y navegación. Para tus interfaces de assets, aprovechar miniaturas comparables y una vista previa grande. Es una referencia visual; no se midieron rendimiento, accesibilidad ni comportamiento responsive real.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 56. Comparación de edición automática con Claude

ID: `DfAomLvu2ey`

Sección: IA y automatización

Destino de integración sugerido: **profe-editor-asistente; candidato de herramienta sin validar**.

Fuente original: https://www.instagram.com/p/DfAomLvu2ey/


Fuente: https://www.instagram.com/p/DfAomLvu2ey/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción ofrece herramienta al comentar Edición. Transcripción afirma zooms, SFX, títulos, subtítulos, eliminación de silencios y muletillas. Diez fotogramas muestran comparación ORIGINAL/EDITADO POR CLAUDE, cambios de escala, rótulos y un archivo de video en chat.

#### Aprendizaje y decisión
La comparación sirve como lista de requisitos para automatizar tus reels: detectar pausas, proponer cortes, mantener sentido, subtitular y controlar estilos. No demuestra precisión general, eliminación segura de todos los errores, archivos editables ni integración en Premiere. Validar un fragmento con voz real y revisar cortes antes de procesar todo; no se obtuvo el recurso por DM.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 57. Music Video Essentials y VFX HUB

ID: `DfBAOi7xUy_`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; profe-efectos-visuales; profe-motion-graphics**.

Fuente original: https://www.instagram.com/p/DfBAOi7xUy_/


Fuente: https://www.instagram.com/p/DfBAOi7xUy_/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción abierta y diez fotogramas, sin voz detectada. Muestra aplicar efecto pre/post, Clean Twitch Shake, controles en Inspector, curva con cuatro presets, brillo para flash y efectos apilados. La descripción distingue VFX HUB, que requiere Resolve Studio, de efectos que podrían usarse desde Power Bins o panel de efectos.

#### Aprendizaje y decisión
Lo útil para tu biblioteca es previsualizar, buscar y ajustar intensidad y curva sin salir del editor. La adaptación a duración del clip es una promesa del creador, no una prueba nuestra en Resolve. Precio, licencia y compatibilidad no verificados; no se descargó ni instaló. No clasificarlo como gratis por aparecer en un reel.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 58. Quince relaciones de aspecto

ID: `DfBJ6q6IIQA`

Sección: Composición y cinematografía

Destino de integración sugerido: **profe-composicion-visual**.

Fuente original: https://www.instagram.com/p/DfBJ6q6IIQA/


Fuente: https://www.instagram.com/p/DfBJ6q6IIQA/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción, audio y diez fotogramas muestran una tabla: 9:16, 4:5, 1:1, 16:9, 2:1, 4:3, 1.85:1, 2.39:1, 5:3, 2.35:1, 1.43:1, 2.76:1, 2.20:1, 2.55:1 y 1.19:1. Ejemplos visuales cambian el rectángulo sobre la imagen. Ofrece hoja al comentar ratio; no se pidió.

#### Aprendizaje y decisión
Elegir el encuadre según destino y composición, después calcular ancho/alto. La fila 2:1 muestra 1920×960 y 3840×1920: ambas dimensiones corresponden a esa proporción. En las otras filas no se deben copiar números sin lectura ampliada. Para 4:5, 864×1080 y 1728×2160 son proporciones correctas aunque no las únicas dimensiones posibles. 1080p y 4K no fijan por sí solos todas estas dimensiones. Los nombres históricos son simplificaciones del autor.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 59. Mostrar el proceso para construir portfolio

ID: `De-1NxJBQme`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; profe-efectos-visuales; profe-motion-graphics**.

Fuente original: https://www.instagram.com/p/De-1NxJBQme/


Fuente: https://www.instagram.com/p/De-1NxJBQme/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción de día uno mostrando trabajo hasta conseguir contratación. Diez fotogramas alternan Photoshop/After Effects con el resultado: amigos sentados, arquitectura, plano desde vehículo, comida y pantalla dividida. No voz detectada.

#### Aprendizaje y decisión
El proceso puede funcionar como prueba de capacidad junto al resultado, pero el espectador necesita entender qué cambió. Conservar como referencia de presentación de antes/después, encuadres cotidianos y reutilización de material propio. No se ha probado el mecanismo exacto de cada transición ni la eficacia comercial de la serie.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 60. Rig modular Sigma FP

ID: `DfBAjDSBxMc`

Sección: Gadgets y equipo

Destino de integración sugerido: **Referencia de equipo; profe-cinematografia solo para criterios aplicables**.

Fuente original: https://www.instagram.com/p/DfBAjDSBxMc/


Fuente: https://www.instagram.com/p/DfBAjDSBxMc/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción atribuye a la FP original salida RAW CDNG de 12 bits a SSD y presenta un rig estilo Super 8. Diez fotogramas sin voz muestran empuñadura inferior, óptica, monitor y SSD o módulo lateral, con cambios de orientación. También menciona una FP II; esa noticia no se verificó.

#### Aprendizaje y decisión
Guardar como inspiración de ergonomía y compra futura. Antes de comprar hay que comprobar formato de grabación, soporte de datos, alimentación, montaje vertical y peso del conjunto, no solo el cuerpo. No se certificaron especificaciones ni se identificaron todos los accesorios. No hay compra ni recomendación de precio.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 61. PowerGrade con aspecto Kodak Gold

ID: `DfAyGDMSgdT`

Sección: Color grading, máscaras, balance de blanco y LUTs

Destino de integración sugerido: **Buscar skill de color ya existente en Claude; si no existe, proponer una única skill conjunta**.

Fuente original: https://www.instagram.com/p/DfAyGDMSgdT/


Fuente: https://www.instagram.com/p/DfAyGDMSgdT/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción ofrece PowerGrade para Resolve mediante comentario Kodak; menciona Sony, Canon, Apple y Lumix. Diez fotogramas sin voz muestran Gallery con variantes, nodos y antes/después Log vs Kodak Gold; la pantalla agrega DJI.

#### Aprendizaje y decisión
Un PowerGrade puede transportar estructura de nodos, distinta de una simple LUT. Debe corresponder al espacio de entrada, exposición y balance de blanco antes de juzgar el look. El antes/después Log frente a imagen terminada mezcla normalización y estilo, por lo que no demuestra emulación exacta de película. No se obtuvo el archivo ni se comprobó coste o compatibilidad.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 62. Guardar el cordón de unas Salomon

ID: `DezW2rNh5fB`

Sección: Moda y cuidado de prendas

Destino de integración sugerido: **Archivo de referencia personal**.

Fuente original: https://www.instagram.com/p/DezW2rNh5fB/


Fuente: https://www.instagram.com/p/DezW2rNh5fB/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción anuncia un truco de uso para zapatillas Salomon. Diez fotogramas muestran ajuste del cordón rápido y recogida del excedente hacia el bolsillo de la lengüeta. La transcripción recoge música/rap y no una explicación fiable; no se conserva como instrucción verbal.

#### Aprendizaje y decisión
La utilidad práctica está en recoger el cordón para evitar que quede colgando, comprobando el diseño concreto del calzado. No es una técnica de barbería ni entrenamiento. Referencia visual secundaria: primer plano fijo de manos y producto, fondo mínimo y texto breve arriba.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 63. Hook de un comentario que se quema

ID: `DfAEetmoMHf`

Sección: Edición y VFX

Destino de integración sugerido: **profe-video-con-ia; profe-efectos-visuales**.

Fuente original: https://www.instagram.com/p/DfAEetmoMHf/


Fuente: https://www.instagram.com/p/DfAEetmoMHf/ · revisión 31/10/2026.

#### Qué dice y qué muestra
Descripción patrocinada ArtlistPartner y transcripción: grabar gesto de quemar, capturar comentario, subir video e imagen a Artlist, indicar efecto y generar; el autor nombra Kling 4.0. Diez fotogramas muestran tarjeta de comentario con fuego y campos de referencia, duración y resolución. El prompt completo no se recupera con seguridad.

#### Aprendizaje y decisión
La técnica narrativa une el gesto del actor con una transformación de un elemento gráfico. Preparar actuación y posición del comentario antes del efecto. La pantalla muestra coste de generación: no es un flujo demostrado gratuito. No se generó ni subió material del usuario. La disponibilidad o identidad exacta del modelo nombrado queda sin verificar; como alternativa conceptual futura puede estudiarse composición local con fuego autorizado y máscaras.

#### Alcance
Descripción leída en Chrome; imágenes estáticas o fotogramas seleccionados inspeccionados y transcripción local cuando existe voz. No equivale a escucha humana ni a reproducción continua. No se enviaron comentarios ni se hicieron compras.

---

### 64. Personaje 3D y humor de prioridades

ID: `De-hWOZhYcm`

Sección: Ilustración y referencias

Destino de integración sugerido: **Referencia de personaje estilizado 3D; no añadir a retrocartoon**.

Fuente original: https://www.instagram.com/p/De-hWOZhYcm/


Fuente: https://www.instagram.com/p/De-hWOZhYcm/ · revisión 31/10/2026.

#### Evidencia observada
Descripción breve con Magnific y seedance25; la transcripción presenta a un personaje sin dinero ni batería que presume su ropa. Ocho imágenes muestran un personaje estilizado 3D, rostro angular, cuello muy largo, camiseta blanca grande y loft cálido con ventana y escalera. Se alternan primer plano, plano medio y detalles de móvil y billetes.

#### Lección y aplicación
El humor nace de la contradicción entre problema y prioridad; los insertos hacen visibles los objetos mencionados. Conservar como actuación y diseño estilizado 3D. No es dibujo retrocartoon ni evidencia de técnica rubber hose; no incorporar automáticamente a esa skill. La descripción no demuestra qué parte realizó cada modelo.

#### Límites
Descripción visible en Chrome, transcripción local y todas las imágenes seleccionadas del reporte inspeccionadas. Muestreo visual, no escucha humana ni revisión continua. No se instaló ni compró nada.

---

### 65. Montaje vertical de una FX3

ID: `De6K8eziOlu`

Sección: Gadgets y equipo

Destino de integración sugerido: **Referencia de equipo; profe-cinematografia solo para criterios aplicables**.

Fuente original: https://www.instagram.com/p/De6K8eziOlu/


Fuente: https://www.instagram.com/p/De6K8eziOlu/ · revisión 31/10/2026.

#### Evidencia observada
No aparece descripción explicativa en h1. Nueve imágenes y texto FX3 vertical rig muestran piezas ordenadas sobre mesa, montaje de cuerpo y óptica, estructura, monitor, batería SmallRig 99, cable y modificador o filtro Tiffen. No se detectó voz.

#### Lección y aplicación
Útil para estudiar acceso a pantalla, distribución de peso, alimentación y orientación al trabajar vertical. No hay lista completa de accesorios o compatibilidades, ni se puede deducir seguridad de montaje del reel. Conservar como referencia de equipo y de video de ensamblaje; no comprar componentes a partir de nombres parcialmente visibles.

#### Límites
Descripción visible en Chrome, transcripción local y todas las imágenes seleccionadas del reporte inspeccionadas. Muestreo visual, no escucha humana ni revisión continua. No se instaló ni compró nada.

---

### 66. Montaje de concierto Wireless y Drake

ID: `De9b8vEOgil`

Sección: Edición y VFX

Destino de integración sugerido: **profe-editor-asistente; referencia de conciertos para Jogo**.

Fuente original: https://www.instagram.com/p/De9b8vEOgil/


Fuente: https://www.instagram.com/p/De9b8vEOgil/ · revisión 31/10/2026.

#### Evidencia observada
Descripción afirma edición en dos horas para Wirelessfest 2025. Diez fotogramas seleccionados muestran primeros planos del artista, escenario completo, público, llamas, barrido y destello desenfocado. La transcripción solo recupera una frase aislada sin explicación técnica.

#### Lección y aplicación
Construir cobertura de concierto con tres escalas: emoción del artista, dimensión del escenario y reacción del público. Barridos y destellos pueden servir de puntuación entre planos. No se certifica ritmo exacto con la música ni tiempo real de trabajo; dos horas es afirmación del autor, no rendimiento medido. Referencia útil para Jogo.

#### Límites
Descripción visible en Chrome, transcripción local y todas las imágenes seleccionadas del reporte inspeccionadas. Muestreo visual, no escucha humana ni revisión continua. No se instaló ni compró nada.

---

### 67. Túnel infinito con planos 3D en Fusion

ID: `De9T7TEKDcU`

Sección: Edición y VFX

Destino de integración sugerido: **profe-efectos-visuales (principal); profe-editor-asistente (enlace)**.

Fuente original: https://www.instagram.com/p/De9T7TEKDcU/


Fuente: https://www.instagram.com/p/De9T7TEKDcU/ · revisión 31/10/2026.

#### Evidencia observada
Descripción completa de ocho pasos y nueve fotogramas. Se ve una habitación con cuadro convertido en portal verde, eliminación de verde, transparencia y escena 3D con planos separados. No se detectó voz. La descripción indica trípode fijo, enfoque manual, espacio alrededor del sujeto y portal iluminado; Delta Keyer y Rectangle Mask; clips de igual duración; Image Plane 3D → Merge 3D → Renderer 3D → MediaOut, con Camera 3D conectada al Merge; capas sucesivas en Z 0, −1, −2, −3; animación de cámara, Spline y Render Cache.

#### Lección y aplicación
El keyer crea transparencia; la máscara delimita la región, evitando afectar otros verdes. Image Plane 3D convierte cada imagen plana en superficie espacial; Merge 3D reúne esas superficies con la cámara y Renderer 3D vuelve a producir una imagen 2D. Mover la cámara entre capas da la ilusión de entrar en mundos repetidos. Los valores Z son ejemplos y requieren ajustar escala, encuadre y recorrido para que los portales se alineen. Render Cache mejora reproducción, no sustituye el render. Procedimiento del creador contrastado visualmente, pendiente de construir y probar en tu Resolve.

#### Límites
Descripción visible en Chrome, transcripción local y todas las imágenes seleccionadas del reporte inspeccionadas. Muestreo visual, no escucha humana ni revisión continua. No se instaló ni compró nada.

---

## Ubicación de archivos de esta revisión

- Análisis: `/Volumes/MUKIWA 2TB/LOS PERGAMINOS/ANÁLISIS GUARDADOS INSTAGRAM/REVISIÓN 2026-10-31/`
- Videos: `/Volumes/VYBZ 1TB/Análisis de guardados de Instagram/REVISIÓN 2026-10-31/Videos/`
- Nombres de videos: `ID.mp4`, usando los IDs de cada ficha. Las copias de las 67 fichas y los 63 videos se verificaron por SHA-256 en la revisión.
- Pendientes: `PENDIENTES-VISIBLES.json` guarda 17 enlaces posteriores todavía no analizados. No sumarlos a las 67 fichas. No se conoce aún el total de guardados.
