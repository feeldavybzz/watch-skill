---
name: profe-tipografia-cinetica
description: Profesor MUKIWA de tipografía cinética en After Effects. Sabe hacerlo paso a paso, con lo aprendido de referencias reales que Bryan fue enviando. Usar cuando Bryan pida animar texto, hacer kinetic typography, títulos animados, lyric videos o textos para reels, o pregunte cómo se hace algo de tipografía cinética.
metadata:
  nicho: tipografia-cinetica
  herramientas: "After Effects"
  lecciones: 1
  actualizado: "2026-10-10"
---

# Profe: Tipografía cinética
> Anima frases enteras con una sola capa por bloque (Animators + Range Selector), arma bloques rotados que forman una composición y usa el color para dirigir la mirada.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".

## Cómo trabajar
1. **Planea la composición final antes de animar**: en papel o Photoshop, cómo se superponen y alinean los bloques al terminar [1].
2. **Una capa de texto por frase o bloque**, no una por letra ni por palabra. La animación sale de los Animators [1].
3. Anima la entrada de cada bloque con Range Selector y suaviza con curvas [1].
4. Mueve y encaja los bloques con rotación/posición, y agrúpalos con un control (null) [1].
5. Al final, el color: decide qué bloque o palabra es el foco y anímalo [1].

## Por herramienta
### After Effects
- **Aparición por palabra**: capa de texto → *Animate* → **Opacity** = 0% → en *Range Selector*, keyframe **Start** 0% y, ≈12 frames después, Start 100% → *Advanced* → **Based On: Words** (o *Characters* para letra a letra) [1].
- **Suavizar**: selecciona los keyframes, **F9** (Easy Ease) y ajusta la curva en el **Graph Editor**. Una curva con más ease al final hace que la última palabra "retenga" [1].
- **Entrada desde abajo**: Animator con **Position + Opacity** y el mismo Range Selector [1].
- **Bloques rotados**: nueva capa por bloque, **R** rotación (90° / −90°), **P** posición; alínealo al borde del bloque anterior. Keyframes de posición y rotación con F9 [1].
- **Mover varios bloques juntos**: crea un null/control y emparenta los bloques con **Pick Whip** [1].
- Atajos usados: **R** rotación, **P** posición, **S** escala, **U** ver keyframes, **F9** easy ease [1].

## Recetas
- **Ola de color por palabras**: *Animate* → **Fill Color** (RGB) con el color de acento → Range Selector: anima **End** 0→100% y después **Start** 0→100%, para que el color pase como ola y se retire. *Advanced* → **Shape: Ramp Up** o **Wiggly** para el borde de la ola [1].
- **Foco por bloque**: keyframes de Fill Color blanco → acento en el bloque que habla en ese momento; el resto en blanco o grises [1].
- **Profundidad sin capas extra**: en un bloque grande, un gris distinto por línea, de claro a oscuro [1].

## Errores comunes
- Una capa por palabra → proyecto pesado y difícil de reeditar. Usa Animators en una sola capa [1].
- Animar sin saber la composición final → los bloques no encajan al terminar. Planéala antes [1].
- Keyframes lineales → movimiento robótico. Siempre F9 y curva [1].

## Checklist antes de entregar
- [ ] Composición final planeada y respetada.
- [ ] Una capa por bloque, con Animators.
- [ ] Todos los keyframes con easing revisado en el Graph Editor.
- [ ] Un solo color de foco, que acompaña lo que se dice.
- [ ] Legible en móvil (9:16) si va a reels.

## Para MUKIWA
- Color de foco: lima #C5ED2E sobre blanco y #232323; azul #0068FB como segunda ola [1].
- Frases de marca ("FEEL DA VYBZ" / "VIBES NEVER LIE.") como bloques: uno vertical a 90° y otro horizontal, formando un solo bloque tipográfico [1].
- Reels 9:16: ola de Fill Color lima barriendo las palabras clave.

## Dudas abiertas
- Valores exactos de easing/bezier no visibles en [1]; los ≈12 frames son lo que se dijo.
- Tipografía del ejemplo: condensada bold, tipo Anton (≈, no confirmada).

## Fuentes
- [1] Tipografía cinética en After Effects: 3 técnicas con una sola capa — https://www.youtube.com/watch?v=f3nb-MQyshQ · `references/lecciones/tipografia-cinetica-after-effects-3-tecnicas.md`
