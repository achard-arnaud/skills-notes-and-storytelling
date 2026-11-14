"""Consume selected analytical findings through the existing writing bootstrap."""
from __future__ import annotations

import copy
import json
from pathlib import Path

from analysis import _shape
from analysis_impact import plan_analysis_revision
from planning import validate_planned_analysis
from writing import EVIDENCE_KEYS, _index, plan_iterative, prepare_from_scratch, study_hash

SCHEMA = json.loads((Path(__file__).parent / 'schemas/analysis-writing.v1.schema.json').read_text(encoding='utf-8'))


def _ref_key(ref):
    return ref['analysis_ref'], int(ref['finding_index'])


def prepare_analysis_writing(study, envelope, plan, brief, synthesis, reader_scaffold, *, perspective):
    """Prepare a candidate narrative, not prose or an approved analytical judgment.

    Findings are selected by identity/index from the exact envelope. Candidate
    thesis/headings are externally authored editorial inputs, not certified by refs.
    """
    verdict = validate_planned_analysis(envelope, plan, brief, study)
    errors = list(verdict['errors'])
    errors += _shape(synthesis, SCHEMA, root=SCHEMA)
    errors += _shape(reader_scaffold, SCHEMA['$defs']['readerScaffold'], '$scaffold', root=SCHEMA)
    if perspective not in ('product', 'business', 'combined'):
        errors.append('unsupported perspective')
    if errors:
        raise ValueError('; '.join(errors))
    if synthesis['study_ref'] != study['id'] or synthesis['envelope_revision'] != study_hash(envelope):
        raise ValueError('stale or foreign synthesis')
    analyses = {row['id']: row for row in envelope['analyses']}
    if set(analyses).intersection(_index(study)):
        raise ValueError('analysis ID collides with a study node')
    selected, findings = {}, []
    for ref in synthesis['observations']:
        row = analyses.get(ref['analysis_ref'])
        index = int(ref['finding_index'])
        if row is None or index >= len(row['findings']):
            raise ValueError('unresolved finding reference')
        selected[_ref_key(ref)] = row['findings'][index]
        findings.append({'reference': copy.deepcopy(ref), **copy.deepcopy(row['findings'][index])})
    if selected and not synthesis['candidate_thesis']['finding_refs']:
        raise ValueError('candidate thesis must reference selected findings')
    if any(_ref_key(ref) not in selected for ref in synthesis['candidate_thesis']['finding_refs']):
        raise ValueError('candidate thesis references findings outside selected synthesis')
    claim_ids = {c['id'] for c in study['claims']}
    pillar_ids = {p['id'] for p in study.get('pillars', [])}
    bindings, topology, used_claims = [], [], set()
    for section in reader_scaffold['sections']:
        if section['id'] in analyses:
            raise ValueError('section ID collides with an analysis')
        if not section['analysis_refs'] and not section['claim_ids']:
            raise ValueError('each block must consume analysis or claims')
        claims = set(section['claim_ids'])
        if not claims.issubset(claim_ids) or not set(section['pillar_ids']).issubset(pillar_ids):
            raise ValueError('unresolved block claim or pillar')
        for ident in section['analysis_refs']:
            if ident not in analyses:
                raise ValueError('unresolved block analysis')
            selection = [finding for (analysis_id, _), finding in selected.items() if analysis_id == ident]
            if not selection and analyses[ident]['state'] != 'partial':
                raise ValueError('block analysis was not selected in synthesis')
            for finding in selection:
                claims.update(finding['claim_refs'])
        used_claims.update(claims)
        topology.append({k: copy.deepcopy(section[k]) for k in ('id', 'title', 'pillar_ids')})
        topology[-1]['claim_ids'] = sorted(claims)
        bindings.append({'section_id': section['id'], 'analysis_refs': list(section['analysis_refs']),
                         'claim_ids': sorted(claims)})
    bound_analyses = {ident for binding in bindings for ident in binding['analysis_refs']}
    if not {ident for ident, _ in selected}.issubset(bound_analyses):
        raise ValueError('selected analytical findings must be consumed by a block')
    covered = set()
    for item in synthesis['claim_disposition']:
        ident = item['claim_ref']
        if ident in covered or ident not in claim_ids:
            raise ValueError('unknown or duplicate claim disposition')
        covered.add(ident)
        if item['state'] != 'included' and not item['reason'].strip():
            raise ValueError('omitted/displaced claim needs a reason')
        if (ident in used_claims) != (item['state'] == 'included'):
            raise ValueError('claim disposition disagrees with core block usage')
    if covered != claim_ids:
        raise ValueError('every study claim needs an explicit disposition')
    evidence = {k: study[k] for k in EVIDENCE_KEYS if k in study}
    result = prepare_from_scratch(evidence, {'sections': topology})
    context = {'schema_version': '1.0', 'study_ref': study['id'],
               'input_revision': envelope['input_revision'], 'envelope_revision': study_hash(envelope),
               'plan_revision': study_hash(plan), 'intent_revision': study_hash(brief),
               'synthesis_revision': study_hash(synthesis), 'perspective': perspective,
               'candidate_thesis': copy.deepcopy(synthesis['candidate_thesis']),
               'resolved_findings': findings, 'bindings': bindings,
               'claim_disposition': copy.deepcopy(synthesis['claim_disposition']),
               'counterevidence': {row['id']: list(row['counterevidence']) for row in envelope['analyses']},
               'unknowns': {row['id']: list(row['unknowns']) for row in envelope['analyses']},
               'analysis_states': {row['id']: row['state'] for row in envelope['analyses']},
               'gaps': copy.deepcopy(verdict['gaps']), 'human_approval': False,
               'limitations': ['Candidate thesis and headings require independent semantic/editorial review.',
                              'No prose, fact, recommendation or approval generated by this adapter.']}
    context['context_revision'] = study_hash(context)
    result['analysis_context'] = context
    return result


