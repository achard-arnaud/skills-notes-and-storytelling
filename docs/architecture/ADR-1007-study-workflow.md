# ADR-1007 — Workflow d’étude en quatre phases et compétences conditionnelles

- Statut proposé pour intégration ; direction favorable exprimée dans la conversation du 14 novembre 2026. L’acceptation de ce texte exact reste à enregistrer.
- Portée : convergence des parcours main, diagnostic-complet et essais de refonte.
- Parent : #294 ; compléments ADR-1001 à ADR-1006.
- Implémentation : lots #295, #296 et #297 ; ce document seul n’active aucune capacité.

## Contexte
Les deux essais ont montré une conformité à des briefs appauvris sans reproduction de la substance attendue. diagnostic-complet fournit des contrats probatoires, de contexte et de rédaction itérative ; le candidat apporte des finalités et méthodes. La synthèse analytique doit pouvoir exister avant les blocs du récit. La multiplication de procédures indépendantes par verticale rendrait la convergence plus coûteuse.

## Choix proposé
Conduire l’étude en quatre phases identifiables : contexte/recherche, analyse/synthèse, direction narrative, rédaction/revue/livraison. Un point d’entrée guide le parcours et charge conditionnellement les profils. Les compétences spécialisées rendent des résultats indépendants du support final. La donnée et l’état appartiennent au projet ; une skill expose la procédure. Les phases ne fixent ni un nombre d’agents ni un nombre obligatoire de skills.

L’analyse se rattache d’abord à des questions et preuves. Le brief relie ensuite résultats et claims aux blocs. Une source ou une analyse modifiée invalide les descendants concernés. L’ancien binding aux blocs reste lisible jusqu’à migration vérifiée.

## Alternatives examinées
Une skill monolithique suffit pour un cas court mais garantit mal la profondeur et la reprise lorsque les contrats sont implicites.
Quatre moteurs autonomes par verticale créeraient des procédures et stocks concurrents.
Un chaînage obligatoire de nombreuses skills et un bus dès le premier cas augmenteraient le coût d’exploitation sans bénéfice démontré.
Le choix proposé conserve une orchestration légère avec des frontières vérifiables.

## Conséquences
Réutiliser le socle diagnostic-complet plutôt que créer un moteur de remplacement. Intégrer les méthodes du candidat après mapping. Adapter l’hygiène de transitions de Candidatures sans copier ses cardinalités de CV ni ses contraintes d’ATS dans les études business. Les profils business et produit peuvent se combiner sur une même étude.

Les contrôles distinguent conformité, preuve, substance analytique, narration, rendu et appréciation humaine. Une étude exploratoire conclut par ses constats et inconnues ; une recommandation dépend d’un mandat décisionnel explicite.

## Vérification et réexamen
#297 exige un cas complet, un cas de réserve, la reprise après analyse et une correction de source. Réexaminer si le coût de coordination dépasse le gain de reprise, si les résultats analytiques ne modifient pas la compréhension, ou si un profil exige un moteur spécifique. La CI ne remplace pas l’appréciation du lecteur.
