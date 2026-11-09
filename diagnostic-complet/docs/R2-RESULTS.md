# R2-12 — Résultats sur le corpus réel

Document public : **comptes agrégés seulement**. Aucun contenu du corpus. Ces mesures décrivent le découpage et la structure, jamais la véracité des assertions.

## Collecte corporate (R2-11)

| Mesure | Valeur |
|---|---|
| Hôte | `www.greenyellow.com` (un seul) ; `robots.txt` : tout autorisé |
| URLs visitées | 737 |
| Pages extraites | 683 (654 contenus distincts après redirections) |
| Découvertes par sitemap / par liens seuls | 649 / 88 |
| Erreurs | 54 : 52 liens morts (HTTP 404, dont 4 listés dans le sitemap lui-même), 2 redirections vers un autre domaine |
| Fichiers non HTML listés | 2 PDF de rapports RSE : le serveur répond HTTP 500, **non récupérés** |
| Mots extraits | 443 697 |
| File restante | 0 |

Limite : couverture des pages HTML du même hôte atteignables par sitemap et liens. Ce n'est pas l'empreinte publique complète de l'entreprise.

## KB atomique (R2-10)

| Mesure | Valeur |
|---|---|
| Sources | 655 (654 pages distinctes + 1 analyse fournie) |
| Atomes dédupliqués | 22 001 |
| Occurrences | 34 210 (12 209 répétées, soit 35,7 %) |
| Nœuds / arêtes du graphe documentaire | 22 670 / 50 038 |
| Caractères non expliqués | 0 |
| Erreurs d'ingestion | 0 |

Types d'atomes : 17 931 assertions, 3 873 titres, 170 questions, 18 directives, 8 tableaux, 1 bloc de code.

Répétition : 1 852 atomes apparaissent dans au moins 2 occurrences, 142 dans au moins 10, le maximum est 1 336. Ce sont en grande partie des éléments de gabarit du site (appels à l'action, pieds de page). Ils sont **conservés** : chaque occurrence porte sa provenance.

## Rattachement lexical aux piliers candidats

Liens `candidate_classification` par pilier du lexique : industrie 5 510, économie 827, IA 459, entreprise (fonctions corporate) 423, stratégie 421, données 287, gouvernance 264, adoption 94. 7 047 atomes portent au moins un pilier candidat.

**Réserve forte** : ce sont des correspondances de mots-clés, pas des classifications validées. Le poids de l'industrie reflète le vocabulaire d'un site d'énergie, pas une conclusion éditoriale. Le choix des piliers reste HITL-258.

## Ontologie sur le corpus réel (v0.4.0)

| Mesure | Valeur |
|---|---|
| Violations | 14 sur 50 038 arêtes |
| — atomes `directive` classés dans un pilier ou une entité | 9 |
| — bloc de code classé par mots-clés | 5 |
| Non classés | 0 |
| Hors ontologie | 0 |
| Candidats d'alias | 3 |
| Part de titres parmi les atomes | 17,6 % |
| Densité dirigée historique | 9,4 × 10⁻⁵ |
| Densité sémantique | 0 (aucune arête entre nœuds sémantiques : les liens sont documentaires) |

Constats corrigés en cours de route grâce à ces données : titres (v0.3.0, D20) puis tableaux (v0.4.0, D21) reconnus comme ancrages thématiques. Constats conservés : les 9 directives sont des **faux positifs de l'heuristique** de `kb.py` (phrases descriptives commençant par un infinitif ou « il faut »). À relire, non corrigés en silence.

## Ce que ces résultats ne disent pas

- Aucune assertion n'est vérifiée ; tout est `SOURCE`, rien n'est `HUMAN_ADJUDICATED`.
- La densité sémantique nulle signifie qu'**aucune relation probatoire n'existe encore** entre atomes : le graphe est documentaire. Les relations (`supports`, `causes`, …) restent à qualifier par revue humaine.
- Le transcript de l'entretien R1, la conversation de travail et l'annonce originale ne sont pas importés (voir `docs/R2-INTAKE.md`).
