# Composition du rapport long

Index pour les humains. Les règles que les agents appliquent vivent dans des fichiers structurés ; ce document ne les redéfinit pas.

| Besoin | Fichier lu par l'agent |
|---|---|
| Types, formats, tags, lignes éditoriales, paquet de rendu, auto-cohérence, routage par pilier | `workflows/side-stories.workflow.json` (source de vérité, lue par `sidestories.py`, `runtime.py`, `render.py`) |
| Candidats de side stories réécrits (objectif, problématique, ponts, critère de choix) | `workflows/side-stories.candidates.json` |
| Exemples issus de la KB (identifiants opaques) | `workflows/kb-examples.json` |
| Procédure par rôle | skills de `skills/` (carte : `docs/SKILLS-MAP.md`) |
| Contrat d'étude (JSON) | `docs/INTERFACES.md` |

## Du mandat au paragraphe

Le mandat borne la décision à éclairer. L'arc propose une démonstration ; les piliers en fournissent les vues analytiques. Le scaffold lecteur fixe les questions successives, la tension, les objections, les transitions et les emplacements latéraux. Chaque paragraphe a une fonction identifiable et consomme un paquet local de claims/fragments/relations ; le remplissage n'est pas un résumé global relancé à chaque passe. Procédure : skill `designing-main-story`.

Pour chaque section, conserver question, bénéfice lecteur, points démontrés, objection, limites et transition. Pour chaque paragraphe, conserver texte, claims mobilisés, piliers pertinents, état de revue et empreinte. Un paragraphe réécrit perd son verdict éditorial précédent. La vérification d'un fait peut rester valide si sa source et son scope n'ont pas changé ; une source infirmée invalide ses descendants.

La génération, la vérification mécanique, la revue par un autre agent et l'approbation humaine sont quatre actes distincts. Le prototype contrôle des liens et des empreintes ; il ne sait pas approuver la qualité argumentative à la place du lecteur. Les tests ne doivent jamais poser `editorial=true` au nom de François.

## Side stories

Une side story explique pourquoi elle est hors du tronc, ce qu'elle apporte, où elle se place et où elle ramène. Cycle de vie : candidate, validated, promoted, retired, sans passage automatique par le rendu. Une illustration n'est pas une nouvelle preuve.

Six types, tag visible, format et ligne éditoriale propres à chacun (détail dans le workflow) :

| Tag | Type | Format |
|---|---|---|
| `[VCP]` | `veille_corporate_perso` | Pitch d'entreprise, 10 à 15 lignes |
| `[VAC]` | `veille_academique` | Lexique de 5 à 7 entrées, cinq blocs par entrée |
| `[DZ]` | `dezoom` | Trois temps, 220 mots |
| `[CMP]` | `comparator` | Table de 3 à 5 lignes, 5 colonnes au plus |
| `[ILL]` | `illustration` | Cas d'usage, citation, objet ou personne, 150 mots |
| `[FOC]` | `analytical_focus` | Question, thèse, deux positions, mécanismes, enseignement |

Les anciens types (`detour`, `also`, `portrait`, `object_focus`, `callback`, `method`, `false_lead`) sont regroupés ; ils restent acceptés pour les études existantes (D22). Le contrat local reste plus strict sur les retours que le dépôt donneur, par décision d'expérimentation.

## Inventaire des side stories

Réécrit après le retour du 2026-11-09 (D24) dans `workflows/side-stories.candidates.json`. Cet inventaire est un ensemble de pistes, pas une liste d'encarts à produire : chaque candidat porte son objectif, son type, une alternative avec le critère de choix, sa problématique, ses ponts et son état de préparation dans la KB. Aucun n'est validé.

## Couverture et profondeur

Une disposition explicite rend les absents visibles : inclus dans le tronc, inclus en side story, recherche requise, différé ou non retenu avec motif. Un graphe dense ou `unaccounted=0` ne prouve ni qualité ni profondeur. Ne jamais raccourcir une limite matérielle uniquement pour passer un budget de contexte : scinder la tâche.

## Visuels

Le diagramme doit rendre une relation exacte plus claire. Mermaid conserve les relations typées et les limites ; le prototype peut fournir la source lisible sans prétendre exécuter un moteur Mermaid. Ne pas transformer une flèche de navigation ou une hypothèse en causalité certaine. Le tag d'un type de side story est toujours affiché en texte ; la couleur le renforce sans le remplacer, et le vert, l'orange et le rouge restent réservés aux statuts de preuve.
