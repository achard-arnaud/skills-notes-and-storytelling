# Decision Notes & Storytelling

Revue documentaire : **22 octobre 2026**. Catalogue réconcilié avec `templates/manifest.json` (9 templates, workflow 1.3.1). La skill et ses contrats existent ; le Workbench agentique est une cible, pas un runtime livré.

Reusable skill for evidence-grounded decision notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side analyses, sell-side diagnostics and ICP opportunity notes.

## Canonical skill
- **Skill:** `decision-notes-and-storytelling`
- **Entry point:** [SKILL.md](SKILL.md)
- **Template enum + generation modes:** [src/template_types.py](src/template_types.py)
- **Workflow:** [references/workflow.md](references/workflow.md)
- **Modes:** [references/modes.md](references/modes.md)
- **Versioning:** [references/versioning-and-lifecycle.md](references/versioning-and-lifecycle.md)
- **Visual contract:** [references/style-contract.md](references/style-contract.md)
- **Side-story retrodocumentation:** [references/side-stories-retro.md](references/side-stories-retro.md)

## Generation modes

| Mode | Status | Purpose |
|---|---|---|
| `from-scratch` | validated | Full evidence → claims → scaffold → document run |
| `iterative` | validated | Delta-first update against a canonical baseline + full regression |
| `feedback-dreaming` | validated | Convert human feedback / QA deltas into candidate system upgrades |
| `retro-engineering` | **TODO** | Reverse-infer a template from a supplied document; vision-first, OCR fallback |

## Choose the note format

| Template | Pages | Orientation | Statut du manifeste |
|---|---:|---|---|
| `architecture-note` | 5–10 | portrait | candidate |
| `one-pager` | 1–1 | adaptive | validated |
| `two-pager` | 2–2 | landscape | validated |
| `benchmarking` | 2–6 | landscape | candidate |
| `buy-side-gap-analysis` | 4–8 | adaptive | candidate |
| `diagnostic-reco-sellside` | 5–9 | portrait | validated |
| `opportunity-note-icp` | 4–8 | portrait | validated |
| `integration-note` | 3–7 | adaptive | candidate |
| `strategic-market-note` | 5–7 | portrait | candidate |

Read [the detailed template catalog](references/template-catalog.md) only after choosing the format.

## Core pipeline

```text
mode selection
→ research
→ atomic fragments
→ claims graph light
→ reranking
→ scaffold
→ fragment-grounded drafting
→ side-story insertion
→ fact-checking & sourcing
→ layout
→ DOCX render QA
→ next-step nudging
→ feedback/dreaming candidate
```

## Cross-version QA

Each template declares:
- semantic version;
- lifecycle;
- compatible modes;
- QA fixture;
- fixture version;
- workflow version.

CI rejects template/fixture major mismatches, stale workflow fixtures, enum/manifest drift, missing fixtures and accidental activation of the `retro-engineering` TODO.

## Git workflow

```text
feature branch
→ PR to dev
→ CI GREEN
→ merge into dev
→ PR dev → main
→ CI GREEN
→ promotion to main
→ fast-forward dev to main
```

Every new `.doc` / `.docx` decision note uses this skill together with the runtime DOCX creation/editing skill and the final render-and-inspect gate. Their boundary is versioned in [the DOCX runtime interface contract](contracts/docx-runtime-interface.schema.json): a layout-ready output specification goes in; a visual QA report comes back.

## Workbench — cadrage courant, sans développement autorisé

[Branche de design du 22 octobre](https://github.com/achard-arnaud/skills-notes-and-storytelling/tree/design/business-notes-workbench-20261022) · [PR #33 vers dev](https://github.com/achard-arnaud/skills-notes-and-storytelling/pull/33).

- [Spécification consolidée Storyteller](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/design/business-notes-workbench-20261022/docs/workbench-proposal/05-STORYTELLER-CONSOLIDATED-SPEC.md) : stepper, Analyste, KB/alerte/contexte, one-shot/deep-search, ToC, blind-spot, side stories et multi-container, relecture, Canvas et formats.
- [Prompt système Superpowers](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/design/business-notes-workbench-20261022/docs/workbench-proposal/06-SUPERPOWERS-SYSTEM-PROMPT.md) : personnae, entrées/sorties, boucles, revues, checkpoints et coûts.
- [Lots, plan nocturne et traçabilité](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/design/business-notes-workbench-20261022/docs/workbench-proposal/07-NIGHT-LOOP-AND-TRACEABILITY.md).
- [Epic et backlog #21](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/21) : BN-00..10 (#22..32) et BN-11..18 (#34..41), plus #19 tests et #20 contrats.

La cible utilise **une étoile binaire**, « partie d'importance stratégique », remplaçant la proposition 0–3. Le prototype et le schéma v0 préexistants ne sont pas modifiés par cette revue. Coach devient **Analyste**. Open Canvas est une intégration à instruire (#37) avec adaptateur remplaçable ; upstream archivé.

Revue workload 22h Europe/Paris et fenêtres proposées 03h/04h/05h : exécution future seulement après GO_DEV explicite, versionné et borné. Aucun runner ni webhook de développement activé. Aucun merge ou export Workbench réel revendiqué. La revue planifiée à 22h, si créée, prépare seulement une proposition.
