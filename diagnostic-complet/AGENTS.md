# Diagnostic complet — espace expérimental isolé

Le mandat utilisateur du 7 novembre 2026 autorise ce sous-projet, son code et ses validations locales, l'intégration fast-forward sur dev avec [skip ci]. Aucun changement global de template/mode, aucune promotion main, aucune installation de skill ni activation d'automation.

- Séparer recherche/navigation, preuve, scaffold lecteur, narration et rendu.
- Les piliers sont des vues analytiques à pertinence explicite, pas des chapitres obligatoires ni des quotas.
- Séparer industrie/opérations sectorielles et fonctions corporate transverses ; data et IA restent distinctes.
- Le lecteur suit le mandat. Les side stories ont provenance, raison hors tronc, payoff et retour résolvable.
- Les validations mécaniques ne constituent pas une approbation éditoriale humaine.
- Ce dépôt est public : méthodes et fixtures synthétiques uniquement. Les conversations, R1 et apports privés restent hors Git et hors issues publiques.
- Un agent écrit uniquement ses chemins délégués ; le coordinateur est seul writer des refs Git et du board consolidé.
- Pour reprendre : README.md, runs/bootstrap/RESUME.md, puis le seul paquet de tâche requis.

## Mandat courant R2 — 7 novembre 2026

Le mandat R2 supersède l'interdiction initiale de création de skills : douze opérations personnelles atomiques sont autorisées via skill-creator, sans copier leurs SKILL.md dans le dépôt public. Workflows initiaux/itératifs, loopback, atomisation, collecte corporate et projection privée Graph1 sont autorisés. Voir docs/R2-SCOPE.md et runs/r2/board.json. Les corpus restent privés. Une correction du catalogue de relations canonique est autorisée avec fixture de non-régression ; aucun template/mode/rendu global n'est changé.

## Mandat éditorial — 9 novembre 2026 (D22 à D24)

- Piliers et trame validés par François pour la première passe (#258). Side stories à rechallenger : inventaire réécrit dans `workflows/side-stories.candidates.json`, aucun encart validé.
- **Source de vérité des side stories** : `workflows/side-stories.workflow.json`. Six types (`veille_corporate_perso` [VCP], `veille_academique` [VAC], `dezoom` [DZ], `comparator` [CMP], `illustration` [ILL], `analytical_focus` [FOC]), tag visible, format et ligne éditoriale par type. Ne pas redéfinir un type ailleurs ; changer un type = workflow + `tests/test_sidestories.py` + ce fichier.
- Toute side story validée ou promue porte `problematique`, `bridge.in` et `bridge.out`, et son `payload` respecte le format du type. `runtime.py validate` le contrôle ; pour un candidat, ce sont des lacunes.
- Dix skills éditoriaux sont versionnés dans `skills/` (carte : `docs/SKILLS-MAP.md`) : un par pilier, `designing-main-story` et `side-stories-business`. Ils ne contiennent aucun texte du corpus privé ; leurs exemples de la KB sont des identifiants opaques (`workflows/kb-examples.json`). Les `SKILL.md` des douze opérations atomiques restent hors dépôt.
- Un agent ne marque jamais une side story `validated` : seul François le fait, une à la fois.
- Commits `[skip ci]`, contrôles locaux (`docs/LOCAL-GATE.md`), aucune promotion `main`.
