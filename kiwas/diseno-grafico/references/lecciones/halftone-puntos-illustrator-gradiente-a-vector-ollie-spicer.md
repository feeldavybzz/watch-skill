# Halftone en Illustrator: de gradiente a puntos vectoriales sobre un personaje retro (Ollie Spicer)
> Se copia una forma de relleno, se le pone un degradado negro→blanco, Effect > Pixelate > Color Halftone con los 4 canales iguales, se rasteriza a 300 ppi transparente y se vectoriza con Image Trace ignorando el blanco para tener puntos editables.

- **Fuente**: youtu.be/CZVk55d7H5A — "How To Make Halftone Dots With Adobe Illustrator" (Ollie Spicer, 4:41, Illustrator 2024)
- **Fecha**: 2026-10-20
- **Tipo de "oídos"**: transcripción de subtítulos automáticos vistos con la extensión Sider en el Chrome de Bryan (inglés traducido al español, con errores como "half te" por halftone). Más cuadros del video con la interfaz.
- **Confianza**: alta para el flujo y los números (hablados y vistos); media en frases sueltas mal traducidas. El primer tramo (0:00–0:39) se leyó de Sider; lo demás completo.
- **Ojo**: es de **halftone (puntos de trama)**, no de duotone.

## Teoría (lo que dice él)
- Estructura de capas del archivo: abajo el fondo (bloqueado para que no estorbe), arriba el contorno del personaje, en medio el relleno [0:07–0:26].
- El **radio máximo** manda el tamaño de los puntos: más chico = círculos más pequeños. Él usa **8**; con ~18 salen más grandes; "siéntete libre de probar" [1:08–1:56].
- Los **cuatro canales deben tener el mismo número**, para que el efecto funcione (ángulo igual en todos) [0:56–1:04].
- El degradado no tiene que ser exacto al inicio porque el efecto sigue siendo editable: se puede cambiar la dirección con la herramienta de degradado, o el tipo (por ejemplo radial) [0:39, 1:25–1:42].
- Al convertir a vector se pierde un poco de suavidad: bordes ásperos en algunos círculos. Si gusta ese look es una buena técnica [2:56–3:09].
- Alternativa para puntos más suaves: Effect > Document Raster Effects Settings, cambiar 72 ppi a 150 o 300. Con mayor resolución se mantiene lo suave, pero el archivo se puede volver lento [3:09–3:59].

## Práctica (lo que se ve)
1. Selecciona una sección de relleno, copia y pega al frente [0:26]. Es la forma de sombra (un paralelogramo en el costado del cartón).
2. Panel Gradient: degradado blanco y negro [0:32–0:44]. Lineal normal en este diseño [2:01].
3. **Effect > Pixelate > Color Halftone** [0:49]: Max Radius 8, canales en 100 [1:06–1:15].
4. Cuando está bien el efecto: **Object > Rasterize** [2:01–2:09]: RGB, **300 ppi**, fondo **Transparent**, anti-aliasing None, sin clipping mask.
5. **Image Trace** (Object > Image Trace > Make si el botón no se ve) [2:20]: preset por defecto, modo Black and White, threshold 128, paths 50%, corners 75%, noise 25 px, Create Fills, Snap Curves To Lines [2:29–2:36].
6. En el panel de Image Trace, bajar hasta **Ignore Color** y marcarlo para quitar el fondo blanco; luego **Expand** [2:36–2:46].
7. Como ahora es vector, se cambia el color y se edita como cualquier vector [2:46–2:52]; puntos oscuros verdes sobre el lado verde y negros sobre el naranja.
8. Resultado: halftone aplicado en todo el personaje, integrado con la línea gruesa [3:59–4:01].

## Cruce teoría ↔ práctica
- Coinciden: 300 ppi + transparente al rasterizar, Ignore Color + Expand, canales iguales, radio ~8.
- Corrección a una lectura previa solo-visual: el radio era 8 (hablado), no 9. Y subir el ppi sirve para suavizar los puntos, no solo para el rasterizado.
- Mostrado sin explicar: el threshold 128 y los porcentajes del panel de trazado (valores por defecto).

## Receta paso a paso
1. Ten el archivo en 3 capas: fondo bloqueado, relleno, contorno. Trabaja la sombra en una forma copiada del relleno.
2. Rellena la forma con degradado negro→blanco (dirección donde el punto se apaga).
3. Effect > Pixelate > Color Halftone: radio 8, canales 100/100/100/100.
4. Opcional para puntos más suaves: Document Raster Effects Settings a 300 ppi.
5. Object > Rasterize: RGB, 300 ppi, transparente.
6. Image Trace, Ignore Color, Expand.
7. Recolorea los puntos con el tono de sombra de cada zona.

## Para MUKIWA
- Halftone en sombras para la mascota retro, en vector y con colores de marca (puntos en dark #232323 sobre azul #0068FB o sobre lima #C5ED2E; decisión de diseño).
- Sirve para que el estilo se vea impreso y editable en cualquier tamaño; combinable con el halftone/grano que ya prevé la skill `retro-cartoon`.
- Para **duotone** (dos tintas) falta otro video: este solo cubre puntos.
- Departamento: Graphic Design.

## Límites
- Subtítulos automáticos traducidos: algunas frases tienen palabras mal traducidas.
- No cubre duotone ni halftone en Photoshop.
- Las pruebas de radio (8 vs 18) las dice de palabra; solo se vio el 8 en pantalla.

## Conecta con
- [[rubber-hose-desde-cero-cuerpos-ojos-manos-zapatos-poses-julina-mae]]
