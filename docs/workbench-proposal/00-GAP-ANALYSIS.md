# Business Notes Workbench — gap analysis croisée (2026-10-22)

Statut : **PROPOSITION**, pas audit d'exécution end-to-end. Référence cible : `skills-notes-and-storytelling` (= Decision Notes & Storytelling). Comparateurs : `Hivest-ptf-analysis` et `Candidatures-nice` à leurs branches principales observées. Ne pas copier aveuglément leurs abstractions, scopes ou données privées.

## Bilan as-is vérifié

| Domaine | Notes & Storytelling actuel | Bonne pratique sourcée | Gap / cible |
|---|---|---|---|
| Routeur | `SKILL.md`, `references/workflow.md` : 15 étapes normatives, sélection mode + template + dimension | Candidatures `workflow/read-manifest.json` + `workflow/cv-v3.md` | Pas d'orchestrateur exécutable par état, checkpoint, propriétaire de sortie, retry, reprise ciblée |
| Mémoire de preuve | `contracts/claims-graph-light.schema.json` + `references/bridges-integration-and-run-memory.md` | Hivest `scripts/research_graph.py`, `contracts/run-context.schema.json` | Contrat source→fragment→claim prescrit ; pas de stockage local transactionnel, sélection/revalidation par entity/cutoff, invalidation des descendants |
| Anti-compaction | Brief de mémoire portable prescrit dans la référence ; pas de manifeste de run effectif | Hivest `docs/agent/context-and-resume.md` : top 12 claims, 3 inconnues et hashes, reprise par gate | Pas de checkpoint signé, garde des questions irrésolues, budget et hash vérifiés en runtime |
| Décision / HITL | `SKILL.md`: contre-perspective, tier dreaming, promotion humaine | Hivest `docs/agent/gates.md`, Candidatures A1–A4 | Phases et "GO_DRAFT" sans moteur bloquant, pas de journal des autorisations |
| Templates | 9 entrées `templates/manifest.json` ; dims "technical/product/business" natives au système | Candidatures `templates/francois-cv-template/zone-contract.json` | Plusieurs templates sans supported_dimensions déclaré ; pas de tags catalogue, ToC structuré, dépendances, rubriques verrouillées, star-depth et ordre utilisateur |
| Export | `contracts/output-spec.schema.json`, DOCX runtime interface, QA contract | Hivest renderer & `renderers/three_pager_exec/qa.py` ; Candidatures A3 QA | Pas de service export Word/PDF/HTML/MD ni validation unifiée (les skills fournissent instructions, pas tous les binaires) |
| GitHub workflow | README : feature→dev→main ; CI `qa.yml` valide contrats | Candidatures branches par case, issues, publication & hooks ; Hivest GitHub Actions tests | Pas de branch lifecycle par recherche, locks, merge policy, dispatch idempotent, action receipt, webhooks |
| UI | Pas de React/frontend/API dans arbre actuel | Candidatures saisie/pipeline ; Hivest gestion programme | Manque catalogue filtres, source company/product, ToC reorder, stars, run monitoring, preview/export |
| Stockage local | Aucune implémentation Obsidian dans le dépôt | Hivest source captures hors Git, wiki commun séparé comptes | Nécessite bridge local PC : vault Markdown canonique, graph-light projection, raw archive autorisée hors Git, one writer |
| Coûts et NRT | CI valide contrats ; modes validés vs TODO | Candidatures tests par impact/loopback, Hivest negative fixtures | Pas de budgets tokens mesurés, tests intégration E2E, faux claims, rerank sans preuve, compatibilité de versions |
| Sécurité | Politique de sourcing / privacy documentaire | Hivest frontière raw/Git, Candidatures permissions/publication | Aucun modèle de sécurité web/PC, GitHub App/webhook signing, secret isolation, export sanitisation |

## Écart de documentation reproductible (constaté sur `main`)

