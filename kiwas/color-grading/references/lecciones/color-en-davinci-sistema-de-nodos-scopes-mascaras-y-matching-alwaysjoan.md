# Color en DaVinci: un sistema ordenado de nodos, scopes, máscaras y matching (AlwaysJoan)
> Método completo para colorizar cualquier plano en Resolve: ajustes de proyecto, CST, 4 nodos con orden fijo (exposición, balance, contraste, saturación HSV), LUT suave, Power Windows en nodo paralelo y matching de planos con PowerGrades.

- **Fuente**: https://youtu.be/3yQrX93_K04 · «Dame 45 minutos y podrás COLORIZAR cualquier vídeo en segundos» · canal AlwaysJoan (AlwaysFilmLab) · 44:46 (2686 s) · español · publicado 2026-02-15
- **Fecha**: 2026-10-30 · **Tema**: color-grading · **Modo**: Completo, foco color
- **Tipo de "oídos"**: subtítulos automáticos de YouTube en español (transcript completo con tiempos, segunda mano; Whisper se lanzó en el contenedor pero se canceló tras ≈6 min de audio por lentitud (2 núcleos)). Chrome/Sider no estaba conectado.
- **Ojos**: 15 hojas de contacto (un fotograma cada 20 s, de 0:00 a 44:20, **todo el video visto a esa resolución**) + 5 fotogramas sueltos a 1280×720 (2:25, 2:58, 6:40, 19:15, 23:50). Los valores de ruedas y curvas en las hojas no se leen; solo los fotogramas sueltos.
- **Confianza**: media-alta en el flujo (audio y pantalla coinciden); media en números dichos (el subtítulo automático mete errores: «loot» por LUT, «Rex 709» por Rec.709, «CS in» por CST in).
- **Aporte**: **alto**. Es el tutorial de proceso completo en pantalla que le faltaba al Kiwa. Promociona su PowerGrade «Evolved Film», LUTs y comunidad (no se abrieron esos enlaces); el método se enseña sin necesitarlos.

## Capítulos (de la descripción)
0:00 el problema real · 0:40 ajustes de proyecto · 3:57 interfaz · 4:28 qué es el log · 4:50 CST · 7:10 qué es Rec.709 · 9:05 estructura de nodos · 10:14 exposición · (resto sin capítulos: balance 14:30, contraste 17:50, saturación 18:40, LUT 20:30, máscaras 24:05, matching y PowerGrade 30:44)

## Teoría (lo que se dijo)
**Ajustes de proyecto, 0:40–3:55** (Resolve Studio 20, en Windows)
- Engranaje abajo a la derecha → **Color Management**. *Color science* = **DaVinci YRGB**; *Timeline color space* = **DaVinci Wide Gamut** (dice que por defecto suele venir en un Rec.709; el subtítulo no deja claro cuál variante, y lo cambia a propósito) para tener margen al empujar color sin romper la imagen.
- *Output color space*: **Rec.709 Gamma 2.2** si se entrega a YouTube, redes o web; **Gamma 2.4** si es broadcast/televisión. **En Mac** el video exportado no se ve igual que en Resolve: usar **Rec.709-A** (de «Apple») como salida [2:46–3:00].
- Para no repetirlo: los tres puntos de arriba → *Set current settings as default* → Update.
- Solo Mac: Preferencias → Sistema → General → marcar la opción *Use Mac Display Color Profiles for viewers* (en Windows sale como «Windows for viewers»).
- Guía de la interfaz: nodos = bloques de ajuste que se aplican de izquierda a derecha (como capas de Photoshop, pero horizontales); visor a la izquierda; herramientas abajo; scopes a la derecha.

