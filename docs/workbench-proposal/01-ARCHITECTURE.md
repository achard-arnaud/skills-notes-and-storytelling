# Workbench — architecture cible / contrat de frontières

**Proposition de design** (non exécutée). Input : entreprise OU produit, éventuellement les deux avec rôles explicites (account truth vs product truth), contexte d'étude et cutoff. Output : Word/PDF/HTML/Markdown **après** composition, gating et QA.

## Pipeline conceptuel

```mermaid
flowchart LR
 UI[React Workbench] --> API[Local API / adapter]
 API --> ORCH[Run Manager + stage gates]
 ORCH --> R[Research planner Search/DeepSearch]
 R --> E[(Obsidian vault: evidence MD)]
 E --> G[(graph-light projection + provenance)]
 G --> C[A2 Coach: selection + depth plan]
 C --> D[Skill/Template overlay + draft]
 D --> Q[Evidence & rendering QA]
 Q --> O[Word PDF HTML MD]
 ORCH --> J[GitHub App adapter: branch PR Actions]
 ORCH --> L[Loopback proposals / HITL]
 ```

### Authority table (un seul writer canonique)

| Objet | Autorité | Projection / synchronisation |
|---|---|---|
| Template, skill, schema, code | Repo Git `skills-notes-and-storytelling` | manifest catalog DTO vers React |
| Recherche et claims locaux par sujet | Vault Obsidian (Markdown YAML + IDs sources/claims) | Graph-light index produit de manière déterministe, reconstruction + hash |
| Captures brutes autorisées (HTML/PDF/CSV) | Storage PC hors Git, référencé par ID/URI et SHA octets | Obsidian ne stocke que locator/metadata, sauf capture admise par politique |
| État run, idempotency journal, task lease | SQLite local (WAL/transactions) | UI status/events; snapshots JSON exportables |
| Editorial overlay & décisions HITL | Dossier du run sur PC, version/hash ; lien dans SQLite | Artefact GitHub éventuellement publié après revue |
| Sorties documentaires | Dossier run local + manifeste de build | branche Git / GitHub artifact optionnel, aucun push implicite |
| Issue/PR/CI état | GitHub comme autorité distante | cache local horodaté, réconciliation au redémarrage |

## Workflow borné (orchestration plutôt qu'agent monolithique)

```
CREATED
→ INTAKE_VERIFIED
→ PRIOR_WORK_CHECKED [REUSE | REFRESH | NEW]
→ RESEARCH_PLANNED [SEARCH | DEEPSEARCH, HITL si coût/sources sensibles]
→ SOURCES_CAPTURED
→ CLAIMS_VALIDATED (fragments, provenance, contradictions)
→ COACH_PLAN_READY (thesis, dimension, ToC, stars, selected claims)
→ COACH_APPROVED (HITL pour plan matériel)
→ DRAFTED
→ COUNTER_PERSPECTIVE_REVIEWED
→ CONTENT_FROZEN (content hash + evidence snapshot)
→ EXPORTS_BUILT (per format et profil)
→ QA_REVIEWED
→ DELIVERED
→ LOOPBACK_RECORDED
```

Transitions persistées avec `run_id/stage/attempt/entry_hash/exit_hash/actor/status/errors/idempotency_key`. Impossible de fermer une étape sans artefact + gate. `EXPORTS_BUILT` ≠ qualité ni livraison, `DELIVERED` ≠ publication GitHub et non plus diffusion externe. LLM non orchestrateur d'autorité : seul le run manager vérifie transitions/hashes.

### Graphe / local Obsidian

Modèle de note de preuve (`vault/BusinessNotes/entities/<entity_id>/claims/<claim_id>.md`):
- frontmatter : `id, entity_id, subject_kind, epistemic_status, observed_at, published_at, valid_until, source_ids, evidence_locator, raw_capture_sha256, version, sensitivity, owner`.
- corps : assertion atomique, contre-preuves, citations source et questions.
- autres notes : `sources/`, `questions/`, `runs/` indexables en liens Wikilinks; aucun claim en double sur `product_truth` et `account_truth`.
- graph-light reconstruit du vault; pas de correction du JSON généré. Édition Obsidian humaine → diff/validation/lock avant index. Contradictions conservées, jamais `null → 0`.
- Index `entity_aliases` + checksum snapshot, lookup by subject/cutoff; `reuse` seulement si fraîcheur et scope suffisants. Si stale/changed source, invalider descendants et relancer **questions touchées**, pas le pipeline complet.

### Anti-compaction / context engineering

Un checkpoint **écrit sur disque à chaque gate** contient `run_id, stage, entity, cutoff, template+version+sha, overlay+sha, sources sha, 12 claims décisifs + leurs réf/contre-preuves, top 3 unknowns, hard gates, decisions/actor, outputs refs+hash, next_action, stop_condition, token_budget`.
12 claims = budget d'entrée indicatif Hivest, extensible lorsque des contradictions sont matérielles ; ne jamais tronquer silencieusement. Sur une nouvelle session LLM, relire seulement contrat stage, checkpoint, paquets fact IDs et preuves ciblées. Aucune vérité ne dépend de la rétention conversationnelle. La compaction ne vaut jamais approbation; après reprise, valider hashes d'entrée.

### Coach editorial = surcouche, pas modification de la skill

`RunOverlay` :
- `template_ref` version+sha et mode `from-scratch|iterative`;
- `analysis_dimension` primary (business/product/technical), dimensions secondaires optionnelles;
- `subject_ref` and `research_mode`;
- `sections[].section_id, rank, stars=0..3, rationale, locked, prerequisites, target_words?`;
- `thesis, audience, decision_question, counter_perspective, must_include_claim_ids, must_not_claim, reviewer_decisions`;
- `outputs_requested, document_languages, optional_hooks`.
Validation dynamique contre **catalogue versionné** ; un champ étoile/ordre ne crée aucune preuve ni changement canonique du template. Le plan A2 reçoit questions/candidats du graphe et retourne une sélection sourcée. Un éditeur ne peut pas enlever la section sources, risques ou verdict si elle est obligatoire.

### Budget / recherche / loopback

`search` : interrogations ciblées sur registres et sources premières, 1 passe de corroboration, stop quand réponse suffisante. `deepsearch` : plan de questions, recherche multi-classe, contradicteurs, branchée par sous-questions; budget max tokens / max sources / max durée, checkpoint par batch. Dépassement => pause / demande humaine, pas poursuite invisible.
Loopback L reçoit uniquement deltas, erreurs et choix; propose jusqu'à 3 actions et 1 patch candidat, sans promouvoir automatiquement une règle, un claim ou une nouvelle skill. Contrôle régression avant merge.
