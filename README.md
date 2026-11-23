# Decision Notes & Storytelling

Transformez une question et des preuves en un support adapté à la décision ou à l’apprentissage. Les cinq compétences S3 traitent le fond. Le profil narratif relie leurs constats au récit. Le workflow complet ajoute un dossier de travail, des étapes contrôlées et une reprise sur preuves.

## Choisir le parcours

| Besoin | Point de départ | Résultat |
| --- | --- | --- |
| **Format court et ciblé** | Donner la question, le lecteur, les preuves et l’usage au [point de routage S3](references/s3-operations.md#point-de-routage-obligatoire). Le domaine retenu choisit ensuite la méthode et le format. | Une note, une comparaison, un exercice ou une fiche avec sources, limites et reçu direct. Aucun dossier A0–A4 à initialiser. |
| **Histoire, rapport ou mémo approfondi** | Écrire le brief : décision ou objectif, entité, périmètre, lecteur, sources autorisées, date de référence, budget de recherche, format et revue attendue. Faire valider le plan de routage, puis ouvrir un cas A0–A4. | Une étude multi-échelle, une chaîne de preuves consultable, un récit relu et une reprise après correction. |

Quand le brief reste flou, résoudre d’abord la question qui change le parcours ou l’analyse. Un support Word ou PDF suit ses propres contrôles. La longueur du support, la profondeur de l’étude et la disponibilité d’un renderer sont trois décisions distinctes.

## Cinq portes d’entrée par thème

| Domaine | La skill répond à | Formats courts à demander | Brief approfondi |
| --- | --- | --- | --- |
| [Business](skills/business-analysis/SKILL.md) | Modèle économique, opérations, valeur et risque | One-pager, two-pager business, arbitrage capital/risque | Diagnostic et trajectoire, analyse buy-side |
| [Produit](skills/product-analysis/SKILL.md) | Usages observés, offre, adoption et valeur produit | Fiche produit, comparaison ciblée | Benchmark, diagnostic d’offre, analyse de fit |
| [Technique](skills/technical-analysis/SKILL.md) | Architecture, interfaces, fiabilité et décision | Mémo de décision, note d’intégration | Architecture, comparaison, trajectoire ou POC |
| [Pédagogie](skills/pedagogical-ai-learning/SKILL.md) | Compétence, pratique, succès observable et transfert | Explication, exercice, retour ou aide au transfert | Séquence d’apprentissage, support six pages si demandé |
| [Réglementaire](skills/regulatory-bootstrap/SKILL.md) | Applicabilité, obligations, exceptions et contrôle | Fiche datée de disposition ou d’obligation | Étude sectorielle et trajectoire de conformité |

Une étude peut croiser plusieurs thèmes. Chaque question a un propriétaire, et les contributions gardent leurs dates, statuts et références. Voir le [contrat d’analyse S3](references/domain-analysis.md) et le [catalogue des supports](templates/manifest.json).

### Exemple direct

> Fais un two-pager business pour le comité d’investissement. Appuie la conclusion sur le ROI attribué et la couverture réellement observée. Précise le test qui ferait évoluer la décision.

Après l’analyse S3, réutiliser [le sélecteur](skills/selecting-narrative-schema/SKILL.md) si le support appelle un récit de décision :

```bash
python scripts/narrative_selector.py select --input examples/narrative-selector-business.json
```

Le paquet porte l’arc, la conclusion, la tension, l’objection, le falsificateur et les sections. Il conserve les preuves, les limites et les lacunes. L’exemple est synthétique. La commande produit du JSON ; la rédaction et la revue restent des étapes explicites.

### Exemple d’étude complète

> Prépare un mémo d’arbitrage avant déploiement. Examine le marché et le cadre externe, le portefeuille de sites, puis les données et workflows du pilote. Fixe les sources, les lots de collecte, les contradictions à instruire et le critère d’arrêt. Livre une recommandation avec conditions et réversibilité.

Pour un nouveau cas sur une version publiée, vérifier le moteur local, préparer `intake.json` et sélectionner `narrative_profile: s3-narrative-v1` pour la projection candidate.

```bash
python scripts/case_runtime.py check
python scripts/case_runtime.py init --case mon-cas --input intake.json
python scripts/case_runtime.py begin --case mon-cas --stage A0
```

| Étape | Travail et artefact |
| --- | --- |
| **A0 · Collecter** | Recherche par lots macro → méso → micro. Captures, locators, date, couverture et motif d’arrêt. |
| **A1 · Analyser** | Graphe de claims, fragments et relations. Les [piliers causaux](references/causal-pillars.md) guident la projection. Les lacunes déclenchent une collecte ciblée. |
| **A2 · Structurer** | Brief narratif, objection, falsificateur, sections et claims. Le format reste indépendant de l’arc. |
| **A3 · Composer** | Un paquet par section. Conclusion en tête, une idée par phrase, preuve au bon endroit. Les encarts restent candidats. |
| **A4 · Relire** | Preuves, contre-perspective et décision. Chaque écart revient à son propriétaire avec un test. L’approbation éditoriale revient à l’humain. |

Le moteur vérifie les étapes, les références et les empreintes ; l’agent réalise la recherche et la composition. Les déploiements, diagnostics ou comparaisons choisissent les mêmes schémas en mode court et via A2. Les étapes A3/A4 réemploient le paquet, avec le contexte propre à leur travail. Voir [les entrées, sorties et commandes](references/case-process.md).

## État, rendu et reprise

- Les cas restent privés dans `data/cases/<id>/`. Reprendre un cas au BUILD épinglé. Une correction ouvre de nouvelles tentatives.
- L’invalidation suit l’étape et ses dépendances dans le cas courant. Les cas indépendants restent intacts. Les anciens parcours et types d’encarts D22 restent lisibles sur leur route.
- La réussite mécanique d’A4, la vérification d’un PDF et l’approbation humaine sont trois actes distincts.
- La [liste des profils exécutables](workflow/case-process.json) fait foi pour le rendu via moteur. Les formats peuvent disposer de renderers séparés, dont le [rendu pédagogique](renderers/pedagogical/). Le contrat [DOCX](contracts/docx-runtime-interface.schema.json) et la [checklist](tests/QA_CHECKLIST.md) s’appliquent aux documents Word.

Le reçu direct indique les méthodes effectivement chargées et le mode d’exécution observé. La disponibilité d’une skill et la validation d’une étape A0–A4 sont documentées séparément. Le suivi du hand-off figé et de sa preuve de rendu reste dans [#318](../../issues/318) ; la proposition [#323](../../pull/323) est facultative. Un plan ou un paquet de preuves ne garantit pas à lui seul qu’un PDF a été rendu ni vérifié.

## Contribuer au produit

Le [PRD #258](docs/specifications/PRD-258-selecteur-narratif.md) est la source des exigences. L’[index d’architecture](docs/architecture/) explique les décisions. Le [mapping opérationnel](references/s3-operations.md) relie skills, agents, artefacts, statuts et boucles ; l’[audit de raccord](docs/planning/AUDIT-258-S3.md) distingue livraison technique, intégration restante et recette humaine.

Travailler sur une branche issue de `dev`, suivre [AGENTS.md](AGENTS.md) et utiliser des fixtures synthétiques. Pour une régression transverse :

```bash
python -m pip install -r requirements.txt
python scripts/validate_contracts.py
python scripts/case_runtime.py check
python -m unittest discover -s tests
(cd diagnostic-complet && python -m unittest discover -s tests)
```

La CI vérifie le commit de livraison. La publication sur `main` suit la validation du projet et la vérification de l’ascendance. Un dossier de run, son corpus et ses sorties restent hors Git.
