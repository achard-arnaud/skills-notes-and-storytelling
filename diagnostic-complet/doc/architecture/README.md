# Décisions locales du prototype

Revue complète : 13 novembre 2026. Les principes communs sont dans [l’index racine](../../../docs/architecture/README.md). Ce dossier conserve les décisions d’implémentation du prototype et leurs identités historiques.

| ADR | Sujet | Statut |
|---|---|---|
| [ADR-0000](ADR-0000-registre-decisions-run.md) | Registre historique et portée des décisions | historique ; principes transverses repris par ADR-1001 à ADR-1006 |
| [ADR-0001](ADR-0001-kb-contrat-documentaire.md) | Ingestion documentaire et identités | accepté, local |
| [ADR-0002](ADR-0002-referentiel-ontologie.md) | Ontologie documentaire et validation structurelle | proposé, implémentation locale en lecture seule |
| [ADR-0003](ADR-0003-loopback-graphe.md) | Loopback du graphe | accepté, observation locale |
| [ADR-0004](ADR-0004-renforcement-kb-spec.md) | Spécification historique du renforcement | historique, consolidé par ADR-0003 et ADR-0005 |
| [ADR-0005](ADR-0005-contrat-skill-reinforce.md) | Distribution de la skill de renforcement | accepté, choix local de packaging |
| [ADR-0006](ADR-0006-calibration-cadence.md) | Calibration de cadence | accepté ; aucun seuil calibré par cette revue |
| [ADR-0007](ADR-0007-projection-graph1.md) | Projection privée Graph1 | accepté, adaptateur local |
| [ADR-0008](ADR-0008-frontiere-run-build.md) | Frontière RUN/BUILD et profils | accepté, spécialisation locale |
| [ADR-0009](ADR-0009-terminologie-kind.md) | Terminologie et éligibilité des sources | accepté, contrat local courant |
| [ADR-0010](ADR-0010-detection-directive.md) | Heuristique de détection des directives | accepté, règle d’implémentation locale |
| [ADR-0011](ADR-0011-acquisition-2026-11-10-et-migration-profil.md) | Migration de profil et résolution des exemples | accepté, décision locale ; bilan du lot conservé historiquement |
| [ADR-0012](ADR-0012-directive-de-style-et-double-cerveau.md) | Style éditorial et contexte métier | accepté pour le style ; interprétations métier hors architecture commune |
| [ADR-0013](ADR-0013-statuts-de-lecture-et-outil-de-migration.md) | Migration sûre et statuts de revue | accepté, contrat local |

Chaque ADR pointe vers sa version antérieure immuable, ses ressources et un principe commun. Les preuves de run restent dans leurs reçus. Ne pas déduire une disponibilité runtime ni une validation humaine d’un statut documentaire. Pour une nouvelle décision, choisir une seule question et conserver contexte, portée, choix, conséquences, contrôle et réexamen.
