---
name: kiwa-imagenes-ia
description: Profesor MUKIWA de creación de imágenes con IA en Higgsfield, Seedream y GPT Image, que aprende de las referencias que Bryan envía. Sabe fijar qué no puede cambiar, pedir a Claude un prompt de hoja de personaje, generar muchas opciones baratas, corregir detalles con un modelo de edición, y armar hojas de referencia por función (identidad, cuerpo y vestuario, mundo, objetos) para video con IA. Usar cuando Bryan pida crear imágenes con IA, una hoja de personaje, referencias de personajes, locaciones u objetos, un prompt de imagen, corregir una imagen generada, o pregunte cómo se hace algo de imágenes con IA.
metadata:
  nicho: imagenes-ia
  herramientas: "Higgsfield (Soul Cinema, Seedream), GPT Image, Claude"
  lecciones: 2
  actualizado: "2026-10-20"
---

# Kiwa · Imágenes con IA
> Crea imágenes con IA como material de producción, no como adorno: decide qué no puede cambiar, genera hojas de referencia con una función cada una (identidad, cuerpo y vestuario, mundo, objetos), pide a Claude el prompt, genera muchas opciones baratas y corrige los detalles con un modelo de edición. Hoy solo sabe hacerlo para **referencias de video con IA**; falta aprender el prompting de imagen en sí (estilo, lente, luz), otros modelos, upscaling y piezas de marca.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Para llevar las imágenes a video, combínalo con `kiwa-video-con-ia`; para el encuadre y la luz de la imagen, con `kiwa-composicion-visual` y `kiwa-iluminacion`; para piezas gráficas de marca, con `kiwa-diseno-grafico`.

## Cómo trabajar (cualquier imagen de referencia)
1. **Decide primero qué NO puede cambiar** (caras, vestuario, lugar, objetos): eso se fija en imágenes antes de generar nada más [2].
2. **Una hoja por función**, no una imagen bonita: identidad, cuerpo y vestuario, mundo, objetos [2]. Que no se contradigan entre sí [2].
3. **Pide a Claude el prompt**, describiéndole la idea básica; lo que le pides es una hoja de personaje: retrato + atuendo de frente y de espalda [1].
4. **Genera muchas opciones baratas y elige**; en Soul Cinema salen ocho imágenes por un crédito [1].
5. **Corrige los detalles con un modelo de edición**, no regenerando de cero: piel muy lisa, luz dura, pecas… con Seedream 5.0 Pro y un prompt de edición que también escribe Claude [1].
6. **No dejes un detalle importante a la interpretación**: si algo tiene que aparecer (un objeto sobre la mesa, un empaque con el logo hacia cámara), dale su propia referencia [1][2].
7. **Guarda cada referencia con nombre** y adjunta solo las que intervienen en la escena, explicando la función de cada una [1][2].

## Áreas
### Hojas de personaje [1][2]
- Prompt: retrato + atuendo **de frente y de espalda** sobre **fondo gris liso** (sin ruido visual, más utilizable) [1].
- **Un solo rostro** para el video: los demás paneles se recortan **del cuello hacia abajo** (solo ropa y proporciones) [1].
- Todas las capas del atuendo deben aparecer (ej. la sudadera con el gorro debajo); itera hasta que cada atuendo las tenga [1].
- Para identidad, rostro legible y en varios ángulos; para cuerpo, proporciones, ropa y accesorios definidos antes de animar [2].
- Guárdalo como **elemento con nombre** (ej. `char_mika`) y adjúntalo en cada escena [1].

### Locaciones y mundo [1][2]
- Como en un rodaje, **fija la luz, la disposición y el fondo** con imágenes de referencia antes de generar [1].
- Una referencia del lugar define luz y materiales; no tiene que ser el primer fotograma [2].
- **Anclas**: elementos fijos del fondo que dicen al modelo cómo colocar o mover la cámara; importan sobre todo en ángulos inversos [1].
- Mezcla de luz cálida interior con azul de la hora azul por la ventana, con cocina abierta para dar profundidad (ejemplo de [1]).

### Objetos y atrezzo [1][2]
- Cada objeto con acción propia va en su referencia (un teléfono que pasa entre personajes, un empaque con el logo hacia cámara, un objeto que se usa en la escena) [1][2].
- Atajo: varios extras en **una sola referencia** (los cuatro músicos juntos) [1].

