#!/usr/bin/env python3
"""Guarda una lección en la biblioteca y actualiza el índice.
Uso: python save_lesson.py --topic motion-edicion --slug easing-curvas --file leccion.md
     (copia a library/<topic>/<slug>.md y regenera library/INDEX.md)
Topics sugeridos: motion-edicion, diseno-grafico (crear carpeta nueva si hace falta).
Discos exFAT (el disco externo de la Mac) crean archivos ocultos "._nombre" con metadatos
de macOS: se ignoran al armar el índice y se copia solo el texto para no generarlos."""
import argparse, os, re, shutil
from datetime import datetime
ap=argparse.ArgumentParser(); ap.add_argument("--topic",required=True); ap.add_argument("--slug",required=True)
ap.add_argument("--file",required=True)
ap.add_argument("--library",default=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","library"))
a=ap.parse_args(); root=a.library
if not all(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", x) for x in (a.topic,a.slug)):
    ap.error("topic y slug deben usar letras minúsculas, números y guiones")
d=os.path.join(root,a.topic); os.makedirs(d,exist_ok=True)
dst=os.path.join(d,a.slug+".md")
if os.path.abspath(a.file)!=os.path.abspath(dst):
    if os.path.exists(dst):
        backup=os.path.join(root,"_history",a.topic)
        os.makedirs(backup,exist_ok=True)
        shutil.copyfile(dst,os.path.join(backup,a.slug+"-"+datetime.now().strftime("%Y%m%d-%H%M%S-%f")+".md"))
    shutil.copyfile(a.file,dst)  # copyfile no arrastra atributos (shutil.copy sí, y en exFAT crea ._dst)
lines=["# Biblioteca VYBZ — índice\n"]
for t in sorted(os.listdir(root)):
    p=os.path.join(root,t)
    if t.startswith(("_",".")) or not os.path.isdir(p): continue
    lines.append(f"\n## {t}\n")
    for f in sorted(os.listdir(p)):
        if f.startswith(".") or not f.endswith(".md"): continue  # ._x.md = metadatos macOS, no lección
        txt=open(os.path.join(p,f),encoding="utf-8").read()
        m=re.search(r"^# (.+)$",txt,re.M); title=m.group(1) if m else f
        m=re.search(r"^> (.+)$",txt,re.M); one=m.group(1) if m else ""
        lines.append(f"- [{title}]({t}/{f}) — {one}")
open(os.path.join(root,"INDEX.md"),"w",encoding="utf-8").write("\n".join(lines)+"\n")
print("OK guardada:",dst)
