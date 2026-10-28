# Actualización de skills Kiwa (27–28 oct 2026)

Para quien abra esta carpeta sin contexto. Lee primero `CLAUDE.md`, luego esto.

## Qué pasó
Las skills de Bryan se reorganizaron: se fusionaron las repetidas y **todas llevan ahora el prefijo `kiwa`**. Los cambios están en la rama `claude/upgrade-skills-21-oct` (PR #9, en borrador, hacia `main`). Si `main` aún no lo trae, cámbiate a esa rama o espera al merge.

## Skills actuales
| Skill | Para qué | Reemplaza a |
|---|---|---|
| `kiwa-watch-learn` | Bajar, ver, escuchar, analizar y aprender de videos o audio; pasa lo aprendido al profe del oficio | `mukiwa-grab`, `mukiwa-learn`, `mukiwa-ver-videos` |
| `kiwa-web-ui` | Diseño web de básico a premium: arquetipos, animación y efectos, estructura, qué conviene y qué no, estilo MUKIWA | `adrian-saenz-hostinger-premium-website` y lo visual de las `crear-web-*` |
| `kiwa-web` | Conectar, construir y publicar sitios en Hostinger. Modos: portfolio, servicio-cliente, saas, afiliados | `crear-web-portfolio`, `crear-web-como-servicio`, `crear-web-saas-suscripcion`, `crear-web-afiliados-amazon` |
| `kiwa-marca-mascota` | Dirección de marca, dibujo retro cartoon, mascota MUKIWA | `direccion-de-marca-y-mascota`, `retro-cartoon`, `retro-cartoon-mascota` |
| `kiwa-instagram` | Carruseles y estudio de feed | `slide-maker`, `instagram-feed-studio` |
| `kiwa-<nicho>` (13 profes, en `profes/<nicho>/`) | Un profe por oficio | `profe-<nicho>` |

Profes: cinematografia, color-grading, composicion-visual, diseno-grafico, editor-asistente, efectos-visuales, iluminacion, imagenes-ia, motion-graphics, narrativa-y-direccion, negocio-creativo, sfx-audio, video-con-ia. Cuatro son nuevos (color-grading, imagenes-ia, sfx-audio, negocio-creativo).

**`kiwa-web-ui` y `kiwa-web` van siempre juntas:** una decide cómo se ve, la otra qué se construye.

## Dónde está cada cosa
- Skills: `skills/<nombre>/SKILL.md`. Profes: `profes/<nicho>/SKILL.md` (índice en `profes/INDEX.md`).
- Lecciones aprendidas de videos: `skills/kiwa-watch-learn/library/` (índice en `library/INDEX.md`).
- Los modos de `kiwa-web` están en `skills/kiwa-web/modos/<modo>/MODO.md`; `skills/kiwa-web/MAPA-DE-ARCHIVOS.md` dice dónde vive cada referencia.
- `kiwa-watch-learn` está enlazada en `.claude/skills/`, así que se activa sola al abrir este repo en Claude Code.

## Reglas de trabajo (de `CLAUDE.md`)
- Conservar las lecciones. No borrar ni reemplazar carpetas enteras para actualizar código.
- No subir videos descargados, cookies, claves, audio privado ni archivos de trabajo (`_descargas`, `work`, `.venv`).
- Antes de cambiar algo, revisar `git status` y conservar cambios ajenos; trabajar en ramas.
- No decir que se vio todo un video si solo se revisaron muestras.
- Después de cada lección, clasificarla y alimentar al profe (`skills/kiwa-watch-learn/references/profesores.md`): fusionar, no reescribir profes enteros.
- Pruebas: `python3 -m unittest discover -s tests -v`. Hoy pasan 84 de 85; la que falla (`test_buzon...test_prefers_deno_then_node_in_path`) ya fallaba antes: espera que no haya `node` instalado.

## Qué no está resuelto
- **claude.ai sigue con las skills viejas** hasta que Bryan suba los `.skill` nuevos y quite las anteriores.
- **Drive** (carpeta "MUKIWA · Skills de Claude") no se actualizó desde la nube. Se sincroniza con `python3 tools/sync_drive.py` en el Mac de Bryan.
- **`mukiwa-ui-plugins` y `portfolio-marca-personal`** solo existen en el Mac y Drive de Bryan; no están en el repo.
- El Mac de Bryan tiene lecciones más nuevas sin commit (por ejemplo diseño gráfico con más lecciones que el repo). Antes de hacer pull allí, hay que hacer commit para evitar conflictos.
- Sin acceso a YouTube desde la nube: esas sesiones solo pueden analizar archivos que se les suban.
- `kiwa-web` y `kiwa-web-ui` no se han probado construyendo una web real tras la fusión.

## Generar los paquetes para subir
`python3 tools/build_skills.py` crea un `.skill` por skill en `dist/` (18 en total).
