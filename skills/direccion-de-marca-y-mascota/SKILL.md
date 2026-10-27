---
name: "direccion-de-marca-y-mascota"
description: "Cierra la identidad de una marca (sistema visual, voz, mascota/personaje, reglas de uso) con criterio de diseño y la deja lista para aplicarse a un sitio web."
---

# Dirección de marca y mascota

Usa esta skill cuando haya que terminar o ampliar un branding (logo, color, tipografía, voz, personaje/mascota, motion) antes o en paralelo a un sitio web. Trabaja con `creador-de-sitios-web-universal` (el sitio consume lo que aquí se define).

## 0. Principios (del conocimiento reunido)

1. **La marca nace del nicho y la oferta**, no del estilo: quién eres, a quién sirves, qué problema resuelves, cómo lo haces (proceso con nombre propio). Sin eso, la mascota es decoración.
2. **Criterio humano sobre la IA.** La IA sirve para explorar; la decisión final, la coherencia y la limpieza del arte final son humanas. Cada elección debe poder justificarse con una razón de marca o de negocio.
3. **Un elemento dominante por capa.** Con varias tendencias a la vez (cristal, textura, nostalgia retro, Y2K) se pierde la marca. Define qué hace cada capa y qué NO hace.
4. **Contención.** Menos reglas bien aplicadas pesan más que muchas mal usadas. Sistema mínimo viable primero, ampliación después.
5. **Accesibilidad y legibilidad desde el sistema:** contraste de color verificado, tamaños mínimos de logo, texto nunca solo sobre ilustración.

## 1. Auditoría de lo que ya existe (antes de diseñar nada)

Inventario: logo (versiones, mínimos, zona de respeto), paleta con valores y roles, tipografías con licencias, voz y slogans, activos existentes, lo que está prometido o pendiente. Marca qué está **cerrado**, qué está **abierto** y qué **bloquea** al sitio. Casi nunca bloquea el personaje: bloquean paleta, tipografía, logo y voz.

## 2. Estrategia en una página

- Nicho: ¿solución obvia de qué problema para quién?
- Oferta: yo + ellos + cómo; proceso con nombre y escalera (hecho para ti / contigo / hazlo tú mismo) si aplica.
- Significado y valores (la idea que la marca defiende) y cómo se nota en el comportamiento.
- Jerarquía de mensajes: línea maestra, creencia, movimiento, estilo de vida, la persona.
- Escalera de confianza: qué muestra la marca (visual, escrito, audio, video, vivo, en persona) y cuál es el siguiente escalón.

## 3. Sistema visual

- **Color:** roles (base, acento primario, acento secundario, texto, estados); contraste mínimo 4.5:1 para texto; reglas de proporción (p. ej. 60/30/10).
- **Tipografía:** una para títulos, una técnica/mono, una de lectura; escala modular; licencias de uso web verificadas (no asumir).
- **Textura/material:** qué superficies existen (grano, papel, cartón, cinta) y dónde se usan.
- **Cristal/UI:** limitado a elementos de interacción; nunca sobre el personaje.
- **Motion:** una variable de tiempo, curvas fijas, qué se anima y qué no; reduced-motion respetado en lo intrusivo.
- **Logo en acción:** estados permitidos (p. ej. un elemento del logo que cambia de expresión) sin alterar la estructura.

## 4. Mascota / personaje (proceso)

**4.1 Brief (una página).** Rol del personaje (secundario, nunca sustituye al logo), personalidad en 3 adjetivos, qué comunica de la marca, dónde vive (sitio, redes, stickers, motion, merch), qué NO debe ser.

**4.2 Reglas de estilo (hoja de decisiones).** Contorno de grosor uniforme; color plano con un solo acento; paleta limitada a la de la marca + 1; anatomía (proporción cabeza/cuerpo, manos, nariz, ojos); vestuario y accesorios que lo hacen reconocible; **silueta legible a 32 px**; sin degradados ni cristal sobre el personaje. Si el estilo es retro (animación de los años 30) con ropa actual (Y2K), fija qué es de cada época: cara, manos y movimiento retro; ropa, accesorios y paleta contemporáneos.

**4.3 Exploración.** 3 direcciones distintas (silueta, nivel de abstracción, expresión). Evalúa con: ¿se reconoce en 1 segundo?, ¿funciona a 32 px?, ¿funciona en negro y en claro?, ¿se puede animar con pocos dibujos?, ¿se parece demasiado a un personaje existente? Elige una y descarta el resto.

