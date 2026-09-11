# Les 4 couches découplées

Le skill sépare 4 couches indépendantes. Chaque template les décline dans sa propre section "Couches" (voir `templates/<template>.md`). Une modification dans une couche ne doit jamais forcer une modification silencieuse dans une autre — c'est la garantie de découplage.

## Couche 1 — Template
Objectif de la note, longueur cible, niveau de détail, stratégie de collecte d'info, organisation des nodes. Portée : `templates/manifest.json` + `references/template-catalog.md` + le fichier `templates/<template>.md` lui-même.

## Couche 2 — Storytelling / stratégie narrative
Le registre des méthodes narratives connues ([narrative-frameworks.md](narrative-frameworks.md)) et le(s) framework(s) que le template utilise par défaut. Indépendante du contenu factuel : deux notes sur des sujets opposés peuvent partager la même stratégie narrative.

## Couche 3 — Scaffold / claims / fragments
Registre claims/fragments/structure et son versioning, règles de retrieving/reranking ([retrieval-and-reranking.md](retrieval-and-reranking.md)), typologie des nodes, gestion des side stories ([side-stories-retro.md](side-stories-retro.md)).

### Typologie des nodes : généralisation par rapport au repo historique
Le repo historique (`tourisme-etude-historico-geographique`) structure ses nodes selon une **logique causale unique** (cause → conséquence, arcs chronologiques). Le repo business **généralise** cette structure : les edges du claims graph light (`supports`, `contradicts`, `qualifies`, `causes`, `depends_on`, `compares_to`, `answers`, `motivates`, voir workflow.md) couvrent une pluralité de logiques — stratégique (`depends_on`, `motivates`), narrative (`answers`), preuve/claim (`supports`, `contradicts`, `qualifies`), et seulement partiellement causale (`causes`). Ne jamais réduire un claims graph business à un unique enchaînement causal : un même claim peut être simultanément motivé par une logique stratégique et challengé par une logique de preuve, sans relation de causalité directe entre les deux.

## Couche 4 — Rédaction & préférences de format
Tone of voice, longueur, langue(s), contrôle du vocabulaire en cohérence avec l'objectif de la note, cohérence linguistique (éviter franglais et novlangue business excessive), gestion des éléments de mise en page (bas de page, en-têtes, etc.). Portée : [style-contract.md](style-contract.md), complété ci-dessous.

### Vocabulaire — règle générale
- Note business/formation destinée à un lecteur non technique : bannir le jargon d'implémentation (noms de frameworks, appels API, termes d'infra) sauf s'il est le sujet même de la décision ; préférer l'effet business ("réduit le délai de mise en marché de X semaines") au mécanisme technique.
- Note technique (ex. `ARCHITECTURE_NOTE`) : le vocabulaire technique précis est attendu et doit être exact — ne pas édulcorer un terme d'architecture pour "faire simple" si cela introduit une ambiguïté.
- Dans tous les cas : éviter le franglais évitable (dire "feuille de route" plutôt que "roadmap" quand un équivalent français courant existe) et la novlangue business creuse ("synergiser", "impact positif" sans métrique, "best-in-class" sans preuve) — préférer une formulation directe et vérifiable.

### Mise en page
- En-tête : nom du destinataire/contexte de décision, date, version.
- Bas de page : numérotation, mention de statut (draft/final), source de la donnée si la page contient un tableau chiffré.
- Cohérence : mêmes styles de titres/tableaux sur tout le document (contrôlé par le rendu DOCX, voir style-contract.md).

## Déclinaison par template

| Template | Couche 1 (objectif/longueur) | Couche 2 (frameworks par défaut) | Couche 3 (typologie de nodes dominante) | Couche 4 (vocabulaire) |
|---|---|---|---|---|
| `ARCHITECTURE_NOTE` | Comprendre architecture/risques/économie, 5-10 pp, détail élevé, collecte technique+business | `ghost_deck`, `pyramid_principle`, `signal_to_noise` | mixte causale (mécanisme) + preuve (fiabilité des chiffres) | technique attendu, précis |
| `ONE_PAGER` | Orientation exécutive rapide, 1 p, détail minimal, collecte = 3-5 faits clés | `pyramid_principle`, `action_titles`, `signal_to_noise` | preuve/claim uniquement, pas de causalité développée | non technique, direct |
| `TWO_PAGER` | Synthèse dense entreprise/produit/personne, 2 pp, détail moyen | `mece`, `action_titles` | preuve/claim + comparaison | non technique, dense mais direct |
| `BENCHMARKING` | Comparaison cohérente d'options, 2-6 pp, détail élevé sur les critères | `mece`, `pyramid_principle`, `action_titles` | comparaison (`compares_to`) dominante | vocabulaire de critère homogène entre options, non technique sauf critère technique explicite |
| `BUY_SIDE_GAP_ANALYSIS` | Décision adopter/remplacer/compléter/partenariat, 4-8 pp | `mece`, `pyramid_principle` | preuve/claim + comparaison + dépendance (`depends_on` pour migration) | technique modéré (nécessaire pour la matrice de gap), toujours traduit en impact business |
| `DIAGNOSTIC_RECO_SELL_SIDE` | Positionnement et motion commerciale vendeur, 5-9 pp | `ghost_deck`, `pyramid_principle`, `signal_to_noise` | stratégique (`motivates`, `depends_on`) dominante | non technique, orienté marché/vente |
| `OPPORTUNITY_NOTE_ICP` | Décider si une cible est une opportunité crédible, 4-8 pp | `pyramid_principle`, `mece` | stratégique + preuve, gates explicites | non technique, orienté décision/sponsor |
