---
template_type: closing
template_version: 0.1.0
fixture_version: 0.1.0
workflow_version: 1.3.1
analysis_dimension: business
fixture_role: nrt
drift_policy: bounded
case: ODDO BHF Head of Transformation and AI interview coaching
---

# Closing NRT — ODDO BHF interview coaching

## Purpose

Replay this fixture when changing Closing routing, input contracts, proof-story selection, interview coaching, objection handling, reach recovery, debrief harvest or bridge behavior. It protects the analytical shape learned from the ODDO coaching artifact; it is not a source of current company, role or candidate facts.

All time-sensitive company, executive, role and hiring claims MUST be revalidated.

## Required run declaration

- `closing_mode`: `BRIEF_AND_DEBRIEF`;
- `conversation_type`: `INTERVIEW`;
- primary audience: senior sponsor and/or hiring panel;
- desired commitment: advance to the next decision stage with an agreed mandate hypothesis;
- minimum acceptable commitment: clarify mandate, decision rights, success criteria and unresolved fit gaps;
- source baseline: current company-strategy note + candidate proof ledger + role context.

## Independent truth lanes

The replay fails if it blends these before match:

1. **Company/role reality:** public strategy, operating model, leadership mandates, job signals and explicit unknowns.
2. **Candidate truth:** achievements, scope, quantified outcomes, methods and limits from the CV or verified evidence.
3. **Coaching hypotheses:** likely interview concerns, desired posture, mandate proposal and conversation tactics.

## Decision spine to preserve

When evidence supports it, the coaching close should:

1. position the candidate against the actual transformation mandate, not a generic “Head of AI” archetype;
2. translate company strategy into likely decision criteria and stakeholder interfaces;
3. map candidate proof to those criteria using explicit transfer mechanisms and gaps;
4. select a small portfolio of non-duplicative proof stories;
5. propose a bounded initial mandate or 90-day hypothesis without pretending it is already agreed;
6. provide senior questions that reveal decision rights, value ownership, governance, adoption and sponsor expectations;
7. expose posture traps: overselling technology, claiming an unofficial org chart, using scale numbers without relevance, or prescribing before discovery;
8. close with an explicit next commitment and a smaller fallback;
9. harvest the debrief into facts, interpretations, objections, stakeholder updates and follow-up actions.

## ODDO functional reference, not frozen facts

The original run found value in testing whether ODDO was assembling a transverse Data/AI transformation capability rather than a standalone technical AI factory. On replay, test the organizational question anew. Do not freeze named executives, reporting lines, role availability, metrics or chronology from the prior artifact.

## Proof portfolio NRT

The fixture should support candidate evidence such as portfolio arbitration, transformation governance, champion/adoption networks, governed GenAI/agentic delivery, vendor choices and product/platform building only when source-backed. Each proof must include:

- the decision criterion it answers;
- context and tension;
- candidate action/choice;
- measurable result or explicitly unavailable metric;
- learning;
- transfer mechanism to the current mandate;
- limitation or validation question.

The replay fails if achievements become a biography list or if impressive numbers substitute for relevance.

## Red-team propositions

At minimum attack:

- the role may be coordination/change leadership rather than ownership of AI delivery;
- public company evidence may not reveal the real internal mandate or reporting line;
- candidate experience may be large-scale but not transferable to the target's governance, culture or business mix;
- a 90-day proposal may be premature before sponsor and decision-right discovery;
- the closing ask may overreach the interview stage.

Record one verdict, one bounded repair when needed and one verification. A second material failure routes to `REOPEN_TARGETED`.

## Reader and artifact NRT

For a two-page coaching artifact, preserve:

- bullet-led landscape format and body text >=9 pt;
- immediately usable posture, mandate hypothesis, proof stories, questions, traps and closing language;
- evidence-status cues without turning the artifact into a research report;
- no loss of decisive content merely to fit the page count.

## Debrief harvest NRT

After the conversation, capture:

- confirmed vs disproved mandate hypotheses;
- decision rights and stakeholder map changes;
- which proof stories landed, failed or raised concern;
- exact objections and unanswered questions;
- commitments, owners and dates;
- company-brief corrections and new research tasks;
- next bridge: updated Closing, Company/Architecture Note, Opportunity Note or no further action.

## Failure conditions

- generic interview advice replaces company-specific evidence;
- company facts and coaching hypotheses are blended;
- candidate claims lack source lineage;
- no transfer mechanism connects proof to mandate;
- questions do not change the recommended positioning;
- red-team is generic or absent;
- reach/objection tactics use deception or bypass explicit refusal;
- debrief interpretations are stored as facts;
- stale ODDO facts are reused without validation.

## Expected closure

End with a proportionate, explicit commitment ask, a reversible fallback, unresolved fit risks and the evidence needed for the next decision.

