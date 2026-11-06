# Reprise — bootstrap terminé, choix éditoriaux candidats

Mandat du 7 novembre 2026 : sous-projet isolé, 72 microétapes, huit epics et quatre phases. Infrastructure, plan et validations locales livrés ; intégration dev sans CI. Aucune promotion main. Source `fb83e0e759d1fef78bbb2cca766fecbb23eda8d5`, base cible `74a6354a4aeb128ade6db951073eeb825efca0a6`. SHA du code dans DELIVERY.md ; reçu final distant dans l'issue #177.

## État fiable

Board JSON : 72 tâches vérifiées avec reçus individuels. 47 tests locaux PASS (18 contexte, 20 preuve/import, 9 HTML), validateur canonique PASS ; contrats/manifests racine inchangés. Reprise indépendante effectuée et écarts du premier passage corrigés. QA visuelle bloquée par environnement ; contrôles statiques seulement. Suivi réel GitHub Issues + Markdown, pas Jira/Projects.

## Prochaine décision : issue #258

François valide ou ajuste les piliers, la trame et les premières side stories candidats. Les huit HIL source ne dictent pas huit chapitres ni huit piliers cibles. Industrie/corporate et data/IA restent distincts. Consulter uniquement docs/PILLARS.md et docs/NARRATIVE.md pour cette décision, puis le paquet du premier slice retenu.

Après décision, résoudre conversation/annonce/R1 et futurs apports dans leurs sources ; importer dans l'espace privé, qualifier les propositions puis élaborer un scaffold lecteur et rédiger par paragraphes. Ne pas relancer un import global ni lire tout le dépôt à chaque tâche.

## Limites conservées

Deux documents accessibles ont été essayés en privé : 190 blocs textuels localisés, non encore atomisés sémantiquement ; un slice de six paragraphes et trois encarts est candidat. Aucun fait automatiquement vérifié. La conversation liée n'est pas intégralement récupérée ; transcript et annonce originale à vérifier. Aucun corpus privé dans Git/issues.

Les paquets comptent mots/octets des seules entrées déclarées ; instructions racine/routées/compagnons à énumérer. Tokens système/historique inconnus. `--for-execution` exige ready/running et dépendances satisfaites au moment du contrôle ; ce snapshot n'acquiert pas de verrou. Writer unique, scopes et réparations bornées restent un protocole coordonné. Drop logique, pas de purge ni de compaction technique forcée. Tests et revues agents ne valent pas validation humaine.
