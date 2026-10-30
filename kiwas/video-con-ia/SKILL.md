---
name: kiwa-video-con-ia
description: "Kiwa de dirección de video con IA (Higgsfield, Seedance): personajes y locaciones consistentes, prompt cronometrado por planos y arreglo de fallos."
metadata:
  nicho: video-con-ia
  herramientas: "Higgsfield Cinema Studio, Seedance, Seedream, Claude"
  lecciones: 5
  actualizado: "2026-10-28"
---

# Kiwa · Dirección de video con IA
> Dirige un anuncio o escena con modelos de imagen y video como si fuera un rodaje: fija personajes y locaciones como referencias con nombre, escribe un prompt cronometrado por planos (lente, enfoque, quién está dónde, sonido, continuidad) y arregla los fallos con un plano general como fotograma clave, anclas de fondo por ángulo y mapas de blocking. Todo lo aprendido viene de una demo en Higgsfield (créditos, Seedance 2.5): el método dura, los modelos y precios cambian. Falta aprender los prompts completos, el montaje final y otros modelos. Tiene **5 lecciones propias** ([1], [7]–[10]) y **4 complementarias** ([3] ángulos, [4] movimientos, [5] línea de 180°, [6] iluminación), más **1 guía pública absorbida** [2] que no cuenta como lección (menos confianza: fuente página pública).

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Para el blocking y la narrativa, combínalo con `kiwa-narrativa-y-direccion`; para ángulos, soportes y planos, con `kiwa-cinematografia`; para el montaje, con `kiwa-editor-asistente`.

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
| El ángulo inverso pone el fondo equivocado (un muro detrás de Alex) | **Describe qué se ve desde ese ángulo** (cámara junto al edificio apuntando al valle, edificio al lado de la cámara, colinas al fondo), **quita las instrucciones generales** que fijaban el fondo y **déscríbelo por separado para cada plano** [1] |
| La IA inventa un elemento (cuatro puestos en la mesa para tres) | Pasa un **mapa de blocking cenital**: dibujo de líneas sobre fondo blanco, con cada figura en **contorno de un color por personaje** (naranja = Jenny, azul = Alex, verde = Mika), platos y teléfono; **el mapa controla la colocación, las fotos aportan personajes y sala y los colores son solo etiquetas**; deja espacio alrededor de las cabezas si la cámara rota [1] |
| El plano final no queda como se pidió | Describe con detalle lo que ocurre **justo cuando el movimiento termina** (el gato come), y deja el logo de frente al inicio [1] |
- **Anclas** = elementos fijos del fondo que dicen al modelo cómo colocar o mover la cámara; son muy importantes en ángulos inversos [1].

### Escenas consistentes: método de la guía pública de Seedance [2]
(Resumen propio de una guía pública de AiLendra Labs; no se vio ningún video ni se probó: confianza menor que [1].)
1. **Decide primero qué NO puede cambiar** (caras, vestuario, lugar, objetos, sonido) y dirige después lo que pasa dentro de ese mundo [2].
2. **Una hoja de referencia por función**: identidad (rostro en varios ángulos), cuerpo y vestuario, mundo (luz, materiales, paleta) y objetos clave; que no se contradigan y adjunta solo las que intervienen [2].
3. **Audio primero**: separa textura (calidad de micro, ruido), voces (quién, acento, actitud) y eventos (qué suena y cuándo entra); escucha y aprueba antes de generar el video, que es lo más caro [2].
4. **Dirección de escena**: asigna el rol de cada referencia según el **orden real de los archivos**; dirige la actuación (quién habla, qué mira, gesto por frase; quien escucha respira y reacciona), la cámara (mano orgánica, paneo que llega ligeramente tarde; sin gimbal flotante ni órbitas) y la textura (cámara doméstica, color de consumo); escribe también lo que **no** buscas (piel pulida, HDR sintético, nitidez artificial) [2].
5. **Una escena a la vez, una variable por iteración**; resume el plan y confirma antes de gastar créditos [2].
- Lo que [2] y [1] comparten: referencias con función clara, anclas y dirigir actuación y cámara; lo que solo trae [2]: el audio como primer paso y la lista de lo que no se busca [1][2].

