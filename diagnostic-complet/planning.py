"""Versioned analysis planning and question packets; no research or generation."""
from __future__ import annotations

import copy
import json
from pathlib import Path

from analysis import _shape, _study_claims, _verdict, validate_analysis_envelope
from writing import EVIDENCE_KEYS, study_hash

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT / 'schemas/analysis-planning.v1.schema.json').read_text(encoding='utf-8'))
CATALOG = json.loads((ROOT / 'workflows/analysis-methods.v1.json').read_text(encoding='utf-8'))


def validate_analysis_plan(plan, brief, study):
    """Validate structure, identity, revision and declared evidence requirements.

    Completeness of the evidence_map is only referential. Whether a claim actually
    establishes a denominator, cohort or date requires analyst/human review.
    Budgets are declared ceilings, not a live consumption ledger or a scheduler.
    """
    errors = _shape(plan, SCHEMA, root=SCHEMA)
    errors += _shape(brief, SCHEMA['$defs']['intentBrief'], '$brief', root=SCHEMA)
    claim_ids, study_errors = _study_claims(study)
    errors += study_errors
    if errors:
        return _verdict(errors, [], [])
    refs, gaps = [], []
    if plan['study_ref'] != study['id'] or brief['study_ref'] != study['id']:
        refs.append('study_ref: plan and brief must belong to current study')
    if plan['intent_ref'] != brief['id']:
        refs.append('intent_ref: unresolved brief')
    try:
        current = study_hash({k: study[k] for k in EVIDENCE_KEYS if k in study})
    except (TypeError, ValueError):
        return _verdict(['study: evidence projection must be JSON serializable'], refs, [])
    for key, expected in [('input_revision', current), ('intent_revision', study_hash(brief)),
                          ('catalog_revision', study_hash(CATALOG))]:
        if plan[key] != expected:
            refs.append(f'{key}: stale or foreign revision')
    seen = {study['id'], brief['id'], plan['id']} | claim_ids
    if len({study['id'], brief['id'], plan['id']}) != 3 or {brief['id'], plan['id']} & claim_ids:
        refs.append('plan/brief: duplicate identity or collision with claims')
    for q in plan['questions']:
        ident = q['id']
        if ident in seen:
            refs.append(f'question {ident}: duplicate identity or collision')
        seen.add(ident)
        inputs = set(q['input_claim_refs'])
        for ref in sorted(inputs - claim_ids):
            refs.append(f'question {ident}: unresolved input claim {ref}')
        method = CATALOG['methods'].get(q['method'])
        if method is None:
            refs.append(f'question {ident}: unknown method {q["method"]}')
            continue
        if q['method_version'] != method['method_version']:
            refs.append(f'question {ident}: unknown method version')
        if brief['intent'] not in method['intents']:
            refs.append(f'question {ident}: method not declared for this intent')
        requirements = set(method['required_evidence'])
        mapped = set()
        for mapping in q['evidence_map']:
            requirement = mapping['requirement']
            if requirement not in requirements or requirement in mapped:
                refs.append(f'question {ident}: unknown or duplicate evidence requirement {requirement}')
            mapped.add(requirement)
            for ref in mapping['claim_refs']:
                if ref not in inputs:
                    refs.append(f'question {ident}: evidence claim outside declared inputs {ref}')
        missing = sorted(requirements - mapped)
        if missing or q['unknowns']:
            gaps.append({'question_ref': ident, 'missing_requirements': missing,
                         'unknowns': list(q['unknowns']), 'needs_research': True})
    return _verdict([], refs, gaps)


def resolve_question(plan, brief, study, question_ref):
    """Return a self-contained candidate method packet, never a block or result."""
    verdict = validate_analysis_plan(plan, brief, study)
    if not verdict['valid']:
        raise ValueError('; '.join(verdict['errors']))
    question = next((q for q in plan['questions'] if q['id'] == question_ref), None)
    if question is None:
        raise ValueError(f'unresolved question: {question_ref}')
    gaps = [g for g in verdict['gaps'] if g['question_ref'] == question_ref]
    claims = {c['id']: c for c in study['claims']}
    return {'schema_version': '1.0', 'study_ref': study['id'], 'plan_ref': plan['id'],
            'input_revision': plan['input_revision'], 'intent_revision': plan['intent_revision'],
            'catalog_revision': plan['catalog_revision'], 'intent': copy.deepcopy(brief),
            'question': copy.deepcopy(question),
            'method': copy.deepcopy(CATALOG['methods'][question['method']]),
            'claims': [copy.deepcopy(claims[ref]) for ref in question['input_claim_refs']],
            'budget': copy.deepcopy(plan['budget']), 'gaps': gaps,
            'state': 'needs_research' if gaps else 'ready_for_analysis',
            'analysis_executed': False, 'human_approval': False}


def validate_planned_analysis(envelope, plan, brief, study):
    """Check externally authored analysis against its frozen question plan.

    Does not write findings, execute a method, judge truth, or promote a claim.
    A valid result may remain partial, and missing results stay visible as gaps.
    """
    plan_check = validate_analysis_plan(plan, brief, study)
    result_check = validate_analysis_envelope(envelope, study)
    if not plan_check['valid'] or not result_check['valid']:
        return _verdict(plan_check['structural_errors'] + result_check['structural_errors'],
                        plan_check['reference_errors'] + result_check['reference_errors'],
                        plan_check['gaps'] + result_check['gaps'])
    refs, gaps = [], copy.deepcopy(plan_check['gaps'] + result_check['gaps'])
    questions = {q['id']: q for q in plan['questions']}
    unresolved = {g['question_ref'] for g in plan_check['gaps']}
    covered = set()
    for row in envelope['analyses']:
        q = questions.get(row['question_ref'])
        if q is None:
            refs.append(f'analysis {row["id"]}: unresolved planned question')
            continue
        if row['question_ref'] in covered:
            refs.append(f'question {q["id"]}: duplicate analysis result')
        covered.add(q['id'])
        for key in ('question', 'method', 'method_version'):
            if row[key] != q[key]:
                refs.append(f'analysis {row["id"]}: {key} differs from plan')
        if row['scope'] != brief['scope']:
            refs.append(f'analysis {row["id"]}: scope differs from brief')
        if set(row['input_claim_refs']) != set(q['input_claim_refs']):
            refs.append(f'analysis {row["id"]}: input claims differ from plan')
        if q['id'] in unresolved and row['state'] == 'complete':
            refs.append(f'analysis {row["id"]}: complete result hides declared research gaps')
        if not brief['decision_requested'] and any(f['status'] == 'recommendation' for f in row['findings']):
            refs.append(f'analysis {row["id"]}: recommendation requires an explicit decision mandate')
    for ident in sorted(set(questions) - covered):
        gaps.append({'question_ref': ident, 'missing_analysis': True})
    return _verdict([], refs, gaps)
