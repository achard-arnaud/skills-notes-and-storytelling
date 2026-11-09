---
name: analyzing-economics-and-financing
description: Use when a business study must show who finances, who pays, who captures value and who bears risk: business model, asset financing, unit economics, cash, TCO, ROI, value thresholds, attributable savings. Make sure to use this skill whenever someone asks about ROI, baseline économique, seuil de valeur, CAPEX, financement de projets, business case, or why a promised gain is not yet an attributable saving.
---

# Analyser l'économie et le financement (P-ECONOMICS)

**Question structurante** : Qui finance, paie, capte la valeur et porte le risque ?
**Scope** : Modèle économique, financement des actifs, unité économique, cash, TCO, ROI.
**Exclusions** : L'automatisation comptable corporate (P-CORPORATE). Une promesse de gain n'est pas une économie attribuable.

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Écrire qui finance, qui détient l'actif, qui porte le risque d'exécution et de performance, sur quelle durée contractuelle.
2. Pour chaque gain annoncé, établir la baseline, le mode d'attribution et la condition de réinvestissement (un temps libéré n'agit sur le compte de résultat que s'il est réinvesti).
3. Appliquer un filtre de valeur minimale avant de chiffrer un cas, et choisir une métrique propre à chaque cas : production d'un actif et temps gagné sur un assistant n'ont pas le même modèle de preuve.
4. Séparer délai de première valeur, délai de retour, coût marginal d'un nouveau cas et effet de réutilisation d'une brique.
5. Ne reprendre aucun montant de concurrent, de ROI ou de taux sans source publique.

## Qualifier les claims

Un montant publié par l'entreprise est `attributed_claim`. Un gain estimé est `hypothesis`. Un seuil de valeur issu d'un ouvrage est `supplied_claim` tant qu'il n'est pas retrouvé avec sa page. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type | Quand | Référence |
|---|---|---|
| `[FOC]` `analytical_focus` | Démonter une promesse de gain : baseline, attribution, seuil de valeur, conditions de réinvestissement. | `../side-stories-business/references/types/analytical_focus.md` |
| `[CMP]` `comparator` | Comparer des modèles économiques ou des niveaux d'investissement sur un critère commun (CAPEX, risque porté, délai de première valeur). | `../side-stories-business/references/types/comparator.md` |
| `[DZ]` `dezoom` | Passer de l'économie d'un cas à celle du portefeuille (coût marginal par nouveau cas, réutilisation). | `../side-stories-business/references/types/dezoom.md` |
| `[VAC]` `veille_academique` | Définir TCO, ROI, délai de retour et seuil de valeur avec leur source et leur limite. | `../side-stories-business/references/types/veille_academique.md` |

### Problématiques types à fournir au rédacteur

- Qui finance, qui capte la valeur, qui porte le risque ?
- À partir de quel seuil un cas vaut-il d'être financé ?

### Ponts types

- du gain annoncé à l'économie attribuable
- du cas local à l'économie de portefeuille

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Comptable de forme : unités, périodes et hypothèses toujours écrites ; aucune ligne de gain sans sa baseline. Voix de François-Pro : sobre, dense, une idée par phrase.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-ECO-01`, `EX-DZ-02`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).
