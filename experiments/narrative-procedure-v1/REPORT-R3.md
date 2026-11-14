# Industrialisation des quatre verticales — 14 novembre 2026

## Décision de migration

Garder un rédacteur commun, une procédure de reprise par bloc et sept méthodes analytiques indépendantes. Le format et la verticale déterminent le scaffold. La question résiduelle détermine la méthode. Le [protocole de reprise](refs/reprise.md) conserve la provenance, le cutoff, les dépendances et la prochaine action.

## Couverture

Le [registre](verticales/registry.json) dessert douze couples. Le [dépouillement historique](history/README.md) ajoute six jumeaux à douze fixtures existantes. Le contrôle du plafond trouve quatre cas au maximum par template. Une friction provient d’une revue de texte et une correction d’une demande reliée à la sortie révisée. Quatre autres cas inversent volontairement un motif positif observé. La recherche directe des conversations était indisponible. Le fil courant, ses sorties et quatre documents archivés accessibles constituent le corpus effectivement examiné.

## Transfert et contrôles

La [revue des sources](HARVEST.md) détaille les mécanismes retenus ou adaptés. Le [contrat de composition](NARRATIVE.md) relie les quatre profils et leurs retours métier. Les [sept cartes MBA](mba/registry.json) ont chacune une question, des entrées, une procédure, une limite, un résultat lié aux claims et un témoin négatif. Le contrôle de dispatch valide les sept résultats avec le schéma canonique et exerce une liaison réelle au bloc de thèse business. Les exercices restent synthétiques.

Les [huit mutations fonctionnelles](verticales/paired-controls.json) sont acceptées par les anciens contrôles qui ignorent les nouveaux champs. Les nouveaux contrôles les rejettent et acceptent les quatre corrections. Les six cas historiques et les sept paires MBA passent leurs oracles. Ces mesures portent sur des champs structurés ou annotés. La lecture d’une note libre et l’évaluation auprès d’un décideur demandent une revue distincte.

## Rejeu apparié sur un comité d’investissement

Deux agents en contextes frais reçoivent le même brief synthétique et les mêmes quatre sources. Le parcours A suit la skill racine du précédent snapshot main 16bcb43. B utilise le candidat consolidé, le profil business et la carte économie unitaire. Les agents disposent de la commande qui journalise les fichiers ouverts. Le bref commun est exclu. Les deux textes ont été examinés par le coordinateur connaissant les bras.

| Mesure | A | B |
|---|---:|---:|
| Lectures de méthode, répétitions incluses | 11 | 14 |
| Octets effectivement lus | 49 597 | 28 959 |
| Conditions de décision retrouvées dans le texte | 5/5 | 5/5 |

Les cinq éléments sont le seuil de 8 000 commandes, le taux de deux tiers, le scénario conditionnel de perte de 7 800 euros, la limite de l’échantillon local et une règle de décision pour un pilote. Les deux réponses les donnent. B explicite aussi la formule de valeur et un prérequis de faisabilité. A détaille la stratification et la fixation préalable du niveau de confiance. Sur cette paire, les ressources spécialisées coûtent trois lectures supplémentaires et réduisent le volume documentaire de 41,6 %. Cette métrique exclut prompts système, calcul, génération, cache et coûts. La densité opérationnelle est rapportée par couverture de décisions et volume lu. La qualité globale et le coût total restent indéterminés.

[Brief](evals/volume/input.md) · [A](evals/volume/A.md) · [B](evals/volume/B.md) · [mesures et empreintes](evals/volume/metrics.json).

## Reproduction

Depuis le dossier de la skill, exécuter les commandes suivantes avec Python et jsonschema. Pour les contrôles pédagogiques, le checkout doit contenir le SHA inscrit dans son manifeste.

    python scripts/check_dispatch.py
    python history/replay.py
    python mba/replay.py
    python verticales/replay.py --repo /chemin/checkout
    python verticales/compare_controls.py --snapshot /chemin/snapshot-epingle

La publication concerne la branche expérimentale. Les contrôles de rendu physique et l’effet réel sur les publics restent à vérifier.
