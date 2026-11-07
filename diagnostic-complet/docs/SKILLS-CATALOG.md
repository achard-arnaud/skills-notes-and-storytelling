# Catalogue des douze opérations atomiques

Généré par `skills_catalog.py catalog`. Les SKILL.md ne sont pas versionnés ici (mandat R2) : `drafts` les produit hors dépôt, `lint` les contrôle.

| # | Opération | Module | Déclencheur (exemples) | Exclut |
|---|---|---|---|---|
| 1 | `source-convert` | `convert.py` | importe ces fichiers ; convertis ce PDF, DOCX, HTML ou ZIP en texte | la collecte web (corporate-crawl), l'atomisation (kb-ingest), toute édition du contenu |
| 2 | `corporate-crawl` | `crawl.py` | scrape le site corporate ; complète la KB avec le site de l'entreprise | la conversion de fichiers, toute collecte hors de l'hôte déclaré, les sites authentifiés |
| 3 | `kb-ingest` | `kb.py` | atomise ces sources ; nourris la KB ; génère les nœuds | la conversion de formats (source-convert), la promotion de faits, la rédaction |
| 4 | `ontology-check` | `ontology.py` | valide l'ontologie ; compare deux versions du référentiel ; classe ce graphe | tout changement de graphe, toute décision de seuil |
| 5 | `reinforce-kb-loopback` | `reinforce.py` | revois la KB après cet apport ; reçu de renforcement du graphe | le diagnostic d'un run CV (run-loopback), la revue d'un A1 sans incident (challenge-a1-template) |
| 6 | `evidence-import` | `runtime.py` | importe ces matériaux avec localisateurs ; valide références et statuts | l'atomisation en KB documentaire (kb-ingest), toute promotion épistémique |
| 7 | `pillar-qualify` | `loopback.py` | qualifie ces nouveaux matériaux par pilier ; quels piliers sont touchés | la création d'un pilier par seuil, la décision éditoriale (HITL) |
| 8 | `writing-fresh` | `writing.py` | prépare un plan de rédaction depuis les preuves ; from-scratch | la révision d'un texte existant (writing-iterative), la génération de faits |
| 9 | `writing-iterative` | `writing.py` | révise ce texte à partir d'un delta ; mets à jour sans réécrire le reste | une nouvelle rédaction (writing-fresh) |
| 10 | `context-packet` | `context.py` | reprends le run ; paquet de contexte de cette tâche ; vérifie la fraîcheur | tout contrôle de la fenêtre du modèle (non prétendu) |
| 11 | `reader-render` | `render.py` | rends cette étude en HTML lecteur | la rédaction automatique, la promotion de preuves |
| 12 | `graph1-project` | `project.py` | publie la KB dans le namespace business de Graph1 | toute modification du graphe de formation gelé |

## Contrat de chaque opération

### `source-convert`

- Commande : `python3 diagnostic-complet/convert.py FICHIERS --out DOSSIER_PRIVÉ`
- Entrées : fichiers .md .txt .html .docx .pdf .zip
- Sorties : Markdown dans un dossier privé + rapport par statut avec empreintes
- Interdits : inventer du texte pour un PDF sans couche texte ; extraire un ZIP sans garde de chemin ni de taille ; écrire hors du dossier privé
- Contre-exemple testé : ZIP contenant ../escape.md : membre refusé, rien écrit hors du dossier.

### `corporate-crawl`

- Commande : `python3 diagnostic-complet/crawl.py --host HÔTE --out DOSSIER_PRIVÉ --sitemap URL_SITEMAP`
- Entrées : un hôte, un sitemap, un dossier privé
- Sorties : pages Markdown, HTML brut, state.json (frontière, erreurs), coverage.json
- Interdits : ignorer robots.txt ; sortir de l'hôte ; écrire dans le dépôt public ; présenter la couverture comme exhaustive
- Contre-exemple testé : Chemin interdit par robots.txt : non collecté et compté dans robots_disallowed.

### `kb-ingest`

