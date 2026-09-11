# Retrieval et reranking — claims (scaffold logique) vs fragments (remplissage business)

## Deux couches distinctes

| | Claims | Fragments |
|---|---|---|
| Rôle | Scaffold logique — l'architecture de la décision | Remplissage business — la matière probante |
| Contrat | `contracts/claim.schema.json`, `contracts/claims-graph-light.schema.json` | `contracts/fragment.schema.json` |
| Granularité | Une affirmation typée, reliée à d'autres claims par des arêtes typées | Une unité atomique de preuve/donnée, adressable par source |
| Ce qu'on reranke | La priorité éditoriale (quel claim mérite une section, un titre d'action) | La sélection des preuves qui remplissent un claim déjà retenu |
| Mutation | Change rarement en cours de run (le scaffold doit se stabiliser avant le fill — cf. `ghost_deck`) | Peut être remplacé/enrichi jusqu'à la fin du fill |

Ne jamais fusionner ces deux registres dans un seul objet : un claim sans fragment attaché reste `unknown`/`hypothesis` ; un fragment sans claim n'entre jamais en rédaction (règle héritée du repo historique : pas de prose sans lignée fragment → claim).

## Retrieval

1. **Requêtes ciblées, pas thématiques.** Une requête de recherche complémentaire doit viser un claim précis à confirmer/infirmer, jamais un thème large (`"marché de l'IA agentique"` est interdit ; `"taux de churn constaté chez les clients Series B de <vendeur>"` est correct). Voir aussi la règle de priorisation dans [runtime-modes.md](runtime-modes.md).
2. **Input utilisateur prioritaire.** Toute source fournie par l'utilisateur (document, lien, donnée orale) est retrievée et fragmentée avant toute recherche complémentaire. La recherche web ne comble que les trous explicitement identifiés après épuisement de l'input fourni.
3. **Fenêtre de retrieval bornée.** Pour un run itératif ciblé (`zoom`, voir modes.md §5), le retrieval se limite aux fragments/claims dont l'ID est dans le périmètre déclaré, plus leurs voisins directs dans le claims graph (profondeur 1).

## Reranking

### Claims (priorité éditoriale)
Utiliser la grille de `workflow.md` (pertinence décisionnelle 30%, force de preuve 25%, pouvoir explicatif 20%, nouveauté 15%, adéquation lecteur 10%), avec gates durs (contradiction non résolue, preuve insuffisante, inconnu critique) en amont du score pondéré.

### Fragments (remplissage)
Une fois un claim retenu, reranker ses fragments candidats sur :
- **spécificité** (donnée précise > généralité) — poids 35%;
- **fraîcheur** (date/version de la source) — poids 25%;
- **indépendance de la source** (éviter deux fragments issus du même émetteur biaisé pour un même claim) — poids 25%;
- **coût de vérification** (facilement vérifiable > affirmation non sourcable) — poids 15%.

Top-k par défaut : garder au plus **3 fragments** par claim en section principale (au-delà, densité illisible) ; les fragments surnuméraires mais valides vont en side story `method` ou en annexe, jamais supprimés silencieusement (traçabilité).

## Déduplication

- Fragments : dédupliquer par similarité sémantique **et** identité de source ; un même fait rapporté par deux documents distincts reste deux fragments liés (renforce la force de preuve) mais n'est cité qu'une fois en rédaction.
- Claims : deux claims quasi identiques formulés différemment doivent être fusionnés avant le scaffold — jamais après (la fusion après scaffold casse la lignée des sections déjà écrites).

## Storytelling / narrative structure vs side-stories

- La **structure narrative** (voir narrative-frameworks.md) porte l'architecture argumentative principale : elle est MECE, Action-Titled, ouverte en pyramide.
- Une **side-story** est un contenu périphérique non structurant (voir side-stories-retro.md) : elle enrichit sans devenir un point de passage obligé de la décision.

### Règle d'exclusion / relégation en annexe

Une side-story candidate est **exclue** si :
- elle ne peut pas être rattachée à un claim ou fragment existant (viole l'invariant "jamais de nouvelle preuve");
- elle allonge la note au-delà du budget de pages du template sans gain décisionnel mesurable;
- elle duplique un point déjà couvert par la structure narrative principale.

Elle est **reléguée en annexe** (plutôt qu'insérée dans le corps) si :
- elle est utile à un sous-ensemble du lectorat seulement (ex. détail méthodologique pour un lecteur technique dans une note business);
- son insertion romprait la cadence Pyramid/Action-Titles de la section courante;
- elle dépasse la densité maximale définie par le scaffold pour la section concernée.

Elle reste **dans le corps** seulement si elle change la compréhension du claim central sans pouvoir être un fragment de plus dans le corps principal (cas `analytical_focus` ou `false_lead` typiquement).
