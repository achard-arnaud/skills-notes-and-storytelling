# Contrat opérationnel S3 : routes, agents, artefacts et statuts

Choisir la profondeur avec le lecteur, le nombre de questions et la preuve requise. Un besoin ciblé suffit au mode direct. Un mandat à plusieurs phases, une collecte étendue ou un besoin de reprise appelle un dossier A0–A4.

| Quand | Appeler | Entrée minimale | Sortie / contrôle | À éviter |
| --- | --- | --- | --- | --- |
| La question porte sur valeur, opérations, économie | Business analysis | Entité, périmètre, décision, date | Mécanisme de valeur et preuve ; one/two-pager ou analyse structurée | Assimiler économie du vendeur et réalité du client |
| La question porte sur l’offre et son usage | Product analysis | Produit/version, utilisateur, tâche, fenêtre | Fiche ou comparaison ; usage, cohorte et fit bornés | Confondre capacité déclarée et usage observé |
| La question porte sur un système ou un choix technique | Technical analysis | Frontière, interfaces, contraintes, décision | Verdict, preuve, alternatives, retour arrière | Déduire le verdict du template |
| L’objectif porte sur un apprentissage | Pedagogical AI Learning | Public, acquis, compétence, pratique | Explication, exercice ou séquence ; succès et transfert observables | Imposer le six-pages à une demande courte |
| La question porte sur les obligations | Regulatory Bootstrap | Juridiction, date, version, activité | Note ou étude ; applicabilité et sources officielles | Appliquer le budget de recherche approfondie au mode direct |
| Les preuves doivent devenir un récit | Selecting Narrative Schema | Intention déclarée, claims, limites, objection et falsificateur | Arc, sections et encarts candidats | Inventer un angle, transformer un encart en preuve primaire |
| Une évolution pose un problème de preuve ou de méthode | Revue locale ou loopback du cas | Constat, référence, action, test de sortie | Reprise limitée du cas ou proposition BUILD traçable | Confondre incident et autorisation de modifier le moteur |

En mode direct : lire le seul manifeste pertinent et les références de la question. Réutiliser les locators ; consigner les omissions et l’arrêt, puis choisir le support. Un arc et un support sont deux choix ; une réponse courte peut se contenter d’une structure de décision.

En mode complet : matérialiser le brief, puis borner les lots de collecte macro, méso et micro. Étendre la recherche lorsque le mandat et les lacunes le justifient ; arrêter selon le budget et le critère de sortie du brief. Scoper une éventuelle délégation par lot : objectif, sources autorisées, emplacement de sortie et test de retour. L’agent de revue reçoit les éléments nécessaires à son contrôle et laisse les données privées à leur emplacement.

| Qui agit / quand | Contrat et artefact | Statut ou garantie |
| --- | --- | --- |
| Auteur du brief | `intake.json` → `workflow/case-process.json` | Cas isolé, sélection explicite, pins |
| Collecteur A0 | `evidence`, captures et couverture | Lecture déclarée, refus de provenance A1 si source insuffisamment lue |
| Analyste A1 et propriétaires S3 | `graph`, claims et relations | Fait, attribution, inférence, hypothèse, recommandation, inconnu |
| Architecte narratif A2 | `scaffold` + `narrative_ref` optionnel à l’échelle du moteur | Structure et preuve liées et hachées ; encarts candidats |
| Rédacteur A3 | Paquet par section → `composition` | Mapping de claims stable ; binding payload séparé si rendu demandé |
| Relecteur A4 | Trois revues + `narrative_review_ref` si profil sélectionné | Blocage si constat ouvert ; reçu séparé du rendu si requis |
| Humain responsable | Validation dans le suivi du produit ou au point de livraison | Approbation explicite de fond ; distincte du statut `passed` |
| Responsable BUILD | Issue, PRD, ADR, test, PR/CI | Choix documenté et vérifié sur SHA ; aucune promotion éditoriale par la CI |

L’état du moteur est `pending → running → passed`, avec rejet journalisé et invalidation des étapes dépendantes. Les statuts de template et d’encart ont leurs propres registres. Dans ce profil, l’encart sort comme `candidate` et reste hors rendu. Les promotions d’encarts historiques suivent leur contrat, jamais celui d’un cas neuf par simple renommage.

Retourner une preuve absente à A0 ; un claim ou une lacune de classement à A1 ; la structure à A2 ; la prose à A3 ; le rendu à A4. En mode direct, revenir à une collecte ciblée ou à la skill propriétaire. Reprendre sur les versions épinglées. Quand le défaut est reproductible hors cas, créer un BUILD avec fixture synthétique et revue d’ADR ; aucun apprentissage automatique ne réécrit les règles. Voir [A0–A4](case-process.md), [règles éditoriales](editorial-and-research-quality.md) et [ADR-1010](../docs/architecture/ADR-1010-narrative-selection.md).
