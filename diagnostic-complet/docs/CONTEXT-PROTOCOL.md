# Protocole de continuité — diagnostic complet

Proposition opérationnelle pour le run GreenYellow, 7 novembre 2026. Document intermédiaire ; ni capacité d'orchestration permanente ni compaction technique installée.

## Autorités et invariants

- Le mandat utilisateur courant autorise l'implémentation isolée sur `dev`, les agents parallèles et l'absence de CI ; il ne promeut pas l'ancienne conception globale Workbench et n'autorise pas la publication de sources privées dans un dépôt public.
- Les issues décrivent objectifs, dépendances, acceptation et reçus ; les fichiers versionnés portent le contenu détaillé. L'historique du chat ne doit pas être nécessaire à la reprise.
- Recherche → fragments → claims/graphe → scaffold → narration → rendu restent des transitions distinctes. Un changement de rendu ne promeut jamais une preuve.
- Les preuves historiques importées restent antérieures et typées. Inconnues, contradictions et alternatives rejetées suivent la reprise.
- Un test local automatique, une relecture éditoriale par un agent et une validation humaine sont trois états différents. Aucun agent ne marque une validation humaine à la place de François.

## Quatre phases et périmètre de planification

1. **Explorer et journaliser** : lire les sources minimales, établir le transfert Sri Lanka→business, constater les gaps et déposer les petits travaux sous les epics existants. Gate : mapping sourcé, source HEAD, exclusions et unknowns explicites.
2. **Renforcer et réorchestrer** : relire les tickets, fusionner les doublons, ajouter entrées/sorties/acceptation/dépendances et construire les sprints. Gate : DAG acyclique, aucun ticket READY sans entrée disponible et validation définie.
3. **Implémenter par sprints** : changements isolés, tests locaux ciblés et intégration fast-forward sans CI. Gate par sprint : critères remplis, reçu, hash/commit et reprise suivante vérifiés ; aucun passage vers `main`.
4. **Revoir puis préparer le dry run** : audit de couverture, reprise simulée et import contrôlé GreenYellow ; produire des propositions de piliers/story/side stories à valider. Gate : statut candidat maintenu pour les choix éditoriaux non validés, gaps de corpus identifiés.

Pour atteindre 60–100 microétapes sans bureaucratie : viser 72 unités logiques, regroupées en 12 lots de 6. Chaque unité doit produire un artefact ou une vérification distincte ; ne pas inventer de faux travail pour atteindre un compte. Les epics sont des index thématiques, les sprints des séquences d'exécution, les piliers des vues analytiques : ces trois axes restent indépendants.

## Paquet de contexte par tâche

`packet.json` énumère explicitement les entrées. L'agent ne parcourt pas toute l'étude à chaque reprise.

```json
{
  "task_id": "DC-024",
  "issue": null,
  "objective": "une seule question à résoudre",
  "base_commit": "SHA exact",
  "inputs": [{"path": "chemin", "sha256": "empreinte", "scope": "section/lignes"}],
  "instructions": ["AGENTS.md", "instruction métier ciblée"],
  "write_scope": ["diagnostic-complet/..."],
  "output": ["artefact attendu"],
  "acceptance": ["contrôle positif", "contre-test pertinent"],
  "depends_on": ["DC-018"],
  "stop_condition": "résultat utile atteint ou blocage qualifié",
  "budget": {"input_words_max": 8000, "return_words_max": 600, "repairs_max": 2}
}
```

Budgets initiaux proposés, ajustables après mesure : capsule centrale ≤800 mots ; paquet tâche ≤8 000 mots de fichiers effectivement chargés ; réponse d'agent ≤600 mots hors artefacts ; maximum trois agents de travail simultanés plus l'orchestrateur. Le nombre de mots est un proxy mesurable, **pas** un nombre de tokens ni une mesure de toute la fenêtre système. Si un tokenizer exact du modèle n'est pas disponible, le reçu indique `token_count: unknown`.

Tout compagnon obligatoire d'une instruction entre dans le calcul. Le contrôle Sri Lanka existant le fait déjà (`scripts/audit_context_budget.py`, testé par `test_context_budget_runtime.py`) ; il refuse aussi d'auditer un ancien manifeste comme s'il couvrait le dernier run. À adapter plutôt que revendiquer une mémoire automatique.

## Boucle minimale d'une microétape

1. Lire la capsule, l'issue et le paquet ; vérifier HEAD, empreintes, prérequis et write scope.
2. Acquérir un lease de tâche : owner, base SHA, fichiers réservés, heure de début, expiration, état. Deux tâches sur les mêmes fichiers sont séquentielles.
3. Exécuter uniquement le delta ; les recherches nouvelles restent liées à une question et une stop condition.
4. Écrire l'artefact avant de raconter le résultat. Distinguer fait observé, interprétation et limite.
5. Exécuter le contrôle déclaré et son contre-test utile ; enregistrer commande, code retour, sortie condensée et empreintes.
6. Déposer un reçu : résultat, artefacts, décisions, unknowns, dependents invalidés, prochain task_id ; le coordinateur valide l'intégration.
7. Actualiser état/board/capsule, libérer le lease, passer à la tâche READY suivante.

