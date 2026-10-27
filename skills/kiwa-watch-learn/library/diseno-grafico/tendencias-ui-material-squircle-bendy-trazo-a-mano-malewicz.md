# Tendencias de UI según Malewicz: material no es estilo, squircle, botones que se doblan y trazo a mano
> Un video de 12:51 separa las modas de «-morfismo» (solo un material) de los estilos con una propiedad propia, explica por qué la esquina squircle se lee mejor en listas y señala dos direcciones para no parecer genérico: comportamiento físico natural y elementos dibujados a mano.

- **Fuente**: https://youtu.be/psyw2_j_5jk · «UI design is changing. New trends emerge.» · Michal Malewicz · 12:51 · inglés.
- **Fecha**: 2026-10-12
- **Tipo de "oídos"**: audio transcrito con faster-whisper small (≈2 050 palabras), cotejado con el inicio de los subtítulos. Errores de Whisper: «glasomorphism» = glassmorphism, «new morphism» = neumorphism, «skew morphism» = skeuomorphism, «square call» = squircle, «this comorphism» = discomorphism, «right-league morphism» sin identificar.
- **Aporte del creador**: MEDIO-ALTO. Opinión de autor (dice haber acuñado «glassmorphism» y cocreado el neumorfismo; es su afirmación). Dos cuñas de venta propias ([7:16–7:33] y [12:26–12:51], ≈6 % del video). Recurso abierto: el prototipo del botón en michalmalewicz.com/bendybutton, que abrió y muestra un botón «Submit» sobre gris oscuro; el panel de ajustes del video no apareció en la página a ancho de móvil.
- **Confianza**: alta en lo dicho y en los rótulos; las 11 hojas y las 2 capturas fijas vistas. Hueco máximo sin captura: 13 s. No hay valores numéricos de diseño.

## Qué NO es este video
- No es un tutorial: no enseña a construir ninguno de los estilos ni da medidas, colores o curvas.
- Las «tendencias» son predicción del autor, sin datos.
- No habla de herramientas profesionales ni de paneles densos.

## Teoría (lo que se dijo)
- [0:45–2:31] Metal, disco, globo y demás «-morfismos» son **subconjuntos del esqueuomorfismo**: solo cambian el material. Un material no es un estilo.
- [2:31–3:37] El **vidrio** sí aporta algo más: es translúcido, y eso da **profundidad y contexto** (se ve lo que hay debajo). Funciona tanto con diseño plano como con esqueuomorfismo. Una textura de vidrio opaca sería solo otro material.
- [3:37–5:07] El **neumorfismo** es minimalista a propósito: sin texturas, solo elementos extruidos del fondo; queda entre el plano y el esqueuomorfismo. Sus problemas de accesibilidad «no son problemas» **si el resto está bien hecho**: contraste, jerarquía y tipografía correctos; el relieve es un extra, no lo que define la estructura. Se ve bien «si no se exagera».
- [5:07–6:00] El disco de Spotify es una textura de espejo ligada al contexto (música); experimento válido, no tendencia: no sirve fuera de una app de música.
- [6:00–7:16] **Squircle**: un radio de esquina intermedio entre cuadrado y círculo. Esquinas vivas = alerta, lujo, profesional, poco amable, y se procesan más rápido; el círculo es amable pero, apilado, hace zigzaguear la mirada; el squircle reduce ese hueco lateral: punto medio.
- [8:00–10:04] **Dirección 1 · realidad aumentada / comportamiento natural**: usar la potencia del dispositivo para luces y sombras reales, o **botones que reaccionan justo donde los pulsas** («bendy buttons»): se inclinan hacia el lado tocado, el lado opuesto se aclara y la sombra de abajo se desplaza. Hizo un prototipo con deslizadores para ajustar los valores a mano después de generarlo con IA.
- [10:04–11:25] **Dirección 2 · escrito o dibujado a mano**: botones con borde irregular y trazo de grosor desigual; más humano, imperfecto y personal, como reacción a que «todos los sitios se ven iguales».
- [11:25–12:26] No toda app necesita esqueuomorfismo: probar, construir, ver si funciona y descartar o usar. Lo curioso distingue al producto de lo genérico.

## Práctica (lo que se ve)
- [0:21] Su generador de glassmorphism: deslizadores Blur value, Refraction y Depth, y el CSS resultante.
- [1:59–3:11] Rótulos: disco y metal = «Material: hardness, reflectiveness, product context only»; vidrio sobre plano y sobre madera = además «Depth, Context»; «Glass texture» opaca = «No depth, no context».
- [3:52] Línea «Flat design — Neumorphism — Skeuomorphism», con «Glass» abarcándola entera.
- [3:43, 4:46] Cuaderno con bocetos a tinta y acuarela de un sistema neumórfico: niveles, vista lateral de botones extruidos y hundidos.
- [4:12] «Accessible: clear, contrasty icons fully visible · Enough whitespace for hierarchy and separation».
- [6:45–7:00] Tres columnas de cuadrados, squircles y círculos con la línea roja de lectura: recta, casi recta y en zigzag. Rótulo: «We read left to right, in an F-like pattern and circles disrupt it».
- [8:31–9:22] Botón gris oscuro sobre fondo gris que se inclina hacia el cursor; panel «Inspector» con ≈9 deslizadores (se leen tilt, depth, corner, perspective, shadow blur, shadow alpha, width, height) y tres colores (surface, depth, shadow); luego el botón en rojo.
- [9:35–9:47] Tarjetas oscuras «Pyramid» y «Diamond» que se inclinan en 3D, con etiquetas en monoespaciada.
- [10:19–10:38] Ejemplos a mano: «Slopless» con letras recortadas y botón amarillo de borde irregular; portfolio de @yanliudesign con trazo de lápiz, subrayados de rotulador y barra de herramientas dibujada.
- [10:55–11:05] Lo que llama «slop»: sitios oscuros con degradado azul y morado.

## Cruce teoría ↔ práctica
- Coinciden. El relieve del botón se demuestra; la iluminación con la cámara real solo se dice.
- Mostrado sin explicar: los valores del Inspector (no se leen completos) y cómo está programado.
- La defensa de la accesibilidad del neumorfismo es opinión del autor; el rótulo de [4:12] pone la condición: iconos con contraste y espacio en blanco suficientes.

## Receta paso a paso
1. Antes de adoptar un «estilo», preguntar qué aporta además del material: ¿profundidad?, ¿contexto?, ¿respuesta al gesto? Si es solo textura, usarla solo si conecta con el producto.
2. Hacer primero la estructura con contraste, jerarquía y tipografía; el relieve o el vidrio van encima como extra y la interfaz debe entenderse sin ellos.
3. En listas y pilas de elementos, esquinas squircle; esquinas vivas para un tono serio y rápido; círculos solo sueltos.
4. Para distinguirse: o un control con respuesta física localizada (inclinación + luz + sombra que se mueven juntas), o trazo a mano irregular. Prototipar con deslizadores, probar y descartar si no suma.
5. Evitar el genérico oscuro con degradado azul-morado.

## Para MUKIWA
- Coincide con la línea de `mukiwa-ui-plugins`: controles físicos sin neón ni glassmorphism; el «bendy button» es la misma idea que el stick con sombra dinámica de VYBZ-64.
- LIKKLE VIEW: ver `identidad/FASE-03-DIRECCIONES-DE-ESTILO.md`.

## Límites
- Sin valores; no se vio cada fotograma; el prototipo no se inspeccionó por dentro.
- Nada de esto está comprobado en un panel UXP de Premiere.

## Conecta con
- [[ux-ui-curso-mas-corto-eze-cichello]]
