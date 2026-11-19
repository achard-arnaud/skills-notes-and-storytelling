# PRD #258 — Sélection du schéma narratif

**v1.0 · 20 novembre 2026 · PRD validé par François · Recette éditoriale #258 ouverte**

Ce fichier est le PRD de référence de [#258](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/258). Il versionne le cadrage relu et validé. Les statuts d’implémentation et les limites de preuve sont suivis dans [l’audit de raccord](../planning/AUDIT-258-S3.md) et [l’ADR-1010](../architecture/ADR-1010-narrative-selection.md).

## Décision attendue

Retenir pour le pilote un sélecteur narratif commun aux cinq skills S3. Le produit couvre deux usages : composer une note courte directement après l’analyse, ou produire un scaffold A2 dans le workflow A0–A4. Une même analyse peut ainsi servir deux supports en conservant ses preuves, ses incertitudes et son périmètre.

**Public.** François et les auteurs de notes de décision ; agents Codex chargés de composer ou de relire. Un auteur veut choisir une démonstration adaptée au lecteur sans reprendre la collecte. Un relecteur veut retrouver la preuve de chaque conclusion et renvoyer un écart à l’étape qui peut le corriger.

**Alternative.** Conserver un choix narratif propre à chaque skill. Cette option réduit l’effort initial et reste le point de comparaison du pilote. Elle laisse à chaque parcours la charge de préserver les mêmes règles de preuve et de reprise. Le gain du sélecteur commun reste une hypothèse à mesurer.

## Sources et limites

| ID | Source | Ce qu’elle établit |
|---|---|---|
| S1 | [Storytelling #258](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/258) et playbook fourni par François | Intention produit, rédaction conclusion en tête, parcours court autonome, réemploi A2–A4 et approbation humaine. La recette reste ouverte. |
| S2 | [Contrat d’analyse S3](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/7509a20833fd947053afb8c3e20d20e9ec099032/references/domain-analysis.md) et cinq SKILL.md lus au snapshot de base | Les méthodes métier restent propriétaires des constats. Business réemploie l’analyse dans un brief et un rapport ; produit fige ses constats avant composition ; technique sépare décision et format. |
| S3 | [Workflow A0–A4](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/7509a20833fd947053afb8c3e20d20e9ec099032/workflow/case-process.json) et prototype local #258 | A2 structure décision, objection et falsificateur. Le prototype projette les claims ; il ne sélectionne pas de schéma. L’invalidation active demeure par étape et dépendances. |
| S4 | [Barbara Minto — Pyramid Principle et SCQ](https://www.barbaraminto.com/) | Référence pour le point directeur et le cadrage de la question. Les schémas nommés ci-dessous constituent le catalogue candidat du produit. |

## Parcours et règles de réemploi

| Moment | Mode direct | Workflow complet |
|---|---|---|
| Analyse | L’auteur mobilise seulement les skills S3 utiles. Il fournit leurs constats et leurs références locales. | A0 collecte et borne la couverture. A1 consolide les claims et leurs références. |
| Choix narratif | L’auteur demande un schéma pour une note courte. Le parcours ne requiert aucun cas A0–A4. | A2 consomme les claims A1. Il fixe la conclusion, la tension, l’objection, le falsificateur et l’ordre des sections. |
| Composition | La note suit le plan et conserve les limites de preuve. | A3 reçoit le paquet de sa section : conclusion, claims, transition et encart éventuel. |
| Revue et reprise | La revue ciblée rend un écart, son propriétaire et un test de sortie. | A4 contrôle preuve, contre-perspective et cohérence de la décision. Le reçu de rendu s’ajoute lorsque requis. L’écart retourne à son étape propriétaire. |

Les liens croisés pointent vers la méthode ou le résultat à réutiliser. L’appel en A3 porte sur le paquet validé pour la section. L’appel en A4 porte sur les contrôles et leurs preuves. Une correction de fond revient à A1 ou au propriétaire S3 ; une preuve manquante appelle A0 ou une collecte ciblée en mode direct. La revue conserve les éléments non affectés selon la granularité réellement prise en charge.

| Domaine S3 | Élément demandé au propriétaire | Arc candidat |
|---|---|---|
| Business | Mécanisme de valeur, unité économique et arbitrage capital/risque | Tension puis résolution |
| Produit | Usage observé, cohorte, comparabilité et conditions de fit | Comparaison ou tension puis résolution |
| Technique | Verdict, alternatives, contrainte décisive et retour arrière | Pyramide, comparaison ou trajectoire |
| Pédagogie | Compétence, erreur fréquente, tâche, réussite observable, transfert | Objectif, exemple, pratique, transfert ; extension à éprouver |
| Réglementaire | Applicabilité, juridiction, date, exception, obligation et contrôle | Pyramide ou trajectoire |

## Exigences et critères de recette

| ID | Exigence observable | Test discriminant |
|---|---|---|
| FR-01 | Choisir selon la décision et les preuves disponibles. Expliquer le choix en une phrase. Le format est une contrainte de composition. | Sur quatre mandats synthétiques, distinguer verdict direct, diagnostic, options et déploiement. Sur mandat ambigu, rendre la donnée manquante plutôt qu’une recommandation fabriquée. |
| FR-02 | Rendre un paquet lisible : schéma et raison, conclusion, tension, objection, falsificateur, sections ordonnées, claims et lacunes. | Composer un two-pager sans initialiser de cas ; produire un scaffold A2 depuis la même analyse ; retrouver la même attribution et les mêmes incertitudes. |
| FR-03 | Conserver la classification A1 : un pilier principal par claim atomique, secondaires facultatifs ou non-classement motivé. Échelle, dimension et couche d’activité restent indépendantes. | La promesse fournisseur de ROI reste attribuée dans P-ECONOMICS. Le manque de données reste une condition P-TECH-DATA. Les claims non examinés restent visibles ; la couverture porte sur le mandat. |
| FR-04 | Limiter les encarts candidats à un ancrage du tronc et à des claims présents dans la section. Exiger objection, limite et retour. | Rejeter un encart orphelin ou porteur d’une preuve nouvelle. Préserver les anciens types D22 et les sorties épinglées. |
| FR-05 | Appliquer la conclusion en tête, une idée par phrase et une formulation affirmative lorsque fidèle au fait. A2 s’en tient au mandat. | Une absence peut devenir « Le ROI reste à établir ». Le contrôle préserve le sens d’un refus, d’un résultat négatif ou d’une citation. Aucun angle éditorial supplémentaire sans demande. |
| FR-06 | Produire pour chaque écart : constat, référence, propriétaire, action et test de sortie. Réserver l’approbation éditoriale à l’humain. | Corriger une source, relire les sorties touchées, distinguer la branche indépendante et vérifier que le moteur applique seulement son invalidation actuelle. Un PASS mécanique laisse l’approbation humaine inchangée. |
| NFR-01 | Charger le plus petit paquet utile et signaler les limites de couverture ou de budget. | Journaliser références, passages chargés, éléments omis et cause de l’arrêt ; aucun corpus ou workflow entier requis pour le cas court. |
| NFR-02 | Préserver manifests actifs, contrats fermés, pins historiques et confidentialité des cas. | Vérifier l’absence de migration et enregistrer les écarts entre contrat cible et champs actuellement acceptés. Une stratégie de raccord séparée reste à instruire. |

Catalogue initial proposé : **pyramide de décision**, **tension–résolution**, **comparaison d’options**, **trajectoire par paliers**. Les cinq encarts candidats sont : contrôle terrain, signal pair, changement d’échelle, matrice d’arbitrage et décryptage de mécanisme. Aucun quota par pilier ou par type d’encart.

## Incréments et règle de décision

1. **I1 — Pilote business + technique, FR-01/02/03/05 et NFR-01.** Même analyse, two-pager direct et scaffold A2. Acceptation : traçabilité des claims, même statut de preuve et parcours court autonome.
2. **I2 — Réemploi A3/A4 et boucle de correction, FR-04/06 et NFR-02.** Dépend d’I1 et d’un raccord compatible. Acceptation : test d’encart et scénario de correction d’une source avec branche indépendante ; contrôle séparé de l’approbation.
3. **I3 — Extension produit, pédagogie et réglementaire.** Dépend des résultats I1/I2. Comparer main/S2/S3 à mandat, sources, formats et règles de classement constants. Figer les définitions de piliers seulement après revue des désaccords et des orphelins.

| Mesure | Collecte et décision |
|---|---|
| M1 — Continuité des preuves | Claims décisifs dont ID, attribution, statut et limite sont conservés / claims décisifs attendus, dans les deux sorties d’I1. Tout changement de sens bloque la recette du pilote. |
| M2 — Effort et autonomie | Nombre d’artefacts nécessaires, passages chargés et temps observé par paire de sorties, comparés au parcours actuel sur le même cas. Baseline et cible à fixer avant l’essai ; aucun gain chiffré à ce stade. |
| M3 — Reprise utile | Écarts injectés renvoyés au bon propriétaire / écarts injectés, avec suivi séparé des sorties affectées et de la branche indépendante. Une approbation automatique ou la perte d’une preuve bloque l’extension. |
| M4 — Usage | Choix réutilisés sans refaire l’analyse / usages candidats du pilote. L’équipe pilote consigne les motifs de contournement ; mesurer l’usage séparément de la qualité de décision. |

**Hypothèse décisive.** Le même paquet sert les deux modes sans rendre la note courte trop lourde. L’objection solide est que les justifications d’A2 imposent un effort disproportionné en mode direct. La paire d’essais I1 départage les deux options. Si la preuve se dégrade ou que l’effort augmente sans bénéfice observable, réduire le paquet court avant d’étendre les appels.

**Conditions de recette.** Le raccord A2–A4 reste optionnel et épinglé à l’intake. La revue directe traite les écarts avec preuve, responsable et test. L’arc pédagogique reste une extension candidate. La couche transverse et la comparaison réelle main/S2/S3 restent à traiter dans le pilote. L’exécution sur un cas synthétique ne valide pas un livrable réel.

**Reçu v0.1.** Relecture documentaire : périmètre, traçabilité FR→incréments→mesures et séparation court/complet vérifiés dans ce PRD. Tests produit, CI, rendu et intégration : non exécutés pour cette passe. Aucun changement aux skills, workflows ou statuts GitHub.
