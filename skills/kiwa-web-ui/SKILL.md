---
name: kiwa-web-ui
description: "Diseño web de nivel básico a premium: arquetipos visuales, animación y efectos (GSAP, scroll, parallax, 3D, cursor), estructura de páginas, imágenes y una guía de qué conviene y qué no (rendimiento, Windows y reduced-motion, caché, errores que rompen el sitio sin avisar). HTML, CSS y JS estáticos, sin build ni npm, listos para Hostinger. Úsala cuando Bryan pida diseñar, rediseñar o mejorar la parte visual de una web, landing o portfolio, o pregunte qué estilo o efecto usar y cuál no. Para construir el sitio completo (portfolio, web para cliente, SaaS, afiliados), conectarlo y publicarlo, usa kiwa-web junto con esta."
---

# kiwa-web-ui — diseño web, de lo básico a lo premium

Genera sitios **estáticos** (HTML + CSS + JS puro + librerías locales: GSAP, Lenis, Three.js solo cuando hace falta) con calidad de estudio, **sin build, sin npm, sin frameworks**. La persona suele no ser técnica: quiere una carpeta que pueda subir por FTP y que se vea increíble.

Es **una de dos skills hermanas**:

| Skill | Qué hace |
|---|---|
| **kiwa-web-ui** (esta) | Cómo se ve y se siente: arquetipos, efectos, animación, estructura, imágenes, errores a evitar, qué conviene y qué no. |
| **kiwa-web** | Construir el sitio completo según su tipo (portfolio, web para cliente, SaaS, afiliados), conectar Hostinger, publicar. Siempre usa esta para lo visual. |

## Cuándo usarla
- Web nueva de cualquier tipo (landing, portfolio, restaurante, agencia, blog, evento, galería…).
- "Hazla premium / con wow", rediseñar, mejorar lo visual, elegir un estilo o un efecto.
- La pregunta "¿esto conviene o no?" sobre un efecto, una librería o un estilo → `reference/11-que-conviene-y-que-no.md`.

**No la uses** para editar un código complejo ya existente (herramientas directas), ni para una app con backend o base de datos (eso es `kiwa-web`, modos saas/afiliados), ni para documentación sin ambición de diseño.

## Lee esto primero (en este orden)
1. `reference/09-environment-detection.md` — qué herramientas tiene la persona (Python, curl). Obligatorio al empezar.
2. `reference/04-critical-gotchas.md` — errores que rompen el sitio en silencio. Obligatorio.
3. `reference/10-deployment-and-cache.md` — la caché es la mayor fuente de confusión tras publicar. Obligatorio.
4. `reference/07-windows-troubleshooting.md` — Windows trae `prefers-reduced-motion` activado y el sitio se ve "muerto". Obligatorio.
5. `reference/02-archetypes.md` — elige **UN** arquetipo. Nunca combines dos.
6. `reference/06-diversity-guardrails.md` — los proyectos de ejemplo son referencia de calidad, no plantillas.
7. `reference/11-que-conviene-y-que-no.md` — beneficios y costos de cada decisión.

Según lo que se necesite: `01-stack-and-conventions.md` (estructura, orden de scripts, IIFE) · `03-effects-catalog.md` (más de 40 efectos listos para copiar) · `05-image-and-asset-pipeline.md` (Openverse, WebP, fotos propias, imágenes con IA) · `08-pre-deploy-checklist.md` (antes de dar por terminado) · `12-estilo-mukiwa.md` (si es para MUKIWA o Bryan lo pide) · `13-motion-en-web.md` (animación dirigida: secciones por scroll, formas que se transforman, springs, cámara única, lista de prohibidos, cristal solo en controles).

