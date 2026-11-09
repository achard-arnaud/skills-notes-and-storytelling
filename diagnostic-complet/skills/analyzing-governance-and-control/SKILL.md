---
name: analyzing-governance-and-control
description: Use when a business study must say who can decide, control and answer for results: mandate, responsibilities, risk, security, compliance, human oversight, dependencies, reversibility. Make sure to use this skill whenever someone asks about gouvernance IA, lock-in fournisseur, droits sur les données, rôles groupe pays site, contrôle humain, réversibilité or supervision, even if the word governance is not used.
---

# Analyser gouvernance et contrôle (P-GOVERNANCE)

**Question structurante** : Qui peut décider, contrôler et répondre des résultats ?
**Scope** : Mandat, responsabilités, risques, sécurité, conformité, contrôle humain, dépendances, réversibilité.
**Exclusions** : Le choix d'outil lui-même (P-AI) et le déploiement des compétences (P-ADOPTION).

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Écrire l'organisation de la décision : qui décide, qui exécute, qui contrôle, à quelle échelle (groupe, pays, site).
2. Cartographier les dépendances : interfaces, droits sur les données, accès aux API, sortie et réversibilité. Une plateforme excellente sur un équipement ne connaît pas le contrat ni les autres équipements.
3. Identifier les actions qui exigent validation humaine et journalisation (sécurité, contrat, paiement, consigne).
4. Vérifier le rôle de la DSI, de la plateforme data et des équipes métier dans l'organisation cible ; ne rien supposer.
5. Distinguer risque de lock-in avéré, hypothèse stratégique et préférence de fournisseur.

## Qualifier les claims

Un avantage d'indépendance ou d'orchestration est `hypothesis` à valider. Un rôle organisationnel non confirmé est `unknown`. Une règle de conformité citée sans texte est `supplied_claim`. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type affiché | Quand | Référence |
|---|---|---|
| Changement d'échelle (`dezoom`) | Passer de la dépendance technique (interface, droits sur les données) à la dépendance contractuelle et stratégique. | `../side-stories-business/references/types/dezoom.md` |
| Veille académique (`veille_academique`) | Définir contrôle humain, réversibilité, supervision et conformité avec source et contre-point. | `../side-stories-business/references/types/veille_academique.md` |
| Exemple concret (`illustration`) | Montrer un cas de décision partagée entre groupe, pays et site, ou une citation de dirigeant sur la responsabilité. | `../side-stories-business/references/types/illustration.md` |

### Problématiques types à fournir au rédacteur

- Qui peut décider, contrôler et répondre ?
- Quelle dépendance fournisseur est réversible ?

### Ponts types

- de la dépendance technique au contrôle contractuel
- du contrôle humain au rôle défini

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Juridiquement prudent : qui, quoi, jusqu'où ; chaque responsabilité nomme son titulaire, jamais « l'organisation ». Voix de François-Pro : sobre, dense, une idée par phrase.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-DZ-01`, `EX-GOV-01`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).
