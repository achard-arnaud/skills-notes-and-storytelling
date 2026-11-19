# ADR-1009 — Cinq skills métier et un socle d’analyse commun

- Date de décision : 18 novembre 2026.
- Statut : direction S3 et cinq frontières métier approuvées explicitement par François. Trajectoire d’implémentation et recette par tranche. Cet ADR complète les [ADR-1004](ADR-1004-run-build-context.md), [ADR-1007](ADR-1007-study-workflow.md) et [ADR-1008](ADR-1008-executable-cases-and-decision-profiles.md), dont les statuts historiques restent lisibles.
- Suivi : [#294](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/294).

## Décision

Retenir S3. Maintenir cinq skills distinctes pour les questions business, produit, techniques, pédagogiques et réglementaires. Choisir la méthode d’après la question, puis le support d’après le lecteur et son usage. Une étude peut faire appel à plusieurs domaines en nommant le propriétaire de chaque question. Les résultats, preuves, inconnues et contradictions restent attachés à l’étude et peuvent alimenter plusieurs templates.

Conserver le moteur de cas et les mécanismes d’analyse, d’invalidation, de rédaction et de revue existants. Un `SKILL.md` court décrit le déclenchement, les frontières et les étapes utiles. Un manifeste propre à chaque domaine indexe les méthodes et leurs références. Les cinq manifests partagent une forme minimale et des identifiants distincts. Ajouter une règle locale lorsque le métier impose une véritable différence d’entrée, d’analyse ou de contrôle. Le catalogue de templates conserve l’autorité sur ses versions et adaptateurs.

## Séparation RUN et BUILD

Le RUN de production épingle le BUILD publié, ses méthodes sélectionnées et ses contrats. Il garde ses sources, budgets, états, reçus et livrables dans son dossier privé sous `data/cases/`. GreenYellow R2 continue sur sa route et dans son espace historique jusqu’à une reprise contrôlée. La recette candidate utilise un cas synthétique distinct. Le BUILD part de `dev`, utilise des fixtures synthétiques et versionne seulement les méthodes, contrats, code et validations. Un défaut observé en RUN ouvre un écart BUILD borné, avec preuve expurgée.

Le dépôt Candidatures-nice fournit le précédent utile : un RUN épinglé et un BUILD séparé, la validation des transitions et la capacité de rendu déclarée par template. Le présent moteur et ses artefacts restent l’autorité. [ADR RUN/BUILD de Candidatures-nice au SHA consulté](https://github.com/achard-arnaud/Candidatures-nice/blob/caf129b7c0037bf0a21562585fb5dae290632153/docs/ADR-007-RUN-BUILD.md)

## Mise en œuvre et arbitrage de l’arborescence

| Proposition | Application |
| --- | --- |
| Méthodes encapsulées et réutilisables | Une référence propriétaire par méthode. Une ressource existante peut servir plusieurs formats par ses références. Garder la disposition des fichiers proportionnée à l’usage. |
| Entrées, état partagé et orchestration | Utiliser le plan et l’enveloppe existants, le graphe, les context packets et les reprises. Le rendu intervient après le binding des résultats aux blocs. |
| Gouvernance des sources et du budget | Le mandat fixe le budget du cas. La méthode précise les exigences probatoires. Une restriction technique exige un consommateur qui l’applique et un test qui le vérifie. |
| Loopback et évaluateurs | Réutiliser les reprises et revues existantes. Une lacune, une contradiction ou un contrôle échoué déclenche une révision ciblée. Un vote de réponses ou un score arbitraire ne décide pas de la force des preuves. |
| Fixtures et vérification | Tester les résultats observables, la provenance, le retraitement ciblé et les invariants indépendants. Préserver les contre-exemples. Les assertions de fond et la qualité du rendu font l’objet de revues dédiées. |
| Plusieurs supports | Garder les templates dans leur catalogue, les adaptateurs au point de composition et les ressources de présentation au point de rendu. |

Le chargement progressif, les noms et descriptions explicites, les références et assets facultatifs ainsi que les liens de dossiers sous `.agents/skills` suivent les mécanismes documentés de Codex. Une arborescence identique et complète dans chaque skill ajouterait des fichiers sans consommateur. Porter, l’adoption ou la qualification d’une clause ne nécessitent chacun un paquet plus lourd que lorsqu’un usage l’établit. [Documentation officielle Codex Skills](https://developers.openai.com/codex/skills/)

## Alternatives et critère de réexamen

S2 fournit le bon modèle de chargement ciblé et de méthodes réutilisables. Dans [la sonde contractuelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/297#issuecomment-6964085319), il a préservé l’inconnue causale dans les deux longueurs avec moins d’octets de méthode consultés. S3 ajoute le refus d’un point de reprise périmé et l’invalidation des dépendances. La sonde n’établit ni gain de temps ni supériorité éditoriale de S3. Cinq moteurs métier autonomes multiplieraient les reprises et contrats. La position retenue reprend le chargement conditionnel de S2 et le moteur existant de S3.

Commencer par une analyse utile à GreenYellow. La même révision alimente un brief et le rapport long. Après correction d’une preuve, vérifier les deux projections, les inconnues, les dépendances et la stabilité d’une branche indépendante. Un recoupement ancien devient une référence, ou sort de la route active après inventaire des appelants, équivalence éprouvée, version restaurable et validation du cas. Réexaminer la séparation si un changement de template oblige à réexécuter le fond ou si la gestion des références coûte davantage que la reprise qu’elle évite.

Voir [le plan d’intégration GreenYellow et la revue du backlog](../planning/S3-GREENYELLOW-INTEGRATION.md).

## Raccord au PRD #258

Les cinq skills gardent la propriété du fond et réemploient un sélecteur commun après le choix de profondeur. Voir le [PRD canonique](../specifications/PRD-258-selecteur-narratif.md) et [ADR-1010](ADR-1010-narrative-selection.md).
