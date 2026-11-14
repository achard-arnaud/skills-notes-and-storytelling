"""Resolve a single analytical note and bind its output to an editorial block."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT.parents[1]


def read(path):
    return json.loads(path.read_text())


def select(route, template, method, block):
    profiles = read(SKILL / 'verticales/registry.json')['routes']
    profile = profiles[route]
    if template not in profile['fixtures']:
        raise ValueError('Unknown route/format combination')
    manifest = read(SKILL / 'verticales' / profile['manifest'])
    formats = manifest.get('formats', manifest.get('templates', {}))
    item = formats.get(template, {})
    blocks = item.get('block_ids') or item.get('required_blocks') or [
        b['block'] for b in item.get('scaffold', [])
    ] or [b[0] for b in manifest.get('blocks', [])]
    if block not in blocks:
        raise ValueError('Unresolved target block')
    entries = read(ROOT / 'catalog.json')['methods']
    asset = entries[method]
    if template not in asset['templates']:
        raise ValueError('Undeclared method/format binding')
    note = ROOT / asset['file']
    if not note.is_file():
        raise FileNotFoundError(note)
    return dict(method=method, note=asset['file'], route=route, template=template,
                affects_blocks=[block], output_contract='contracts/analysis-result.schema.json')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    for field in ('route', 'template', 'method', 'block'):
        parser.add_argument('--'+field, required=True)
    print(json.dumps(select(**vars(parser.parse_args())), ensure_ascii=False, indent=2))
