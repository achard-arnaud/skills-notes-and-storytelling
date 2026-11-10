# Renforcement de la KB par loopback — proposition d'adaptation

> Note du 9 novembre 2026 : le plafond de trois actions décrit ci-dessous est retiré (D32). Document conservé comme historique de spécification.

Statut : **SPEC, aucun GO_DEV**. Document public : méthode et mesures sur fixture synthétique uniquement. Rien de ce qui suit ne promeut un fait, ne fusionne un atome, ni ne modifie un contrat.

## 1. Constat : la skill n'existe pas encore dans cette forme

| Source vérifiée | Ce qu'elle couvre | Écart avec le besoin |
|---|---|---|
| Dépôt `Candidatures-nice` (privé), commit `1a33eeb`, skill `workflow/skills/run-loopback` | Diagnostic d'un **run CV** après signal ou retour humain : trace → qualification → proposition → validation sans mutation. Max trois actions, `no_change` valide. | Ne lit ni densité, ni types de nœuds, ni graphe. Pas de déclencheur de revue HIL par croissance. |
| Même dépôt, `experiments/.../01-kb-health.md` (brouillon) | Contrat de santé KB : verdicts `pass/warn/needs_human/fail/not_checked`, linters KH01–KH09. | Brouillon non promu. Ne mesure pas la densité ni la pertinence des types. |
| Même dépôt, `scripts/ontology.py` | Référentiel de classes et de types, lecture seule, cloisonné par persona. | Classifie les étiquettes ; ne mesure pas l'usage des types dans le graphe. |
| Ce dépôt, `diagnostic-complet/loopback.py` | Analyse en lecture seule : densité, isolés, doublons, types, sous-types, piliers, rapport comparable. | Pas de règle de pertinence de type ; pas de cadence de revue HIL. |
| Tickets : `skills-notes#31` (BN-09, SPEC_ONLY) ; `Candidatures-nice#341` et `#450` (fermé) | Cadrage du loopback « ≤3 actions, un patch, pas d'auto-promotion KB/template » ; diagnostic de la skill run-loopback (enrichir les évals, cas négatifs, frontière avec challenge-a1). | Aucun ticket dédié à la **KB** en tant que graphe qui grandit. |

Conclusion : les principes existent, dispersés. Une skill `reinforce-kb-loopback` doit les assembler pour le graphe documentaire.

## 2. Mesure de référence (fixture synthétique)

Chaîne exécutée à `dev` (`0bd21f1`) : Markdown synthétique → `kb.py` → `graph.json` → `loopback.py`.

| Mesure | Valeur |
|---|---|
| Nœuds / arêtes | 18 / 18 |
| Types | `atom` 15, `pillar` 2, `source` 1 |
| Sous-types d'atomes | `assertion` 10, **`heading` 4**, `question` 1 |
| Densité dirigée | 0,059 (18/306) — non interprétée comme qualité |
| Alertes | **0** ; décision `no_change` |

**Écart mesuré** : 4 atomes sur 15 sont des titres Markdown (`## …`). Ils sont comptés comme assertions dans la densité, et ne déclenchent aucune alerte. Le builder porte déjà un drapeau `structural` sur chaque atome, mais l'analyseur ne l'utilise pas. Ce cas est le premier ticket du renforcement (K2).

## 3. Principes repris du loopback candidatures, adaptés au graphe

| Principe source | Adaptation KB |
|---|---|
| Diagnostic sur signal réel, jamais systématique | Déclenchement seulement si : atomes ou sources récents explicites (`recent_ids`), ou seuil de croissance défini, ou dérive de types observée. Sinon `no_change`. |
| Observation ≠ cause ≠ hypothèse | Chaque constat est étiqueté (structurel, sémantique, hypothèse). La densité n'établit ni qualité ni causalité. |
| Au plus trois actions, un correctif | Au plus trois propositions par cycle, dont au plus une modification de type. Le reste est différé et compté. |
| Validateur = forme, pas vérité | L'analyseur vérifie la structure ; la pertinence sémantique reste une revue HIL. |
| Pas d'auto-promotion KB/template | Aucun merge, alias ou suppression appliqué. Seulement des candidats réversibles (tombstone, redirection). |
| Deux réparations max | Deux échecs identiques sur un même blocage : arrêt, réserve consignée. |
| Évals avec cas négatifs | Cas « cycle propre → no_change », « titre compté comme assertion → alerte », « fusion demandée sans source → refus ». |

## 4. Boucle proposée

1. **Déclencheur** : liste explicite d'IDs récents et/ou cadence (nombre d'atomes ou de sources ajoutés depuis le dernier rapport). Un seuil de cadence n'est qu'une **hypothèse à calibrer**, jamais une cible.
2. **Mesure** : `loopback.py graph.json --recent-id … --previous rapport-précédent.json`.
3. **Qualification** : pour chaque constat, séparer structure (isolés, doublons, références), typage (structure vs assertion), sémantique (à relire) et hypothèse.
4. **Périmètre HIL** : identifier les piliers et les HIL touchés par le matériau récent ; lister les questions à poser, sans répondre à leur place.
5. **Proposition** : au plus trois actions, par exemple :
   - reclasser des titres en nœuds `structure` ;
   - ajouter un type de nœud ou de lien au catalogue versionné (avec fixture) ;
   - signaler un alias ou un doublon candidat, avec sources et contre-exemple d'homonymie ;
   - demander une revue HIL ciblée.
6. **Validation** du reçu : forme, empreintes, aucune mutation.
7. **Décision humaine** : hors de l'outil. Le reçu porte `candidate_approval: false`.

## 5. Renforcements de types (densité et pertinence)

- **Types de nœuds** : le catalogue actuel (`source, fragment, claim, atom, pillar, hil, entity`) mélange structure et contenu. Proposition : séparer explicitement `structure` (titres, en-têtes) du contenu, avant de compter la densité.
- **Types de liens** : le catalogue de relations versionné (`contracts/relation-types.json`, 12 valeurs) distingue les liens probatoires des liens documentaires (`derived_from`, `candidate_classification`, `explicit_mention`). Proposition : mesurer la part de chaque classe par pilier, et signaler une classe absente ou surreprésentée. Pas de quota.
- **Pertinence** : un type est pertinent s'il sert une question HIL ouverte ou un pilier actif. Un type sans usage depuis N cycles est candidat à revue, pas à suppression.

## 6. Limites explicites

- Aucun seuil de densité n'est défini ; la densité n'est pas un score.
- Les seuils de cadence sont des hypothèses, à calibrer sur le corpus réel et non sur la fixture.
- L'analyseur ne peut pas juger la véracité d'un atome, ni la pertinence d'un lien pour une question HIL. Il signale ; l'humain décide.
- Aucune compaction ne supprime d'ID, de preuve ou de lignée. Un atome déprécié reste résolvable.

## 7. Négatifs à tester avant toute implémentation

| Cas | Attendu |
|---|---|
| Cycle sans matériau récent | `no_change` |
| Titre compté comme assertion | Constat structurel, pas une assertion |
| Fusion demandée sans source | Refus |
| Densité présentée comme qualité | Refus du libellé (`density_is_quality_score: false` maintenu) |
| ID récent absent du graphe | `unknown_recent_ids`, pas de devinette de date |
| Corpus privé dans un dépôt public | Refus (règle D06) |

## 8. Suite

Découpage des tickets et ordre des sprints : `docs/BACKLOG-REVIEW.md`. Ticket de suivi : `skills-notes#31` (sous-ticket créé pour cette proposition).
