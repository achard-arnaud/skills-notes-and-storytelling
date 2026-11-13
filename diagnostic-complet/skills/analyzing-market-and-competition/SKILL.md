---
name: analyzing-market-and-competition
description: Use when a business study must explain why a company has to evolve: macro and sector forces, competitive archetypes, value-capture models, sector constraints. Make sure to use this skill whenever someone asks pourquoi l'entreprise doit évoluer, une analyse de marché, de concurrence, de Porter, des archétypes d'acteurs, or a benchmark of players, even if they only say "contexte marché".
---

# Analyser le marché et la concurrence (P-MARKET)

**Question structurante** : Pourquoi cette entreprise doit-elle évoluer ?
**Scope** : Macro, marché, concurrence, Porter si utile, contraintes sectorielles.
**Exclusions** : Une capacité interne déjà acquise (P-INDUSTRY, P-CORPORATE) ; tout chiffre de performance d'un concurrent sans source publique.

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Partir du mandat : quelle décision le lecteur doit-il prendre ? Écrire la tension macro en une phrase avant de collecter.
2. Collecter trois niveaux : macro (statistiques officielles), mezzo (résultats et priorités publiés par l'entreprise), micro (pages offre, cas). Marquer chaque fait Publié, Échange, Inférence ou Hypothèse.
3. Décrire des archétypes avant de nommer des acteurs : proximité et contrat, financement et cycle de vie, exploitation physique, couche numérique. Les noms viennent ensuite.
4. Pour les concurrents, comparer sur un critère commun ; ne noter ni intensité d'IA, ni disponibilité, ni ROI sans source publique.
5. Traiter un indicateur national (adoption d'une technologie par pays) comme contexte de marché, jamais comme mesure de maturité de la cible.

## Qualifier les claims

Les communications de l'entreprise sont `supplied_claim` ou `attributed_claim` ; une synthèse fournie reste `supplied_claim`. Un classement de concurrents reste `hypothesis` tant qu'aucune source publique ne l'établit. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type affiché | Quand | Référence |
|---|---|---|
| Comparatif (`comparator`) | Situer la cible face à 3 à 5 acteurs sur un même critère de création de valeur. | `../side-stories-business/references/types/comparator.md` |
| Changement d'échelle (`dezoom`) | Passer du site au portefeuille puis au marché quand un indicateur local ne s'explique que par la structure sectorielle. | `../side-stories-business/references/types/dezoom.md` |
| Veille entreprise (`veille_corporate_perso`) | Présenter un acteur clé du marché (concurrent, partenaire, fournisseur) à partir de ses signaux publics. | `../side-stories-business/references/types/veille_corporate_perso.md` |
| Veille académique (`veille_academique`) | Installer une notion de stratégie ou d'économie industrielle avec sa source et sa limite. | `../side-stories-business/references/types/veille_academique.md` |

### Problématiques types à fournir au rédacteur

- Pourquoi cet acteur doit-il évoluer maintenant ?
- Quel archétype d'acteur capte la valeur dans cette chaîne ?

### Ponts types

- du constat sectoriel à la décision de la cible
- de la comparaison au critère de choix

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Macro factuelle : chiffres datés avec année et périmètre, formulations comparatives symétriques, aucune hiérarchie d'acteurs implicite. Directive de style adoptée (ADR-0012) : direct, factuel, analytique, didactique ; l'essentiel d'abord ; phrases courtes ; jamais d'effet de balancement ni de double négation ; orienté décision.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-MKT-01`, `EX-CMP-01`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).


## Références d’architecture conditionnelles

Pour une évolution de méthode, lire [ADR-1001](../../../docs/architecture/ADR-1001-routing-capabilities.md) et [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Le chargement RUN reste limité au contrat et au paquet de l’étape ; les principes communs ne changent pas les capacités locales.
