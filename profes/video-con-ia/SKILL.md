---
name: profe-video-con-ia
description: Profesor MUKIWA de dirección de video con IA (anuncios y escenas hechas con modelos como Seedance, Seedream y Soul Cinema dentro de Higgsfield, con Claude escribiendo los prompts), que aprende de las referencias que Bryan envía. Sabe fijar personajes y locaciones como referencias, escribir un prompt cronometrado por planos con lente, enfoque, sonido y continuidad, y arreglar fallos con un plano general como fotograma clave, anclas de fondo y mapas de blocking; también transiciones con corte oculto. Usar cuando Bryan pida dirigir o promptear un video o anuncio con IA, hacer personajes consistentes, hojas de personaje, locaciones de referencia, prompt por planos con tiempos, Seedance, Higgsfield, mapa de blocking para IA, o pregunte cómo se hace algo de video con IA.
metadata:
  nicho: video-con-ia
  herramientas: "Higgsfield Cinema Studio, Seedance, Seedream, Claude"
  lecciones: 1
  actualizado: "2026-10-11"
---

# Profe: Dirección de video con IA
> Dirige un anuncio o escena con modelos de imagen y video como si fuera un rodaje: fija personajes y locaciones como referencias con nombre, escribe un prompt cronometrado por planos (lente, enfoque, quién está dónde, sonido, continuidad) y arregla los fallos con un plano general como fotograma clave, anclas de fondo por ángulo y mapas de blocking. Todo lo aprendido viene de una demo en Higgsfield (créditos, Seedance 2.5): el método dura, los modelos y precios cambian. Falta aprender los prompts completos, el montaje final y otros modelos.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Para el blocking y la narrativa, combínalo con `profe-narrativa-y-direccion`; para ángulos, soportes y planos, con `profe-cinematografia`; para el montaje, con `profe-editor-asistente`.

## Cómo trabajar (de la idea al anuncio)
1. **Crea un proyecto y carpetas por activo** (personajes, locaciones, props, cada escena): con cientos de generaciones lo agradecerás [1].
2. **Fija el elenco antes de las escenas**: hoja de personaje por cada uno, guardada como elemento con nombre [1].
3. **Fija las locaciones con imágenes de referencia** (luz, disposición, fondo) antes de generar video [1].
4. **Escribe el prompt de video por planos con tiempos** (ver «Anatomía del prompt») y adjunta las referencias con **los mismos nombres** que uses en el texto [1].
5. **Genera, revisa y arregla** un fallo por vez; antes de culpar al modelo, revisa si el prompt lo dijo [1].
6. **Elige los mejores momentos de cada toma**; no hace falta usar todos los planos (el plano general de apoyo se deja fuera) [1].

## Áreas
### Personajes consistentes
- Pide a **Claude** un **prompt de hoja de personaje**: retrato + atuendo **de frente y de espalda**, sobre **fondo gris liso** (sin ruido visual, más utilizable) [1].
- Genera **muchas opciones baratas** (en Soul Cinema, ocho imágenes por un crédito) y elige; arregla detalles (piel muy lisa, luz dura, pecas) con un **modelo de edición** (Seedream 5.0 Pro) y un prompt de edición que escribe Claude [1].
- Deja **un solo rostro** para el video: los demás paneles **recortados del cuello hacia abajo** (solo ropa y proporciones) [1].
- Guarda como **elemento con nombre** (`char_mika`) y adjúntalo en cada escena [1].
- Todas las capas del atuendo deben aparecer (la sudadera con el gorro debajo) [1].

### Locaciones con referencias
- Como en un rodaje, **fija luz, distribución y fondo** antes de generar [1].
- Usa **siempre ángulo de tres cuartos**: da profundidad a la que el movimiento de cámara pueda «agarrarse» y rinde mejor que un plano frontal plano [1].
- Mezcla luz cálida interior con azul de la hora azul; una cocina abierta da profundidad [1].
- **Despeja con un prompt de edición** lo que estorbe (mueble de primer plano grande, mesa llena) y deja **sitio para lo que llegará** (las bolsas) [1].
- **Pon la comida y los asientos ya en la imagen** (un plato delante de cada silla, nada que tape la cámara): no hacen falta referencias de comida aparte [1].
- Define **anclas de fondo** por cada posición (tragaluces detrás de Mika, estantes detrás de Jenny, lámpara roja detrás de Alex) para poder comprobar que la escena se mantiene mientras la cámara se mueve [1].

