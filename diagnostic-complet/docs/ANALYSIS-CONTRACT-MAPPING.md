# Mapping du contrat analytique — tranche S1a #303

14 novembre 2026. Parent #295 ; epic #294. Base d’étude dev 8023fd0c36fdf825eef67909811b5eb20b0129d2. Donneur candidat 75c8293de6984c6fac80e016528bdfa4ec019226. Spécification de compatibilité, sans adaptateur exécuté.

## Résultat de la lecture
Le candidat impose onze champs et au moins un résultat et un bloc destinataire. diagnostic-complet conserve une étude sources/fragments/claims/relations et un scaffold. Il n’offre pas de champ analyses dans le contrat documenté. writing.prepare_from_scratch refuse les clés en dehors de EVIDENCE_KEYS, notamment une clé analyses ajoutée sans évolution. Copier AnalysisResult dans une étude puis appeler ce bootstrap échouerait donc, même si la prose décrit un chaînage.

## Mapping proposé
La destination proposée est une enveloppe analytique distincte, rattachée à study_id et à la révision d’entrée. Le constructeur de paquets passe une projection evidence-only à writing.py ; les références d’analyse restent dans le brief et le paquet de direction tant que le contrat de scaffold n’est pas adapté. Cette enveloppe reste une proposition à implémenter dans #295.

| Champ candidat | Sens / propriétaire | Destination proposée | Invariant / disposition |
|---|---|---|---|
| id | Identité du résultat, analyste | analysis.id | Préserver ; unicité dans l’enveloppe, aucune collision avec claims |
| method | Méthode choisie | analysis.method | Préserver, référence au catalogue résoluble |
| method_version | Version de méthode | analysis.method_version | Préserver ; inconnue explicite et relecture si la méthode change |
| question | Question instruite | analysis.question et question_ref | Adapter ; identité de question indépendante des sections |
| scope | Périmètre de conclusion | analysis.scope | Préserver sans élargir secteur/produit/société |
| as_of | Date d’observation analytique | analysis.as_of | Préserver ; distincte des dates de publication/consultation |
| input_claim_refs | Claims effectivement mobilisés | analysis.input_claim_refs | Préserver, résoudre dans study.claims et conserver révision/hash d’entrée |
| findings | Conclusions attribuées | analysis.findings | Préserver en objets d’analyse, pas promotion automatique en faits du graphe |
| counterevidence | Contre-preuves textuelles | analysis.counterevidence | Préserver ; ajouter les références de claims disponibles dans la prochaine version |
| unknowns | Lacunes connues | analysis.unknowns | Préserver ; lacune sans claim n’exige pas un faux fragment |
| affects_blocks | Affectation narrative | binding.affects_blocks | Différer en phase analyse ; rattacher après création du scaffold, conserver les anciennes valeurs si leur bloc résout |

L’enveloppe proposée porterait schema_version, study_ref, input_revision et analyses. Aucun champ nouveau n’est ajouté au runtime par cette tranche. L’ajout de question_ref et de références structurées aux contre-preuves demande une version de contrat ; le mapping ne modifie pas le candidat historique.

## Statuts et pertes à éviter
- attributed_claim, inference, hypothesis et unknown existent dans les deux périmètres. Conserver le statut et l’attribution ; la résolution d’ID ne vérifie pas la vérité.
- recommendation existe dans les findings candidats, mais pas dans les statuts claim documentés de diagnostic-complet. La conserver comme recommandation dans l’enveloppe analytique ; ne pas la convertir silencieusement en inference ou verified_fact.
- supplied_claim et verified_fact existent côté étude, mais pas côté findings candidat. Les claims d’entrée gardent leur statut dans l’étude. Une nouvelle conclusion dérivée reste qualifiée par l’analyste.
- Les findings du contrat candidat exigent claim_refs non vide. Une analyse sans entrée suffisante doit rendre une sortie partielle/demande de recherche ; le contrat cible devra exprimer ce cas sans conclusion inventée.
- Counterevidence sous forme de texte perd sa résolution structurée ; la conservation du texte et des sources d’origine est obligatoire avant enrichissement.
- Une méthode calculatoire doit porter ses unités et hypothèses dans la sortie de méthode. Le contrat générique actuel ne les contrôle pas.

## Parcours nominal
Mandat → question Q1 → claims C1/C2 → analyse A1 → synthèse → brief → bloc B1. L’analyse A1 existe sans B1. La liaison tardive ajoute B1 et n’altère ni le résultat ni ses entrées.
Une source modifiée invalide C1 puis A1 et B1. Une correction de mise en page de B1 ne rouvre pas la recherche.
resolve_method.select nécessite actuellement block et vérifie le binding. Son comportement constitue une route legacy à préserver ; une nouvelle résolution d’analyse avant blocs doit être une voie explicite.

## Acceptation indépendante
La fixture analysis-contract-mapping.json contient deux scénarios synthétiques et des oracles rédigés avant tout adaptateur.
Le nominal conserve l’attribution et la recommandation comme objets distincts ; la liaison aux blocs arrive plus tard.
L’incomplet garde la question ouverte et la recherche nécessaire ; absence de conclusion et de bloc ne devient pas résultat factice.
Cette fixture est un matériau d’acceptation. Aucun parseur de ce nouveau contrat ni test logiciel de l’adaptateur n’est livré ici.

## Prochaine tranche #295
Implémenter un contrat d’enveloppe analytique versionné et une validation des références study/claims/révision ; prévoir état partial. Ajouter une voie de résolution par question et conserver la voie legacy par bloc. Tester nominal, incomplete, unknown claim, recommendation préservée, baseline périmée et étude legacy. Définir les fichiers exacts à partir du schéma de l’étude courant avant BUILD ; aucun fichier réservé par cette unité après sa clôture.

## Sources de travail et contrôle
[Rapport #300](../../docs/architecture/SKILLS-CRITICAL-REVIEW-2026-11-14.md) ; docs/INTERFACES.md ; writing.py ; candidat contracts/analysis-result.schema.json et mba/taxonomy/tools/resolve_method.py au SHA donneur.
Le lien au rapport depuis ce dossier se résout à la racine via ../../docs/architecture. Contrôles de cette tranche : JSON parsé, onze champs couverts une seule fois, deux cas et leurs références locales contrôlés. Rendu et runtime de l’adaptateur NOT_RUN.
