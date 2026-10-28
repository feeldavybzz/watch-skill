---
name: kiwa-sfx-audio
description: "Profesor MUKIWA de sonido para video: música, voz, efectos de sonido, ambiente y mezcla, que aprende de las referencias que Bryan envía. Sabe fijar el audio antes del video de IA (textura, voces, eventos), mezclar voz y música con ducking y fades, limpiar ruido de voz, elegir música instrumental y planear cómo cambia el sonido entre planos. Usar cuando Bryan pida música para un video, mezclar o nivelar audio, limpiar una voz, poner efectos de sonido, diseñar el ambiente, un J cut o L cut, el volumen para reels y YouTube, o pregunte cómo se hace algo de sonido. No es para efectos especiales de rodaje ni visuales: eso es `kiwa-efectos-visuales`."
metadata:
  nicho: sfx-audio
  herramientas: "ffmpeg, ElevenLabs, RNNoise, Premiere Pro, DaVinci Resolve"
  lecciones: 6
  actualizado: "2026-10-28"
---

# Kiwa · SFX y audio
> Decide el sonido antes que la imagen cuando la imagen es cara de rehacer, mezcla voz y música con ducking y fades, limpia solo el ruido de la voz y planea cómo cambia el ambiente entre planos (el sonido cambia antes que la imagen). Todo lo aprendido viene de **guías y demos de edición y de video con IA**: ningún video enseñó diseño sonoro ni foley a fondo, y los números de mezcla son puntos de partida (≈), no estándares probados.

Instrucciones para HACER el trabajo, no resúmenes de videos. Cada técnica aparece una sola vez;
la fuente va entre corchetes [n] (ver Fuentes). Valores exactos solo si se vieron o dijeron;
si no, con ≈. Si dos fuentes se contradicen, anotarlo en "Dudas abiertas".
Aquí «SFX» es **sonido**. Los efectos especiales de rodaje (SFX) y los visuales (VFX/CGI) están en `kiwa-efectos-visuales`. Para cortar el montaje, combínalo con `kiwa-editor-asistente`; para audio de video con IA, con `kiwa-video-con-ia`.

## Cómo trabajar (cualquier pieza)
1. **Si el video se genera con IA, el audio va primero**: iterar audio cuesta menos que repetir una escena completa [4].
2. **Separa tres decisiones**: textura (calidad de micro, ruido, proximidad), voces (quién, acento, actitud, cómo dice cada frase) y eventos (qué se oye, cuándo entra y qué queda de fondo) [4].
3. **Escucha el audio entero antes de seguir**: frases, interlocutores, pausas, sonidos; corrige ahí, no después de generar el video [4].
4. **Limpia la voz solo de ruido**, conservando los niveles; coloca los efectos sobre palabras exactas y revisa la lista de efectos a mano antes de mezclar [2].
5. **La música nunca compite con la voz**: baja sola mientras se habla (ducking) [1] y entra y sale con fades [2].
6. **Revisa el resultado completo con audio, una persona**: la IA solo ve fotogramas y no puede escuchar; busca cortes a mitad de palabra y el volumen de la música [1].

## Áreas
### Diseño sonoro antes del video de IA [4]
- Prompt de audio con **duración exacta**, indicación explícita de si hay música y narrador («cero música, cero narrador»), una parte de estética (micro, ruido, entorno, voces) y una de ejecución con los eventos en orden y, cuando importan, con su segundo (ej. un clic a 2,2 s, un corte duro al final) [4].
- Varios interlocutores y diálogo + ambiente + efectos en una misma pista [4].
- Ese audio aprobado se adjunta después al prompt de video [4].

### Cambios de sonido entre planos [3][5]
- En una transición entre locaciones, **corta la música y mete el ambiente de la nueva locación antes de la revelación**; el sonido cambia antes que la imagen [3].
- **J cut**: el audio del siguiente plano empieza antes de verlo; **L cut**: el audio del plano anterior continúa sobre el siguiente; ayudan a que los diálogos suenen más naturales [5].

### Voz [1][2]
- **Nivel de salida**: voz a **−13,5 LUFS** (el que dice usar YouTube) [1].
- **Limpieza**: solo ruido, sin tocar niveles; RNNoise es gratis y local; ElevenLabs es de pago para ruido difícil [2].
- **Pausas**: una pausa menor de ≈0,2 s entre palabras suena comprimida [2].

### Música [1][2]
- Instrumental, **80–110 BPM**, tonalidad que no choque con la voz, al menos **90 s más larga** que el video [2].
- Mezcla de partida: voz a 0 dB y música a `volume=0.13` (≈ −18 dB), **fade-in de 2 s** y **fade-out de 3 s** [2]. Música lo-fi que baja sola cuando se habla (ducking) [1].
- Una biblioteca de efectos y música normalizada a ≈ **−20 LUFS** con techo de **−1,5 dBFS** [2].

### SFX con IA guiados por tu voz (Adobe Firefly) [6]
- Prompt corto del sonido («sfx transiciones whoosh»), duración (8–10 s) y un **audio guía**: se graba la voz imitando el ritmo y el volumen que quieres y el generador respeta duración y pulsos. Salen variaciones; se elige y se alinea a los impactos de la animación (en After Effects, proyecto en capas con nulos). El resultado sonoro no se pudo evaluar.

