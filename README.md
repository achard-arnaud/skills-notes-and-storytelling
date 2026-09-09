# Decision Notes & Storytelling

Reusable skill for evidence-grounded business notes, architecture notes, one-pagers, two-pagers, benchmarks and buy-side gap analyses.

## Canonical skill
- **Skill:** `decision-notes-and-storytelling`
- **Entry point:** [SKILL.md](SKILL.md)
- **Template enum:** [src/template_types.py](src/template_types.py)
- **Workflow:** [references/workflow.md](references/workflow.md)
- **Visual contract:** [references/style-contract.md](references/style-contract.md)
- **Side-story retrodocumentation:** [references/side-stories-retro.md](references/side-stories-retro.md)

## Core pipeline
```text
research
→ atomic fragments
→ claims graph light
→ reranking
→ scaffold
→ fragment-grounded drafting
→ side-story insertion
→ layout
→ fact-checking & sourcing
→ DOCX render QA
→ next-step nudging
→ human-reviewed dreaming update
```

Every new `.doc` / `.docx` note must use this skill together with the platform DOCX creation/editing skill. New document templates remain candidates until human review promotes them into the template catalog.
