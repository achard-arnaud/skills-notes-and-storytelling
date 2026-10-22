# Business Notes Workbench — change-request register & tranche de livraison

**État : backlog de propositions.** Le dépôt contient actuellement une skill documentaire solide, des templates et la validation de contrats, **pas** la plateforme Workbench. Ne pas considérer l'ouverture d'une issue ou d'une PR de spécification comme livraison de runtime/UI.

## Epics / ordre imposé par la valeur et les risques

| ID | Priorité | Lot | Source à emprunter | Exit/anti-test |
|---|---|---|---|---|
| BN-00 | P0 | Alignement catalogue/README/routes & vérification des versions, ownership des sources de vérité | Hivest README/quickstart + Candidatures read-manifest | Un agent bootstrap sans scan repo complet; as-is / cible distingués |
| BN-01 | P0 | Registry templates: tags dimensions, audience, jobs, ToC stable, required/deps/allowed depth | Candidatures zone contract | Tous les 9 templates annotés **sans feindre** un mode supporté; validator anti-reorder impossible |
| BN-02 | P0 | Overlay Coach / section prioritisation & schema, diff du template | Candidatures A2 editorial briefs | Overlay ne modifie jamais skill; stars 0–3 sans inventer de claims; changes reviewables |
| BN-03 | P0 | Evidence store PC Obsidian, recherches antérieures, GraphLight, source snapshots, permissions | Hivest wiki/evidence, graph impact | REUSE/REFRESH/NEW stable; conflits/invalidations ciblés, raw Git leak 0 |
| BN-04 | P0 | Stage-run manager checkpoints, hash+lease+resume, budget anti-compaction | Hivest context/resume + Candidatures V3 | crash/reprise sans doublon, unknowns préservés, >budget refuse sans couper preuve |
| BN-05 | P1 | React catalogue / entreprise-produit / ToC drag-keys / stars / progress | Candidatures Coach/template semantics | V0 local mock, 3 dims, 9 templates, accessibilité, no backend claims |
| BN-06 | P1 | Recherche planifiée / Search / Deepsearch sourcés, coût, réutilisation | Hivest Extract/targeted graph | Déduplication, freshness, contradictions, human gate budget |
| BN-07 | P1 | GitHub branches, Actions & webhooks sécurisé, pr/commit receipt | Candidatures publishing, Hivest Actions | HMAC/replay/permissions, branches dédiées, CI/merge human |
| BN-08 | P1 | Export Word PDF HTML MD, QA visuelle & état par format | Hivest renderer + Candidatures A3/A4 | Each format real file, check, hash and preview, failures disable download |
| BN-09 | P1 | Loopback trace / diff / CI tests de preuves et sémantique | Hivest Loopback, Candidatures L | ≤3 deltas utiles, gate HITL, regression tests, no auto KB mutation |
| BN-10 | P2 | Packaging multi-workspace/cloud optionnel/observability & release security | GitHub App local-first patterns | Only after validated local path, no public webhook necessary for MVP |

## Tranches verticales qui évitent le programme de 10+ JH d'emblée

- **V0 documentation + React catalogue** : read-only templates from manifest, filtre text/tags, ToC avec moves et étoiles, overlay JSON en mémoire ou fichier local. **Aucune recherche, aucun Word/PDF** prétendu.
- **V1 local** : Run SQLite, local Obsidian read/write consent, planner search + evidence capture, graph-light projection, deux templates pilotes (`two-pager`, `architecture-note`), Markdown et HTML avec QA.
- **V2 publication** : DOCX et PDF réels, preview + QA, GitHub App branch/PR, Actions et reçus. Webhook cloud optional **last**.
- **V3 couverture** : neuf templates, mode iterative/feedback-dreaming, multi-subject bridge, tests NRT, éventuel cloud multi-workspace après ROI mesuré.

### Tests de décision / métriques

Mesurer temps humain, temps exécution, tokens réellement observables, nombre de sources relues, nombre de claims cités, couverture des exigences, régressions d'attribution, conflit/dupliqué, reprise, QA pages. Ne pas substituer un score sans dénominateur.
No-go si le prototype nécessite GitHub webhooks publics ou une migration Obsidian complète avant de rendre un Two-Pager. Checkpoint stop après deux réparations locales sur le même défaut; produire issue, cause et replanification.

## Garde-fous de gouvernance

Ce plan doit rester sous PR contre `dev`, CI et approbation humaine. Template lifecycle `candidate → validated` seulement après fixture; ne jamais reclasser les neuf templates à `validated` sans test. Les issues opérationnelles sont la source du backlog; ce document pointe les dépendances, sans créer un second statut de vérité.
