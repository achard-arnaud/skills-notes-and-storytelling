# Diagnostic complet — enquête business et récit long

Prototype isolé : mandat → enquête fragmentée → preuves → scaffold lecteur → paragraphes → side stories → vues HTML. Les piliers sont transverses ; ni pagination ni sommaire prédéfini. Le corpus réel reste privé, ce dépôt public ne contient que méthode et démonstration synthétique.

## Reprendre le run

1. Lire [runs/bootstrap/RESUME.md](runs/bootstrap/RESUME.md), puis [BOARD.md](BOARD.md).
2. Lire seulement l'issue et le paquet de la prochaine tâche ; vérifier empreintes et prérequis.
3. Produire artefact, validation et reçu avant de changer le statut. Aucun état humain ne découle d'un test.

## Points d'entrée

- [Plan détaillé, 72 microétapes](docs/PLAN.md) et [board JSON](board.json).
- [Transfert Sri Lanka](docs/SOURCE-TRANSFER.md), [audit cible](docs/BUSINESS-TRANSFER.md), [ownership](docs/OWNERSHIP.md).
- [Piliers candidats](docs/PILLARS.md), [recherche](docs/RESEARCH.md), [narration](docs/NARRATIVE.md), [interfaces](docs/INTERFACES.md).
- [Protocole de contexte](docs/CONTEXT-PROTOCOL.md), [intake privé](docs/INTAKE-POLICY.md), [décisions](docs/DECISIONS.md).
- [Workflow des side stories](workflows/side-stories.workflow.json), [candidats](workflows/side-stories.candidates.json), [carte des skills](docs/SKILLS-MAP.md), [skills éditoriaux](skills/).

## Commandes locales

Depuis ce dossier, consulter `python runtime.py --help`, `python context.py --help`, `python render.py --help` pour les commandes exactes de la version courante. Vérifier : `python -m unittest discover -s tests -v`. Depuis la racine du dépôt : `python scripts/validate_contracts.py`.

L'import conserve les localisateurs et ne promeut aucun fait. Le renderer matérialise une étude ; il ne rédige pas automatiquement un rapport. Le graphe est local, sans DB ni GraphRAG. Le contexte est géré par paquets/checkpoints, sans worker permanent ni compaction technique forcée. Les tokens exacts du runtime restent inconnus.

## Livraison

Branche d'intégration dev, commits `[skip ci]`, contrôles locaux ; aucune promotion main. Le suivi réel est GitHub Issues + fichiers versionnés, pas une instance Jira/Projects. Les choix éditoriaux business restent candidats en attente de validation.
