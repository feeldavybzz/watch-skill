#!/usr/bin/env python3
"""Inventario de skills y notas privadas explícitas. Solo biblioteca estándar."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import uuid


def inventory(root):
    rows = []
    for f in sorted(root.rglob('SKILL.md')):
        if any(p in {'.git', 'node_modules', 'uninstalled', '.venv'} for p in f.relative_to(root).parts):
            continue
        text = f.read_text(encoding='utf-8')
        name = None
        if text.startswith('---\n'):
            for line in text.split('---', 2)[1].splitlines():
                if line.startswith('name:'):
                    name = line.split(':', 1)[1].strip().strip('\"\'')
        rows.append({'name': name, 'path': str(f), 'sha256': hashlib.sha256(f.read_bytes()).hexdigest()})
    return rows


def private_store(path):
    path = path.expanduser().resolve()
    # Refuse storage inside any checkout unless an operator deliberately chooses
    # a different private destination. Avoid publishing notes via later git add.
    for parent in (path, *path.parents):
        if (parent / '.git').exists():
            raise ValueError('El almacén de memoria debe quedar fuera de cualquier repositorio.')
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='command', required=True)
    inv = sub.add_parser('inventory'); inv.add_argument('--root', type=Path, required=True)
    note = sub.add_parser('note'); note.add_argument('--store', type=Path, required=True)
    note.add_argument('--kind', choices=['decision', 'observation', 'handoff'], required=True)
    note.add_argument('--text', required=True); note.add_argument('--source', required=True)
    notes = sub.add_parser('notes'); notes.add_argument('--store', type=Path, required=True)
    a = ap.parse_args()
    if a.command == 'inventory':
        if not a.root.is_dir(): ap.error('La raíz no existe o no es una carpeta.')
        rows = inventory(a.root.resolve())
        print(json.dumps({'skills': rows, 'count': len(rows)}, ensure_ascii=False, indent=2))
        return
    try: store = private_store(a.store)
    except ValueError as e: ap.error(str(e))
    if a.command == 'notes':
        if not store.is_dir(): ap.error('El almacén no existe; no significa que no haya memoria en otro destino.')
        print(json.dumps([json.loads(p.read_text()) for p in sorted(store.glob('*.json'))], ensure_ascii=False, indent=2))
        return
    if not a.text.strip() or not a.source.strip(): ap.error('Texto y fuente son obligatorios.')
    store.mkdir(parents=True, mode=0o700, exist_ok=True)
    ident = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex
    payload = {'id': ident, 'created': dt.datetime.now(dt.timezone.utc).isoformat(), 'kind': a.kind,
               'text': a.text, 'source': a.source, 'status': 'open' if a.kind == 'observation' else 'recorded'}
    destination = store / (ident + '.json')
    fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    if json.loads(destination.read_text()) != payload: raise RuntimeError('Falló la verificación de relectura')
    print(json.dumps({'saved': str(destination), 'id': ident}, ensure_ascii=False))


if __name__ == '__main__':
    main()
