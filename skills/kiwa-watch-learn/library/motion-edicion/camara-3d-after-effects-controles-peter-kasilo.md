# Cámara 3D de After Effects: crear, controlar, profundidad de campo y mover con keyframes
> Qué hace cada ajuste de la cámara 3D de After Effects (tipo, focal, profundidad de campo, iris), cómo se mueve con las herramientas o con keyframes y cómo dejarla enfocada en una capa.

- **Fuente**: https://youtu.be/qO3_WBYCe-E · Peter Kasilo (Kasix Creativity) · «How to use the 3D camera tool in After Effects» · 12:23 · inglés · publicado 2023-01-12
- **Fecha**: 2026-10-30
- **Tipo de "oídos"**: subtítulos automáticos de YouTube en inglés (`oir.py`, ≈2 200 palabras, video completo). Sin Whisper.
- **Confianza**: alta en el flujo y en los valores de los paneles (leídos en pantalla, ampliados); media en las frases del autor (subtítulos automáticos con errores como «casa 2» por «cursor» o «Dolly 2» por «dolly tool»).
- **Aporte**: medio-alto para el control de cámara; es un tutorial de principiante con un solo ejemplo animado (un logo sobre círculos concéntricos). Enlaces de la descripción (bundle de AEJuice, Dehencer) son de venta/afiliado y no se abrieron.

## Teoría (lo que se dijo)
- [00:00–00:35] La cámara 3D da profundidad, dimensión y movimientos a los gráficos. Tres formas de crearla: botón de nueva capa abajo → Camera; menú Layer → New → Camera; atajo **Ctrl + Alt + Shift + C**.
- [00:37–01:35] Tipo de cámara: **one-node** (orienta sobre sí misma; captura lo que la rodea sin desplazarse) y **two-node** (orienta alrededor de un **punto de interés**). Todos los ajustes imitan una cámara real.
- [01:40–02:30] El nombre se deja («Camera 1»). El **preset** viene en **focales de 15 a 200 mm**: corta (15 mm) = ángulo muy amplio; larga (200 mm) = ángulo estrecho, sujeto más grande, más desenfoque y más nitidez en el sujeto. **50 mm** se acerca a cómo ve el ojo humano (afirmación del autor).
- [02:28–02:50] Antes de aceptar, marcar **Enable Depth of Field** (por defecto puede venir desmarcado): es el desenfoque entre lo enfocado y lo que no. Los ajustes se pueden cambiar después.
- [02:53–03:55] En AE 2023 hay un menú de vistas (en versiones anteriores, un icono de cámara). Con varias vistas (Active Camera, Left, Top, Front, Right) se ve la cámara desde fuera y se puede alejar o acercar la vista. Dejar la vista en **Active Camera** = lo que ve la cámara en pantalla.
- [04:10–05:55] Controles principales: **Orbit** (orbitar), **Pan** (barrer de izquierda a derecha) y **Dolly**. Dolly ≠ zoom: con zoom la cámara está quieta y se acerca con ajustes digitales; con dolly **la cámara se mueve hacia el sujeto**. Orbit tiene tres modos (alrededor del cursor, de la escena y del punto de la cámara). El autor aclara que en AE lo que parece «pan» a veces es un **tilt**. El dolly acerca hacia el cursor (una crucecita marca el punto).
- [06:00–07:30] Con la capa de cámara seleccionada hay dos grupos: **Transform** (Point of Interest, Position, Orientation, Rotation en X, Y, Z) y **Camera Options**. Eje Z = frente, X = lado, Y = vertical. Se animan con keyframes para movimientos distintos a los de las herramientas: Position mueve (panea y inclina), Rotation gira en cada eje, Orientation orienta. Con una cámara one-node, la cámara orientaría sobre sí misma.
- [07:40–09:40] **Camera Options**: Zoom; **Depth of Field**; **Focus Distance** (a qué distancia el sujeto está nítido); **Aperture** (abertura delante del sensor; con más abertura más se desenfoca); **Blur Level** (100 % = desenfoque natural). En una cámara real la abertura se mide en f-stops: f más bajo = fondo más borroso (bokeh), f más alto = más imagen nítida; en la cámara de AE funciona distinto. **Iris Shape**: dejar «Fast Rectangle» porque afecta cómo se ven los píxeles fuera de foco y renderiza más rápido. Los **Highlight** (gain, threshold, saturation) refuerzan la luminosidad de los píxeles desenfocados.
- [09:45–10:40] **Foco automático**: con la capa de cámara seleccionada, Layer → Camera: **Link Focus Distance to Point of Interest**, **Link Focus Distance to Layer** y **Set Focus Distance to Layer**. Su favorita es la del medio (Link to Layer), que él llama autofocus: al hacer dolly adelante o atrás, **el foco se queda en el logo**.
- [10:41–12:00] Movimiento con keyframes: activar el cronómetro de **Position**, hacer dolly hacia el centro del logo, avanzar en la línea de tiempo y hacer dolly de salida; aplicar **Easy Ease** (salida y entrada); reproducir. Se puede acortar la animación para hacerla más rápida y keyframear **Z Rotation** para sumar giro (el logo termina girado).

