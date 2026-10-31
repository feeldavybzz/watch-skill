# Evaluar edición y subtítulos automáticos con Claude antes de adoptar una herramienta
> Una lista de criterios para probar con un clip real cualquier flujo de «Claude edita tu video», separando lo que se muestra de lo que se demuestra.

- **Fuentes**: https://www.instagram.com/p/DfAomLvu2ey/ · /Det7Ic-oeHB/ · /De25A0jANdz/ · /Deqg7kFgeRe/ · /DfDe25xqLGM/ · /Deb92wnISDm/ · /DfGHAUsOgSt/ · /DfBAOi7xUy_/ (reels y demos de varios creadores)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local cuando hay voz (varios reels sin voz o con música); descripción abierta; fotogramas muestreados
- **Confianza**: media en los criterios (síntesis nuestra); baja en las promesas de cada herramienta (no se probó ninguna)

## Teoría (lo que se dijo)
- DfAomLvu2ey: Claude añade zooms, SFX, títulos, subtítulos y quita silencios y muletillas (comparación ORIGINAL / EDITADO POR CLAUDE).
- Deqg7kFgeRe: selector de estilos con vista previa sobre el mismo clip (Titles, Captions, Colors, B-roll).
- De25A0jANdz: un ZIP de instrucciones, estilos y materiales se arrastra al chat con un prompt.
- Det7Ic-oeHB: tarjetas STORYBOARD / ANIMATION con Approve y Change antes de animar (ya hay una nota previa en `references/instagram-2026-10-30/revision-por-planos-claude.md`).
- Deb92wnISDm: generar motion directamente en una timeline editable (InVideo) en vez de regenerar por prompt; SFX propios que Claude coloca.
- DfDe25xqLGM: cinco proyectos: Ghost Editor (elegir tomas), FFmpeg Skill (afirma 42 herramientas, local), Higgsfield Editorial Motion Graphics, Claude Shorts, OpenMontage.
- DfGHAUsOgSt: panel que reúne estadísticas, planificación, carruseles y reels (lista de espera).
- DfBAOi7xUy_: efectos pre/post (p. ej. Clean Twitch Shake) con curva y brillo desde el Inspector; **VFX HUB exige Resolve Studio**.

## Práctica (lo que se ve)
- Interfaces, comparaciones y resultados promocionales. No se ven proyectos nativos de Premiere, tiempos de render, correcciones ni archivos editables finales.

## Cruce teoría ↔ práctica
- Se muestra el **resultado** o la **interfaz**, no el proceso reproducible. No está demostrado que los cuatro reels (DfAomLvu2ey, Det7Ic-oeHB, De25A0jANdz, Deqg7kFgeRe) sean el mismo producto ni que sean gratuitos.
- «Open source» no vuelve gratuita toda la cadena (modelos, proveedores, cuotas).

## Receta paso a paso (lista de evaluación, propuesta nuestra)
1. Define **una salida concreta** (p. ej. quitar pausas de un reel de 30 s y subtitularlo) y pruébala con **tu propio clip**, con voz en español.
2. Revisa: transcripción en español, corrección de nombres propios, edición por palabra, estilos reutilizables, vista previa sobre el clip real, color por palabra, tipografías y animación editable.
3. Comprueba que el **significado se conserva al cortar** (no solo que desaparezcan las pausas). Revisa cada corte a mano.
4. Exige **formato editable**: si una frase, un color o un fondo queda mal, debes poder corregirlo sin rehacer el video (criterio de Deb92wnISDm).
5. Aprueba una **muestra** antes del lote. Aprobar intención y composición por plano antes de generar animación (Det7Ic-oeHB) evita rehacer.
6. Verifica el retorno a tu editor (Premiere o Resolve): que lo entregado se pueda abrir y seguir editando.
7. Anota coste, licencia y consumo de créditos **desde la fuente oficial** antes de recomendarla.

## Para MUKIWA
- Visual Edits: Bryan quiere subtítulos animados y corregibles, colores consistentes y assets accesibles dentro del editor. Esta lista es el filtro para decidir qué probar primero.
- Prioridad alta de investigación: DfDe25xqLGM y DfAomLvu2ey. **No se instaló ni se probó nada**, no se comentó, no se pidió ningún recurso por DM y no se consumieron créditos.

## Límites
- Un ZIP adjunto no entrena al modelo ni asegura memoria entre sesiones.
- Una demo con Claude no demuestra integración con Premiere.
- VFX HUB: precio y compatibilidad sin verificar; no clasificar como gratis.
- Enlaces de repositorios vistos en pantalla (p. ej. kajisho5/ffmpeg-skill, AgriciDaniel/claude-shorts, calesthio/OpenMontage) **no están auditados**: son candidatos.

## Conecta con
- [[archivar-medios-usados-con-margen-resolve]] · [[arquitectura-de-asistentes-con-agentes]] · [[plugins-para-claude-code-promesas-y-verificacion]]
