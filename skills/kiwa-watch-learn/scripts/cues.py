#!/usr/bin/env python3
"""Detecta en la transcripción los momentos en que el presentador señala algo en pantalla
("fíjate", "como ves", "acá tenemos", "look here"...) para capturarlos con --at.
Watch obliga a una segunda pasada manual; aquí sale sola en la primera.

Uso: python cues.py transcript.md [--max 12] [--min-gap 8]   -> imprime JSON [{t, text}]
Es una heurística: puede marcar muletillas ("mirá, la verdad...") y perder señales sin
palabra clave. Las capturas resultantes son evidencia a revisar, no conclusiones."""
import argparse, json, re

PATTERNS = [
    r"\bf[ií]ja(?:te|os|nse)\b", r"\bsi te f[ií]jas\b", r"\bmir(?:a|á|en|ad)\b(?! que)",
    r"\bcomo (?:ves|ven|ver[aá]s|pueden ver|pod[eé]s ver|se ve)\b",
    r"\b(?:ac[aá]|aqu[ií]|ah[ií]) (?:tenemos|tengo|ves|ven|est[aá]|aparece|me dice|vemos)\b",
    r"\ben (?:la )?pantalla\b", r"\beste (?:diagrama|gr[aá]fico|bot[oó]n|men[uú]|panel|c[oó]digo|archivo|link|enlace)\b",
    r"\b(?:hac[eé]|haz|dale) (?:click|clic)\b", r"\b(?:click|clic) en\b", r"\bvamos a abrir\b",
    r"\blook (?:at|here)\b", r"\bnotice\b", r"\bas you can see\b", r"\bhere (?:we have|you can see|is)\b",
    r"\bon (?:the )?screen\b", r"\bthis (?:diagram|chart|button|menu|panel|code|file)\b", r"\bclick (?:on|here)\b",
]
CUE = re.compile("|".join(PATTERNS), re.I)
LINE = re.compile(r"^\[(\d+):(\d{2}):(\d{2}(?:\.\d+)?)\]\s*(.*)$")

def find_cues(lines, max_n=12, min_gap=8.0, lead=0.5):
    hits = []
    for line in lines:
        m = LINE.match(line.strip())
        if not m: continue
        t = int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))
        text = m.group(4)
        if CUE.search(text) and (not hits or t - hits[-1]["t"] >= min_gap):
            hits.append({"t": round(t + lead, 2), "text": text})   # lo señalado suele verse justo después
    if len(hits) > max_n:                                          # repartir a lo largo del video
        hits = [hits[round(i*(len(hits)-1)/(max_n-1))] for i in range(max_n)] if max_n > 1 else hits[:1]
    return hits

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("transcript")
    ap.add_argument("--max", type=int, default=12); ap.add_argument("--min-gap", type=float, default=8.0)
    a = ap.parse_args()
    with open(a.transcript, encoding="utf-8") as f:
        print(json.dumps(find_cues(f.read().splitlines(), a.max, a.min_gap), ensure_ascii=False, indent=1))
