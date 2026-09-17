# Tier 3 dreaming — ODDO strategy + interview coaching → Closing

## Run signal

Two related artifacts exposed a reusable gap:

- the business architecture note reconstructed company strategy, operating model, people-as-evidence, capability trajectory and hard gates;
- the interview coaching note converted that context plus candidate evidence into posture, mandate, proof stories, questions, traps and a closing formulation.

The second artifact was unusually useful because it did not merely summarize the first. It translated evidence into a specific consequential conversation while preserving uncertainty. Existing templates could approximate parts of that work, but none governed the full transition from researched truth to commitment and debrief harvest.

## Case-specific versus reusable

Case-specific and excluded from the canonical template:

- ODDO executives, reporting hypotheses, chronology and hiring signals;
- François Arnaud's achievements, numbers and proposed positioning;
- the exact Head of Transformation & AI mandate and interview language.

Reusable and included:

- independent lanes for counterparty truth, candidate/offer truth and conversation hypotheses;
- explicit desired/minimum commitments and stop conditions;
- mandate → proof → transfer mechanism → gap → validation question mapping;
- compact proof-story portfolio;
- listening gates and decision-changing questions;
- objection and reach-obstacle diagnosis before response;
- truthful, boundary-respecting reach recovery;
- debrief harvest that updates RunContext without turning interpretation into fact;
- bounded red-team of mandate, proof transfer, stakeholder veto and close size.

## Dependencies and expected inputs

Closing is downstream of evidence collection. Preferred inputs are a current company/strategy note, role or opportunity context, candidate/offer proof ledger, source ledger, unknowns and prior exchanges. It can run with partial inputs only by narrowing to discovery and a low-commitment next step.

The template should normally bridge from `ARCHITECTURE_NOTE`, `TWO_PAGER`, `OPPORTUNITY_NOTE_ICP` or `DIAGNOSTIC_RECO_SELL_SIDE`; it routes back when target truth or proof is insufficient.

## Candidate delta

- add `CLOSING` as a candidate template;
- add a machine-readable closing-run contract;
- add the generic QA fixture and ODDO coaching NRT;
- extend enum, manifest, shared schemas, catalog, bridges and QA checklist;
- retain the existing workflow version because stage order is unchanged;
- validate UTF-8 explicitly so fixtures can safely contain normal decision notation.

## Review pass 1 — conformance and reader decision

Findings repaired:

- A prose-only contract would be hard for downstream tooling to validate; added `contracts/closing-run.schema.json` and manifest linkage.
- A business/product-only dimension list was too narrow for technical architecture or security closing conversations; Closing now supports all three analysis dimensions while defaulting to business.
- Debrief harvest needed an explicit provenance/privacy boundary; added authorized-source and sensitive-attribute constraints.

Verdict: the candidate is internally routable, versioned, fixture-backed and readable as a distinct document family rather than a renamed two-pager.

## Review pass 2 — mandatory red-team

### Proposition attacked

`CLOSING` deserves a distinct reusable template and will improve meeting preparation without encouraging premature or manipulative persuasion.

### Strongest counter-perspectives

1. It may duplicate `TWO_PAGER` or `OPPORTUNITY_NOTE_ICP` and add catalog noise.
2. “Closing” may bias the agent toward a predetermined yes instead of discovery.
3. Reach recovery may normalize bypassing gatekeepers or explicit refusal.
4. Candidate/company matching may launder public inference into interview fact.
5. A generic proof-story recipe may reward impressive but non-transferable achievements.

### Repair / narrowing

- defined Closing by its decision object: an observable next commitment plus debrief harvest, not page count or meeting summary;
- required desired and minimum commitments, but allowed an explicit no-go as valid closure;
- required insufficient-input behavior that narrows to discovery;
- prohibited impersonation, misrepresentation, pressure and refusal bypass;
- separated truth lanes until match and required revalidation of time-sensitive inputs;
- required a transfer mechanism, limitation and validation question for decisive proof.

### Verification verdict

`SURVIVES_WITH_NARROWING` — the template is justified as a candidate only with the discovery fallback, ethical reach boundary, proof-transfer gate and debrief provenance controls. Promotion should wait for at least one additional non-interview replay.

## Compatibility and rollback

- additive enum and manifest change; no existing template behavior changes;
- existing fixtures remain valid after shared schema enum expansion;
- rollback removes the Closing enum/manifest entry, two fixtures, template and contract, then reverts catalog/bridge/QA references;
- lifecycle stays `candidate`; no merge or promotion is implied.

