---
name: decision-notes-and-storytelling
description: Create, revise, or industrialize evidence-grounded .doc/.docx business notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side gap analyses, sell-side diagnostic/recommendation notes, and ICP opportunity notes. Own the research-to-claims-to-storytelling workflow, generation mode, template selection, side-story routing, sourcing gates, next-step nudging, and human-reviewed template learning. Always pair with the runtime DOCX creation/editing skill for rendering and visual QA.
---

# Decision Notes & Storytelling

## Scope

This skill is the governed document OS for decision notes. It owns **content architecture, evidence lineage, narrative composition, template contracts and learning loops**. The runtime DOCX skill owns **Word generation, rendering and file-level QA**.

Use this skill whenever the requested output is a `.doc` or `.docx` note, brief, comparison, architecture memo, one-pager, two-pager, benchmark, buy-side analysis, sell-side diagnostic or ICP opportunity note.

## Variables de run à déclarer avant toute exécution

Trois axes indépendants, à déclarer explicitement en tête de run :

1. `execution_mode` : `chat` | `cowork` — environnement d'hébergement, contraint la consommation de contexte. Lire [references/execution-modes.md](references/execution-modes.md).
2. `runtime_mode` : `debug` | `run_lourd` | `run_léger` — intensité d'exécution du pipeline pour ce run. **Règle impérative : un intake documentaire fourni par l'utilisateur force `run_lourd`.** Lire [references/runtime-modes.md](references/runtime-modes.md).
3. `generation_mode` (`GenerationMode`, ci-dessous) : quelle portion du pipeline s'exécute et ce qui doit être préservé.

L'effort de raisonnement par étape du pipeline est calibré séparément, en config plutôt qu'en dur — voir [references/reasoning-effort.md](references/reasoning-effort.md) et `config/reasoning-effort.json`. Aucun nom de modèle n'apparaît jamais dans ces fichiers.

## Generation mode

Select one mode from `GenerationMode` before selecting the output template. Read [references/modes.md](references/modes.md).

- `FROM_SCRATCH` — no trusted canonical draft exists; execute the complete evidence → claims → scaffold → draft pipeline.
- `ITERATIVE` — a canonical prior output exists; establish the accepted baseline, compute the delta, update only the required evidence/content/layout scope, then regression-check preserved material. Includes the **zoom** sub-mode: target specific claim/fragment/side-story IDs without rereading the full baseline (see [references/modes.md](references/modes.md) §2bis).
- `FEEDBACK_DREAMING` — post-run improvement loop; convert repeated feedback and QA defects into candidate changes to contracts/templates with explicit human promotion.
- `RETRO_ENGINEERING` — **TODO / non-production**. Reverse-engineer a supplied document into a candidate template using visual inspection first and OCR only as fallback. The planned workflow is documented but must not be treated as implemented.

## Template enum

Select exactly one value from `OutputTemplateType` in `src/template_types.py`:

- `ARCHITECTURE_NOTE`
- `ONE_PAGER`
- `TWO_PAGER`
- `BENCHMARKING`
- `BUY_SIDE_GAP_ANALYSIS`
- `DIAGNOSTIC_RECO_SELL_SIDE`
- `OPPORTUNITY_NOTE_ICP`

Every template is versioned in `templates/manifest.json` together with its QA fixture and compatible workflow version. Read [references/versioning-and-lifecycle.md](references/versioning-and-lifecycle.md).

## Les 4 couches découplées

Chaque template se décline en 4 couches indépendantes : Template (objectif/longueur/détail/collecte/nodes), Storytelling (frameworks narratifs), Scaffold/claims/fragments (retrieval/reranking/typologie de nodes/side stories), Rédaction & format (ton/langue/vocabulaire/mise en page). Lire [references/layered-architecture.md](references/layered-architecture.md) pour la déclinaison par template, et [references/narrative-frameworks.md](references/narrative-frameworks.md) pour le registre des méthodes narratives (Pyramid Principle, Action Titles, MECE, Ghost Deck first, Signal-to-noise).

## Retrieval, reranking et distinction claims / fragments

