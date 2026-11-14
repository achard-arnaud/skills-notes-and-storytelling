# Choisir une méthode depuis une décision

Entrer par la question du bloc de rédaction et sa verticale. Le catalogue indique les formats pour lesquels une fiche est proposée. Une méthode peut servir plusieurs verticales. Les liens entre fiches représentent des dépendances d’analyse ou des pistes de recherche. Une relation causale dans une note exige des preuves propres au cas.

## Parcours de diagnostic

| Question | Paquet à ouvrir | Sortie consommable et décision suivante |
|---|---|---|
| Quel événement externe changerait la décision ? | PESTEL puis, si la captation de valeur est en jeu, cinq forces ou comparaison concurrentielle | Signal daté, exposition locale et mécanisme plausible. Conserver les signaux hors périmètre avec leur motif. |
| Quelle capacité interne permet de réagir ? | Chaîne de valeur puis compétences centrales ou VRIO | Activité, dépendance et capacité observée. Le lien à la marge reste une hypothèse en l’absence de mesure. |
| Quelles options méritent une épreuve ? | SWOT/TOWS à partir des deux paquets | Option avec facteurs sources, alternative et condition d’abandon. |
| Quel public et quelle offre tester ? | Segmentation, ICP, mix et PMF selon le besoin | Segment hypothétique, usage, alternative actuelle et observation de valeur. RICE sert aux arbitrages comparables. |
| Quel coût et quel volume rendent l’option viable ? | TCO pour les alternatives, économie unitaire pour le seuil, ROI ou VAN pour la décision d’investissement | Scénarios datés, dénominateurs explicites, bornes et risque de double comptage. |
| Comment exécuter puis réviser le choix ? | FCS, plan d’exécution et business plan | Hypothèses conditionnelles, ressources, responsables et mesure qui rouvre la décision. |

**Exemple synthétique.** Un fournisseur annonce 3 € économisés par dossier éligible pour 24 000 € annuels. Le bloc économique reçoit une recommandation conditionnelle. Le seuil de 8 000 dossiers suppose que les 3 € se matérialisent. Le plan d’exécution reçoit une demande de mesure portant à la fois sur l’éligibilité et sur le gain récupérable. Si le pilote révise le gain à 2 €, le seuil devient 12 000 dossiers. Rouvrir la projection financière et la décision, conserver les observations de marché indépendantes.

## Périmètre et alternatives examinées

- Une note autonome correspond à une question susceptible d’inverser une décision. Un alias et une variante conservent un ID commun quand leurs données et leurs conclusions sont substituables.
- Le catalogue sert la sélection à la demande. La skill conserve l’orchestration et importe un AnalysisResult lié aux claims et aux blocs. Une méthode enseignée, un outil de mesure, un cadre de représentation et un format éditorial ont des fonctions différentes.
- La segmentation qualitative garde une valeur exploratoire avant disponibilité des volumes. Une population atypique peut révéler un autre segment et mérite un traitement explicite.
- Le niveau de zoom C4 dépend de la question. Les modes de défaillance sont instruits pour les interfaces critiques. La grille pédagogique locale conserve ses six types de pages et permet d’évaluer le transfert indépendamment du rendu.
- La traçabilité, l’analyse du besoin et l’évaluation sont rapprochées du référentiel PMI-PBA. La correspondance est thématique. L’accréditation d’un cursus ou d’une certification demanderait une évaluation distincte.
- Le réexamen d’une option s’appuie sur une hypothèse opposée et l’observation qui la départagerait. Ce contrôle est transposable aux quatre verticales. Les conclusions issues de plusieurs méthodes utilisant le même claim conservent une seule origine probatoire.

## Sources transverses

[Harvard Business School, The Value Chain](https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-value-chain.aspx) relie configuration des activités et sources d’avantage. [PMI, PMI-PBA](https://www.pmi.org/certifications/business-analysis-pba) précise le rôle des besoins, parties prenantes et bénéfices attendus. [McKinsey, Have you tested your strategy lately?](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/have-you-tested-your-strategy-lately) propose des questions pour mettre les choix sous tension. Chaque fiche précise ses propres références et ses conventions locales.

Ouvrir [le catalogue de lecture](CATALOGUE.md) pour choisir une fiche. Le [registre JSON](catalog.json) alimente le sélecteur. Pour reprendre un run, conserver méthode, version, question, source, bloc et résultat. Réouvrir les dépendances modifiées à la reprise.

## Exécution

Depuis la racine de la skill candidate, exécuter `python mba/taxonomy/tools/resolve_method.py --route business --template one-pager --method business.break-even --block thesis`. Le sélecteur vérifie le couple dans le registre de verticales, résout le bloc et renvoie la fiche et le contrat de sortie. Le modèle applique le protocole avec les preuves du RUN. Le reçu historique porte sur la précédente version. Pour le produit, sélectionner par exemple `python mba/taxonomy/tools/resolve_method.py --route produit --intent traction-commerciale --method product.adoption --block retention`. Les finalités et blocs disponibles sont déclarés dans le manifeste produit.

Rejouer le banc indépendant avec `python mba/taxonomy/validation/replay.py`. Les 25 contrôles couvrent les conventions de flux, les hypothèses de coût, la priorisation et les cohortes. Les oracles qualitatifs des 39 fiches servent à la revue du raisonnement. Une revue humaine sur des données réelles reste nécessaire pour qualifier la pertinence de la recommandation.
