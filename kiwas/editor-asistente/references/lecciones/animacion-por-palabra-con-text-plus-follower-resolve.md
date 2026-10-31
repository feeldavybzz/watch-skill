# Animación por palabra dentro de un solo Text+ en DaVinci Resolve (procedimiento parcial)
> Separar el movimiento de cada palabra del movimiento del bloque usando modificadores del Text+; receta incompleta que hay que probar.

- **Fuente**: https://www.instagram.com/p/DfDEPNBtWHO/ · reel en francés (preset ofrecido al comentar TEXT, no obtenido)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local, **pierde términos y una expresión**; 10 fotogramas con la interfaz de Resolve
- **Confianza**: baja-media — la idea es clara, el procedimiento está incompleto

## Teoría (lo que se dijo)
- Basta **un** Text+. Se propone **Follower**, un retraso entre elementos, transformación por palabra, **Offset con XY Path** y **Anim Curves**; una progresión entre 0 y 1 alrededor de 25 fotogramas.

## Práctica (lo que se ve)
- Interfaz de Resolve y texto con trayectoria curva. No se leen los valores de cada modificador.

## Cruce teoría ↔ práctica
- Falta la expresión completa; **no hay evidencia suficiente para escribirla**. No se inventa el código.

## Receta paso a paso (parcial)
1. Crea un Text+ con la frase.
2. Añade un modificador **Follower** para aplicar el movimiento con retraso entre palabras.
3. Controla la trayectoria con Offset (XY Path) y suaviza con **Anim Curves**.
4. Anima la progresión de 0 a 1 en ≈25 fotogramas (valor orientativo del autor, no fijo).

## Para MUKIWA
- Motion / Visual Edits: títulos animados editables dentro de Resolve. Guardado como **prueba pendiente** en Resolve; no se presenta como receta terminada ni como preset instalado.

## Límites
- Sin la expresión, no se puede reproducir el efecto exacto. No se obtuvo el preset.
- Estaba en la cola de «ampliar evidencia» de la tanda del 30 oct (`references/instagram-2026-10-30/criterios-motion.md`): esta lección la resuelve solo en parte.

## Conecta con
- `kiwas/motion-graphics/references/instagram-2026-10-30/criterios-motion.md` · [[motion-en-codigo-render-determinista-seek-springs-y-motion-blur]]
