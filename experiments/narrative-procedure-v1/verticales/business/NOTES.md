# Transfert et observation — 14 novembre 2026

## Matériaux et arbitrages

| Source examinée | Mécanisme retenu | Traduction locale | Ce qui demande une preuve distincte |
|---|---|---|---|
| [Composition du rapport long](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/docs/NARRATIVE.md) | Plan argumentatif déterminé par la décision, preuve servie au bloc et retour des encarts | Chaque rôle transmet un résultat précis et une condition de retour. Le profil relie une évolution économique aux blocs dépendants | Une validation de structure ne démontre pas la pertinence de la thèse |
| [Contrats versionnés](https://github.com/achard-arnaud/skills-notes-and-storytelling/tree/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/templates) | Chaque format change les obligations de preuve | Six fixtures couvrent les formats de classe business. Les options de comparaison restent sous un périmètre identique. Le seuil de décision dépend d’un volume encore inconnu | Les fixtures contrôlent un sous-ensemble des contrats. Les fourchettes de pages et les benchmarks longs restent à éprouver sur un rendu complet |
| [Skill publique Equity Research, LSEG sur le dépôt Anthropic](https://github.com/anthropics/financial-services/blob/main/plugins/partner-built/lseg/skills/equity-research/SKILL.md) | Interroger les sources en fonction de leur contribution à la thèse | Distinguer hypothèse externe, exposition locale et test de révision | La disponibilité des données de marché et des outils dépend du contexte utilisateur |
| [Skill publique Deal Screening, Anthropic](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/private-equity/skills/deal-screening/SKILL.md) | Extraire les faits du dossier avant de les confronter aux critères | Relier la décision à un seuil explicite, puis demander le minimum de donnée nécessaire | Les critères de fonds sont spécifiques à leur mandat |

## Essai rédigé — note de décision synthétique

**V1.** Le fournisseur chiffre le lancement à 1 200 euros et annonce huit euros économisés par dossier. À 150 dossiers, le lancement est amorti. Déployer le traitement.

**Diagnostic.** L’égalité arithmétique est exacte. L’économie de huit euros par dossier et le volume éligible restent à vérifier. Le verdict de déploiement engage donc des ressources à partir d’une hypothèse. Le contrôle de statut échoue sur le premier objet de décision.

**V2.** Mandater une mesure sur des dossiers éligibles avant d’engager les 1 200 euros. L’annonce fournisseur de huit euros évités par dossier place le seuil à 150 dossiers sous cette hypothèse. Si la mesure ramène l’économie à quatre euros, le seuil double à 300. Le maintien du traitement manuel reste préférable tant que le volume et l’économie observés sur le même horizon ne couvrent pas le lancement. La responsable opérations vérifie les exceptions et rapporte le volume réellement traitable.

## Relecture et reproduction

Exécuter python check.py pour contrôler les six fixtures et les deux objets de décision. receipt.json conserve les résultats. Le défaut V1 est injecté pour éprouver le détecteur de promotion abusive. V2 corrige sa cause et conserve les mêmes entrées synthétiques. Ce replay déterministe mesure la couverture structurelle et une erreur de statut. La note a été rédigée et relue par le même agent. Qualité éditoriale indépendante, généralisabilité, exhaustivité des obligations de chaque template et pagination physique restent à vérifier.
