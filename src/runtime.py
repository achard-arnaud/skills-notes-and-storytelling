"""Deterministic routing and evidence packets; no model/network calls."""
from __future__ import annotations
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT/'config/retrieval.json').read_text())
WEIGHTS = CONFIG['claim_weights']
RELATIONS = {'supports','contradicts','qualifies','causes','depends_on','compares_to','answers','motivates'}

def plan(intake):
    env = intake.get('environment', intake.get('execution_mode','work'))
    if env == 'cowork': env = 'work'
    if env not in {'chat','work'}: raise ValueError('environment must be chat|work|cowork')
    generation = intake.get('generation', 'from-scratch')
    if generation not in {'from-scratch','iterative','feedback-dreaming'}:
        raise ValueError('unsupported generation; retro-engineering remains TODO')
    if generation == 'iterative' and not intake.get('baseline_id'):
        raise ValueError('iterative requires baseline_id')
    legacy = intake.get('runtime_mode')
    mapped = {'run_lourd':'heavy','run_léger':'light','run_leger':'light','debug':'heavy'}
    if legacy is not None and legacy not in mapped: raise ValueError('unknown runtime_mode')
    requested = intake.get('execution', mapped.get(legacy, 'light' if env == 'chat' else 'heavy'))
    if requested not in {'light','heavy'}: raise ValueError('execution must be light|heavy')
    if not isinstance(intake.get('debug',False),bool): raise ValueError('debug must be boolean')
    documents = bool(intake.get('documents'))
    heavy = documents or requested == 'heavy'
    high = bool(intake.get('contradictions') or len(intake.get('entities', [])) > 1
                or intake.get('complex_comparison'))
    return dict(environment=env, execution='heavy' if heavy else 'light',
                debug=bool(intake.get('debug', False) or legacy=='debug'), generation=generation,
                baseline_id=intake.get('baseline_id'),
                reason='documents_force_heavy' if documents else 'environment_or_request',
                reasoning_recommendation='high' if high else 'medium' if heavy else 'low',
                reasoning_applied=False,
                stage_efforts=json.loads((ROOT/'config/reasoning-effort.json').read_text())['stages'], packet_words=2000 if env == 'chat' else 6000,
                initial_gap_queries=3 if env == 'chat' else 6)

def indexed(rows):
    out = {}
    for row in rows:
        if not row.get('id') or row['id'] in out: raise ValueError('missing/duplicate ID')
        out[row['id']] = row
    return out

