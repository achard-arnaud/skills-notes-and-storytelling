"""Replay the local fixture oracles and preserve both outcomes."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
manifest=json.loads((root/'manifest.json').read_text())
results=[]
for template,spec in manifest['templates'].items():
    f=json.loads((root/spec['fixture']).read_text())
    for version in ['v1','v2']:
        body=(root/template/f'{version}.md').read_text()
        errors=[]
        for token in f['oracle']['required']:
            if token not in body: errors.append('missing literal '+token)
        for b in spec['scaffold']:
            for ref in b['claim_refs']:
                if ref not in f['claims'] or f'[{ref}]' not in body: errors.append('claim '+ref)
        if f['oracle']['pages'] and body.count('## Page ')!=f['oracle']['pages']: errors.append('logical pages')
        results.append(dict(template=template,version=version,status='FAIL' if errors else 'PASS',errors=errors))
print(json.dumps(results,ensure_ascii=False,indent=2))
assert all(x['status']==('FAIL' if x['version']=='v1' else 'PASS') for x in results)
