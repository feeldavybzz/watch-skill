---
name: kiwa-color-grading
description: Kiwa de color grading en DaVinci Resolve: ajustes de proyecto y CST, rodaje y grade de S-Log3 de Sony, exposición y balance con scopes, saturación HSV, LUTs, máscaras, matching de planos con PowerGrades, aislar colores, proteger piel y look MUKIWA.
metadata:
  nicho: color-grading
  herramientas: "DaVinci Resolve, Premiere Pro"
  lecciones: 2
  actualizado: "2026-10-30"
---

# Kiwa · Color grading (DaVinci Resolve)
> Arma el grade como un árbol de nodos ordenado y con nombres, envuelto entre un CST de entrada y uno de salida cuando el material es log; aísla un color o un objeto sin ensuciar la piel, y baja o cambia solo ese verde, rojo o azul con Qualifier, Magic Mask y curvas. Tiene **2 lecciones en video**: [4] rodaje y grade de S-Log3 de Sony y [5] el sistema completo de Resolve (proyecto, CST, 4 nodos, scopes, HSV, LUT, máscaras y matching); lo demás sigue siendo conocimiento general de Resolve y la captura de Bryan, así que esos números son puntos de partida (≈), no valores probados.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez; la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron en pantalla o se dijeron; si no, con ≈. Para la luz de la escena combínalo con `kiwa-iluminacion`; para el encuadre, con `kiwa-composicion-visual`.

## Cómo trabajar (cualquier clip)
1. **Sabe qué cámara y qué gamma es.** Si el material es log (S-Log3), el primer paso es convertirlo con un CST (ver «Material log»); si ya es Rec.709, no hace falta [4].
2. **Mira los scopes antes de tocar nada.** El vectorscopio muestra dónde está la piel (línea de piel, entre R y Y) y qué color domina; es la referencia para saber si estás ensuciando a la persona [1]. Waveform en luminancia (0–100) para exponer y en RGB para balancear [5].
3. **Ordena los nodos de izquierda a derecha y ponles nombre** (clic derecho en el nodo → *Node Label*). Un nodo = un trabajo [2].
4. **Primero corrige, luego da estilo.** Orden fijo: **la luz, luego el color y luego la intención** (exposición → balance → contraste → saturación → LUT → máscaras) [5]. Si el look va primero, los aislamientos reaccionan distinto en cada plano.
5. **Aísla en nodos propios.** Cada aislamiento (verdes, palmera, piel) va en su nodo, para poder apagarlo con Ctrl/Cmd+D y comparar.
6. **Comprueba el aislamiento con Highlight** antes de oscurecer o cambiar nada: si se ilumina la piel, el rango está mal.
7. **Revisa el resultado en 2-3 planos distintos** de la misma escena; un qualifier que funciona en un plano suele fallar en otro.
8. **Guarda el look con Grab Still** (PowerGrade) y aplícalo a los demás planos desde la galería con Apply Grade o clic con la rueda del ratón [4][5]. Luego ajusta cada plano: exposición, balance y por último lo fino [5].

## Áreas
### Rodar para gradear: S-Log3 en Sony [4]
Configuración que usa Gaku Lange en una Sony ZV-E1 (dice que es igual en su FX3). Solo vale para Sony; en otra marca cambia el perfil.
- **Picture Profile PP1**: gamma **S-Log3** y color mode **S-Gamut3.Cine**; lo demás en estándar.
- **Formato**: XAVC S 4K (cree que «SI 4K» es más alto, no lo asegura), 30 fps (también 24 o 60) y **4:2:2 10-bit**, que es lo que da el máximo rango y color.
- **Gamma Display Assist ON** (Menu → Setup → Display Option): el visor muestra una Rec.709 para exponer; es solo ayuda de pantalla. Sin él, S-Log3 se ve gris.
- **Exposición**: el medidor del visor va de −2 a +2; él sobreexpone de **+1.7 a +2**, lo más alto posible **sin quemar las altas luces importantes**. Subexponer S-Log3 te quita calidad al levantar sombras en post.
- **Zebras ON** (Menu → Exposure/Color → Zebra): lo que tiene zebra se perdió. El cielo puede quemarse. En post se baja la exposición.
- Probar en la cámara de Bryan antes de copiar el «+1.7 a +2»: no se dijo el ISO base ni el nivel de zebra [4].

