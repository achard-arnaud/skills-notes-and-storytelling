# Carte des skills, du workflow et des étapes de `AGENTS.md`

Deux familles coexistent. Les **douze opérations atomiques** (`docs/SKILLS-CATALOG.md`, générées par `skills_catalog.py`) enveloppent des modules de ce dossier ; leurs `SKILL.md` restent hors dépôt (mandat R2). La **famille éditoriale** de dix skills vit dans `skills/` (D23) et porte les règles de rédaction ; elle ne contient aucun texte du corpus privé.

Aucun dossier `.skills/` n'existe dans ce dépôt. Les skills éditoriaux sont dans `diagnostic-complet/skills/` ; le dossier racine `skills/` contient un skill sans rapport (`pedagogical-ai-learning`).

## Étapes obligatoires (`AGENTS.md` racine) et couverture

| Étape | Skill éditorial | Opération atomique ou module | Remarque |
|---|---|---|---|
| mode | `designing-main-story` | | Choix `from-scratch` ou `iterative` |
| research | `designing-main-story` (investigation), `analyzing-*` | `corporate-crawl`, `source-convert` | Plan d'investigation par section |
| fragments | | `evidence-import`, `kb-ingest` | Import avec localisateurs, sans promotion |
| claims graph light | `analyzing-*` (qualifier) | `pillar-qualify`, `ontology-check`, `reinforce-kb-loopback` | Statuts de claims, jamais de promotion |
| rerank | | | Non couvert par ce sous-projet |
| scaffold | `designing-main-story` | `writing-fresh`, `writing-iterative`, `context-packet` | Scaffold lecteur, pas de prose |
| fill | | | Rédaction externe ; ce sous-projet ne rédige aucun fait |
| side stories | `side-stories-business` | `runtime.py validate` | Types, formats, paquet de rendu |
| sourcing | `analyzing-*` | `kb-ingest` | Références citables, pointeurs opaques |
| layout | | `reader-render` | HTML lecteur, tag visible par type |
| DOCX QA | | | Aucun DOCX produit ici ; toute sortie DOCX suit `tests/QA_CHECKLIST.md` |
| nudging, feedback/dreaming | | | Non couvert |

## Piliers, skills et side stories

| Pilier | Skill | Types de side stories recommandés (identifiants internes) |
|---|---|---|
| P-MARKET | `analyzing-market-and-competition` | `comparator`, `dezoom`, `veille_corporate_perso`, `veille_academique` |
| P-INDUSTRY | `analyzing-industry-value-chain` | `analytical_focus`, `illustration`, `dezoom`, `veille_corporate_perso` |
| P-CORPORATE | `analyzing-corporate-functions` | `illustration`, `comparator` |
| P-DATA | `analyzing-data-foundations` | `veille_academique`, `analytical_focus` |
| P-AI | `analyzing-ai-capabilities` | `veille_academique`, `analytical_focus`, `comparator`, `veille_corporate_perso` |
| P-ECONOMICS | `analyzing-economics-and-financing` | `analytical_focus`, `comparator`, `dezoom`, `veille_academique` |
| P-GOVERNANCE | `analyzing-governance-and-control` | `dezoom`, `veille_academique`, `illustration` |
| P-ADOPTION | `analyzing-adoption-and-change` | `illustration`, `veille_academique`, `comparator` |

Cette table reprend `pillar_routing` du workflow ; `tests/test_sidestories.py` vérifie qu'elles ne divergent pas. Les piliers restent des hypothèses de travail validées pour la première passe (#258) et peuvent être scindés ou fusionnés sans changer le moteur.

## Anatomie d'un skill éditorial (format skill-creator)

```text
skills/<nom>/
├── SKILL.md                 frontmatter name + description, corps sous 500 lignes
├── references/              chargées à la demande (types, modes, paquet de rendu)
├── examples/kb-pointers.json   un à deux exemples de la KB, identifiants opaques
└── evals/<cas>/             prompt.md, case.yaml, graders/ (format claude plugin eval)
```

Les cas d'évaluation sont écrits, pas exécutés : aucune exécution comparée avec et sans skill n'a été faite à ce stade.

## Origine et adaptation

| Source (dépôt tourisme, épinglé au commit lu) | Adaptation |
|---|---|
| `composing-side-stories`, `docs/SOP_SIDE_STORIES.md` | `side-stories-business` : dix types ramenés à six, paquet de rendu, auto-cohérence |
| `analyzing-*` (six domaines, HIL) | Huit skills de pilier business, avec problématiques et ponts par type |
| `zooming-geographic-scales` | Type `dezoom` à échelles business |
| `building-causal-bridges` | Ponts d'entrée et de sortie, et gate « tronc ou side story » |
| `storytelling-historical-travel` (contrat problème d'abord) | `designing-main-story` |
| `structuring-chronological-arcs` | Fil proposé : tension, mécanismes, conditions de valeur, trajectoire |

## Garde-fous communs

- Une side story ne crée aucune preuve ; la réalité du compte et la vérité de l'offre restent séparées jusqu'à un fit explicite.
- Les exemples de la KB sont des **identifiants opaques** : le texte du corpus privé ne se copie ni dans un skill, ni dans une issue, ni dans le dépôt (D06, D23).
- Un test local vert n'est ni une relecture par un agent ni une validation humaine.
- Commits de ce sous-projet en `[skip ci]` ; le gate local est dans `docs/LOCAL-GATE.md`.
