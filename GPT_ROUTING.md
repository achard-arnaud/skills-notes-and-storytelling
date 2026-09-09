# GPT runtime routing policy

This file records the user-level routing preference for GPT environments that can load this repository as a skill source.

## Document routing
When the requested deliverable is a `.doc` or `.docx` note:
1. invoke `decision-notes-and-storytelling`;
2. invoke the runtime DOCX creation/editing skill;
3. apply render → inspect every page → iterate;
4. deliver only after the final render passes.

## Template learning
When a run requires a new output family:
- build it as a candidate;
- record QA deltas and reusable rules;
- update this repository on a branch;
- require explicit human validation before promotion.

The skill may propose and test its own improvement. Canonical promotion remains human-controlled.
