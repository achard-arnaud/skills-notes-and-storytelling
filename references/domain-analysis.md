# Domain analysis for S3 cases

Choose the domain by the question it owns. Open its skill and manifest, then read only the references selected for that question. An additional domain can contribute to the same study when the mandate requires it. Give each question one owner and keep the same study ID, proof references and unknowns.

| Domain | Lead question | Entry |
| --- | --- | --- |
| Business | How does the organization operate, create value or bear risk? | [Business analysis](../skills/business-analysis/SKILL.md) |
| Product | What can the offer do, for whom, in which workflow, with what observed usage? | [Product analysis](../skills/product-analysis/SKILL.md) |
| Technical | How does the system work, integrate or fail, and what evidence changes the decision? | [Technical analysis](../skills/technical-analysis/SKILL.md) |
| Pedagogy | What should this learner be able to do, and how will they practice and demonstrate it? | [Learning design](../skills/pedagogical-ai-learning/SKILL.md) |
| Regulatory | Which provisions apply, to whom, when and under what exceptions? | [Regulatory analysis](../skills/regulatory-bootstrap/SKILL.md) |

## RUN

Use [the case process](case-process.md) for a new independent case. Keep the intake, company or learner context, source snapshots, budgets, analyses, checkpoints, draft and QA under the private case directory `data/cases/<id>/`. Pin the published BUILD revision, selected domain manifest, methods and format contract in the run's context or handoff. On this increment the case engine pins its own declared dependencies. Record domain method pins explicitly in the handoff. Existing cases continue on their recorded version and private storage, including legacy report runs.

Use the existing [analysis plan and envelope](../diagnostic-complet/docs/ANALYSIS-CONTRACT-MAPPING.md) for findings. Record a question, applicability, method version, input claim IDs, finding and status, counterevidence, unknowns and condition for revision. Keep analysis independent of the template. Link findings and claims to sections at synthesis and composition using [the writing adapter](../diagnostic-complet/analysis_writing.py). Reusing a result keeps its claim status, dates, source and known limitations. Recheck freshness where the question changes.

Use S3's existing [writing and side-story workflow](../diagnostic-complet/docs/WRITING-WORKFLOWS.md) for a long report. A shorter view uses the same findings with its own scaffold and contract. Follow [editorial and research quality](editorial-and-research-quality.md) in each view. Apply the budget appropriate to the domain and mandate. Inspect the support actually delivered and retain a separate business review.

## BUILD

Version the skill entry, method references, manifest, shared contracts and synthetic regression fixtures from `dev`. Keep case-specific sources, budgets, jargon and results out of these files. A RUN correction follows the case's pinned dependencies and reopens affected work. A recurring or proven defect in the method or engine gets an independently reviewed BUILD ticket with a synthetic reproduction.

The per-domain `manifest.json` inventories methods and references. Paths are repository-relative and validated by the BUILD contract check. A method may point to an existing reference or capability. Method IDs are prefixed by their owning domain. Templates keep their separate contract, catalogue and adapters. Use the existing context validation, impact plan and review ledgers. Add an executable policy or adapter only when an observed workflow needs it.
