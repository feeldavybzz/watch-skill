---
name: kiwa-web
description: "Construye, conecta y publica sitios web completos en Hostinger, en cuatro modos: portfolio personal, web para vender a negocios (con asistente de IA, calculadoras y captura de leads), SaaS de IA con cuentas, créditos y pagos (de prueba a reales) y web de afiliados de Amazon con base de datos de productos. Incluye conectar Hostinger, poblar productos, publicar, dominio y salida a producción. Úsala cuando Bryan diga hazme una web, un portfolio, un SaaS o una web de afiliados, publícala, ponle dominio o conéctame Hostinger. Lo visual (arquetipos, animación, efectos, qué conviene y qué no) lo pone kiwa-web-ui: usa siempre las dos juntas."
---

# kiwa-web — construir, conectar y publicar sitios completos

Una sola skill con **cuatro modos** y tres capacidades comunes. Sustituye a las cuatro skills `crear-web-*` y a la de diseño premium: nada se perdió, se reorganizó.

> **Siempre junto a `kiwa-web-ui`.** Esa skill decide cómo se ve (arquetipos, efectos, gotchas, caché, checklist). Esta decide **qué se construye y cómo se publica**. Si solo se instala una de las dos, falta la mitad.

## Regla de oro: haz solo lo que se pidió y detente
- "conéctame Hostinger" → solo conecta y verifica.
- "hazme una web / portfolio / SaaS / web de afiliados" → solo construye. No publiques, no añadas IA, no cobres.
- "publícala / ponle el dominio" → solo publica.
- Cambios sobre un proyecto existente → solo edita lo pedido, respetando su estilo.
Al final ofrece **una sola frase** con el siguiente paso natural ("¿la publico en tu hosting?") y no lo empieces solo. Lee el estado cada vez: ¿conectado?, ¿existe el proyecto?, ¿publicado?

## 1. Elige el modo
| Lo que pide | Modo | Empieza por |
|---|---|---|
| Un portfolio, página personal, "sobre mí", web para mostrar su trabajo y que lo contraten | **portfolio** | `modos/portfolio/MODO.md` |
| Una web para un negocio o cliente, algo que se vende; asistente de IA, calculadora, lector de documentos, leads | **servicio-cliente** | `modos/servicio-cliente/MODO.md` |
| Una app de IA con cuentas, créditos y suscripción ("quiero cobrar por…") | **saas** | `modos/saas/MODO.md` |
| Una web de comparativas y afiliados de Amazon con productos | **afiliados** | `modos/afiliados/MODO.md` |
| Solo diseño: "dame ideas", "¿qué estilo?", "mejórala visualmente" | — | `kiwa-web-ui` |
| Solo conectar o publicar | común | `comun/reference/12-hostinger-connect.md` / `13-hostinger-deploy.md` |

Si el pedido mezcla dos modos (p. ej. portfolio con tienda), arranca por el que define la estructura y trata lo demás como extensión; no mezcles sus invariantes sin leerlos.

## 2. Capacidades comunes
- 🔌 **Conectar Hostinger**: `comun/reference/12-hostinger-connect.md`. Necesita **Node.js 24+**; el chequeo está en `comun/scripts/diagnostico.sh` (o `.ps1` en Windows).
- 🎨 **Construir**: el modo elegido + `kiwa-web-ui` para lo visual. Necesita **Python 3** (ayudantes, conversión a WebP, vista previa local); sin Python degrada con gracia (`kiwa-web-ui/reference/09-environment-detection.md`).
- 🚀 **Publicar**: `comun/reference/13-hostinger-deploy.md`, más `kiwa-web-ui/reference/10-deployment-and-cache.md` (`.htaccess` y `?v=AAAAMMDD`; sin ellos Hostinger sirve archivos viejos).
- ✅ **Verificar** antes de decir que está listo: `kiwa-web-ui/scripts/verify_project.py` y `kiwa-web-ui/reference/08-pre-deploy-checklist.md`.

## 3. Reglas siempre activas
**Comunicación.** La persona **no es técnica**. Cero jerga: no digas "proxy", "endpoint", "API", "scraper", "deploy"; di "el asistente", "la clave de la IA", "publicar la web", "saco los datos de tus enlaces". Ejecuta tú todos los comandos; lo único manual son clics en el navegador (entrar a Hostinger, pegar una clave, pegar enlaces). Anuncia antes de actuar, celebra los hitos (✅), nunca muestres un error en bruto, **verifica antes de afirmar**.

**Calidad web** (detalle en `kiwa-web-ui/reference/04-critical-gotchas.md`): scripts clásicos `defer` + IIFE; `.htaccess` y `?v=`; scroll nativo por defecto; contenido escrito en el HTML; cada `init` dentro de `safe()`; el contenido primero y la animación después; la robustez gana al espectáculo.

**Honestidad.** No inventes proyectos, clientes, premios, cifras ni reseñas de una persona o negocio reales. Si no lo dieron, no va en la página; lo provisional se marca como provisional. Las claves (Gemini, OpenAI, etc.) no se pegan en el chat ni se guardan en el repositorio: van en el archivo de configuración del servidor, como indica cada modo.

**Pagos.** En el modo SaaS el sistema de cobro empieza **de prueba (mock)**, claramente etiquetado, y solo pasa a cobros reales cuando la persona lo pide y el producto ya funciona (`modos/saas/reference/18-go-live-playbooks.md`).

Si una regla y un adorno chocan, gana la regla.

## 4. Variables de entorno y límites
- Todo corre en el PHP del propio plan de Hostinger (sin VPS). Los proxies de IA son PHP + cURL contra el nivel gratuito de Gemini, con la clave en el servidor.
- Imágenes con IA: Node 18+ y la clave de OpenAI de la persona.
- Afiliados: el extractor de productos necesita Python y el navegador de Scrapling; la skill lo instala.
- Una base de datos dentro de `public_html` se borra en cada publicación: va **un nivel por encima** (`modos/saas/reference/15-backend-proxy.md`).

## 5. Modo sin preguntas (opcional)
Copia el contenido de `recommended-settings.json` (permisos de los propios scripts de la skill, nada destructivo) dentro de `~/.claude/settings.json` una sola vez.

## 6. Dónde está cada archivo
Los textos de cada modo conservan los nombres originales de sus referencias (`04-critical-gotchas.md`, `12-hostinger-connect.md`…). `MAPA-DE-ARCHIVOS.md` dice en qué skill y carpeta está cada una.

```
SKILL.md                      ← este enrutador
MAPA-DE-ARCHIVOS.md           ← nombre de archivo → ruta
recommended-settings.json
comun/                        ← conectar y publicar en Hostinger, diagnóstico
modos/
  portfolio/                  ← nichos, estructura, mejorar uno existente, módulos con datos reales
  servicio-cliente/           ← vender la web, IA (chat, lector de documentos, calculadoras, leads), imágenes con IA
  saas/                       ← catálogo de 11 SaaS, Gemini, cuentas, créditos, pagos de prueba y reales
  afiliados/                  ← esquema de producto, base de datos, páginas generadas, extractor de Amazon
```
