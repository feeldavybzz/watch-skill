#!/usr/bin/env python3
"""Medidas objetivas para edición y diseño (Watch no las tiene):
  - Ritmo: cortes detectados, cortes por minuto, duración de planos y si acelera hacia el final.
  - Gancho: cortes en los primeros 3 y 10 segundos, y cuándo llega el primer corte.
  - Paleta: colores dominantes medidos en las capturas, con hex y porcentaje.

Uso: python metrics.py --manifest DIR/visual/manifest.json [--video VIDEO] [--threshold 0.30]
     -> imprime JSON. Si el manifest ya trae los cortes de escena, no vuelve a recorrer el video.

Límites: la detección de escena mide cambios de imagen, no la intención del editor. Puede contar
como corte un flash, un zoom brusco o un scroll rápido, y no ve fundidos lentos. Los números son
aproximados (≈) y sirven para comparar videos entre sí, no como verdad absoluta. La paleta sale
de capturas comprimidas en JPEG: los hex son cercanos, no exactos."""
import argparse, json, os, statistics, sys
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_frames as ef

def rhythm(cuts, start, end):
    cuts = sorted(t for t in cuts if start < t < end)
    span = end - start
    if span <= 0: return None
    shots = [b-a for a,b in zip([start]+cuts, cuts+[end])]
    q = span/4
    per_q = [sum(1 for t in cuts if start+i*q <= t < start+(i+1)*q) / (q/60) for i in range(4)]
    return {
        "cortes": len(cuts),
        "cortes_por_minuto": round(len(cuts)/(span/60), 1),
        "plano_promedio_s": round(statistics.mean(shots), 2),
        "plano_mediana_s": round(statistics.median(shots), 2),
        "plano_mas_corto_s": round(min(shots), 2),
        "plano_mas_largo_s": round(max(shots), 2),
        "cortes_por_minuto_por_cuarto": [round(x, 1) for x in per_q],
        "tendencia": "acelera" if per_q[3] > per_q[0]*1.25 else "frena" if per_q[3] < per_q[0]*0.8 else "estable",
        "gancho": {
            "cortes_0_3s": sum(1 for t in cuts if t < start+3),
            "cortes_0_10s": sum(1 for t in cuts if t < start+10),
            "primer_corte_s": round(cuts[0]-start, 2) if cuts else None,
        },
    }

def palette(files, n=6, tile=48):
    ims = []
    for f in files:
        try: ims.append(Image.open(f).convert("RGB").resize((tile, tile)))
        except Exception: pass
    if not ims: return []
    strip = Image.new("RGB", (tile*len(ims), tile))
    for i, im in enumerate(ims): strip.paste(im, (i*tile, 0))
    q = strip.quantize(colors=n, method=Image.MEDIANCUT)
    pal = q.getpalette(); total = tile*tile*len(ims)
    out = []
    for count, idx in sorted(q.getcolors(), reverse=True):
        r, g, b = pal[idx*3:idx*3+3]
        out.append({"hex": "#%02X%02X%02X" % (r, g, b), "porcentaje": round(100*count/total, 1)})
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--manifest", required=True)
    ap.add_argument("--video"); ap.add_argument("--threshold", type=float, default=0.30)
    a = ap.parse_args()
    with open(a.manifest, encoding="utf-8") as f: man = json.load(f)
    start, end = man["range_s"]
    cuts = man.get("scene_cuts")
    if cuts is None or man.get("scene_threshold") != a.threshold:
        cuts = ef.scene_times(a.video or man["video"], a.threshold, start, end)
    files = [f["file"] for f in man["frames"] if f.get("reason") == "detail"] or [f["file"] for f in man["frames"]]
    print(json.dumps({"ritmo": rhythm(cuts, start, end), "paleta": palette(files),
                      "umbral_escena": a.threshold, "aproximado": True}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
