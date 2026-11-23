# Contrat opérationnel S3 : routes, agents, artefacts et statuts

## Point de routage obligatoire

Appliquer au début de chaque nouveau mandat S3, y compris une demande qui nomme déjà une skill. Les reprises restent sur leur route et leurs pins enregistrés. Une surface dépourvue de routeur exécutable suit le même contrat avec un coordinateur manuel.

1. **Cadrer.** Résoudre le sujet et le distinguer du dépôt qui fournit la méthode. Relever les questions, le livrable, le lecteur, la date d’arrêt, les preuves attendues, les droits et la limite de collecte. Le contexte de l’opérateur sert à cadrer uniquement s’il est pertinent et autorisé. Les constats externes gardent leurs propres sources.
2. **Planifier.** Épingler une révision Git unique. Déterminer la profondeur, puis le domaine principal selon la question qui gouverne le résultat demandé. Ajouter une contribution pour chaque question secondaire distincte et attribuer à chaque question un seul propriétaire. Déclarer la raison des exclusions pertinentes. En cas d’ambiguïté qui change sensiblement la route ou la collecte, résoudre ce point avant de lancer le travail.
3. **Vérifier la capacité.** Résoudre, à cette révision, les entrées canoniques depuis [les cinq domaines S3](domain-analysis.md), vérifier la disponibilité de l’exécuteur et n’ouvrir que les manifests et méthodes retenus. Le plan inclut la raison du choix, les références prévues et les conditions d’arrêt. Choisir le format après le domaine et la profondeur. Si une capacité manque, qualifier le blocage ou consigner un repli manuel compatible avec le mandat. Une révision invérifiable laisse le contrôle de version ouvert.
4. **Transmettre.** Donner à chaque agent un identifiant de question et son propriétaire, l’objectif, les entrées et versions autorisées, les droits/outils accordés, les références et chemins de travail, le résultat attendu, le contrôle de retour, le budget et l’arrêt. Le coordinateur possède le plan et traite toute demande de changement. Le destinataire retourne statut, sorties et références réellement consultées, preuves, limites, contrôle effectué et écart éventuel. Une sortie hors périmètre, non traçable ou sur pins incohérents retourne à son propriétaire pour correction.
5. **Clôturer.** Relier chaque sortie aux preuves et statuts des claims. Appliquer les contrôles finaux du domaine. Pour un appel direct, joindre une synthèse du reçu au livrable et garder la trace détaillée dans la destination privée de travail si elle existe. Pour un cas complet, garder le plan et le reçu dans le dossier privé et lier les états et artefacts des tentatives A0–A4 effectivement observées.

### Reçu et niveau de preuve

| Élément | Trace minimale |
| --- | --- |
| Mandat et plan | Identifiant ou objectif expurgé, sujet, questions et propriétaires ordonnés, profondeur, révision, raison de la route et exclusions utiles |
| Entrées et lectures | Chemins et versions des manifests/méthodes réellement ouverts, référence immuable ou empreinte si disponible, sections lues, locators des sources consultées, origine et rôle du contexte, exclusions, omissions et motif d’arrêt |
| Exécution | Par intervention, acteur ou surface, état et référence d’événement si exposée. Distinguer planifiée, manuelle déclarée, invocation observée, indisponible et non exécutée. Une invocation exige un événement attribuable à l’exécuteur, lié au plan et à la sortie. Un lien de distribution atteste une disponibilité locale. |
| Résultat | Référence aux constats et statuts des claims, écart et limites, méthode et résultat de chaque contrôle, approbation humaine si recueillie |
| Cas complet | Référence de l’état, étapes et tentatives réellement exécutées. Le mode direct laisse A0–A4 non exécuté. |

Un contrôle mécanique valide les éléments qu’il peut inspecter. Les lectures non exposées par le harnais restent déclaratives ou inconnues. Toute trace publique est expurgée des prompts privés, captures, secrets et éléments de mémoire personnelle.

### Recette initiale

[Le jeu de données et l’oracle synthétiques](../tests/fixtures/s3-routing-mixed-v1.json) préparent la recette sans source privée. Exécuter l’entrée seule, puis comparer avec l’oracle. Le mandat centré sur l’offre attend Produit → Business. Le mandat centré sur la viabilité du financement inverse l’ordre. Une demande d’étude complète oriente vers le brief A0–A4.

[#378](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/378) porte le validateur et les cas négatifs du reçu. [#377](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/377) porte la recette des méthodes. [#297](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/297) porte la recette d’étude complète.

## Domaines, profondeur et exécution

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

En mode direct, lire les manifests des seuls domaines retenus et les références de chaque question. Réutiliser les locators et consigner les limites dans le reçu, puis choisir le support. Un arc et un support sont deux choix ; une réponse courte peut se contenter d’une structure de décision.

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
