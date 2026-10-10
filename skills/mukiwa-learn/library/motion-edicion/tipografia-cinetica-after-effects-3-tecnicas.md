# Tipografía cinética en After Effects: 3 técnicas con una sola capa
> Animar caracteres/palabras con Animator + Range Selector, armar bloques de texto rotados que forman un gran bloque, y dar jerarquía con color — sin una capa por palabra.

- **Fuente**: https://www.youtube.com/watch?v=f3nb-MQyshQ · canal Koncepto (Juan Manuel) · 15:23
- **Fecha**: 2026-10-06
- **Tipo de "oídos"**: transcripción de subtítulos automáticos (.srt es; auto-sub con errores de reconocimiento: "kit frames" = keyframes, "ring selector" = range selector)
- **Confianza**: media-alta — técnica clara en frames + transcript; nombres de propiedades confirmados en UI; valores numéricos solo donde se dicen o se ven.

## Teoría (lo que se dijo)
- [0:42] Antes de animar tipografía cinética, **planea cómo se superponen los bloques** (papel o Photoshop) para saber cómo termina la composición.
- [1:36] Contra el método común (una capa por letra/palabra), aquí **una sola capa** anima todos los caracteres con Animator.
- [3:16] Técnica 2: **bloques de texto distintos** (títulos creativos / para after effects / gráficos de gran energía y ritmo rápido) rotados 90° / −90° y alineados entre sí.
- [10:33] Técnica 3: **color como foco de atención**: cambia el color por bloque según aparece, y degrada grises por línea.
- [12:30] Último efecto: color por palabra a medida que aparecen, con Fill Color + Range Selector (Start/End).

## Práctica (lo que se ve)
- [1:43–2:53] Capa "Títulos creativos": Animate → Opacity 0%, Range Selector con keyframe Start en 0 y ~12 frames después Start 100%; en Advanced, **Based On: Characters → Words**.
- [3:39–6:20] Atajos en pantalla: R (rotación), P (posición), S (escala), U (ver keyframes), F9 (easy ease). Bloque 1 rota 90° y se alinea junto a "PARA AFTER EFFECTS".
- [6:42–8:39] Tercer bloque con rotación −90°; se usan **controles/null con Pick Whip** para mover dos bloques a la vez ("pick whip al control").
- [9:14–10:11] Última capa: Animate → Position + Opacity 0%, keyframe de Start; en el **Graph Editor** curva con ease marcado para que la última palabra retenga más.
- [10:34] Se ve efecto de blur/desplazamiento en "GRAFICOS" entrando (animator con position + opacidad).
- [10:51–11:43] Color: keyframes de color blanco → naranja (#≈ naranja/amarillo) en bloques 1 y 2; blanco → grises degradados por línea en el bloque 3.
- [12:55–13:46] Fill Color (RGB) naranja + Range Selector animado **End 0→100% y luego Start 0→100%** para que el color "pase" como ola y se retire; modo Advanced Shape: **Ramp Up/Wiggly** (menú visible a 14:02).
- Look final: fondo morado-oscuro con viñeta, marco naranja-amarillo, texto blanco condensado bold (Anton-like), acentos naranja.

## Cruce teoría ↔ práctica
- Coincide: la lógica de "una capa, muchos animators" se ve en los timelines (un solo layer con Animator 1/2).
- Se dijo "planear en papel" pero no se muestra boceto; el frame de 8:47 muestra el bloque final completo como referencia visual de la composición.
- Valores exactos (frames, % de color) los dice de pasada; los hex del naranja no se muestran: ≈ estimado.

## Receta paso a paso
1. Crea el texto en una capa. Add → Animator → **Opacity** → 0%.
2. En Range Selector: keyframe **Start** 0% en t0; unos 12 frames después Start 100%.
3. Advanced → **Based On = Words** (o Characters). Selecciona keyframes, F9, y ajusta curva en el Graph Editor.
4. Para el bloque 2/3: nueva capa de texto, R/P para rotar (90°/−90°) y alinear al borde del bloque anterior; keyframes de posición+rotación entrantes con F9.
5. Usa un **control (null)** + Pick Whip para mover varios bloques juntos.
6. Última capa: Animator con Position + Opacity para entrada desde abajo.
7. Color: keyframes de Fill Color por bloque (blanco → naranja); degradado de grises por línea en el bloque grande.
8. Efecto extra: Animator → Fill Color; Range Selector End 0→100% y luego Start 0→100% (ola de color), Shape Ramp/Wiggly.

## Para MUKIWA
- Lime #C5ED2E como "foco" en vez del naranja; blanco/#232323 para el resto; blue #0068FB como color de ola secundaria.
- "FEEL DA VYBZ" / "VIBES NEVER LIE." como bloques: uno vertical (90°) y otro horizontal, formando un solo bloque tipográfico.
- Una sola capa por frase = proyectos más ligeros y fáciles de reeditar (Visual Edits Dept.).
- Aplicar Range Selector con Fill Color lime para que el color barra las palabras en reels 9:16.

## Límites
- Sin audio original (solo texto de subs auto con errores); no se leen valores exactos de easing/bezier.
- 44 frames cubren ~15:23 cada ~23 s: cambios finos entre keyframes se infieren.
- Primera frase del video se pierde en el parser de subs (bug conocido de VTT).

## Conecta con
- [[portfolio-de-diseno-profesional]] (mostrar proceso)