## Práctica (lo que se ve)
- [00:00–00:50, 01:45–03:55, 05:00–11:55] Presentador en recuadro redondo (picture-in-picture) sobre pantalla de After Effects (interfaz oscura; comp con anillos concéntricos azul-verdosos sobre negro y un logo central).
- [00:25] Menú de la capa nueva → Camera; [00:35] rótulo «CTRL + ALT + SHIFT + C».
- [00:45–00:46] (ampliado) **Camera Settings**: Type = Two-Node Camera (la lista muestra One-Node y Two-Node), Name «Camera 1», **Preset 50mm**, **Film Size 36.00 mm**, **Focal Length 50.00 mm**, **Angle of View 39.60°**, Zoom 940.74 mm, Enable Depth of Field marcado, **Focus Distance 940.74 mm**, Lock to Zoom marcado, **Aperture 8.93 mm**, **F-Stop 5.6**, **Blur Level 100.0 %**, Units millimeters, Measure Film Size Horizontally, Comp Size 677.33 mm, «Create Camera From Current View» desmarcado.
- [02:25] Lista de presets: Custom, 15, 20, 24, 28, 35, **50 (marcado)**, 80, 135, 200 mm.
- [03:05] Tooltip de la barra de herramientas: «Pan Camera POI Tool: Pan speed remains constant relative to the camera's point of interest (2, Shift+2)».
- [03:35–03:55] Vista de cuatro paneles: activa arriba a la izquierda, más Top y Right con la cámara dibujada como icono; después se aleja para ver la cámara lejos de la capa.
- [05:15–05:55, 07:05] Efecto del dolly/orbit sobre los anillos: la perspectiva se curva y se ve el túnel de círculos.
- [06:05–06:25] (ampliado en hoja) Capa «Camera 1» → Transform: **Point of Interest 960.0, 540.0, 0.0**; **Position 960.0, 540.0, −2666.7**; **Orientation 0.0°, 0.0°, 0.0°**; X/Y/Z Rotation 0x+0.0°. Debajo, Camera Options.
- [09:15] Menú **Iris Shape**: Fast Rectangle, Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon.
- [09:35] (ampliado) **Camera Options**: **Zoom 2666.7 pixels (39.6° H)**, Depth of Field On, **Focus Distance 2666.7 pixels**, **Aperture 25.3 pixels**, Blur Level 100 %, Iris Shape Fast Rectangle, Iris Rotation 0x+0.0°, Iris Roundness 0.0 %, Iris Aspect Ratio 1.0, Iris Diffraction Fringe 0.0, **Highlight Gain 0.0**, **Highlight Threshold 255**, Highlight Saturation 0.0.
- [09:55–10:15] Menú Layer → Camera: Create Camera from 3D View, Create Stereo 3D Rig, Create Orbit Null, **Link Focus Distance to Point of Interest**, **Link Focus Distance to Layer**, **Set Focus Distance to Layer**, Reset Camera 1.
- [10:35–11:45] Rótulo «CLICK, HOLD, DRAG!» al hacer dolly; keyframes en Position; menú contextual con **Keyframe Assistant** (Easy Ease); la animación acerca la cámara hasta el logo («KASIX CREATIVITY»).
- [11:55] El logo aparece girado boca abajo tras keyframear Z Rotation.
- [12:15] Pantalla final con «Subscribe» (llamada a la acción del canal).

