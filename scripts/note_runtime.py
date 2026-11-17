#!/usr/bin/env python3
"""Run from any working directory. JSON stdout; nonzero status for failed QA."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.runtime import plan,packet,validate,search_plan,selected_profile
p=argparse.ArgumentParser(); p.add_argument('command',choices=['plan','packet','validate','search-plan','profile'])
p.add_argument('input'); p.add_argument('--targets',nargs='*',default=[])
p.add_argument('--query',default=''); p.add_argument('--budget',type=int)
a=p.parse_args()
try:
 data={} if a.command=='profile' else json.loads(Path(a.input).read_text())
 if a.command=='profile': result=selected_profile(a.input)
 elif a.command=='plan': result=plan(data)
 elif a.command=='packet': result=packet(data,a.targets,a.query,a.budget)
 elif a.command=='search-plan': result=search_plan(data)
 else:
  errors=validate(data); result={'pass':not errors,'errors':errors}
 print(json.dumps(result,ensure_ascii=False,indent=2))
 if a.command=='validate' and not result['pass']: sys.exit(1)
except (ValueError,KeyError,TypeError) as e:
 print(json.dumps({'error':str(e)}));sys.exit(1)
