"""Apply the pinned adoption method to explicit, analyst-declared measurements."""
from __future__ import annotations

import copy
from decimal import Decimal, ROUND_HALF_UP, localcontext

from planning import resolve_question, validate_planned_analysis
from writing import study_hash


def analyze_adoption(study, brief, plan, question_ref, measurements, *, analysis_id):
    """Compute active/eligible for one declared cohort, never infer values from prose.

    Claim references establish lineage, not measurement truth. The caller is
    responsible for deduplication, eligibility, same cohort/window and useful-event
    semantics. Missing prerequisites produce partial without a numerical finding.
    """
    packet = resolve_question(plan, brief, study, question_ref)
    q = packet['question']
    if q['method'] != 'product.adoption':
        raise ValueError('this executor supports product.adoption only')
    if not isinstance(analysis_id, str) or not analysis_id.strip():
        raise ValueError('nonempty analysis_id required')
    keys = {'eligible', 'active', 'unit', 'cohort', 'period', 'frequency'}
    if not isinstance(measurements, dict) or set(measurements) != keys:
        raise ValueError('measurements must contain exactly eligible/active/unit/cohort/period/frequency')
    if measurements['unit'] != 'users':
        raise ValueError('adoption counts must use users')
    evidence = {e['requirement']: set(e['claim_refs']) for e in q['evidence_map']}
    gaps = list(q['unknowns'])
    for gap in packet['gaps']:
        gaps.extend(f'missing required evidence: {r}' for r in gap['missing_requirements'])
    for key, requirement in [('eligible', 'eligible_population'), ('active', 'useful_event')]:
        measure = measurements[key]
        if not isinstance(measure, dict) or set(measure) != {'value', 'claim_refs'}:
            raise ValueError(f'{key}: value and claim_refs required')
        value, refs = measure['value'], measure['claim_refs']
        if value is not None and (type(value) is not int or value < 0):
            raise ValueError(f'{key}: nonnegative integer or None required')
        if not isinstance(refs, list) or any(not isinstance(ref, str) for ref in refs) or len(set(refs)) != len(refs):
            raise ValueError(f'{key}: unique claim_refs required')
        if not set(refs).issubset(evidence.get(requirement, set())):
            raise ValueError(f'{key}: claim reference outside the declared requirement')
        if value is not None and not refs:
            raise ValueError(f'{key}: known measurement must cite evidence')
        if value is None:
            gaps.append(f'{key}: measurement unknown')
    for key in ('cohort', 'period', 'frequency'):
        value = measurements[key]
        if value is None:
            gaps.append(f'{key}: context unknown')
        elif not isinstance(value, str) or not value.strip():
            raise ValueError(f'{key}: nonempty text or None required')
    eligible, active = measurements['eligible']['value'], measurements['active']['value']
    if eligible == 0:
        gaps.append('eligible: zero denominator cannot establish an adoption percentage')
    if eligible is not None and active is not None and active > eligible:
        raise ValueError('active users cannot exceed eligible users in the same cohort')
    gaps = list(dict.fromkeys(gaps))
    percentage = None
    findings = []
    if not gaps:
        with localcontext() as context:
            context.prec = max(len(str(eligible)), len(str(active))) + 10
            percentage = format((Decimal(active) * 100 / Decimal(eligible)).quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP), 'f')
        findings = [{'statement': f'According to the declared measurements, {active} / {eligible} users '
                     f'performed the useful task ({percentage}%); cohort {measurements["cohort"]}, '
                     f'period {measurements["period"]}, expected frequency {measurements["frequency"]}.',
                     'status': 'inference', 'claim_refs': list(q['input_claim_refs'])}]
    row = {'id': analysis_id, 'question_ref': q['id'], 'question': q['question'],
           'method': q['method'], 'method_version': q['method_version'], 'scope': brief['scope'],
           'as_of': brief['as_of'], 'input_claim_refs': list(q['input_claim_refs']),
           'findings': findings, 'counterevidence': [], 'unknowns': gaps,
           'state': 'partial' if gaps else 'complete', 'needs_research': bool(gaps)}
    envelope = {'schema_version': '1.0', 'study_ref': study['id'],
                'input_revision': plan['input_revision'], 'analyses': [row]}
    verdict = validate_planned_analysis(envelope, plan, brief, study)
    if not verdict['valid']:
        raise ValueError('; '.join(verdict['errors']))
    return {'envelope': envelope, 'method_output': {
                'method': q['method'], 'method_version': q['method_version'],
                'measurements': copy.deepcopy(measurements), 'measurements_revision': study_hash(measurements),
                'percentage': percentage, 'percentage_unit': 'percent of eligible users',
                'rounding': '0.01 percentage point, HALF_UP',
                'limitations': ['Measurements are supplied by the analyst, not extracted or independently verified.',
                                'Same cohort/window, distinct users and useful-event semantics require review.',
                                'This result does not establish retention, causal benefit or another period.']},
            'human_approval': False}
