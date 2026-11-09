# Ontologie de la KB documentaire — décision d'architecture

Statut : **proposé, implémenté en lecture seule**. Aucun GO produit. Référentiel : `ontology/ontology-v1.json` (version 0.1.0). Code : `ontology.py`, intégré dans la section `ontology` de `loopback.py`.

## 1. Pourquoi une ontologie

Le graphe grandit par apports. Sans référentiel commun, trois dérives deviennent invisibles :

- un titre compté comme assertion (constaté sur la fixture : 4 titres sur 15 atomes, zéro alerte avant ce travail) ;
- une instruction contenue dans une source qui devient un fait candidat ;
- une relation probatoire ajoutée sans preuve, ou entre des types incompatibles.

L'ontologie nomme les types, fixe les domaines et codomaines des liens, et rend ces dérives observables. Elle ne corrige rien.

## 2. Héritage et différences

Le référentiel `kb-ontology` du dépôt Candidatures-nice (privé, commit `1a33eeb`) sert de méthode, pas de données. Repris :

| Élément source | Adaptation ici |
|---|---|
| Classes `<class>.<type>` | Cinq classes : `assertion`, `instruction`, `structure`, `evidence`, `analysis`. |
| Classes de relations distinctes (dont `causality` isolée) | Les 12 relations probatoires viennent de `contracts/relation-types.json`, pas d'une copie. `causes` exige une preuve. |
| Facettes séparées du type | `validation` et `evidence_basis` ; jamais dans le type. |
| Liste de champs non contrôlés | `uncontrolled_fields`, affichée sans être normalisée. |
| Politique d'autorité en lecture seule | Même règle : aucun réécrit, aucune fusion, aucune promotion. |

Non repris : les personas, les alertes de sourcing d'emploi, les classes de références métier.

## 3. Classes et types

| Classe | Types | Rôle | Dans la densité sémantique |
|---|---|---|---|
| `assertion` | `fact`, `question` | Contenu confrontable à une source | oui |
| `instruction` | `directive` | Phrase impérative contenue dans une source | non ; jamais promouvable |
| `structure` | `heading`, `code`, `table` | Mise en forme, sans assertion | non |
| `evidence` | `source` | Provenance (empreinte, localisateurs) | non |
| `analysis` | `pillar`, `hil`, `entity` | Organisation : piliers candidats, questions HIL, entités | HIL seulement |

Le découpage de `kb.py` produit six kinds d'atomes ; tous ont une classe. Un kind inconnu est `unclassified`, jamais deviné.

## 4. Règles de liens

Seize règles : quatre structurelles (`derived_from`, `candidate_classification`, `explicit_mention`, `addresses_pillar`) et les douze relations probatoires canoniques. Chaque règle déclare domaine, codomaine, exigence de preuve et, pour la classification, un statut `candidate*`.

Un lien hors ontologie (par exemple `source_of` du graphe de preuves) est compté à part, pas comme violation.

## 5. Densité

La densité historique (`directed_density`) reste inchangée. La densité sémantique est calculée en plus, sur les classes déclarées dans `density_scope`. Les deux valeurs ne remplacent jamais l'une l'autre, et aucune n'est un score de qualité (`is_quality_score: false`).

## 6. Déclencheurs de revue

| Déclencheur | Règle | Seuil | Statut |
|---|---|---|---|
| `hil_touched` | nœud sémantique récent classé vers un pilier porteur d'un HIL | 1 | décidé par construction, pas de calibration |
| `directive_in_material` | instruction récente dans le matériau | 1 | idem |
| `cadence_semantic` | écart de nœuds sémantiques depuis le rapport précédent | **aucun** | mesure seule, `calibration: pending_real_corpus` |

Un seuil sans calibration est refusé par le validateur du référentiel. La cadence de revue HIL reste donc une décision humaine tant que le corpus réel n'est pas mesuré.

## 7. Candidats d'alias

Même texte normalisé, au moins deux sources distinctes. Sortie : candidat seulement, `action: none`, `candidate_approval: false`, avec `requires: [source_review, counter_example_check]`. Le libellé est tronqué à 180 caractères par `kb.py` : la vérification d'homonymie est donc obligatoire.

## 8. Invariants

- Aucune écriture dans le graphe, la KB ou les contrats.
- Aucune promotion d'un atome en fait vérifié.
- Un référentiel incohérent (type inconnu, liste canonique décalée, seuil sans calibration, politique d'alias qui applique) est rejeté au chargement.
- Les tests exercent positif, négatif, et non-mutation.

## 9. Limites

- Le référentiel ne prouve ni la véracité d'une assertion, ni la pertinence d'un lien pour une question HIL.
- Le lexique de rattachement reste un lexique : ses correspondances sont des candidats.
- Les seuils de cadence ne sont pas calibrés. Toute décision à leur sujet est humaine et hors de ce dépôt.
- La KB réelle (Graph1, privée) n'est pas accessible depuis ce dépôt ; la mesure porte sur des fixtures synthétiques.

## 10. Décisions consignées

- **D13** : référentiel séparé du code, lu par `ontology.py`, versionné.
- **D14** : la relation probatoire n'est définie qu'une fois, dans `contracts/relation-types.json` ; le référentiel la référence et vérifie l'alignement.
- **D15** : `instruction.directive` n'est pas une assertion. Une instruction de la matière est signalée, jamais exécutée ni promue.
- **D16** : pas de seuil de cadence avant calibration sur corpus réel.
- **D17** : le vocabulaire d'arêtes de `loopback.py` est dérivé du référentiel, et non recopié. Constat S7 : la liste codée en dur ne contenait que 3 des 12 relations canoniques ; tout graphe utilisant `causes`, `answers` ou `enables` déclenchait à tort un `type_review`. Un test verrouille l'alignement.
- **D18** : un seuil de déclencheur n'est accepté qu'avec `calibration: human_approved` et une référence de décision (`docs/CADENCE-CALIBRATION-PROTOCOL.md`).
- **D19** : la facette `knowledge_status` (v0.2.0) reprend le vocabulaire de statut de Graph1 : `SOURCE`, `DERIVED`, `CANDIDATE`, `HUMAN_ADJUDICATED`, `UNKNOWN`, `NOT_EVALUABLE`. Une machine ne peut poser `HUMAN_ADJUDICATED` ; la règle exige une `decision_ref`. Aucun import de contenu depuis Graph1 n'est fait : le graphe de formation reste gelé et séparé.
- **D20** (v0.3.0, constat sur corpus réel) : `kb.py` rattache des titres à des piliers et à des entités par son lexique. Sur 80 pages collectées, 513 des 514 violations de la v0.2.0 avaient ce seul motif. La règle était trop stricte : un titre est un ancrage thématique. `candidate_classification` et `explicit_mention` acceptent désormais `structure.heading` ; blocs de code et tableaux restent exclus, et aucune relation probatoire n'est permise à un titre. La violation restante (une instruction classée dans un pilier) est conservée : c'est un vrai constat.
- **D21** (v0.4.0, corpus complet : 655 sources, 22 001 atomes) : après D20, 56 violations subsistaient. 42 venaient de tableaux du document R1 classés par mots-clés : un tableau porte du contenu thématique, il devient ancrage au même titre qu'un titre. Restent volontairement signalées : 5 classifications d'un bloc de code (le lexique appliqué à du code est douteux) et 9 atomes `directive` classés dans un pilier ou une entité. Ces 9 sont des faux positifs de l'heuristique de `kb.py` (phrases descriptives commençant par un infinitif ou « il faut ») : constat à relire, pas à corriger en silence.

