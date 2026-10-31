# S-Log3: cómo rodarlo y gradearlo bien (Gaku Lange)

- **Fuente:** https://www.youtube.com/watch?v=0GBqqfMjPuQ · canal Gaku Lange · 17:37 (1057 s) · 1920×1080
- **Fecha de análisis:** 2026-10-15 · **Tema:** color-grading · **Modo:** Completo, foco color
- **Fuentes de datos:** subtítulos automáticos en inglés (transcript, segunda mano) + 2 frames de DaVinci Resolve (7:58 y ≈ 9:05). Los menús de la cámara **solo se oyeron**, no se miraron frame a frame.
- **Aporte:** medio. Es un flujo real y reproducible (cámara + CST), pero la parte del grade usa su PowerGrade de pago, que no se ve nodo por nodo. Mucha promoción de su tienda.

## Capítulos (de la descripción)
0:00 intro · 0:22 configurar S-Log3 · 2:59 filmar y exponer · 5:24 preproducción con Claude + Higgsfield · 7:14 cómo gradea S-Log3 · 16:14 cierre

## Teoría (lo que dijo)
**Cámara (Sony ZV-E1; dice que es igual en su FX3), 0:22–2:50**
- Picture Profile **PP1**: gamma **S-Log3** y color mode **S-Gamut3.Cine**. Todo lo demás en estándar.
- Formato: **XAVC S 4K** (cree que el más alto es «SI 4K» pero elige S 4K por equilibrio peso/calidad), **30 fps** (también 24 o 60), **4:2:2 10-bit** «lo más importante».
- **Gamma Display Assist** activado (Menu → Setup → Display Option): el visor muestra una Rec.709 para exponer en tiempo real; es solo ayuda de pantalla.

**Exposición, 2:59–5:13**
- El medidor del visor marca de −2 a +2. Él **sobreexpone de +1.7 a +2**.
- Razón: si subexpones S-Log3, al levantar sombras en post pierdes calidad y detalle. Quiere el máximo de sombras **sin quemar las altas luces importantes**.
- Usa **zebras** (Menu → Exposure/Color → Zebra) como límite: lo que tiene zebra está perdido. El cielo puede quemarse, no pasa nada.
- En post baja la exposición y recupera.

**Preproducción (5:24–7:00):** checklist de equipo, planos y focales con Claude conectado a Higgsfield por MCP; agrupa los planos **por focal** (10 mm, luego 35, luego 50) para no cambiar de lente. Es patrocinio.

**Resolve, 7:14–15:50**
- **Base mínima de 3 nodos:** 01 = **CST de entrada**, 02 = todo el grade, 03 = **CST de salida**.
  - CST 1: entrada **Sony S-Gamut3.Cine / S-Log3** → salida **DaVinci Wide Gamut / DaVinci Intermediate**.
  - CST 3: **DaVinci Wide Gamut / Intermediate → Rec.709, gamma «Rec.709-A»** (así suena en el audio).
  - Exposición, color y estilo se hacen en el nodo del medio, ya en DaVinci Wide Gamut.
- **Su PowerGrade «Odyssey Pro» (de pago):** árbol grande donde **solo enciendes el primer y el último CST**; el resto son nodos que él armó:
  1. *Denoise espacial* antes del CST (solo si hay ruido, p. ej. de noche).
  2. *Exposición*, HDR wheels: baja un poco **global** y **lights**.
  3. *White balance*: clip algo azul → lo calienta «ever so slightly».
  4. *Shadows*: curva con **3 puntos enlazados**, baja un poco las sombras y sube un poco el punto izquierdo → más roll-off «filmic». Igual en highlights (mueve un poco a la izquierda).
  5. *HSV*: sube **gain** en las ruedas → más densidad y saturación solo en altas luces («punch»).
  6. *Skins (Color Slice)*: piel oversaturada → baja **saturación** y un poco la **densidad**.
  7. *Filmic* (grano, gate weave, polvo): **apagado** porque no quiere look de película.
  8. *Tones*: curvas prehechas; si gustan, se dejan.
  9. *7 LUTs de acabado* (vintage, overcast, outdoors…): bajan el **Key Output Gain** a **0.28** y luego a **0.1** para que sean sutiles. Eligió «outdoors» a 0.1.
  10. *Contrast* y *Warmth* (curvas prehechas): apagados en este plano.
  11. *Azules*: en Color Slice sube la saturación de azules y cianes; si quiere más teal, mueve el **hue del azul** hacia la derecha.
  12. *Viñeta (bonus)*: nodo con **Radial Blur** + máscara circular, **feather**, **invertida**, centrada; fuerza **0.29 → 0.25** («casi no se nota»).
