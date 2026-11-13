# Normalisation documentaire des 14 ADR locaux

Date de revue : 2026-11-14. Source de travail : snapshot de `dev` épinglé au commit `f20cfc3ee4cd630371ee28af5cae073680a40e0d`, fourni pour cette revue. Périmètre : les quatorze textes ADR-0000 à ADR-0013 de `diagnostic-complet/doc/architecture/` et le présent rapport. Cette livraison renforce la lisibilité de décisions existantes ; elle ne prend aucune décision d’implémentation nouvelle.

## Résultat et méthode

Les quatorze ADR ont été lus intégralement, avec les instructions racine et locales, l’index commun, l’index local et la [revue du 13 novembre](ADR-REVIEW-2026-11-13.md). Ils partageaient un contexte, une conséquence et un réexamen génériques. Ils contenaient une date identique ambiguë, sans approbateur identifié ni comparaison explicite d’options. Le lien intitulé « revue et owners » ne menait pas à un registre d’owners.

Chaque fiche comporte désormais une nature documentaire, une autorité non documentée explicitement signalée, une qualification de la date conservée, un contexte propre, le choix inchangé, les limites des alternatives connues, des conséquences propres, les références et une condition de réexamen adaptée. Le lien trompeur est renommé « revue des 14 ADR » ; aucun owner n’est inventé.

La normalisation distingue trois niveaux :

- **Trace conservée** : titre, identifiant, statut, mention de date, portée, décisions liées, paragraphe « Décision » et liens immuables sont inchangés. La mention de date est qualifiée comme ambiguë, sans transformer la restructuration en acceptation.
- **Lecture de revue** : les contextes reformulent l’enjeu visible dans le choix existant. Les risques et coûts déduits sont signalés comme implications ; ils ne sont ni des raisons historiques reconstituées ni des mesures d’impact.
- **Lacunes ouvertes** : approbateur, trace d’approbation, date précise et comparaisons d’alternatives ne sont pas attestés par les fiches sources. La normalisation ne les complète pas par supposition. Les options parfois nommées dans la rubrique alternatives sont expressément non documentées, jamais présentées comme ayant été évaluées.

Les liens vers `ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd` conservent les versions détaillées antérieures. Leurs contenus et les reçus privés n’ont pas été réaudités dans ce lot. Les statuts existants demeurent des traces documentaires ; ils ne constituent pas une preuve d’exécution ou une nouvelle approbation.

## Matrice complète

Les défauts indiqués ci-dessous concernent la qualité de la fiche source, sans constituer des constats d’anomalie du code. « Réexamen » désigne un déclencheur documentaire proposé, sans activation d’un changement de comportement.