### Utilería y extras
- **Una referencia por objeto clave** (el teléfono que pasa entre personajes; el empaque con el **logo hacia cámara**) [1].
- **Extras en una sola referencia** (los cuatro músicos juntos) [1].

### Anatomía del prompt de video (leída en pantalla) [1]
1. **REFERENCES**: cada `@char_…`, `@loc_…`, `@prop_…` con su descripción y una **restricción de uso** («Background only», «Geometry only; camera angle and any people in it are ignored», «Ignore the studio backdrop») [1].
2. **LOOK**: look global (ej. «clean modern digital cinema look, 35mm anamorphic, 24mm: rich saturated colour, deep clean blacks, punchy contrast, crisp detail — no faded film look, no lifted blacks, no haze, no halation, no noticeable grain»), color dominante (el rojo del empaque) [1].
3. **WHAT IS BEHIND EACH OF THEM** y **WHO IS WHERE**: qué se ve detrás de cada personaje y su posición exacta [1].
4. **Planos con tiempos y lente** («1.5–6.8s — Jenny and the flower, 28mm… focus on Jenny 1.5–2.7s; racks to the vase 2.7–5.5s; back to Jenny 5.5–6.8s»; «6.8–9.8s — 24mm, three-quarter angle, camera low… at 8.55s Mika cuts in»): posición de cámara, movimiento, **fases de enfoque**, acción con tiempos y expresión que se mantiene [1].
5. **SOUND**: p. ej. «No music, no effects. Room tone only…»; para voz en off, tipo de voz, ausencia de eco y tiempos de cada frase [1].
6. **KEEP CONSISTENT**: caras y ropa como en la referencia, color rico y saturado, sin subtítulos en pantalla [1].
- **Claude escribe el prompt** con un *skill* cargado (Customize → Skills → «+» → Upload a skill, un .zip con SKILL.md) que organiza la escena en planos con tiempos de diálogo y movimientos [1].
- Una toma de ≈17 s cuesta ≈200 créditos en Seedance 2.5 [1].

### Transiciones y cortes ocultos
- **Match cut**: corta en un gesto (el toque en el teléfono), conserva el encuadre y el movimiento de cámara; **solo cambia la locación** [1].
- **Cortes en acción** a través de las ubicaciones: la postura del personaje coincide a través del corte y la cámara sigue moviéndose [1].
- **Oculta el corte** con una espalda que llena el cuadro (el barrido lateral detrás de Mika hacia Japón); la cámara no se detiene, parece una toma continua [1].
- **Sonido**: corta la música y mete el ambiente de la nueva locación **antes** de la revelación [1].
- Dale a la locación un **momento propio** antes del corte (pasa un gondolero) [1].

### Arreglar fallos
| Fallo | Arreglo |
|---|---|
| Un personaje termina donde no debía (Alex en el sofá) | **Asigna su asiento explícitamente**, añade un **plano general corto antes del primer plano** como **fotograma clave** (fija quién está dónde y da anclas) y liga cada asiento a una referencia del fondo [1] |
| El ángulo inverso pone el fondo equivocado (un muro detrás de Alex) | **Describe qué se ve desde ese ángulo** (cámara junto al edificio apuntando al valle, edificio al lado de la cámara, colinas al fondo), **quita las instrucciones generales** que fijaban el fondo y **descríbelo por separado para cada plano** [1] |
| La IA inventa un elemento (cuatro puestos en la mesa para tres) | Pasa un **mapa de blocking cenital**: dibujo de líneas, figuras en gris con un **color por personaje** (naranja = Jenny, azul = Alex, verde = Mika), platos y teléfono; **el mapa controla la colocación, las fotos aportan personajes y sala y los colores son solo etiquetas**; deja espacio alrededor de las cabezas si la cámara rota [1] |
| El plano final no queda como se pidió | Describe con detalle lo que ocurre **justo cuando el movimiento termina** (el gato come), y deja el logo de frente al inicio [1] |
- **Anclas** = elementos fijos del fondo que dicen al modelo cómo colocar o mover la cámara; son muy importantes en ángulos inversos [1].

