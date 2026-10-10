#!/usr/bin/env python3
"""Guarda una lección en la biblioteca y actualiza el índice.
Uso: python save_lesson.py --topic motion-edicion --slug easing-curvas --file leccion.md
     (copia a library/<topic>/<slug>.md y regenera library/INDEX.md)
Topics sugeridos: motion-edicion, diseno-grafico (crear carpeta nueva si hace falta)."""
import argparse, os, re, shutil
from datetime import datetime
root=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","library")
ap=argparse.ArgumentParser(); ap.add_argument("--topic",required=True); ap.add_argument("--slug",required=True)
ap.add_argument("--file",required=True); a=ap.parse_args()
if not all(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", x) for x in (a.topic,a.slug)):
    ap.error("topic y slug deben usar letras minúsculas, números y guiones")
d=os.path.join(root,a.topic); os.makedirs(d,exist_ok=True)
dst=os.path.join(d,a.slug+".md")
if os.path.abspath(a.file)!=os.path.abspath(dst):
    if os.path.exists(dst):
        backup=os.path.join(root,"_history",a.topic)
        os.makedirs(backup,exist_ok=True)
        shutil.copy2(dst,os.path.join(backup,a.slug+"-"+datetime.now().strftime("%Y%m%d-%H%M%S-%f")+".md"))
    shutil.copy(a.file,dst)
lines=["# Biblioteca VYBZ — índice\n"]
for t in sorted(os.listdir(root)):
    p=os.path.join(root,t)
    if t.startswith("_") or not os.path.isdir(p): continue
    lines.append(f"\n## {t}\n")
    for f in sorted(os.listdir(p)):
        if not f.endswith(".md"): continue
        txt=open(os.path.join(p,f),encoding="utf-8").read()
        m=re.search(r"^# (.+)$",txt,re.M); title=m.group(1) if m else f
        m=re.search(r"^> (.+)$",txt,re.M); one=m.group(1) if m else ""
        lines.append(f"- [{title}]({t}/{f}) — {one}")
open(os.path.join(root,"INDEX.md"),"w",encoding="utf-8").write("\n".join(lines)+"\n")
print("OK guardada:",dst)