| ADR | Nature et statut conservé | Défaut ou risque de lecture | Correction propre et réexamen |
|---|---|---|---|
| [0000](../../diagnostic-complet/doc/architecture/ADR-0000-registre-decisions-run.md) | Registre historique ; principes repris par 1001–1006 | Mandats datés lisibles comme permissions permanentes ; contexte uniforme | Distinguer registre, mandat et canon courant. Nouvelle décision transverse ou contradiction : décision liée, sans réécriture du mandat ancien. |
| [0001](../../diagnostic-complet/doc/architecture/ADR-0001-kb-contrat-documentaire.md) | Accepté, local | Rôle des sources, occurrences et atomes insuffisamment expliqué | Expliciter traçabilité et distinction import/vérification. Réexaminer identité, offsets, normalisation et déduplication avec conservation des références. |
| [0002](../../diagnostic-complet/doc/architecture/ADR-0002-referentiel-ontologie.md) | Proposé, implémentation locale en lecture seule | Implémentation pouvant être lue comme acceptation ; structure confondue avec vérité métier | Maintenir le statut proposé et la limite de validation structurelle. Réexaminer référentiel, domaines ou mutation automatique ; acceptation distincte requise. |
| [0003](../../diagnostic-complet/doc/architecture/ADR-0003-loopback-graphe.md) | Accepté, observation locale | Densité susceptible d’être lue comme score de qualité ; budget peu expliqué | Distinguer inventaire sans plafond, candidat et budget de traitement. Réexaminer métrique de promotion, plafond masquant des constats ou budget insuffisant. |
| [0004](../../diagnostic-complet/doc/architecture/ADR-0004-renforcement-kb-spec.md) | Historique, consolidé par 0003/0005 | Ancienne spécification pouvant réintroduire le plafond de trois propositions | Clarifier rôle de pointeur historique et consolidation par D32. En cas de divergence, agir sur le contrat courant, sans réactivation du plafond. |
| [0005](../../diagnostic-complet/doc/architecture/ADR-0005-contrat-skill-reinforce.md) | Accepté, packaging local | Triplication pouvant devenir une prescription universelle ; coût de synchronisation implicite | Expliciter synchronisation et limites de généralisation. Réexaminer surface, dépendance ou divergence de copie. |
| [0006](../../diagnostic-complet/doc/architecture/ADR-0006-calibration-cadence.md) | Accepté ; aucun seuil calibré par la revue | Acceptation pouvant être confondue avec calibration réalisée | Rappeler absence de seuil établi et besoin de cycles observés. Réexaminer avec observations ou contradiction d’un seuil existant ; aucune valeur ajoutée. |
| [0007](../../diagnostic-complet/doc/architecture/ADR-0007-projection-graph1.md) | Accepté, adaptateur local | Publication passée confondue avec disponibilité présente | Distinguer reçu historique, isolation du namespace et disponibilité. Réexaminer namespace, graphe protégé, chemins ou identifiants. |
| [0008](../../diagnostic-complet/doc/architecture/ADR-0008-frontiere-run-build.md) | Accepté, spécialisation locale | Profil métier public lisible comme choix universel ; question RF-18 ouverte | Rappeler indépendance du moteur, fixtures synthétiques et version/migration. Réexaminer dépendance au corpus, incompatibilité de profil ou résolution de RF-18. |
| [0009](../../diagnostic-complet/doc/architecture/ADR-0009-terminologie-kind.md) | Accepté, contrat local courant | Vocabulaire historique concurrent et validation structurelle trop facilement surinterprétée | Préciser autorité de terminology.json et absence de vérification par réemploi. Réexaminer vocabulaire, éligibilité ou consommateur réintroduisant les tiers. |
| [0010](../../diagnostic-complet/doc/architecture/ADR-0010-detection-directive.md) | Accepté, heuristique locale | Absence de performance mesurée ; risque sur identité lors d’une reclassification | Rappeler limites de détection et conservation des références. Réexaminer exemples documentés de faux positifs/négatifs ou changement des marqueurs. |
| [0011](../../diagnostic-complet/doc/architecture/ADR-0011-acquisition-2026-11-10-et-migration-profil.md) | Accepté, décision locale ; bilan historique | Migration compatible, reclassification et résultat d’acquisition risquent d’être confondus | Séparer compatibilité et changement de lexique, BUILD et vérification RUN. Réexaminer schéma, lexique, namespace ou pointeur non résolu. |
| [0012](../../diagnostic-complet/doc/architecture/ADR-0012-directive-de-style-et-double-cerveau.md) | Accepté pour le style ; métier hors architecture commune | D39 et D40 de portée différente dans une même fiche | Garder le style local et l’apport D40 historique, sans généralisation métier. Réexaminer public, mandat, approbation mécanique ou proposition de définition commune distincte. |
| [0013](../../diagnostic-complet/doc/architecture/ADR-0013-statuts-de-lecture-et-outil-de-migration.md) | Accepté, contrat local | Réétiquette confondue avec migration sûre et validation partielle avec validation globale | Préciser compatibilité, reçu et portée assertion par assertion. Réexaminer conditions de migration, statuts ou extension abusive d’une validation partielle. |

## Écarts résiduels et portée du renforcement

La correction éditoriale est terminée sur les quatorze fiches, mais elle ne reconstitue pas l’arbitrage historique absent. Trois niveaux restent distincts :

| Niveau | Constat après normalisation | Résolution requise |
|---|---|---|
| Gouvernance et compréhension | Date précise, approbateur et preuve d’acceptation non documentés par les fiches ; statuts conservés | Retrouver une trace datée et attribuée si elle est nécessaire à une nouvelle décision ; ne pas réaccepter par défaut |
| Arbitrage substantiel | Alternatives évaluées, comparaison sur critères communs et meilleure objection historique non documentées | Les laisser inconnues ; préparer une proposition comparative distincte seulement si un choix est réellement rouvert |
| Éditorial | Contexte, conséquences et réexamen génériques ; libellé de lien trompeur | Corrigé dans les quatorze fichiers, avec séparation explicite des implications de revue |