### Ajustes de proyecto (una sola vez) [5]
Visto en pantalla en Resolve Studio 20: engranaje abajo a la derecha → **Color Management**.
- **Color science**: DaVinci YRGB. **Timeline color space**: **DaVinci Wide Gamut / Intermediate** (en vez de Rec.709): da margen para empujar exposición, contraste y color sin que la imagen se rompa. Demostrado: con el timeline en Rec.709 al subir la exposición se pierden altas luces y fondo; en Wide Gamut se recuperan.
- **Output color space**: **Rec.709 Gamma 2.2** para YouTube, redes y web; **Gamma 2.4** para broadcast/televisión; **en Mac, Rec.709-A** (la opción existe en la lista de Resolve, vista en pantalla) porque en Mac el video exportado no se ve igual que en Resolve.
- Solo Mac: Preferencias → Sistema → General → activar *Use Mac Display Color Profiles for viewers*.
- Tres puntos → *Set current settings as default* → Update: no hay que repetirlo en cada proyecto.
- Contexto: lo dice un creador (Windows); lo de Mac, «Rec.709-A», coincide con lo que dijo [4] en audio (ver Dudas).

### Material log: Color Space Transform (CST) [4][5]
**Estructura mínima de 3 nodos** (visto en pantalla): **01 → 02 → 03**.
| Nodo | Nombre propuesto | Qué hace |
|---|---|---|
| 01 | `CST · ENTRADA` | Input Color Space **Sony S-Gamut3.Cine**, input gamma **S-Log3**; salida **DaVinci Wide Gamut / DaVinci Intermediate** |
| 02 | `GRADE · WIDE GAMUT` | Exposición, color, estilo. Todo el trabajo va aquí |
| 03 | `CST · SALIDA` | De DaVinci Wide Gamut / Intermediate a **Rec.709**, gamma «Rec.709-A» (dicho en audio, no confirmado en pantalla) |
- Con cámara Sony FX30 [5] pone igual: CST IN = S-Gamut3.Cine / S-Log3 → DaVinci Wide Gamut / DaVinci Intermediate; CST OUT = DaVinci Wide Gamut / Intermediate → **Rec.709**, gamma **2.2 o 2.4 según el destino** (o 709-A en Mac). Dos nodos en serie con Alt+S, nombrados **CST IN** y **CST OUT**; efecto *Color Space Transform* desde Library → Effects. Si el material ya es Rec.709, no hace falta.
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

**Cadena base de [5]** (vista en pantalla, nodos 01–07): `CST IN → EXP → WB → CONTRAST → SAT → CST OUT → LUT`. Entre los CST van **cuatro nodos con nombre y en ese orden**: **EXP** (exposición), **WB** (balance de blancos), **CONTRAST**, **SAT** (saturación). El LUT va **después** del CST OUT, en su propio nodo; las máscaras (nodos paralelos) se meten antes del CST OUT. Para MUKIWA el árbol de la tabla de arriba (BASE, VERDES, PALMERA, PIEL, LOOK) puede ir **dentro** de esta cadena; unir los dos es propuesta mía, no probada.
- Etiquetar rápido: *Resolve → Keyboard Customization* → buscar «node label» → asignar una tecla (él usa **R**) y escribir el nombre sobre el nodo [5].

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

### Exponer con scopes [5]
- Exposición con las **HDR wheels → Global** («se comporta como el ISO de una cámara»); luego se afina sombras y luces con lift, gamma y gain, o con *Dark / Shadow / Light* de las HDR wheels. Ruedas normales: offset = exposición global, gain = altas luces, gamma = tonos medios, lift = sombras.
- **Waveform en luminancia**: ajustes → modo **Y** (sin *colorize*) → tres puntos → *Display Qualifier Focus* activado y escala en **porcentaje** (0–100). Con el Qualifier encima de una zona, un círculo en la waveform marca su valor exacto (cielo, árbol, pelo).
- 0 es negro absoluto y 100 blanco absoluto; por encima de 100 clipea y si todo se aplasta en 0 se pierden sombras. **El contexto manda**: un plano nocturno puede vivir cerca de 0 y uno a contraluz clipear arriba. Referencia que dijo: el **cielo en ≈ 80 es aceptable y mejor en 60–70**. «No buscamos números perfectos, buscamos una imagen coherente.»

