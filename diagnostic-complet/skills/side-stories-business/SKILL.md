---
name: side-stories-business
description: Use when material from a business study (une entreprise, une offre, un marché, un mécanisme) should stay outside the main story but remain traceable, as a pitch d'acteur en 10 à 15 lignes, un lexique sourcé de 5 à 7 entrées, un dézoom, un comparatif, une illustration ou un focus analytique. Make sure to use this skill whenever someone asks for un encart, un aparté, une side story, une veille corporate ou académique, a sidebar, a company pitch, un lexique, or wants to decide which kind of side story fits a passage, even if they never say "side story".
---

# Side stories business

Une side story est un artefact de composition : elle éclaire le récit principal sans en faire partie, et elle ne crée jamais de preuve. Ce skill adapte `composing-side-stories` (dépôt tourisme) au cas business et ramène dix types hérités à **six types**, parce que peu de formats bien définis valent mieux que beaucoup de formats vagues.

La source de vérité est `diagnostic-complet/workflows/side-stories.workflow.json`. Lire d'abord ses sections `invariants`, `choice_tree` et `types`. `python3 diagnostic-complet/sidestories.py types` liste les types, leurs tags et leurs exemples.

## Les six types

| Libellé affiché | Type | Format en une ligne | Référence |
|---|---|---|---|
| Veille entreprise | `veille_corporate_perso` | Pitch d'entreprise, 10 à 15 lignes, faits datés puis lecture signée | `references/types/veille_corporate_perso.md` |
| Veille académique | `veille_academique` | Lexique de 5 à 7 entrées en cinq blocs, sources explicites | `references/types/veille_academique.md` |
| Changement d'échelle | `dezoom` | Local, canal de transmission, retour local ; 220 mots | `references/types/dezoom.md` |
| Comparatif | `comparator` | Table de 3 à 5 lignes et 5 colonnes au plus, critère commun | `references/types/comparator.md` |
| Exemple concret | `illustration` | Cas d'usage, citation, objet ou personne ; 150 mots | `references/types/illustration.md` |
| Analyse approfondie | `analytical_focus` | Question, thèse, deux positions, mécanismes avec statut de preuve | `references/types/analytical_focus.md` |

Anciens types : `detour`, `also`, `portrait`, `object_focus`, `callback` deviennent `illustration` ; `method` devient `veille_academique` ; `false_lead` devient `analytical_focus`. Ils restent acceptés pour les études existantes mais ne se créent plus. Un rappel (callback) est un champ `bridge.callback_to`, utilisable sur tout type.

## Procédure

1. **Recevoir un candidat** d'un skill de pilier : type probable, problématique, passage d'accueil, claims. Sans problématique ni passage, demander au skill de pilier de les produire ; ne pas les inventer, car une side story sans question dérive vers l'anecdote. Si le texte du passage n'est pas fourni, en demander deux phrases clés avant d'écrire les liens avec le passage : un « à confirmer » dans une entrée ne rend aucun service au lecteur.
2. **Choisir le type** avec `choice_tree`. Écrire une ligne qui dit pourquoi les deux types voisins ne conviennent pas : c'est le critère de choix qui manquait aux premiers inventaires.
3. **Construire le paquet de rendu** : voir `references/renderer-packet.md`. Le rédacteur ne reçoit que ce paquet.
4. **Rédiger** au format du type (fichier de référence du type, squelette JSON compris). Un type, une ligne éditoriale : un encart mixte devient deux side stories.
5. **Auto-cohérence** : une passe indépendante, qui ne voit que le texte, reformule problématique et ponts ; les écarts se réparent au plus deux fois, puis le candidat est marqué bloqué avec la preuve.
6. **Valider mécaniquement** : `python3 diagnostic-complet/runtime.py validate etude.json`. Les erreurs ne concernent que les états `validated` et `promoted` ; pour `candidate`, ce sont des lacunes à lire.
7. **Remettre à François.** Seul un humain fait passer un encart à `validated`. Un test vert n'est pas une approbation éditoriale.

## Contrat

- **Entrées** : candidat (type, problématique, passage, claims), claims et sources existants, extrait de `workflows/side-stories.workflow.json`.
- **Sorties** : un enregistrement `side_stories[]` au format de l'étude (`diagnostic-complet/docs/INTERFACES.md`), avec `problematique`, `bridge.in`, `bridge.out`, `reason_outside`, `payoff`, `claim_ids`, `payload` ; état `candidate`.
- **Interdits** : créer un fait, relever un statut de preuve par la mise en forme, mélanger compte et offre, reconstituer une citation, copier du texte du corpus privé dans le dépôt, marquer `validated`.

## Style indicatif

Sobre, dense, une idée par phrase, chiffres datés et sourcés, conditionnel pour toute hypothèse. Le détail par type est dans les fichiers de référence ; il oriente la rédaction et ne se vérifie pas mécaniquement.

## Exemples issus de la KB

`examples/kb-pointers.json` liste des identifiants d'atomes opaques par type. Les résoudre dans le dépôt Graph1 privé (chemin indiqué dans `workflows/kb-examples.json`) ; ne jamais recopier leur texte ici (D23). Les exemples dont le statut est `to_collect`, `to_ingest`, `research_required` ou `to_confirm` ne sont pas utilisables tels quels.

## Hors périmètre

Qualifier les piliers (skills `analyzing-*`), rédiger le tronc (`designing-main-story`), rendre le HTML (`render.py`).
