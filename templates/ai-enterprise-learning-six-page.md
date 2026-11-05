---
template_type: ai-enterprise-learning-six-page
template_class: pedagogique
version: 0.1.0
lifecycle: candidate
pages: 6
binding_contract: contracts/pedagogical-binding.schema.json
backlog_catalog_contract: contracts/pedagogical-use-case-catalog.schema.json
scaffold_contract: contracts/pedagogical-scaffold.schema.json
scaffold_template: templates/pedagogical-six-page-scaffold.json
skill: skills/pedagogical-ai-learning/SKILL.md
---

# Contrat éditorial — fiche pédagogique « Pour aller plus loin »

## Public et usage

Fiche autonome de six pages, conçue pour un débutant en IA en entreprise et réutilisable par un « poisson pilote » qui anime un échange d'équipe. Chaque page répond à une question et transmet un takeaway qui ouvre la suivante. Le ton reste clair, concret et orienté valeur ; tout terme spécialisé reçoit une explication courte.

## Séquence fixe des pages

| Page | Question de l'apprenant | Blocs de contenu à lier |
|---|---|---|
| 1 — Comprendre | De quoi parle-t-on et pourquoi cela compte ici ? | Signalétique, définition en mots simples, exemples progressifs, TOWS avec 4 postures : offensive, défensive, opportuniste, préservation |
| 2 — Transmettre | Comment l'expliquer à l'équipe en 30 secondes ? | Pitch, postulat, mini-framework visuel, 3 leviers de conviction (urgence, douleur résolue, simplicité), objections/réponses |
| 3 — Diagnostiquer | Qu'est-ce qui doit changer autour du travail ? | Carte Ishikawa ou mindmap, facteurs Processus, Outils, Compétences, Données, Gouvernance, signaux d'adoption |
| 4 — Se projeter | Quel premier pas mène à une intégration plus utile ? | Trajectoire Assistant → Copilot → Autopilot/Agent, low-hanging fruit / quick win / big bet, lien au niveau 2 et aux 17 piliers |
| 5 — Relier à la valeur | Où cette capacité aide-t-elle les fonctions de l'entreprise ? | Chaîne de valeur de Porter, Logistique, Opérations, Marketing/Vente, Services, besoin métier et enabler; signaler les fonctions de soutien quand utiles |
| 6 — Agir | Que tester, avec quel contrôle, et comment apprendre ? | Automatisation × intégration, top 3 à 5 cas, grille BAC, cinq notes sur 3 étoiles (valeur, coût, risque, complexité, généricité), prompt d'essai encadré |

## Règles de contenu et d'enchaînement

- Les pages 1 à 6 suivent une seule histoire : comprendre → expliquer → diagnostiquer → se projeter → relier à la valeur → essayer.
- Chaque page finit avec une phrase de passage qui prépare la suivante. La page 6 ferme la boucle et propose un retour d'expérience mesurable.
- Pour la synthèse multicapacité, identifier au moins quatre capacités parmi Prédiction, Perception, Création, Raisonnement et Agentique. Nommer les entrées, les transformations, les décisions humaines et les sorties.
- Les notes étoilées sont ordinales, liées à une règle explicite; elles ne remplacent ni une étude de faisabilité ni les hard gates. Plus d'étoiles signifie « plus favorable » pour Valeur, Risque maîtrisable et Généricité; « plus favorable » pour Coût et Complexité signifie ici moins de coût/d'effort. Toujours écrire la règle.
- BAC signifie ici Bénéfices, Avantages, Caractéristiques, selon le brief du programme. Ne pas substituer silencieusement une autre définition.
- Une promesse d'économie ou de performance reste une hypothèse tant qu'elle n'est pas mesurée dans un pilote.
- Une capacité IA seule n'est jamais un cas d'usage : préciser le processus, l'utilisateur, l'entrée, la sortie et le contrôle.
- Ne pas placer CSS, tokens, dimensions d'écran ou règles de pagination dans les contrats de binding. Le scaffold décrit seulement le HTML sémantique et les points d'ancrage.

## Contrat d'enchaînement pédagogique

headline → idée clé → exemple → question de transfert → takeaway → transition

Chaque page doit répondre à une question métier ou d'apprentissage, et chaque tableau ou schéma doit pouvoir être compris sans la narration orale du formateur.

## Sources et limites

Partir d'un corpus fourni; tracer les assertions au registre source/locator. Pour ce programme, le livre de Tobias Zwingmann est une source de cadrage, pas une preuve qu'un use case produit déjà un ROI. Écrire les synthèses avec ses propres mots et citer des localisateurs brefs (chapitre/page ou section). Toute connaissance opérationnelle au-delà du livre doit être identifiée comme apport de conception ou enrichie par une source autorisée.

## Rendu appliqué

Le mécanisme de composition Hivest est importé sous renderers/pedagogical/upstream avec commit et empreintes. La projection six pages est exécutable par `python renderers/pedagogical/render.py <module.md> --out <dir>`. Les tableaux TOWS et Porter deviennent des cartes; les grands tableaux BAC deviennent des cartes de use case et cinq notes. Le renderer conserve les textes et les scores du Markdown. La QA navigateur est recoupée avec les six pages physiques du PDF et leurs PNG.
