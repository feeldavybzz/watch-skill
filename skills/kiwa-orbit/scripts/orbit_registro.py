#!/usr/bin/env python3
"""Registro privado mínimo de ORBIT: qué chats se renombraron o movieron, para no repetir.

Uso:
  orbit_registro.py add  --id ID --antes "T viejo" --despues "T nuevo" [--proyecto P] [--estado verificado|pendiente|saltado] [--motivo ".."]
  orbit_registro.py seen --id ID        # imprime el último registro o "NUEVO"
  orbit_registro.py list [--estado X]
El archivo vive FUERA del repo (privado): $ORBIT_REGISTRO o ~/.mukiwa/orbit-registro.jsonl
Nunca guarda contenido de chats, solo ID, títulos, proyecto, motivo y estado.
"""
import argparse, json, os, sys, time
from pathlib import Path

def ruta():
    return Path(os.environ.get("ORBIT_REGISTRO") or Path.home() / ".mukiwa" / "orbit-registro.jsonl")

def leer(p):
    if not p.exists():
        return []
    out = []
    for l in p.read_text(encoding="utf-8").splitlines():
        if l.strip():
            try: out.append(json.loads(l))
            except ValueError: pass
    return out

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("--id", required=True); a.add_argument("--antes", default="")
    a.add_argument("--despues", default=""); a.add_argument("--proyecto", default=""); a.add_argument("--motivo", default="")
    a.add_argument("--estado", default="pendiente", choices=["verificado", "pendiente", "saltado"])
    s = sub.add_parser("seen"); s.add_argument("--id", required=True)
    l = sub.add_parser("list"); l.add_argument("--estado")
    n = ap.parse_args(argv)
    p = ruta()
    if n.cmd == "add":
        p.parent.mkdir(parents=True, exist_ok=True)
        r = {"id": n.id, "antes": n.antes, "despues": n.despues, "proyecto": n.proyecto,
             "motivo": n.motivo, "estado": n.estado, "fecha": time.strftime("%Y-%m-%d")}
        with p.open("a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("OK", n.id, n.estado)
    elif n.cmd == "seen":
        rs = [r for r in leer(p) if r.get("id") == n.id]
        print(json.dumps(rs[-1], ensure_ascii=False) if rs else "NUEVO")
    else:
        for r in leer(p):
            if not n.estado or r.get("estado") == n.estado:
                print(f'{r["fecha"]} {r["estado"]:<10} {r["id"]}  {r["antes"]} -> {r["despues"]}  [{r["proyecto"]}]')
    return 0

if __name__ == "__main__":
    sys.exit(main())
