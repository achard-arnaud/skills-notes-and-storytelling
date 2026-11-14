# Reprise autonome — convergence Business/Product et essai 3

## Action immédiate
Lire ce document puis l’epic #294 et le lot #295. Vérifier les HEAD distants, la PR de préparation et tout owner actif avant d’écrire. Le présent document prépare une nouvelle conversation ; aucune tâche distante n’est lancée par sa présence.

## Besoin du lecteur
François veut des analyses substantielles et mémorisables : comprendre une entreprise et son produit, mécanismes, usages détaillés, architecture fonctionnelle, valeur et limites ; les liens, aperçus et widgets doivent rendre la lecture plaisante. Sans mandat décisionnel, produire une analyse et un diagnostic. Les huit finalités produit sont fiche produit, diagnostic produit, traction commerciale, benchmark fonctionnel, marché, 4P, clients 360, usages/chaîne de valeur.
Pour l’approfondissement demandé, 40–70 publications utiles avec provenance, indépendance et couverture ; le nombre seul ne garantit pas la qualité. Produits et entreprise partagent un dossier mais gardent leurs périmètres, unités et dates.

## Historique utile et erreurs à éviter
Current AI fut le run apprécié : tension écosystème ouvert fragmenté → expérience intégrée adoptée ; produits, architecture, use cases, KPI et moyens de l’entreprise. Original rendu et conversation intégrale non retrouvés dans les recherches de cette session ; les retours utilisateur visibles sont l’oracle disponible.
L’essai 1 factorisait trop fortement la procédure ; le replay Current AI n’autorisait qu’une annonce comme source et le Markdown, ce qui ne pouvait reproduire le run apprécié.
L’essai 2 a ajouté quatre verticales et une bibliothèque méthodologique. Son sélecteur relie méthode/finalité/bloc ; il ne conduit pas l’analyse à la place de l’agent. Les deux sorties Delos furent jugées hors sujet : le brief avait inventé un service support et une décision de pilote, sur quatre sources. Les scores 9/10 et 10/10 récompensaient ce brief divergent. Ne pas les utiliser comme preuve de transfert.
La correction a produit une recherche Delos de 50 URL et huit finalités, puis une étude comparative. La satisfaction finale et l’équivalence au run Current AI restent à éprouver.

## Cible proposée
Quatre phases :
1. contexte, recherche et qualification ;
2. analyse et synthèse, retours de recherche ciblés ;
3. direction narrative, tension et scaffold, retour analytique si nécessaire ;
4. rédaction, revue et rendu, retour à la couche fautive.
Point d’entrée commun, spécialisations conditionnelles ; une phase n’impose pas une skill ni un agent. Données et budget de run hors skill. Réutiliser diagnostic-complet ; intégrer les méthodes candidates et l’hygiène de transitions de Candidatures. Aucun moteur supplémentaire ni bus imposé.

## Frontières d’intégration
Le contrat candidat AnalysisResult exige affects_blocks trop tôt ; prévoir une question analytique avant le scaffold, puis liaison ultérieure, avec migration compatible.
Les compétences GreenYellow mêlent parfois analyse et paquet d’encart ; produire l’analyse indépendamment avant de décider de son usage narratif.
Le graphe de preuves, la carte d’enquête et le scaffold lecteur sont des vues distinctes ; aucune flèche exploratoire ne devient causalité.
La méthode peut produire un schéma candidat sans génération de prose automatique ; les scripts ne remplacent pas l’analyse ni le jugement.

## Versions et emplacements
- Storytelling main de référence : 7000c86a7e54cafc68c5bb5ada9aeed5df186aae.
- dev restauré initialement au même SHA, actualiser avant chaque lot.
- Deux essais conservés : experiment/narrative-procedure-ab-20261113, 75c8293de6984c6fac80e016528bdfa4ec019226.
- Préparation documentaire : plan/convergence-essai3-20261114, branche issue de dev ; résoudre son HEAD après publication.
- Candidatures Nice donneur dev : 1bd568775b7903623c2ae21d892c791963b5756a ; main 710c0db29d865af0c15d3dced64f72aa65a2c710. Lire seulement workflow/PROCESS.md et phase pertinente.
- diagnostic-complet est déjà dans main. Son ancien README parle encore d’une livraison dev ; ne pas en déduire l’état distant.

## Lecture minimale de reprise
1. #294, #295 et [plan courant](CONVERGENCE-PLAN-2026-11-14.md).
2. [ADR proposé 1007](../architecture/ADR-1007-study-workflow.md), puis seulement ADR-1001/1002/1004/1006 utiles.
3. diagnostic-complet/docs/INTERFACES.md ; docs/WRITING-WORKFLOWS.md ; docs/RESEARCH.md.
4. Contrat d’analyse candidat sous experiments/narrative-procedure-v1/contracts/analysis-result.schema.json, au SHA donneur.
L’analyse complète précédente : docs/architecture/WORKFLOW-CONVERGENCE-OPPORTUNITY-2026-11-14.md dans la branche expérimentale.
La rétro-analyse Current AI : experiments/narrative-procedure-v1/BOOTSTRAP-CURRENT-AI.md.
Les observations Delos : experiments/narrative-procedure-v1/evals/delos-product-research/ ; publications non indépendantes à dédupliquer par origine.
Ne pas charger tout le dépôt ou toutes les fixtures. Lire le paquet actif et les dépendances qui changent le résultat.

