# ADR-1010 — Un paquet narratif, deux parcours S3

**20 novembre 2026 · Choix d’implémentation du pilote · Recette humaine ouverte**

Sources : [PRD #258](../specifications/PRD-258-selecteur-narratif.md), [ticket maître](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/258) et [ADR-1009](ADR-1009-domain-skills.md). Voir [preuve et limites](../planning/AUDIT-258-S3.md).

## Décision

Un profil déclaratif maintient les six piliers candidats, les arcs et le routage de revue. Un seul sélecteur partage ce contrat entre la note directe et le cas A0–A4. Les méthodes S3 possèdent l’analyse ; le catalogue des supports possède les formats et le moteur existant possède les transitions. Le sélecteur choisit selon l’intention fournie et retourne les informations manquantes en cas d’ambiguïté. Le format peut changer sans réanalyser le fond.

Le raccord est opt-in à l’intake. A2 fournit une demande locale à sa tentative. Le moteur extrait les preuves A0/A1, valide le scaffold et épingle cette demande. A3 lit une section ; A4 a un reçu de routage et ses trois revues. Le résultat du moteur peut passer avec une approbation éditoriale encore ouverte. Les encarts du profil restent candidats, avec des références au tronc. Toute promotion d’encart ou migration d’un cas relève de son propre mandat et de sa propre preuve.

## Conséquences

Un même claim conserve son texte, son statut et ses références dans les deux parcours. Le mode direct utilise un ledger fourni ; le mode complet l’attache aux artefacts épinglés. La classification et les formats restent indépendants des preuves ; aucune règle du moteur ne fixe le nombre de piliers. Le profil peut évoluer par version. Les cas existants peuvent continuer sur leur BUILD épinglé. Les schémas du moteur acceptent les champs additionnels de manière explicite et leur interprétation reste liée à l’opt-in.

L’invalidation active suit les étapes et dépendances. Le moteur n’a pas de reprise sélective au claim. Un changement de preuve relance les étapes touchées dans la même instance. Une étude indépendante conserve ses pins. Le profil n’étend ni les capacités de recherche/rendu ni la gouvernance de publication.

## Alternative et réexamen

Un sélecteur par domaine réduit le raccord initial ; il multiplie les contrats et tests de preuve. Un nouveau moteur simplifierait certaines interfaces ; il dupliquerait l’état, les gardes et les reçus. Réutiliser le moteur et mesurer M1–M4 sur le pilote. Si le chemin direct exige un effort excessif ou perd des preuves, réduire son paquet avant l’extension. Figer les piliers après revue comparative main/S2/S3. Un choix de vocabulaire ou une migration demandent une décision séparée.