Les événements de réexamen désignent les faits discriminants à rechercher : référence source non résolue, changement de vocabulaire ou de schéma, divergence de copie, faux positif/faux négatif documenté, ou observation permettant une calibration. Ils ne constituent pas des tests exécutés. Les responsables du réexamen ne sont pas nommés lorsque leur identité n’est pas documentée. Cette distinction empêche de présenter la présence de rubriques comme une preuve que tous les arbitrages sont historiquement complets.

## Contrôles réellement exécutés

Un contrôle local de comparaison du snapshot source et des quatorze fichiers normalisés a réussi le 14 novembre 2026 :

| Contrôle documentaire | Résultat |
|---|---|
| Inventaire exact ADR-0000 à ADR-0013, un fichier par identifiant | PASS — 14 fichiers |
| Titres, identifiants, statuts, mentions de date, portées et décisions liées conservés | PASS — 14/14 |
| Paragraphes « Décision » identiques au texte source | PASS — 14/14 |
| Liens HTTPS historiques conservés à l’identique | PASS — 14/14 |
| Contexte, alternatives, conséquences, références, réexamen et métadonnées présents | PASS — 14/14 |
| Contextes, conséquences et réexamens différents des paragraphes génériques sources | PASS — 14/14 ; ceci reste un contrôle textuel, pas une preuve de qualité éditoriale |
| Liens Markdown relatifs des ADR résolus dans le snapshot vérifié | PASS — 46 liens |

Le contrôle utilise la copie source en lecture seule et les fichiers normalisés ; il n’exécute aucun composant du prototype. La revue éditoriale des quatorze choix est distincte de ces assertions mécaniques. Aucune fixture runtime n’est ajoutée : aucun contrat exécutable, enum, moteur ou comportement n’a changé. Deux repères opérationnels ont été ajoutés aux ADR-0002 et ADR-0005 après vérification de leurs ressources au SHA source : `cadence_semantic` et les quatre identifiants de fixtures ontologiques. Ils réparent cinq assertions documentaires déjà en échec sur la base sans dupliquer les spécifications. Les propositions de nouveaux déclencheurs de réexamen sont des recommandations documentaires.

## Limites et statut d’intégration

Ce lot ne vérifie ni le code d’ingestion, ni les calculs de loopback, ni les migrations, ni la projection Graph1, ni une calibration de cadence, ni la disponibilité d’une skill. Il ne relit pas les corpus privés, ne valide aucune side story et ne ferme aucun ticket d’implémentation. Les liens externes sont conservés textuellement ; leur disponibilité réseau n’est pas testée.

Les gates locaux ont ensuite été exécutés dans le lot d’intégration sur un snapshot partiel épinglé dont les dépendances nécessaires ont été matérialisées et vérifiées (336 blobs sources). Contrats racine : PASS (10 templates,4 modes,workflow1.3.1). Ontologie : PASS (v0.5.0,10 types,16 règles). Suite de312 tests :6 échecs sur la base,1 après correction, aucune nouvelle régression observée. Les cinq assertions documentaires de calibration/fixtures sont réparées ; `test_extracted_text_is_written_to_markdown_files` reste en échec sur la base et sur le résultat normalisé, avec une différence liée à l’ordre des fichiers. La suite complète n’est donc pas verte. `ci: intentionally_not_run` ; publication préparée en branche de revue, sans promotion sur dev ou main.

Les ADR communs 1001–1006, les manifests, les enums et les ressources opérationnelles restent hors du delta. Les fiches locales pointent vers le canon actuel et les ressources épinglées sans y réintroduire de spécification runtime. Les versions antérieures restent adressables par leur commit immuable.

## Vérification d’intégration complémentaire

Les62liens relatifs du lot complet (ADR et rapports) ont été résolus sans manque au moment du gate final. Ce compteur décrit ce périmètre et ne valide pas les liens externes. L’ajout de liens de navigation après ce contrôle se revérifie séparément. Le [rapport des méthodes et replays](SKILL-METHOD-REVIEW-2026-11-14.md) distingue les tests indépendants des lectures de couverture.
