#!/usr/bin/env python3
"""Measure explicitly loaded files/slices, not the full repository. Words != tokens."""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('--budget',type=int,default=6000)
a=p.parse_args();root=Path(__file__).resolve().parents[1]
rows=json.loads(Path(a.manifest).read_text())['reads'];counts={};seen=set()
for row in rows:
 path=(root/row['path']).resolve()
 if not path.is_relative_to(root):raise SystemExit('read path escapes skill')
 text=path.read_text();start=row.get('line_start',1);end=row.get('line_end',len(text.splitlines()))
 if start<1 or end<start or end>len(text.splitlines()):raise SystemExit('invalid read slice')
 key=f"{row['path']}:{start}-{end}"
 if key in seen:continue
 seen.add(key);counts[key]=len('\n'.join(text.splitlines()[start-1:end]).split())
words=sum(counts.values())
print(json.dumps({'measurement':'words_not_tokens','files':counts,'words':words,'budget':a.budget,'pass':words<=a.budget},indent=2))
sys.exit(0 if words<=a.budget else 1)
