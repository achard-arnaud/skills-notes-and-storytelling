"""Replay synthetic contract checks. Run from any directory."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parent
manifest=json.loads((root/'manifest.json').read_text())
results=[]
for name,spec in manifest['templates'].items():
    fixture=json.loads((root/spec['fixture']).read_text())
    for version in ['v1','v2']:
        doc=(root/f'evals/{name}-{version}.md').read_text()
        headings=re.findall(r'^## (.+)$',doc,re.M)
        missing=sorted(set(fixture['expected_blocks'])-set(headings))
        invalid_refs=sorted(set(re.findall(r'\[(C\d+)\]',doc))-set(fixture['claims']))
        expected=[fixture['negative_oracle']] if version=='v1' else []
        results.append(dict(template=name,version=version,missing=missing,invalid_refs=invalid_refs,expected_observed=(missing==expected and not invalid_refs)))
print(json.dumps(results,ensure_ascii=False,indent=2))
sys.exit(int(any(not item['expected_observed'] for item in results)))