## Backlog et PR
181 issues et quatre PR observées avant création ; #294–297 ajoutées. Inventaire complet de navigation dans BACKLOG-TRIAGE-2026-11-14.tsv. Douze owners enrichis, les périmètres hors convergence restent à qualifier.
#13 clean lors de la revue, règle hygiène utile à extraire et contrôler.
#12 CLOSING, #17 fonds stratégique et #33 Workbench sont en conflit ; #17/#33 drafts. Checks validate réussis sur les HEAD respectifs, sans preuve de compatibilité avec le nouvel état.
Aucun merge ni fermeture effectué. Quatre commentaires de disposition sont présents. Ne pas résoudre par écrasement de catalogues.

## Plan d’exécution
#295 → #296 → #297, trois unités séquentielles et conditionnelles. Pas de promesse horaire. Prochaine journée demandée, 15 novembre 2026 selon date client, ordre utilisable si démarrage le 14.
Branche de lot depuis dev vérifié, PR dev, contrôle exact du HEAD, puis promotion main cumulative après compatibilité et autorité de publication en vigueur. Respecter AGENTS.md et le contrat SDLC actuel, notamment #40. Pas de nouvelle automation créée.
Le premier lot est READY après mapping précis des contrats, entrées et fichiers ; ne pas confondre préparation et résultat BUILD.
Tâches indépendantes possibles en cas de blocage : oracle sémantique, mapping documentaire ou fixture synthétique ; consigner le blocage et sa reprise.

## Critères de validation
Même demande originale et mêmes conditions entre comparaison main/cible. Une analyse réelle doit alimenter une synthèse, un brief puis le résultat. Pause après phase 2 et reprise à froid. Modification d’une source, invalidation des seuls descendants. Cas de réserve distinct. Revue de substance/narration/rendu et décision du lecteur séparées. L’original Current AI manquant reste une limite, pas un artefact à inventer.

## Agents, contexte et nettoyage
Au contrôle de cette session, seul /root était actif. Aucun agent secondaire n’est à arrêter.
Aucun compteur fiable des compactions antérieures ni commande de compaction manuelle disponible. Sauvegarde durable et nouvelle conversation constituent le moyen de reprise contrôlable.
Les fichiers transitoires supprimés figurent dans CLEANUP-RECEIPT-2026-11-14.json ; les sources et livrables restent préservés dans leurs destinations. Supprimer des fichiers n’efface pas les tokens déjà lus. Aucun effacement de préférences ou de mémoire utilisateur.
Statut de réception : dossier préparé et vérifié par lecture distante ; aucun run dans une nouvelle conversation lancé.


## Mise à jour PR #300 — 14 novembre 2026
Lire le [rapport critique](../architecture/SKILLS-CRITICAL-REVIEW-2026-11-14.md) pour les noms canoniques et les limites des preuves. Le premier lot documentaire de mapping est [#303](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/303), enfant de #295 ; #296/#297/#301 appliquent les mêmes principes selon leur finalité. Consulter le contrat SDLC courant pour les horaires et l’admission, les anciens horaires de cette documentation restent historiques.


## Reprise consolidée après S1a — 14 novembre 2026
La PR #300 est synchronisée par #304, commit dev 8023fd0c36fdf825eef67909811b5eb20b0129d2. Le rapport critique est maintenant une entrée des tickets #294–297/#301/#130/#142.
La tranche #303 produit diagnostic-complet/docs/ANALYSIS-CONTRACT-MAPPING.md et fixtures/analysis-contract-mapping.json. Lire le mapping avant d’implémenter l’enveloppe analytique de #295 ; l’étude documentée n’accepte pas une clé analyses ajoutée silencieusement. Les blocs narratifs doivent être liés après l’analyse.
La revue des PR multi-repo est enregistrée dans Skills-SDLC-superpower#7 : sept PR sur cinq dépôts, conditions de reprise documentées ; les deux PR non draft mais bloquées/attente de revue ont été remises en draft. Aucune fermeture globale ni fusion fonctionnelle de ce portefeuille. Relire owners et HEAD.
Stratégie explicite : branche bornée depuis le dev courant, PR vers dev, vérification du HEAD, promotion main selon les gates. Pas d’écriture directe sur dev pour les prochains lots.
Pour la reprise, garder GPT-6.1 Sol pour l’exécution bornée. Une revue d’architecture plus approfondie est ponctuelle ; le changement de modèle ne remplace pas mandat et critères. Nouvelle conversation recommandée pour repartir des seuls artefacts utiles. Aucune compaction manuelle contrôlée et aucun gain de tokens promis.
Le contrat SDLC opérationnel courant est SDD-TDD-20261114-v5 au moment de cette rédaction ; résoudre sa version en vigueur au prochain démarrage, les anciens horaires de cette capsule ne constituent pas le calendrier actif.
