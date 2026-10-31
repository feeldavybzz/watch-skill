> Texto íntegro de la skill `instagram-feed-studio`.

# Instagram Feed Studio (MUKIWA DEPT.)

Construye un "Content Studio" web privado donde el equipo y el cliente organizan el próximo bloque de publicaciones de Instagram de una marca, ven cómo queda el perfil y dejan listo el plan. Es el mismo sistema que se hizo para ARIAT Panamá ("Tierra Adentro"): úsalo como referencia y fuente de verdad.

Responde siempre en español casual, directo. Iteración controlada: si piden cambiar una cosa, cambia solo esa.

## 1. Datos que necesitas antes de construir

Pregunta solo lo que falte (una sola ronda, con AskUserQuestion si hay varias dudas):

1. **Marca / cliente** y handle de Instagram (ej. `ariatpanama`), nombre visible, bio, categoría, seguidores/seguidos (para el mock del perfil). Logo o captura del perfil para el avatar.
2. **Fotos:** link de la carpeta de Google Drive (se leen con el conector de Drive) o archivos adjuntos.
3. **Estructura del bloque:** cuántas publicaciones (por defecto 24), cuántos reels (por defecto 4), cadencia (por defecto 3 por semana: lunes, miércoles, viernes → 8 semanas).
4. **Título de campaña** para el encabezado (ej. "Tierra Adentro."), nunca un genérico.
5. **Contraseña** del estudio (la da el usuario; se guarda solo como hash SHA-256 en un secret).
6. **Dónde publicarlo:** por defecto Cloudflare Worker en `*.workers.dev` de la cuenta del usuario (gratis, sin dominio). Si no hay acceso a Cloudflare, ofrece la alternativa: Artifact con base de datos compartida (skill `artifact-capabilities`).

## 2. Arquitectura (Cloudflare, igual que ARIAT)