## Cruce teoría ↔ práctica
- Coinciden: el menú de crear cámara, el atajo, las dos clases de cámara, los presets de 15 a 200 mm, las opciones de iris, los tres comandos de enfoque en Layer → Camera y las propiedades de Transform.
- Los mismos 50 mm se ven en **mm** en el diálogo (Zoom 940.74 mm, Focus Distance 940.74 mm; comp de 677.33 mm de ancho) y en **píxeles** en la capa (2666.7 px). Es la misma cámara con otras unidades: la cámara de AE queda a **−2666.7 en Z** de la comp (la capa se ve a escala 100 %).
- El autor dice que lo que se llama «pan» es un tilt; el tooltip lo llama «Pan Camera POI Tool»: no es una contradicción, pero no se demuestra qué cambia.
- Dicho sin mostrar: «50 mm se parece al ojo humano», la relación entre f-stop y bokeh en cámaras reales (explicada con una cámara de película en escena, no con valores de AE) y los efectos exactos de los parámetros Highlight (no los cambia).
- Mostrado sin explicar: Film Size 36 mm, Lock to Zoom, Units y Measure Film Size; Create Orbit Null y Create Stereo 3D Rig aparecen en el menú pero no se usan.
- La parte «Link Focus Distance to Point of Interest» no se prueba en pantalla; sí se prueba la de capa (foco fijo en el logo durante el dolly).

## Receta paso a paso
1. Crea la cámara (Ctrl+Alt+Shift+C): **Two-Node** para orbitar alrededor de un punto; preset (50 mm para empezar; 15–24 mm para plano amplio y más perspectiva; 80–200 mm para plano cerrado y más desenfoque); **marca Enable Depth of Field**; OK.
2. Convierte en 3D (cubo) cada capa que debe reaccionar a la cámara; deja la vista en **Active Camera**. Abre una vista de cuatro paneles cuando necesites ver dónde está la cámara.
3. Muévela con **Orbit/Pan/Dolly** para probar; para un movimiento repetible, activa el cronómetro de **Position** (y Point of Interest si hace falta), cambia en el tiempo y aplica **Easy Ease**; añade **Z Rotation** si quieres giro.
4. Foco: con la capa de cámara seleccionada, Layer → Camera → **Link Focus Distance to Layer** y elige la capa (por ejemplo el logo) para que se mantenga nítida durante el dolly.
5. Desenfoque: sube **Aperture** para más desenfoque, mueve **Focus Distance** para elegir qué queda nítido; **Blur Level 100 %** es el natural. Deja **Iris Shape = Fast Rectangle** para renderizar más rápido y usa otra forma solo cuando quieras bokeh con forma.
6. Si no te gusta algo del diálogo inicial, edita **Camera Options** en la capa: se puede cambiar después.

## Para MUKIWA
- **Motion Graphics Dept.**: una cámara dolly lenta con foco enlazado al logo es una base limpia para presentar el logo MUKIWA o el «I» con el ojo (el punto del I como punto de interés); probar sobre capas 3D con luz azul/lima y fondo negro.
- Para reels 9:16 las medidas del autor son de una comp horizontal; la relación de Zoom (≈ focal × ancho de comp ÷ 36 mm) cambia con el ancho de la comp (a 1920 px y 50 mm da 2666.7 px, como se ve). Es lectura mía, no del video.
- Usa **Aperture/Focus Distance** con moderación para no competir con el tipo: «cada efecto con una razón».
- Complementa la lección de movimientos de cámara reales (dolly vs zoom) del Kiwa de cinematografía.

## Límites
- Subtítulos automáticos; sin cotejo con Whisper. Los valores de los paneles se leyeron en pantalla (3 ampliados: diálogo, Transform y Camera Options).
- Se vieron 7 hojas (un fotograma cada 10 s) y 3 fotogramas ampliados; los 4 paneles de vista y las herramientas de la barra son pequeños.
- No se muestran los atajos de las herramientas de cámara (solo «2, Shift+2» en un tooltip), ni el render final, ni cómo animar Point of Interest, Focus Distance o Aperture con keyframes.
- Versión: AE 2023 (dicho por el autor); en versiones anteriores la UI de vistas cambia.
- Sin medida de rendimiento: «Fast Rectangle renderiza más rápido» es dicho, no medido.
- Lo de «50 mm = ojo humano» es la afirmación del autor.

## Conecta con
- (ninguna lección previa sobre cámara 3D en AE)
