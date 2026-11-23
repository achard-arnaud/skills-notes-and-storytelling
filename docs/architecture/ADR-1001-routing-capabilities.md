# ADR-1001 — Routage et capacités d’analyse

- Statut : accepté comme principe documentaire ; implémentation selon les contrats publiés.
- Date : 2026-11-13.
- Portée : dépôt entier ; les choix spécifiques restent dans leur périmètre.
- Autorité : accord utilisateur du 13 novembre sur l’architecture cible et sa publication documentaire ; demande du 23 novembre 2026 rendant obligatoire le point de routage S3 et sa traçabilité.
- Tickets : [#23](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/23), [#42](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/42), [#165](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/165), [#378](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/378), [#377](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/377).

## Contexte

Le catalogue mêle intention, méthode et format. Cette ambiguïté multiplie les variantes et rend les transferts fragiles.

## Décision

Tout nouveau mandat S3 traverse un **point de routage unique** avant chargement des méthodes, recherche ou délégation. Le [contrat opérationnel](../../references/s3-operations.md#point-de-routage-obligatoire) définit les entrées, le plan, les handoffs, le reçu et le repli. Une demande explicite de skill fixe une préférence que le routeur vérifie. Une ambiguïté déterminante ou une capacité indisponible déclenche le repli prévu au contrat.

Les cinq domaines déclarés par [ADR-1009](ADR-1009-domain-skills.md) sont les propriétaires de questions. Le routeur choisit un domaine principal selon le résultat demandé, une contribution secondaire par question distincte et la profondeur directe ou complète. Le choix du template intervient après ces décisions. Chaque méthode est sélectionnée selon la question, les preuves disponibles et son contrat au SHA du run. Une capacité décrit déclencheur, entrées, sortie, limites et contrôle ; elle peut être une procédure ou une référence.

Le coordinateur fait respecter les permissions, limite le contexte et valide le retour de chaque agent. Les instructions racine fixent la politique, les instructions locales encadrent leur sous-arbre, et les manifests déclarent le contenu des skills. Les agents peuvent déléguer seulement dans le périmètre et avec les droits explicitement transmis par le coordinateur. Tout changement de propriétaire, de sujet ou de permissions revient au coordinateur.

Un routeur exécuté doit produire un plan traçable puis un reçu. La preuve distingue le plan, l’invocation attribuable, les lectures déclarées, les contrôles mécaniques et la revue humaine. Le fonctionnement uniforme prime sur le confort d’un dispatch implicite par mot-clé ou d’un routage redéfini dans chaque skill. Le coût attendu est une trace courte par appel et un point d’intégration par harnais.

## Conséquences et vérification

| Niveau | État constaté au [SHA audité de dev](https://github.com/achard-arnaud/skills-notes-and-storytelling/tree/5538660446704c319baeaefafa7ac6946ab75b0e) | Preuve attendue |
| --- | --- | --- |
| Disponibilité documentaire | Cinq skills de domaine et leurs manifests ; liens de distribution locaux dans `.agents/skills/` | Résolution des chemins et versions au SHA sélectionné |
| Route et contrôle d’un appel direct | Le coordinateur applique les instructions. Le sélecteur narratif et les profils techniques ont leurs propres commandes. | Plan suivi, reçu et événement pour chaque invocation déclarée native |
| Cas complet | `manual_agent` dans [le manifeste](../../workflow/case-process.json). [Le moteur](../../scripts/case_runtime.py) contrôle intake, références épinglées, tentatives et sorties A0–A4 ; l’agent effectue le travail. | Plan conservé à côté du dossier de cas, puis états et artefacts de la tentative concernée |
| Cible exécutable | Premier lot dans [#378](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/378). | Une commande et des tests pour construire/valider le plan direct et contrôler son reçu. Les étapes d’adoption A0–A4 et le dispatch natif demandent leurs propres preuves. |

Les clés, enums et reprises existants restent compatibles jusqu’à une migration versionnée. La politique est applicable via repli manuel dès publication documentaire. Seuls les contrôles effectivement exécutés, sur la révision citée, peuvent figurer comme réussis. Le pilote mixte vérifie l’étanchéité entre offre, organisation, dépôt méthode et contexte personnel. Son oracle est décrit dans [le mapping opérationnel](../../references/s3-operations.md#recette-initiale).

## Réexamen

Réexaminer si le pilote permet un faux statut d’exécution, si le propriétaire d’une question varie avec le template ou si deux domaines partagent un contexte non autorisé. Le responsable BUILD ouvre un écart avec preuve, révision, contrat concerné et contre-test. Les autres principes sont accessibles dans [l’index](README.md).

## Raccord au PRD #258

Le choix explicite entre appel direct et workflow complet est documenté dans le mapping S3. Voir le [PRD canonique](../specifications/PRD-258-selecteur-narratif.md) et [ADR-1010](ADR-1010-narrative-selection.md).
