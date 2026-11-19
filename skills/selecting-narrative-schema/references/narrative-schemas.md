# Schémas narratifs et contrat de réemploi S3

Le schéma répond à la décision. Le format répond à l’usage du lecteur. Le diagnostic thématique et le verdict technique restent chez leurs propriétaires S3.

| Intention déclarée | Schéma | Parcours de lecture |
| --- | --- | --- |
| `verdict` | `decision-pyramid` | Verdict → preuves hiérarchisées → objection → prochain test |
| `diagnose` | `tension-resolution` | Conclusion → tension → mécanismes → conditions → trajectoire |
| `compare` | `option-comparison` | Choix → critère décisif → options sur les mêmes critères → condition de bascule |
| `deploy` | `phased-trajectory` | Cible → prérequis → jalons → critères de passage et retour arrière |
| `teach` | `practice-transfer` · extension à éprouver | Objectif → exemple → pratique → feedback → transfert |

[Barbara Minto](https://www.barbaraminto.com/) documente une organisation hiérarchique sous un point directeur et le cadrage situation, complication, question. Les identifiants, arcs et critères ci-dessus sont le catalogue local de ce projet. Le [profil versionné](../../../workflow/narrative-profile.json) expose le routage et les types consommés par le code.

## Entrées et sorties

Le concret est fourni par l'auteur ou l'étape amont. Le sélecteur renvoie `needs_input` si l'intention ou un élément directeur manque. Il réalise un choix déterministe à partir de l'intention déclarée. Le lecteur relève l'objection principale et le fait discriminant qui changerait la conclusion. En A2, s'en tenir à la question du brief et aux lacunes identifiées. Les budgets et les critères d'arrêt relèvent du mandat.

| Surface | Entrée / appel | Sortie |
| --- | --- | --- |
| Direct | JSON `request`, `claims` et relations facultatives → `python scripts/narrative_selector.py select --input FILE` | Paquet candidat. Le format court et sa revue restent autonomes. |
| A2 | Intake `narrative_profile: s3-narrative-v1` ; `request` seul dans la tentative A2 → `case_runtime.py narrative --case ID --stage A2 --request REF` | Paquet et champs de scaffold. Ajouter `kind`, `case_id`, `narrative_ref` au résultat A2. Le cas fournit les preuves A0/A1. |
| A3 | `case_runtime.py narrative --case ID --stage A3 --section SECTION_ID` | Claims d'une section, transition, relations et encarts candidats. Conserver le mapping A2 dans la composition. |
| A4 | `case_runtime.py narrative --case ID --stage A4 --findings REF` | Reçu de routage. Le résultat A4 référence le JSON des constats via `narrative_review_ref`. Les trois revues et un éventuel rendu restent exigés séparément. |
| Revue directe | `narrative_selector.py review --input PACKET --findings FINDINGS` | Collecte ciblée ou correction chez la skill propriétaire. |

Le [packet synthétique](../../../examples/narrative-selector-business.json) donne la forme exacte de `request` et de la preuve directe. Un claim matériel a une référence et un locator. Une citation attribuée conserve sa formulation, son origine et son statut. Les relations vers des claims hors du paquet restent signalées par leur ID. Le reçu `coverage` distingue passages chargés, omissions et motif d'arrêt. A0 et les revues portent la qualité réelle de la lecture : les comptes du paquet sont déclarés par l'auteur.

Chaque `classification` documente un pilier principal et des rattachements secondaires facultatifs. Un pilier nul demande un motif. Les claims avec motif et ceux restant à examiner ont deux traces distinctes. `required_pillars` vient du mandat. `scale`, `dimension` et `domain_layer` sont des axes distincts. La couche transverse et la généralisation à tous les graphes restent à éprouver. Voir les [frontières de classement](../../../references/causal-pillars.md).

## Tronc et encarts

La section porte les preuves de sa conclusion. Un encart candidat réutilise ses claims : `section_id`, `anchor_claim_id` dans `claim_ids`, objection, limite et `return_hook`. Les types historiques restent lus par leur route épinglée. Tout nouvel encart passe par la revue éditoriale et le binding du support avant affichage.

| Type | Libellé pour le lecteur | Usage |
| --- | --- | --- |
| `reality_check` | Contrôle terrain | Cas, mécanisme observé, limite de généralisation |
| `peer_signal` | Signal pair | Acteur, mouvement et portée pour l'entité |
| `scale_shift` | Changement d'échelle | Maille de départ, rupture, effet sur la décision |
| `tradeoff_matrix` | Matrice d'arbitrage | Options crédibles sur les mêmes critères |
| `deep_mechanism` | Décryptage | Deux explications et le fait qui les départage |

## Lecture et boucle de correction

Rédiger la conclusion en tête. Développer une idée par phrase. Choisir une formulation affirmative fidèle aux preuves. Conserver le sens d'un résultat négatif, d'une limite ou d'une citation. Un diagramme explicite le type de lien ; une navigation ou une hypothèse ne prouve pas une relation causale.

Un constat contient `kind`, `observation`, `ref`, `action` et `exit_test`. Types : `missing_source`, `claim`, `pillar_coverage`, `scaffold`, `prose`, `render`. `ref` désigne un claim, une section, `mandate`, `coverage` ou `render`. Une liste vide signifie « aucun écart déclaré » ; les trois revues demeurent distinctes. Voir [reprise et invalidation](../../../references/case-process.md).