### Balance de blancos [5]
- Referencia: **la piel** (la mejor, si se ve) o **un neutro** (negro, gris o blanco). Ejemplo: el negro del pelo.
- **Waveform en RGB con colorize**: sobre el negro, las tres «bolitas» (R, G, B) deben quedar **en el mismo sitio** formando una redonda. Se corrige con la **rueda de offset** (restar o sumar el color que sobra; «no mucho»).
- Si el fondo tiene un color fuerte (por ejemplo algo rojo), no quitar rojo global: aísla a la persona.
- **Vectorscopio**: activar *Show Skin Tone Indicator*; la piel debe quedar lo más cerca posible de esa línea. Zoom: **Alt + rueda del ratón**.

### Contraste y saturación [5]
- **Contraste**: slider **Contrast** + **Pivot**. **Pivot 0 → afecta más a las altas luces; Pivot 1 → más a las sombras.** Solo un toque: demasiado se ve artificial.
- **Saturación sin reventar**: nunca el slider de saturación a tope (revienta todo y mezcla colores). En el nodo **SAT** clic derecho → **Color Space → HSV**, luego **Channels** y quita el primer y el tercer canal, dejando **solo Saturación**. Empuja con la rueda de **gamma**: sube saturación en las partes **menos** saturadas y protege las más saturadas (la piel).

### Máscaras (Power Windows) y nodo paralelo [5]
- Sirven para oscurecer bordes, iluminar al sujeto y reducir distracciones. Nodo propio con nombre (MASK) **antes del CST OUT**; **Softness** siempre alto; Global (HDR wheels) o gain/offset dentro de la máscara.
- **Varias máscaras → nodo paralelo (Alt+P)**: cada una parte de la misma imagen limpia y no se acumulan errores. **Viñeta** = círculo grande **invertido** bajando Global.
- **Tracker** (junto a Power Windows): seguir adelante y atrás para que la máscara siga al sujeto, y luego ajustar *Size* y *Softness*.
- **Shift+H** muestra solo lo que hace el nodo (isolate). Qualifier para elegir un color (ej. solo los rojos) y Magic Mask (Studio) para el sujeto.
- **Regla: ve siempre con la key light.** Si el sol viene de la izquierda: sube un poco ese lado y baja el opuesto con **rampas lineales** («no muy heavy»); da direccionalidad: «un plano que es día y noche».

### Matching de planos y PowerGrade [5]
- **PowerGrade** = guardar todo el árbol: clic derecho en el visor → **Grab Still**; se aplica desde la galería con clic derecho → **Apply Grade** o **clic con la rueda del ratón** (a varios planos: seleccionarlos con Shift).
- Orden para igualar: **1) exposición, 2) balance de blancos, 3) lo fino** (saturación, máscaras, LUT).
- **Split Screen + Image Wipe** contra el still de la galería para ver las diferencias (la cara suele delatar el balance).
- Si la luz viene del mismo lado, iguala con ese plano como referencia. Un fondo distinto (tierra frente a mármol) no se puede igualar exacto: aproxima exposición y baja saturación (≈ 0.3), y baja highlights.
- Para centrar el vectorscopio es habitual empujar la rueda de offset hacia cálido.

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
- Nodos: Alt+S = nuevo nodo serie; Alt+P = paralelo; Alt+L = capa (*Layer*); Ctrl/Cmd+D = activar/desactivar nodo; Shift+H = ver solo lo que hace un nodo; *cleanup node graph* (clic derecho) ordena el árbol [2][5].
- Scopes: Vectorscopio (color y piel), Waveform (exposición), Parade (balance RGB) [1][2].
- Magic Mask solo existe en **Resolve Studio**; Bryan tiene Studio 21 [1][4] (el tutorial [5] usa Studio 20).
- **Color Space Transform**: búscalo en Effects (en [4] se busca «color s»); se aplica como un nodo [4].
- **HDR wheels** (Dark / Shadow / Light / Global) y **Color Slice** (Red, Skin, Yellow, Green, Cyan, Blue, Magenta) son los paneles que usa [4].

