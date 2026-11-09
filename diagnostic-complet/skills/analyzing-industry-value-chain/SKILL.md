---
name: analyzing-industry-value-chain
description: Use when a business study must explain how the physical value chain creates and loses value: studies, assets, operations, maintenance, supervision, field work, subcontracting. Make sure to use this skill whenever someone asks about exploitation d'actifs, O&M, sous-performance, télémaintenance, diagnostic terrain, supervision multi-sites, or a field-to-decision flow, even if the word industrie is absent.
---

# Analyser la chaîne de valeur industrielle (P-INDUSTRY)

**Question structurante** : Comment la chaîne de valeur physique crée-t-elle et perd-elle de la valeur ?
**Scope** : Études, actifs, exploitation, maintenance, supervision, terrain, sous-traitance.
**Exclusions** : Les fonctions corporate générales (P-CORPORATE). Une fiche fournisseur ne prouve ni déploiement, ni intégration, ni ROI chez la cible.

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Cartographier la chaîne d'exécution de bout en bout : site, étude, financement, construction, exploitation, mesure, optimisation. Repérer où chaque maillon produit une donnée différente.
2. Décrire le flux signal vers décision : signal, détection et confiance, impact estimé, criticité contractuelle, diagnostic distant, décision d'intervention, habilitations, pièces, contrôle de retour à la normale, preuve.
3. Séparer ressource, équipement, donnée et modèle, exploitation et maintenance, site et réseau, contrat et économie quand on explique une perte de performance (grille générique, pas un incident de la cible).
4. Demander à chaque outil de supervision ce qu'il prouve : un monitoring observe, il ne supprime pas l'intervention physique ni les contraintes d'accès.
5. Noter ce que le terrain sait et que la plateforme ignore (accès, sécurité, habilitations).

## Qualifier les claims

Les cas décrits par l'entreprise sont `attributed_claim` ; les causes de sous-performance d'une grille générique sont `inference`. Une dépendance de l'équipement à un fournisseur est `hypothesis` tant que les droits sur la donnée ne sont pas établis. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type | Quand | Référence |
|---|---|---|
| `[FOC]` `analytical_focus` | Traiter un mécanisme d'exploitation trop étroit pour une section : diagnostic de sous-performance, arbitrage entre alerte et déplacement. | `../side-stories-business/references/types/analytical_focus.md` |
| `[ILL]` `illustration` | Faire voir un équipement, une mesure, un document de maintenance ou un cas d'usage terrain. | `../side-stories-business/references/types/illustration.md` |
| `[DZ]` `dezoom` | Relier une anomalie locale à la logique de portefeuille ou à la dépendance à un fournisseur d'équipement. | `../side-stories-business/references/types/dezoom.md` |
| `[VCP]` `veille_corporate_perso` | Présenter une offre de supervision ou un éditeur d'outil d'exploitation, sans prétendre à un déploiement chez la cible. | `../side-stories-business/references/types/veille_corporate_perso.md` |

### Problématiques types à fournir au rédacteur

- Pourquoi un actif sous-performe-t-il et qui le sait à temps ?
- Quelle alerte justifie un déplacement ?

### Ponts types

- du signal à la décision d'intervention
- de l'installation au portefeuille

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Descriptif et séquentiel : chaînes causales nommées étape par étape, vocabulaire d'exploitation stable, aucune métrique sans définition. Voix de François-Pro : sobre, dense, une idée par phrase.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-FOC-01`, `EX-VCP-01`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).