### Vocabulario de cámara, luz y línea de 180° para el prompt [3][4][5][6]
(Los términos salen de las lecciones; usarlos en un prompt de IA es una aplicación mía, ≈, sin probar.)
- **Ángulo** [3]: bajo, alto, cenital, holandés, a la altura de los ojos, del hombro, de la cadera, de la rodilla y a ras de suelo. El anuncio de [1] ya pide «three-quarter angle, camera low» en un plano; el efecto de cada ángulo (poder, vulnerabilidad, tensión, conexión) está en `kiwa-cinematografia` [3].
- **Movimiento** [4]: estático, paneo, whip pan, tilt, push in, pull out, zoom, crash zoom, dolly zoom, roll, tracking, trucking, arc, boom y aleatorio; la rotación suave del cenital de [1] es un *arc* [4].
- **Luz** [6]: clave alta o baja, claroscuro, luz dura o suave, lado ciego o corto, y temperatura (≈3 200 K tungsteno, ≈5 600 K día); sirve para escribir el LOOK y para fijar la luz de la locación [6].
- **Línea de 180°** [5]: en un **ángulo inverso**, define de qué lado de la línea queda la cámara y qué se ve detrás de cada personaje; es la causa más probable del fallo del muro detrás de Alex junto con la instrucción de fondo general de [1] (relación mía, ≈) [5].

### Efectos de transformación y motion transfer (reels de creadores) [7][8][9][10]
- **Imagen primero, video después** [7]: se edita un fotograma de tu clip con un modelo de imagen (dos referencias: tu fotograma y un fotograma del efecto) y esa imagen entra al modelo de video como primer fotograma. Así el efecto se decide en la imagen (barata de iterar) y el video solo lo anima.
- **Prompt de imagen para copiar un efecto** [7]: «edita solo la imagen 1; la 2 muestra el efecto, no copies su persona/ropa/cuarto/colores» + el efecto en una frase + dónde empieza + forma + superficie y color + «todo lo demás idéntico (encuadre, pose, ropa, luz, grade, grano), fotorrealista, sin texto».
- **Prompt de video del efecto** [7]: movimiento de cámara lento y estable (sin sacudida, sin cortes, sin rotación) + «solo se mueve X» + lo que nunca debe pasar (p. ej. que la cara se reforme) + mismo grade, contraste y grano + sin texto.
- **Hook con material real** [8]: grabar el gesto real (encendedor), capturar el comentario como imagen y darle al modelo el video (@video1) y la imagen (@img1); el prompt pide el efecto (quemarse con llamas, brasas, ceniza) **solo sobre la tarjeta** y fija lo que se mantiene (identidad, expresión, manos, ropa, movimiento original, fondo, encuadre, audio, formato vertical). Se usó un modelo de «movimiento y control avanzados» (Kling 4.0).
- **Motion transfer (Genjutsu en Higgsfield)** [9][10]: el clip original manda el movimiento y la referencia manda el look. Flujo: clip simple → sacar un fotograma → editarlo con un modelo de imagen (p. ej. cambiar el fondo) → Genjutsu «Motion transfer» con el clip y el fotograma → describir la escena → generar. Hay una segunda pestaña «Objects swap». En pantalla: video de hasta 30 s y hasta 30 imágenes de referencia.
- Modelos vistos en la lista de Artlist [8] (cambian rápido): Seedance 2.5 (30 s, hasta 50 referencias), Kling 4.0 (30 s, 1080p), Gemini Omni 1.1 Flash (4K, 10 s).

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
- Generar el video sin haber decidido el audio → es lo más caro de rehacer [2].
- Dejar sin decir lo que NO quieres (piel pulida, HDR sintético) → el modelo tiende a ese aspecto [2] (≈, sin probar).

## Checklist antes de entregar
- [ ] Hoja de personaje con una sola cara y atuendo completo para cada personaje.
- [ ] Locaciones fijadas (tres cuartos), despejadas y con anclas.
- [ ] Props y extras con referencia propia.
- [ ] Prompt con REFERENCES, LOOK, quién está dónde, planos con tiempos y lente, SOUND y KEEP CONSISTENT.
- [ ] Transiciones con corte oculto y sonido que cambia antes de la imagen.
- [ ] Mejores momentos de cada toma elegidos y montados; revisión final con audio.
- [ ] Audio decidido antes del video y lista de lo que no se busca escrita [2].
- [ ] En ángulos inversos: lado de la cámara y fondo visible descritos por plano [1][5].