### LUTs
- Un LUT puede ir **al principio** (para convertir de log a Rec.709) o **al final** (como look), nunca en medio [2]. Con la gestión de color por CST de [4], el LUT va como **acabado suave**: baja su ganancia de salida a ≈ 0.1–0.28 para que no mande sobre tu grade.
- **Key Output → Gain** es la «opacidad» del LUT: en pantalla [5] se lee **0.528** (dijo «≈ 0.6, por ahí»); el LUT va **después del CST OUT** en nodo propio. Un LUT pensado para log y aplicado sobre un grade ya hecho «revienta» la imagen; aplicado desde cero queda mejor [5].
- **LUTs de DaVinci (Film Looks)** aplicados directo «matan la imagen»: están hechos para **Cineon Film Log**. Para usarlos, cambia el *Output Gamma* del CST OUT de 2.2 a **Cineon Film Log** y baja su ganancia [5].
- Galería de LUTs: clic derecho → *Open file location* → copiar el LUT → clic derecho → Refresh [5].
- Bryan tiene un paquete `luts.zip` en Descargas; no se ha abierto ni analizado todavía.

## Recetas
(Mezcla de [4] con conocimiento general de Resolve [1][2]; lo que no sale de [4] no está probado en el proyecto de Bryan.)
- **Clip S-Log3 de cero**: CST entrada → exposición baja → WB → curvas de sombras/luces → HSV gain → piel y azules en Color Slice → LUT suave → CST salida [4].
- **Plano nuevo con el sistema de [5]**: ajustes de proyecto una vez → CST IN/OUT (si es log) → EXP (waveform Y, cielo ≈ 80 o menos) → WB (waveform RGB sobre un neutro + línea de piel) → CONTRAST (un toque, pivote) → SAT (HSV, solo canal de saturación, gamma) → LUT con Key Output Gain a mitad → máscaras en nodo paralelo con la key light.
- **Igualar un plano a otro**: Grab Still del plano bueno → Apply Grade al otro → Split Screen + Image Wipe → exposición, balance, luego saturación/máscaras/LUT [5].
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
- Timeline en Rec.709 al subir exposición o contraste → se clipea antes; trabaja en DaVinci Wide Gamut y convierte al final [5].
- Slider de saturación a tope → se revienta todo; usa el nodo HSV con solo saturación [5].
- Aplicar un LUT de DaVinci sin pasar el CST OUT a Cineon Film Log → se ve muerto [5].
- Varias máscaras en serie → los errores se acumulan; usa nodo paralelo [5].
- Quitar un color global cuando el fondo tiene ese color (ej. rojo) → daña el fondo; aísla a la persona [5].
- Exportar en Mac con salida 2.2 y ver otro gamma → usa Rec.709-A y la opción de perfiles de pantalla [5].

## Checklist antes de entregar
- [ ] Si es log: CST de entrada y de salida puestos, y el grade entre los dos.
- [ ] Vectorscopio revisado: la piel sigue en su línea.
- [ ] Cada aislamiento tiene su nodo con nombre.
- [ ] Magic Mask o Power Window revisados en todo el plano (sin fugas).
- [ ] Highlight comprobado en al menos 2-3 planos.
- [ ] LUT de acabado con ganancia baja, no al 100 %.
- [ ] Look final guardado con Grab Still para los demás planos.
- [ ] Probado en reproducción, no solo en un fotograma.
- [ ] Ajustes de proyecto correctos (Wide Gamut en el timeline; salida 2.2, 2.4 o 709-A según el destino).
- [ ] Waveform: cielo y altas luces sin clipear (≈ 80 o menos), sombras con sentido; piel cerca de la línea del vectorscopio.
- [ ] Máscaras en nodo paralelo, con softness y siguiendo la key light.
- [ ] Planos de una misma secuencia igualados (exposición → balance → lo fino).

