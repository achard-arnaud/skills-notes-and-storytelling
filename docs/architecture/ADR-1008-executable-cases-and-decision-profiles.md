# ADR-1008 — Cas exécutables et profils de décision technique

- Date : 2026-11-17.
- Statut : mise en œuvre autorisée par François dans cette session ; aucun nouveau template promu.
- Objectif : rendre exécutables les frontières RUN/BUILD (ADR-1004) et le loopback (ADR-1005), sans multiplier les skills.
- Issues : [#338](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/338), [#339](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/339).

## Écart établi

La skill installée avait déjà src/runtime.py, note_runtime.py et des profils quatre couches absents de ce main. Le main avait, à l'inverse, dix templates dont trois absents de l'installation. Le schéma historique des claims imposait au moins un fragment à une inconnue : il encourageait la fausse preuve.

## Décision et prescriptions

Conserver les templates du dépôt et réconcilier les ajouts runtime. Ajouter un manifeste A0 acquisition → A1 graphe typé → A2 scaffold → A3 écriture → A4 revue, consommé par case_runtime.py. Les règles et l'I/O communs sont une release hachée ; chaque dépôt possède ses bindings de templates. Les cas nouveaux sont isolés dans data/cases, les anciens bundles restent historiques. Un changement d'empreinte bloque la reprise ; une correction explicite invalide les descendants et conserve l'historique. Le journal réel porte appels, acteur déclaré, tentative, hashes et rejets ; usage fournisseur inconnu sans mesure.

Séparer format, type de décision et criticité. Sept profils dans config/technical-decisions.json partagent technical-decision.schema.json et technical_decision.py : rupture ADR, dette/risque, migration/TCO, impact écosystème, bootstrap/DX, run readiness et verdict PoC. Chaque profil impose ses sections, preuves ou inconnues, alternatives et hypothèses falsifiables. Adopt exige des seuils explicites tous satisfaits par des mesures déclarées observées et hachées. Cela ne prouve pas l'acceptation du CTO.

Loopback : axe architecture/bugfix/CI/runtime/skill, état et preuves hachés, relation aux ADR/objectifs/contraintes, expérience bornée ou no_change, avant/après sourcés ou inconnus. Validation sans mutation. La conformité du document reste une revue distincte.

## Alternatives, conséquences et objection forte

Prose seule : coût faible mais aucun consommateur ne refuse les transitions incohérentes. Sept nouvelles skills : duplication et dérive. Orchestrateur autonome : coût d'exploitation et d'intégration disproportionné au besoin actuel. Moteur local et profils : retenu, avec coût réel de tests et de versioning. Les étapes manuelles restent une frontière de confiance : le moteur observe les artefacts soumis, pas toutes les actions d'un hôte agentique. Les copies de release sont contrôlées en CI ; une divergence répétée déclenche l'extraction en paquet partagé.

## Hypothèses falsifiables et réexamen

Si un cas de transfert ne peut finir sans modifier le moteur, revoir la séparation profil/méthode. Si un incident échappe aux contrôles, ajouter d'abord sa reproduction, puis corriger la couche fautive et le contrat si nécessaire. Si une dépendance de rendu n'est pas épinglée ou une preuve ne résout plus son origine, la reprise doit bloquer ; sinon l'hypothèse de traçabilité est réfutée.

Vérifications : tests de chaîne positive, sauts, empreintes périmées, références étrangères, mapping de claims, inconnu numérique et Adopt non mesuré ; validation de release et de profils en CI. Le contrôle structurel n'approuve ni un ADR ni un template. Les inconnues de coûts/temps demeurent explicites.


## Renforcement exécutable du 17 novembre 2026

La reproduction d'un renderer.args de type string accepté par check_contracts réfute
la couverture supposée du manifeste, sans invalider la décision de séparer RUN/BUILD.
Le schéma case-process.schema.json devient prescriptif et consommé avant init.
Les liens adapter/payload-schema/refs épinglées sont contrôlés ; les profils sans
adapter ne créent aucun cas lorsqu'un rendu est demandé. Régressions négatives
et chaîne valide : tests/test_case_runtime.py. Détails et limites dans
[le diagnostic](manifest-contract-hardening-2026-11-17.md).

## Raccord au PRD #258

Le paquet narratif du pilote est optionnel à l’intake et conserve le validateur du mémo technique. Voir le [PRD canonique](../specifications/PRD-258-selecteur-narratif.md) et [ADR-1010](ADR-1010-narrative-selection.md).
