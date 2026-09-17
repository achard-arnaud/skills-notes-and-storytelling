# Template — Closing

Version: 0.1.0 candidate

## Purpose

Turn a sufficiently researched opportunity into a meeting-ready strategy for earning a credible next commitment. Use for interviews, executive meetings, sales or partnership conversations, objection recovery and access/reach obstacles. The output may prepare the conversation, harvest a debrief, or do both.

Do not use it as a generic meeting brief, transcript summary, coercive persuasion script or substitute for missing account/company research.

## Required declaration

Before scaffolding, declare:

- `closing_mode`: `BRIEF | DEBRIEF | BRIEF_AND_DEBRIEF`;
- `conversation_type`: `INTERVIEW | EXECUTIVE_MEETING | SALE | PARTNERSHIP | REACH_RECOVERY | OTHER`;
- primary audience and decision maker, when known;
- desired commitment and minimum acceptable commitment;
- timebox and channel;
- source baseline and freshness cutoff;
- active ethical, legal, confidentiality or contact constraints.

When a machine-readable run record is created, validate it against [contracts/closing-run.schema.json](../contracts/closing-run.schema.json).

## Input contract

### Required

- conversation objective and stakes;
- counterparty identity or bounded persona;
- target/account/company context sufficient to state the mandate or problem;
- offer, proposition or candidate evidence sufficient to support at least one relevant proof;
- known unknowns and hard gates;
- meeting stage, channel and expected duration.

### Optional but high-value

- prior strategic/company brief and its `RunContext`;
- CV, achievement ledger, case studies or product proof;
- prior exchanges, transcript, objections and stakeholder map;
- public strategy, executive mandates, role description and job-posting signals;
- reach path, gatekeeper context and permitted alternate routes;
- competitive alternatives, incumbent/default option and timing trigger.

### Insufficient-input behavior

If counterparty truth or proof is too weak, do not fabricate a personalized close. Produce a bounded discovery close: assumptions to validate, questions, evidence to collect and a low-commitment next step. Mark unavailable or stale inputs explicitly.

## Dependency contract

Closing consumes prior evidence but does not promote it to fresh truth.

- Import the source ledger, fragments, claims, contradictions, unknowns and rejected alternatives from `RunContext` when available.
- Revalidate time-sensitive company, role, executive and hiring signals.
- Keep three lanes independent until match: `counterparty reality`, `candidate/offer truth`, `conversation hypothesis`.
- Prefer a bridge from `ARCHITECTURE_NOTE`, `TWO_PAGER`, `OPPORTUNITY_NOTE_ICP` or `DIAGNOSTIC_RECO_SELL_SIDE` when those runs already contain the needed truth.
- Route back to company research or an opportunity note when the mandate, stakeholders or proof remain materially unresolved.

## Construction logic

### 1. Define closure

State one desired commitment, one minimum acceptable commitment and one walk-away/stop condition. A commitment may be a decision, sponsored next meeting, evidence request, pilot framing or explicit no-go. Do not equate politeness or vague interest with closure.

### 2. Reconstruct the mandate

Infer what the counterparty must accomplish, protect and avoid. Separate public facts, supplied context and hypotheses. Include stakeholder incentives and decision rights only when evidenced or clearly marked unknown.

### 3. Build the match

Map each material mandate or decision criterion to:

- relevant proof;
- transfer mechanism: why the proof applies here;
- gap or caveat;
- question that tests the match;
- source/claim IDs.

Do not use biography, feature inventory or generic credentials as proof without a transfer mechanism.

### 4. Select proof stories

Use 2–4 stories that cover the decisive criteria without duplication. Each story carries `context → tension → action/choice → measurable result → learning → relevance here`. Keep unsupported numbers out. Prepare a short and a deep version when meeting time is uncertain.

### 5. Design the conversation

Sequence:

`opening thesis → diagnostic questions → listening gate → matched proof → challenge/objection → mandate proposal → commitment ask → fallback`.

Questions must change the recommended path; remove questions whose answers would not affect the close. Include cues for when to stop presenting and listen.

### 6. Handle obstacles without deception

For objections and reach barriers, classify the obstacle before responding:

- missing relevance or proof;
- timing/budget/priority;
- stakeholder or decision-right mismatch;
- risk/control concern;
- access/gatekeeper constraint;
- explicit refusal or contact boundary.

Use truthful reframing, a smaller ask, sponsor-safe forwarding material or an alternate legitimate route. Never recommend impersonation, misrepresentation, pressure, bypass of an explicit refusal, or tactics that expose a gatekeeper or sponsor to harm.

### 7. Close and preserve optionality

Make the ask explicit, proportionate and easy to answer. Provide a fallback that still produces information or a reversible next step. Name the evidence or event that should stop pursuit.

### 8. Harvest the debrief

Capture observations separately from interpretation:

- commitments made and by whom;
- objections and exact decision criteria;
- new facts, hypotheses and contradictions;
- stakeholder/decision-right updates;
- proof that landed or failed;
- follow-up owner, due date and artifact;
- next template/bridge, if any;
- reusable learning candidate for dreaming.

Harvest only information obtained legitimately in the conversation or its authorized follow-up. Preserve provenance and access restrictions; do not infer personal or sensitive attributes that were not volunteered or needed for the decision.

## Output spine

1. closing thesis, desired commitment and fallback;
2. mandate / decision criteria / stakeholder map;
3. match matrix: need → proof → transfer → gap → validation question;
4. proof-story cards;
5. conversation sequence with listening gates;
6. objections and reach-recovery matrix;
7. explicit ask, fallback and stop conditions;
8. debrief harvest block and next bridge.

## Counter-perspective and review

Run two distinct passes:

1. **Conformance + reader pass:** input sufficiency, evidence lineage, usable sequencing, clarity of ask and timebox fit.
2. **Red-team pass:** attack whether the mandate is wrong, the proof is non-transferable, the close is premature, a hidden stakeholder can veto, the reach tactic violates a boundary, or the proposed commitment is too large.

Use the normal verdicts. Apply at most one repair/narrowing pass and one verification pass. If the proposition still fails, output `REOPEN_TARGETED` and route to the missing research or proof task.

## QA gates

- desired and minimum acceptable commitments are observable;
- facts, proofs and hypotheses remain separate until match;
- every decisive proof has lineage and a transfer mechanism;
- questions have decision value;
- objections include a diagnostic branch, not only canned answers;
- reach recovery remains truthful and respects refusal/contact boundaries;
- fallback is smaller and reversible, not disguised repetition of the same ask;
- debrief harvest can update `RunContext` without laundering interpretation into fact;
- output fits the stated meeting timebox and channel.