## Para MUKIWA
- Creative Direction: hoja de personaje + locaciones fijadas + prompt cronometrado es un brief de rodaje para cualquier video de IA; el mapa de blocking cenital sirve también para dirigir personas reales.
- Visual Edits: lista de planos con tiempos por toma; elegir lo mejor de cada generación (ver `kiwa-editor-asistente`).

## Dudas abiertas
- [1] Es una **demo de producto de Higgsfield**: los modelos (Soul Cinema, Seedream 5.0 Pro, Seedance 2.5), los créditos (≈2 100 créditos el anuncio, ≈200 por toma de ≈17 s) y las ventajas («el mejor modelo ahora») son del momento y del vendedor; el método de referencias, anclas, tiempos y mapas es lo transferible.
- [1] Los prompts completos y los dos *skills* de Claude que menciona no se pudieron obtener (el enlace de la descripción no los trae). Higgsfield Academy tiene cursos con un *prompt-builder skill* parecido (no abierto).
- [1] El presentador afirma que una producción en vivo de EE. UU. cuesta decenas de miles de dólares: sin fuente.
- [1] El montaje final y el audio (voz en off, ambiente) solo se ven en el anuncio terminado al inicio y en fragmentos.
- Sin pasos para otras plataformas (Runway, Veo, etc.).
- [2] Es una guía pública de otro creador (Seedance), resumida sin ver el ZIP de la skill: faltan prompts y valores; nada se probó en Higgsfield.
- [3][4][5][6] Las cuatro lecciones complementarias son de cine real: dan vocabulario, no sirven como prueba de que el modelo de IA obedezca cada término.
- [7] Los prompts de [7] y [8] solo se leen en parte (se entregan por comentario); la estructura de bloques es lo transferible.
- [9][10] Genjutsu: no se vio el costo en créditos ni la calidad en planos largos; el nombre del modelo de imagen de [10] viene mal oído por Whisper (≈ Seedream 5 Pro).
- [7][8] Son reels de creadores que venden/regalan prompts por comentario: lo mostrado son resultados escogidos.

## Fuentes
- [1] Dirigir un anuncio de 30 s con video de IA: personajes, locaciones, prompt cronometrado y arreglo de fallos (Higgsfield, con Claude Opus 5.5 y Seedance 2.5) — https://youtu.be/kFKpcCHkuPI · `references/lecciones/dirigir-anuncio-con-video-ia-higgsfield-seedance.md`
- [2] Escenas consistentes con Seedance (guía pública de AiLendra Labs, https://ailendra.com/ailab/lite/seedance-25-escenas/; fuente: página pública, resumen propio, registrada en `library/skills-absorbidas.md`)
- [3] Los 9 ángulos o alturas de cámara (StudioBinder, Shot List ep. 3) — https://youtu.be/wLfZL9PZI9k · `references/lecciones/nueve-angulos-de-camara-studiobinder.md`
- [4] Los 15 movimientos de cámara (StudioBinder, Shot List ep. 6) — https://youtu.be/IiyBo-qLDeM · `references/lecciones/movimientos-de-camara-15-studiobinder.md`
- [5] La regla de los 180° (StudioBinder) — https://youtu.be/iW0bKUfvH2c · `references/lecciones/regla-de-los-180-grados-studiobinder.md`
- [6] Iluminación de cine, parte 1 (StudioBinder, Shot List ep. 12) — https://youtu.be/r2nD_knsNrc · `references/lecciones/iluminacion-cine-parte-1-tipos-terminos-equipo-studiobinder.md`
- [7] Efecto «doom scroll» con Nano Banana Pro + Kling 3.0 en Artlist (@artzenmedia) — reel de Instagram, archivo local · `references/lecciones/doom-scroll-efecto-nano-banana-kling-artzenmedia.md`
- [8] Hook «quemar un comentario» con video IA, Artlist + Kling 4.0 (@futurist__) — reel de Instagram, archivo local · `references/lecciones/hook-quemar-comentario-kling-artlist-futurist.md`
- [9] Genjutsu de Higgsfield: cambiar ropa, objetos y lugar manteniendo el movimiento (@elmundoderabbit) — reel de Instagram, archivo local · `references/lecciones/genjutsu-higgsfield-cambiar-ropa-y-entorno-elmundoderabbit.md`
- [10] Genjutsu: rodar en casa y convertir el fondo en un vagón de lujo (@tseily) — reel de Instagram, archivo local · `references/lecciones/genjutsu-motion-transfer-seedream-tseily.md`
