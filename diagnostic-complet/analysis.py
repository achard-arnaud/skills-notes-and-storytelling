"""Pure pre-scaffold analysis validation (stdlib); no generation or migration."""
from __future__ import annotations

from datetime import date
import json
from pathlib import Path
import re

from writing import EVIDENCE_KEYS, study_hash

SCHEMA = json.loads((Path(__file__).parent / 'schemas/analysis-envelope.v1.schema.json').read_text(encoding='utf-8'))
LEGACY_SOURCE = '75c8293de6984c6fac80e016528bdfa4ec019226/b2303d0bd50e23a7c7a2ad7eb71b896fcacdc446'


def _shape(value, schema, path='$'):
    """Evaluate only the JSON Schema vocabulary used by this fixed local contract.

    Internal helper, not a general JSON Schema implementation. Schema changes must
    extend the supported vocabulary and its parity checks before using new keywords.
    """
    if '$ref' in schema:
        schema = SCHEMA['$defs'][schema['$ref'].removeprefix('#/$defs/')]
    errors = []
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str, 'boolean': bool}
    if kind and type(value) is not types[kind]:
        return [f'{path}: expected {kind}']
    if 'const' in schema and (type(value) is not type(schema['const']) or value != schema['const']):
        errors.append(f'{path}: expected constant {schema["const"]!r}')
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{path}: unsupported value')
    if isinstance(value, dict):
        for key in schema.get('required', []):
            if key not in value:
                errors.append(f'{path}.{key}: required')
        properties = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            errors.extend(f'{path}.{key}: unexpected field' for key in value if key not in properties)
        for key in properties.keys() & value.keys():
            errors.extend(_shape(value[key], properties[key], f'{path}.{key}'))
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errors.append(f'{path}: too few items')
        if schema.get('uniqueItems') and any(item in value[:i] for i, item in enumerate(value)):
            errors.append(f'{path}: duplicate items')
        if 'items' in schema:
            for i, item in enumerate(value):
                errors.extend(_shape(item, schema['items'], f'{path}[{i}]'))
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0):
            errors.append(f'{path}: text too short')
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            errors.append(f'{path}: invalid pattern')
        if schema.get('format') == 'date':
            try:
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                    raise ValueError('not an ISO date')
                date.fromisoformat(value)
            except ValueError:
                errors.append(f'{path}: invalid date')
    for clause in schema.get('allOf', []):
        if 'if' in clause:
            if not _shape(value, clause['if'], path):
                errors.extend(_shape(value, clause['then'], path))
        else:
            errors.extend(_shape(value, clause, path))
    return errors


def _study_claims(study):
    if not isinstance(study, dict) or not isinstance(study.get('id'), str) or not study['id']:
        return set(), ['study: nonempty id required']
    claims = study.get('claims')
    if not isinstance(claims, list):
        return set(), ['study.claims: expected array']
    ids, errors = set(), []
    for i, claim in enumerate(claims):
        ident = claim.get('id') if isinstance(claim, dict) else None
        if not isinstance(ident, str) or not ident:
            errors.append(f'study.claims[{i}]: nonempty id required')
        elif ident in ids:
            errors.append(f'study.claims[{i}]: duplicate id {ident}')
        else:
            ids.add(ident)
    return ids, errors


def _references(rows, claim_ids):
    errors, seen = [], set()
    for row in rows:
        ident = row['id']
        if ident in seen or ident in claim_ids:
            errors.append(f'analysis {ident}: duplicate id or collision with claim')
        seen.add(ident)
        refs = row['input_claim_refs'] + [ref for finding in row['findings'] for ref in finding['claim_refs']]
        for ref in dict.fromkeys(refs):
            if ref not in claim_ids:
                errors.append(f'analysis {ident}: unresolved claim {ref}')
    return errors


def _verdict(structure, references, gaps):
    return {'valid': not (structure or references), 'errors': structure + references,
            'structural_errors': structure, 'reference_errors': references,
            'gaps': gaps, 'human_approval': False}


def validate_analysis_envelope(envelope, study):
    """Validate a separate v1 envelope against the current study, without mutation.

    References and input freshness are checked only after structural validation.
    The study remains owned by runtime.validate_study; this validates just the study
    identity/claim index needed here. Method catalog and question registry resolution,
    truth, narrative binding and descendant invalidation are outside this contract.
    """
    structure = _shape(envelope, SCHEMA)
    claim_ids, study_errors = _study_claims(study)
    structure.extend(study_errors)
    if structure:
        return _verdict(structure, [], [])
    references = _references(envelope['analyses'], claim_ids)
    if envelope['study_ref'] != study['id']:
        references.append('study_ref: does not match current study')
    try:
        revision = study_hash({key: study[key] for key in EVIDENCE_KEYS if key in study})
    except (TypeError, ValueError):
        return _verdict(['study: evidence projection must be JSON serializable'], references, [])
    if envelope['input_revision'] != revision:
        references.append('input_revision: stale or foreign evidence projection')
    gaps = [{'analysis_id': row['id'], 'unknowns': list(row['unknowns']),
             'needs_research': row['needs_research']} for row in envelope['analyses']
            if row['state'] == 'partial' or row['unknowns'] or row['needs_research']]
    return _verdict([], references, gaps)


def validate_legacy_analysis_result(payload, study):
    """Explicit legacy route, pinned to LEGACY_SOURCE; never convert to v1.

    Preserve the donor's required nonempty affects_blocks/findings/input refs and
    statuses. Block existence is not asserted here: no scaffold is passed in.
    Original study identity and revision are absent from legacy, hence not proven.
    """
    structure = _shape(payload, SCHEMA['$defs']['legacyResult'])
    claim_ids, study_errors = _study_claims(study)
    structure.extend(study_errors)
    gaps = ['legacy: original study/revision and block resolution not established']
    if structure:
        return _verdict(structure, [], gaps)
    return _verdict([], _references([payload], claim_ids), gaps)
