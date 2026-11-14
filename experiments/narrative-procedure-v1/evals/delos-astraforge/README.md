# Deux tests appariés de rédaction et benchmark AstraForge

14 novembre 2026. A = point d’entrée de main au commit 7000c86a7e54cafc68c5bb5ada9aeed5df186aae. B = procédure expérimentale au commit 6655ae1f9fb3bf3d1a115c8aaae8913e31f72eea. Quatre agents de rédaction isolés, une production par cas et par méthode. Un brief et un corpus figés par cas, sans transfert du one-pager vers le two-pager. Un évaluateur distinct a reçu les briefs et les textes sous identifiants X/Y, sans les journaux ni les branches. Société X=B et Y=A ; produit X=A et Y=B.

| Fixture et mandat | A : appréciation /10, mots, fichiers, octets | B : appréciation /10, mots, fichiers, octets | Interprétation |
|---|---|---|---|
| [Delos société](company-brief.txt) · opportunité d’un entretien | [10, 307, 2, 13 159](company-A.md) | [9, 270, 12, 28 758](company-B.md) | A distingue mieux prise de rendez-vous et décision après entretien. B est plus court et prépare l’échange. |
| [AI Worker](product-brief.txt) · décision de pilote support | [10, 445, 9, 49 381](product-A.md) | [9, 493, 10, 28 415](product-B.md) | A précise le lot, les exceptions et le seuil de gain. B apporte une cadence de suivi, un dénominateur d’adoption et la réutilisation. |

[Évaluation à l’aveugle](blind-review.md) · [Benchmark documentaire et protocole commun](benchmark.md).

Les journaux JSON homonymes consignent les fichiers de méthode effectivement chargés. Les octets UTF-8 dédupliqués indiquent la matière consultée ; les enveloppes d’outils, raisonnements, répétitions et tokens de sortie en sont exclus. Les mots sont comptés par wc -w sur le Markdown avec titres et sources. Les pages sont des pages logiques Markdown. L’échantillon et le juge unique permettent un diagnostic local. Aucune mesure de coût modèle, de latence ou de pagination PDF.

## Conséquence pour la migration

Conserver la sortie rapide de main pour un mandat simple. À la qualification société, exiger deux décisions distinctes si un entretien doit produire les preuves nécessaires à la suite. Dans le profil produit, ajouter au bloc pilote le lot, la proportion d’exceptions, le comparateur, la grille de qualité et le seuil fixé avant mesure. Conserver la cadence et la réutilisation de B pour un pilote en conditions réelles. Rejouer avec plusieurs tirages et un second juge sur des secteurs différents avant de modifier le routage par défaut. Ce commit conserve les méthodes comparées et ajoute les résultats.
