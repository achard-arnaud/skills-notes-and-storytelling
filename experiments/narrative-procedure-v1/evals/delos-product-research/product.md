# Delos AI Worker · produit, usages et conditions d’exécution

Revue documentaire du 14 novembre 2026. Question ouverte : que délègue une équipe à un Worker, comment le travail circule-t-il et que peut-on effectivement attribuer au produit ? La preuve la plus informative associe l’aide qui expose les limites de configuration, un essai de presse qui montre les sorties et les réserves, et un témoignage client attribué. Aucun accès à une instance Delos dans cette revue.

## Fiche produit

Delos commercialise une suite bureautique et, séparément, des Workers. L’Assistant de la suite sait déjà converser et enchaîner des actions. Ce qui caractérise le Worker est **la persistance d’une fonction déléguée** : un responsable humain configure un profil nommé, ses missions durables, ses moyens de communication, ses procédures et ses accès. Le collaborateur humain peut ensuite lui adresser une tâche dans son canal habituel ; le Worker peut aussi démarrer sur événement ou à échéance. Le catalogue propose notamment des profils marketing, design, data et développement et autorise la configuration sur mesure. [P01–P04, P12]

**Du mandat au résultat.** Le responsable attribue une mission récurrente ou ponctuelle, rattache les ressources de référence, choisit les canaux et connecte les outils nécessaires. À la réception d’un événement, le Worker le qualifie, consulte les procédures et le contexte pertinents, active une intégration à la demande, appelle une action autorisée par les identifiants du service, puis remet ou enregistre le résultat. Le cockpit expose l’activité horodatée. Le RAG et la mémoire persistante annoncés jouent des rôles différents : retrouver une information dans les sources connectées ; conserver le contexte d’une interaction à l’autre. [P02–P08, P15]

## Positionnement dans la chaîne de valeur

| Étape, acteur et besoin | Mécanisme → sortie | Niveau de preuve et limite |
|---|---|---|
| Communication, rédaction : recueillir puis mettre en forme un témoignage | Une consigne reçue par mail mène à un entretien téléphonique, un SMS de confirmation et un fichier Word renvoyé par mail. | Parcours observé par le Journal du Net avec un interlocuteur fictif. L’agent a omis des informations et mal restitué un point exprimé pendant l’entretien. La coordination des étapes et la fidélité du livrable se jugent séparément. [P16] |
| Ventes : préparer un suivi après un signal entrant | Le Worker peut enrichir un contact, mettre à jour le CRM, préparer un message et coordonner le rendez-vous. | Parcours décrit par Delos et son communiqué. Le catalogue ne prouve ni la disponibilité de toutes les opérations sur l’instance acheteur ni l’amélioration du taux de transformation. [P08, P09, P19] |
| Opérations et communication : intégrer des Workers dans une équipe établie | Meilleurtaux Placement rapporte le déploiement de premiers Workers auprès de la direction, en communication et opérations. | Témoignage nominatif du président reproduit par un financeur. Volumes, tâches détaillées, taux de reprise et économies client non fournis. [P19] |
| Développement : préparer une modification et sa revue | Le profil technique est présenté comme capable d’écrire des tests, commenter une pull request ou entretenir la documentation dans l’environnement connecté. | Cas d’usage du catalogue ; aucun taux d’acceptation, taux de régression ou délai causé par l’outil dans cette source. [P03, P20] |

## Diagnostic fonctionnel et commercial

L’offre réunit identité métier, réception de demandes, procédures, connexions et retour du travail sous un même profil. Le cas JDN documente l’intérêt d’une orchestration couvrant téléphone, SMS, courriel et document. Le même cas montre que la livraison réussie d’un fichier ne prouve pas la couverture des faits recueillis. La proposition paraît la plus lisible pour des missions à consignes explicites dont un humain peut contrôler le résultat à coût raisonnable. C’est une inférence sur son positionnement. [P01, P16]

**Trois conditions changent le diagnostic.** Une compétence est un document chargé en contexte ; l’exécution dépend des actions réellement exposées par la connexion. Le choix du niveau d’initiative et les règles orientent la conduite du Worker, alors que l’authentification détermine ce que l’outil autorise. Selon l’aide, une règle de confirmation peut suspendre l’action lorsqu’elle est appelée ; elle reste une consigne et ne se propage pas automatiquement aux sous-agents. Enfin, l’aide décrit une connexion limitée à un Worker par organisation Teams : le raccordement du suivant déconnecte le précédent. C’est une contrainte du canal documenté, pas une limite générale sur le nombre de Workers dans Delos. [P05–P08, P10–P11]

**L’unité économique demeure la mission acceptée.** Au 17 octobre, Aikiwi a relevé un plan Team à 50 €/mois avec 40 000 crédits ; Koïno avait publié un relevé similaire. Le test du JDN décrit une autre grille au crédit et chiffre deux productions à 3 172 crédits, soit environ 3,5–4 € dans ses conditions. Cet exemple exclut notamment le temps de contrôle éditorial. Les conditions de forfait, la date et le périmètre doivent accompagner toute estimation. L’essai gratuit annoncé et le tarif des sièges bureautiques ne suffisent pas à reconstituer un coût par mission. [P13–P18]

**Ce qui n’est pas encore mesuré.** La part de missions exécutées sans assistance, les corrections par type d’usage, la rétention payante propre aux Workers, et le coût des erreurs ne sont établis par aucune des pièces de cette sélection. Des séries de missions terminées, leurs résultats acceptés ou repris, des factures par périmètre et des cohortes commerciales datées permettraient de distinguer usage récurrent, utilisation exploratoire et gain économique.

