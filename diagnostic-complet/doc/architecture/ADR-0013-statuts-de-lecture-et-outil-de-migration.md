# ADR-0013 — Statuts de lecture, validation humaine et outil de migration du profil

- **Statut** : accepté
- **Date** : 2026-11-10
- **Décisions liées** : D41 (outil de migration), D42 (statuts de lecture et validation humaine)
- **Tickets** : RF-06, #291

## Contexte

François a demandé de relancer les recherches sur les concurrents et le marché, de considérer le complément sur l'industriel comme validé et vérifié, de rechercher la notion de double cerveau sur internet, et de traiter RF-06.

## Décision

1. **D41 — outil de migration.** `kb_migrate.py` déclare le profil de run sur un index qui n'en porte pas. Essai à blanc par défaut ; `--apply` exige une sauvegarde hors de la base et écrit un reçu (empreintes et nombres, aucun contenu). Il refuse si le schéma, le lexique ou le profil diffèrent : un nouveau lexique demande une réingestion, pas une étiquette. Il ne touche ni aux atomes ni aux sources.
2. **D42 — deux statuts nouveaux dans le registre d'exemples.** `read_at_source` : la page ou le texte officiel a été lu en entier ; l'atome n'est pas promu en fait vérifié. `human_validated` : François a validé, à la date inscrite dans `decisions` ; les limites écrites restent en vigueur. Aucun agent ne pose `human_validated`.

## Conséquences

- Validation de l'industriel : périmètre limité à la relation client et au programme de gestion des connaissances ; le déploiement et les gains restent hors validation.
- La promotion d'un atome en fait vérifié suit toujours le circuit humain de la base ; le registre public ne le remplace pas.
- Concurrents : aucune cible de disponibilité confirmée sur cinq ; Engie Impact est cédée à un tiers, ce qui sort cette branche de la comparaison.
- Marché : les seuils du reporting de durabilité (450 millions d'euros, 1 000 salariés) et les échéances de l'article 10 sont lus au Journal officiel.
