# ADR-0001 — Contrat de la KB documentaire locale

- **Statut** : accepté
- **Date** : 2026-11-10 (consignation ; décisions d'origine ci-dessous)
- **Décisions liées** : D06 (corpus privé hors dépôt public)
- **Tickets** : #25, #75

## Contexte

Le besoin : atomiser des sources Markdown sans rien promouvoir en fait, et garder la provenance de chaque unité.

## Décision

Copie exacte des octets, identité des atomes par type et texte normalisé, identité des occurrences par source et offsets, statut `supplied_unverified` par défaut.

## Conséquences

Les atomes dédupliqués gardent toutes leurs occurrences. Changer le type d'un atome change son identifiant (voir ADR-0010).

## Spécification migrée (contenu d'origine, non modifié)

`kb.py` fournit une ingestion incrémentale de fichiers Markdown ou texte UTF-8. Elle conserve les octets des sources, découpe des unités localisables, écrit les fiches Markdown et construit un graphe documentaire. Aucune assertion ne devient un fait vérifié : le statut reste `supplied_unverified`.

```bash
python diagnostic-complet/kb.py /chemin/prive/texte.md /chemin/prive/autre.txt --out /chemin/prive/kb --profile diagnostic-complet/profiles/greenyellow.profile.json
```

API : `ingest_files(paths, out, source_kind="supplied_context", allow_private_git=False, profile=None) -> receipt`. Sans `profile`, le profil `neutral` s'applique (aucun vocabulaire de run). Une KB est liée à un seul profil : l'index refuse un autre `profile_id`. Par défaut, le répertoire de sortie doit être hors de tout dépôt Git. Une destination Git déclarée privée par l'appelant est autorisée avec `allow_private_git=True` ou l'option CLI `--allow-private-git`, après vérification de visibilité par le coordinateur. Le module local ne vérifie pas la visibilité distante et son reçu le précise. Toute destination sous la racine du dépôt business public contenant ce module reste interdite, même avec cette option. Le coordinateur extrait les ZIP au préalable après contrôle de traversée de chemin, liens symboliques, tailles et types ; le module refuse directement les ZIP. Le contenu fourni, y compris une directive, est indexé comme donnée et jamais exécuté.

## Autorités et sorties

| Fichier | Contenu et rôle |
|---|---|
| `sources/SRC-<sha256>.source` | Copie exacte des octets ; source de vérité documentaire, UTF-8 strict, CRLF conservés |
| `sources-manifest.json` | Identités, tailles, hash, locations d'origine, copies, couverture mécanique et versionnements explicites |
| `kb.json` | Index des sources, unités dédupliquées et occurrences exactes ; autorité pour la reprise |
| `atoms/ATOM-<sha256>.md` | Fiche de lecture avec frontmatter JSON-compatible YAML, statut, type, pistes de piliers et IDs d'occurrences |
| `graph.json` | Projection `nodes/edges` avec `from/to/kind`, reconstruite depuis l'index |

Une source est identifiée par son hash SHA-256 complet. Plusieurs chemins contenant les mêmes octets partagent cette source et conservent tous leurs localisateurs. Le `source_kind` décrit l'origine déclarée, sans changer le statut de connaissance.

## Découpage et traçabilité

Types : `assertion`, `heading`, `directive`, `question`, `table`, `code`. La découpe des phrases/propositions est heuristique : ponctuation terminale ou point-virgule hors parenthèses/crochets, items de liste distincts, maintien des décimaux et de certaines abréviations. Elle ne prétend pas résoudre toute proposition logique. Les titres, tableaux et blocs de code restent des unités structurelles, avec `semantic_atomization=false` ; le contenu d'un tableau ne devient pas une série de faits atomiques.

Chaque occurrence conserve `text` exact, offsets caractères et octets UTF-8 `[start,end)`, lignes 1-based inclusives, source hashée et localisateurs. Les offsets sont vérifiés contre la copie exacte, indépendamment du texte représentatif affiché dans la fiche dédupliquée. Les espaces de séparation non portés par un atome restent dans la source complète.

Identités :

- `ATOM-<hash(type + NUL + texte normalisé)>` : contenu documentaire dédupliqué ; normalisation NFKC, casefold et espaces fusionnés, versionnée.
- `OCC-<hash(source_id + offsets + texte exact)>` : occurrence originale, stable et globale. C'est cette identité qui porte la preuve de localisation.

La déduplication ne fusionne aucune signification : elle rapproche uniquement un texte normalisé de même type. Les variations originales et tous localisateurs restent dans les occurrences. Les paraphrases ne sont pas fusionnées automatiquement.

## Graphes et pistes de classement

Le graphe documentaire contient sources, atomes, entités et piliers candidats. Les liens source → atome sont `derived_from` et portent l'occurrence ; ils signifient une provenance documentaire, jamais une preuve de vérité. Les liens atome → pilier sont `candidate_classification`, avec termes déclencheurs et version de lexique. Ils ne prouvent ni pertinence éditoriale ni causalité.

Le lexique `PILLAR_LEXICON` distingue data, IA, industrie, corporate, économie, gouvernance, stratégie et adoption. Aucun texte n'est obligé de couvrir ces huit pistes. Le lexique `ENTITY_LEXICON` reconnaît uniquement des mentions explicites de noms/termes listés (GreenYellow/GY, PV, efficacité énergétique, etc.). Chaque mention conserve texte exact et positions dans le texte représentatif ; un nom propre hors lexique n'est pas inventé. Les lexiques sont versionnés `1.0.0` et exposés dans le code.

Ces relations ne remplacent ni le graphe probatoire qualifié de `runtime.py`, ni le scaffold lecteur. Aucune relation `causes` n'est créée.

## Reprise et versions

Relancer une ingestion identique ne crée aucune nouvelle source, aucun atome ni occurrence ; les fichiers JSON restent identiques. Un nouveau lot conserve toutes les anciennes sources et unités. Aucun élément n'est supprimé automatiquement.

Un changement d'octets au même chemin crée une nouvelle identité source et un événement `supersedes` avec séquence, ancienne/nouvelle identité et chemin. Les `location_heads` désignent la dernière version observée. Revenir à d'anciens octets crée un nouvel événement de version, sans supprimer l'histoire ; cela ne réconcilie pas les contradictions sémantiques. Un changement de version de schéma/lexique exige une migration explicite.

Un verrou local refuse deux writers simultanés. Les fichiers individuels sont remplacés atomiquement, puis `kb.json` est écrit en dernier. Il ne s'agit pas d'une transaction multi-fichiers distribuée : après interruption, l'index précédent reste autorité et une relance reconstruit les projections. Un verrou laissé par un processus tué exige une inspection avant retrait manuel. Une source conservée corrompue bloque la reprise.

## Couverture et limites

Le reçu et chaque source indiquent tailles d'entrée, nombre d'unités, caractères couverts et caractères non blancs inexpliqués. Cette couverture mesure l'extraction mécanique. Elle ne prouve ni lecture sémantique intégrale, ni recherche publique, ni vérification des assertions. Les unités restent candidates à revue, découpage plus fin ou rattachement narratif.

L'import accepte seulement Markdown/texte UTF-8 extrait. Le module ne fait ni OCR, ni téléchargement, ni extraction ZIP, ni contrôle d'accès distant. Les sources et chemins d'origine peuvent être sensibles : l'ensemble du corpus généré doit rester dans la destination privée du run.

Validation locale :

```bash
cd diagnostic-complet
python -m unittest discover -s tests -p test_kb.py -v
```

