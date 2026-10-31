# Ajustes de grabación Sony (S-Log3) y la diferencia entre PowerGrade y LUT
> Qué preguntarse antes de copiar una receta de cámara o instalar un look, y por qué un antes/después Log vs. terminado no prueba nada.

- **Fuentes**: https://www.instagram.com/p/DeMWZ_aDlMx/ (ajustes de grabación Sony y S-Log3, 5 láminas) · /DfAyGDMSgdT/ (PowerGrade «Kodak Gold» para Resolve)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: ninguno (láminas y reel sin voz); descripciones abiertas; fotogramas
- **Confianza**: media — conceptos sí; compatibilidad con la cámara de Bryan **no verificada**

## Teoría (lo que se dijo)
- DeMWZ_aDlMx: XAVC HS 4K, 50p, 100 Mbps, 4:2:2 10-bit, S-Log3 y PP8, más Save/Load Settings. Instagram marca el contenido como generado con IA; **no es una demostración real del menú**.
- DfAyGDMSgdT: PowerGrade para Resolve mediante comentario «Kodak»; menciona Sony, Canon, Apple, Lumix (la pantalla agrega DJI).

## Práctica (lo que se ve)
- Gallery de Resolve con variantes, nodos y antes/después Log vs. «Kodak Gold». **El PowerGrade anunciado no se obtuvo**.

## Cruce y aclaraciones
- **Codec, muestreo, fps y perfil son decisiones distintas.** No es una configuración universal de «máxima calidad».
- S-Log3 exige exposición y gestión de color apropiadas. **No atribuir menor tamaño de archivo solo a usar 10 bits.**
- Un **PowerGrade** puede transportar estructura de nodos; **una LUT no es lo mismo**. Hay que comprobar espacio de entrada, exposición y balance de blancos antes de juzgar el look.
- Un antes/después **Log → imagen terminada mezcla normalización y estilo**: no demuestra emulación exacta de película.

## Receta paso a paso
1. Investiga el modelo concreto de cámara antes de fijar códec, muestreo, fps y perfil; usa estos valores solo como punto de partida.
2. Normaliza el Log (CST) **antes** del look creativo; mantén separados nodos de normalización y de estilo.
3. Antes de aplicar un look de terceros, comprueba que el material coincida en espacio de entrada, exposición y balance de blancos.

## Para MUKIWA
- Se suma a la familia de color (LUTs, máscaras, balance de blancos) del Kiwa de color; no se crea otro. Ver la lección de S-Log3 y Resolve ya existente.

## Límites
- No se obtuvo ningún archivo ni se comprobó coste. Compatibilidad con el equipo de Bryan sin verificar.

## Conecta con
- [[s-log3-rodaje-y-grade-en-resolve-gaku-lange]] · [[color-en-davinci-sistema-de-nodos-scopes-mascaras-y-matching-alwaysjoan]] · [[numero-f-apertura-y-paradas]]
