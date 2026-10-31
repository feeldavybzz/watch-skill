# Editar video con Claude Code: tres guías escritas (cortes, pausas, música, subtítulos, Remotion)
> Tres guías públicas coinciden en el mismo patrón: transcripción con tiempo por palabra, corte decidido por el significado (no por silencios), animaciones y subtítulos en Remotion, y revisión humana final. Aportan valores concretos que el video de Melina Blanco no daba.

- **Fuentes** (artículos, no videos):
  - [A] Learn With Hasan, «Claude Code Video Editing: From Raw Recording to Published YouTube Video» — https://learnwithhasan.com/guide/claude-code-video-editing/
  - [B] Mejba Ahmed, «Claude Code video editing workflow» — https://www.mejba.me/es/blog/claude-code-video-editing-workflow
  - [C] Tella, «How to Use Remotion Agent Skills With Claude Code» — https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code.md
- **Fecha**: 2026-10-10
- **Tipo de "ojos" y "oídos"**: solo texto. Leídas con WebFetch (un resumen automático de cada página), sin abrir los repositorios ni probar nada. No hay audio ni imágenes. Los valores son lo que declaran los autores.
- **Aporte de los creadores**: ALTO en datos. Promocionan cosas: [A] un curso de pago y un boletín (el repo es gratis, licencia MIT); [B] enlaces de afiliado (Descript, Remotion, Epidemic Sound) y sus servicios; [C] es documentación divulgativa de Tella. Lo útil no está detrás de registro.
- **Confianza**: media. Cifras de tiempo y costos son de sus propias pruebas.

## Teoría (lo que dicen)
- [A] **Todo depende del primer paso**: transcribir con tiempo por palabra y que Claude decida qué cortar (tomas repetidas, falsos comienzos, muletillas) en un `cuts.json`. Salida: un mapa de palabra con tiempos, del que dependen los demás pasos. Prefiere AssemblyAI a Whisper por la calidad de la transcripción.
- [B] **La edición es semántica, no acústica.** Con un script de ffmpeg por silencios los cortes caían sobre consonantes y se borraban pausas que importaban. La limpieza de frases repetidas debe ser decisión humana.
- [B] Pausas entre palabras: umbral de **0,2 s** (probó de 0,15 a 0,35): por debajo de 0,2 s el audio suena comprimido; por encima de 0,25 s la mejora ya no se nota. Quitar muletillas en explicaciones técnicas, no en momentos narrativos (dan ritmo humano).
- [B] Música: solo instrumental, **80–110 BPM**, tonalidad que no choque con la voz, al menos **90 s más larga** que el video.
- [B] Mezcla: voz a 0 dB y música a `volume=0.13` (≈ −18 dB) con fade-in de **2 s** y fade-out de **3 s**. [A] Su biblioteca de efectos y música va normalizada a ≈ **−20 LUFS** con techo de **−1,5 dBFS**.
- [B] Transcripción: Whisper con granularidad por palabra (`verbose_json` + `word`), audio mono 16 kHz. Costo declarado 0,006 USD/min; 10 min tardan ≈ 40 s. Sin granularidad por palabra solo se obtienen tiempos por frase.
- [B] Subtítulos animados en Remotion: fuente **Inter 56 px, peso 800, trazo negro de 3 px**, palabra activa resaltada en violeta (#8B5CF6; luego #A78BFA).
- [A] Limpieza de voz: aislar la voz solo con quitar ruido, conservando niveles; hay opción gratis local (RNNoise) y otra de pago (ElevenLabs) para ruido difícil. Efectos de sonido colocados sobre palabras exactas, con **revisión manual** de la lista antes de mezclar.
- [A] Control antes de publicar: un verificador que detecta **palabras cortadas por la mitad y desfase del audio** (cita un desfase de 200 ms; sin tolerancia declarada). Las tres piezas de marca (texto de marca, colores, fuentes) deben coincidir o falla en silencio.
- [C] Remotion genera video desde código; **no edita metraje grabado**: los cortes los hace otra herramienta. Instalación: `claude plugin marketplace add remotion-dev/claude-code-plugin` y `claude plugin install remotion@remotion`, o `npx remotion skills add`. Habilidades: `/remotion-captions`, `/remotion-render`, `/remotion-markup`, `/remotion-studio`, etc.
- [C] Buenas prácticas de pedido: indicar duración, dimensiones, fps, orden y tiempos de escenas, texto literal, rutas de recursos permitidas, colores, fuentes y estilo de movimiento; **un cambio por vez**; movimiento contenido; revisar en Remotion Studio en vez de renderizar a cada paso; pedir que preserve lo existente y revisar el diff.

## Práctica (lo que dicen que hacen)
- [B] Flujo: (1) limpieza semántica en Descript sobre la transcripción (≈ 8 min por 30 min de grabación); (2) pausas a 0,2 s; (3) muletillas; (4) música; (5) extraer audio con ffmpeg; (6) mezclar con ffmpeg; (7) transcribir con Whisper; (8) subtítulos animados en Remotion; (9) bucle de revisión en Studio; (10) revisión final a **1,5x**, de 4 a 6 min por video de 10 min.
- [A] Flujo de seis skills encadenadas: cortar → elementos visuales sincronizados con las palabras → limpiar voz → efectos → título y miniaturas → subida privada.
- [B] Tiempos declarados: de ≈ 4 h a ≈ 25 min por video; render de 10 min con subtítulos simples ≈ 3 min en un MacBook Pro M2 (12–15 min con efectos complejos).

## Cruce teoría ↔ práctica
- Las tres coinciden en que el corte lo decide el significado y que hace falta una pasada humana. Es coherente con el video de [Melina Blanco], donde Claude avisa de que no puede escuchar el audio y marca minutos a revisar.
- Contradicción menor: [A] prefiere AssemblyAI y [B] Whisper; ambos dan tiempos por palabra. Nosotros usamos Whisper local.
- Los límites no coinciden: [A] probó solo en Windows 11 (Mac sin probar); [B] en MacBook Pro M2.

## Receta paso a paso
1. Transcribir con **tiempo por palabra** (Whisper local o equivalente).
2. Marcar a mano o con ayuda de la IA qué se corta por **significado**: tomas repetidas, falsos comienzos; conservar la última toma completa.
3. Reducir pausas a ≈ 0,2 s y quitar muletillas solo donde no den ritmo.
4. Limpiar la voz (solo ruido) y mezclar la música a ≈ −18 dB con fades de 2 s y 3 s.
5. Subtítulos animados con la palabra activa resaltada (Inter 56 px, peso 800, trazo 3 px como punto de partida).
6. Verificar: palabras cortadas, desfase de audio, ortografía de términos técnicos y marcas.
7. Revisar a 1,5x con audio antes de entregar.

## Para MUKIWA
- Valores de partida para el profesor `editor-asistente`: pausa 0,2 s, música −18 dB, fades 2/3 s, subtítulo 56 px/800/trazo 3 px. Comprobar con un video terminado de referencia antes de fijarlos como estándar propio.
- El plan de MUKIWA para clientes puede usar el mismo patrón: IA para el primer corte, decisión humana en el significado.

## Límites
- Solo leí resúmenes automáticos de las páginas; no abrí los repositorios, no probé las skills y no vi videos.
- Sin umbral de silencio en dB, sin relleno de cortes (padding), sin lista de muletillas ni tolerancia de desfase.
- Los precios de herramientas y los ahorros de tiempo son afirmaciones de los autores.

## Conecta con
- [[editor-asistente-claude-flujo-reels-carrusel]]
