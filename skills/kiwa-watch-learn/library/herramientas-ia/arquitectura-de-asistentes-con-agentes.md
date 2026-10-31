# Arquitectura de un asistente con agentes («Jarvis»): capas, orden y criterio de selección
> Una sola lección que consolida nueve reels que repiten la misma idea: separar equipo, modelo, arnés, contexto, herramientas, memoria, skills, tareas programadas, canales e interfaz.

- **Fuentes**: https://www.instagram.com/p/DeabErVp_AL/ (nueve pasos) · /Dd1ux3PNjsn/ (cinco pasos) · /DfF0Y6bnSAK/ (siete pasos) · /DfFSE1TEprr/ (cinco proyectos) · /DcNLTtzOTIY/ (doble aplauso) · /De1o2dFi44O/ · /DcJ3VAZy1mg/ (crítica) · /Dd4xIpYRruE/ (God's Eye View) · /DeosZ3QSd0X/ (narrativo, gimnasio)
- **Fecha**: 2026-10-31
- **Tipo de "oídos"**: Whisper local; en varios el reconocimiento degrada nombres propios (**no se convierten en comandos ni enlaces**); De1o2dFi44O tiene transcripción poco fiable tras dos intentos y **no se completa por intuición**; Dd1ux3PNjsn y DfFSE1TEprr necesitaron un reintento offline en español
- **Confianza**: media en el mapa conceptual; **baja** en cualquier afirmación de ahorro, gratuidad o funcionamiento (nada se ejecutó)

## Teoría (lo que se dijo, sintetizado)
- Capas: **equipo/servidor** (VPS, laptop u ordenador viejo) → **modelo** → **arnés de agente** → **contexto** personal o laboral → **herramientas** (MCP: correo, calendario, navegador) → **memoria** persistente → **skills** de tareas repetidas → **tareas programadas** → **canales** (WhatsApp, Telegram) → **voz/interfaz**. El de siete pasos añade énfasis en la programación periódica; el de nueve añade memoria, canales y voz.
- Cinco proyectos propuestos: asistente, segundo cerebro / biblioteca de contexto, panel de vida/negocio, agente de contenido y equipo de agentes con coordinador.
- DcNLTtzOTIY: un disparador simple (dos aplausos) abre un conjunto fijo de herramientas; el tutorial pide Python, VS Code o Cursor, API key y voice ID de ElevenLabs.
- DcJ3VAZy1mg: parodia de un asistente futurista que «no puede ejecutar tareas»; propone decidir antes si se quiere ahorrar tiempo o dinero.

## Práctica (lo que se ve)
- Tarjetas de pasos, gráficos oscuros con acento azul o cian, interfaces circulares y un panel tipo «War Room». **Nunca** se ve código, configuración, permisos ni una ejecución verificable de las tareas programadas.

## Cruce teoría ↔ práctica
- **Una skill aporta un proceso; un MCP aporta acceso a una herramienta.** Tener uno no demuestra que el otro esté resuelto (síntesis nuestra).
- Automatización por evento (dos aplausos) **no es** un agente que razona sobre todo el ordenador. El tutorial es para Windows: no está demostrada su compatibilidad con el Mac.
- «Guía gratis» no implica que todos los servicios lo sean (servidor en nube, voz externa). El código «gratuito/open source» se separa del servicio de voz.
- «Acceso a todo lo que pasa en el planeta» (God's Eye View) es exageración promocional; no se verificó repositorio, latencia, autenticidad de feeds ni licencias de datos.
- Narrativa (DeosZ3QSd0X): demostrar una herramienta dentro de una situación con objetivo y consecuencia es más claro que una lista de funciones; **no** prueba backend, dispositivos ni permisos.

## Receta paso a paso (propuesta nuestra)
1. **Empieza por una función concreta** y define sus entradas y salidas antes de añadir accesos o canales. Ejemplo: preparar carpetas y listar el material de edición.
2. Mide el resultado: minutos ahorrados y dónde quedaron los archivos. **Evalúa voz y automatización por separado.**
3. Amplía accesos de forma incremental, comprobando la salida en cada paso.
4. Para un panel futuro: que muestre qué lecciones faltan por revisar y cuáles se repiten (esta biblioteca ya cumple parte del «segundo cerebro»).
5. Un agente de contenido necesita fuentes y revisión editorial: generar más guiones no es el objetivo.

## Para MUKIWA
- Referencia para el asistente editorial de Bryan (preparar un proyecto y presentar la lista de archivos antes de importar). Estética de ciencia ficción: **no confundir complejidad visual con fiabilidad ni ahorro medido**.
- **No se instaló nada, no se comentó ni se abrió ningún DM.** Se conserva como mapa conceptual; no marcar nada como instalado, gratuito ni con memoria persistente funcional.

## Límites
- Nombres como Hermes Agent o Letta (memoria) aparecen degradados por el reconocimiento; no se confirman.
- Quedan duplicadas entre sí DeabErVp_AL, Dd1ux3PNjsn y DfF0Y6bnSAK: se conservan los tres enlaces y las diferencias (memoria/canales/voz, programación periódica), **contadas como una sola lección**.

## Conecta con
- [[plugins-para-claude-code-promesas-y-verificacion]] · [[evaluar-edicion-automatica-y-subtitulos-con-claude]]
