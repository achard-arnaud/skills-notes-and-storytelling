# Template — Buy-side gap analysis

## Purpose
Support a buyer deciding whether to adopt, replace, complement or partner with a vendor/platform.

## Page 1 — Decision
- recommendation;
- confidence and key condition;
- buyer baseline;
- target outcome;
- top 3 gaps / advantages;
- smallest reversible validation step.

## Core sections

### 1. Buyer baseline
Current systems, workflows, queues, operating ownership, licenses, pain, constraints.

### 2. Target architecture / operating model
Describe the desired state before naming the winning vendor.

### 3. Capability matrix
Use a table. Required columns:
`criterion | incumbent | challenger | gap/implication | evidence`

### 4. Replacement / coexistence path
- replace directly;
- wrap and coexist;
- migrate by queue/use-case;
- retain incumbent for residual UI-only automation.

### 5. Economics
- license/subscription;
- infra;
- PS/integration;
- run/SRE;
- migration;
- change and retraining;
- avoided cost.

### 6. Hard gates
Security, unsupported UI surface, throughput, latency, regulatory, audit, rollback, SLAs.

### 7. Risks and falsifiers
State what evidence would reverse the recommendation.

### 8. Recommendation
`PURSUE | VALIDATE | NURTURE | REJECT` plus owner, experiment and stop condition.

## Side stories
- `false_lead`: superficial feature parity;
- `analytical_focus`: migration/TCO mechanism;
- `comparator`: adjacent alternative;
- `dezoom`: operating-model consequence;
- `method`: score/evidence caveat.

## Couches (4-layer)

Ce template est un cas concret des [4 couches découplées](../references/layered-architecture.md). Voir la ligne `BUY_SIDE_GAP_ANALYSIS` de la table de déclinaison pour l'objectif/longueur, les frameworks narratifs par défaut, la typologie de nodes dominante et les règles de vocabulaire propres à ce template. Le registre des méthodes narratives est détaillé dans [references/narrative-frameworks.md](../references/narrative-frameworks.md) ; les règles de retrieval/reranking claims vs fragments dans [references/retrieval-and-reranking.md](../references/retrieval-and-reranking.md).
