---
name: kiwa-color-grading
description: Profesor MUKIWA de color grading en DaVinci Resolve, con rodaje y grade de S-Log3 de Sony (CST), aislar colores, proteger piel, LUTs y look MUKIWA.
metadata:
  nicho: color-grading
  herramientas: "DaVinci Resolve, Premiere Pro"
  lecciones: 1
  actualizado: "2026-10-15"
---

# Kiwa · Color grading (DaVinci Resolve)
> Arma el grade como un árbol de nodos ordenado y con nombres, envuelto entre un CST de entrada y uno de salida cuando el material es log; aísla un color o un objeto sin ensuciar la piel, y baja o cambia solo ese verde, rojo o azul con Qualifier, Magic Mask y curvas. Tiene **1 lección en video** [4] (rodaje y grade de S-Log3 de Sony); lo demás sigue siendo conocimiento general de Resolve y la captura de Bryan, así que esos números son puntos de partida (≈), no valores probados.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez; la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron en pantalla o se dijeron; si no, con ≈. Para la luz de la escena combínalo con `kiwa-iluminacion`; para el encuadre, con `kiwa-composicion-visual`.

## Cómo trabajar (cualquier clip)
1. **Sabe qué cámara y qué gamma es.** Si el material es log (S-Log3), el primer paso es convertirlo con un CST (ver «Material log»); si ya es Rec.709, no hace falta [4].
2. **Mira los scopes antes de tocar nada.** El vectorscopio muestra dónde está la piel (línea de piel, entre R y Y) y qué color domina; es la referencia para saber si estás ensuciando a la persona [1].
3. **Ordena los nodos de izquierda a derecha y ponles nombre** (clic derecho en el nodo → *Node Label*). Un nodo = un trabajo [2].
4. **Primero corrige, luego da estilo.** Exposición y balance primero; el look al final. Si el look va primero, los aislamientos reaccionan distinto en cada plano.
5. **Aísla en nodos propios.** Cada aislamiento (verdes, palmera, piel) va en su nodo, para poder apagarlo con Ctrl/Cmd+D y comparar.
6. **Comprueba el aislamiento con Highlight** antes de oscurecer o cambiar nada: si se ilumina la piel, el rango está mal.
7. **Revisa el resultado en 2-3 planos distintos** de la misma escena; un qualifier que funciona en un plano suele fallar en otro.
8. **Guarda el look con Grab Still** y aplícalo a los demás planos desde la galería [4].

## Áreas
### Rodar para gradear: S-Log3 en Sony [4]
Configuración que usa Gaku Lange en una Sony ZV-E1 (dice que es igual en su FX3). Solo vale para Sony; en otra marca cambia el perfil.
- **Picture Profile PP1**: gamma **S-Log3** y color mode **S-Gamut3.Cine**; lo demás en estándar.
- **Formato**: XAVC S 4K (cree que «SI 4K» es más alto, no lo asegura), 30 fps (también 24 o 60) y **4:2:2 10-bit**, que es lo que da el máximo rango y color.
- **Gamma Display Assist ON** (Menu → Setup → Display Option): el visor muestra una Rec.709 para exponer; es solo ayuda de pantalla. Sin él, S-Log3 se ve gris.
- **Exposición**: el medidor del visor va de −2 a +2; él sobreexpone de **+1.7 a +2**, lo más alto posible **sin quemar las altas luces importantes**. Subexponer S-Log3 te quita calidad al levantar sombras en post.
- **Zebras ON** (Menu → Exposure/Color → Zebra): lo que tiene zebra se perdió. El cielo puede quemarse. En post se baja la exposición.
- Probar en la cámara de Bryan antes de copiar el «+1.7 a +2»: no se dijo el ISO base ni el nivel de zebra [4].

