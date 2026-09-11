# Feedback / dreaming / self-healing governance

The loop harvests reusable improvements from completed runs while keeping promotion human-governed.

## Trigger

Run this mode when:
- a new document family was required;
- a repeated manual layout repair appeared;
- a side-story type repeatedly solved the same reading problem;
- a contract gap caused unsupported prose, poor sourcing or visual defects;
- explicit human feedback defines a reusable preference;
- the same post-delivery correction appears across multiple outputs.

## Procedure

1. Capture QA defects, human feedback and successful adaptations.
2. Separate:
   - case-specific content;
   - reusable research rule;
   - reusable content rule;
   - reusable layout rule;
   - reusable contract/gate;
   - reusable mode/routing rule.
3. Identify the affected template and current version.
4. Create a candidate patch with a proposed semantic version bump.
5. Add or update the linked regression fixture.
6. Run the validator and all compatible fixtures.
7. Produce a delta note:
   - why change;
   - affected templates/modes;
   - compatibility;
   - evidence/QA impact;
   - rollback.
8. Request human validation.
9. Promote only after explicit approval.

## Cross-lifecycle rule

Template, workflow and QA example versions evolve together. See [references/versioning-and-lifecycle.md](versioning-and-lifecycle.md).

No template version may be promoted when:
- its declared fixture is absent;
- the fixture targets another major template version;
- the workflow compatibility is stale;
- a new hard visual/content gate lacks regression coverage.

## Hard rule

No autonomous promotion to the canonical template catalog.

The system may:
- propose;
- branch;
- test;
- render;
- report;
- open a draft PR.

A human decides:
- promote;
- revise;
- reject;
- retire.

## DOCX preference contract

Every requested `.doc` / `.docx` decision note routes through:
1. `skills-notes-and-storytelling`;
2. the runtime DOCX creation/editing skill;
3. render-and-inspect QA.

This repository is the durable auditable source of truth for that behavior.
