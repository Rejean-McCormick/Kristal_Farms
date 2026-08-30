from __future__ import annotations
import json, re
from pathlib import Path

def load_targets(path):
    import csv
    with open(path,encoding='utf-8') as f: return list(csv.DictReader(f))

def normalized(s):
    if not s: return ''
    s=s.upper()
    s=re.sub(r'[^A-Z0-9]+',' ',s)
    return ' '.join(s.split())

def write_json(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
