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

Status: **documented design only; production routing disabled**.

Purpose: infer a reusable document template from a supplied document when no explicit template contract exists.

### Planned reverse workflow
```text
supplied document
→ visual pass page by page
→ OCR only if visual/text extraction is insufficient
→ page geometry + style inventory
→ infer scaffold
→ infer section fill criteria
→ infer language/tone rules
→ infer comparison/table/diagram grammar
→ analyze content objectives
→ meta-prompt each section
→ infer logical transitions
→ reconstruct template contract
→ build neutral holdout exemplar
→ compare against source
→ human validation
```

### Planned analysis layers
1. **Vision/layout**
   - page size/orientation/margins;
   - grid and whitespace;
   - typography hierarchy;
   - tables, figures, captions, callouts;
   - recurring visual components.
2. **Scaffold deduction**
   - section order;
   - mandatory vs optional blocks;
   - density budget;
   - page-break behavior.
3. **Fill contract deduction**
   - evidence type expected per block;
   - prose vs bullets vs table;
   - claim count and source coverage;
   - side-story opportunities.
4. **Content objective deduction**
   - decision being served;
   - intended reader;
   - persuasion/information balance;
   - implicit acceptance criteria.
5. **Meta-prompting**
   - derive a bounded prompt for each block;
   - derive transitions and callbacks;
   - identify what information is necessary before rendering.
6. **Validation**
   - create a content-neutral fixture;
   - render against inferred geometry;
   - compare visually;
   - require human promotion.

### OCR policy
Vision and native text extraction are preferred. OCR is a last-resort fallback for unavailable or image-only text and must not silently override visible structure.

### TODO gate
Before this mode becomes production-ready:
- schema for inferred template contract;
- visual feature extraction contract;
- holdout fixture;
- regression scoring;
- minimum two human-reviewed reverse-engineering cases;
- explicit lifecycle transition from `todo` to `candidate`.