- Al terminar: **clic derecho → Grab Still** y reutiliza el look en otros clips desde la galería.

## Práctica (lo que se ve en los frames)
- **7:58:** nodos **01 → 02 → 03** en serie. El panel de CST muestra *Input Color Space = Sony S-Gamut3.Cine*; *Input Gamma* todavía en «Use timeline» (aún no lo había puesto); *Tone Mapping Method = DaVinci*, *Adaptation 9.00*, *Gamut Mapping Method = None*. Interfaz: **DaVinci Resolve Studio 21**.
- **≈ 9:05:** en la galería aparece el álbum «Testing» con el still «Odyssey Powergrade»; el clip de ejemplo es una escena de bosque/casa con montaña, en ProRes 422 LT.
- Los frames **confirman** la estructura de 3 nodos y el color space de entrada; no se pudieron leer los demás valores del PowerGrade.

## Cruce
- Coinciden: 3 nodos, CST de entrada con S-Gamut3.Cine, CST de salida al final.
- Solo en el audio: gamma de salida «Rec.709-A», y todos los valores de cámara y exposición.
- Solo en pantalla: Tone Mapping DaVinci / Adaptation 9.00 / Gamut Mapping None (no los comenta).

## Método reproducible
1. Cámara: PP1 → S-Log3 + S-Gamut3.Cine; 4:2:2 10-bit; Gamma Display Assist ON; zebras ON.
2. Exponer **por encima de lo cómodo** (≈ +1.7 a +2 en su medidor) hasta el borde de quemar lo importante.
3. Resolve: CST (S-Gamut3.Cine/S-Log3 → DaVinci Wide Gamut/Intermediate) → grade → CST (→ Rec.709).
4. En el grade: bajar exposición, curvas de sombras/luces suaves, saturar luces con gain, piel y azules en Color Slice, LUT de acabado con intensidad baja, viñeta sutil.
5. Guardar con Grab Still y aplicar a los demás planos.

## Para MUKIWA
- **Base del árbol de nodos**: `01 CST ENTRADA · 02 GRADE · 03 CST SALIDA`; el árbol de 8 nodos del profe (BASE, VERDES, PALMERA, PIEL, LOOK…) va **dentro** del nodo 02 o entre los dos CST, nunca antes del primero ni después del último.
- LUT de look MUKIWA: aplícalo **con ganancia baja** como acabado (≈ 0.1–0.3 según este video), no al 100 %.
- Si la cámara de Bryan no es Sony S-Log3, el CST de entrada cambia; los valores de este video son solo de Sony.

## Límites y dudas
- Transcript automático, a veces confuso («Rec. 709 A»). El gamma de salida «Rec.709-A» queda **sin confirmar en pantalla**.
- Los valores del PowerGrade (curvas, gain de HSV, saturaciones) **no se vieron**; solo los números dichos (+1.7/+2, 0.28, 0.1, 0.29, 0.25).
- No dice **ISO base** ni **nivel de zebra**; el «+1.7 a +2» depende de cómo lea el medidor su cámara con el display assist activo: probar en la cámara de Bryan antes de copiarlo.
- Su otro video de flujo completo (https://www.youtube.com/watch?v=7imay44H3_Q) y su tienda no se abrieron.
