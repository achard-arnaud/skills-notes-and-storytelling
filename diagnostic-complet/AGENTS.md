# Diagnostic complet — espace expérimental isolé (AGENTS v2, 9 novembre 2026)

Sous-projet méthodologique du dépôt business. Il fournit du code et des référentiels **run-agnostiques** ; les corpus et les runs vivent ailleurs (Graph1, namespace du profil). Ce fichier est lu par tout agent avant action.

## 0. Bootstrap de l'agent (ordre obligatoire)

1. Ce fichier, puis `README.md`.
2. `runs/r2/RESUME.md` : état fiable du run courant. Puis `docs/R2-RESULTS.md` : chiffres réels, comptes agrégés seulement.
3. `docs/REFACTOR-BACKLOG.md` : tickets ouverts et clôturés, avec leur preuve.
4. `ontology/terminology.json` (vocabulaire unique) et `profiles/` (vocabulaire de run). Avant tout code qui manipule statuts, tiers ou entités.
5. Seulement ensuite le paquet de la tâche active (`context.py packet`). Ne jamais relire tout le dépôt par défaut.
6. Vérifier les empreintes déclarées (SHA du graphe gelé, SHA de base, hashes d'entrées) avant d'agir. Une empreinte différente arrête la reprise.

## 1. Mandat courant

- Mandat R2 (7 novembre 2026, `docs/R2-SCOPE.md`) : douze opérations atomiques, skills personnelles hors dépôt, projection Graph1 du namespace business.
- Instruction du 9 novembre 2026 : séparation build/run complète, terminologie centralisée, skill `reinforce-kb-loopback`, tickets de refactor, push fast-forward sur `dev` sans CI.
- Le mandat initial du 7 novembre (« aucune installation de skill ») est **superseded** par R2 : les skills existent, en circuit personnel, jamais versionnées ici.
- Aucune promotion sur `main`. Aucune décision humaine n'est prise par un agent.

## 2. Design pattern : séparation build / run (MUST)

- **M1 — Build run-agnostique.** Les modules `*.py`, `ontology/*.json` et `contracts/` ne contiennent aucun nom de client, de run, d'entité, de pilier, de namespace ni de décision de run.
- **M2 — Vocabulaire de run dans `profiles/` uniquement.** Lexique d'entités, piliers et namespace de projection vivent dans `profiles/<profile_id>.profile.json`. Le profil `neutral` est le défaut du code.
- **M3 — Une KB, un profil.** L'index `kb.json` porte `profile_id`. Mélanger deux profils dans un index est refusé. Une migration est explicite (RF-06).
- **M4 — Pas de namespace par défaut.** La projection exige `--namespace` ou le `projection.namespace` d'un profil.
- **M5 — Terminologie unique.** Tous les statuts de claim, tiers de source, états de validation et correspondances `knowledge_status` sont dans `ontology/terminology.json`. Aucun module ne redéfinit ces chaînes. Un terme nouveau = modification de ce fichier + test d'alignement.
- **M6 — Second profil obligatoire.** `profiles/synthetic-logistics.profile.json` reste valide. Il prouve que le build ne dépend d'aucun run réel.
- **M7 — Garde-fou par test.** `tests/test_profiles_terminology.py::test_core_code_contains_no_run_vocabulary` échoue si un terme de run apparaît dans le code de build. Ne jamais l'affaiblir pour faire passer un test.
- **M8 — Documents de run à part.** `runs/<run>/`, `docs/R2-*` et les résultats de run peuvent nommer le run. Le code et les référentiels ne le peuvent pas.
- **M9 — Décision référencée.** Tout seuil, toute calibration, tout `HUMAN_ADJUDICATED` exige un `decision_ref` (`docs/DECISIONS.md`). Une machine ne pose jamais `HUMAN_ADJUDICATED`.
- **M10 — Une règle n'est pas une décision.** Une règle de graphe qui attribue une responsabilité, déclenche une action ou change une posture reste un **candidat** dans le profil, avec son statut de calibration. Elle n'est jamais appliquée automatiquement.
- **M11 — Changement de contrat.** Modifier un statut, un tier, une relation ou une règle exige une fixture de non-régression, un test et une entrée dans `docs/DECISIONS.md`.

## 3. Interdits (DON'T)

- **D-1** Coder une valeur de run par défaut (namespace, lexique, entité, pilier).
- **D-2** Définir un statut, un tier ou une relation hors de `terminology.json` ou `contracts/relation-types.json`.
- **D-3** Tenir une auto-déclaration vendeur ou corporate pour un fait. Elle reste un `attributed_claim` (tier T1 ou T2).
- **D-4** Inférer une responsabilité, une décision ou une posture depuis la structure d'un graphe.
- **D-5** Fusionner, supprimer, réaffecter un identifiant, ou réécrire un corpus déjà publié.
- **D-6** Écrire du corpus, des transcripts, des `SKILL.md` ou des données privées dans ce dépôt public.
- **D-7** Versionner un `SKILL.md`. Le contrat (`docs/REINFORCE-KB-SKILL-CONTRACT.md`) est versionné ; la skill vit en circuit personnel.
- **D-8** Présenter un PASS local comme un PASS CI, ou une densité comme une mesure de qualité.
- **D-9** Pousser en force, pousser sur `main`, ou merger une PR.
- **D-10** Relancer la projection Graph1 sans reçu de la passe précédente et sans `--profile` explicite.

## 4. Process (sans CI sur dev)

- **P1 — Gate local obligatoire avant tout push.** La CI sur `dev` est volontairement désactivée (`[skip ci]`). Le gate local remplace la CI :
  ```bash
  python3 -m unittest discover -s diagnostic-complet/tests -p 'test_*.py'
  python3 scripts/validate_contracts.py
  python3 diagnostic-complet/ontology.py check
  ```
  Le résultat est déclaré dans le message de commit et le reçu : `ci: intentionally_not_run`.
- **P2 — Fast-forward uniquement.** `git push -u origin dev`. En cas de rejet : `git fetch origin dev`, intégrer par fast-forward ou rebase des seuls commits locaux, puis repousser. Jamais de `--force`. Retry réseau seulement : 2, 4, 8, 16 secondes.
- **P3 — PR draft.** Après un push, si aucune PR ouverte n'existe pour la branche, ouvrir une PR **draft** vers `main` (règle opérateur). Un agent ne la merge jamais.
- **P4 — Commits.** Préfixe `feat|fix|docs|test(diagnostic):`, suffixe `[skip ci]`, footer `Claude-Session`. Aucun identifiant de modèle dans un commit, une PR ou un fichier poussé.
- **P5 — Tickets de refactor.** Chaque constat de couplage ou de dérive est une entrée `RF-nn` dans `docs/REFACTOR-BACKLOG.md`, avec statut et preuve de clôture (un test). Les items « backlog » sont aussi suivis en GitHub Issues.
- **P6 — Reçus.** Tout changement de KB, de graphe ou de projection produit un reçu dans `runs/<run>/receipts/`, lié au SHA de base.
- **P7 — Empreintes.** Toute entrée d'une reprise est nommée par son SHA-256 dans un checkpoint ; une entrée modifiée rend la reprise refusée (`context.py resume-check`).

## 5. Revue de cette version (v1 → v2)

| Point relevé en v1 | Correction |
|---|---|
| Pas de bootstrap ordonné : l'agent pouvait commencer par le code | Section 0 : lecture ordonnée, vérification des empreintes |
| Séparation build/run décrite, non contrainte : `kb.py` et `project.py` embarquaient GreenYellow | M1 à M8, tests de garde-fou, RF-01 à RF-05 |
| « Interdit : installer une skill » (7 novembre), contredit par R2 | Mandat daté et superseded explicitement (section 1) |
| Pas de règle de process sans CI ; PR et « sans PR » contradictoires avec la règle opérateur | P1 à P3 : gate local, fast-forward, PR draft non mergée |
| Terminologie éparpillée (statuts, tiers, facettes) | M5, `ontology/terminology.json`, RF-03, RF-04 |
| Règles de graphe présentées comme logique métier | M10, D-4 |

Le `AGENTS.md` racine (framework des modes et templates) n'est pas modifié : ses règles de changement de template et de mode ne sont pas déclenchées par ce travail.

## 6. Mandat éditorial du 9 novembre 2026 (D22 à D26)

- Piliers et trame validés par François pour la première passe (#258). Side stories à rechallenger : inventaire réécrit dans `workflows/side-stories.candidates.json`, aucun encart validé.
- **Source de vérité des side stories** : `workflows/side-stories.workflow.json`. Six types (veille entreprise, veille académique, changement d'échelle, comparatif, exemple concret, analyse approfondie), libellé lisible affiché au lecteur, format et ligne éditoriale par type. Les codes courts du workflow sont internes et ne figurent jamais dans une sortie finale ; éviter les abréviations inutiles. Ne pas redéfinir un type ailleurs ; changer un type = workflow + `tests/test_sidestories.py` + ce fichier.
- Toute side story validée ou promue porte `problematique`, `bridge.in` et `bridge.out`, et son `payload` respecte le format du type. `runtime.py validate` le contrôle ; pour un candidat, ce sont des lacunes.
- Dix skills éditoriaux sont versionnés dans `skills/` (carte : `docs/SKILLS-MAP.md`) : un par pilier, `designing-main-story` et `side-stories-business`. **Exception à D-7, décidée par François le 9 novembre 2026 (D23)** : ils ne contiennent aucun texte du corpus privé ni aucun nom de run ; leurs exemples sont des jumeaux synthétiques (`fixtures/examples/`) et des identifiants opaques résolus côté exécution. Les `SKILL.md` des douze opérations atomiques restent hors dépôt.
- Séparation exécution/construction : `docs/RUN-BUILD-BOUNDARY.md` (D25, D26). Un jumeau synthétique par type de side story ; aucun test ne lit le corpus privé.
- Un agent ne marque jamais une side story `validated` : seul François le fait, une à la fois.
- Commits `[skip ci]`, gate local de la section 4, aucune promotion `main` : la fusion de la PR #285 dans `main` n'a pas été faite par un agent.
