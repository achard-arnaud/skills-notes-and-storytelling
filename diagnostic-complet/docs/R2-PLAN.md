# Seconde passe — ordre d’exécution

16 tickets / 64 microétapes / 8 lots. Recherche source, collecte corporate et intake peuvent progresser en parallèle ; rédaction et publication attendent leurs prérequis. Chaque tâche conserve un paquet ciblé, sorties, limites et reçu. Les 72 anciens tickets restent des snapshots du premier bootstrap.

## R2-01 — Cadrer sources et destinations

Prérequis : aucun. Sortie : `docs/R2-SCOPE.md`.

1. Épingler dev des deux dépôts.
2. Identifier namespaces autorisés.
3. Lire instructions applicables.
4. Consigner couverture et manquants.

## R2-02 — Rapatrier les matériaux accessibles

Prérequis : R2-01. Sortie : `docs/R2-INTAKE.md`.

1. Inventorier les 15 textes joints.
2. Récupérer dossier et titres GreenYellow.
3. Récupérer transcript R1 original.
4. Tracer conversation inaccessible et exports.

## R2-03 — Transférer rédaction from-scratch

Prérequis : R2-01. Sortie : `writing.py`.

1. Lire source et pin.
2. Refuser prose antérieure.
3. Préparer scaffold depuis preuves.
4. Tester frontière core et encarts.

## R2-04 — Transférer révision itérative

Prérequis : R2-03. Sortie : `writing.py`.

1. Résoudre baseline et empreinte.
2. Calculer fermeture de dépendances.
3. Préserver hors delta.
4. Invalider les seules revues affectées.

## R2-05 — Transférer loopback graphe et piliers

Prérequis : R2-01. Sortie : `loopback.py`.

1. Lire loopback Candidatures.
2. Mesurer types densité et isolés.
3. Qualifier nouveaux matériaux par pilier.
4. Proposer au plus trois actions sans mutation.

## R2-06 — Réconcilier catalogue des relations

Prérequis : R2-05. Sortie : `docs/RELATIONS.md`.

1. Comparer prose et schéma 12 versus 8.
2. Ajouter catalogue versionné.
3. Étendre contrat compatible.
4. Tester divergence et types inconnus.

## R2-07 — Décomposer douze opérations atomiques

Prérequis : R2-03, R2-04, R2-05. Sortie : `docs/SKILLS-CATALOG.md`.

1. Définir déclencheurs et exclusions.
2. Initialiser dans répertoire personnel.
3. Approfondir invariants et contre-exemples.
4. Valider syntaxe et frontières.

## R2-08 — Éprouver et installer les skills

Prérequis : R2-07. Sortie : `docs/SKILLS-CATALOG.md`.

1. Évaluer sur tâches sans historique.
2. Corriger les écarts observés.
3. Sauvegarder chaque skill séparément.
4. Vérifier état réconcilié et catalogue.

## R2-09 — Préparer tous les formats sources

Prérequis : R2-02. Sortie : `doc/architecture/ADR-0001-kb-contrat-documentaire.md`.

1. Préserver bytes et hashes.
2. Extraire ZIP sans traversée.
3. Convertir PDF DOCX HTML en texte.
4. Tenir compte des doublons et conversions.

## R2-10 — Atomiser et construire KB incrémentale

Prérequis : R2-09. Sortie : `kb.py`.

1. Découper phrases et items.
2. Conserver tables et code signalés.
3. Maintenir occurrences et versions.
4. Tester idempotence et liens de preuve.

## R2-11 — Collecter site corporate au périmètre explicite

Prérequis : R2-01. Sortie : `crawl.py`.

1. Lire robots et sitemaps.
2. Parcourir liens internes.
3. Checkpoint frontier et erreurs.
4. Relire couverture et fichiers non extraits.

## R2-12 — Enrichir graphe depuis corpus complet disponible

Prérequis : R2-10, R2-11. Sortie : `docs/R2-RESULTS.md`.

1. Intégrer textes corporate sourcés.
2. Créer nœuds et liens structurels.
3. Rattacher piliers comme candidats.
4. Exécuter loopback récent et relever dettes.

## R2-13 — Préparer projection KB privée Graph1

Prérequis : R2-12. Sortie : `doc/architecture/ADR-0007-projection-graph1.md`.

1. Préserver graphe formation gelé.
2. Créer namespace business indépendant.
3. Préparer MD sources occurrences et shards.
4. Vérifier hashes endpoints et identité privée.

## R2-14 — Publier KB et graphe sur dev Graph1

Prérequis : R2-13. Sortie : `runs/r2/DELIVERY.md`.

1. Créer commit skip CI sans force.
2. Relire namespace au SHA livré.
3. Vérifier baseline canonique inchangée.
4. Tracer couverture et liens de reprise.

## R2-15 — Revoir et intégrer seconde passe business

Prérequis : R2-06, R2-08, R2-14. Sortie : `runs/r2/QA.json`.

1. Relire différences source/cible.
2. Exécuter tests et régression.
3. Enrichir tickets existants avec limites.
4. Intégrer dev skip CI et vérifier refs.

## R2-16 — Livrer capsule et décisions suivantes

Prérequis : R2-15. Sortie : `runs/r2/RESUME.md`.

1. Stabiliser reçus et board.
2. Persister outputs privés utiles.
3. Maintenir gate éditoriale distincte.
4. Restituer acquis limites et prochaine unité.
