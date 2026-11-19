# Audit de raccord #258 — analyse, narration et gouvernance S3

Base BUILD : `dev` 109bc90a72d14c5c08835c6a822d0de788927a30 ; `main` 7509a20833fd947053afb8c3e20d20e9ec099032 au démarrage. Le PRD canonique est [versionné ici](../specifications/PRD-258-selecteur-narratif.md). Le jugement éditorial du cas d’origine et la recette de convergence restent à leurs propriétaires.

## Harvest : conserver ce qui a un consommateur

| Source relue | Principe retenu | Réemploi dans cette PR |
| --- | --- | --- |
| Business | Réemployer mécanisme, limites et inconnues du brief au rapport | Le format reste une projection des mêmes constats |
| Produit | Figer utilisateur, version, cohorte, usage attesté et critères de fit | Le choix du schéma conserve les comparables et les limites |
| Technique | Séparer profil de décision, alternatives, format et rollback | Le mémo technique reste exigible et distinct du paquet narratif |
| Pédagogie | Partir de l’action observable et du transfert | Arc candidat pratique-transfert ; parcours six pages réservé à son contrat |
| Réglementaire | Ancrer version, juridiction, exceptions et effectivité | Budget approfondi local à son mandat ; distinction autorité/attribution conservée |
| [Harvest contrats/runtime](../architecture/harvest-contract-runtime-2026-11-17.md) | Contrat I/O avant exécution, dépendances épinglées, reprise bornée, incident avec test de sortie | Une projection sans moteur supplémentaire ; même mécanisme de reprises |
| [Agent Skills](https://agentskills.io/specification) | Point d’entrée court, fichiers de référence chargés selon besoin | Package et lien de découverte dans le dépôt. Aucune installation personnelle |

L’inventaire consulté n’a pas permis d’identifier un dépôt « AD Skills » appartenant au compte GitHub. Le transfert repose sur les cinq sources versionnées, le harvest déjà publié et la spécification Agent Skills ; aucun harvest externe supplémentaire ne fait partie des preuves.

## ADR et contrats

| Décision existante | Alignement #258 |
| --- | --- |
| 1001, 1007 et 1009 · Routage, étude et domaines | Cinq propriétaires S3 ; profondeur, format et arc ont chacun un choix. La route courte contourne l’initialisation A0–A4. |
| 1002 · Connaissance | Le sidecar narratif indexe des claims existants. La provenance et les statuts restent chez leurs propriétaires. Le prototype devient le point de départ du contrat de projection, sans migration de l’ontologie. |
| 1003 · Narration et rendu | A2 fixe le récit et son ancrage ; A3 consomme une section ; A4 vérifie la preuve, l’objection et la décision. Le rendu garde son binding. |
| 1004 et 1008 · RUN/BUILD et moteur | Le profil est opt-in, sa spec et son code sont épinglés. Les mêmes tentatives et journaux sont réutilisés. |
| 1005 · Apprentissage | Écart → propriétaire → action → test. Revue de fond humaine. Défaut reproductible → BUILD avec fixture. |
| 1006 · Autorités | Le PRD versionné porte les exigences ; l’ADR porte le choix ; les manifests portent les capacités ; les reçus portent la preuve d’exécution. |
| ADR diagnostic-complet 0000–0013 et D22 | Conclusions, contrats et formats historiques conservés ; ce changement se branche uniquement sur les cas qui le demandent. Le [mapping existant](../architecture/ADR-REVIEW-2026-11-13.md) reste l’index pour les correspondances. |

## Registre des tickets rapprochés

| Suivi | Disposition au regard du PRD |
| --- | --- |
| [#258](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/258), [#255](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/255), [#256](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/256), [#261](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/261) | #258 garde la recette humaine du premier rapport ; #255/#256 sont les antécédents de trame et d’encarts ; #261 reste le périmètre narratif historique. |
| [#294](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/294), [#295](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/295), [#303](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/303), [#296](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/296) | Réemploi du socle de preuves. Raccord du sélecteur aux résultats A1 ; l’adaptateur d’analyse historique et l’intégration GreenYellow restent dans leurs lots. |
| [#297](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/297), [#279](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/279) | Couverture du call direct, de la reprise et des cinq domaines par fixtures. Rejeu comparatif réel main/S2/S3, installation et retrait des anciennes routes restent distincts. |
| [#317](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/317), [#318](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/318), [#331](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/331), [#332](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/332), [#333](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/333) | Paquets scindés et preuves épinglées ; le sélecteur ne remplace ni l’adaptateur two-pager, ni OutputSpec, ni QA du renderer, ni le chantier de catalogue. |
| [#289](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/289), [#337](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/337), [registre RF](../../diagnostic-complet/docs/REFACTOR-BACKLOG.md) | Loopback repris comme contrat de routage ; preuve indépendante et installation de reinforce-kb-loopback restent à ces tickets. Les migrations/recettes privées RF-18/RF-22/RF-23/RF-24 ne sont pas couvertes. |
| [#301](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/301), [#338](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/338), [#339](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/339) | Extension pédagogique candidate indépendante des annexes F01. Le moteur de cas et l’autorité du mémo technique sont conservés. |
| [PR #12](https://github.com/achard-arnaud/skills-notes-and-storytelling/pull/12), [PR #323](https://github.com/achard-arnaud/skills-notes-and-storytelling/pull/323), [PR #341](https://github.com/achard-arnaud/skills-notes-and-storytelling/pull/341) | Travaux parallèles : contrats CLOSING/Workbench, preuve business deux pages et miroirs KB. #12 partage le fichier d’entrée SKILL.md ; sa branche et ses bindings restent à son propriétaire. Aucun de ces lots n’est repris dans cette PR. |

## Revue et limites de validation

| Critère | Vérification / prochaine étape |
| --- | --- |
| FR-01/02 · choix et continuité | Tests des intentions et refus sur ambiguïté ; un même jeu de faits passe directement et via A2 → A3 → A4. |
| FR-03/04 · classification et encarts | Attribution de la promesse ROI, axes séparés, pilier absent/non classé ; refus d’un claim étranger à la section. Compatibilité des anciens types par la route historique. |
| FR-05 · écriture et revue | Contrat rédactionnel ; fidélité du texte, force de la contre-preuve et qualité éditoriale restent à vérifier humainement. |
| FR-06 · correction | Rejet d’une capture modifiée, nouvelle tentative, branches indépendantes intactes. Cas synthétiques ; vérification mécanique distincte de l’approbation. |
| NFR-01/02 · contexte et compatibilité | Ledger limité aux claims choisis ; extrait par section et déclarations de couverture. Cas historiques à leur BUILD. Aucun gain mesuré de temps, de coût ou de tokens. |
| Recette I3 et mesures | Réserver une comparaison réelle conforme à #297 : même mandat, même accès, mêmes locators et même support. Examiner les désaccords, mesurer la charge (M2) et faire valider le rapport par son responsable. |