### Material log: Color Space Transform (CST) [4]
**Estructura mínima de 3 nodos** (visto en pantalla): **01 → 02 → 03**.
| Nodo | Nombre propuesto | Qué hace |
|---|---|---|
| 01 | `CST · ENTRADA` | Input Color Space **Sony S-Gamut3.Cine**, input gamma **S-Log3**; salida **DaVinci Wide Gamut / DaVinci Intermediate** |
| 02 | `GRADE · WIDE GAMUT` | Exposición, color, estilo. Todo el trabajo va aquí |
| 03 | `CST · SALIDA` | De DaVinci Wide Gamut / Intermediate a **Rec.709**, gamma «Rec.709-A» (dicho en audio, no confirmado en pantalla) |
- En el frame del nodo 01 se ve *Tone Mapping Method = DaVinci*, *Adaptation 9.00* y *Gamut Mapping = None*; el autor no los comenta.
- Los nodos de aislamiento de abajo (verdes, palmera, piel, look) van **entre el CST de entrada y el de salida**, nunca antes del primero ni después del último (aplicación mía, ≈).

### Árbol de nodos recomendado (nombres para etiquetar)
Estructura que Bryan ya usa en CULTURA ANUNCIO (nodos 01–08 con un Layer Mixer) [1], puesta en orden y con nombres. Si el material es log, va entre los dos CST:

| Nodo | Nombre | Qué hace |
|---|---|---|
| 01 | `BASE · CORRECCIÓN` | Exposición, balance de blancos, contraste general |
| 02 | `VERDES · QUALIFIER` | Aísla todos los verdes (hojas, plantas) |
| 03 | `PALMERA · MAGIC MASK` | Separa la palmera del resto de verdes |
| 05 | `PALMERA · VERDE OSCURO` | Oscurece y profundiza solo la palmera |
| 06 | `PIEL · PROTEGER` | Qualifier de piel para que no se contamine con el verde |
| 07 | `LOOK · MUKIWA` | Azul en sombras, toque lima en luces, contraste |
| 08 | `OUTPUT · FINAL` | Salida final (con material log, es el `CST · SALIDA`) |

Los números salen de la captura de Bryan; el orden y los nombres son propuesta mía [1][2].

### Grade de un clip log, paso a paso (flujo de [4])
Lo que hace Gaku Lange en su nodo de grade; los valores son los que dijo, el resto de su PowerGrade (de pago) no se vio nodo por nodo.
1. **Denoise espacial** antes del CST, solo si hay ruido (nocturno).
2. **Exposición** (HDR wheels): baja un poco **global** y **lights** para compensar la sobreexposición del rodaje.
3. **Balance de blancos**: si el clip es azul, calienta «ever so slightly».
4. **Sombras y luces**: curva con **3 puntos enlazados**; baja un poco las sombras y sube un poco el punto izquierdo → roll-off más «filmic». Mueve un poco las altas luces a la izquierda.
5. **HSV**: sube el **gain** → más densidad y saturación solo en las luces («punch»).
6. **Piel y colores** (Color Slice): piel oversaturada → baja **saturación** y un poco la **densidad**; azules y cianes → sube saturación; si quieres teal, mueve el **hue del azul** a la derecha.
7. **Grano, gate weave y polvo** apagados si no quieres look de película.
8. **LUT de acabado** (tiene 7: vintage, overcast, outdoors…): bájale el **Key Output Gain** a **0.28** y luego a **0.1** para que sea sutil. Eligió «outdoors» a 0.1.
9. **Viñeta**: nodo con **Radial Blur** + máscara circular, feather, **invertida**, centrada; fuerza **0.29 → 0.25**.
10. **Grab Still** y reutiliza en otros planos.

### Aislar y oscurecer un verde (ejemplo: solo la palmera)
La palmera y las otras plantas son del mismo verde, así que el Qualifier solo no las separa. Hay que **cruzar dos cosas**: el color (Qualifier) y la forma (máscara) [2].

1. **Un solo nodo `PALMERA · VERDE OSCURO`.** Dentro de él: Qualifier HSL + Magic Mask (o Power Window) a la vez. En Resolve, la máscara y el Qualifier del mismo nodo se **multiplican**: solo cambia lo que es verde **y** está dentro de la máscara [2]. Es más simple y estable que cruzar dos nodos con un Layer Mixer.
2. **Qualifier**: con el cuentagotas sobre una hoja, ajusta *Hue* (franja de verdes; en la escala 0–100 de Resolve el verde cae ≈ entre 30 y 40, confírmalo con el cuentagotas y no con este número), sube *Softness* y activa Highlight para comprobar [2].
3. **Magic Mask** (Resolve Studio): modo *Object*, un trazo sobre las hojas de la palmera, *Track Forward/Backward*; revisa el seguimiento en todo el plano y corrige fotogramas donde se escape [2].
4. **Oscurecer**: baja *Gamma* (y un poco *Gain*) en las ruedas; el verde oscuro se ve profundo si **mantienes o subes algo la saturación** en vez de bajarla [2].
5. **Desplazar el tono** (opcional): en Hue vs Hue, mover el punto del verde hacia el verde-azulado con *Hue Rotate* ≈ −5 a −10 da un verde más esmeralda [2]. Bryan ya tenía puntos en el verde-amarillo con *Hue Rotate* −2.40 [1].
6. **Suavizar el borde**: *Blur Radius* en el Qualifier (≈ 1–3) si la máscara se ve dura [2].

