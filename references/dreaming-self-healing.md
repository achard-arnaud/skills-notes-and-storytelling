# Dreaming / self-healing template governance

The loop borrows the useful principle behind "dreaming" and self-healing systems: every completed run can expose reusable improvements. Promotion remains human-governed.

## Trigger

Run this routine when:
- a new document family was required;
- a repeated manual layout repair appeared;
- a side-story type repeatedly solved the same reading problem;
- a contract gap caused unsupported prose, poor sourcing or visual defects;
- a reader asks for a reusable new output pattern.

## Procedure

1. Capture the run's QA defects and successful adaptations.
2. Separate:
   - case-specific content;
   - reusable content rule;
   - reusable layout rule;
   - reusable contract/gate.
3. Create a `candidate` template or contract patch.
4. Add a regression fixture representing the failure.
5. Rerun the existing examples and the new fixture.
6. Produce a delta note:
   - why change;
   - affected templates;
   - compatibility;
   - evidence/QA impact;
   - rollback.
7. Request human validation.
8. Promote only after explicit approval.

## Hard rule

No autonomous promotion to the canonical template catalog.

The system may:
- propose;
- branch;
- test;
- render;
- report.

A human decides:
- promote;
- revise;
- reject;
- retire.

## DOCX preference contract

For this repo's users, every requested `.doc` / `.docx` note routes through:
1. `decision-notes-and-storytelling`;
2. the runtime DOCX creation/editing skill;
3. render-and-inspect QA.

This repository is the durable auditable source of truth for that behavior.