- Commande : `python3 diagnostic-complet/kb.py FICHIERS_MD --out KB_PRIVÉE --source-kind TYPE`
- Entrées : Markdown ou texte extrait
- Sorties : sources, atomes dédupliqués avec occurrences et localisateurs, graphe documentaire
- Interdits : promouvoir un atome en fait ; fusionner des occurrences distinctes ; écrire sous un Git public sans déclaration explicite
- Contre-exemple testé : Même texte dans deux sources : un atome, deux occurrences, aucune fusion de sources.

### `ontology-check`

- Commande : `python3 diagnostic-complet/ontology.py check | diff ancien nouveau | analyze graph.json`
- Entrées : référentiel JSON ou graph.json
- Sorties : validité, diff (breaking, revue humaine requise), classes, violations
- Interdits : fixer un seuil ; corriger un graphe ; accepter une relation probatoire sans règle
- Contre-exemple testé : Seuil sans decision_ref : référentiel refusé.

### `reinforce-kb-loopback`

- Commande : `python3 diagnostic-complet/reinforce.py graph.json --recent-id ID --output reçu.json`
- Entrées : graph.json, IDs récents explicites
- Sorties : un reçu : décision, au plus trois actions, déclencheurs, mesures
- Interdits : fusionner, supprimer ou réaffecter un identifiant ; approuver un candidat ; traiter la densité comme un score
- Contre-exemple testé : Aucun ID récent et graphe propre : no_change.

### `evidence-import`

- Commande : `python3 diagnostic-complet/runtime.py import|validate|graph`
- Entrées : Markdown source
- Sorties : fragments localisés, claims importés comme supplied_claim, graphe probatoire
- Interdits : marquer un fait vérifié sans qualification déclarée ; déduire une cause
- Contre-exemple testé : Fait vérifié sans revue déclarée : refusé.

### `pillar-qualify`

- Commande : `python3 diagnostic-complet/loopback.py graph.json --recent-id ID`
- Entrées : graph.json, IDs récents
- Sorties : couverture par pilier, matériaux non classés, revue proposée
- Interdits : créer un pilier parce qu'un seuil est franchi ; promouvoir une classification lexicale
- Contre-exemple testé : Association par mots-clés : reste candidate.

### `writing-fresh`

- Commande : `python3 diagnostic-complet/writing.py from-scratch`
- Entrées : scaffold et claims du graphe
- Sorties : topologie et plan sans prose
- Interdits : rédiger des faits ; accepter une unité sans claim connu
- Contre-exemple testé : Conteneur de prose antérieure fourni : refusé.

### `writing-iterative`

- Commande : `python3 diagnostic-complet/writing.py iterative`
- Entrées : baseline identifiée par empreinte, delta de sources
- Sorties : plan de révision, revues invalidées ciblées, journal append-only
- Interdits : remplacer hors delta ; ignorer une dépendance non résolue
- Contre-exemple testé : Remplacement hors delta : rejeté.

### `context-packet`

- Commande : `python3 diagnostic-complet/context.py board|packet|checkpoint|resume-check`
- Entrées : board, tâche, entrées déclarées
- Sorties : paquet borné, checkpoint avec empreintes, refus si périmé
- Interdits : relire tout le dépôt par défaut ; prétendre purger la fenêtre
- Contre-exemple testé : Entrée modifiée depuis le checkpoint : reprise refusée.

### `reader-render`

- Commande : `python3 diagnostic-complet/render.py ETUDE.json SORTIE.html`
- Entrées : étude JSON (récit, piliers, preuves, side stories)
- Sorties : HTML autonome sans ressource externe
- Interdits : afficher un état humain non validé comme validé ; charger une ressource externe
- Contre-exemple testé : Contenu injecté : échappé.

### `graph1-project`

- Commande : `python3 diagnostic-complet/project.py --graph1 CLONE --frozen-sha SHA --source kb=KB`
- Entrées : KB privée, clone Graph1, empreinte du graphe gelé
- Sorties : fichiers sous knowledge/business/, MANIFEST avec empreintes
- Interdits : écrire sous canonical/, build/, tests/, scripts/, docs/ ; publier sans [skip ci] ni fast-forward ; forcer un push
- Contre-exemple testé : Namespace hors knowledge/business/ : refusé.
