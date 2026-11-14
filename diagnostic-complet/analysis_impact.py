"""Plan selective analysis review using the existing evidence dependency closure."""
from __future__ import annotations

from analysis import validate_analysis_envelope
from writing import _index, plan_iterative, study_hash


def plan_analysis_revision(study, envelope, changed_ids, *, expected_study_hash, expected_envelope_hash):
    """Plan from an explicit, unchanged baseline; never refresh or mutate outputs.

    Call before applying an evidence/output correction. The receipt invalidates
    dependent analyses for review, but does not make the old envelope valid against
    a changed study. Its global evidence revision still must be reconciled explicitly.
    Narrative analysis bindings are not available in this layer; the nested writing
    plan includes only existing claim-to-section/paragraph/side-story dependencies.
    """
    if expected_study_hash != study_hash(study) or expected_envelope_hash != study_hash(envelope):
        raise ValueError('baseline lease mismatch; reread study and envelope')
    if not isinstance(changed_ids, list) or any(not isinstance(i, str) or not i for i in changed_ids):
        raise ValueError('changed_ids must be a list of nonempty IDs')
    if len(set(changed_ids)) != len(changed_ids):
        raise ValueError('changed_ids must be unique')
    verdict = validate_analysis_envelope(envelope, study)
    if not verdict['valid']:
        raise ValueError('; '.join(verdict['errors']))
    indexed = _index(study)
    analyses = {row['id']: row for row in envelope['analyses']}
    if set(analyses) & set(indexed):
        raise ValueError('analysis ID collides with a study node')
    changed = set(changed_ids)
    missing = changed - set(indexed) - set(analyses)
    if missing:
        raise ValueError(f'unknown changed IDs: {sorted(missing)}')
    writing_plan = plan_iterative(study, sorted(changed & set(indexed)))
    affected_claims = set(writing_plan['claim_ids'])
    affected = {ident for ident, row in analyses.items()
                if ident in changed or affected_claims.intersection(row['input_claim_refs'])}
    return {'schema_version': '1.0', 'study_ref': study['id'],
            'baseline_study_hash': expected_study_hash,
            'baseline_envelope_hash': expected_envelope_hash,
            'input_revision': envelope['input_revision'], 'changed_ids': sorted(changed),
            'claim_ids': sorted(affected_claims), 'invalidate_analysis_ids': sorted(affected),
            'question_refs': sorted({analyses[ident]['question_ref'] for ident in affected}),
            'untouched_analysis_ids': sorted(set(analyses) - affected),
            'writing': writing_plan, 'envelope_refreshed': False, 'human_approval': False,
            'limits': ['No narrative analysis bindings evaluated.',
                       'No evidence, finding, status or revision mutated.',
                       'Mandate/scope changes require a new analysis plan.',
                       'This baseline receipt does not certify a future envelope or revised study.']}
