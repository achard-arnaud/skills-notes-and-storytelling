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

## Mandat éditorial — 9 novembre 2026 (D22 à D26)

- Piliers et trame validés par François pour la première passe (#258). Side stories à rechallenger : inventaire réécrit dans `workflows/side-stories.candidates.json`, aucun encart validé.
- **Source de vérité des side stories** : `workflows/side-stories.workflow.json`. Six types (veille entreprise, veille académique, changement d'échelle, comparatif, exemple concret, analyse approfondie), libellé lisible affiché au lecteur, format et ligne éditoriale par type. Les codes courts du workflow sont internes et ne figurent jamais dans une sortie finale ; éviter les abréviations inutiles. Ne pas redéfinir un type ailleurs ; changer un type = workflow + `tests/test_sidestories.py` + ce fichier.
- Toute side story validée ou promue porte `problematique`, `bridge.in` et `bridge.out`, et son `payload` respecte le format du type. `runtime.py validate` le contrôle ; pour un candidat, ce sont des lacunes.
- Dix skills éditoriaux sont versionnés dans `skills/` (carte : `docs/SKILLS-MAP.md`) : un par pilier, `designing-main-story` et `side-stories-business`. Ils ne contiennent aucun texte du corpus privé ; leurs exemples de la KB sont des identifiants opaques (`workflows/kb-examples.json`). Les `SKILL.md` des douze opérations atomiques restent hors dépôt.
- Chaque type de side story a un **jumeau synthétique** (`fixtures/examples/`) : les tests et les évaluations n'utilisent que lui, jamais le corpus privé (D25, D26).
- Un agent ne marque jamais une side story `validated` : seul François le fait, une à la fois.
- Commits `[skip ci]`, contrôles locaux (`docs/LOCAL-GATE.md`), aucune promotion `main`.

## Périmètre léger (9 novembre 2026)

- Ce sous-projet reste **léger et non intégré** au framework racine. Il ne modifie ni `templates/`, ni `modes/`, ni le routage des skills racine (one-pager, two-pager, etc.). Vérifiable : aucun commit de ce sous-projet ne touche un chemin hors de `diagnostic-complet/` (`git diff --stat <base> -- . ':!diagnostic-complet'` doit être vide).
- Il porte un type de rapport plus long, le **rapport business**. Ce type **coexiste** avec les autres types : il ne remplace, ne renomme ni ne migre aucun de ces types.
- Le rapport business reste candidat. Il n'entre dans `templates/manifest.json` qu'après approbation humaine et fixture passante, selon la règle racine.

## Invariants (détail dans les documents cités)

- **Build / run** : code et référentiels run-agnostiques. Le vocabulaire de run vit dans `profiles/` ; une KB est liée à un seul profil. Règles complètes : `docs/RUN-BUILD-BOUNDARY.md`, qui prévaut sur les autres formulations.
- **Terminologie** : statuts, tiers et correspondances viennent de `ontology/terminology.json` uniquement (`docs/TERMINOLOGY.md`). Une source vendeur (T2) ou corporate (T1) ne soutient jamais un `verified_fact`.
- **Refactor** : chaque constat de couplage est un ticket `RF-nn` dans `docs/REFACTOR-BACKLOG.md`, avec sa preuve de clôture.
- **Process** : pas de CI sur `dev`. Gate local avant tout push :
  ```bash
  python3 -m unittest discover -s diagnostic-complet/tests -p 'test_*.py'
  python3 scripts/validate_contracts.py
  python3 diagnostic-complet/ontology.py check
  ```
  Le résultat se déclare comme `ci: intentionally_not_run`.
- **Push** : fast-forward uniquement, jamais de force. Si `origin/dev` a changé, rebaser ses seuls commits locaux puis repousser.
- **Pull request** : la PR #285 a été fusionnée dans `main` le 9 novembre à 23:51 par le compte du dépôt (passée en prête puis fusionnée en 5 secondes ; pas un agent). Le suivi est dans la PR draft #290. Un agent ne merge jamais une PR.
