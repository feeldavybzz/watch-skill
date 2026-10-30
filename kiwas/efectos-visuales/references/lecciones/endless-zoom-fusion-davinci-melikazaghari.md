# «Endless zoom» en DaVinci Resolve: portal de papel verde + Fusion 3D
> Zoom infinito por apilamiento de tomas en un Fusion Clip con cámara 3D.

- **Fuente**: reel de Instagram (archivo local `.mp4`) · @melikazaghari · 29 s
- **Fecha**: 2026-10-28
- **Tipo de "oídos"**: ninguno útil: Whisper devuelve «I'm happy» (música); explicación solo en texto en pantalla
- **Confianza**: media — pasos escritos legibles; sin valores numéricos

## Teoría (lo que se dijo)
- Sin teoría hablada. Los pasos vienen de los rótulos en pantalla (EN).

## Práctica (lo que se ve)
- [0–7 s] Resultado: la protagonista entra por un marco de la pared que vuelve a contener la misma escena, repetido.
- [9–11 s] «1) Locked tripod shot 2) Manual focus 3) Green paper portal»: trípode fijo, foco manual, papel verde en el marco como portal.
- [13 s] «In Fusion, remove green screen using Delta Keyer and Mask».
- [15–17 s] «Cut clips, match length, stack them» y «New Fusion Clip».
- [19–25 s] «3D Node Setup – layers placed in Z-depth»: clip principal → Image Plane 3D → Merge 3D → Renderer 3D → MediaOut; Camera 3D al mismo Merge 3D; los otros clips → Image Plane 3D → mismo Merge; empujar las capas hacia atrás en Z.
- [27–29 s] «Animate Camera 3D, smooth in Spline, Render Cache ON»; en el árbol se cuentan 8 MediaIn.

## Cruce teoría ↔ práctica
No aplica.

## Receta paso a paso
1. Rodar varias tomas iguales (trípode, foco manual) con papel verde donde irá el siguiente nivel.
2. En Fusion, Delta Keyer + máscara para quitar el verde.
3. Apilar los clips (misma duración) en un Fusion Clip.
4. Image Plane 3D por clip → Merge 3D → Renderer 3D; separar en Z.
5. Animar Camera 3D con spline suave; activar Render Cache.

## Para MUKIWA
- Transición/identidad: mismo truco con un portal que lleve al logo MUKIWA; iluminación oscura y cálida con acento lima.

## Límites
- **No entendido**: distancias en Z, keyframes de cámara, cuántas tomas por segundo ni cómo se alinea el marco entre tomas; no hay voz.
- Texto del paso 6 de nodos leído a baja resolución (≈).

## Conecta con
- [[soportes-de-camara-12-rigs-studiobinder]]