**Log y CST, 4:28–7:10**
- El log captura el máximo rango dinámico a costa de contraste y saturación; por eso se ve plano. Si el plano ya es Rec.709/estándar, no hace falta CST.
- Dos nodos en serie (clic derecho → añadir nodo serie, o **Alt+S**; **cleanup node graph** para ordenarlos), nombrados **CST IN** y **CST OUT**; en ambos el efecto *Color Space Transform* (Library → Effects → buscar «color space transform»).
- **CST IN** (su cámara es una Sony FX30): Input Color Space **Sony S-Gamut3.Cine**, Input Gamma **S-Log3**; Output Color Space **DaVinci Wide Gamut**, Output Gamma **DaVinci Intermediate**.
- **CST OUT**: Input = DaVinci Wide Gamut / DaVinci Intermediate; Output Color Space **Rec.709**; Output Gamma **2.2 o 2.4** según el destino (él, 2.2 para YouTube).
- Por qué trabajar en Wide Gamut (7:10–9:00): Rec.709 es un espacio chico (casi todas las pantallas); Wide Gamut es mucho mayor y deja empujar exposición, contraste y color sin que la imagen se rompa. Demostración: con el timeline en Rec.709 sube un poco la exposición y se pierden las altas luces y el fondo; vuelve a Wide Gamut y se recupera «muchísimo detalle del fondo»; en la waveform se ve que sube toda la imagen por igual, «como subir la exposición en cámara».

**Estructura base de nodos, 9:03–10:14**
- Cuatro nodos en serie **entre** CST IN y CST OUT: **EXP** (exposición), **WB** (balance de blancos), **CONTRAST**, **SAT** (saturación). Atajo para etiquetar: *Resolve Keyboard Customization* → buscar «node label» → asignar una tecla (él usa **R**) y escribir el nombre sobre el nodo.
- **Orden que insiste en mantener: primero la luz, luego el color y luego la intención.**

**Exposición con scopes, 10:14–14:30**
- Usa las **HDR wheels**, apartado **Global**, que «se comporta como el ISO de una cámara». Para ver las HDR wheels: icono junto a las ruedas normales.
- **Waveform** configurada así: ajustes → modo **Y** (luminancia, sin colorize) → los tres puntos → activar *Display Qualifier Focus* y *Waveform scale style* = **porcentaje** (0 a 100).
- 0 = negro absoluto, 100 = blanco absoluto. Algo por encima de 100 clipea; si todo se aplasta en 0 se pierden sombras. **«El contexto manda»**: un plano nocturno puede vivir cerca de 0; uno a contraluz puede clipear arriba y estar bien. «No buscamos números perfectos, buscamos una imagen coherente.»
- Display Qualifier Focus: con el Qualifier encima de una zona del visor, la waveform marca un círculo donde cae esa zona (sirve para ver el valor exacto de cielo, árbol, pelo).
- Para el cielo: «**80 es un buen rango**, aunque si puedes tenerlo en 70 o 60, mejor» (13:48–13:55). Dice que en el plano de noche la gorra, la chaqueta y el cielo están cerca de 0 y los neones clipean, y está bien por ser de noche.
- Ruedas normales: **offset** = exposición global; **gain** = altas luces; **gamma** = tonos medios; **lift** = sombras. Las *Log wheels* las deja para otro tutorial.

**Balance de blancos, 14:30–17:30**
- Dos referencias: **la piel** (si se ve, es la mejor) o **un neutro** (negro, gris o blanco). En el ejemplo usa el **negro del pelo**.
- Waveform en **RGB con colorize**: sobre un negro puro, las tres «bolitas» (rojo, verde, azul) deben quedar **en el mismo sitio, formando una redonda perfecta**. Si hay más rojo/azul de un lado, se resta con la **rueda de offset** (en el ejemplo, un poco de azul, «no mucho»).
- Cuando el fondo tiene un color fuerte (aquí un torii rojo), quitar rojo global arruina el fondo: habría que aislar la piel/persona y corregir solo eso.
- **Vectorscopio**: activar *Show Skin Tone Indicator* (línea de piel). La piel debe quedar **lo más cerca posible de esa línea**; en el ejemplo está algo a la derecha y se corrige moviendo hacia la izquierda con las ruedas en un nodo nuevo (no lo hace en el tutorial por ser más complejo). Zoom del vectorscopio: **Alt + rueda del ratón**.