Une tâche ne devient DONE que si ses sorties et critères sont présents. Un reçu manquant laisse `VERIFY`, pas DONE. Un succès d'écriture GitHub n'est pas une relecture conforme ; un timeout d'écriture exige une relecture avant toute répétition.

## Artefacts de mémoire recommandés

| Artefact | Contenu | Chargement |
|---|---|---|
| `RUN_STATE.json` | phase/sprint/tâche, refs exactes, verrous et prochaine action | Toujours |
| `RESUME.md` | mandat courant, décisions durables, gaps matériels, trois prochaines actions | Toujours, borné |
| `PLAN.json` | tâches, epics, dépendances, statuts et critères | Filtre sprint/tâche |
| `DECISIONS.md` | décisions datées, raisons et invalidations ; append-only | Entrées nécessaires |
| `source_register.json` | provenance, version, droits, couverture réelle | Sources utiles |
| `receipts/<task>.json` | inputs/outputs/checks/limites/commit | Prédécesseurs utiles |
| `handoffs/<agent>.md` | résultat court et liens vers détails | À réception seulement |
| `CONTEXT_LEDGER.jsonl` | chemins/hashes, mots lus, cache/réutilisation, budget | Contrôle automatique |

Les captures privées et transcriptions d'entretien restent en stockage privé ; le dépôt public conserve contrats, code, fixtures synthétiques et identifiants opaques autorisés. Une capsule de reprise publique ne doit pas devenir une fuite condensée du corpus.

## Drop et compaction : ce qui est réellement contrôlable

À chaque fin de sprint, sauvegarder puis relire `RUN_STATE.json` et `RESUME.md` ; clôturer les agents terminés ; ne plus réinjecter logs exhaustifs, réponses déjà persistées ou documents non nécessaires. Ne supprimer ni provenance ni décision pour économiser du contexte : retirer du paquet actif, conserver dans l'archive/index.

Un agent nouveau peut repartir avec une mission autonome et seulement les chemins utiles ; c'est une isolation de tâche, pas la preuve que la fenêtre du coordinateur a été effacée. Ni prompt `compact`, ni fichier `DROP.md` ne force la compaction du runtime. Après compaction automatique ou interruption, reprendre depuis les fichiers, rafraîchir la ref distante et revalider les entrées ayant changé. Les tokens déjà lus ne deviennent pas remboursés par un drop logique.

**Test de reprise** : confier une tâche à un agent sans historique conversationnel, avec `RESUME.md` + paquet + prérequis ; vérifier qu'il identifie la prochaine action, les interdits, les incertitudes et l'oracle sans demander une relecture complète.

## Parallélisation, réparation et intégration

- Paralléliser source bootstrap, audit cible, adaptation de contrats ou revue indépendante ; pas les étapes claims→scaffold ou validation→promotion qui dépendent du résultat précédent.
- Chaque agent commence par proposer sa sous-planification au coordinateur/issue et travaille dans un scope distinct. Un seul intégrateur écrit les refs, ordonne les commits et ferme les tickets.
- Pour une cause déterministe : au plus deux corrections. Après deux échecs, marquer BLOCKED avec preuve et poursuivre les branches indépendantes ; ne pas prendre le temps écoulé pour une approbation.
- Si HEAD ou une source change, invalider les seuls descendants du DAG dépendant de l'empreinte changée. Une modification de mise en page ne réouvre pas le sourcing ; un claim infirmé réouvre narration et rendus qui le consomment.
- Vérifier les workflows avant écriture ; utiliser des messages de commit skip CI compatibles, aucun dispatch, aucun PR déclenchant la CI. L'absence de CI n'est pas un PASS ; les reçus disent `local checks passed; CI intentionally not run`.
- Vérifier la branche distante après fast-forward et traiter un HEAD concurrent sans force ni écrasement. Aucune promotion `main` dans ce mandat.

## Gates éditoriaux GreenYellow

L'import sec peut créer fragments, questions, graphes et HTML candidats. Il ne transforme pas l'étude fournie en preuve primaire vérifiée ; VisioSense reste une illustration tant que produit/identité/preuves ne sont pas établis. Piliers corporate et industrie restent distincts, data et IA explicites, sans imposer huit piliers business par analogie. L'inventaire des stories et side stories et la stratégie de récit sont remis à François pour validation, tandis que l'infrastructure et les contrôles déjà autorisés peuvent continuer.

## Limites connues et preuves consultées

Sources directes : `business/AGENTS.md`, `business/references/bridges-integration-and-run-memory.md`, `source-sri/scripts/audit_context_budget.py`, `source-sri/tests/test_context_budget_runtime.py`. Les capacités existantes sont de la méthode, des schémas et scripts locaux, pas un orchestrateur autonome persistant ni Jira installé. Si Projects/Jira n'est pas exposé, construire l'index issue/epic Markdown et annoncer explicitement la surface réellement écrite.
