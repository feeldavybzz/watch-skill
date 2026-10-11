---
name: profe-motion-graphics
description: Profesor MUKIWA de motion graphics y animación, que aprende de las referencias en video que Bryan envía. Cubre tipografía cinética, animación de logos y títulos, transiciones gráficas, lower thirds, elementos para reels, easing y timing, en After Effects (y Premiere o DaVinci Fusion cuando haya fuentes). Usar cuando Bryan pida animar texto, un logo o gráficos, hacer kinetic typography, títulos animados, intros, transiciones, lyric videos, textos o gráficos para reels, ajustar keyframes o curvas, o pregunte cómo se hace algo de motion graphics.
metadata:
  nicho: motion-graphics
  herramientas: "After Effects, Blender"
  lecciones: 3
  actualizado: "2026-10-10"
---

# Profe: Motion graphics
> Anima con criterio: planea la composición final, una capa por bloque con Animators, curvas siempre suavizadas y el color para dirigir la mirada. Hoy domina la tipografía cinética en After Effects; el resto de áreas crece con cada video.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Todo lo animado vive aquí, en su área. El diseño estático va a `profe-diseno-grafico`.

## Cómo trabajar (cualquier animación)
1. **Planea el cuadro final antes de animar**: en papel o Photoshop, cómo encajan los elementos al terminar [1].
2. **Pocas capas, mucha animación**: una capa por bloque o frase, animada con Animators, no una capa por letra [1].
3. **Nunca keyframes lineales**: Easy Ease (F9) y ajuste en el Graph Editor [1].
4. **Agrupa con un control (null)** para mover conjuntos sin romper la animación [1].
5. **El color va al final** y marca el foco: qué debe mirar el espectador en cada momento [1].

## Áreas
### Tipografía cinética
- **Aparición por palabra o letra**: capa de texto → *Animate* → **Opacity** = 0% → *Range Selector*: keyframe **Start** 0% y, ≈12 frames después, 100% → *Advanced* → **Based On: Words** (o *Characters*) [1].
- **Entrada desde abajo**: Animator con **Position + Opacity** y el mismo Range Selector [1].
- **Bloques rotados que forman una composición**: una capa por bloque, rotación 90° / −90°, cada bloque alineado al borde del anterior, con keyframes de posición y rotación suavizados [1].
- **Ola de color por palabras**: *Animate* → **Fill Color** con el color de acento → anima **End** 0→100% y luego **Start** 0→100%; *Advanced* → **Shape: Ramp Up** o **Wiggly** [1].
- **Foco por bloque**: Fill Color de blanco al acento en el bloque que habla; el resto en blanco o grises [1].
- **Profundidad sin capas extra**: un gris distinto por línea, de claro a oscuro [1].

### Easing y timing
- Selecciona keyframes → **F9** → Graph Editor. Más ease al final hace que el último elemento "retenga" [1].

### Animación de logos, transiciones, lower thirds, elementos para reels
- **Guía que se dibuja y luego revela la foto** (reel de composición): línea blanca fina que se traza sobre negro (≈ 0,7 s), entra la imagen con la línea encima (≈ 1 s) y la línea se desvanece; etiqueta de texto integrada en la geometría. Cada bloque dura ≈ 2–3 s [2]. Valores de easing y trazo: no visibles, solo ≈.

### Animación 2D de personajes (cartoon clásico)
- **Orden de trabajo**: boceto tosco cuadro a cuadro → segunda pasada más clara (expresión, forma, diseño) → tinta → color plano → ajustes → escenario → ajuste de velocidad [3].
- **Boceto**: círculos y líneas para torso, cabeza y piernas, con la piel de cebolla del cuadro anterior; la sombra al suelo como trazo aparte [3].
- **Tinta**: una capa por parte del cuerpo (se mueve una sin tocar las demás); línea limpia que no tiembla, en marrón oscuro y no negro puro; color plano debajo de la línea [3].
- **Escenario 3D con aire de dibujo animado**: fondo en banda curva (arena que sube a mar y cielo) y objetos 3D como sombrillas; el personaje, un plano que recorre una trayectoria; el paralaje da el efecto Popeye [3].
- **Pies que no patinan**: ajusta la velocidad del avance del personaje hasta que el paso coincida con el suelo [3] (valor no visto).
- **Cierre para reels**: un objeto pasa a ras de cámara y tapa al personaje antes del corte [3].

## Por herramienta
### After Effects
- Atajos: **R** rotación, **P** posición, **S** escala, **U** ver keyframes, **F9** easy ease [1].
- Emparentar a un null con **Pick Whip** [1].

### Blender
- Dibujo 2D cuadro a cuadro con capas, piel de cebolla y barra de pinceles, línea de tiempo con un keyframe por cuadro, y vista 3D con cámara vertical 9:16 [3]. Nombres de menús y valores: no vistos; el creador no los dice.

## Errores comunes
- Una capa por palabra → proyecto pesado y difícil de reeditar [1].
- Animar sin saber el cuadro final → los elementos no encajan al terminar [1].
- Keyframes lineales → movimiento robótico [1].
- Todo el cuerpo en una sola capa de dibujo → cualquier ajuste obliga a redibujar [3].
- Velocidad de avance que no coincide con el paso → los pies patinan [3].

## Checklist antes de entregar
- [ ] Cuadro final planeado y respetado.
- [ ] Capas mínimas, con Animators.
- [ ] Easing revisado en el Graph Editor.
- [ ] Un solo color de foco, sincronizado con lo que se dice.
- [ ] Legible en móvil (9:16) si va a reels.

## Para MUKIWA
- Color de foco lima #C5ED2E sobre blanco y #232323; azul #0068FB como segunda ola [1].
- Frases de marca ("FEEL DA VYBZ" / "VIBES NEVER LIE.") como bloques: uno a 90° y otro horizontal, formando un solo bloque [1].
- Mascota o personaje retro animado: método de [3], a 9:16 nativo.
- Reels 9:16: ola de Fill Color lima barriendo las palabras clave.

## Dudas abiertas
- Valores de easing/bezier no visibles en [1]; los ≈12 frames son lo que se dijo.
- De [3] no hay fps, pinceles ni cómo se arma el fondo curvo; falta un tutorial completo de animación 2D en Blender.
- Animación de logos, transiciones, lower thirds y herramientas fuera de After Effects: sin fuentes todavía; de [2] solo se ve el resultado, no el método.

## Fuentes
- [1] Tipografía cinética en After Effects: 3 técnicas con una sola capa — https://www.youtube.com/watch?v=f3nb-MQyshQ · `references/lecciones/tipografia-cinetica-after-effects-3-tecnicas.md`
- [2] Reel de 24 s con 8 recursos de composición dibujados sobre fotos — archivo local · ver `profe-composicion-visual` (lección `reel-8-recursos-composicion-guias-sobre-fotos.md`)
- [3] Cartoon clásico en Blender (Youpie Toons, short de 61 s) — https://youtube.com/shorts/DCzXpBqt558 · `references/lecciones/dibujo-animado-clasico-blender-youpie-toons.md`
