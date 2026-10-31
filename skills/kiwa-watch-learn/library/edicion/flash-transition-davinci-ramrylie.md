# Transición «frame flash» en DaVinci Resolve: tratamiento por fotograma
> Una transición de Fusion de 4 fotogramas con inversión/desenfoque direccional por fotograma.

- **Fuente**: reel de Instagram (archivo local `.mp4`) · @ramrylie · 93 s
- **Fecha**: 2026-10-28
- **Tipo de "oídos"**: Whisper (EN, voz clara) + subtítulos
- **Confianza**: alta para uso; baja para valores (UI pequeña) y no hay acceso al preset

## Teoría (lo que se dijo)
- [8–15 s] Arrastrar la transición entre dos clips.
- [15–28 s] Por defecto ocupa **cuatro fotogramas** y luego entra al clip normal.
- [32–44 s] Se puede cambiar el **tratamiento** de cada fotograma: invertir, desenfoque direccional, desenfoque + invertir.
- [44–51 s] En desenfoque direccional: dirección y longitud del desenfoque.
- [51–64 s] Para extender más de 4 fotogramas: pestañas «before 3…» y cambiar el tratamiento.
- [64–80 s] Controles de luces altas, sombras, contraste y saturación dentro del efecto (sin ir a Color).
- [80 s] Añadir diseño de sonido.
- Efecto gratuito comentando «flash».

## Práctica (lo que se ve)
- [5,6–15,52 s] Inspector: «Transition – RAM Frame Flash Four»; Duration ≈ 0,6 s (15 fotogramas); Sequence: Before 4 / 3 / 2 / 1 / After 1…; Treatment (Normal, Invert, Directional Blur, Blur + Invert), Footage (Outgoing/Automatic), Blur Length, Blur Direction, Pre-Invert Exposure, Exposure After Invert, Highlights, Shadows, Contrast, Saturation.
- [36–50 s] Resultado: blanco y negro con inversión que pasa a desenfoque horizontal.

## Cruce teoría ↔ práctica
Coinciden. El preset es del autor: no se puede reproducir sin recibirlo.

## Receta paso a paso
1. Poner la transición entre dos clips.
2. En Inspector → Transition, tratamiento por fotograma (Before 4…After 1).
3. Directional blur para dirección y longitud; invert para el flash.
4. Ajustar luces/sombras en el mismo panel.
5. Sonido de whoosh/impacto encima.

## Para MUKIWA
- Se puede replicar con Fusion/Adjustment Clip invertido 1–2 fotogramas + blur direccional; usar para cortes de acción con el color de marca.

## Límites
- **No entendido**: valores numéricos de cada fotograma; la UI es pequeña y no se leen. El preset no se obtuvo.

## Conecta con
- [[frame-rate-captura-presentacion-camara-lenta-studiobinder]]