### Proteger la piel
- Nodo `PIEL · PROTEGER` después de los aislamientos de verde: Qualifier de piel y, si hace falta, bajar saturación o corregir el matiz en esa zona para quitar rebote verde [2]. En [4] la piel se corrige con *Color Slice → Skin*: bajar saturación y un poco la densidad.
- Regla de oro: **la piel manda**. Si al cambiar el verde la piel se mueve en el vectorscopio, el aislamiento está mal [1][2].

### Curvas por color (Hue vs Hue / Sat / Lum)
- **Hue vs Hue**: cambia el matiz de un color sin tocar los demás. Fija puntos a ambos lados del color para que el cambio no se escape a los vecinos [1][2].
- **Hue vs Sat**: sube o baja la saturación de un solo color.
- **Hue vs Lum**: aclara u oscurece un solo color; útil como ajuste fino después del Qualifier [2].
- En la captura de Bryan la curva Hue vs Hue tiene cuatro puntos fijados en la zona amarillo-verde, con *Hue Rotate* −2.40 [1].

### Look MUKIWA
- Base negra con **azul eléctrico #0068FB** en sombras y un toque de **lima #C5ED2E** en luces o en un solo color de acento; el morado solo como acento atmosférico. Esto sale de la paleta de marca de Bryan, no de un tutorial [3].
- Guardar el look en su propio nodo (`LOOK · MUKIWA`) y copiarlo entre planos con *Grab Still* + *Apply Grade* [4], o como PowerGrade.

## Por herramienta
### DaVinci Resolve (página Color)
- Nodos: Alt+S = nuevo nodo serie; Alt+P = paralelo; Alt+L = capa (*Layer*); Ctrl/Cmd+D = activar/desactivar nodo [2].
- Scopes: Vectorscopio (color y piel), Waveform (exposición), Parade (balance RGB) [1][2].
- Magic Mask solo existe en **Resolve Studio**; Bryan tiene Studio 21 [1][4].
- **Color Space Transform**: búscalo en Effects (en [4] se busca «color s»); se aplica como un nodo [4].
- **HDR wheels** (Dark / Shadow / Light / Global) y **Color Slice** (Red, Skin, Yellow, Green, Cyan, Blue, Magenta) son los paneles que usa [4].

### LUTs
- Un LUT puede ir **al principio** (para convertir de log a Rec.709) o **al final** (como look), nunca en medio [2]. Con la gestión de color por CST de [4], el LUT va como **acabado suave**: baja su ganancia de salida a ≈ 0.1–0.28 para que no mande sobre tu grade.
- Bryan tiene un paquete `luts.zip` en Descargas; no se ha abierto ni analizado todavía.

## Recetas
(Mezcla de [4] con conocimiento general de Resolve [1][2]; lo que no sale de [4] no está probado en el proyecto de Bryan.)
- **Clip S-Log3 de cero**: CST entrada → exposición baja → WB → curvas de sombras/luces → HSV gain → piel y azules en Color Slice → LUT suave → CST salida [4].
- **Solo una planta o palmera, verde oscuro**: nodo único con Qualifier de verdes + Magic Mask, bajar Gamma, mantener saturación, Hue Rotate ≈ −5 [2].
- **Quitar el rebote verde de la piel**: nodo `PIEL · PROTEGER` con Qualifier de piel, bajar saturación del verde y corregir matiz [2].
- **Dar un look de marca**: azul en sombras, lima en luces, contraste con curva en S suave.
- **Comparar antes/después**: Ctrl/Cmd+D en el nodo, o *Split Screen* con un still.

