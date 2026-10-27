---
name: kiwa-instagram
description: "Todo para Instagram en una skill: carruseles listos para publicar (descubrimiento de marca, sistema visual, voz y copy, big idea, estructura de slides, HTML con fuentes embebidas, PNG retina y caption) y el estudio privado de preview del feed (grilla editable, carruseles, formatos, pies de foto, vista tipo Instagram, compartido con contraseña). Úsala cuando Bryan pida carruseles, slides, posts, hooks, copy o plantillas para Instagram, o un estudio para previsualizar y ordenar el feed de una marca o cliente."
---

# kiwa-instagram — carruseles + estudio de feed

Une `slide-maker` e `instagram-feed-studio`. El texto de cada una está **entero** en `references/`.

## Elige el camino
| Pedido | Lee |
|---|---|
| Crear carruseles, slides o posts; sistema visual y copy de una marca; PNG y caption listos para publicar | `references/carruseles-slide-maker.md` (proceso de 8 etapas, con validación en varias) |
| Un estudio privado para ver y ordenar el feed: grilla editable, carruseles, formatos, vista tipo Instagram, con contraseña | `references/estudio-de-feed.md` |
| Primero el contenido y luego previsualizarlo | Carruseles → estudio de feed, en ese orden |

## Reglas que cruzan los dos textos
- Es un proceso con **etapas validadas por la persona**: no saltes una etapa marcada para validar.
- El estudio de feed es privado y con contraseña; la contraseña la da la persona y se guarda solo como hash en un secret del servidor, nunca en el repositorio ni en el chat.
- Cambios de DNS, dominios o secrets requieren permiso explícito; pídelo con los pasos exactos.
- Si la marca es MUKIWA, el sistema visual parte de `kiwa-web-ui/reference/12-estilo-mukiwa.md` (negro + azul eléctrico + lima, vidrio solo en elementos interactivos).
- Si el estudio se publica como sitio, usa `kiwa-web` para el alojamiento.
