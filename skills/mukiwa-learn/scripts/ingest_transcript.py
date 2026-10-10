#!/usr/bin/env python3
"""Los 'oídos' (vía texto): normaliza cualquier transcripción/resumen a un .md con marcas de tiempo.

Acepta: .srt .vtt .json3 (YouTube) .json (Whisper/faster-whisper segments) .txt/.md (pegado de
Sider, resumen de YouTube, SpeakApp, etc. con o sin tiempos).
Uso: python ingest_transcript.py ARCHIVO --out transcript.md [--kind auto|captions|summary]
Si el texto NO tiene tiempos, se marca como 'sin-tiempos' (útil para teoría, no para alinear con frames).
Si parece un RESUMEN (Sider, IA) en vez de transcripción literal, lo marca 'summary':
 es útil pero de segunda mano -> la lección debe indicarlo.
"""
import argparse, json, re, sys, os

def ts(sec):
    sec=float(sec); return f"{int(sec//3600):02d}:{int(sec%3600//60):02d}:{sec%60:05.2f}"

def parse_time(s):
    s=s.replace(",",".").strip(); p=s.split(":")
    p=[float(x) for x in p]
    while len(p)<3: p.insert(0,0)
    return p[0]*3600+p[1]*60+p[2]

def collapse_repeat(x):
    """'A B C A B C' -> 'A B C' (auto-subs repiten cada frase dentro del mismo bloque)."""
    w=x.split(); n=len(w)
    for k in range(n//2, 0, -1):
        if n % k == 0 and w[:k]*(n//k) == w: return " ".join(w[:k])
    h=n//2
    if n>=4 and n%2==0 and w[:h]==w[h:]: return " ".join(w[:h])
    return x

def from_srt_vtt(txt):
    out=[]; blocks=re.split(r"\n\s*\n", txt.replace("\r",""))
    for b in blocks:
        m=re.search(r"([\d:.,]+)\s*-->\s*([\d:.,]+)", b)
        if not m: continue
        text=" ".join(l.strip() for l in b[m.end():].split("\n") if "-->" not in l and l.strip() and not l.strip().isdigit())
        text=re.sub(r"<[^>]+>","",text)
        text=collapse_repeat(re.sub(r"\s+"," ",text).strip())
        if text: out.append((parse_time(m.group(1)), text))
    # VTT auto-captions de YouTube duplican líneas: dedupe consecutivo
    ded=[]
    for t,x in out:
        if ded and (x==ded[-1][1] ): continue
        ded.append((t,x))
    return ded

def from_json(txt):
    d=json.loads(txt)
    if isinstance(d,dict) and "events" in d:   # json3 YouTube
        return [(e["tStartMs"]/1000, "".join(s.get("utf8","") for s in e.get("segs",[])).strip())
                for e in d["events"] if e.get("segs")]
    segs = d.get("segments", d) if isinstance(d,dict) else d
    return [(s["start"], s["text"].strip()) for s in segs]

def from_plain(txt):
    out=[]; pat=re.compile(r"^\s*\[?\(?(\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d+)?)\)?\]?\s*[-–:]?\s*(.*)$")
    for line in txt.splitlines():
        m=pat.match(line)
        if m and m.group(2): out.append((parse_time(m.group(1)), m.group(2).strip()))
        elif line.strip() and out: out[-1]=(out[-1][0], out[-1][1]+" "+line.strip())
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("file"); ap.add_argument("--out",required=True)
    ap.add_argument("--kind",default="auto"); a=ap.parse_args()
    raw=open(a.file,encoding="utf-8",errors="ignore").read(); ext=os.path.splitext(a.file)[1].lower()
    timed=True
    if ext in (".srt",".vtt"): segs=from_srt_vtt(raw)
    elif ext in (".json",".json3"):
        try: segs=from_json(raw)
        except Exception: segs=from_plain(raw)
    else:
        segs=from_plain(raw)
    if not segs:
        timed=False; segs=[(0,l.strip()) for l in raw.splitlines() if l.strip()]
    kind=a.kind
    if kind=="auto":
        low=raw.lower()
        kind="summary" if any(k in low for k in ["resumen","summary","key points","puntos clave","takeaway"]) else "captions"
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out,"w",encoding="utf-8") as f:
        f.write(f"<!-- fuente: {os.path.basename(a.file)} | tipo: {kind} | tiempos: {'si' if timed else 'sin-tiempos'} -->\n")
        for t,x in segs:
            f.write((f"[{ts(t)}] " if timed else "- ")+x+"\n")
    words=sum(len(x.split()) for _,x in segs)
    print(f"OK {len(segs)} segmentos, ~{words} palabras, tipo={kind}, tiempos={timed} -> {a.out}")

if __name__=="__main__": main()
