# Revelado de un logo con ruido y goteo con CC Smear en After Effects
> Separar el revelado (ruido + mapa de desplazamiento) de la deformación localizada (goteo) en un título o logo.

- **Fuente**: https://www.instagram.com/p/DfF8uSkRgmx/ · reel de un creador (la segunda mitad promociona un concurso con fecha)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local + 10 fotogramas generales y 8 adicionales entre 25 y 95 s
- **Confianza**: media — los controles de CC Smear se leen; la mejora del revelado hecha tras consultar a Claude **no se ve completa**

## Teoría (lo que se dijo)
- Empieza transformando una foto de producto con IA, anima el fondo y trabaja texto y logo en After Effects.
- Fractal Noise en un sólido o precomposición; texto y logo en precomposiciones separadas; **Displacement Map** usando ese ruido. Luego mejora el aspecto del revelado tras consultar a Claude.
- Para el goteo nombra **CC Smear**.

## Práctica (lo que se ve)
- Controles **From** y **To**, fotogramas clave y desplazamiento de manejadores para estirar zonas del logo. Duplica el efecto para repartir varios goteos. Capturas entre 65 y 95 s corroboran controles, timeline y resultado.

## Cruce teoría ↔ práctica
- Revelado (ruido/máscara/distorsión) y deformación localizada (goteo) son **operaciones distintas**; no se resuelven ambas bajando la opacidad de forma uniforme. No se reconstruye un stack exacto del revelado final.

## Receta paso a paso
1. Escribe tu palabra o logo y **precomponla**; mantén texto y logo en precomposiciones separadas.
2. Revelado: Fractal Noise en un sólido/precomp + **Displacement Map** (o máscara) que use ese ruido; anima la evolución del ruido.
3. Goteo: aplica **CC Smear** a la precomposición; anima *From* y *To* con fotogramas clave y mueve los manejadores para estirar la zona elegida.
4. Prueba **un solo estiramiento** antes de duplicar el efecto para varios goteos.

## Para MUKIWA
- Motion: títulos y logos con revelado orgánico. No se copian los valores de coordenadas: dependen del tamaño y composición de cada proyecto, y varios son ilegibles.

## Límites
- La parte del concurso es temporal y no es conocimiento técnico. No se participó ni se generó material con créditos.

## Conecta con
- [[camara-3d-after-effects-controles-peter-kasilo]] · [[cc-composite-after-effects-boone]]
