#!/usr/bin/env python3
"""Build or review a narrative packet from supplied evidence. No model calls or case writes."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'workflow/narrative-profile.json'
REVIEW_FIELDS = ('kind', 'observation', 'ref', 'action', 'exit_test')
MATERIAL = {'fact', 'attributed_claim', 'inference'}
STATUSES = MATERIAL | {'hypothesis', 'recommendation', 'unknown'}


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def load_profile(root=ROOT):
    return load(root / PROFILE)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shape(row, required, optional=()):
    require(isinstance(row, dict) and set(required) <= row.keys()
            and row.keys() <= set(required) | set(optional), 'Unexpected or missing packet fields')


def filled(value):
    return isinstance(value, str) and bool(value.strip())


def texts(values, allowed=None):
    return (isinstance(values, list)
            and all(filled(v) and (allowed is None or v in allowed) for v in values)
            and len(set(values)) == len(values))


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode('utf-8')).hexdigest()


def claim_ids(request):
    """The selected ledger consists only of referenced/classified claims."""
    shape(request, ('domain',), ('decision_kind', 'conclusion', 'tension', 'objection', 'falsifier',
                                  'sections', 'classification', 'required_pillars', 'coverage', 'side_stories', 'transitions'))
    sections = request.get('sections', [])
    classification = request.get('classification', {})
    require(isinstance(sections, list) and isinstance(classification, dict), 'Invalid sections or classification')
    ids = set(classification)
    for section in sections:
        shape(section, ('id', 'action_title', 'claim_ids'))
        require(texts(section['claim_ids']) and section['claim_ids'], 'Expected unique section claim IDs')
        ids.update(section['claim_ids'])
    return ids


def classify(rows, profile):
    pillars = profile['pillars']
    for row in rows.values():
        shape(row, ('primary_pillar',), ('secondary_pillars', 'unclassified_reason', *profile['axes']))
        main = row['primary_pillar']
        related = row.get('secondary_pillars', [])
        require(texts(related, pillars), 'Invalid secondary pillars')
        if main is None:
            require(filled(row.get('unclassified_reason')) and not related, 'Explain the unclassified claim')
        else:
            require(main in pillars and main not in related and 'unclassified_reason' not in row,
                    'Invalid primary pillar')
        for axis, options in profile['axes'].items():
            require(axis not in row or row[axis] in options, 'Invalid analytic axis: ' + axis)
    return rows


def side_stories(rows, sections, profile):
    require(isinstance(rows, list), 'Side stories must be a list')
    result = []
    for row in rows:
        shape(row, ('type', 'section_id', 'anchor_claim_id', 'claim_ids', 'objection', 'limitation', 'return_hook'))
        require(row['type'] in profile['side_story_types'], 'Unknown side-story type')
        require(filled(row['section_id']) and filled(row['anchor_claim_id']), 'Expected side-story anchors')
        covered = sections.get(row['section_id'], set())
        require(texts(row['claim_ids'], covered) and row['anchor_claim_id'] in row['claim_ids'],
                'Side story must use claims already in its trunk section')
        require(all(filled(row[k]) for k in ('objection', 'limitation', 'return_hook')),
                'Side story requires objection, limitation and return hook')
        result.append({**row, 'status': 'candidate', 'render_eligible': False})
    return result


def build(request, claims, profile, universe=None, relations=()):
    selected = claim_ids(request)
    domain = request['domain']
    require(domain in profile['domains'], 'Unknown domain')
    kind = request.get('decision_kind')
    scheme = profile['by_decision'].get(kind) if isinstance(kind, str) else None
    needs = [] if scheme else ['decision_kind']
    needs.extend(k for k in ('conclusion', 'tension', 'objection', 'falsifier') if not filled(request.get(k)))
    needs.extend(k for k in ('sections', 'coverage') if not request.get(k))
    if needs:
        return {'profile': profile['id'], 'status': 'needs_input', 'missing': needs, 'editorial_approved': False}
    require(selected <= claims.keys(), 'Unknown claim in narrative packet')
    all_ids = set(claims if universe is None else universe)
    require(selected <= all_ids, 'Narrative claims exceed source scope')
    coverage = request['coverage']
    shape(coverage, ('loaded', 'omitted', 'stop_reason'))
    require(texts(coverage['loaded']) and texts(coverage['omitted']) and filled(coverage['stop_reason']),
            'Declare passages loaded, omissions and stop reason')
    ledger = {cid: claims[cid] for cid in sorted(selected)}
    for claim in ledger.values():
        shape(claim, ('statement', 'status', 'evidence'))
        require(filled(claim['statement']) and claim['status'] in STATUSES and isinstance(claim['evidence'], list),
                'Invalid claim statement/evidence status')
        require(claim['evidence'] or claim['status'] not in MATERIAL, 'Material claim requires evidence')
        for source in claim['evidence']:
            shape(source, ('source_id', 'locator'), ('attribution', 'url', 'fetched_at', 'fragment_id', 'evidence_status'))
            require(all(filled(value) for value in source.values()), 'Evidence requires a source ID and locator')
    classification = classify(request.get('classification', {}), profile)
    required = request.get('required_pillars', [])
    require(texts(required, profile['pillars']), 'Invalid required pillars')
    examined = {c for x in classification.values()
                for c in (x['primary_pillar'], *x.get('secondary_pillars', [])) if c}
    sections = {}
    for section in request['sections']:
        sid = section['id']
        require(filled(sid) and sid not in sections and filled(section['action_title']),
                'Duplicate section or missing action title')
        sections[sid] = set(section['claim_ids'])
    transitions = request.get('transitions', {})
    require(isinstance(transitions, dict) and transitions.keys() <= sections.keys()
            and all(filled(v) for v in transitions.values()), 'Transitions must target known sections')
    relevant = []
    for rel in relations:
        shape(rel, ('from', 'to', 'type'))
        left, right = rel['from'], rel['to']
        require(filled(left) and filled(right) and left != right
                and rel['type'] in {'contradicts', 'depends_on', 'supports'}, 'Invalid claim relation')
        if selected.intersection((left, right)):
            relevant.append({**rel, 'outside_packet': sorted({left, right} - selected)})
    packet = {
        'profile': profile['id'], 'status': 'candidate', 'schema_id': scheme, 'domain': domain,
        'rationale': profile['rationales'][scheme], 'conclusion': request['conclusion'],
        'tension': request['tension'], 'objection': request['objection'], 'falsifier': request['falsifier'],
        'sections': request['sections'], 'transitions': transitions, 'claims': ledger, 'relations': relevant, 'classification': classification, 'coverage': coverage,
        'pillar_coverage': {'missing': sorted(set(required) - examined),
                            'unclassified': sorted(k for k, v in classification.items() if v['primary_pillar'] is None),
                            'unexamined': sorted(all_ids - classification.keys())},
        'side_stories': side_stories(request.get('side_stories', []), sections, profile),
        'editorial_approved': False,
    }
    return {**packet, 'packet_sha256': fingerprint(packet)}


def check_packet(packet, profile):
    body = {k: v for k, v in packet.items() if k != 'packet_sha256'}
    require(packet.get('status') == 'candidate' and packet.get('editorial_approved') is False
            and packet.get('profile') == profile['id'] and fingerprint(body) == packet.get('packet_sha256'),
            'Missing or changed candidate packet')


def section_packet(packet, section_id):
    section = next((s for s in packet['sections'] if s['id'] == section_id), None)
    require(section is not None, 'Unknown section')
    return {'schema_id': packet['schema_id'], 'section': section, 'conclusion': packet['conclusion'],
            'claims': {cid: packet['claims'][cid] for cid in section['claim_ids']},
            'transition': packet['transitions'].get(section_id),
            'relations': [{**rel, 'outside_section': sorted({rel['from'], rel['to']} - set(section['claim_ids']))}
                          for rel in packet['relations'] if {rel['from'], rel['to']}.intersection(section['claim_ids'])],
            'side_stories': [s for s in packet['side_stories'] if s['section_id'] == section_id],
            'packet_sha256': packet['packet_sha256']}


def review(packet, findings, mode, profile):
    check_packet(packet, profile)
    require(mode in {'direct', 'workflow'} and isinstance(findings, list), 'Invalid review mode or findings')
    allowed = set(packet['claims']) | {s['id'] for s in packet['sections']} | {'mandate', 'coverage', 'render'}
    output = []
    for row in findings:
        shape(row, REVIEW_FIELDS)
        require(all(filled(row[key]) for key in REVIEW_FIELDS) and row['ref'] in allowed
                and row['kind'] in profile['findings'], 'Unknown review target or incomplete finding')
        owner = profile['findings'][row['kind']]
        if mode == 'direct':
            owner = 'targeted_research' if owner == 'A0' else profile['domains'][packet['domain']]
        output.append({**row, 'owner': owner})
    return {'status': 'changes_requested' if output else 'no_declared_findings',
            'packet_sha256': packet['packet_sha256'], 'findings': output, 'editorial_approved': False}


def graph_ledger(graph, evidence, selected):
    """Read only direct support and locators for selected claims; keep A1 truth labels."""
    sources = {s['id']: s for s in evidence['sources']}
    nodes = {n['id']: n for n in graph['nodes']}
    claims = {cid for cid, row in nodes.items() if row['type'] == 'claim'}
    support = {}
    extraction = {}
    for edge in graph['edges']:
        f, t = edge['from'], edge['to']
        if edge['type'] == 'supports' and t in selected and nodes[f]['type'] == 'fragment':
            support.setdefault(t, []).append(f)
        elif edge['type'] == 'extracted_from':
            extraction.setdefault(f, []).append(t)
    ledger = {}
    for cid in sorted(selected & claims):
        refs = []
        for fid in support.get(cid, []):
            fragment = nodes[fid]
            for sid in extraction.get(fid, []):
                src = sources[nodes[sid]['source_id']]
                refs.append({'source_id': src['id'], 'locator': fragment['locator'], 'url': src['url'],
                             'fetched_at': src['fetched_at'], 'fragment_id': fid,
                             'evidence_status': fragment['evidence_status']})
        ledger[cid] = {'statement': nodes[cid]['statement'], 'status': nodes[cid]['status'], 'evidence': refs}
    relations = [edge for edge in graph['edges']
                 if edge['from'] in claims and edge['to'] in claims]
    return ledger, claims, relations


def scaffold(packet):
    require(packet['status'] == 'candidate', 'Narrative input incomplete; inspect missing fields')
    return {'decision': packet['conclusion'], 'strongest_objection': packet['objection'],
            'falsifier': packet['falsifier'], 'sections': packet['sections']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['select', 'section', 'review'])
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--section')
    parser.add_argument('--findings', type=Path)
    args = parser.parse_args(argv)
    try:
        profile = load_profile()
        data = load(args.input)
        if args.command == 'select':
            shape(data, ('request', 'claims'), ('relations',))
            result = build(data['request'], data['claims'], profile, relations=data.get('relations', []))
        elif args.command == 'section':
            check_packet(data, profile)
            result = section_packet(data, args.section)
        else:
            result = review(data, load(args.findings), 'direct', profile)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result.get('status') != 'needs_input' else 2
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'status': 'blocked', 'error': str(error)}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