**4.4 Hoja de personaje (entregable mínimo).** Vistas frontal, 3/4, perfil y espalda; 6 expresiones; 6 poses clave; paleta con valores; construcción con formas básicas; versión cabeza/icono; versión una tinta; 3 acciones de marca (saludar, señalar, “drag it”). Para animación: ciclo de parpadeo, rebote y 2 transiciones.

**4.5 Archivos finales.** Vectorial (SVG/AI) para uso gráfico; PNG/WebP con fondo transparente; hoja de sprites o Lottie/video alfa si se anima. Nombres y carpetas ordenados.

## 5. Originalidad, derechos y producción

- **Diseño original:** puedes inspirarte en una época o estilo general (p. ej. animación de caucho de los años 30), pero no reproduzcas personajes, mascotas ni diseños concretos existentes, ni cambies solo pose o color de uno conocido. Si el resultado recuerda a un personaje famoso, rehazlo.
- **Quien lo dibuja:** contrato escrito con alcance, número de revisiones, entregables y **cesión de derechos o licencia comercial**; pago por hitos (depósito primero). Sin depósito pagado no hay trabajo ni derechos sobre bocetos.
- **IA como herramienta:** útil para explorar; la protección legal de obras generadas solo con IA es incierta y depende del país. Para un activo central de marca, haz el arte final con intervención humana y verifica con un abogado de propiedad intelectual. No es asesoría legal.
- Registro de marca (nombre, logo, personaje) como paso posterior: consultar con abogado de PI.

## 6. Libro de marca mínimo (1 documento)

Estrategia en una página, logo y reglas, color con roles y contraste, tipografías, textura/cristal, voz con ejemplos de “suena a” y “no suena a”, personaje con reglas, motion, ejemplos de aplicación, hacer / no hacer. Exporta también los **tokens** (CSS variables) que el sitio consumirá.

## 7. Entrega al sitio web

Define y entrega: archivo del personaje en sus versiones, **espacios reservados** en el sitio (hero, 404, carga, éxito de formulario, estado vacío, pie), reglas de aparición (máximo 1 por pantalla, nunca tapa la CTA), y su comportamiento de movimiento. Mientras el personaje no esté listo, el sitio usa un hueco con medidas y se actualiza solo con reemplazar el archivo.

## 8. Preset MUKIWA (datos ya decididos)

- Significado: no definirse por lo que no se eligió (etiquetas de origen, tono, clase, barrio, apellido, títulos); “ver más allá de las etiquetas”. La marca habla de cómo miras a la gente, nunca de quién sufre más.
- Jerarquía de mensajes: FEEL DA VYBZ (línea maestra) · VYBZ NEVA LIE (creencia) · VYBZ NEVA DIE (movimiento) · WE MOVE OUR LIFE BY VYBZ (estilo de vida) · VYBZTAR (la persona).
- Paleta: lima #C5ED2E, azul #0068FB, blanco #FFFFFF, casi negro #232323. Tipos: Satoshi, Cygnito Mono, KNERD, Inter. Logo burbuja con “MU” y “KIWA” en colores contrastados; el punto de la I es el ojo (“The MUKIWA Eye”, pupilas/estados variables, estructura fija).
- Agencia: MUKIWA DEPARTMENT; departamentos: Graphic Design Dept. · Visual Edits Dept. · Creative Direction Dept.
- Personaje: secundario, el logo limpio sigue siendo lo principal. Dirección: cara de dibujo animado retro (nariz redonda grande, un ojo grande con corte, ceja arqueada, sonrisa amplia, perilla), su peinado real (tazón/mullet con línea rapada en zigzag), guantes blancos, ropa negra oversize actual (Y2K), contorno grueso uniforme, color plano con un acento. El boceto encargado por Fiverr no se usó ni se pagó y no es utilizable.
- Estilo del sitio: cristal solo en botones/tarjetas/nav; textura táctil como mundo; el personaje es la única figura plana y sin cristal.
- Tono: directo, creativo, seguro, humano; slogan del plugin “Made for Editors.”; nunca “rodar”.

## 9. Verificación

Cada pieza pasa: legible a 32 px, contraste ≥4.5:1 en texto, funciona en fondo oscuro y claro, ningún elemento rompe la jerarquía de mensajes, la mascota no tapa la CTA, derechos claros por escrito, y alguien ajeno entiende la marca en 5 segundos.