## Por herramienta
### Higgsfield Cinema Studio
- Proyecto con carpetas y subcarpetas; **elementos** (personajes, locaciones, props) que se adjuntan automáticamente al pegar el prompt; botón Generate con el costo en créditos [1].
- **Soul Cinema**: modelo de imagen preferido para personajes y locaciones (ocho imágenes por un crédito) [1]. **Seedream 5.0 Pro**: edición de imagen que conserva luz y textura [1]. **Seedance 2.5**: video (≈200 créditos por una toma de ≈17 s) [1].
- La descripción del video promete un enlace con prompts y assets, pero el que abrí lleva a otra página con el cuerpo vacío [1].

### Claude
- Modelo **Opus 5.5 High**; escribe los prompts de personaje, de edición de imagen, de locación y de video; con un *skill* de prompts cronometrados y otro de blocking (no obtenidos) [1].

## Errores comunes
- Cuando el modelo hace algo inesperado, **revisa tu prompt antes de culpar al modelo** (Alex: no se le asignó asiento) [1].
- Referencias sin nombre o con nombres distintos a los del prompt → el modelo no las enlaza [1].
- Instrucciones generales de fondo («el mural detrás de Alex en todos los ángulos») → rompen los ángulos inversos [1].
- Esperar que el modelo respete «tres personas» sin un mapa → añade puestos de más [1].
- Generar varias caras por referencia → inconsistencia; deja una cara [1].

## Checklist antes de entregar
- [ ] Hoja de personaje con una sola cara y atuendo completo para cada personaje.
- [ ] Locaciones fijadas (tres cuartos), despejadas y con anclas.
- [ ] Props y extras con referencia propia.
- [ ] Prompt con REFERENCES, LOOK, quién está dónde, planos con tiempos y lente, SOUND y KEEP CONSISTENT.
- [ ] Transiciones con corte oculto y sonido que cambia antes de la imagen.
- [ ] Mejores momentos de cada toma elegidos y montados; revisión final con audio.

## Para MUKIWA
- Creative Direction: hoja de personaje + locaciones fijadas + prompt cronometrado es un brief de rodaje para cualquier video de IA; el mapa de blocking cenital sirve también para dirigir personas reales.
- Visual Edits: lista de planos con tiempos por toma; elegir lo mejor de cada generación (ver `profe-editor-asistente`).

## Dudas abiertas
- [1] Es una **demo de producto de Higgsfield**: los modelos (Soul Cinema, Seedream 5.0 Pro, Seedance 2.5), los créditos (≈2 100 créditos el anuncio, ≈200 por toma de ≈17 s) y las ventajas («el mejor modelo ahora») son del momento y del vendedor; el método de referencias, anclas, tiempos y mapas es lo transferible.
- [1] Los prompts completos y los dos *skills* de Claude que menciona no se pudieron obtener (el enlace de la descripción no los trae). Higgsfield Academy tiene cursos con un *prompt-builder skill* parecido (no abierto).
- [1] El presentador afirma que una producción en vivo de EE. UU. cuesta decenas de miles de dólares: sin fuente.
- [1] El montaje final y el audio (voz en off, ambiente) solo se ven en el anuncio terminado al inicio y en fragmentos.
- Sin pasos para otras plataformas (Runway, Veo, etc.).

## Fuentes
- [1] Dirigir un anuncio de 30 s con video de IA: personajes, locaciones, prompt cronometrado y arreglo de fallos (Higgsfield, con Claude Opus 5.5 y Seedance 2.5) — https://youtu.be/kFKpcCHkuPI · `references/lecciones/dirigir-anuncio-con-video-ia-higgsfield-seedance.md`
