---
name: kiwa-efectos-visuales
description: "Kiwa de efectos visuales: distingue y combina SFX, VFX y CGI, y planea cada efecto desde el guion hasta igualar luz y cámara."
metadata:
  nicho: efectos-visuales
  herramientas: "Croma (pantalla verde), Composición, Pantalla LED (producción virtual), Pre-vis"
  lecciones: 2
  actualizado: "2026-10-28"
---

# Kiwa · Efectos visuales
> Decide y planea cada efecto con el vocabulario correcto: qué se hace en el set (SFX), qué se añade a lo filmado (VFX) y qué se crea entero en digital (CGI), quién se encarga y cómo combinarlos sin costuras. Hoy domina las definiciones, las técnicas y el flujo de planeación; falta aprender la ejecución en software (composición, croma, rotoscopia) con pasos y valores. Tiene **1 lección propia** [1] y **3 complementarias** de cine real ([2] soportes, [3] iluminación, [4] composición).

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Para animar o componer gráficos en software, combínalo con `kiwa-motion-graphics`; para el montaje, con `kiwa-editor-asistente`.

## Cómo trabajar (cualquier efecto)
1. **Desglosa el guion** marcando cada efecto visual o especial [1].
2. **Clasifica cada efecto** con las tres categorías (tabla de abajo) antes de decidir cómo hacerlo [1].
3. **Haz el storyboard** de la secuencia y compártelo con los supervisores de efectos (SFX y VFX) [1].
4. Si habrá CGI, **planea con pre-vis** de baja resolución y define con el departamento de arte cómo se verá [1].
5. **Combina lo práctico y lo digital** según lo que gane el plano; el CGI debe **igualar la luz y el aspecto** de lo real [1].
6. **Seguridad primero** en todo lo que se hace en el set: la tarea principal del supervisor de SFX es que se haga de forma responsable y segura [1].

## Áreas
### Las tres categorías
| | Qué es | Ejemplos |
|---|---|---|
| **SFX (efectos especiales)** | Elementos **creados físicamente en el set**; hoy sobre todo **mecánicos o prácticos** | lluvia falsa, niebla con máquina, pirotecnia (explosiones y fuego controlados), animatrónica, maquillaje protésico [1] |
| **VFX (efectos visuales)** | Efectos **añadidos a las imágenes captadas** durante la producción; pueden incluir CGI pero abarcan más técnicas | composición, croma, borrado de objetos, rotoscopia, producción virtual, stitching, exposiciones múltiples, perspectiva forzada, impresora óptica [1] |
| **CGI** | Elemento visual **creado solo de forma digital** (ciudades, vehículos, personajes enteros) | WALL·E (plano 100 % CGI); Paddington 2 (personaje CGI en un cuadro real) [1] |
- «**Sin CGI**» no significa «sin VFX digitales»: puede haber muchos VFX que no son generados por computadora [1].
- **RoboCop**: un objeto de stop-motion compuesto sobre planos reales con una impresora óptica es VFX **y no es CGI** [1].

### Efectos especiales (SFX)
- **Mecánicos o prácticos**: atmosféricos (lluvia, niebla), pirotecnia (explosiones y fuego **controlados**), animatrónica, maquillaje protésico [1].
- **Supervisor de efectos especiales**: diseña junto con el director, los diseñadores de producción y los especialistas; su tarea principal es la seguridad [1].
- Suelen **subcontratarse** a empresas especializadas [1].

