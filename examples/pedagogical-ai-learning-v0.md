---
template_type: ai-enterprise-learning-six-page
template_version: 0.2.0
fixture_version: 0.2.0
workflow_version: 1.3.1
---
# Fixture éditoriale — fiche pédagogique IA (candidate 0.1.0)

**Classe :** pedagogique  
**Niveau :** débutant  
**Module :** Prédiction  
**Source principale :** Tobias Zwingmann, The Profitable AI Advantage (2025), chapitre 2, « Prediction mode », pp. 23–26; chapitres 5–6 pour mapping de processus et conception des cas d'usage. Synthèses originales.

## Page 1 — Comprendre
**Titre :** De l'historique à une décision mieux préparée  
**Idée clé :** La prédiction estime une catégorie ou un résultat probable à partir de données antérieures; elle aide à anticiper, sans garantir l'avenir.  
**Exemple progressif :** estimer un volume mensuel → repérer des dossiers atypiques → aider une équipe à répartir sa capacité.  
**TOWS :** offensive, tester un signal de demande sur une ligne rentable; défensive, surveiller la dérive et garder un recours humain; opportuniste, commencer par une prévision déjà alimentée par des données propres; préservation, différer si les données sont pauvres ou les erreurs trop coûteuses.  
**Takeaway :** une estimation utile commence par une décision réelle.

## Page 2 — Transmettre
**Pitch :** « Nous avons déjà des historiques qui guident nos décisions. La prédiction aide à en tirer un signal plus tôt, afin que l'équipe prépare une action; elle ne décide pas à sa place. Commençons sur un cas répétitif où l'erreur reste visible et corrigeable. »  
**Postulat :** si la donnée passée reflète encore le contexte, un modèle peut aider à prioriser les cas à examiner.  
**Framework :** historique → estimation → vérification → décision métier → mesure.  
**Objections :** « Le modèle peut se tromper » → oui, définissons seuils et recours; « nos données sont imparfaites » → audit court avant prototype; « cela va remplacer l'équipe » → l'essai mesure une décision assistée, pas un remplacement.  
**Takeaway :** la confiance se gagne par un test limité.

## Page 3 — Diagnostiquer
| Facteur | Question terrain |
|---|---|
| Processus | À quel moment une prévision modifie-t-elle la décision ? |
| Outils | Où afficher le signal et recueillir la correction ? |
| Compétences | Qui comprend les faux positifs et les limites ? |
| Données | L'historique est-il représentatif et licite ? |
| Gouvernance | Qui surveille les écarts et peut suspendre l'usage ? |
**Takeaway :** le modèle n'est qu'un maillon du système.

## Page 4 — Se projeter
Assistant : expliquer une prévision existante. Copilot : intégrer le signal dans la préparation d'une décision. Autopilot/Agent : déclencher une action limitée seulement si les règles et seuils sont validés. Low-hanging fruit : tableau de prévisions; quick win : alerte revue hebdomadaire; big bet : orchestration de capacité à l'échelle. Lien niveau 2 : qualité des données, mesure de valeur et contrôle du modèle.  
**Takeaway :** augmenter l'intégration seulement après un apprentissage concluant.

## Page 5 — Relier à la valeur
Logistique : anticiper volumes et stocks (responsable supply, données de commandes et délais). Opérations : prévoir charge ou anomalies (responsable de production, séries temporelles fiables). Marketing/Vente : prioriser des prospects ou prévoir conversion (responsable CRM, historique documenté et surveillance de biais). Services : estimer le flux de demandes (responsable de service, motifs et saisonnalité).  
**Takeaway :** chaque fonction doit préciser la décision à améliorer.

## Page 6 — Agir
Top cas : prévision de charge (intégration et automatisation moyennes), détection d'anomalies (automatisation basse, intégration moyenne), scoring de leads (intégration moyenne, contrôle renforcé). BAC : Bénéfice = anticiper; Avantage = hiérarchiser les cas; Caractéristique = score ou plage avec date et incertitude. Score exemple à valider : valeur ★★★, coût ★★, risque ★★, complexité ★★, généricité ★★★.  
**Prompt d'essai :** « À partir de ce tableau fictif de volumes hebdomadaires et d'événements connus, propose une estimation pour les quatre prochaines semaines, signale les hypothèses et les anomalies, distingue ce que les données montrent de ce qu'elles ne permettent pas de conclure, puis liste les vérifications qu'un responsable doit effectuer avant toute décision. N'invente aucune donnée. »  
**Boucle :** mesurer la qualité du signal et son effet sur la décision avant d'élargir.

Convention de score : 1 faible, 2 moyen, 3 élevé. Valeur et généricité élevées sont favorables; coût, risque et complexité élevés demandent plus de prudence. Le rendu conserve ces valeurs.