- **Worker** `<cliente>-content-studio` (módulo ES, un solo archivo `worker.mjs`).
  - Login: `POST /api/login` {name, password} → compara SHA-256 con `PASSWORD_HASH`; cookie `HttpOnly; Secure; SameSite=Strict`, sesión 24 h en D1; rate limit 12 intentos / 10 min por IP hasheada.
  - `GET /api/state` → estado de la grilla + versión + quién está en línea (visto < 35 s) + últimos accesos + fotos subidas.
  - `POST /api/state` → guarda con **control de versión optimista** (409 si otra persona cambió). Valida en servidor: longitud exacta, reels únicos, ids permitidos, sin fotos repetidas en todo el feed (portadas + slides), `ratio` dentro de la lista, `caption` ≤ 2200. Guarda revisión en `revisions`.
  - `POST /api/upload` → imagen JPG/PNG/WebP (verifica magic bytes), ≤ 10 MB, nombre saneado (sin `<>"'`\&`), se guarda en KV `assets/up/<id>.<ext>` y en D1 `photos`.
  - Estáticos desde KV (`index.html`, `assets/*`); `assets/*` con `Cache-Control: private, max-age=86400`, lo demás `no-store`. Cabeceras de seguridad y CSP estricta (`default-src 'self'`, `img-src 'self' data: blob:`).
  - Chequeo de `Origin` en todo lo que no sea GET.
- **D1**: tablas `board(id=1,state,version,updated_by,updated_at)`, `sessions`, `access_log`, `limits`, `revisions`, `photos`.
- **KV** `<cliente>-content-studio-assets`: `index.html`, `allowed.json` (ids de Drive permitidos), `assets/N.jpg` (fotos redimensionadas), fuentes, logo, `_backup/…`.
- **Secret** `PASSWORD_HASH`. Observabilidad (logs) activada.

## 3. Funciones del frontend (todas ya probadas en ARIAT)

- Encabezado: eyebrow `CLIENTE / CONTENT STUDIO`, título grande de campaña (Bootzy o la display de la marca, `clamp(46px,7.2vw,112px)`), resumen "N fotos + N reels · N semanas · N por semana".
- Controles glass: Feed completo / Mes 1 / Mes 2 / Publicación · Claro / Oscuro · Amplio / Móvil · Presentar.
- **Mock del perfil de Instagram**: avatar, usuario, stats, bio, botones, grilla 3 columnas en **3:4** (así muestra Instagram el perfil), la más reciente arriba a la izquierda.
- **Editar grilla**: clic selecciona (con 240 ms de espera para distinguir doble clic), clic en otra intercambia, arrastrar y soltar, elegir foto del banco reemplaza la portada, Deshacer, Restablecer.
- **Doble clic** en cualquier publicación → vista de publicación tipo Instagram.
- **Panel flotante glass al seleccionar**: en desktop ancho al costado izquierdo, en laptop barra abajo al centro, en móvil centrado. Botones: ＋ Hacer carrusel / Editar carrusel (principal, grande), Ver publicación, Cambiar portada ↓.
- **Carruseles** (hasta 10 fotos): editor en modal grande con las slides arriba (‹ › Portada ×) y el banco de imágenes abajo en **cuadros grandes 1:1** (`grid-auto-rows:max-content`, `minmax(170px,1fr)`), buscador, "Solo disponibles", subir fotos. Se guarda solo al pulsar Guardar. En la grilla el carrusel se desliza (scroll-snap, puntitos, flechas al hover) y lleva el ícono de carrusel.
- **Vista de publicación (clon de Instagram, fondo negro)**: media con carrusel deslizable, header con avatar + usuario + Seguir, íconos like/comentar/enviar/guardar, y panel con:
  - **Formato** (se reencuadra al instante y se guarda):
    | Ratio | Nombre | Medida |
    |---|---|---|
    | 4:5 | Vertical (recomendado, por defecto) | 1080 × 1350 |
    | 3:4 | Vertical alto | 1080 × 1440 |
    | 1:1 | Cuadrado | 1080 × 1080 |
    | 5:4 | Horizontal | 1080 × 864 |
    | 4:3 | Horizontal | 1080 × 810 |
    | 1.91:1 | Panorámico | 1080 × 566 |
    | Reel | 9:16 fijo | 1080 × 1920 |
    Botón ↻ Girar (4:5↔5:4, 3:4↔4:3). Aviso: en carrusel todas las slides usan el formato de la portada; en el perfil la miniatura se recorta a 3:4. **Verifica con una búsqueda web que las medidas sigan vigentes** antes de construir.
  - **Pie de foto**: genérico de la marca (3–4 plantillas alternadas, con hashtags de campaña) + Editar (contador /2200) + Usar genérico. Escapar HTML siempre; hashtags y @ resaltados.
- **Banco de imágenes** lateral: buscador, "Solo fotos sin usar", etiquetas "En post N" / "Carrusel N" / "Subida", doble clic amplía, **＋ Subir fotos** y arrastrar archivos (se redimensionan en el navegador a 2048 px JPEG 0.86; HEIC → pedir JPG).
- **Plan**: tabla semana/día/post/contenido/formato y **Descargar plan** (CSV con BOM: tipo, formato, medida, fotos, pie de foto, links originales).
- **Colaboración**: sincroniza cada 8 s, muestra quién está en línea y últimos accesos, "Copiar enlace" (usa `location.origin`).
- **Temas**: oscuro = negro + lime `#CEFF00` (o el acento de la marca); claro = alto contraste con negros y **azul `#0068FB` con texto blanco** en pills activas, botones principales negros. Glass selectivo (pills, paneles, botones), nunca toda la página.
- Tipografías: Satoshi para UI y textos de ayuda, mono (Cygnito Mono) para metadatos, display de la marca para el título. En desktop (≥1024 px) subir tamaños (cuerpo 15 px, botones 14 px).

## 4. Proceso de construcción

1. **Material primero**: lista la carpeta de Drive (paginando), descarga y redimensiona cada foto (lado largo ~1600–2048 px, JPEG), arma `ASSETS=[{id,name,short,src,url}]` y `allowed.json`. Selección inicial: repartir fotos variadas (producto, lifestyle, detalle) con los reels en posiciones regulares.
2. Escribe `worker.mjs` e `index.html` en el scratchpad; `node --check` a todo el JS.
3. **Prueba local** con Playwright/Chromium (preinstalado) sirviendo el HTML con rutas mockeadas antes de subir nada.
4. Crea recursos en Cloudflare (D1 + tablas, KV, Worker con bindings `DB`, `ASSETS`, secret `PASSWORD_HASH`, observabilidad). Sube assets a KV con metadata `{type}`.
5. Verifica en vivo con una **sesión QA temporal** (insertar fila en `sessions` con hash de un token propio, cookie en el navegador) — nunca escribir la contraseña del usuario en formularios. Al terminar: borra la sesión QA y revierte cualquier cambio de prueba en `board`/`revisions`.
6. Entrega: URL `https://<worker>.<subdominio>.workers.dev`, contraseña que definió el usuario, resumen corto (HECHO / URL / PENDIENTE).

## 5. Lecciones aprendidas (no repetir errores)

- **Nunca** reemplaces data-URIs con regex greedy al armar el HTML: en ARIAT el `src` del avatar se tragó 1.7 MB de CSS/base64. Después de construir, parsea con `DOMParser` y confirma que ningún `src` pase de 200 caracteres y que la página pese < 150 KB.
- Si la grilla de un editor sale aplastada dentro de un contenedor flex con altura fija, usa `grid-auto-rows:max-content`.
- Dialogs de `<dialog>`: usa `width:fit-content` y lados con `flex:none`; no dependas solo del evento `close` para reabrir otra vista (llama la función directo desde los botones).
- Especificidad: `.x button:not(#id)` gana a `.x #id`; usa `.x button#id` para el botón principal.
- Doble clic sobre elementos que se re-renderizan no dispara `dblclick`: detecta el doble clic manualmente con un timer.
- Cambios sobre una app ya en uso: construye el nuevo HTML con reemplazos exactos (cada marcador debe aparecer 1 vez), sube primero una copia `_staging/index.html` con `fetch` mockeado para POST (así no tocas la grilla real), prueba, guarda `_backup/index-FECHA-vN.html` y recién ahí publica. Compara hashes SHA-256 de lo que pegas en el navegador contra el archivo local.
- Dashboard de Cloudflare vía navegador: la API interna funciona con `fetch('/api/v4/...')` + header `x-atok` (de `/api/v4/system/bootstrap`) y nada más; agregar otros headers devuelve 403. Para sacar archivos grandes del navegador sin filtros, escríbelos a una tabla temporal de D1 y léelos con el conector; bórrala al final.
- Cambios de DNS, dominios o secrets requieren permiso explícito del usuario; pídelo con pasos exactos si el sistema lo bloquea.
- Pestañas en segundo plano congelan timers, scroll suave y eventos `close`: si una prueba "falla" por tiempo, verifica el estado real antes de concluir que hay bug.

## 6. Variantes

- **Sin Cloudflare**: mismo frontend como Artifact publicado con la capacidad de base de datos compartida para el estado y la de archivos para las subidas (carga primero `artifact-capabilities`).
- **Otro cliente** (Columbia Tours, Chess King, Timberland…): cambia avatar, handle, bio, acento de color y plantillas de pie de foto; mantén la estructura.