### Efectos visuales (VFX)
- **Composición (compositing)**: combinar dos o más imágenes en un plano [1].
- **Croma verde o azul (chroma key)**: quita elementos del metraje; el fondo se reemplaza por una toma real o un paisaje de CGI [1].
- **Producción virtual**: una **pantalla LED** da un fondo que se mueve respecto a la cámara (renderizado en tiempo real y motores de juego); exige trabajo de VFX **antes de rodar** (el fondo interactivo) y a veces después [1].
- **Borrado de objetos (paint-out)** [1]. **Captura de pantalla** [1].
- **Rotoscopia**: antes la hacían animadores dibujando sobre metraje de referencia; hoy una computadora proyecta imágenes sobre el metraje [1].
- **Stitching**: unir dos tomas para que parezcan una continua; no es posible con actores en cuadro, así que se **compone una toma aparte** con ellos [1].
- **Supervisor de VFX**: dirige todo el *pipeline* y debe estar en preproducción y en el set para que el material sea utilizable (en *Oppenheimer* leyó el guion entre los primeros) [1].

### CGI
- **Departamentos**: **arte** (define cómo deben verse los elementos digitales), **pre-vis** (gráficos de baja resolución para planear), **simulación de FX** (la física de agua, pelo y fuego), **iluminación** (igualar la luz del plano real), **assets** (modelos, texturas y shaders) y **investigación y desarrollo** (el software) [1].
- **Flujo del CGI** (guía escrita): modelado 3D, texturizado, rigging y animación; además composición y matte painting [1].
- Hacerlo creíble requiere mucho trabajo; puede ser épico o un retoque sutil [1].

### Combinar los tres (caso *1917*, choque del avión)
- Para que parezca **un solo plano**: aviones **CGI** en el cielo → transición (stitch) a un **avión real** construido y lanzado desde una rampa a **20 pies** de altura → toma aparte con los actores compuesta sobre ese metraje → otra toma con el avión práctico en locación y un **avión y un granero digitales idénticos** a los que ardían en el set; escenas de estudios distintos (Shepperton y Glasgow) mezcladas sin costuras [1].
- Reparto: **CGI** (avión y granero), **VFX** (stitching y composición) y **SFX** (pirotecnia y efectos mecánicos del avión) [1].

### Rodar pensando en el VFX: cámara, luz y cuadro [2][3][4]
(Salen de lecciones de cine real; no son pasos de software.)
- **Control de movimiento (motion control)**: dispositivo con control total y repetición precisa del movimiento; hoy su uso más común es VFX, con **dos tomas del mismo movimiento y encuadre** que se combinan después (*La red social*: los gemelos Winklevoss) [2]. Si piensas componer dos tomas, planea desde el rodaje que la cámara repita el movimiento [2].
- **Soporte según el efecto**: en la lección aparece una cámara en grúa frente a una pantalla verde como ejemplo de detrás de cámaras [2]; qué soporte conviene para croma no se dice (el video no lo cubre).
- **Igualar la luz** (ya en [1]): usa el vocabulario de [3] para describir el plano real y pedirlo al departamento de iluminación de CGI: clave alta o baja, luz dura o suave, lado ciego o corto y temperatura (≈3 200 K tungsteno, ≈5 600 K día) [3]. Que el CGI use esos mismos valores es aplicación mía, ≈.
- **Integración visual del plano** [4]: el CGI debe respetar la **profundidad** (primer plano, plano medio y fondo; foco corto o profundo), el **tono** (el ojo va a lo más brillante) y el **color** del plano real para no parecer pegado [4] (aplicación mía a VFX, ≈).
- **Encuadre del elemento digital**: colócalo con los mismos criterios de composición (puntos focales, equilibrio, espacio negativo) que el resto del cuadro [4].

### «Endless zoom» (portal dentro del portal) en DaVinci Resolve [5]
- Rodaje: trípode fijo, foco manual y un papel verde en el marco que será el portal de la siguiente toma. Fusion: quitar el verde con Delta Keyer + máscara; cortar los clips a la misma duración y apilarlos en un Fusion Clip; cada clip → Image Plane 3D → mismo Merge 3D → Renderer 3D → MediaOut, con Camera 3D al mismo Merge; empujar las capas atrás en Z; animar la cámara 3D con spline suave y activar Render Cache. Se cuentan 8 clips en el árbol.

## Por herramienta
### Croma (pantalla verde o azul)
- Sin fuentes todavía (iluminación del fondo, recorte, spill).

