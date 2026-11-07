# Reprise — passe H (passation bootstrap)

Date : 7 novembre 2026. Base `main` = `74a6354` (inchangé). `dev` avant cette passe = `d29882b`.

## État fiable

- Diagnostic : `docs/HANDOVER-DIAGNOSTIC.md`.
- Gate local équivalent à la CI désactivée : `docs/LOCAL-GATE.md`. Validateur racine PASS ; 13 tests pédagogiques PASS avec navigateur ; rendu landscape + `--verify` PASS ; 105 tests de passation PASS.
- Board R2 désynchronisé (16 `planned`, code livré) : propositions dans `runs/handover/R2-RECONCILIATION.md`. `runs/r2/board.json` non modifié.
- Contrat racine modifié à `d29882b` : delta additif (8 → 12 types), revue humaine du delta encore à faire : `runs/handover/CONTRACT-AUDIT.md`.
- Empreintes des reçus : 71/72 concordantes ; DC-002 (AGENTS.md, modifié par R2) expliqué : `runs/handover/freshness.json`.
- QA visuelle HTML : faite sur le fixture synthétique uniquement (`runs/handover/qa/study-desktop.png`).

## Interdits

- Pas de PR, pas de `workflow_dispatch`, pas de modification de workflow.
- Pas de promotion vers `main`.
- Pas de contenu privé (R1, transcript, corpus, contacts) dans Git.
- Chaque commit porte `[skip ci]`. Intégration fast-forward uniquement, sans force.

## Gates humains ouverts

- HITL-258 : piliers, trame et side stories (François).
- Revue sémantique du delta contrat racine avant toute promotion.
- Confirmation de la mention « voix Sarah » dans les fichiers publics.

## Prochaines actions

1. Vérifier après push : `origin/dev` au SHA attendu, aucun run Actions pour ce `head_sha`.
2. Coordonner avec Codex avant R2-11 (collecte corporate), pour éviter le conflit d'écriture sur `dev`.
3. Produire les reçus R2 uniquement après revue, et les intégrer dans `runs/r2/`.
