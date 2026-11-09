# Plan du run — 72 microétapes / 8 epics

Mandat du 7 novembre 2026. Plan de ce sous-projet isolé, pas autorisation globale du programme #48. Les epics indexent des thèmes ; les sprints séquencent les dépendances ; les piliers structurent l’analyse.

## Quatre phases

1. Explorer et journaliser le bootstrap (E1/E2).
2. Renforcer, relier et réorchestrer les tickets (E3/E4/E5).
3. Implémenter par sprints avec validations locales (E6/E7).
4. Revoir, intégrer dev sans CI, préparer le dry run privé et les choix éditoriaux (E8).

## Séquence de sprints

| Sprint | Périmètre | Gate |
|---|---|---|
| S1 | Exploration et transfert source/cible | Couverture et matrice de transfert sourcées |
| S2 | Piliers, contexte, board et interfaces | DAG, scopes, critères et paquets définis |
| S3 | Import, qualification et graphe | Tests positifs/négatifs ciblés |
| S4 | Récit libre, side stories et HTML | Contrôles de liens/échappement et revue de structure |
| S5 | Non-régression, reprise, livraison et candidats | Ref dev vérifiée ; aucune promotion main |

Les recherches source/cible/contexte sont parallèles ; les unités dépendantes restent séquentielles. Chaque unité écrit son artefact, produit un reçu, puis retire ses entrées du paquet actif. Deux corrections maximum par blocage. Les tokens exacts du runtime restent inconnus : mesures locales de mots/octets seulement.

## E1 — Explorer et délimiter le mandat

Owner historique : #48. Phase 1.

### DC-001 — Épingler les deux dépôts et branches · [#193](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/193)