Les claims (scaffold logique) et les fragments (remplissage business) sont deux registres distincts, chacun avec ses propres règles de retrieval, reranking et déduplication. Lire [references/retrieval-and-reranking.md](references/retrieval-and-reranking.md), qui couvre aussi la règle d'exclusion/relégation en annexe des side stories.

## Canonical workflow

Follow [references/workflow.md](references/workflow.md). Stage boundaries remain explicit.

1. **Research** — collect source evidence; separate account/company reality, product truth and market alternatives.
2. **Fragments** — convert evidence into atomic, source-addressable fragments.
3. **Claims graph light** — create claim nodes and typed edges without building a heavy ontology.
4. **Rerank** — prioritize decision relevance, evidence strength, explanatory value, novelty and audience fit.
5. **Scaffold** — build a section skeleton from ranked claims before drafting.
6. **Fill** — draft only from fragments attached to claims; preserve evidence status.
7. **Side stories** — insert bounded detours after the core decision spine is coherent.
8. **Layout** — map content to the selected template; prefer bullets and comparison tables.
9. **Fact-check & source** — verify every material claim and source line.
10. **DOCX QA** — invoke the runtime DOCX skill; render every page; inspect and iterate.
11. **Next-step nudging** — expose bounded follow-ups, open questions and highest-value deeper dives.
12. **Feedback/dreaming** — when the run reveals a reusable pattern, create a candidate change linked to a regression fixture; human review decides promotion.

## Evidence and prose rules

- Lead with the decision, result or central thesis.
- Prefer direct affirmative formulations.
- Use contrast only when the contrast carries analytical value.
- Prefer bullets for enumerations of 3+ items.
- Prefer tables for structured comparisons.
- Label `fact | inference | hypothesis | recommendation | unknown`.
- Side stories never create new proof.
- Preserve source lineage from fragment → claim → section → side story.
- Apply hard evidence gates before any scoring or narrative ranking.
- Keep seller recommendations separate from buyer reality until the explicit fit stage.

## Visual rules

Apply [references/style-contract.md](references/style-contract.md).

Key gates:
- body text target 10.5–11 pt; hard minimum 9 pt;
- no clipping, overlap or out-of-bounds content;
- tables use column widths proportional to semantic density;
- comparisons default to tables;
- Mermaid source remains canonical and rendered diagrams are embedded as images;
- if fitting a Mermaid would reduce either dimension by more than **30%**, transpose the same semantic graph and rerender;
- every final DOCX passes render → page-by-page inspection → correction → rerender.

## Side stories

Use [references/side-stories-retro.md](references/side-stories-retro.md). Preferred business-note kinds:

- `dezoom` — broader operating-model, portfolio or market implication;
- `method` — method, evidence or scoring caveat;
- `false_lead` — tempting analogy rejected with an explicit break point;
- `comparator` — bounded comparison on one decision criterion;
- `analytical_focus` — deeper mechanism, economics or conjecture;
- `callback` — return to a prior decision thread.

Every side story has a stable ID, source claim IDs, purpose, insertion anchor and return-to anchor.

## Specialized templates

### BUY_SIDE_GAP_ANALYSIS
Use when the reader evaluates whether to adopt, replace, complement or partner with a product/vendor. Start from the buyer baseline, hard gates and migration reality before feature richness.

### DIAGNOSTIC_RECO_SELL_SIDE
Use when advising a vendor/founder on how to package, position, sell and expand an offer. Diagnose market narrative, ICP, entry wedge, proof mechanics, packaging, pricing, competitive threats and sales motion before issuing recommendations.

### OPPORTUNITY_NOTE_ICP
Use when deciding whether a concrete target account, partner or internal platform is a plausible opportunity for an offer. Keep target reality and product truth separate, apply hard gates, map capability gaps to product outcomes, identify sponsor/terrain/veto hypotheses and end with a reversible validation step.

## Feedback / dreaming

Read [references/dreaming-self-healing.md](references/dreaming-self-healing.md). A reusable change requires:
- at least one real output;
- QA findings or explicit user feedback;
- separation of case-specific vs reusable deltas;
- a candidate contract/template/mode patch;
- a version-linked regression fixture;
- human approval before promotion.

Never silently mutate the canonical template after a single run.