- Le registre de référence `templates/manifest.json` déclare **9** templates ; `src/template_types.py` contient effectivement neuf valeurs, dont `strategic-market-note`.
- La section `SKILL.md > Template enum` n'énumère que **8** templates : `STRATEGIC_MARKET_NOTE` en est absent, bien que le système le connaisse et que le registre le déclare candidat.
- Le tableau `README.md > Choose the note format` ne couvre que **7** entrées : `integration-note` et `strategic-market-note` absents; il qualifie `architecture-note` de **validated**, mais son état actuel dans le manifest est **candidate**.
- Le script `scripts/validate_contracts.py` vérifie l'égalité enum/manifest et des fixtures, pas la fidélité de ces deux listes rédigées en prose. D'où CI verte possible malgré ce drift documentaire.
- Correctif BN-00 : générer ou valider les tables du README/skill depuis le manifest, avec test négatif documentaire et ownership unique. **Ne pas** promouvoir l'architecture-note au statut validated par simple correction de README.

## Non-gaps : réutiliser, ne pas réécrire

1. `SKILL.md` : dimensions `business/product/technical`, modes, 15 phases, trois revues et dreaming.
2. `templates/manifest.json` : identité/version/lifecycle/fixtures, template canonique; ne pas générer un deuxième enum divergent.
3. `contracts/claim.schema.json`, `claims-graph-light.schema.json` : source de preuve de la skill; envisager une projection incrémentale et une migration explicite.
4. `references/bridges-integration-and-run-memory.md` : frontières product truth / account truth, bridges et état épistémique.
5. Hivest : emprunter le **modèle** Extract→Transform→Publish, checkpoints, gates, source snapshots, HITL, QA visuelle; ne pas importer ses règles Investment Committee spécifiques.
6. Candidatures : réutiliser patterns A1 intake, A2 Coach & evidence roundtrip, A3 génération, A4 revue, L Loopback; **pas** de dépendance aux CV, personas, règles ATS ou à la KB privée.

## Conséquences de design

- Ne pas migrer un seul octet de preuve brute dans un dépôt Git public.
- Une interface React n'est **pas** une autorité métier : elle compose une `RunOverlay` versionnée et signée avec `template_id+sha`, `toc_override` et `depth_priority`. Le moteur serveur reste propriétaire des gates.
- Les étoiles modulent le **budget d'approfondissement éditorial** et les questions prioritaires, jamais le statut d'une preuve.
- `rerank` n'autorise pas suppression d'un contrôle obligatoire ; contraintes de précédence validées avant RUN.
- Recherche d'existant avant deepsearch : fingerprint entity, aliases, sujet, cutoff, types de sources, provenance, hashes. Reuse/refresh/new explicite.
- Prioriser tests sur falsification, reprise, permission, contamination source-vendeur, non-inflation et preuve de rendu; une CI verte ne certifie pas le sens.
- Produire un POC local-only avant tout GitHub webhook public; GitHub ne peut écrire directement sur un PC sans bridge local autorisé.

## Risques critiques et réduction

R1 **compaction/perte de contexte** : checkpoint de contrat, pas conversations; listes ordonnées de preuves et inconnues liées à SHA, reprise fail-closed.
R2 **injection de prompt des sources** : sources non fiables, extraction hors instructions, citations requises pour claims, approval humaine.
R3 **double vérité Git/Obsidian** : vault MD source de recherche, `graph-light.json` dérivé; SQLite source des *états de run seulement*; Git pour code/templates et publications explicitement approuvées.
R4 **webhook espion/boucle d'écriture** : HMAC, delivery ID unique, journal append-only, séparation des scopes, interdiction de remote-to-vault sans consentement.
R5 **surcoût tokens** : recherche delta, checkpoint et cache ciblé; gate budget et plan de query avant `deepsearch`.
R6 **suite tests massive à chaque action** : matrice impact→tests; CI étendue sur changement contrat ou release, rendu ciblé par template.
R7 **surspécification de produit** : vertical slice catalogue+ToC+run synthetic sans backend réel avant cloud integration.
