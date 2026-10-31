# Efectos con video de IA: fondo generado + recorte, gesto + comentario en llamas, juego → calle
> Tres recetas de reels que combinan acción real con transformación generada, con las comprobaciones que hay que hacer y lo que cuestan.

- **Fuentes**: https://www.instagram.com/p/DeMmA5AP9QQ/ (efecto de construcción, InVideo + ChatGPT, Oscar Merino) · https://www.instagram.com/p/DfAEetmoMHf/ (comentario que se quema, patrocinado por Artlist) · https://www.instagram.com/p/DfDGkkVOycz/ (del videojuego a la escena, atribuido a Higgsfield)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local (en DeMmA5AP9QQ confunde «InVideo»; en DfDGkkVOycz no recupera explicación técnica); descripciones abiertas; fotogramas muestreados
- **Confianza**: baja-media — procesos incompletos: faltan prompts, nodos y ajustes legibles

## Teoría (lo que se dijo)
- DeMmA5AP9QQ: foto del lugar → conectar InVideo con ChatGPT → adjuntar foto y prompt → generar y descargar la animación → colocar al presentador encima en la timeline. (La guía y el prompt se daban al comentar GUÍA; **no se obtuvieron**.)
- DfAEetmoMHf: grabar el gesto de quemar, capturar el comentario, subir video e imagen a Artlist, indicar el efecto y generar. El autor nombra «Kling 4.0».
- DfDGkkVOycz: «PAUSE THE GAME, IT'S THE FEDS», creado con Higgsfield; el desglose se ofrecía por comentario.

## Práctica (lo que se ve)
- DeMmA5AP9QQ: edificios junto al mar → resultados con terreno y maquinaria; recorte del presentador con transparencia en DaVinci/Fusion (MediaOut1) delante del fondo. No se ven los nodos del recorte.
- DfAEetmoMHf: tarjeta de comentario con fuego y campos de referencia, duración y resolución; **la pantalla muestra el coste de generación**.
- DfDGkkVOycz: sofá con juego en CRT → transición a una calle con motocicletas, barbería, automóvil y luces policiales.

## Cruce teoría ↔ práctica
- El efecto de construcción mezcla **dos tareas**: transformar el fondo y separar al sujeto. No se puede atribuir al conector una máscara perfecta sin revisar.
- El nombre del modelo, la configuración y los prompts **no se pueden certificar** con lo visible.

## Receta paso a paso (criterio nuestro a partir de las fichas)
1. Planifica el gesto y la posición del elemento gráfico **antes** de generar el efecto.
2. Genera o transforma el fondo; por separado, recorta al sujeto.
3. Revisa escala, bordes (cabello y manos), iluminación y continuidad del fondo con la cámara real **en movimiento**, no en un fotograma.
4. Para dar el salto a otro mundo, convierte una acción cotidiana en la puerta de entrada y mantén la continuidad de energía y ambientación (DfDGkkVOycz).
5. Alternativa futura a estudiar: composición local con fuego autorizado y máscaras, sin generación de pago.

## Para MUKIWA
- Visual Edits / Creative Direction: referencia narrativa de «puerta a otro mundo» y de composición sujeto + fondo generado.
- **No se generó ni se subió material de Bryan, no se consumieron créditos y no se comentó.**

## Límites
- Costes y disponibilidad de InVideo, Artlist y del modelo nombrado: sin verificar. No clasificar como flujo gratuito.
- El prompt completo no se recuperó. Sin guía, credenciales ni prueba propia no se marca como workflow instalado.

## Conecta con
- [[evaluar-edicion-automatica-y-subtitulos-con-claude]] · [[doom-scroll-efecto-nano-banana-kling-artzenmedia]]
