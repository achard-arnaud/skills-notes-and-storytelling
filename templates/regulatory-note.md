# Regulatory note — v0.1.0

Classe `legal-reglementaire`, libellé « Legal & réglementaire ». Source métier — [Regulatory Bootstrap](../skills/regulatory-bootstrap/SKILL.md). Statut candidate. Longueur par défaut trois à cinq pages denses, orientation adaptée à la matière.

## Contrat d’entrée

Réglementation et version, juridiction, secteur et sous-segments, date d’arrêté, public expert, format et corpus initial. Choisir le mode de génération et une dimension primaire existante — business, product ou technical. La classe décrit la finalité juridique du livrable; la dimension décrit l’angle sectoriel.

## Chaîne de production

Cadrage → recherche officielle → guides et sources tier-one → confrontation → fragments et claims sourcés → mécanismes sectoriels → scaffold → rédaction Top-Down → relectures juridique, sectorielle et anti-répétition → rendu éventuel et inspection finale.

Appliquer les seuils et le journal de [recherche](../skills/regulatory-bootstrap/references/research-budget.md). Pour chaque run approfondi, viser 50 % d’effort documentaire primaire, respecter le plancher de 30 % et exécuter au moins 100 requêtes complémentaires distinctes. Déclarer le budget réel et les limites dans le dossier de méthode.

## Contenu canonique et scaffold

Utiliser `contracts/output-spec.schema.json` pour l’enveloppe du contenu et `contracts/scaffold.schema.json` pour les questions et claims de chaque section. Porter les paramètres juridiques et locators dans les sections et les sources. Le champ historique `decision` du scaffold décrit ici la question juridique ou la thèse descriptive. Les champs `sections` accueillent les sections souples suivantes.

1. Cadrage juridique et tension sectorielle, trois à cinq conclusions descriptives.
2. Carte globale conditionnelle, légende et source éditable.
3. Objet, périmètre territorial et matériel, acteurs, qualification, seuils et exceptions.
4. Cycle de vie, preuves, droits et interactions normatives.
5. Appareil productif, données, processus, compétences, dépendances et économie de conformité.
6. Supervision, recours, calendrier et sanctions conditionnelles.
7. Portée des conclusions, incertitudes de fond et bibliographie datée.

Examiner les huit axes de la skill et expliquer les absences d’effet matériel établi. Distinguer droit, lecture attribuée, observation et inférence. Les recommandations et plans d’action correspondent aux variantes demandées explicitement.

## Contrat de composition

Appliquer [style-contract.md](../references/style-contract.md) et [editorial-review.md](../skills/regulatory-bootstrap/references/editorial-review.md). Les phrases exposent directement le mécanisme et ses conditions. Les pieds de page et fins de containers servent à la pagination, aux sources et aux légendes discrètes. Conserver la méthode et les contrôles dans les sidecars du run.

Le binding transporte le contenu. Le scaffold organise les questions. Le moteur de rendu gère géométrie, styles et export selon le support choisi. L’ajout de ce template constitue un contrat de contenu; les preuves d’export dépendent du run et du renderer réellement exécuté.

## Critères de validation

Vérifier version et statut des textes, finalité et rôle de chaque acteur, exceptions, calendrier, sanctions, indépendance et fraîcheur des lectures. Contrôler le journal de recherches, le budget primaire et la revue anti-répétition. Relier chaque conséquence à sa disposition et à sa condition limite. Inspecter les pages après le dernier changement lorsqu’un export est produit.

La fixture synthétique décrit les observables et les échecs. Sa présence vérifie le routage et le contrat. Le passage à validated requiert revue humaine et fixture concluante selon la politique du dépôt.
