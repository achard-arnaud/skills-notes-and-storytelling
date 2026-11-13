# Méthodes rédactionnelles et relais graphiques

Revue du 14 novembre 2026. Ce rapport décrit un lot de méthodes personnelles et les contrôles documentaires réalisés. Il ne copie aucun SKILL.md dans le dépôt public, n'ajoute aucun type au manifeste et n'active aucun runtime.

## Méta-procédé commun

Les méthodes PRD, ADR et Story/TDD séparent cinq états : cadrer l'intention et les preuves ; sélectionner une déclinaison et ses références ; modéliser puis rédiger ; vérifier et qualifier ; corriger la première couche fautive et rejouer les sorties affectées. Le noyau porte les décisions de travail et le contrat de sortie. Les références portent les variantes, templates, règles, bornage, contrôles, sources et cas synthétiques. Les bindings lisent un manifeste fourni sans inventer un chemin ni migrer son schéma.

Les références méthodologiques servent d'inspiration attribuée, sans installation ni revendication de conformité complète à BMAD ou Superpowers. Les sources effectivement lues sont enregistrées dans chaque paquet de méthode. Un PRD ne prend pas une décision d'architecture ; un ADR n'implémente pas son choix ; une story spécifie les tests sans prétendre avoir observé Red/Green.

## Relais graphique

Les quatre méthodes — note pédagogique, PRD, ADR, story — déclenchent explicitement `schema-flow-master` lorsqu'une représentation de relations, topologie, séquence ou processus doit être créée ou matériellement révisée. Une typo, une liste simple, un tableau suffisant ou le déplacement d'une image correcte ne déclenchent pas cette sous-étape.

Le paquet transmis porte question visuelle, public, zoom, faits et relations autorisés, inconnues, ancre, cible et critères de fidélité. Le retour distingue source éditable, ressource rendue nullable, légende, inconnues et reçu. Syntaxe, sens, rendu et intégration sont quatre observations distinctes. Le propriétaire documentaire conserve le scaffold et l'insertion ; aucun paquet ne promet une approbation ou une écriture qui n'a pas eu lieu.

Le loopback remonte à la première couche fautive. Une relation changée invalide source, image, légende et assertions dérivées. Une erreur de placement ne justifie pas de régénérer un modèle valide. Un reçu conserve baseline, delta, ressources effectivement lues, contrôles PASS/FAIL/NOT_RUN, éléments rejoués et statut de persistance. Les oracles d'évaluation ne sont pas transmis à l'exécutant d'un replay indépendant.

## Cas exécutés et itérations

| Méthode | Exécution observée | Correction ou limite |
|---|---|---|
| Note pédagogique | Replay indépendant sur processus avec branches et retours ; lecture du noyau, contrat visuel, loopback et Schema Flow Master ; contrôle statique de la source | Relais désormais explicite. Pas de parseur/rendu disponible ; reçu qualifié, aucune insertion prétendue |
| Note pédagogique | Correction orthographique indépendante dans la même session de test, avec nouvelle lecture du noyau/loopback | Aucun appel graphique, aucune régénération |
| PRD | Utilisations d'auteur nominale/entrée pauvre puis replay frais sur exigences contradictoires de conservation | Incrément corrigé pour conserver une valeur autonome ; arbitrage proposé distingué d'approbation ; KPI/ROI non inventés |
| ADR | Lecture intégrale des14 ADR courants puis replay frais sur proposition locale avec implémentation read-only et demande d'élargissement | Statut/portée historiques conservés ; successeur proposé ; relations manquantes rendues hypothétiques, aucun rendu prétendu |
| ADR | Replay après correction sur date de révision absente | Date historique conservée et date nouvelle non fournie ; contrat renforcé après datation non vérifiée dans le premier replay |
| Story/TDD | Replay frais sur relance de génération et idempotence, avec comportement en cours indécis et demande de tests verts | Inconnue bloquante conservée ; aucun test vert fabriqué ; seuil cyclomatique seulement proposé à qualifier. Précision ajoutée sur effet partiel et succès non confirmé |

Les cas négatifs et certaines utilisations d'auteur ne sont pas tous des sessions indépendantes. La présence de fixtures ne démontre pas leur exécution. Ces résultats ne sont ni une mesure de gain de temps ni une validation d'apprentissage auprès d'utilisateurs. Aucun parseur ou moteur Mermaid n'a été exécuté dans ce lot, et aucun de ces replays n'a modifié un produit.

## Couverture du corpus

Les14 ADR sont les cas réels de lecture, de préservation et de normalisation d'ADR ; ils fournissent aussi des contraintes et contre-exemples de statut, portée, preuve et historique pour les autres méthodes. Ils ne sont pas présentés comme14 PRD ou14 stories testés. Les variantes PRD et Story sont éprouvées sur des exemples synthétiques adaptés à leur contrat.

La [matrice des14 ADR](ADR-NORMALIZATION-2026-11-14.md) détaille la couverture et les limites. Les décisions opérationnelles, manifests, contrats exécutables et ressources de run restent les autorités au SHA résolu. Les principes 1001–1006 restent inchangés.

## Gates du corpus normalisé

Contrats et ontologie locaux : PASS. Suite de312 tests :6échecs sur la base,1échec de crawl préexistant après correction des5assertions documentaires. Aucune nouvelle régression observée ; suite complète non verte, CI non exécutée. La publication reste une proposition en branche/PR, sans promotion sur dev/main.