### Composición (software)
- Sin fuentes todavía (After Effects, Nuke, DaVinci Fusion).

### Pantalla LED (producción virtual)
- Fondo que se mueve en relación con la cámara; requiere preparar el fondo antes del rodaje [1].

### Pre-vis
- Gráficos de baja resolución para planear escenas y que el director y el equipo vean el resultado final [1].

## Errores comunes
- Usar «CGI» como sinónimo de todo → es solo lo creado enteramente en digital; el resto son otros VFX o SFX [1].
- Decir «sin CGI» y olvidar los VFX digitales que sí hay → pueden ser muchos [1].
- Dejar los efectos para postproducción sin planear → desglosa el guion, haz storyboard y comparte con los supervisores antes de rodar [1].
- Un supervisor de VFX ausente del set → el metraje puede no servir [1].
- CGI que no iguala la luz del plano real → no se integra [1][3].
- Componer dos tomas sin haber repetido el movimiento de cámara → no encajan; planea motion control si hace falta [2].

## Checklist antes de entregar
- [ ] Guion desglosado por efectos y cada efecto clasificado (SFX, VFX o CGI).
- [ ] Storyboard compartido con los supervisores.
- [ ] Pre-vis hecha para lo que sea CGI.
- [ ] Seguridad de los efectos de set aprobada por el supervisor de SFX.
- [ ] Luz y aspecto de los elementos digitales igualados con los reales (temperatura, dureza, dirección) [1][3].
- [ ] Si hay dos tomas que se combinan: movimiento y encuadre repetidos [2].

## Para MUKIWA
- Visual Edits / Creative Direction: usar la clasificación SFX/VFX/CGI en briefs y cotizaciones (qué se resuelve en rodaje y qué en post).
- Motion graphics: composición, croma, rotoscopia y borrado se hacen en software; los pasos aún no están aprendidos.

## Dudas abiertas
- **Definiciones en conflicto**: el video separa SFX (en el set) de VFX (añadido después) y dice que el VFX *puede incluir* CGI [1]; la guía escrita del mismo creador dice que **VFX es la categoría madre que incluye CGI y SFX** [1 (guía escrita)]. Aquí se usa la del video.
- Faltan los pasos de ejecución en software, y valores (costos, tiempos).
- [2][3][4] son de cine real y no hablan de software de VFX; la aplicación al CGI es mía y no está probada.
- La guía escrita no habla de supervisores, croma, rotoscopia, stitching ni producción virtual.
- [5] No hay voz y faltan los números: distancias en Z, keyframes de cámara y cuántas tomas por segundo; el texto de los nodos se lee a baja resolución.

## Fuentes
- [1] CGI vs VFX vs SFX: qué es cada uno y cómo se combinan (StudioBinder, con Ian Failes) — https://youtu.be/Pok6EN3cfA4 · guía escrita https://www.studiobinder.com/blog/vfx-vs-cgi-vs-sfx-definitions/ · `references/lecciones/cgi-vfx-sfx-diferencias-y-1917.md`
- [2] Los 12 soportes de cámara (StudioBinder, ep. 5) — https://youtu.be/heJ9hWNb10g · `references/lecciones/soportes-de-camara-12-rigs-studiobinder.md`
- [3] Iluminación de cine, parte 1 (StudioBinder, ep. 12) — https://youtu.be/r2nD_knsNrc · `references/lecciones/iluminacion-cine-parte-1-tipos-terminos-equipo-studiobinder.md`
- [4] Los 9 elementos de la composición en cine (StudioBinder, ep. 11) — https://youtu.be/hUmZldt0DTg · `references/lecciones/nueve-elementos-composicion-cine-studiobinder.md`
- [5] «Endless zoom» en DaVinci Resolve: portal de papel verde + Fusion 3D (@melikazaghari) — reel de Instagram, archivo local · `references/lecciones/endless-zoom-fusion-davinci-melikazaghari.md`
