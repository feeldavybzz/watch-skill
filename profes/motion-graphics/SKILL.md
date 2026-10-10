---
name: profe-motion-graphics
description: Profesor MUKIWA de motion graphics y animación, que aprende de las referencias en video que Bryan envía. Cubre tipografía cinética, animación de logos y títulos, transiciones gráficas, lower thirds, elementos para reels, easing y timing, en After Effects (y Premiere o DaVinci Fusion cuando haya fuentes). Usar cuando Bryan pida animar texto, un logo o gráficos, hacer kinetic typography, títulos animados, intros, transiciones, lyric videos, textos o gráficos para reels, ajustar keyframes o curvas, o pregunte cómo se hace algo de motion graphics.
metadata:
  nicho: motion-graphics
  herramientas: "After Effects"
  lecciones: 1
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
- Sin fuentes todavía.

## Por herramienta
### After Effects
- Atajos: **R** rotación, **P** posición, **S** escala, **U** ver keyframes, **F9** easy ease [1].
- Emparentar a un null con **Pick Whip** [1].

## Errores comunes
- Una capa por palabra → proyecto pesado y difícil de reeditar [1].
- Animar sin saber el cuadro final → los elementos no encajan al terminar [1].
- Keyframes lineales → movimiento robótico [1].

## Checklist antes de entregar
- [ ] Cuadro final planeado y respetado.
- [ ] Capas mínimas, con Animators.
- [ ] Easing revisado en el Graph Editor.
- [ ] Un solo color de foco, sincronizado con lo que se dice.
- [ ] Legible en móvil (9:16) si va a reels.

## Para MUKIWA
- Color de foco lima #C5ED2E sobre blanco y #232323; azul #0068FB como segunda ola [1].
- Frases de marca ("FEEL DA VYBZ" / "VIBES NEVER LIE.") como bloques: uno a 90° y otro horizontal, formando un solo bloque [1].
- Reels 9:16: ola de Fill Color lima barriendo las palabras clave.

## Dudas abiertas
- Valores de easing/bezier no visibles en [1]; los ≈12 frames son lo que se dijo.
- Animación de logos, transiciones, lower thirds y herramientas fuera de After Effects: sin fuentes todavía.

## Fuentes
- [1] Tipografía cinética en After Effects: 3 técnicas con una sola capa — https://www.youtube.com/watch?v=f3nb-MQyshQ · `references/lecciones/tipografia-cinetica-after-effects-3-tecnicas.md`