**Contraste, 17:50–18:40**
- Slider **Contrast** + **Pivot**: contraste expande la distribución de luz; el pivote decide si afecta más a sombras o a luces. **Pivote a 0 → afecta más a las altas luces; a 1 → más a las sombras.**
- «Un buen contraste da profundidad; demasiado se siente artificial»: solo un toque.

**Saturación con HSV, 18:40–20:30**
- No empujar el slider de saturación al máximo: «ha reventado absolutamente todo» (waveform y colores mezclados); es «lo número uno que no se tiene que hacer».
- Alternativa: en el nodo SAT, clic derecho → **Color Space → HSV**; luego clic derecho → **Channels** y se **quitan el primer y el tercer canal**, dejando solo **Saturación** activa Con eso, la rueda de **gamma** ya no toca la exposición de los tonos medios: solo añade saturación **a las partes menos saturadas**, y las más saturadas (la piel) quedan protegidas. Resultado «más equilibrado y cinematográfico».

**LUT (look), 20:30–24:00**
- Un LUT es «como un preset de fotografía, pero para vídeo». **No debe hacer todo el trabajo: es un empujón sutil**; hay que bajarlo con **Key Output → Gain** («menos es más»).
- Pasar todos los nodos un poco a la izquierda para dejar un hueco; el LUT va **después del CST OUT** en un nodo propio (en pantalla: nodo 07 `LUT`).
- Galería de LUTs: clic derecho → *Open file location* → copiar el LUT → clic derecho → Refresh.
- **LUTs de DaVinci (Film Looks)**: aplicados directo «matan la imagen» porque están hechos para espacio **Cineon Film Log**. Solución: en el **CST OUT**, cambiar el *Output Gamma* de 2.2 a **Cineon Film Log**; ahí sí funcionan (aun así hay que bajarlos). Con su propio LUT («Evolved», pensado para esta cadena) no hace falta ese cambio.
- Su LUT sobre el grade ya hecho «revienta» la imagen; aplicado desde cero (a la imagen log) queda mejor. Para que interactúe: **Key Output Gain ≈ 0.6** («por ahí»); en pantalla se lee **0.528** (ver Práctica).

**Power Windows (máscaras), 24:05–30:40**
- Sirven para oscurecer bordes, iluminar al sujeto y reducir distracciones. Nodo **antes del CST OUT** (en el tutorial lo crea «anterior al CST OUT»), renombrado «MASK» con la tecla R.
- **Softness** para suavizar el borde de la máscara; con las HDR wheels (Global) se sube/baja la exposición solo dentro de la máscara.
- **Nodo paralelo (Alt+P)** para usar varias máscaras: cada máscara parte de **la misma imagen limpia** y no se acumulan errores; las salidas se combinan. Segunda máscara: círculo agrandado e **invertido** (icono de invertir) y bajar Global → **viñeta**; subir su softness.
- **Tracker** (a la derecha de Power Windows): seguir adelante y atrás para que la máscara siga al sujeto; luego se puede ajustar *Size* y *Softness*.
- Otros métodos de selección dentro de nodos paralelos: **Qualifier** (y **Shift+H** para ver solo lo que hace ese nodo, un «isolate»; ejemplo: solo las partes rojas) y **Magic Mask** (versión de pago).
- **Regla de máscaras: siempre ir con la key light** (luz principal; aquí el sol viene de la izquierda): iluminar un poco más ese lado y oscurecer el opuesto con **rampas** (lineal): una desde una esquina para subir, otra para bajar la contraria; «no muy heavy». Con eso el plano gana **direccionalidad**: «un plano que es día y noche».