## Para MUKIWA
- Visual Edits: usar el árbol propuesto como plantilla en cada proyecto y guardarlo como PowerGrade para reusarlo. Si la cámara es Sony en S-Log3, usar la estructura CST entrada / grade / CST salida.
- Plantilla única para Visual Edits: `CST IN · EXP · WB · CONTRAST · SAT · CST OUT · LUT` + nodo paralelo de máscaras, guardada como PowerGrade MUKIWA; el LUT de marca en el nodo final con **Key Output Gain a mitad o menos** [5].
- Entregas desde Mac: salida **Rec.709-A** y la opción de perfiles de pantalla; exportar una prueba y compararla en el móvil antes de dar por bueno [5].
- Rodaje de MUKIWA: si se graba en S-Log3, sobreexponer con zebras (≈ +1.7 a +2 en el medidor de una Sony, a probar en la cámara de Bryan) y activar Gamma Display Assist [4].
- Creative Direction: traducir «verde profundo, lujoso» → verde oscuro con saturación alta; «frescura» → verde más claro y amarillento.
- Graphic Design: la paleta #232323 / #0068FB / #C5ED2E sirve igual como referencia de color para el grade.

## Dudas abiertas
- [4] es un creador que vende su PowerGrade, LUTs y curso: los valores del grade (curvas, gain de HSV, saturaciones) **no se vieron en pantalla**; solo valen los números que dijo (+1.7/+2, 0.28, 0.1, 0.29, 0.25).
- Gamma de salida «Rec.709-A»: la opción **existe en la lista de Resolve** (visto en pantalla [5]) y dos creadores la nombran, uno para Mac [5]; sigue sin verse cuál elige [4] en su CST de salida.
- Ninguna fuente dice el ISO base ni el nivel de zebra; el «+1.7 a +2» depende de cómo lea el medidor cada cámara.
- Los valores de hue, gamma y blur de la receta de la palmera siguen siendo puntos de partida (≈), sin validar en el proyecto de Bryan.
- No se leyeron los parámetros reales de los nodos de Bryan (solo se ve el árbol y la curva Hue vs Hue en la captura).
- `luts.zip` y la carpeta `Color Grading LLC/CineDream` (vacía) no aportan todavía material.
- [5] también vende su PowerGrade, LUTs y comunidad: el método se enseña completo, pero los valores de su PowerGrade no se vieron; y la fuente de audio es el subtítulo automático de YouTube (términos como «Rec.709» o «LUT» salían mal escritos).
- Cifras dichas y no vistas en pantalla [5]: cielo ≈ 80 (mejor 60–70), saturación ≈ 0.3 en un plano; los números de ruedas, tamaños y softness de las máscaras no se leyeron.
- «Rec.709-A» y «Use Mac Display Color Profiles» se dicen para Mac; el autor trabaja en Windows y no lo mostró. Sin probar en el Mac de Bryan.
- Dos flujos distintos de CST/nodos [4] (3 nodos, grade dentro de un PowerGrade) y [5] (cuatro nodos con nombre, LUT después del CST OUT); no hay prueba de cuál rinde mejor en los planos de Bryan.
- Falta aprender: ACES y otros flujos de color management, HDR, matching entre cámaras distintas, y grading de log de otras marcas (Canon, Panasonic, Blackmagic). Matching entre planos de una misma cámara ya está en [5].

## Fuentes
- [1] Captura de la página Color de DaVinci Resolve Studio 21, proyecto «CULTURA ANUNCIO», timeline «VIDEO 2 CAPSULA» (Bryan, 2026-10-15).
- [2] Conocimiento general de DaVinci Resolve (Claude); no viene de un video analizado.
- [3] Paleta y dirección de marca MUKIWA DEPARTMENT (preferencias de Bryan).
- [4] Cómo rodar y gradear S-Log3 bien: cámara Sony, exposición con zebras, CST y grade en Resolve (Gaku Lange) — https://www.youtube.com/watch?v=0GBqqfMjPuQ · `references/lecciones/s-log3-rodaje-y-grade-en-resolve-gaku-lange.md`
- [5] Color en DaVinci: un sistema ordenado de nodos, scopes, máscaras y matching (AlwaysJoan) — https://youtu.be/3yQrX93_K04 · `references/lecciones/color-en-davinci-sistema-de-nodos-scopes-mascaras-y-matching-alwaysjoan.md`
