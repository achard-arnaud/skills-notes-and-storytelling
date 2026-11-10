# ADR-0008 — Frontière entre exécution (RUN) et construction (BUILD)

- **Statut** : accepté
- **Date** : 2026-11-10 (consignation ; décisions d'origine ci-dessous)
- **Décisions liées** : D25, D26 (autre session), D27, D28 (profils), D33 (microsoft conservé)
- **Tickets** : #141, #94, #75, #25, RF-01 à RF-05, RF-08

## Contexte

Le corpus réel et les notes de travail ne doivent pas se retrouver dans le code de construction public, ni le code dépendre d'un run.

## Décision

Le code et les référentiels sont run-agnostiques. Le vocabulaire de run vit dans `profiles/<run>.profile.json`. Une KB est liée à un seul profil (`profile_id`). Les exemples de KB sont des identifiants opaques, avec un jumeau synthétique par type. Le profil GreenYellow est conservé dans le dépôt, avec le lexique `microsoft` (D33) ; son emplacement reste à trancher (RF-18).

## Conséquences

Un test échoue si un terme de run apparaît dans le code de build. Changer le lexique du profil change sa version : une migration explicite est requise (RF-06).

## Spécification migrée (contenu d'origine, non modifié)

Décisions D25 et D26. Tickets prioritaires pris en compte : #141 (séparer la maintenance de construction et la production d'exécution), #94 (connaissance sectorielle et réalité de l'entreprise séparées), #75 (captures immuables hors dépôt public), #25 (base de connaissances, captures hors dépôt public, branchement optionnel).

## Les deux côtés

| | Construction (BUILD) | Exécution (RUN) |
|---|---|---|
| Contenu | Contrats, code, tests, skills, workflows, jumeaux synthétiques | Corpus réel, base de connaissances privée, notes de recherche, sorties d'évaluation, brouillons |
| Lieu | Ce dépôt public, branche `dev` | Graph1 privé (`knowledge/business/…`) et dossiers de travail hors dépôt |
| Qui change quoi | Un commit avec tests | Une ingestion ou une recherche, avec reçu |
| Visible dans le dépôt public | Oui | Seulement des identifiants opaques, des comptes et des empreintes |

Le vocabulaire de run (entités, piliers, namespace de projection) vit dans `profiles/` et une base de connaissances est liée à un seul profil (D27, D28). Le registre `workflows/kb-examples.json` nomme encore le namespace de la base privée : c'est un reste de couplage à déplacer vers un profil.

*Note du 2026-11-10 : le registre ne nomme plus le namespace, il renvoie au profil (D38, ADR-0011).*

## Règles (ticket #141)

1. Une exécution ne corrige jamais silencieusement un contrat, un skill, un workflow ou un gabarit. Un défaut constaté pendant une exécution devient une **proposition de construction** liée (commit séparé ou ticket) ; l'exécution garde la version qu'elle a utilisée.
2. Aucun test de construction ne lit le corpus privé. Les tests et les évaluations utilisent des **jumeaux synthétiques** (`fixtures/examples/`).
3. Une sortie d'exécution ne promeut ni fait ni règle.
4. Les captures brutes restent hors du dépôt public (#75) ; le dépôt ne garde que l'identifiant, l'empreinte et le statut.

## Stockage des exemples issus de la base de connaissances (D26)

Trois emplacements étudiés :

| Option | Verdict |
|---|---|
| Copier des blocs de texte réel dans les skills ou les fixtures du dépôt public | Refusée : fuite du corpus (D06, #75), couplage construction-exécution |
| Garder uniquement des identifiants dans les skills | Insuffisante seule : l'agent ne voit pas la forme attendue sans accès privé |
| **Identifiant opaque côté exécution + jumeau synthétique côté construction** | **Retenue** |

Fonctionnement : chaque exemple du registre `workflows/kb-examples.json` pointe vers son contenu réel par des identifiants d'atomes (résolus dans Graph1) et, pour les six types de side stories, vers un jumeau synthétique `fixtures/examples/<type>.study.json`. Le jumeau reproduit la **forme** de l'exemple (nombre de lignes, blocs, champs, limites) avec un contenu fictif et sans citation inventée. `tests/test_sidestories.py` vérifie que chaque jumeau valide au format du type, qu'il se rend dans la vue lecteur en langage clair et qu'il ne contient aucun marqueur du corpus.

## Séparation du sectoriel et de l'entreprise (ticket #94)

Une connaissance de secteur ne devient pas un déploiement chez la cible sans claim spécifique. Les sources acquises sont étiquetées `scope: sector` ou `scope: company` dans leurs notes. La veille académique reste sectorielle ; seule la ligne « en pratique » transfère au cas, au conditionnel. La veille entreprise reste centrée sur un acteur et ses signaux publics.

## Ce que cette passe ne fait pas

Elle n'ouvre aucun développement des tickets #141, #94, #75 et #25, qui restent en statut de spécification. Elle applique leurs règles aux livrables de cette session.