**Matching y PowerGrades, 30:44–42:30**
- **PowerGrade** = guardar todo el árbol de nodos: clic derecho en el visor → **Grab Still** → queda en la galería; aplicar con clic derecho → **Apply Grade** o **clic con la rueda del ratón**. Sirve para que los planos de una misma secuencia «tengan relación y no salten».
- Cuatro planos de Corea (plano de templo/palacio y pasillo de columnas) con el mismo PowerGrade + ajustes por plano: **1) igualar exposición, 2) igualar balance de blancos, 3) afinar lo fino (saturación, máscaras, LUT).**
- Herramientas: **Split Screen → Image Wipe** con el still de la galería: se compara el plano actual con el de referencia; el still que se quiere ver se elige en la galería.
- Ajustes que hace en el segundo plano (cara muy distinta por balance de blancos): Global hacia tonos más azulados, **bajar saturación** (gamma), máscaras iguales con la luz del mismo lado, algo más de contraste con el pivote hacia sombras. Para el plano del suelo de tierra vs mármol: «no se puede machear exacto»; sube exposición y baja saturación (≈ **0.3**, «solo un toquecito») y baja un pelín highlights.
- Técnica habitual: para centrar el vectorscopio, **empujar la rueda de offset hacia tonos más cálidos** hasta que la bolita quede cerca del centro.
- Cierre: «Cuatro planos bastante bien macheados y sin saltos de continuidad.» Su PowerGrade «Evolved Film» (de pago) añade grano, shadow tone, saturación, noise, blacks, un nodo «custom» y un nodo para corregir pieles «en un clic» con vectors; el resultado: ajustar solo exposición y balance de blancos (≈ «tres clics»).
- Resumen final: «Si entiendes este sistema, puedes colorizar cualquier plano hecho con cualquier cámara; no es magia, es orden.»

## Práctica (lo que se ve)
- **2:25 (fotograma suelto, 1280×720):** *Project Settings → Color Management*: **Color science = DaVinci YRGB**; **Timeline color space = DaVinci WG/Intermediate**; *Output color space* con la lista abierta: **Rec.709 Gamma 2.2, Rec.709 Gamma 2.4, Rec.709-A, Rec.709 HLG ARIB STD-B67, Rec.709 (Scene), Rec.2020…**. Confirma que **«Rec.709-A» existe** como opción (el cursor está sobre Gamma 2.2). Lo de «para Mac» es de audio.
- **6:40 (suelto):** CST IN / CST OUT en dos nodos (01, 02), en Resolve **Studio 20**; Input Color Space en lista abierta (Canon Cinema Gamut, **DaVinci Wide Gamut**, DJI D-Gamut…) y *Gamut Mapping Method = None*, *Use White Point Adaptation* marcado.
- **7:00 (hoja):** CST OUT con entrada DaVinci Wide Gamut / Intermediate, salida Rec.709 y Output Gamma Gamma 2.2 (rótulo en pantalla «LOG – DAVINCI WIDE GAMUT – REC 709»).
- **10:00–10:40 (hoja):** árbol visto: `CST IN → EXP → WB → CONTRAST → SAT → CST OUT`.
- **12:20 (hoja):** rótulo «Gamma = Tonos Medios»; HDR wheels con rótulos *Dark / Shadow / Light / Global*.
- **15:40 (hoja):** rótulo «Podéis usar la piel o un color neutro».
- **16:00–17:40 (hoja):** un nodo del árbol aparece desplazado hacia arriba (nodo creado a mano para el ajuste de piel; no se lee qué contiene); vectorscopio con la bolita de piel y la línea indicadora.
- **17:20 (hoja):** panel de columnas que parece **Color Slice** (rótulo ilegible, sin leer valores); **17:40:** curva personalizada (diagonal con una subida suave) en CONTRAST.
- **19:00 (hoja):** rótulo «Saturación HSV».
- **21:20–22:40 (hoja):** galería de LUTs («Evolved LUT…», «Joan LUTs», «Film Looks»); el LUT de DaVinci aplicado se ve con color verdoso azulado y el plano reventado; CST OUT con otro gamma.
- **23:50 (suelto):** árbol final: **CST IN (01) → EXP (02) → WB (03) → CONTRAST (04) → SAT (05) → CST OUT (06) → LUT (07)**; en el panel *Key* → **Key Output Gain = 0.528**. Waveform con altas luces ≈ 90 en el cielo.
- **24:00–26:40 (hoja):** Power Windows (círculo) con rótulo «Máscaras de DaVinci»; nodo paralelo con dos nodos `MASK` y `MASK 2` en rombo; círculo invertido para viñeta.
- **27:20 (hoja):** Tracker abierto; **28:20:** Qualifier HSL con selección en blanco sobre las partes rojas (isolate con Shift+H).
- **29:40–30:00 (hoja):** rampa lineal (línea blanca diagonal) sobre el plano; nodos paralelos de 4 ramas.
- **31:00–42:00 (hojas):** PowerGrade guardado en la galería (miniaturas «Evolved Film / PowerGrade»); planos de Corea con el árbol paralelo; Split Screen con wipe vertical entre dos planos; vectorscopio con bolita cerca del centro tras empujar hacia cálido.
- **42:00–43:30 (hojas):** su PowerGrade «Evolved Film» (árbol grande de ≈15 nodos con etiquetas ilegibles en la hoja; el audio nombra grano, shadow tone, saturación, noise, blacks, un nodo «custom» y uno de piel), sin leer valores.