Relever HEAD source, main et dev cible avec les fichiers effectivement consultés.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : aucune.
- Sortie : `docs/BASELINE.md`.
- Acceptation : Les SHA et la couverture des lectures sont explicites.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-002 — Lire les instructions et frontières · [#189](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/189)

Résoudre les instructions racine et isoler le périmètre autorisé du sous-projet.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-001.
- Sortie : `AGENTS.md`.
- Acceptation : Mandat courant, absence de CI et absence de promotion main sont écrits.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-003 — Inventorier les capacités réellement présentes · [#188](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/188)

Distinguer méthode, schéma, script exécutable et projet non implémenté.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-002.
- Sortie : `docs/BUSINESS-TRANSFER.md`.
- Acceptation : Aucune capacité planifiée n’est présentée comme livrée.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-004 — Rattacher le programme existant · [#186](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/186)

Relier le chantier aux owners #48–55 sans remplacer les anciennes US.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-003.
- Sortie : `docs/OWNERSHIP.md`.
- Acceptation : Chaque epic local référence un owner existant et son delta.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-005 — Identifier les huit HIL source · [#229](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/229)

Retrouver les identifiants exacts dans le code et leurs sous-thèmes.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-004.
- Sortie : `docs/SOURCE-TRANSFER.md`.
- Acceptation : Huit HIL vérifiés ; climat et vents restent sous-thèmes.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-006 — Inventorier les matériaux GreenYellow · [#200](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/200)

Consigner rapport disponible, apports et conversation inaccessible.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-005.
- Sortie : `docs/INTAKE-POLICY.md`.
- Acceptation : Couverture réellement lue et manquants séparés ; pas de source privée en Git.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-007 — Séparer méthodes publiques et corpus privé · [#190](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/190)

Définir les destinations autorisées pour captures, fixtures et vues.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-006.
- Sortie : `docs/INTAKE-POLICY.md`.
- Acceptation : La fixture publique est synthétique ; aucun R1 ni contact privé publié.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-008 — Borner les décisions techniques · [#191](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/191)

Écarter base de données, serveur et automatisation non nécessaires au premier cycle.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-007.
- Sortie : `docs/DECISIONS.md`.
- Acceptation : Le prototype est local et indépendant des templates canoniques.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-009 — Valider le jalon exploration · [#209](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/209)

Consolider gaps, hypothèses et critères de passage à la conception.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-008.
- Sortie : `runs/bootstrap/exploration.json`.
- Acceptation : Les limites de couverture sont consignées, sans faux verdict exhaustif.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E2 — Bootstrap narratif Sri Lanka

Owner historique : #51. Phase 1.

### DC-010 — Cartographier arc et brief · [#194](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/194)

Extraire leurs fonctions et définir l’équivalence mandat/business case.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-009.
- Sortie : `docs/SOURCE-TRANSFER.md`.
- Acceptation : Chronologie historique non imposée au récit business.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-011 — Transférer HIL vers vues analytiques · [#201](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/201)

Documenter le multi-rattachement pertinent par section et paragraphe.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-010.
- Sortie : `docs/PILLARS.md`.
- Acceptation : Aucun quota ni obligation de huit chapitres cible.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-012 — Distinguer graphe et scaffold lecteur · [#187](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/187)

Séparer topologie probatoire et ordre éditorial.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-011.
- Sortie : `docs/NARRATIVE.md`.
- Acceptation : Une relation de graphe ne dicte pas une transition narrative.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-013 — Transférer le lineage des side stories · [#192](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/192)

Conserver provenance, placement, payoff et retour au tronc.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-012.
- Sortie : `docs/NARRATIVE.md`.
- Acceptation : Les retours requis sont résolvables ; les encarts ne créent pas de preuves.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-014 — Adapter zoom et dézoom · [#198](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/198)

Passer de site/actif à portefeuille, entreprise, marché et système.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-013.
- Sortie : `docs/NARRATIVE.md`.
- Acceptation : Tout dézoom indique mécanisme et utilité du retour.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-015 — Adapter comparateurs et contrechamps · [#215](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/215)

Borner périmètre, temporalité, baseline et facteurs de confusion.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-014.
- Sortie : `docs/RESEARCH.md`.
- Acceptation : Un benchmark fournisseur ne prouve pas un ROI local.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-016 — Transférer revue paragraphe et réécriture · [#196](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/196)

Séparer revue structurelle, probatoire, éditoriale et humaine.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-015.
- Sortie : `docs/NARRATIVE.md`.
- Acceptation : Un texte modifié perd sa revue antérieure ; aucune approbation humaine simulée.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-017 — Adapter disposition et couverture · [#202](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/202)

Suivre inclus, side story, recherche requise et écart motivé.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-016.
- Sortie : `docs/NARRATIVE.md`.
- Acceptation : Aucun élément écarté n’est supprimé de la provenance.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-018 — Valider la matrice reuse adapt exclude · [#195](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/195)

Faire relire le transfert par la perspective cible.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-017.
- Sortie : `docs/SOURCE-TRANSFER.md`.
- Acceptation : Voix historique et plafonds de longueur exclus explicitement.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E3 — Adapter les piliers et le raisonnement business

Owner historique : #49. Phase 2.

### DC-019 — Définir le contrat de mandat · [#199](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/199)

Question, audience, scope et exclusions gouvernent le rapport.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-009.
- Sortie : `docs/INTERFACES.md`.
- Acceptation : Une instance sans question de mandat est refusée.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-020 — Séparer industrie et corporate · [#206](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/206)

Délimiter opérations sectorielles et fonctions commerciales/support transverses.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-019.
- Sortie : `docs/PILLARS.md`.
- Acceptation : Un même cas peut être relié aux deux avec justification, sans fusion.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-021 — Séparer data et IA · [#197](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/197)

Distinguer instrumentation/qualité/BI de modèles, agents et décisions.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-020.
- Sortie : `docs/PILLARS.md`.
- Acceptation : Un problème de données n’est pas qualifié automatiquement de problème IA.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-022 — Ajouter économie et gouvernance candidates · [#205](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/205)

Définir finance du modèle, valeur, organisation, risques et adoption.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-021.
- Sortie : `docs/PILLARS.md`.
- Acceptation : Les axes sont candidats et révisables selon mandat.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-023 — Définir la recherche macro micro Porter · [#211](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/211)

Traiter ces méthodes comme questions d’enquête déclenchées par un besoin.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-022.
- Sortie : `docs/RESEARCH.md`.
- Acceptation : Pas de grille remplie mécaniquement ni de score sans preuve.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-024 — Définir collecte et benchmark des use cases · [#204](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/204)

Relier problème, utilisateur, décision, données, workflow et preuve.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-023.
- Sortie : `docs/RESEARCH.md`.
- Acceptation : Déploiement cible et cas vendeur restent distincts.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-025 — Définir économie et ROI · [#208](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/208)

Exiger baseline, coût complet, horizon, attribution et sensibilité.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-024.
- Sortie : `docs/RESEARCH.md`.
- Acceptation : Les gains sans baseline restent hypothèses et non business case prouvé.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-026 — Rattacher les compétences existantes · [#207](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/207)

Mapper capacités de recherche/architecture/rendu sans créer de skills installées.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-025.
- Sortie : `docs/CAPABILITIES.md`.
- Acceptation : Frontières fonctionnelles et absence d’installation sont explicites.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-027 — Stabiliser les interfaces expérimentales · [#210](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/210)

Valider les contrats locaux sans modifier manifests racine.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-026.
- Sortie : `docs/INTERFACES.md`.
- Acceptation : Fixtures négatives requises ; aucun template_type global ajouté.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E4 — Assurer contexte et reprise

Owner historique : #55. Phase 2.

### DC-028 — Définir la capsule de reprise · [#212](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/212)

Fixer mandat, état, décisions et trois prochaines actions.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-009.
- Sortie : `runs/bootstrap/RESUME.md`.
- Acceptation : Reprise possible sans relire le chat.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-029 — Implémenter les paquets ciblés · [#203](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/203)

Charger seulement les entrées déclarées avec empreintes.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-028.
- Sortie : `context.py`.
- Acceptation : Chemin extérieur ou fichier absent refusé.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-030 — Mesurer le budget réellement chargé · [#234](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/234)

Compter octets et mots des fichiers, tokenizer exact inconnu si absent.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-029.
- Sortie : `context.py`.
- Acceptation : Le dépassement refuse le paquet ; aucune économie fictive.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-031 — Valider DAG et tâche prête · [#217](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/217)

Détecter cycles et prérequis absents avant sélection.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-030.
- Sortie : `context.py`.
- Acceptation : Les fixtures cycle et dépendance inconnue échouent.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-032 — Définir writer et handoff agent · [#218](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/218)

Réserver chemins distincts, résultats courts et coordinateur intégrateur.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-031.
- Sortie : `docs/CONTEXT-PROTOCOL.md`.
- Acceptation : Les mutations Git et clôtures restent coordonnées.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-033 — Implémenter checkpoint et contrôle de fraîcheur · [#228](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/228)

Sauvegarder empreintes et détecter entrée modifiée.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-032.
- Sortie : `context.py`.
- Acceptation : Une entrée modifiée invalide la reprise au lieu de passer silencieusement.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-034 — Définir drop logique et compaction · [#214](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/214)

Retirer les documents des futurs paquets sans prétendre purger le runtime.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-033.
- Sortie : `docs/CONTEXT-PROTOCOL.md`.
- Acceptation : Aucune commande ne promet de vider la fenêtre réelle.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-035 — Borner réparations et blocages · [#213](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/213)

Deux corrections puis réserve explicite et poursuite des branches indépendantes.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-034.
- Sortie : `docs/CONTEXT-PROTOCOL.md`.
- Acceptation : L’écoulement du temps ne vaut ni réponse ni approbation.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-036 — Éprouver une reprise indépendante · [#220](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/220)

Faire lire capsule et paquet à un agent sans historique.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-035.
- Sortie : `runs/bootstrap/recovery-review.md`.
- Acceptation : Prochaine action, limites et interdits retrouvés depuis les artefacts.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E5 — Orchestrer issues epics et sprints

Owner historique : #55. Phase 2.

### DC-037 — Créer l’index du chantier · [#219](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/219)

Créer une issue de run reliée au programme historique.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-009.
- Sortie : `board.json`.
- Acceptation : Issue distante relue et correspondance locale persistée.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-038 — Créer les huit epics thématiques · [#216](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/216)

Créer les index de travail sans nouvelles autorités métier globales.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-037.
- Sortie : `board.json`.
- Acceptation : Huit liens parents disponibles et pas de doublons de run.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-039 — Déposer 72 microtickets · [#223](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/223)

Chaque unité a objectif, entrées, sorties, dépendances et acceptation.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-038.
- Sortie : `board.json`.
- Acceptation : Tous les IDs locaux correspondent à une issue distante.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-040 — Intégrer les sous-plans agents · [#221](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/221)

Faire remonter les propositions source, cible et contexte au plan consolidé.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-039.
- Sortie : `docs/PLAN.md`.
- Acceptation : Contributions intégrées ; les agents ont des scopes disjoints.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-041 — Relier les dépendances de tickets · [#225](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/225)

Ajouter liens cliquables vers prérequis, epic et propriétaire historique.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-040.
- Sortie : `board.json`.
- Acceptation : DAG local valide et liens GitHub réels.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-042 — Renforcer les critères négatifs · [#222](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/222)

Inscrire les échecs attendus avant code des contrats.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-041.
- Sortie : `docs/PLAN.md`.
- Acceptation : Hypothèse non promue, retour invalide et reprise périmée sont couverts.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-043 — Ordonnancer les sprints · [#224](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/224)

Séparer exploration, conception, infrastructure, narration et revue.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-042.
- Sortie : `docs/PLAN.md`.
- Acceptation : Les tâches dépendantes ne sont pas parallélisées aveuglément.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-044 — Générer le board lisible · [#226](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/226)

Produire vue Markdown par état, epic et sprint.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-043.
- Sortie : `BOARD.md`.
- Acceptation : Statuts et liens dérivés du même board JSON.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-045 — Valider le jalon de lancement · [#227](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/227)

Relecture du plan renforcé avant délégation de code.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-044.
- Sortie : `runs/bootstrap/planning.json`.
- Acceptation : Périmètre, entrées, contrôles et garde main/CI explicites.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E6 — Implémenter ingestion et graphe

Owner historique : #50. Phase 3.

### DC-046 — Importer Markdown avec localisateurs · [#231](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/231)

Découper par blocs et conserver provenance et lignes exactes.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-027, DC-036, DC-045.
- Sortie : `runtime.py`.
- Acceptation : Relire chaque fragment dans le fichier source original.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-047 — Stabiliser les identités de fragments · [#230](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/230)

Rendre un même import déterministe et détectable.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-046.
- Sortie : `runtime.py`.
- Acceptation : Deux imports identiques donnent les mêmes IDs et empreintes.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-048 — Qualifier les claims sans promotion automatique · [#232](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/232)

Conserver le statut supplied_claim des matériaux fournis.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-047.
- Sortie : `runtime.py`.
- Acceptation : Aucun claim importé n’est verified_fact.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-049 — Valider les références et IDs · [#237](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/237)

Contrôler unicité et résolution des sources/fragments/claims/piliers.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-048.
- Sortie : `runtime.py`.
- Acceptation : Références pendantes et IDs dupliqués refusés.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-050 — Valider les faits qualifiés · [#235](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/235)

Exiger revue de vérification et sources réellement lues pour verified_fact.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-049.
- Sortie : `runtime.py`.
- Acceptation : Une synthèse seule ne suffit pas à qualifier un fait.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-051 — Construire le graphe probatoire · [#243](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/243)

Exporter nœuds et relations typées sans confondre navigation et causalité.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-050.
- Sortie : `runtime.py`.
- Acceptation : Relations inconnues ou endpoints pendants refusés.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-052 — Préparer la carte de recherche · [#233](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/233)

Documenter questions, rebonds, inconnues et stop conditions.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-051.
- Sortie : `docs/RESEARCH.md`.
- Acceptation : Les pistes exploratoires restent hors causalité probatoire.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-053 — Ajouter fixtures positives et adversariales · [#236](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/236)

Couvrir import, preuve, scaffold et retours.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-052.
- Sortie : `tests/test_runtime.py`.
- Acceptation : Les cas négatifs échouent pour la raison attendue.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-054 — Valider le sprint de données · [#238](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/238)

Exécuter tests locaux et enregistrer les limites.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-053.
- Sortie : `runs/bootstrap/data.json`.
- Acceptation : Commande, code retour, couverture et résultat conservés.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E7 — Implémenter narration et vues HTML

Owner historique : #51. Phase 3.

### DC-055 — Créer une étude synthétique multi-piliers · [#239](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/239)

Montrer des axes distants et un récit de taille libre.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-027, DC-045.
- Sortie : `fixtures/synthetic.json`.
- Acceptation : Aucune donnée réelle confidentielle dans la fixture.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-056 — Matérialiser le reader scaffold · [#241](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/241)

Ordonner sections et paragraphes indépendamment des piliers.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-055.
- Sortie : `render.py`.
- Acceptation : Un nombre de sections différent des piliers est accepté.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-057 — Valider les side stories · [#240](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/240)

Contrôler parent, claims, raison hors tronc et return_to.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-056.
- Sortie : `runtime.py`.
- Acceptation : Une side story sans retour résolvable échoue.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-058 — Rendre récit et paragraphes · [#244](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/244)

Afficher statuts et limites sans marqueurs techniques parasites dans la prose.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-057.
- Sortie : `render.py`.
- Acceptation : Les textes sont échappés et les ancres sont uniques.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-059 — Rendre les onglets piliers · [#246](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/246)

Permettre navigation croisée data IA industrie corporate.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-058.
- Sortie : `render.py`.
- Acceptation : Clavier et liens internes fonctionnent sans CDN.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-060 — Rendre preuves et side stories · [#242](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/242)

Permettre retour au tronc et consultation de provenance.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-059.
- Sortie : `render.py`.
- Acceptation : Aucun encart ne transforme son contenu en preuve.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-061 — Préparer les diagrammes exacts · [#251](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/251)

Émettre un Mermaid source explicite depuis les relations typées.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-060.
- Sortie : `render.py`.
- Acceptation : Pas de faux rendu Mermaid annoncé si moteur absent.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-062 — Éprouver HTML et injection · [#245](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/245)

Contrôler échappement, ancrages, visibilité et navigation.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-061.
- Sortie : `tests/test_render.py`.
- Acceptation : Un payload HTML injecté reste texte, les retours résolvent.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-063 — Valider le sprint narratif · [#247](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/247)

Produire une démonstration HTML et une revue de structure.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-062.
- Sortie : `runs/bootstrap/narrative.json`.
- Acceptation : Prototype candidat distinct d’un rapport éditorial approuvé.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

## E8 — Revoir livrer et préparer GreenYellow

Owner historique : #55. Phase 4.

### DC-064 — Exécuter la non-régression canonique · [#248](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/248)

Vérifier le validateur racine sans modification des contrats.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-054, DC-063.
- Sortie : `runs/bootstrap/qa.json`.
- Acceptation : Commande locale racine passe et manifests inchangés.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-065 — Auditer couverture et clôtures · [#249](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/249)

Vérifier chaque tâche contre artefact et critère.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-064.
- Sortie : `runs/bootstrap/coverage.json`.
- Acceptation : Une tâche sans preuve reste ouverte.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-066 — Intégrer fast-forward sans CI · [#253](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/253)

Committer avec skip CI et avancer dev sans force.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-065.
- Sortie : `runs/bootstrap/DELIVERY.md`.
- Acceptation : Ref distante au SHA attendu ; main inchangé.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-067 — Vérifier état distant et workflows · [#250](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/250)

Lire ref et runs du SHA exact après intégration.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-066.
- Sortie : `runs/bootstrap/DELIVERY.md`.
- Acceptation : Distinguer absence de run et succès de tests locaux.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-068 — Revoir la structure du projet · [#252](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/252)

Présenter points d’entrée, commandes et limites réelles.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-064.
- Sortie : `README.md`.
- Acceptation : Aucun serveur permanent ou compaction technique revendiqué.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-069 — Préparer import privé GreenYellow · [#254](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/254)

Lister matériaux disponibles, manquants et destination privée.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-068.
- Sortie : `docs/INTAKE-POLICY.md`.
- Acceptation : Pas d’import brut dans dépôt public ; conversation inaccessible signalée.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-070 — Proposer piliers et fil narratif · [#255](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/255)

Préparer des choix éditoriaux candidats depuis le corpus disponible.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-069.
- Sortie : `docs/PILLARS.md`.
- Acceptation : Aucun choix candidat n’est déclaré approuvé par François.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-071 — Inventorier les side stories candidates · [#256](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/256)

Lister zooms/contrechamps/vision/ROI avec questions et retours envisagés.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-070.
- Sortie : `docs/NARRATIVE.md`.
- Acceptation : VisioSense reste à vérifier ; aucune recommandation fournisseur implicite.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

### DC-072 — Livrer capsule et décision suivante · [#257](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/257)

Consolider reçus et éléments à valider pour le dry run étendu.

- Entrées ciblées : AGENTS.md, docs/INTERFACES.md et reçus des prérequis.
- Dépendances : DC-067, DC-071.
- Sortie : `runs/bootstrap/RESUME.md`.
- Acceptation : Reprise autonome possible ; validation éditoriale reste explicitement en attente.
- Passage : artefact écrit → contrôle ciblé → reçu → intégration par coordinateur.

