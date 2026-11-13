# Revue complète des 14 ADR historiques

Date : 2026-11-13. Baseline dev : ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd ; main : 92e9fc941346af756b5ba560e6d2c85ec66518d6. Inventaire Git récursif non tronqué : 14 ADR, tous dans diagnostic-complet ; aucun ADR sur main avant cette livraison.

La revue porte sur tous les ADR inventoriés, leurs décisions, conséquences et spécifications historiques. La couverture des issues est distincte : un inventaire complet ne prouve pas une revue technique exhaustive de chacun de leurs critères.

## Résultat par ADR

| ADR historique | Traitement | Principe commun |
|---|---|---|
| [ADR-0000](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0000-registre-decisions-run.md) — Registre historique et portée des décisions | historique ; principes transverses repris par ADR-1001 à ADR-1006 ; réécrit avec portée locale et historique immuable | ADR-1006 |
| [ADR-0001](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0001-kb-contrat-documentaire.md) — Ingestion documentaire et identités | accepté, local ; réécrit avec portée locale et historique immuable | ADR-1002 |
| [ADR-0002](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0002-referentiel-ontologie.md) — Ontologie documentaire et validation structurelle | proposé, implémentation locale en lecture seule ; réécrit avec portée locale et historique immuable | ADR-1002 |
| [ADR-0003](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0003-loopback-graphe.md) — Loopback du graphe | accepté, observation locale ; réécrit avec portée locale et historique immuable | ADR-1005 |
| [ADR-0004](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0004-renforcement-kb-spec.md) — Spécification historique du renforcement | historique, consolidé par ADR-0003 et ADR-0005 ; réécrit avec portée locale et historique immuable | ADR-1005 |
| [ADR-0005](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0005-contrat-skill-reinforce.md) — Distribution de la skill de renforcement | accepté, choix local de packaging ; réécrit avec portée locale et historique immuable | ADR-1001 |
| [ADR-0006](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0006-calibration-cadence.md) — Calibration de cadence | accepté ; aucun seuil calibré par cette revue ; réécrit avec portée locale et historique immuable | ADR-1005 |
| [ADR-0007](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0007-projection-graph1.md) — Projection privée Graph1 | accepté, adaptateur local ; réécrit avec portée locale et historique immuable | ADR-1004 |
| [ADR-0008](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0008-frontiere-run-build.md) — Frontière RUN/BUILD et profils | accepté, spécialisation locale ; réécrit avec portée locale et historique immuable | ADR-1004 |
| [ADR-0009](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0009-terminologie-kind.md) — Terminologie et éligibilité des sources | accepté, contrat local courant ; réécrit avec portée locale et historique immuable | ADR-1002 |
| [ADR-0010](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0010-detection-directive.md) — Heuristique de détection des directives | accepté, règle d’implémentation locale ; réécrit avec portée locale et historique immuable | ADR-1002 |
| [ADR-0011](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0011-acquisition-2026-11-10-et-migration-profil.md) — Migration de profil et résolution des exemples | accepté, décision locale ; bilan du lot conservé historiquement ; réécrit avec portée locale et historique immuable | ADR-1004 |
| [ADR-0012](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0012-directive-de-style-et-double-cerveau.md) — Style éditorial et contexte métier | accepté pour le style ; interprétations métier hors architecture commune ; réécrit avec portée locale et historique immuable | ADR-1003 |
| [ADR-0013](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0013-statuts-de-lecture-et-outil-de-migration.md) — Migration sûre et statuts de revue | accepté, contrat local ; réécrit avec portée locale et historique immuable | ADR-1005 |

## Découpage retenu

- Les 1001–1006 exposent les choix transverses souples : routage, preuve, narration, contexte, amélioration, gouvernance.
- Les 0000–0013 gardent leurs IDs et le périmètre du prototype. Les versions détaillées restent accessibles au commit de baseline. Les anciens textes contradictoires ne sont plus réinjectés comme politique courante.
- Les décisions de run (acquisition, validation partielle, métriques métier) restent historiques ; elles n’entrent pas dans les principes communs ni dans un nouveau schéma de données.
- Les détails de commande, champs, versions et heuristiques se lisent dans leurs ressources opérationnelles au SHA épinglé.
- Les références aux anciens tiers sont historiques ; le contrat local courant utilise kind. L’ADR ontologie reste proposé, sans approbation produit ajoutée par la revue.

## Publication et portée

Les principes communs et ce rapport sont livrés sur main et dev. Les ADR locaux restructurés restent sur dev avec le prototype. Les manifests de templates/modes et les schémas exécutables sont inchangés : introduire une clé documentaire dans ces schémas fermés ferait dériver le contrat. Un registre séparé sert uniquement la navigation.

La stratégie de convergence reste une décision ultérieure : migration par capacités ou intégration du prototype. La note tactique d’opportunité est remise dans la conversation. Aucun runtime ni nouvelle skill n’est activé par cette livraison.