## Por herramienta
### ffmpeg
- Para transcribir, extraer el audio en mono, 16 kHz, PCM s16le [2]. La música se mezcla con `volume=0.13` y fades de 2 s y 3 s [2].
### Premiere Pro / DaVinci Resolve
- Sin fuente todavía: no se ha aprendido de un video real cómo se hace el ducking, la nivelación a LUFS ni los J/L cuts en cada programa.
### ElevenLabs / Seed Audio
- ElevenLabs aparece como opción de pago para limpiar ruido difícil [2]. Seed Audio es el modelo con el que la guía de Seedance prepara el audio de la escena [4]; los ajustes de cada uno no se han visto en pantalla.

## Recetas
- **Reel con voz y música**: voz limpia (solo ruido) → música instrumental 80–110 BPM más larga que el video → música a ≈ −18 dB bajo la voz con ducking → fade-in 2 s y fade-out 3 s → voz a ≈ −13,5 LUFS de salida → revisar entero con audio [1][2].
- **Escena de video IA**: texto del audio (textura, voces, eventos, duración exacta) → generar y escuchar entero → corregir → adjuntar al video [4].

## Errores comunes
- Generar el video sin haber decidido el audio → es lo más caro de rehacer [4].
- Cortar solo por silencios → cortes sobre consonantes y pausas que importaban; revisar a mano [2].
- Pausas por debajo de ≈0,2 s → suena comprimido [2].
- Dar por bueno el montaje sin escucharlo → la IA no puede oír [1].
- Cambiar la imagen y el sonido a la vez en una transición → el sonido debe adelantarse [3].

## Checklist antes de entregar
- [ ] Audio decidido antes del video (si es video IA) y escuchado entero [4].
- [ ] Voz sin ruido y sin cortes a mitad de palabra [1][2].
- [ ] Música bajo la voz con ducking y fades [1][2].
- [ ] Nivel de salida de la voz comprobado (≈ −13,5 LUFS) [1].
- [ ] Transiciones: el sonido cambia antes que la imagen [3].
- [ ] Revisión final con audio por una persona [1].

## Para MUKIWA
- Visual Edits: reels 9:16 con voz a ≈ −13,5 LUFS y música que baja sola [1][2].
- Creative Direction: en anuncios con video de IA, aprobar la banda sonora antes de gastar créditos de video.
- Pendiente de fusionar (`docs/pendientes-de-fusionar/`): el flujo de reel de marca incluye elegir voz y música escuchando opciones antes de montar y exportar a ≈ −14 LUFS.

## Dudas abiertas
- Los valores de [2] (BPM, −18 dB, fades, −20 LUFS con techo −1,5 dBFS) salen de **guías escritas** con herramientas y afiliados propios y no se han comprobado con una edición terminada de referencia.
- [1] dice que −13,5 LUFS es el nivel de YouTube: no se verificó con una fuente de la plataforma. El flujo de reel de marca (pendiente de fusionar) exporta a ≈ −14 LUFS: dos números cercanos sin criterio para elegir.
- [4] es una guía pública resumida sin oír el MP3 de ejemplo; el prompt completo de audio no se reproduce aquí.
- [3] y [5] solo tocan el sonido de pasada: no dan niveles ni herramientas.
- Falta aprender: diseño sonoro y foley a fondo, efectos de sonido (bibliotecas, capas, sincronía a la imagen), mezcla y masterización (EQ, compresión, de-esser), ducking y nivelación en Premiere y DaVinci (Fairlight), música con IA (Suno, ElevenLabs Music), voz en off y clonación de voz, audio para reels y para YouTube con valores comprobados.
- [6] Solo se vio la interfaz (en portugués): no se oyó el efecto resultante ni se ve cómo se sincronizó; no hay niveles ni formato de exportación.

## Fuentes
- [1] Editar un video en crudo con Claude: video largo, reels y carrusel — https://youtu.be/viztypMn7D0 · `references/lecciones/editor-asistente-claude-flujo-reels-carrusel.md`
- [2] Editar video con Claude Code: tres guías escritas (cortes, pausas, música, subtítulos, Remotion) — https://learnwithhasan.com/guide/claude-code-video-editing/ · https://www.mejba.me/es/blog/claude-code-video-editing-workflow · https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code.md · `references/lecciones/guias-claude-code-cortes-pausas-musica-subtitulos.md`
- [3] Dirigir un anuncio de 30 s con video de IA (Higgsfield, Seedance), sección de transiciones y sonido — https://youtu.be/kFKpcCHkuPI · `references/lecciones/dirigir-anuncio-con-video-ia-higgsfield-seedance.md`
- [4] Escenas consistentes con Seedance 2.5: referencias, audio primero y dirección de escena (AiLendra Labs) — https://ailendra.com/ailab/lite/seedance-25-escenas/ · `references/lecciones/escenas-consistentes-seedance-ailendra.md`
- [5] Seis formas de editar una escena (StudioBinder, Shot List ep. 10), sección J cut y L cut — https://youtu.be/FVR8zz8ci2k · `references/lecciones/seis-formas-de-editar-una-escena-studiobinder.md`
- [6] Efectos de sonido con Adobe Firefly guiados por tu voz (@tcastro.motion) — reel de Instagram, archivo local · `references/lecciones/sfx-adobe-firefly-guia-de-voz-tcastro-motion.md`
