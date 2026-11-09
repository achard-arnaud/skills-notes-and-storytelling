# Réconciliation du board R2 avec le code livré

Constat : `runs/r2/board.json` marque 16 tickets `planned`. Ce fichier appartient à la passe Codex en cours et n'est pas modifié ici. Cette table propose un statut à partir des preuves présentes à `d29882b`. Le statut définitif relève du coordinateur de la passe R2, après revue.

| Ticket | Sortie attendue | Preuve présente | Statut proposé | Reste à faire |
|---|---|---|---|---|
| R2-01 | `docs/R2-SCOPE.md` | Fichier présent, mandat daté | `verified-candidate` | Reçu manquant. |
| R2-02 | `docs/R2-INTAKE.md` | Absent ; `docs/INTAKE-POLICY.md` présent | `partial` | Matériaux privés, pas de sortie publique. |
| R2-03 | `writing.py` | `writing.py`, 16 tests `test_writing.py` (scaffold from-scratch, refus de prose antérieure) | `verified-candidate` | Reçu. |
| R2-04 | `writing.py` (révision) | Tests de delta, baseline, invalidation des revues | `verified-candidate` | Reçu ; à confirmer par Codex. |
| R2-05 | `loopback.py` | `loopback.py`, 17 tests | `verified-candidate` | Reçu. |
| R2-06 | `docs/RELATIONS.md` | `contracts/relation-types.json`, 4 tests, fixture | `verified-candidate` | Revue sémantique (voir `CONTRACT-AUDIT.md`). |
| R2-07 | `docs/SKILLS-CATALOG.md` | Absent | `planned` | Hors dépôt par mandat. |
| R2-08 | `docs/SKILLS-CATALOG.md` | Absent | `planned` | Dépend de R2-07. |
| R2-09 | `docs/KB.md` | Présent ; conversions PDF/DOCX non démontrées | `partial` | Tests de conversion. |
| R2-10 | `kb.py` | `kb.py`, 21 tests | `verified-candidate` | Reçu. |
| R2-11 | `crawl.py` | Absent | `planned` | Décision de passation : prochaine unité, après accord Codex. |
| R2-12 | `docs/R2-RESULTS.md` | Absent | `planned` | Dépend de R2-10 et R2-11. |
| R2-13 | `docs/GRAPH1-BRIDGE.md` | Absent | `planned` | Dépôt Graph1 hors scope GitHub courant. |
| R2-14 | `runs/r2/DELIVERY.md` | Absent | `planned` | Dépend de R2-13. |
| R2-15 | `runs/r2/QA.json` | Absent | `planned` | Dépend de R2-06, R2-08, R2-14. |
| R2-16 | `runs/r2/RESUME.md` | Absent | `planned` | Dépend de R2-15. |

Règle : `verified-candidate` signifie « le code et ses tests existent à `d29882b` ». Ce n'est ni un reçu, ni une validation éditoriale.
