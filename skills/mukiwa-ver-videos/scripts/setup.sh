#!/usr/bin/env bash
# Instala/actualiza SIN Homebrew y sin depender de tu Python viejo:
#  - yt-dlp (binario independiente, siempre la última versión)  -> ../bin/yt-dlp
#  - deno (lo necesita YouTube para resolver desafíos)          -> ../bin/deno
#  - ffmpeg incluido (imageio-ffmpeg) y gallery-dl (pip)
set -e
BIN="$(cd "$(dirname "$0")/.." && pwd)/bin"; mkdir -p "$BIN"
ARCH="$(uname -m)"
echo "Bajando yt-dlp..."; curl -fL --progress-bar -o "$BIN/yt-dlp" https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos
chmod +x "$BIN/yt-dlp"; xattr -d com.apple.quarantine "$BIN/yt-dlp" 2>/dev/null || true
echo "Bajando deno..."
if [ "$ARCH" = "arm64" ]; then D=deno-aarch64-apple-darwin; else D=deno-x86_64-apple-darwin; fi
curl -fL --progress-bar -o "$BIN/deno.zip" "https://github.com/denoland/deno/releases/latest/download/$D.zip"
unzip -o -q "$BIN/deno.zip" -d "$BIN" && rm "$BIN/deno.zip"; chmod +x "$BIN/deno"; xattr -d com.apple.quarantine "$BIN/deno" 2>/dev/null || true
python3 -m pip install -q --upgrade gallery-dl imageio-ffmpeg certifi 2>/dev/null || true
echo "yt-dlp $("$BIN/yt-dlp" --version)"; echo "deno $("$BIN/deno" --version | head -1)"
python3 -c "import imageio_ffmpeg;print('ffmpeg',imageio_ffmpeg.get_ffmpeg_exe())" 2>/dev/null
echo "Listo. Prueba: python3 \"$(cd "$(dirname "$0")" && pwd)/grab.py\" 'URL'"
