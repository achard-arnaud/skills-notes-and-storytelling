---
name: analyzing-adoption-and-change
description: Use when a business study must show how an organization turns a tool into a lasting practice: skills, roles, change, training, usage, value measurement, communities, support. Make sure to use this skill whenever someone asks about adoption, conduite du changement, communautés de pratique, centre d'expertise, passage du POC à l'usage, or how to avoid a proof-of-concept factory, even without the word adoption.
---

# Analyser l'adoption et le changement (P-ADOPTION)

**Question structurante** : Comment l'organisation transforme-t-elle un outil en pratique durable ?
**Scope** : Compétences, rôles, changement, formation, usages, mesure de valeur.
**Exclusions** : Un taux d'adoption supposé : ne jamais en inventer. Le choix de la capacité (P-AI) et la gouvernance (P-GOVERNANCE).

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Distinguer deux flux : ascendant (irritants et idées du terrain) et descendant (thèses de valeur issues de la stratégie), puis décrire où ils convergent.
2. Classer chaque demande terrain : donnée manquante, friction dans un outil existant, besoin autonome, décision de portefeuille.
3. Décrire les rôles (collaborateurs, power users, développeurs citoyens, data et IT) avec, pour chacun, sa fonction et sa mesure de valeur.
4. Définir un pipeline de la remontée à la réutilisation, avec une décision explicite à chaque étape : continuer, corriger, réutiliser ou arrêter.
5. Mesurer l'amélioration du travail et la conversion de besoins en capacité durable, pas le nombre de licences.

## Qualifier les claims

Un dispositif d'accompagnement décrit est `attributed_claim` ; son efficacité est `hypothesis`. Aucun taux d'adoption n'est supposé : sans mesure, `unknown`. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type affiché | Quand | Référence |
|---|---|---|
| Exemple concret (`illustration`) | Montrer un cas où un irritant terrain devient une capacité réutilisable, ou un dispositif d'accompagnement. | `../side-stories-business/references/types/illustration.md` |
| Veille académique (`veille_academique`) | Définir les notions de conduite du changement et de pratique durable (cadre d'augmentation des processus, par exemple) avec source. | `../side-stories-business/references/types/veille_academique.md` |
| Comparatif (`comparator`) | Comparer deux dispositifs d'adoption (communauté, centre d'expertise, produit) sur un critère commun. | `../side-stories-business/references/types/comparator.md` |

### Problématiques types à fournir au rédacteur

- Comment un outil devient-il une pratique durable ?
- Quel dispositif transforme un irritant en capacité réutilisable ?

### Ponts types

- de l'essai à la pratique
- du pilote à la réutilisation

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Humain et concret : des rôles, des gestes, des décisions ; une mesure par rôle, jamais un taux global sans définition. Directive de style adoptée (ADR-0012) : direct, factuel, analytique, didactique ; l'essentiel d'abord ; phrases courtes ; jamais d'effet de balancement ni de double négation ; orienté décision.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-ADO-01`, `EX-VAC-02`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).


## Références d’architecture conditionnelles

Pour une évolution de méthode, lire [ADR-1001](../../../docs/architecture/ADR-1001-routing-capabilities.md) et [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Le chargement RUN reste limité au contrat et au paquet de l’étape ; les principes communs ne changent pas les capacités locales.
