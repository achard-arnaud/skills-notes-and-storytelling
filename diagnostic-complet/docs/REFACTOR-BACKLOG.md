# Registre des tickets de refactor — séparation build / run et terminologie

Document public : méthode et état du code uniquement. Aucun contenu de corpus. Chaque ticket a une preuve de clôture mécanique (test) ou un statut humain explicite. Convention : `RF-nn`, règles dans `AGENTS.md` (M1–M11, P5).

## Clôturés dans ce changement (9 novembre 2026)

| ID | Constat initial | Action | Preuve de clôture |
|---|---|---|---|
| RF-01 | `kb.py` embarquait `ENTITY_LEXICON` et `PILLAR_LEXICON` (GreenYellow, VisioSense, PV, onduleur…) | Lexiques déplacés dans `profiles/greenyellow.profile.json` (identiques, version 1.0.0). `kb.py` lit un profil passé en argument, défaut `neutral` | `test_golden_greenyellow_classification_is_unchanged` ; `test_core_code_contains_no_run_vocabulary` |
| RF-02 | `project.py` avait `DEFAULT_NAMESPACE = knowledge/business/greenyellow` | Défaut supprimé. Namespace exigé par argument ou par `projection.namespace` du profil | `test_projection_requires_a_namespace` ; tests `test_project.py` sur `knowledge/business/fixture-run` |
| RF-03 | Trois vocabulaires de statut sans correspondance (claims, `evidence_basis`, `knowledge_status`) | `ontology/terminology.json` unique. `evidence_basis` retirée de l'ontologie (facette jamais produite). Ontologie 0.5.0 | `TerminologyTests` ; `ontology.validate_referential` refuse toute divergence |
| RF-04 | `PRIMARY_KINDS` incluait `primary_vendor` et `primary_corporate` : une auto-déclaration pouvait valider un `verified_fact` | Tier explicite, sinon mapping legacy (`primary_vendor`→T2, `primary_corporate`→T1). Seuls T3 et T4 sont éligibles, plus `qualified: true` | `VerifiedTierRegressionTests` |
| RF-05 | Aucun second profil : la généricité n'était pas prouvée | `profiles/synthetic-logistics.profile.json` (fictif) ; isolation et exclusivité des termes testées | `test_synthetic_profile_is_isolated_from_greenyellow` |

## Ouverts

| ID | Sujet | Statut | Décideur | Note |
|---|---|---|---|---|
| RF-06 | Migrer les index KB sans `profile_id` (produits avant ce changement) vers un profil déclaré | open | coordinateur | Refus explicite aujourd'hui. Le corpus privé n'est pas présent dans ce conteneur |
| RF-07 | Projection Graph1 : passer `--profile` ou `--namespace` explicitement à chaque lot ; ajouter `profile_id` au MANIFEST | open | coordinateur + rédacteur business | Lien avec le lot R2-14 déjà publié : ne rien rejouer sans reçu |
| RF-08 | Entité `microsoft` dans le profil GreenYellow : terme générique, probablement un artefact de l'échantillon initial | open | humain | Retirer ou garder change le graphe dérivé ; décision avant tout nouveau lot |
| RF-09 | 9 faux positifs `directive` dans le corpus (phrases descriptives à l'infinitif, « il faut ») | open, HITL | humain | Corriger l'heuristique de `kb.py` demande une nouvelle version de lexique et un reçu |
| RF-10 | Un `attributed_claim` n'exige pas aujourd'hui de source de tier T1 à T3 | open | — | Règle à ajouter dans `runtime.py` avec fixture de non-régression |
| RF-11 | Installer la skill `reinforce-kb-loopback` en circuit personnel (R2-08) | awaiting_human | humain | Le `.skill` est livré ; l'installation se fait depuis l'environnement personnel |
| RF-12 | Calibrer la cadence HIL (D18) | open, backlog | humain | Plusieurs cycles mesurés requis ; aucun seuil avant `decision_ref` |
| RF-13 | Revue sémantique du catalogue de relations (8 → 12) avant tout passage sur `main` | open | humain | Bloque la promotion, pas le développement sur `dev` |
| RF-14 | Migrer les études JSON existantes de `kind` vers `tier` | open, basse priorité | — | Le mapping legacy garde la compatibilité ; la migration est cosmétique |
| RF-15 | Contrat : au plus une modification de type par cycle. `reinforce.py` tronque à trois actions sans vérifier ce point | open | — | Contrôle fait aujourd'hui par la skill (étape 5) ; le code doit l'imposer, avec fixture négative |
| RF-16 | Évaluation de la skill : le groupe témoin « sans skill » et le jugement LLM n'ont pas été exécutés ; les cas de refus sont vérifiés sur des réponses rédigées pour le test | open | humain | Relancer avec un juge indépendant avant de déclarer la skill validée |