def validate(run):
    """Validate actual records, cross-references and semantic evidence boundaries."""
    from jsonschema import Draft202012Validator
    root = Path(__file__).resolve().parents[1]
    schema = json.loads((root/'contracts/run-bundle.schema.json').read_text())
    errors = [f'{list(e.path)}: {e.message}' for e in Draft202012Validator(schema).iter_errors(run)]
    if errors: return errors
    try:
        sources, fragments, claims, sections = [indexed(run[k]) for k in ('sources','fragments','claims','sections')]
        stories = indexed(run['side_stories'])
        all_ids = [*sources,*fragments,*claims,*sections,*stories]
        if len(all_ids) != len(set(all_ids)): errors.append('IDs must be globally unique')
    except ValueError as exc: return [str(exc)]
    for source in sources.values():
        if source['coverage_status'] not in {'read','scoped','unread'}: errors.append('invalid source coverage status')
        if source['coverage_status']=='scoped' and not source.get('coverage'): errors.append('scoped coverage requires read/excluded/unread regions')
    for f in fragments.values():
        if f['source_id'] not in sources: errors.append(f"{f['id']}: unresolved source")
        if not f.get('source_locator'): errors.append(f"{f['id']}: missing source locator")
    for c in claims.values():
        refs = c['fragment_ids']
        if any(f not in fragments for f in refs): errors.append(f"{c['id']}: unresolved fragment")
        if c['claim_type'] == 'fact':
            if not refs: errors.append(f"{c['id']}: fact without evidence")
            if any(fragments.get(f, {}).get('evidence_status') != 'verified' for f in refs):
                errors.append(f"{c['id']}: fact requires verified evidence; use attributed claim")
        for key in WEIGHTS:
            value = c.get(key,0)
            if isinstance(value,bool) or not isinstance(value,(float,int)) or not 0 <= value <= 5:
                errors.append(f"{c['id']}: invalid {key}")
    for edge in run['edges']:
        if edge['from'] not in claims or edge['to'] not in claims: errors.append('unresolved graph endpoint')
        if edge['type'] not in RELATIONS: errors.append('unknown relation')
        if edge['type'] == 'causes' and not edge.get('mechanism'): errors.append('causes needs mechanism')
    for s in sections.values():
        if any(c not in claims for c in s['claim_ids']): errors.append(f"{s['id']}: unresolved claim")
    for s in stories.values():
        if not s['claim_ids'] or any(c not in claims for c in s['claim_ids']): errors.append(f"{s['id']}: missing lineage")
        if s['section_anchor'] not in sections: errors.append(f"{s['id']}: unresolved insertion")
        if s['return_to'] not in sections and not (s['kind']=='method' and s['return_to'] is None):
            errors.append(f"{s['id']}: unresolved return")
    try: resolved = plan(run['intake'])
    except ValueError as exc: return errors+[str(exc)]
    if run['profile'] != resolved: errors.append('profile does not match resolved intake')
    if resolved['generation']=='iterative' and not run.get('targets'): errors.append('iterative requires targets')
    return errors

def closure(run, targets):
    claims, fragments, sections = [indexed(run[k]) for k in ('claims','fragments','sections')]
    known = set(claims)|set(fragments)|set(sections)
    if set(targets)-known: raise ValueError('unresolved targets: '+','.join(sorted(set(targets)-known)))
    selected = set(targets)&set(claims)
    for fid in set(targets)&set(fragments):
        selected.update(c['id'] for c in claims.values() if fid in c['fragment_ids'])
    for sid in set(targets)&set(sections): selected.update(sections[sid]['claim_ids'])
    changed = True
    while changed:
        before = set(selected)
        for e in run['edges']:
            a,b,t = e['from'],e['to'],e['type']
            if t in {'depends_on','supports','causes','contradicts','qualifies'} and ({a,b}&selected):
                selected.update((a,b))
        changed = before != selected
    return selected

def packet(run, targets=(), query='', budget=None):
    errors = validate(run)
    if errors: raise ValueError('; '.join(errors))
    candidates = set(targets)
    if query:
        terms = set(re.findall(r'\w+',query.casefold()))
        for family in ('claims','fragments'):
            for row in run[family]:
                text = row.get('statement',row.get('content',''))
                if terms & set(re.findall(r'\w+',text.casefold())): candidates.add(row['id'])
    selected = closure(run,candidates) if candidates else {c['id'] for c in run['claims']}
    rows = [copy.deepcopy(c) for c in run['claims'] if c['id'] in selected]
    for c in rows:
        c['score'] = round(sum(c.get(k,0)*w for k,w in WEIGHTS.items()),4)
        c['eligible_as_fact'] = c['claim_type']=='fact' and c.get('hard_gate') not in {'fail','open'}
    rows.sort(key=lambda c:(c.get('hard_gate') in {'fail','open'},-c['score'],c['id']))
    fids = {f for c in rows for f in c['fragment_ids']}
    fragments = [copy.deepcopy(f) for f in run['fragments'] if f['id'] in fids]
    for f in fragments:
        f['evidence_rank_score']=round(sum(f.get(k,0)*w for k,w in CONFIG['fragment_weights'].items()),4)
    fragments.sort(key=lambda f:(-f['evidence_rank_score'],f['id']))
    source_ids = {f['source_id'] for f in fragments}
    sections = [s for s in run['sections'] if set(s['claim_ids'])&selected]
    result = dict(claims=rows, fragments=fragments,
                  sources=[s for s in run['sources'] if s['id'] in source_ids],
                  sections=sections, edges=[e for e in run['edges'] if {e['from'],e['to']}<=selected],
                  side_stories=[s for s in run['side_stories'] if set(s['claim_ids'])&selected],
                  preserved_claim_ids=sorted({c['id'] for c in run['claims']}-selected))
    words = len(json.dumps(result,ensure_ascii=False).split())
    limit = budget if budget is not None else run['profile']['packet_words']
    if limit <= 0: raise ValueError('budget must be positive')
    result['display_fragments_by_claim']={c['id']:[f['id'] for f in fragments if f['id'] in c['fragment_ids']][:CONFIG['display_top_k']] for c in rows}
    displayed={f for ids in result['display_fragments_by_claim'].values() for f in ids}
    result['retained_non_display_fragment_ids']=[f['id'] for f in fragments if f['id'] not in displayed]
    result['budget'] = dict(words=words,limit=limit,overflow=words>limit,
                            action='split_required_do_not_drop_evidence' if words>limit else 'ready')
    return result