## Errores comunes
- Rodar S-Log3 subexpuesto → al levantar sombras en post pierdes calidad [4].
- Quemar las altas luces importantes por sobreexponer sin zebras [4].
- Olvidar el CST de entrada (el clip se ve gris) o poner uno de salida distinto al del timeline [4].
- Poner nodos de grade antes del primer CST o después del último → el grade se aplica en el espacio equivocado.
- Subir *Softness* poco → el borde de la máscara «parpadea» en movimiento; súbelo y revisa en reproducción.
- Aislar con el Qualifier sin comprobar con Highlight → se cambia la piel o el fondo sin querer.
- Fiarse de un solo plano → la luz cambia y el Qualifier falla; prueba en varios planos de la escena.
- Bajar saturación para «oscurecer» un verde → queda apagado; mejor bajar Gamma y mantener saturación.
- LUT a ganancia 1.0 sobre un grade ya hecho → se come tu trabajo; bájalo [4].
- Nodos sin nombre → nadie entiende el grade; etiquétalos.

## Checklist antes de entregar
- [ ] Si es log: CST de entrada y de salida puestos, y el grade entre los dos.
- [ ] Vectorscopio revisado: la piel sigue en su línea.
- [ ] Cada aislamiento tiene su nodo con nombre.
- [ ] Magic Mask o Power Window revisados en todo el plano (sin fugas).
- [ ] Highlight comprobado en al menos 2-3 planos.
- [ ] LUT de acabado con ganancia baja, no al 100 %.
- [ ] Look final guardado con Grab Still para los demás planos.
- [ ] Probado en reproducción, no solo en un fotograma.

## Para MUKIWA
- Visual Edits: usar el árbol propuesto como plantilla en cada proyecto y guardarlo como PowerGrade para reusarlo. Si la cámara es Sony en S-Log3, usar la estructura CST entrada / grade / CST salida.
- Rodaje de MUKIWA: si se graba en S-Log3, sobreexponer con zebras (≈ +1.7 a +2 en el medidor de una Sony, a probar en la cámara de Bryan) y activar Gamma Display Assist [4].
- Creative Direction: traducir «verde profundo, lujoso» → verde oscuro con saturación alta; «frescura» → verde más claro y amarillento.
- Graphic Design: la paleta #232323 / #0068FB / #C5ED2E sirve igual como referencia de color para el grade.

## Dudas abiertas
- [4] es un creador que vende su PowerGrade, LUTs y curso: los valores del grade (curvas, gain de HSV, saturaciones) **no se vieron en pantalla**; solo valen los números que dijo (+1.7/+2, 0.28, 0.1, 0.29, 0.25).
- Gamma de salida «Rec.709-A»: se oye en el audio y no se confirmó en pantalla.
- Ninguna fuente dice el ISO base ni el nivel de zebra; el «+1.7 a +2» depende de cómo lea el medidor cada cámara.
- Los valores de hue, gamma y blur de la receta de la palmera siguen siendo puntos de partida (≈), sin validar en el proyecto de Bryan.
- No se leyeron los parámetros reales de los nodos de Bryan (solo se ve el árbol y la curva Hue vs Hue en la captura).
- `luts.zip` y la carpeta `Color Grading LLC/CineDream` (vacía) no aportan todavía material.
- Falta aprender: ACES y otros flujos de color management, HDR, matching de planos y de cámaras, y grading de log de otras marcas (Canon, Panasonic, Blackmagic).

## Fuentes
- [1] Captura de la página Color de DaVinci Resolve Studio 21, proyecto «CULTURA ANUNCIO», timeline «VIDEO 2 CAPSULA» (Bryan, 2026-10-15).
- [2] Conocimiento general de DaVinci Resolve (Claude); no viene de un video analizado.
- [3] Paleta y dirección de marca MUKIWA DEPARTMENT (preferencias de Bryan).
- [4] Cómo rodar y gradear S-Log3 bien: cámara Sony, exposición con zebras, CST y grade en Resolve (Gaku Lange) — https://www.youtube.com/watch?v=0GBqqfMjPuQ · `references/lecciones/s-log3-rodaje-y-grade-en-resolve-gaku-lange.md`