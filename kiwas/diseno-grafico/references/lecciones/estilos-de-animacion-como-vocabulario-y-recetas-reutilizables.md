# Estilos de animación como vocabulario y como recetas reutilizables
> Un nombre de estilo (Glassmorphism, Swiss grid…) describe apariencia, no animación: para pedir movimiento hay que añadir sujeto, disparador, duración, easing y límites.

- **Fuentes**: https://www.instagram.com/p/DfIob_ZOC7s/ (diez estilos para pedir a Claude, Sebas Dev, 17,1 s) · https://www.instagram.com/p/DfErDx0RE40/ (estilos con comandos de barra en Claude Code, 22,3 s) · https://www.instagram.com/p/DfAqpTsOHYn/ (catálogo web de zapatillas)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local (en DfIob_ZOC7s «Cloud» = Claude; DfErDx0RE40 sin voz); descripciones; fotogramas
- **Confianza**: media — vocabulario y estructura sí; código y prompts no se obtuvieron

## Teoría (lo que se dijo)
- DfIob_ZOC7s: Liquid Morph, Glassmorphism, Kinetic Type, ASCII Art, Isometric, Gradient Mesh, Comic Book, Blueprint, Pixel Art y Partículas.
- DfErDx0RE40: estilos construidos con Claude Code, cada uno con un prompt: /swiss-grid, /retro-crt, /blue-editorial, /oscilloscope y /animate que los agrupa.

## Práctica (lo que se ve)
- Ejemplos arriba, presentador abajo, rótulos grandes con contorno. Algunas etiquetas llegan tarde o persisten sobre el siguiente ejemplo: **no usar un fotograma aislado** para asignar el estilo. La fuente de DfIob_ZOC7s es 360×640.
- DfAqpTsOHYn: una parrilla de productos que pasa a una ficha con la zapatilla protagonista, controles y un móvil al frente; fondo oscuro neutro y base naranja.

## Cruce teoría ↔ práctica
- Los comandos con barra son **definiciones que el creador preparó**; el video no demuestra que existan por defecto. Escribir el mismo comando sin crear su definición no hace nada.
- «CRT» es una estética de pantalla, **no una lección de dibujo rubber hose**: no va a `retro-cartoon`.

## Receta paso a paso
1. Define para cada estilo: **retícula y márgenes, colores, familia tipográfica, ritmo de entrada y salida** y contenido intercambiable.
2. Al pedir motion, completa el brief: sujeto, acción, disparador, duración, easing, límites y salida. Ejemplo propuesto (nuestro): «al terminar la importación, transforma el indicador circular en una marca de confirmación en 250 ms; conserva el espacio del control y respeta reducir movimiento». Los 250 ms son una elección nuestra.
3. Crea una receta que reciba titular y subtítulo y produzca una vista previa y un video de dimensiones conocidas (propuesta; **no implementada aquí**).
4. Catálogo y detalle: la misma identidad debe sobrevivir a ambos (fondo, escala del producto y navegación); miniaturas comparables y vista previa grande.

## Para MUKIWA
- Motion y UI: glosario para briefs de paneles de plugin; se enlaza con la skill `kiwa-ui-plugins`.

## Límites
- No se obtuvieron los prompts ni el código. No se midió rendimiento, accesibilidad ni comportamiento responsive del catálogo. No es un plugin demostrado.

## Conecta con
- [[prompt-motion-catalogo-265-motions-hechos-con-claude]] · [[motion-en-codigo-render-determinista-seek-springs-y-motion-blur]]