## Flujo (pocas preguntas, decide en silencio)
1. **Volcado.** La persona cuenta su proyecto. Anota tipo, nombre, tono, si tiene fotos, funciones especiales. No preguntes todavía.
2. **Mínimo de preguntas** (un solo mensaje, máximo 5, cada una de 15 palabras o menos): nombre de marca, fotos propias o de Openverse (por defecto Openverse), objetivo del botón principal, qué debe incluir sí o sí, cuántas páginas (por defecto una). **No preguntes** paleta, fuentes, layout, efectos ni nada técnico.
3. **Arquetipo en silencio** según la tabla de `02-archetypes.md`. Si dos encajan igual, rota al que menos se ha usado.
4. **Preparación en silencio** (carpetas, librerías, imágenes, conversión a WebP) con los scripts de `scripts/`. Sin Python existe la variante en bash. Revisa si salió WebP o se quedaron los originales y usa las extensiones reales.
5. **Genera** `index.html`, `styles.css`, `main.js`, `lib/manifest.js` con la receta del arquetipo y las reglas de abajo.
6. **Verifica**: `python scripts/verify_project.py --project <carpeta>`; si reporta fallos, corrígelos y repite.
7. **Vista previa local** con `python3 -m http.server 8765` en segundo plano (`file://` bloquea `fetch()`).
8. **Entrega**: dónde está la carpeta, que la vista previa ya corre, una frase de cómo publicar. No des una charla técnica.

## Reglas que no se rompen (detalle en `04-critical-gotchas.md`)
1. Nada de `<script type="module">` con imports relativos: scripts clásicos `defer` + patrón IIFE + `window.__BRAND__`. Única excepción: el puente ESM que `01-stack-and-conventions.md` §16 permite para los modos SaaS y afiliados de `kiwa-web`.
2. `.htaccess` en la raíz (copia `templates/htaccess.template`) y `?v=AAAAMMDD` en cada `<link>` y `<script>`.
3. Scroll nativo por defecto. Lenis solo si el arquetipo lo pide.
4. CSS defensivo para `.reveal[data-split]` (que nunca quede invisible).
5. Cero dependencias npm en runtime: solo archivos en `lib/`.
6. No filtres micro-interacciones con `prefers-reduced-motion` (solo lo realmente intrusivo).
7. Todas las imágenes en WebP; nunca mezcles `.jpg`, `.png` y `.webp`.
8. Contenido crítico escrito en el HTML; el JS solo lo enriquece.
9. Cada `init*` dentro de `safe(fn, nombre)` con try/catch.
10. IntersectionObserver con umbral ≤ 0.05 y un seguro de 6 s que revela lo que siga oculto.
11. Splash con doble seguro (animación CSS de 4.5 s + JS).
12. Montajes idempotentes (`if (target.children.length > 0) return;`).
13. Contenido primero, animación después.
14. Sin estela de miniaturas siguiendo el cursor por defecto: parece un fallo, no un efecto.

## Qué es "premium" aquí
- **Primera pantalla con impacto**: que no parezca una plantilla.
- **Efectos con razón**: ninguno duplica a otro; 4 o 5 por página y una sola "firma".
- **Móvil como composición propia**, no un escritorio aplastado.
- **Copy editorial**: sin "desbloquea", "transforma", "secretos", "revolucionario".
- **Robustez antes que espectáculo**: una web sólida con menos wow gana a una vitrina rota.

## Diversidad
Cada sitio debe sentirse distinto: rota arquetipo, familia de paleta, topología de layout y efecto firma. La persona nunca debe pensar "esto se parece a otra web que hiciste".

## Archivos
```
SKILL.md                       ← esta entrada
intake-template.md             ← guion corto para preguntar
reference/
  01-stack-and-conventions.md  ← estructura, IIFE, puente ESM
  02-archetypes.md             ← 10 arquetipos (paleta, tipografía, efectos)
  03-effects-catalog.md        ← 40+ efectos con código
  04-critical-gotchas.md       ← errores aprendidos en proyectos reales (A–E)
  05-image-and-asset-pipeline.md
  06-diversity-guardrails.md
  07-windows-troubleshooting.md
  08-pre-deploy-checklist.md
  09-environment-detection.md
  10-deployment-and-cache.md
  11-que-conviene-y-que-no.md  ← beneficios y costos, qué evitar
  12-estilo-mukiwa.md          ← estilo de marca por defecto
  13-motion-en-web.md          ← motion dirigido en la web (Prompt Motion)
templates/htaccess.template
scripts/ download_libs · openverse_fetch · webp_convert · verify_project
```
