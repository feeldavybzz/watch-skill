# Oídos: cómo conseguir el texto de un video (probado 2026-10-30)

Claude no oye: lee **texto con tiempos**. Esta guía junta lo que ya funcionó. Todo lo que sigue lo hace un solo comando:

```
python3 scripts/oir.py FUENTE --out work/oidos [--lang es] [--whisper] [--budget 100]
```

`FUENTE` = link, video/audio local o un transcript (.srt .vtt .json3 .txt .md). Deja `transcript.md` + `oidos.json` (qué peldaño, cuántas palabras, qué falló y por qué, confianza). Códigos de salida: `0` listo · `3` parcial (repetir el MISMO comando) · `2` sin oídos.

## La escalera

| # | Peldaño | Quién lo hace | Cuándo |
|---|---------|---------------|--------|
| 1 | Transcript que Bryan ya tiene | `oir.py` (FUENTE o `--transcript`) | Siempre primero |
| 2 | Chrome + Sider (YouTube) | el agente, a mano (ver SKILL.md «Chrome: Sider») | Si Chrome está conectado y se quiere traducción/Resumen; es transcript real pero traducido |
| 3 | Subtítulos con yt-dlp (del autor, luego automáticos) | `oir.py` | **5 s** en la VM el 2026-10-30 (45 min, ≈10 000 palabras, sin 429) |
| 4 | Whisper (faster-whisper) sobre el audio | `oir.py` / `transcribe.py` | Faltan subtítulos, o el audio debe mandar (`--whisper`) |
| 5 | Nada | — | «sin-oidos» = **voz no verificada**, nunca «sin voz» (Regla #2) |

Los peldaños 2 y 3 se pueden invertir: si Chrome no está conectado, 3 va primero. No te quedes esperando a Chrome.

## Dónde corre cada cosa

| Lugar | yt-dlp (YouTube) | Whisper | Notas |
|-------|------------------|---------|-------|
| **VM del dispositivo** (`device_bash`) | Sí. `pip install --user --break-system-packages yt-dlp faster-whisper` | Sí, ≈2x tiempo real con `small` y 4 núcleos | Corta a 180 s por llamada → usar `--budget 100` y repetir el comando. Alcanza HuggingFace y PyPI |
| **Contenedor** | No alcanza YouTube | Sí, lento (≈1x con 2 núcleos). `pip install --user --break-system-packages --proxy "$HTTPS_PROXY" faster-whisper` | Sirve para audio que ya está en el contenedor |
| **Terminal del Mac de Bryan** | Sí | Sí, el más rápido | `watch.py` ya lo hace todo en un paso: el audio manda |

Copiar scripts a la VM: `device_commit_files` a una carpeta de la carpeta conectada, y desde la VM `cp` a un `$HOME/oirtest` local (no trabajar dentro de la carpeta conectada: no deja borrar intermedios).

## Whisper reanudable (VM)

```
python3 oir.py "URL" --out $HOME/work-x --lang es --whisper --budget 100   # repetir hasta estado «completo»
```
- Cada segmento se guarda al terminar y el avance queda en `transcript.md.progreso.json`; al repetir continúa, no reinicia.
- La **primera corrida** baja el modelo (`small` ≈ 460 MB, ~1 min) y avanza poco: es normal.
- Un video de 45 min con `small` = unas 14 llamadas. Si solo hace falta cotejar términos o cifras, transcribe un tramo y compáralo con los subtítulos (`oidos.json → cotejo`). Si hay prisa, `--model base` es más rápido y menos preciso.
- Música: si el idioma sale con probabilidad < 0.8 el estado es «dudoso»: **música, voz no verificada**, no es teoría.

## Qué tan fiable es cada texto

- **Subtítulos automáticos**: flujo fiable, pero fallan términos técnicos y cifras (el 2026-10-30 convirtieron «LUT» en «loots»). Confianza media-alta. Siempre se contrastan con pantalla cuando hay un número o un valor.
- **Subtítulos del autor**: los mejores, pero muchos videos no los traen (`subtitulos-del-autor: no hay pista`).
- **Whisper**: confianza alta en frases; mejor con términos mezclados español/inglés («Current Settings as default»). Aun así un número dudoso se confirma en pantalla.
- **Cotejo**: si hay subtítulos Y Whisper completos, `oidos.json → cotejo` lista los números que solo aparecen en uno de los dos. Esos son los que hay que mirar en los frames.
- **Resumen de Sider/IA**: segunda mano (lo marca `ingest_transcript.py` como `summary`); baja la confianza de la teoría.

## Fallos y qué hacer

| Salida de `oir.py` | Significa | Qué hacer |
|---|---|---|
| `HTTP 429 …` | límite de peticiones: acceso, no ausencia de voz | pasar a Whisper o a Sider; reintentar subs más tarde |
| `YouTube pide sesión/verificación` | bloqueo | cookies solo si el sitio está en `permisos.json` (CLAUDE.md); si no, pedir permiso a Bryan |
| `no hay pista en el idioma pedido` | sin subs en ese idioma | probar otro `--lang` o Whisper |
| `NO_WHISPER` / `NO_MODEL` | falta la librería o el modelo | instalar; si no se puede, pedir transcript a Bryan. No rodear con otras rutas |
| `yt-dlp no está instalado` | — | `pip install --user --break-system-packages yt-dlp` y `PATH="$HOME/.local/bin:$PATH"` |

## Extensiones

No hace falta instalar otra: el problema de Sider no es la precisión sino que Claude no puede leer su panel como texto. Con `oir.py` + Whisper se evita. Instalar extensiones sigue siendo decisión de Bryan.

## En la lección

`Tipo de «oídos»` y `Confianza` copian lo que dice `oidos.json` (peldaño, idioma, palabras, cobertura). Si el estado fue «parcial», «dudoso» o «sin-oidos», va en la primera línea de la lección.
