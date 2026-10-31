---
name: kiwa-marca-mascota
description: "Identidad de marca y mascota en una sola skill: dirección de marca (auditoría, estrategia en una página, sistema visual, voz, libro de marca, entrega al sitio web), método de dibujo cartoon retro o rubber hose de los años 20 y 30 (cuerpos, ojos, manos, zapatos, poses, caricatura, acabado) y la mascota de MUKIWA con pupila de estrella (datos fijos, proceso en 3 capas, moods, entregables). Úsala cuando Bryan pida cerrar la identidad de una marca, diseñar, dibujar o variar un personaje o mascota, o aplicar el estilo retro cartoon."
---

# kiwa-marca-mascota — marca + mascota + dibujo retro

Une tres skills que se repetían: `direccion-de-marca-y-mascota`, `retro-cartoon` y `retro-cartoon-mascota`. El texto de cada una está **entero** en `references/`; aquí se decide cuál leer.

## Elige el camino
| Pedido | Lee |
|---|---|
| "Cierra la identidad de la marca", sistema visual, voz, reglas de uso, libro de marca, dejarla lista para la web | `references/direccion-de-marca.md` |
| Dibujar o diseñar cualquier personaje cartoon retro: cuerpos, ojos, manos, zapatos, poses, caricatura, acabado | `references/retro-cartoon-metodo-y-mascota.md`, **Parte A** |
| Diseñar, dibujar o variar **la mascota de MUKIWA** (pupila de estrella, moods, outfits, hoja de modelo) | `references/retro-cartoon-metodo-y-mascota.md`, **Parte B** |
| Una marca nueva con mascota completa | Primero `direccion-de-marca.md` (estrategia y sistema), luego la Parte A para el dibujo, y la sección 4 de la dirección de marca para el proceso del personaje |

`references/mascota-version-anterior.md` es una versión previa de la Parte B (93% igual). Solo sirve para comparar; **ante una diferencia, manda la Parte B**.

## Reglas que cruzan los tres textos
- **Audita antes de diseñar**: lo que ya existe de la marca (logo, colores, tipografía, personaje) se conserva salvo que se pida lo contrario. Nada de rediseñar entero.
- Los **datos fijos de la mascota** (sección «Datos del personaje», por ejemplo la pupila en forma de estrella) no se reinterpretan: están en la Parte B.
- Proceso de la mascota **por capas** (3 capas) y en el orden de cara que marca la Parte B, antes de pasar a moods y outfits.
- **Originalidad y derechos**: la caricatura de personas reales tiene confianza baja; síguele el aviso del texto. No copies personajes existentes.
- Entrega con el **checklist de la Parte B** y verifica contra la sección 9 de la dirección de marca antes de decir que está terminado.
- Para llevar la identidad a una web, pasa a `kiwa-web` (estilo MUKIWA en `diseno/reference/12-estilo-mukiwa.md`).

## Contexto de marca MUKIWA
La marca valora a las personas por quiénes son hoy, no por origen, color de piel ni clase social. La referencia cultural es inspiración, no tema. El punto de la "i" del logo puede funcionar como pupila y conecta con el personaje Arenio. No reemplaces el logo (MU en tratamiento Knerd, KIWA en Satoshi Black, ajustados a mano) por una tipografía genérica salvo petición expresa.

## Lecciones de rubber hose (Julina Mae)
Dos lecciones completas viven en `references/lecciones/`: `rubber-hose-desde-cero-cuerpos-ojos-manos-zapatos-poses-julina-mae.md` (5 tutoriales: cuerpos, ojos, guantes y manos, zapatos y poses femeninas; solo-visual, enseñanza en tarjetas) y `rubber-hose-caricatura-de-personas-reales-julina-mae.md` (de referencia de cine mudo a caricatura entintada). Úsalas junto a la Parte A.

## Criterios de enseñanza retro cartoon (fusionado de la skill `retrocartoon` de Codex, 2026-10-31)
Esa skill suelta se retiró: aquí queda una sola. Su SKILL.md solo traía reglas de método; las fichas `CURSO.md`/`INDICE.md` de Codex no llegaron, así que **no se absorbió su contenido** (pendiente si Bryan las pasa).
- Antes de adornos: intención emocional, función y acción del personaje. Si aún se estudia, explicar y proponer ejercicios; no presentar un personaje como aprobado.
- Orden de construcción: gesto y apoyo → masas de torso y cadera → extremidades → rostro, vestuario, accesorios. Comparar siluetas y proporciones, no aplicar curvas arbitrarias.
- Sistema coherente de ojos, manos y zapatos. Guantes, pie eyes y número de dedos son **elecciones**, no requisitos; conservar volumen entre frontal, tres cuartos y perfil.
- Contornos y áreas negras para legibilidad antes de textura y color; revisar la silueta a tamaño pequeño.
- Al explicar: principio, evidencia concreta, razón visual y ejercicio; separar lo que la fuente demuestra, lo que relata y nuestra interpretación. Ejercicios propios = propuestas, no palabras del creador.
- Animación: los clips terminados no prueban FPS, rigs ni timing exacto; pedir evidencia específica antes de enseñarlos.
- No mezclar rubber hose con retro shoujo, pixel art u otras familias retro: identificar la variante con la referencia real. Extraer principios de Julina, no clonar sus personajes. La skill es conocimiento consultable, no entrenamiento del modelo.
- Nueva lección: ficha con fuente, autor, fecha, tiempos/capturas, método de revisión (frames, audio, ASR), aplicación y límites; ampliar o corregir el principio existente, no duplicar; conservar contradicciones hasta resolverlas.
- **Por desarrollar (sin evidencia aún):** cabezas y bocas, perspectiva y giros, equilibrio y línea de acción, consistencia de model sheets, expresiones, peso, squash and stretch, timing.