## Cruce teoría ↔ práctica
- **Coinciden:** árbol `CST IN / EXP / WB / CONTRAST / SAT / CST OUT / LUT`; Studio 20; salida a Rec.709; opción Rec.709-A existente; uso de nodo paralelo para varias máscaras; matching con split screen.
- **Corrige al audio:** el LUT al «0.6 por ahí» está en **0.528** en pantalla. Gana la pantalla.
- **Aclara «Rec.709-A»:** [lección Gaku Lange] lo decía en audio sin confirmar; aquí **una segunda fuente lo dice** (opción para Mac/Apple) y la lista de Resolve **lo muestra**. Sigue sin verse cuál elige él en el CST OUT del video de Gaku.
- **Solo en el audio:** pivote 0 → luces / 1 → sombras; quitar los canales primero y tercero en HSV (la pantalla solo muestra el nodo SAT con HSV); «80 es buen rango para el cielo».
- **Solo en pantalla:** Key Output Gain 0.528; el árbol de 7 nodos con LUT al final; Studio 20 (la lección de Gaku vio Studio 21).
- **Diferencia de método con Gaku Lange [lección anterior]:** Gaku usa **3 nodos** (CST IN / grade / CST OUT) y su grade va dentro de un PowerGrade grande; AlwaysJoan separa el grade en **4 nodos con nombre** entre los CST y pone el LUT **después** del CST OUT. Los dos exponen en Wide Gamut/Intermediate y convierten a Rec.709 al final. Con LUTs de DaVinci, Joan cambia el gamma del CST OUT a Cineon Film Log; Gaku no lo dice.
- **Sobre exposición:** Gaku sobreexpone en cámara (+1.7 a +2) y baja en post; Joan expone en post con la waveform (cielo ≈ 80 o menos). Son complementarios, no se contradicen.

