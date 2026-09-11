# Generation modes

The mode controls **how the workflow enters and what it must preserve**. The template controls the output shape. Modes and templates are independent axes.

## 1. From scratch

Use when no trusted canonical document exists.

### Entry contract
- decision question;
- target reader;
- scope/cutoff;
- requested template or routing permission;
- source restrictions, if any.

### Workflow
```text
decision
→ research plan
→ source ledger
→ atomic fragments
→ claims graph light
→ rerank
→ scaffold
→ fragment-grounded fill
→ side stories
→ sourcing
→ layout
→ DOCX QA
```

### Business strengthening harvested from the historical project
The historical project builds arc-first: evidence → typed claims → graph → composition. The business adaptation keeps the same separation and replaces chronological arcs with a **decision spine**:
- account/product/market evidence first;
- typed claims second;
- causal/fit links third;
- side stories only after the core decision logic stabilizes;
- visual composition never upgrades evidence.

### Stop condition
The document is self-contained, source-complete for material claims and passes its template fixture.

---

## 2. Iterative

Use when a prior canonical note already exists and the requested work is a delta.

### Entry contract
Resolve:
- canonical source document/version;
- accepted content/evidence;
- accepted template/version;
- requested functional delta;
- requested visual delta;
- protected sections;
- **form-global changes** that intentionally reopen a whole section/span.

### Workflow
```text
canonical baseline
→ delta intake
→ impacted claims/fragments
→ targeted research
→ claims graph delta
→ rerank impacted scope
→ scaffold delta
→ update content
→ re-evaluate side stories
→ full-document regression QA
```

### Preservation rule
Material outside the review scope is preserved. A form-global rule such as "prefer direct affirmative language across the note" expands the review scope by contract, while factual approval remains anchored to the existing evidence.

### Regression checks
- no accepted claim silently disappears;
- no source lineage is weakened;
- side stories retain anchors/return points;
- page geometry and table/diagram readability remain valid;
- template/fixture versions remain compatible.

### 2bis. Iterative — zoom ciblé par ID

Sous-mode de `ITERATIVE` : au lieu de résoudre toute la baseline, le runtime **zoome** sur un sous-ensemble explicite de claim IDs et/ou fragment IDs déjà produits, sans relire l'intégralité du document ou du registre.

Entry contract additionnel :
- liste des `claim_id`/`fragment_id`/`side_story_id` ciblés;
- profondeur de voisinage autorisée dans le claims graph (défaut : 1 — voisins directs uniquement, voir retrieval-and-reranking.md);
- confirmation que le périmètre hors zoom reste inchangé.

Le zoom reste éligible à `run_léger` (voir runtime-modes.md) tant que le périmètre est petit et local ; il repasse en `run_lourd` si l'approfondissement touche une part large du document ou déclenche un intake documentaire nouveau (règle impérative de runtime-modes.md).

---

## 3. Feedback / dreaming

Use after delivery, human review or repeated QA repairs to improve the system.

### Entry contract
- delivered artifact and template version;
- explicit human feedback;
- QA defects;
- manual corrections;
- observed repeated patterns.

### Workflow
```text
feedback + QA deltas
→ classify case-specific vs reusable
→ propose contract/template/mode change
→ choose semver bump
→ update linked fixture
→ regression run
→ branch / PR
→ human review
→ validate/promote or reject
```

### Human governance
The system may propose, branch, test and open a PR. It never autonomously promotes a candidate template or mode.

---

## 4. Retro-engineering — TODO

Status: **documented design only; production routing disabled**. It must not be selected for a delivery run.

Its future purpose is to infer a reusable, content-neutral template from a supplied document: visual inspection first, native extraction second, OCR only for image-only material. The output would be a candidate scaffold and holdout fixture, always subject to human review.

Before lifecycle can move from `todo` to `candidate`, the repository needs an inferred-template schema, a visual-feature contract, regression scoring and at least two human-reviewed cases. The detailed implementation design belongs in an issue or ADR once work is funded.
