---
template_type: closing
template_version: 0.1.0
fixture_version: 0.1.0
workflow_version: 1.3.1
analysis_dimension: business
fixture_role: qa
---

# Closing fixture — evidence-grounded executive conversation

## Run declaration

- `closing_mode`: `BRIEF_AND_DEBRIEF`
- `conversation_type`: `EXECUTIVE_MEETING`
- desired commitment: sponsor a 45-minute working session with the process owner and control owner;
- minimum acceptable commitment: confirm the decision criteria and name the correct owner;
- stop condition: explicit no-priority decision or unresolved legal/contact restriction.

## Source lanes

| Lane | Input | Status |
|---|---|---|
| Counterparty reality | public strategy, role mandate, prior exchange | mixed fact / unknown |
| Offer truth | two measured cases and one failed case | sourced proof |
| Conversation hypothesis | operating friction is now a sponsor-level priority | hypothesis to test |

## Mandate and match

| Decision criterion | Proof | Transfer mechanism | Gap | Validation question |
|---|---|---|---|---|
| Cross-functional ownership | Case P1 | Same sponsor/process/control triangle | Industry scope differs | Who owns the operating outcome? |
| Measurable adoption | Case P2 | Comparable distributed user base | Baseline metric unknown | Which behavior must change first? |

## Proof stories

- P1 short form: context → contested ownership → decision-right design → measured cycle-time result → relevance.
- P2 short form: adoption plateau → workflow redesign → observable usage outcome → relevance.

## Conversation sequence

1. State the meeting thesis and ask permission to test it.
2. Ask two decision-changing questions about ownership and priority.
3. Stop and listen; select P1 or P2 only after the answer.
4. Surface the strongest risk or objection.
5. Propose the desired working session; fall back to owner identification and criteria confirmation.

## Objection and reach recovery

| Signal | Diagnosis branch | Ethical response | Stop/escalate condition |
|---|---|---|---|
| “Not my remit” | owner mismatch vs polite refusal | ask for the correct owner and a forwardable two-line note | no referral or explicit refusal |
| Gatekeeper requests purpose | relevance/proof threshold | give truthful purpose, sponsor value and bounded duration | respect contact restriction |

## Debrief harvest

Record commitments, exact objections, new facts vs interpretations, stakeholder updates, proof response, follow-up owner/date, source IDs and the smallest next bridge.

## Expected QA result

- observable ask and fallback;
- independent truth lanes preserved;
- proof transfer tested rather than asserted;
- reach path contains no deception or refusal bypass;
- red-team verdict recorded before delivery.

