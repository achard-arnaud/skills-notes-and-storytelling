---
name: designing-main-story
description: Use when a business study needs its main story designed or revised, from scratch from evidence only, or iteratively against an existing canonical text: mandate, tension, reader scaffold, per-section investigation questions, collection plan, and slots for side stories. Make sure to use this skill whenever someone asks for un plan de rapport long, un fil narratif, un scaffold lecteur, la stratégie de récit, what to investigate next for a section, or how to update a study after new material, even if they only say "structure l'étude".
---

# Designing the main story

Le tronc répond au mandat ; les piliers en sont des vues analytiques ; les side stories l'éclairent. Ce skill transfère les invariants du dépôt tourisme (`storytelling-historical-travel`, `structuring-chronological-arcs`, `building-causal-bridges`) vers le cas business et renforce l'**investigation** et la **collecte** avant toute rédaction. Il ne rédige pas : la prose relève d'un rédacteur, la vérification de faits d'une revue.

## Choisir le mode

| Situation | Mode | Référence |
|---|---|---|
| Preuves disponibles, aucun texte antérieur à réutiliser | `from-scratch` | `references/from-scratch.md` |
| Un texte canonique existe et un delta (source, claim, forme) l'atteint | `iterative` | `references/iterative.md` |
| Qu'investiguer ensuite, avec quelles sources | les deux | `references/investigation.md` |

## Fil proposé (à valider par François, jamais figé)

Tension d'entreprise, puis mécanismes et choix, puis conditions de valeur, puis trajectoire proposée. C'est une proposition de lecture, pas un sommaire : le code accepte un autre nombre de sections et de piliers (`docs/PILLARS.md`).

## Procédure

1. **Cadrer le mandat** : la décision que le lecteur doit prendre, son audience, ce qui est hors périmètre. Sans décision, pas de tronc.
2. **Écrire la tension** en une phrase : ce qui change pour l'entreprise et pourquoi cela l'oblige à choisir. Le modèle de forme est `EX-NAR-01`.
3. **Poser les sections par question.** Pour chacune : question, bénéfice lecteur, points démontrés, objection, limites, transition. Une section sans objection est un exposé, pas un raisonnement.
4. **Rattacher les piliers** à ce que chaque paragraphe traite réellement, sans quota (`analyzing-*`).
5. **Planifier l'investigation** de chaque section (`references/investigation.md`) : sources, niveau de preuve visé, inconnues, condition d'arrêt.
6. **Réserver des emplacements de side stories** : pour chaque emplacement, passage d'accueil, problématique et ponts ; le skill `side-stories-business` prend le relais.
7. **Poser les gates** : qui valide quoi. La génération, la vérification mécanique, la relecture par un autre agent et l'approbation humaine sont quatre actes distincts ; aucun agent ne pose `editorial=true` au nom de François.

## Contrat

- **Entrées** : mandat, preuves (sources, fragments, claims, relations) ; en itératif, étude canonique et empreinte attendue.
- **Sorties** : scaffold lecteur (sections, ordre, claims, piliers), plan d'investigation par section, emplacements de side stories ; jamais de paragraphes en mode `from-scratch`.
- **Interdits** : réutiliser une prose antérieure en `from-scratch`, requalifier un claim, déduire un pilier d'un mot-clé, imposer huit chapitres, relever un statut de preuve par la mise en forme.

## Style indicatif

Titres de section sous forme de question ou d'affirmation à démontrer ; une idée par phrase ; marqueurs de statut visibles (Publié, Échange, Inférence, Hypothèse). Directive de style adoptée (ADR-0012) : direct, factuel, analytique, didactique ; l'essentiel d'abord ; phrases courtes ; jamais d'effet de balancement ni de double négation ; orienté décision.

## Exemples issus de la KB

`examples/kb-pointers.json` : identifiants opaques uniquement (D23).

## Modules associés

`writing.py from-scratch` et `writing.py iterative` (conservation et invalidation), `context.py` (paquets bornés), `render.py` (vue lecteur), skills `analyzing-*` (piliers), `side-stories-business` (encarts).


## Références d’architecture conditionnelles

Pour une évolution de méthode, lire [ADR-1003](../../../docs/architecture/ADR-1003-narrative-artifacts.md) et [ADR-1005](../../../docs/architecture/ADR-1005-learning-validation.md). Le chargement RUN reste limité au contrat et au paquet de l’étape ; les principes communs ne changent pas les capacités locales.
