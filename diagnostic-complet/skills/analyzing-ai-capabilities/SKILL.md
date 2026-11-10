---
name: analyzing-ai-capabilities
description: Use when a business study must say which intelligence or automation is useful to a decision: perception, prediction, optimization, generation, agents, evaluation, supervision, and the adoption postures that fit. Make sure to use this skill whenever someone asks about cas d'usage IA, RAG, agents, LLM versus ML, capabilities, postures stratégiques, or how to compare AI solutions, even if they never mention a pillar.
---

# Analyser les capacités d'IA utiles (P-AI)

**Question structurante** : Quelle intelligence ou automatisation est utile à la décision ?
**Scope** : Perception, prédiction, optimisation, génération, agents, évaluations, supervision ; solutions conditionnées par la donnée et le workflow.
**Exclusions** : Un effet de mode : le choix technique s'explique par la décision à prendre. Le déploiement et les compétences relèvent de P-ADOPTION.

Un pilier est une vue analytique, pas un chapitre ni un quota : on le mobilise quand la question traitée est la sienne, pas quand un mot-clé apparaît. Le rattachement lexical reste candidat (D20, D21) ; la décision revient à François.

## Investiguer

1. Associer chaque besoin métier à un mode d'IA (perception, création, prédiction, raisonnement, agentique) plutôt qu'à un produit.
2. Distinguer trois familles d'usage : productivité et service, opérationnel sur données physiques, multimodal au service des intervenants ; leur preuve de valeur et leur risque diffèrent.
3. Placer le cas sur son niveau d'intégration et d'automatisation avant de le chiffrer ; commencer par assistants et copilotes pour valider la valeur à faible risque.
4. Examiner les postures d'adoption (opportuniste, centre d'expertise, produit, pari) comme un portefeuille hybride, pas comme des étapes obligatoires.
5. Toute action qui touche sécurité, contrat, paiement ou consigne exige validation et journalisation : l'écrire dans la solution.

## Qualifier les claims

Une capacité décrite par un fournisseur est `supplied_claim`. Un gain d'IA non mesuré chez la cible est `hypothesis`. Les étiquettes de synthèse d'une posture ne sont pas des intitulés canoniques d'ouvrage : retrouver la référence avant de citer. Aucun claim n'est promu en `verified_fact` sans revue déclarée.

## Renvois side stories

Lire `../side-stories-business/SKILL.md`, puis le fichier du type retenu. Types recommandés pour ce pilier :

| Type affiché | Quand | Référence |
|---|---|---|
| Veille académique (`veille_academique`) | Installer les capacités de l'IA ou les postures d'adoption avec source et contre-point. | `../side-stories-business/references/types/veille_academique.md` |
| Analyse approfondie (`analytical_focus`) | Instruire une architecture ou un mécanisme (RAG agentique multimodal, base de connaissances à ontologie, double cerveau) par la décision qu'il sert. | `../side-stories-business/references/types/analytical_focus.md` |
| Comparatif (`comparator`) | Comparer des postures ou des solutions sur un critère unique (contrôle, réversibilité, valeur attendue). | `../side-stories-business/references/types/comparator.md` |
| Veille entreprise (`veille_corporate_perso`) | Présenter un éditeur, un cabinet ou un retour d'expérience d'IA en 10 à 15 lignes, offre et preuves séparées. | `../side-stories-business/references/types/veille_corporate_perso.md` |

### Problématiques types à fournir au rédacteur

- Quelle capacité d'IA répond à cette décision ?
- Quelle posture d'adoption convient à ce stade ?

### Ponts types

- de la capacité au cas d'usage
- du cas d'usage à la supervision humaine

Fournir au rédacteur le **paquet de rendu** (`../side-stories-business/references/renderer-packet.md`) : type, passage d'accueil, problématique, `bridge.in`, `bridge.out`, claims et statuts, interdits. Le rédacteur le vérifie en mode auto-cohérence. Une side story sans problématique ni ponts n'est pas rédigée.

## Contrat

- **Entrées** : mandat, claims et sources du pilier, passage du tronc concerné.
- **Sorties** : claims candidats avec statut, lacunes et inconnues, candidats de side stories avec type, problématique et ponts.
- **Interdits** : promouvoir un fait, déduire un pilier d'un mot-clé, reprendre un chiffre non sourcé, écrire une side story à la place de `side-stories-business`, mélanger la réalité du compte et la vérité de l'offre.

## Style indicatif

Neutre sur la technologie, exigeant sur la décision : une capacité ne s'écrit jamais sans le cas, la donnée requise et la supervision. Directive de style adoptée (ADR-0012) : direct, factuel, analytique, didactique ; l'essentiel d'abord ; phrases courtes ; jamais d'effet de balancement ni de double négation ; orienté décision.

## Exemples issus de la KB

`examples/kb-pointers.json` : `EX-VAC-01`, `EX-VAC-02`. Identifiants opaques à résoudre dans le dépôt Graph1 privé (voir `workflows/kb-examples.json`) ; ne jamais copier leur texte ici (D23).
