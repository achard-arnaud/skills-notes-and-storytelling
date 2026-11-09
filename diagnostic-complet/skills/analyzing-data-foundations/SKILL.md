---
name: analyzing-data-foundations
description: Use when a business study must establish which information makes decisions reliable: instrumentation, quality, reference data, time, BI, ownership, access, architecture, interoperability, baselines. Make sure to use this skill whenever someone asks about qualité de données, baseline, référentiel, BI versus IA, data platform, or why a measurement is not decision-grade, even if no AI is involved.
---

# Analyser les fondations data (P-DATA)

**Question structurante** : Quelles informations rendent les décisions fiables ?
**Scope** : Instrumentation, qualité, référentiels, temporalité, BI, ownership, accès, architecture, interopérabilité.
**Exclusions** : Le besoin automatique d'IA : une donnée fiable n'appelle pas un modèle. L'automatisation comptable relève de P-CORPORATE.

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Partir de la décision : quelle question de gestion (mesurer, reporter, piloter, anticiper, optimiser) et quelle donnée la rend fiable ?
2. Auditer la baseline : une erreur de référence affaiblit tout le business case. Décrire qui la définit et qui peut la contester.
3. Vérifier temporalité, synchronisation, qualité des capteurs et des compteurs, droits d'accès et propriétaire de chaque jeu de données.
4. Séparer socle BI et modèles : la BI fournit la définition commune sans laquelle un modèle ne sera pas actionnable.
5. Noter ce qui n'est pas disponible plutôt que de supposer un volume ou un SLA : les chiffres non sourcés ne se reprennent pas.

## Qualifier les claims

Les définitions d'un référentiel fourni sont `supplied_claim`. Un volume de données, un taux de disponibilité ou un SLA sans source sont `hypothesis` ou `unknown`, jamais repris comme faits. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type affiché | Quand | Référence |
|---|---|---|
| Veille académique (`veille_academique`) | Définir 5 à 7 notions (qualité de données, référentiel, baseline, interopérabilité, ownership) avec sources. | `../side-stories-business/references/types/veille_academique.md` |
| Analyse approfondie (`analytical_focus`) | Expliquer pourquoi une mesure n'est pas décisionnelle (baseline, temporalité, accès) et ce qui la rendrait fiable. | `../side-stories-business/references/types/analytical_focus.md` |

### Problématiques types à fournir au rédacteur

- Quelle donnée rend la décision fiable ?
- Quelle baseline rend un gain attribuable ?

### Ponts types

- de la mesure au référentiel
- de la donnée au workflow

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Précis et défini : chaque terme technique est défini à sa première occurrence, les unités et les périodes sont toujours écrites. Voix de François-Pro : sobre, dense, une idée par phrase.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-DAT-01`, `EX-FOC-01`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).
