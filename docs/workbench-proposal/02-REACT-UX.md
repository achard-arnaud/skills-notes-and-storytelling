# Business Notes Workbench — UX React v0 (spécification)

**Cible** : un cockpit local-first de création de notes. Ce document n'est **pas** la preuve d'une UI livrée ou d'un backend existant.

## Écran principal (trois zones)

**A. Démarrer / Reprendre** : switch `Entreprise | Produit | Étude de couple` avec identité, URL canonique, aliases, pays/juridiction, question de décision et cutoff. Recherche dans le vault des études précédentes : date, subject, template, source freshness, statut de qualité. Actions `Réutiliser | Actualiser | Nouvelle étude`. Aucun deepsearch avant choix.

**B. Bibliothèque de templates** : cards/liste, recherche full-text, filtres combinables `business/product/technical` (axes multiples mais `primary_analysis_dimension` explicite), tag objectifs et audience, `lifecycle` (validated/candidate/todo), longueur, formats compatibles; ne proposer que les combinaisons effectivement supportées dans manifest. Statut candidat visible, aucun résultat faussement production. Preview du ToC du template choisi et de ses rubriques verrouillées, dependencies et longueur.

**C. Table des matières — Coach** : sections et sous-sections ordonnables par drag & drop **et** contrôles clavier Up/Down; badge obligatoire/conditionnel; étoiles 0–3 (0 normal, 1 soutenir, 2 approfondir, 3 partie critique); champ `why?` / question, budget mots estimé, preuves candidates; confirmation d'un nouvel ordre et retour au template. Les sections `sources, constraints, decision, risks/falsifiers` restent protégées quand l'autorité template les exige. Les dépendances sont appliquées (impossibilité de placer conclusions avant preuves lorsque interdit). Drag n'autorise pas l'écrasement d'ID stable.

## Maquette fonctionnelle

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ BUSINESS NOTES  [Entreprise|Produit|Couple] [Recherche existante...] [Profil]│
├──────────────────────┬─────────────────────────────┬─────────────────────────┤
│ Intention & cible    │ Bibliothèque des templates  │ ToC & Coach              │
│ Entreprise : [      ]│ Recherche [________]        │ 1. Decision   [LOCK] ★★★ │
│ Produit   : [      ] │ Filtres B  P  T            │ 2. Evidence          ★★ │
│ Cutoff    : [      ] │ Architecture note [T/B/P]  │ 3. Market & peers    ★★ │
│ Reuse/refresh/new    │ Two-pager         [B/P]    │ 4. Risks & gates [LOCK]★ │
│ SEARCH | DEEPSEARCH  │ Benchmark         [T/P/B]  │ ↑ ↓  Réinitialiser ordre│
│ Estimation budget    │ ...                         │ Thèse + redteam         │
├──────────────────────┴─────────────────────────────┴─────────────────────────┤
│ Historique étapes: intake / sources / graph / coach / draft / QA / deliver   │
│ [Planifier recherche] [Valider le Coach] [Construire]  [Word] [PDF] [HTML][MD]│
└──────────────────────────────────────────────────────────────────────────────┘
```

## Comportements API (proposés)

- `GET /api/templates?dimension=business&lifecycle=validated&q=...` retourne un snapshot du manifest, chaque template et les sections `toc` + `sha`.
- `GET /api/entities?query=...&kind=company|product` retourne ID, aliases, recent_runs, staleness (nullable) et source refs, jamais raw secret.
- `POST /api/runs/plan` valide l'overlay et retourne plan, coût **estimé**, recherches déjà disponibles, conflit et constraints; aucun appel LLM profond dans ce POST.
- `POST /api/runs` crée une session, un ID idempotent, branch facultative après vérification consentement; aucun Git push implicite.
- `POST /api/runs/:id/search` `{mode:search|deepsearch, approved_budget}` démarre une étape autorisée, avec gate.
- `POST /api/runs/:id/coach` stocke révisions des contraintes de section, preuves choisies et HITL.
- `GET /api/runs/:id/events` retour d'état en polling/SSE lecture seule; le frontend ne maîtrise pas la progression du WF.
- `POST /api/runs/:id/exports` `{formats:[docx,pdf,html,md], expected_frozen_sha}` crée un job, jamais un document magique. Buttons désactivés tant que gate bloque.
- `GET /api/runs/:id/artifacts` fournit manifest, QA par format, liens téléchargeables seulement si outputs réellement présents.

### Erreurs produit explicites

1. Aucun travail antérieur : `new`, pas `reuse`.
2. Recherche périmée ou contradictoire : plan refresh borné avec sources impactées et raison.
3. Template `candidate` : usage preview avec avertissement; pas mark `validated`.
4. Reorder viole une dépendance / section mandatory : refuser avec message et possibilité reset.
5. Stars 3 sur section sans preuves : demander recherches/unknowns, ne pas inventer du contenu.
6. PC/Obsidian bridge offline : mode lecture/démo uniquement; file d'attente non autorisée par défaut.
7. GitHub token non disponible : poursuivre local si autorisé, `remote_sync=pending` et pas de branche prétendue.
8. Export QA KO : laisser preview/diagnostic, désactiver livraison de format KO.

## Accessibilité, qualité et livrables

React/TypeScript, formulaires accessibles, contrôles clavier et aria, responsive trois colonnes→onglets, section reordering testable par clavier; zero business secrets in client state, DTO non sensibles.
V0 à exécuter sur localhost seulement : catalogue mocké depuis manifest, fixture synthétique, ToC + stars + overlay JSON téléchargeable, sans moteurs externes. V1 ajoute API, vault, run store. V2 GitHub/runs/export multi-format; ne pas commencer par l'intégration webhook cloud.