## Registre de preuves

Chaque entrée désigne une pièce distincte. Les pages d’un même éditeur partagent une provenance. L’autoattestation hébergée chez Microsoft reste rédigée par Delos ; les relevés tarifaires externes peuvent avoir la même page source. Date de consultation : 14 novembre 2026.

| ID | Publication | Ce qu’elle apporte | Limite |
|---|---|---|---|
| P01 | [Delos, Premiers pas](https://help.delos.so/categories/workers/first-steps) | Profil, manager, directives, missions programmées ou événementielles. | Documentation fournisseur. |
| P02 | [Delos, cycle du Worker](https://help.delos.so/categories/getting-started/workers-on-delos) | Triage puis exécution ; transfert conservant mémoire et configuration. | Les intégrations peuvent demander une reconfiguration. |
| P03 | [Delos, catalogue des Workers](https://delos.so/fr/workers) | Exemples de rôles par fonction, configuration sur mesure. | Profils et gains attendus relèvent de l’offre. |
| P04 | [Delos, création et cockpit](https://help.delos.so/categories/workers/create-workers) | Écrans activité, profil, comportement, ressources, communication, intégrations. | Parcours documenté et illustré ; aucun chronométrage. |
| P05 | [Delos, Behavior Studio](https://help.delos.so/categories/workers/behaviour-studio) | Procédures et références, quatre niveaux d’initiative, chargement à la demande des outils, journal d’activité. | La compétence constitue un apport de connaissances. |
| P06 | [Delos, garde-fous](https://help.delos.so/categories/workers/rules-for-workers) | Trois conduites, plafond de vingt règles, absence d’héritage automatique aux sous-agents. | Les règles restent des instructions comportementales. |
| P07 | [Delos, canaux](https://help.delos.so/categories/workers/workers-communication-channels) | Slack, Teams, Telegram et messagerie interne ; consentement administrateur pour Teams. | Le guide documente un Worker à la fois par organisation Teams. |
| P08 | [Delos, prise en main des intégrations](https://help.delos.so/categories/workers/workers-integrations) | OAuth, clé API, identifiants d’application propres au client ; choix de compte. | Une clé saisie peut n’être vérifiée qu’à la première action. |
| P09 | [Delos, couverture d’intégration](https://delos.so/fr/integrations) | Offre revendiquée de plus de 3 000 intégrations ; exemples de tâches par famille. | Quantité revendiquée, sans test de chaque service ou opération. |
| P10 | [Microsoft Marketplace, Delos Workers](https://marketplace.microsoft.com/en-us/product/wa200011292) | Référencement Teams, compte et Worker Delos préalables, administrateur, services mail/calendrier à connecter. | Description déposée par Delos. |
| P11 | [Microsoft Learn, Publisher Attestation](https://learn.microsoft.com/en-us/microsoft-365-app-certification/teams/delos-workers) | L’éditeur détaille données Teams, métadonnées d’exécution, cloud et identifiants traités. | Autoévaluation datée du 7 juillet 2026. |
| P12 | [Delos, Assistant](https://help.delos.so/applications/assistant) | Application conversationnelle distincte capable d’actions multiétapes. | Ne pas transférer ses quotas ou son packaging au Worker. |
| P13 | [Delos, offre Workers](https://delos.so/fr/pricing) | Essai annoncé et offre flexible. | Aucun prix unitaire fiable dans la version textuelle lue. |
| P14 | [Delos, abonnements de la suite](https://help.delos.so/categories/credits-billing/subscription-plans) | Paliers et quotas de la suite, option étudiante. | Ce n’est pas la grille de coût d’une mission Worker. |
| P15 | [Delos, technologie](https://delos.so/fr/tech) | RAG, mémoire, modèles, orchestration et journalisation annoncés. | Les performances et mécanismes d’isolement restent déclaratifs dans cette page. |
| P16 | [Journal du Net, essai de Lucia](https://www.journaldunet.com/intelligence-artificielle/1555809-ia-comment-j-ai-recrute-un-employe-virtuel-avec-delos/) | Parcours multicanal exécuté, deux productions, propos omis, coût de crédits estimé par le testeur. | Un métier et deux sorties, coût humain exclu. |
| P17 | [Aikiwi, relevé du 17 octobre](https://aikiwi.com/fr/ia/workers-delos/) | 50 €/mois, 40 000 crédits sur le plan Team observé. | Relevé historique de la page commerciale. |
| P18 | [Koïno, étude documentaire](https://www.koino.fr/articles/delos-avis-ai-workers-2026) | Relevé daté du 6 octobre et séparation offre suite/Worker. | L’auteur précise ne pas avoir testé le produit. |
| P19 | [Bpifrance, communiqué du 16 septembre](https://presse.bpifrance.fr/plus-de-300-entreprises-clientes-et-2-000-workers-qui-travaillent-en-continu-la-scale-up-parisienne-veut-faire-passer-lia-du-statut-doutil-a-celui-de-collegue/?lang=fra) | Déclarations de traction et témoignage attribué au président de Meilleurtaux Placement. | Pièce de communication d’un financeur ; les agrégats n’établissent pas la rétention du produit. |
| P20 | [Delos, profil développement](https://delos.so/solutions/developpement) | Revue de modifications, tests, documentation et outils annoncés. | Aucune mesure autonome du résultat. |