def plan_analysis_writing_revision(study, envelope, analysis_context, changed_ids, *,
                                   expected_study_hash, expected_envelope_hash):
    """Plan claim/output impacts through explicit late bindings, without mutation."""
    if not isinstance(analysis_context, dict):
        raise ValueError('analysis_context required')
    context = {k: v for k, v in analysis_context.items() if k != 'context_revision'}
    if analysis_context.get('context_revision') != study_hash(context):
        raise ValueError('analysis context revision mismatch')
    if (context.get('study_ref') != study.get('id')
            or context.get('envelope_revision') != study_hash(envelope)
            or context.get('input_revision') != envelope.get('input_revision')):
        raise ValueError('stale or foreign analysis context')
    receipt = plan_analysis_revision(study, envelope, changed_ids,
                                     expected_study_hash=expected_study_hash,
                                     expected_envelope_hash=expected_envelope_hash)
    binding_schema = {'type': 'object', 'additionalProperties': False,
                      'required': ['section_id', 'analysis_refs', 'claim_ids'],
                      'properties': {'section_id': {'type': 'string', 'minLength': 1},
                                     'analysis_refs': {'type': 'array', 'uniqueItems': True, 'items': {'type': 'string'}},
                                     'claim_ids': {'type': 'array', 'uniqueItems': True, 'items': {'type': 'string'}}}}
    if context.get('schema_version') != '1.0' or context.get('human_approval') is not False:
        raise ValueError('unsupported or approved analysis context')
    binding_errors = _shape(context.get('bindings'), {'type': 'array', 'items': binding_schema})
    if binding_errors:
        raise ValueError('; '.join(binding_errors))
    analyses = {row['id'] for row in envelope['analyses']}
    sections = {section['id']: section for section in study.get('sections', [])}
    affected = set(receipt['invalidate_analysis_ids'])
    affected_sections = set()
    seen = set()
    for binding in context['bindings']:
        ident = binding['section_id']
        if ident in seen or ident not in sections or not set(binding['analysis_refs']).issubset(analyses):
            raise ValueError('unknown or duplicate narrative analysis binding')
        seen.add(ident)
        if not set(binding['claim_ids']).issubset(set(sections[ident].get('claim_ids', []))):
            raise ValueError('binding claims differ from current section')
        if affected.intersection(binding['analysis_refs']):
            affected_sections.add(ident)
    indexed = _index(study)
    writer_ids = sorted((set(changed_ids) & set(indexed)) | affected_sections)
    writing_plan = plan_iterative(study, writer_ids)
    paragraphs = {p['id'] for ident in affected_sections for p in sections[ident].get('paragraphs', [])}
    writing_plan['evidence_invalidated_paragraph_ids'] = sorted(
        set(writing_plan['evidence_invalidated_paragraph_ids']) | paragraphs)
    receipt['writing'] = writing_plan
    receipt['analysis_invalidated_section_ids'] = sorted(affected_sections)
    receipt['analysis_invalidated_paragraph_ids'] = sorted(paragraphs)
    return receipt