def search_plan(run):
    """No network: emit only unresolved, justified and deduplicated gap requests."""
    if any(s.get('origin')=='manual' and s.get('coverage_status') not in {'read','scoped'} for s in run['sources']):
        return {'blocked':'manual_intake_not_reviewed','queries':[]}
    seen=set(); rows=[]
    for gap in run.get('gaps',[]):
        if gap.get('status')!='open': continue
        if gap.get('reason') not in {'missing','contradiction','freshness','independence'}:
            raise ValueError('gap requires actionable reason')
        key=' '.join(gap['query'].casefold().split())
        if key in seen: continue
        seen.add(key); rows.append(gap)
    limit=run['profile']['initial_gap_queries']
    return {'queries':rows[:limit],'deferred_gap_ids':[g['id'] for g in rows[limit:]]}

def revise(run, patches, targets, baseline_id, reason):
    """Return a new immutable baseline; reject edits outside declared impact closure."""
    import hashlib
    if not baseline_id or not reason: raise ValueError('baseline_id and reason required')
    if run.get('run_id') != baseline_id: raise ValueError('baseline_id does not match canonical run_id')
    affected=closure(run,targets)
    allowed=set(targets)|affected
    allowed.update(f for c in run['claims'] if c['id'] in affected for f in c['fragment_ids'])
    allowed.update(s['id'] for s in run['sections'] if set(s['claim_ids'])&affected)
    allowed.update(s['id'] for s in run['side_stories'] if set(s['claim_ids'])&affected)
    result=copy.deepcopy(run); changed=[]
    for patch in patches:
        family=patch['family']; row=patch['record']; rid=row['id']
        if family not in {'claims','fragments','sections','side_stories'} or rid not in allowed:
            raise ValueError('patch outside declared impact scope')
        existing=next((i for i,x in enumerate(result[family]) if x['id']==rid),None)
        if existing is None: raise ValueError('revision requires existing stable ID')
        result[family][existing]=copy.deepcopy(row);changed.append(rid)
    result['intake'].update(generation='iterative',baseline_id=baseline_id)
    result['profile']=plan(result['intake']);result['targets']=list(targets)
    digest=hashlib.sha256(json.dumps(result,sort_keys=True).encode()).hexdigest()[:12]
    result['run_id']='run-'+digest
    result.setdefault('revisions',[]).append({'parent':baseline_id,'id':result['run_id'],'reason':reason,'changed_ids':changed})
    errors=validate(result)
    if errors: raise ValueError('; '.join(errors))
    return result

def selected_profile(template_type):
    root=Path(__file__).resolve().parents[1]
    profiles=json.loads((root/'templates/profiles.json').read_text())['profiles']
    if template_type not in profiles: raise ValueError('unknown template')
    return profiles[template_type]