## Receta paso a paso (cualquier plano; lo no marcado viene del video)
1. **Una sola vez:** Project Settings → Color Management → Color science DaVinci YRGB, Timeline color space DaVinci Wide Gamut, Output color space Rec.709 Gamma 2.2 (web/redes) o 2.4 (broadcast); **en Mac**, Rec.709-A y activar *Use Mac Display Color Profiles*. «Set current settings as default».
2. Si el clip es log: **CST IN** (espacio y gamma de tu cámara → DaVinci Wide Gamut / DaVinci Intermediate) y **CST OUT** (→ Rec.709, gamma 2.2 o 2.4). Alt+S para crear nodos; cleanup node graph.
3. Entre los dos CST, 4 nodos en este orden y con nombre: **EXP → WB → CONTRAST → SAT**.
4. **EXP:** HDR wheels → Global; waveform en luminancia (0–100); cielo ≈ 80 o menos; piel/fondo coherentes; no buscar números perfectos.
5. **WB:** waveform en RGB; sobre un negro/gris, las 3 bolitas juntas; ajustar con offset; revisar piel en el vectorscopio (línea de piel).
6. **CONTRAST:** un toque; pivote 0 (luces) a 1 (sombras).
7. **SAT:** nodo en HSV con solo el canal de saturación; empujar con **gamma**, nunca el slider de saturación a tope.
8. **LUT** en nodo propio **después** del CST OUT; **Key Output Gain** a mitad (≈ 0.5 en el ejemplo).
9. **Máscaras** (después del grade): nodo paralelo (Alt+P), una máscara por intención; siempre siguiendo la key light; Softness en todas; Tracker si hay movimiento; viñeta = círculo invertido bajando exposición.
10. **Matching:** Grab Still → Apply Grade (rueda) en los demás planos; Split Screen + Image Wipe contra el still; ajustar **exposición → balance → saturación/máscaras → LUT**, en ese orden.

## Para MUKIWA
- **Visual Edits:** adoptar este árbol como plantilla única: `CST IN · EXP · WB · CONTRAST · SAT · CST OUT · LUT · MASKS`, y guardarlo como PowerGrade MUKIWA. El árbol de BASE/VERDES/PALMERA/PIEL/LOOK que ya usa Bryan se mantiene **dentro** de esta cadena (entre los CST).
- **Look MUKIWA:** el LUT de marca (azul #0068FB en sombras, lima #C5ED2E en luces) va en su nodo `LUT` final, con **Key Output Gain a mitad o menos**, nunca al 100 %.
- Para entregas de Bryan en **Mac**: salida **Rec.709-A** y activar la opción de perfiles de pantalla de Mac; confirmarlo exportando una prueba y comparando en el móvil.
- **Creative Direction:** la regla «máscaras con la key light» es una forma barata de dar dirección de luz y atención al sujeto (viñeta invertida + rampas).
- Cámara de Bryan: si no es Sony FX30/S-Log3, el CST IN cambia; el resto del árbol no.

## Límites
- **Valores que no se leyeron:** posiciones exactas de las ruedas y curvas, los números de los ajustes de máscaras (tamaño, softness) y los de su PowerGrade; en las hojas son ilegibles y solo se ampliaron 5 fotogramas.
- **Transcript automático** de YouTube: puede haber errores en términos y cifras; las cifras citadas (≈ 80, 0.3, ≈ 0.6) son de audio, salvo el 0.528 (pantalla).
- «El Wave4/wave from» y «loots» son errores de transcripción que se corrigieron por contexto.
- No se abrió su PowerGrade, su LUT ni su comunidad (venta). No se descargó el clip log que ofrece.
- Los pasos 8–9 de la receta (posición del LUT y orden de máscaras) combinan lo dicho con lo visto; la cifra 0.5 para el LUT es mi redondeo de 0.528.
- Se vio con detalle el bloque 0:00–31:00; entre 31:00 y 42:00 solo hojas (las máscaras de los 4 planos de Corea no se leyeron valor por valor).

## Conecta con
- [[s-log3-rodaje-y-grade-en-resolve-gaku-lange]] (mismo flujo de CST; Joan lo amplía con proyecto, scopes, HSV, máscaras y matching)
- Kiwa `kiwa-iluminacion` («luz como guía de la mirada»): las máscaras con la key light son la versión en postproducción
