# Qué conviene y qué no — guía rápida de decisiones de diseño web

Resumen en español de lo que dicen los demás archivos de esta skill. Cuando haya duda, manda el archivo citado entre paréntesis; esto es solo el mapa para decidir rápido.

---

## 1. Qué arquetipo conviene según el negocio
(Tabla completa y receta de cada uno en `02-archetypes.md`.)

| Tipo de proyecto | Conviene primero | Alternativa |
|---|---|---|
| Restaurante, izakaya, alta cocina | 02 Editorial Dark Warm | 09 Newspaper Editorial (si es una institución con historia) |
| Agencia de viajes, experiencias boutique | 01 Editorial Light Cream | 06 Magazine Multi-Page |
| Newsletter, revista | 03 Cinematic 3D Storytelling | 06 Magazine, 09 Newspaper |
| SaaS, tech, herramientas de desarrollo | 05 Mouse-Reactive Gradient | 04 Glassmorphism Modern |
| Bienestar, spa, hidratación | 08 Liquid Wave Backgrounds | 04 Glassmorphism |
| Estudio, agencia, portfolio | 07 Brutalist Grid | 03 3D, 05 Mouse |
| Lanzamiento de producto boutique | 10 Spline Embed Premium | 04 Glassmorphism |
| Publicación editorial | 06 Magazine | 09 Newspaper |
| Cultura, galería, evento | 07 Brutalist | 09 Newspaper |
| Café, artesanal | 01 Cream | 06 Magazine |
| Hotel boutique | 01 Cream | 02 Dark Warm |
| Vinoteca, sumiller | 02 Dark Warm | 03 3D |
| Cripto, web3 | 05 Mouse | 10 Spline |
| Arquitectura | 07 Brutalist | 09 Newspaper |
| Música clásica, sala | 03 3D | 06 Magazine |
| Surf, outdoor | 08 Liquid Wave | 05 Mouse |
| Marca personal, creador | 05 Mouse | 07 Brutalist |
| Portfolio de fotografía | 06 Magazine | 09 Newspaper |
| Despacho de abogados, profesional | 09 Newspaper | 02 Dark Warm |

**Regla de oro:** un solo arquetipo por sitio. Combinar dos produce una web confusa.

---

## 2. Efectos: qué aportan y qué cuestan
(Código y detalle en `03-effects-catalog.md`; el número es la sección.)

**Conviene, bajo riesgo**
- **Aparición al hacer scroll** (2.4, universal) y **parallax multicapa** en el héroe (2.5): dan vida sin pelear con nada.
- **Transiciones entre páginas con la View Transitions API** (3.1): sin JavaScript.
- **Botón que se eleva con sombra** (7.1): el preferido para los botones de acción principal.
- **Efectos sutiles sobre las tarjetas** (inclinación 3D, sombra, aberración cromática al pasar): según el propio catálogo, dan más impacto con menos riesgo que un efecto llamativo.
- **Inclinación 3D de máximo 7–9°** (5.1), **zoom ambiental tipo Ken Burns** (5.3), **grano SVG** (5.5): refinan sin distraer.
- **Mesh gradient animado en CSS** (4.3): fondo vivo sin WebGL.
- **Contenido escrito en el HTML**: si el JS falla, el sitio igual se lee.

**Úsalo con cuidado**
- **Lenis (scroll con inercia)**: bonito en teoría, pero frágil según la configuración de Windows (drivers de trackpad, escalado de pantalla, ahorro de batería). **Por defecto, scroll nativo.** Solo con Lenis si el arquetipo lo exige (B.1.4).
- **Three.js / escenas 3D** (4.1): solo para el arquetipo 03. Solo en escritorio; en móvil se omite.
- **Cursor personalizado y botones magnéticos** (1.1, 1.2): solo en dispositivos con hover; arranca el cursor con `opacity: 0` hasta el primer movimiento (A.3).
- **Letter scramble** (6.4): puede parpadear si se pasa rápido el ratón (B.7).
- **Texto dividido por letras o palabras** (6.1): cuidado con `<br>` y `<em>`, que se aplastan (A.4), y no combinar `.reveal` con `data-split` (A.4.5).
- **Paleta de comandos Cmd+K, puntos laterales de navegación**: son de panel de control; en una web editorial sobran.

**Evítalo**
- **Desplazamiento WebGL sobre fotos del héroe** (4.6): se probó y se quitó; puede voltear la imagen y se ve "de truco" en un contexto editorial. Mejor parallax + zoom ambiental + aberración al pasar.
- **Estela de miniaturas siguiendo el cursor** (C.11.5): casi siempre se lee como un error visual (las fotos se apilan encima). Solo en una sección claramente de juego, con pocas miniaturas y con interruptor para apagarla.
- **Lenis + scroll-snap a la vez**: no se llevan bien.
- **Inclinación 3D + magnético en el mismo elemento**: compiten.
- **Partículas + mesh gradient juntos**: saturan.

**Cuántos:** 4 o 5 efectos por página, **uno como firma** y el resto de apoyo. Si se acumulan scramble bilingüe, Cmd+K, puntos laterales, cursor y tilt, ya es un panel de control, no una web editorial.

---

## 3. Qué evitar siempre (los 12 mandamientos de `04-critical-gotchas.md`)
1. `<script type="module">` con imports relativos.
2. Filtrar micro-interacciones con `prefers-reduced-motion` (Windows lo trae activado y el sitio se ve plano).
3. Cursor visible en (0,0) antes del primer movimiento.
4. Dividir texto aplastando `<br>`.
5. Usar `mouseenter` / `mouseleave` (mejor `mouseover` / `mouseout` con `relatedTarget`).
6. Enlazar listeners con `setTimeout` global en vez de por elemento al renderizar.
7. `gsap.from` sobre los hijos de un ScrollTrigger fijado (deja tarjetas translúcidas).
8. Umbral de IntersectionObserver alto sin seguro de 6 s (la imagen no aparece).
9. Splash sin doble seguro.
10. Mezclar `.jpg`, `.png` y `.webp`.
11. `init*` sin `safe()` (un fallo rompe todos).
12. Contenido que existe solo cuando carga el JS.

Y la caché: sin `.htaccess` y sin `?v=AAAAMMDD`, Hostinger puede servir JS y CSS viejos durante horas o semanas tras subir una versión nueva (A.13, `10-deployment-and-cache.md`).

---

## 4. Qué beneficia y qué no, por decisión de estructura
| Decisión | Beneficia | Cuesta |
|---|---|---|
| **Estático, sin build ni npm** | Se sube por FTP y funciona; cualquiera lo mantiene | No hay backend: para cuentas, pagos o base de datos usa `kiwa-web` (modos saas/afiliados) |
| **Una página** (por defecto) | Rápido de hacer y de leer | Si hay menú, blog o detalle de portfolio, se necesitan varias |
| **Fotos propias** | Se ve auténtico, es de la persona | Hay que pedirlas y convertirlas a WebP |
| **Fotos de Openverse** | Cero fricción, sin clave | Menos personal; hay que acreditarlas (`credits.json`) |
| **Mucho efecto** | Primera impresión fuerte | Más puntos de fallo; el contenido nunca debe depender de la animación |
| **Móvil como composición propia** | Se ve intencional en el teléfono, que es donde llega el tráfico de enlaces | Hay que diseñarlo, no solo achicar el escritorio |
| **Texto editorial, sin hype** | Suena a persona real | Cuesta más escribirlo que rellenar con frases de moda |

**Prueba final antes de entregar:** `08-pre-deploy-checklist.md` + `python scripts/verify_project.py`. Mejor una web sólida con un poco menos de wow que una vitrina rota.