### Mapas de blocking [1]
- Cuando la IA pone el número de puestos o personajes equivocado, un diagrama de blocking cenital hecho con Seedream (solo líneas) sirve de mapa para colocar a cada uno [1].

## Por herramienta
### Higgsfield (Soul Cinema, Seedream 5.0 Pro)
- **Soul Cinema**: modelo de imagen para personajes y locaciones (ocho imágenes por un crédito) [1]. **Seedream 5.0 Pro**: edición de imagen que conserva luz y textura [1]. Proyecto con carpetas y subcarpetas para ordenar referencias [1].
### GPT Image
- Se usó GPT Image 2.5 para las hojas de referencia de personajes, objetos y mundo de la guía de Seedance [2]. Los prompts de hoja de personaje y las plantillas editables de AiLendra no se han leído (ver Dudas abiertas).
### Claude
- Escribe el prompt de hoja de personaje y los prompts de edición a partir de la idea básica [1].

## Recetas
- **Personaje nuevo**: idea básica → Claude escribe el prompt de hoja (retrato + atuendo, frente y espalda, fondo gris) → muchas opciones baratas → elegir → corregir con edición → recortar paneles del cuello hacia abajo menos uno → guardar como elemento con nombre [1].
- **Objeto con acción**: referencia propia del objeto, descrita en el prompt de video con su función [1][2].

## Errores comunes
- Dejar un detalle importante a la interpretación → el modelo inventa otro; ponlo en una referencia [2].
- Hojas que se contradicen (ropa o cara distinta entre hojas) → el video pierde identidad [2].
- Fondo con ruido visual → pesa más y se usa peor; pide gris liso [1].
- Atuendo con capas faltantes → itera hasta que estén todas [1].
- Más de un rostro en la hoja que se adjunta → deja uno [1].

## Checklist antes de entregar
- [ ] Escrito qué no puede cambiar.
- [ ] Una hoja por función y sin contradicciones.
- [ ] Hoja de personaje con una sola cara y atuendo completo.
- [ ] Objetos importantes con su referencia.
- [ ] Detalles corregidos con edición, no dejados al azar.
- [ ] Referencias guardadas con nombre y solo las necesarias adjuntas.

## Para MUKIWA
- Creative Direction: personajes de la marca (p. ej. Arenio) como hojas de referencia fijas, siempre sobre fondo gris liso para poder recortar y reutilizar.
- Paleta lima #C5ED2E, azul #0068FB y negro #232323 como referencia de mundo cuando la pieza sea de marca.
- Graphic Design: estas imágenes son referencias de producción; las piezas finales de marca siguen el flujo de `kiwa-diseno-grafico`.

## Dudas abiertas
- [1] Es una **demo de producto de Higgsfield**: los modelos, los créditos y las ventajas son del momento y del vendedor; lo transferible es el método (hoja por función, opciones baratas, corrección con edición).
- [1] Los prompts completos y los dos *skills* de Claude que menciona no se pudieron obtener.
- [2] Es una guía pública resumida sin ver los ejemplos ni probar nada en Higgsfield; la propia página dice que el prompt original de la toma está pendiente de publicarse.
- AiLendra lista «Character Sheets Prompts» (dos variantes: ficha completa y frontal sin rostro) y tres plantillas editables de GPT Image 2.5 (creativo editorial, postal arquitectónica, ilustración editorial); solo se leyeron los títulos, **no los prompts**.
- Ninguna fuente enseña a escribir el prompt de una imagen en sí (estructura, estilo, lente, luz): el método de [1] delega eso en Claude sin mostrar el prompt.
- Falta aprender: prompting de imagen a fondo (estilo, lente, luz, composición), otros modelos (GPT Image, Nano Banana, Midjourney, Flux), inpainting y edición, variaciones, upscaling, consistencia de estilo de marca y piezas de marca para MUKIWA.

## Fuentes
- [1] Dirigir un anuncio de 30 s con video de IA: personajes, locaciones, prompt cronometrado y arreglo de fallos (Higgsfield, con Claude Opus 5.5 y Seedance 2.5) — https://youtu.be/kFKpcCHkuPI · `references/lecciones/dirigir-anuncio-con-video-ia-higgsfield-seedance.md`
- [2] Escenas consistentes con Seedance 2.5: referencias, audio primero y dirección de escena (AiLendra Labs) — https://ailendra.com/ailab/lite/seedance-25-escenas/ · `references/lecciones/escenas-consistentes-seedance-ailendra.md`
