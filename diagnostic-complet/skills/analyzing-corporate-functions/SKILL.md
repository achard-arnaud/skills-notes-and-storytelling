---
name: analyzing-corporate-functions
description: Use when a business study must cover the transversal processes of the company: sales, marketing, administrative purchasing, accounting, budget, corporate finance, HR, legal, internal support. Make sure to use this skill whenever someone asks about usages corporate, back-office, commercial, finance d'entreprise, support interne or documentary assistants, and needs them kept apart from industrial operations.
---

# Analyser les fonctions corporate (P-CORPORATE)

**Question structurante** : Quels processus transverses soutiennent l'entreprise ?
**Scope** : Commercial, marketing, achats administratifs, comptabilité, budget, finance d'entreprise, RH, juridique, support interne.
**Exclusions** : Le pilotage industriel et la baseline de production (P-INDUSTRY, P-DATA). L'émission d'une facture est corporate ; la liaison contractuelle peut faire intervenir P-ECONOMICS et P-GOVERNANCE sans les fusionner.

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Lister les processus transverses par fonction et repérer ceux qui ont leur propre économie, leurs propres données et leurs propres propriétaires.
2. Pour chaque usage candidat, noter le résultat à mesurer et le garde-fou (validation humaine, traçabilité des sources, permissions).
3. Vérifier si un cas corporate est confirmé par la cible ou seulement candidat ; ne jamais le présenter comme un besoin exprimé.
4. Distinguer productivité individuelle (assistants, synthèse) et automatisation de processus (règles, intégration), car leur preuve de valeur diffère.
5. Écarter ce qui relève de l'exploitation d'actifs : s'il touche la mesure physique, c'est P-INDUSTRY.

## Qualifier les claims

Les cas candidats sont `hypothesis` ; les gains annoncés non confirmés pour la cible restent `supplied_claim`. Aucun gain n'est repris comme acquis. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type affiché | Quand | Référence |
|---|---|---|
| Exemple concret (`illustration`) | Montrer un usage transverse (commercial, finance, support interne) avec sa propre économie, séparé des usages industriels. | `../side-stories-business/references/types/illustration.md` |
| Comparatif (`comparator`) | Comparer deux manières de traiter un même processus corporate sur un critère commun (délai, contrôle, coût). | `../side-stories-business/references/types/comparator.md` |

### Problématiques types à fournir au rédacteur

- Quel processus transverse change réellement avec l'IA ?
- Quel usage corporate a sa propre économie ?

### Ponts types

- de l'usage corporate à son économie propre
- du cas au standard réutilisable

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Sobre et opérationnel : un processus, un propriétaire, un résultat mesurable, une limite. Pas de vocabulaire de démonstration technologique. Directive de style adoptée (ADR-0012) : direct, factuel, analytique, didactique ; l'essentiel d'abord ; phrases courtes ; jamais d'effet de balancement ni de double négation ; orienté décision.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-COR-01`, `EX-ILL-01`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).


## Références d’architecture conditionnelles

Pour une évolution de méthode, lire [ADR-1001](../../../docs/architecture/ADR-1001-routing-capabilities.md) et [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Le chargement RUN reste limité au contrat et au paquet de l’étape ; les principes communs ne changent pas les capacités locales.
