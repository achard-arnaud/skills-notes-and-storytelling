# ADR-0010 — Détection des directives : marqueurs non ambigus

- **Statut** : accepté ; migration des atomes existants à planifier
- **Date** : 2026-11-10 (consignation ; décisions d'origine ci-dessous)
- **Décisions liées** : D35 (#288)
- **Tickets** : #288, RF-09

## Contexte

La règle `directive` attrapait des infinitifs (analyser, utiliser, lire) et des formes indicatives (« il faut », « doit »). Selon le constat du run, neuf atomes classés directive dans un pilier ou une entité sont des faux positifs, sur dix-huit directives au total.

## Décision

Seuls des marqueurs sans ambiguïté déclenchent une directive : « tu dois », « vous devez », « merci de », « please », « must », « ignore/oublie » suivi d'un déterminant, et les impératifs pluriels en -ez. Les infinitifs et les impératifs singuliers ne suffisent plus.

## Conséquences

Le cas « Analyse les données. » devient une assertion : c'est le prix de la précision. L'identifiant d'un atome dépend de son type : reclasser un atome existant crée un nouvel identifiant. La migration des atomes existants doit donc garder les occurrences résolvables ; elle exige un accès au corpus et un reçu (RF-09, #288).
