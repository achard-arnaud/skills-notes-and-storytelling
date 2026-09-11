# TODO

## Retro-engineering mode
Implement the documented reverse workflow in `references/modes.md`.

Required before production routing:
- inferred-template schema;
- visual/layout feature extraction contract;
- vision-first document inspection pipeline;
- OCR fallback adapter;
- neutral holdout exemplar generation;
- template similarity / regression checks;
- at least two human-reviewed reverse-engineering cases;
- lifecycle promotion from `todo` to `candidate`.

The first target use case should reverse-engineer a supplied professional note with:
- mixed prose and comparison tables;
- at least one diagram;
- repeated visual hierarchy;
- side-story/callout equivalent;
- enough semantic structure to infer transition logic.

## v2 backlog disposition — 2026-09-11

GitHub open-issue search returned no open issues at audit time. Unmerged branches are work inventory,
not proof of production completion.

Completed here: adaptive execution profiles; four template layers; typed evidence bundle validation;
manual-first gap planning and query deduplication; targeted retrieval and impact-preserving revisions;
context read-slice audit; selective language/ICP harvest; regression tests in CI.

Retained candidates:
- Debrief 360: preserved in references/debrief-360-candidate.md. Requires meeting fixtures and human
  validation before adding enum/schema routing. Do not infer posture from automatic summaries.
- Action plan from feat/icp-language-analysis-boundary: downstream execution artifact, not activated
  as an analysis template. Needs its own objective, owner/date/stop-condition contract and fixture.
- Personal branding profiles: do not inject named-person preferences into the generic skill. Resolve
  user-selected preferences per run; add persona-isolation tests before enabling saved profiles.
- Retro-engineering: original gates above remain unmet; no false promotion.
- Learned retrieval/reranking: add only after recall/error evaluation beats current ID+lexical baseline.
- Lower-cost models: paired multi-task evaluation and observed token/correction cost needed. Reasoning
  recommendation is implemented; automatic host model switching is not.
- Full intake automation: extraction adapters/OCR and semantic reading coverage remain host/model work;
  metadata and validation do not prove a page has been understood.

## Compléments du passage Claude

 Retro-engineering mode
Implement the documented reverse workflow in `references/modes.md`.

Required before production routing:
- inferred-template schema;
- visual/layout feature extraction contract;
- vision-first document inspection pipeline;
- OCR fallback adapter;
- neutral holdout exemplar generation;
- template similarity / regression checks;
- at least two human-reviewed reverse-engineering cases;
- lifecycle promotion from `todo` to `candidate`.

The first target use case should reverse-engineer a supplied professional note with:
- mixed prose and comparison tables;
- at least one diagram;
- repeated visual hierarchy;
- side-story/callout equivalent;
- enough semantic structure to infer transition logic.

### Mise à jour post-refonte 4 couches (2026-09-11)

L'implémentation de retro-engineering doit produire un candidat qui se décline sur les 4 couches de [references/layered-architecture.md](references/layered-architecture.md), pas seulement un scaffold de contenu :
- Couche 1 (Template) : objectif, longueur, densité observés — inférés par mesure directe du document fourni.
- Couche 2 (Storytelling) : détection du/des framework(s) narratifs déjà en jeu dans le document source, par comparaison au registre [references/narrative-frameworks.md](references/narrative-frameworks.md) — si aucun framework connu ne correspond, ouvrir une proposition d'extension du registre plutôt que de forcer un mauvais mapping.
- Couche 3 (Scaffold) : extraction de la typologie de nodes dominante (voir table de généralisation dans layered-architecture.md) — un document business reverse-engineered n'a pas de raison d'être purement causal.
- Couche 4 (Rédaction/format) : extraction du contrat de vocabulaire et de mise en page observé (technique vs non-technique, langue, en-tête/bas de page).

Runtime : cette mode reste TODO/non-production. Toute implémentation future doit déclarer `execution_mode: cowork` et `runtime_mode: run_lourd` (voir references/execution-modes.md et references/runtime-modes.md) car l'inspection visuelle + OCR fallback nécessite un accès fichiers garanti, incompatible avec `execution_mode: chat`.

## Issues GitHub

Aucune issue ouverte au 2026-09-11 (`gh`/API GitHub interrogée : `achard-arnaud/skills-notes-and-storytelling` a 0 issue ouverte). Le seul backlog actif restait ce TODO.md ; il est désormais aligné sur l'architecture à 4 couches ci-dessus.
