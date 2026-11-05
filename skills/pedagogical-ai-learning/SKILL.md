---
name: pedagogical-ai-learning
description: Build beginner-friendly, evidence-grounded six-page “Pour aller plus loin” learning sheets for enterprise AI, with a separate content binding, semantic HTML scaffold and downstream visual renderer. Use for the 17-pillar AI-in-business learning programme, Train-the-Trainer kits, capability explainers and multicapability case studies.
template_class: pedagogique
template_type: ai-enterprise-learning-six-page
---

# Skill — fiches pédagogiques IA en entreprise

## Mission

Transformer un corpus de référence et une question de formation en une fiche modulaire de six pages. Le lecteur doit pouvoir comprendre l'idée sans bagage technique, l'expliquer à une équipe, repérer les conditions d'adoption et choisir un petit essai responsable. Le livrable éditorial n'est pas le rendu visuel.

## Entrées et frontières

Lire le brief, les modules concernés des 17 piliers, les sources réellement accessibles et le contrat [pedagogical-binding.schema.json](../../contracts/pedagogical-binding.schema.json). Créer trois objets séparés :

1. **Binding contenu** — audience, capacité, source ledger, contenu rédigé, use cases et notes.
2. **Scaffold HTML sémantique** — six pages et blocs HTML ordonnés, selon [pedagogical-scaffold.schema.json](../../contracts/pedagogical-scaffold.schema.json); aucun CSS.
3. **Rendu** — transmettre le scaffold et le binding au renderer choisi par le projet. Le renderer gère CSS, accessibilité visuelle, pagination et export; il ne change pas les faits.

Ne pas mélanger le contrat métier, le DOM et la présentation.

## Choix du module et du corpus

- Traiter l'ordre demandé une capacité à la fois : Prédiction, Perception, Création, Raisonnement, Agentique, puis Synthèse multicapacité.
- Le livre de Tobias Zwingmann nomme « Thinking » la capacité ici appelée « Raisonnement ». Préserver les deux libellés dans les métadonnées de source pour faciliter le rapprochement.
- Lire le passage complet pertinent, noter le locator (chapitre/page ou section), relever les idées sans recopier de longues formulations. Les exemples et le cadre pédagogique doivent être reformulés.
- Distinguer ce que la source affirme, ce que l'équipe en déduit et les exemples proposés pour l'apprentissage. Une description d'une capacité n'est pas une promesse de résultat financier.
- S'il manque une source, écrire l'inconnue et proposer une question de recherche; ne pas combler en prétendant citer le livre.
- Rechercher les modules liés des 17 piliers pour expliciter les prérequis, le transfert et les dépendances. S'il manque le syllabus, signaler les liens proposés comme provisoires.

## Parcours en six pages

Écrire chaque module page par page, puis boucler la page entière avant de commencer la capacité suivante. Conserver le chaînage des takeaways.

1. **Comprendre** — définition courte, pourquoi l'entreprise s'y intéresse, trois exemples progressifs, matrice TOWS. Décrire une posture offensive, défensive, opportuniste et de préservation sans présenter les quatre choix comme universels.
2. **Transmettre** — pitch oral d'environ 30 secondes, postulat, framework visuel lisible, arguments sur l'urgence, la douleur et la facilité de prise en main; objections et réponses honnêtes.
3. **Diagnostiquer** — carte Ishikawa/mindmap couvrant Processus, Outils, Compétences, Données et Gouvernance. Décrire les dépendances et signaux d'adoption, pas seulement une liste de facteurs.
4. **Se projeter** — progression Assistant → Copilot → Autopilot/Agent. Séparer low-hanging fruit, quick win et big bet; préciser contrôle humain et niveau d'intégration. Rattacher au niveau 2 et aux 17 piliers lorsque le syllabus le permet.
5. **Relier à la valeur** — couvrir Logistique, Opérations, Marketing/Vente et Services. Pour chaque fonction, nommer une tâche ou douleur, l'ICP métier (rôle qui porte le problème) et les enablers. Rattacher à Porter sans inventer de chaîne spécifique au secteur.
6. **Agir** — backlog de 3 à 5 cas; positionner Automatisation × Intégration; appliquer BAC (Bénéfices, Avantages, Caractéristiques); noter Valeur, Coût, Risque, Complexité et Généricité de 1 à 3 étoiles. Définir explicitement le sens de chaque note. Donner un prompt concret qui n'invite ni données personnelles/confidentielles ni action réelle sans validation.

## Catalogue massif des cas

Le backlog complet reste dans un catalogue séparé, lié par référence depuis le binding. Utiliser `contracts/pedagogical-use-case-catalog.schema.json`. Garder les IDs stables, la provenance, les liens possibles aux 17 piliers et les doublons à résoudre; les fiches ne retiennent que 3 à 5 cas. Les champs inconnus restent absents ou null; ne pas inventer pour compléter.

## La synthèse multicapacité

Choisir un parcours métier où au moins quatre capacités apportent une contribution distincte. Représenter chaîne d'entrée → perception → raisonnement → création/prédiction éventuelle → décision humaine → action contrôlée. Préciser les capacités absentes, les handoffs, les points d'arrêt et la mesure. « Agentique » décrit le degré d'action, non une qualité intrinsèque supérieure.

## Critères de qualité

- Zéro jargon non expliqué; exemple professionnel concret sur chaque page.
- Takeaway explicite et phrase de transition sur chaque page.
- Chaque use case relie douleur, personne, processus, entrée/sortie, valeur potentielle, données, contrôle et prochaine mesure.
- La matrice TOWS est construite à partir de forces/faiblesses et opportunités/menaces; les options doivent croiser des facteurs, pas répéter un SWOT.
- Garder les scores et hypothèses visibles. Les étoiles ne signifient pas de valeur absolue; hard gates de droits, sécurité, contrôle humain et faisabilité viennent avant le classement.
- Traçabilité claim → fragment → source; séparer faits, inférences, hypothèses et recommandations.
- Le prompt d'exemple sert au prototypage avec données fictives ou anonymisées.
- Vérifier que le binding contient exactement six pages, que le scaffold est sémantique et que les deux objets se réfèrent aux mêmes blocs.

## Exemple de QA avant handoff

Conformité : les six pages sont présentes, chaque bloc a une cible, BAC et scoring sont expliqués, source locator est précis.
Contre-épreuve : tester le risque de surautomatisation, biais, qualité des données, erreurs plausibles ou transfert de responsabilité.
Lecture apprenant : vérifier qu'une personne débutante peut résumer le pitch, expliquer un exemple et nommer le prochain essai sans le formateur.
Visuel : à effectuer dans le renderer du programme après le contenu et le scaffold; aucun CSS n'est généré ici.
