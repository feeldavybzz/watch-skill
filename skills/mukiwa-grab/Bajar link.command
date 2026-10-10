#!/bin/bash
# Doble clic: abre Terminal, te pide el link y lo baja a _descargas/
cd "$(dirname "$0")"
python3 scripts/grab.py
echo; read -n 1 -s -r -p "Listo. Presiona una tecla para cerrar..."
