# Loopback du graphe — observation, hypothèse, proposition, test, revue

Le graphe grandit par apports documentaires. Son loopback lit sa structure et prépare des décisions bornées ; il ne réécrit ni les connaissances, ni leurs preuves, ni les piliers. Les associations par mots-clés restent candidates. La revue s'appuie sur les nouveaux matériaux et le mandat de l'étude.

## Bootstrap vérifié

Donneur consulté via le plugin GitHub, sans authentification terminal ni copie de dossier candidat : `achard-arnaud/Candidatures-nice`, commit exact `1a33eeb3d7bee058a914a1d405c420c5d16d57cd`. Cette référence est celle des fichiers effectivement lus, pas une affirmation sur le HEAD futur du dépôt.

| Fichier lu au commit épinglé | Blob observé | Transfert retenu |
|---|---|---|
| `workflow/LOOPBACK.md` | `c65eeb7fa412fa54b2861925f008e5c08b739f83` | Déclenchement sur signal/retour/lot choisi ; observation distincte de cause ; trois actions, un correctif, deux réparations maximum ; no_change valide. |
| `workflow/LOOPBACK-INTERFACE.md` | `c0514aa713725312313995f8dcc295fdf43323b6` | Entrées épinglées, preuves, bornes, reçu ; inconnue et refus explicites ; résolution de guides distincte d'une enquête exécutée. |
| `workflow/skills/run-loopback/SKILL.md` | `61b7e9483bf282ed8a8dc0933fcd1578a40fa5fe` | Trace réelle → qualification → proposition → test → revue ; recouvrement lexical traité comme piste. |
| `workflow/skills/run-loopback/references/operating-contract.md` | `c2736f9135da282218c7a34fd96b5baf1a7a0b66` | Hashes et contexte du cas ; reçu de proposition non appliquée ; validité de forme distincte de vérité sémantique. |
| `workflow/skills/run-loopback/references/signal-catalogue.md` | `5dab8baac1fcd4b0a2420cb64d4918f21e353976` | Une question et une expérience minimales par signal ; aucune case à remplir sans besoin ; coûts natifs inconnus restent inconnus. |
| `scripts/check_workflow_loopback.py` | `91b0feb0acd600b6b1a7aad933b1b5bd6b4ed3d1` | Validation structurelle des bornes et invariants ; aucune écriture ni promotion. |

Le fichier `.agents/skills/run-loopback/SKILL.md` a aussi été lu : il renvoie à la skill canonique ci-dessus. Aucune installation ni modification de skill n'a été réalisée. Les personas, templates de CV, gates A1–A4 et faits candidats ne sont pas importés dans le graphe business. Les règles de maintenance sont adaptées au domaine, pas recopiées comme un second moteur Process.

## Entrées et commande

```python
from loopback import analyze_graph
report = analyze_graph(graph, recent_ids=["ATOM-..."], previous=previous_graph_or_report)
```

```bash
python3 loopback.py /chemin/prive/graph.json --recent-id ATOM-... --output /chemin/prive/loopback.json
python3 loopback.py /chemin/prive/graph.json --previous /chemin/prive/previous-loopback.json
python3 -B -m unittest discover -s tests -p test_loopback.py -v
```

`recent_ids` désigne explicitement les IDs des nœuds ou liens apportés/révisés dans le lot. L'analyseur ne devine pas leur date à partir de la position du fichier. Un lien récent valide étend la revue à ses deux extrémités ; un ID absent reste inconnu. Sans matériau récent résolu, aucune revue de pilier n'est déclenchée par un seuil de densité ou une baisse de fréquence. Un appel manuel sans anomalie peut retourner `no_change`.

Deux formes sont prises en charge :

- Projection de preuves : nœuds `source`, `fragment`, `claim`, `kind` comme type structurel ; liens `source_of`, `evidence_for` et relations typées des claims.
- Projection documentaire KB : nœuds `type=source|atom|pillar|entity`, avec `kind` comme sous-type éventuel (`assertion`, `question`, `candidate_pillar`…) ; liens `derived_from`, `candidate_classification`, `explicit_mention`.

Pour un nœud, `type` prime sur `node_type`, puis `kind` ; les sous-types sont comptés séparément. Pour un lien, `kind` prime sur `type`, puis `edge_type`. Extrémités `from/to` ou `source/target` ; IDs textuels requis. Les mentions d'entités ne sont pas des relations causales. Le sens documentaire d'un lien `derived_from` reste celui de sa projection, sans conversion en preuve de vérité.

## Mesures et signaux

Le rapport conserve l'empreinte SHA-256 de la représentation JSON du graphe, les compteurs de types, les isolés, doublons d'IDs/liens, localisateurs non résolus et incompatibilités de types connues. Les graphes invalides restent observables : les extrémités inexistantes sont signalées et exclues de la densité, sans réparation automatique.

La densité orientée vaut `paires orientées uniques valides non réflexives / n(n−1)`, avec `n` égal au nombre d'IDs de nœuds uniques valides. Elle vaut zéro si `n<2`. Les doublons, boucles et liens parallèles ne l'inflationnent pas ; leur comptage reste séparé. Un graphe clairsemé peut conserver de bonnes notes ouvertes ; un graphe dense peut accumuler des liens sans valeur. **Aucune cible de densité ni score de qualité n'est défini.**

La couverture des piliers compte seulement les rattachements déclarés (`pillar_ids`, `hil_ids`) ou exprimés par un lien d'appartenance reconnu. Les `candidate_classification` sont comptées distinctement comme appartenances candidates, jamais comme approbation humaine. Une projection sans piliers retourne `not_projected`, pas une note de qualité nulle. Une revue déclenchée par l'apport récent examine les piliers concernés, les matériaux non classés et les contre-exemples ; elle peut conserver le découpage courant. Industrie et fonctions corporate, data et IA restent des distinctions à préserver ou discuter explicitement au regard du mandat.

`previous` accepte un graphe ou un rapport antérieur. Les deltas de nœuds, liens et densité sont descriptifs : ils ne prouvent ni amélioration, ni cause, ni économie de tokens.

## Boucle et compaction proposées

Chaque fiche candidate porte : observation traçable dans le rapport, hypothèse encore non vérifiée, proposition, test à exécuter, revue en attente et arrêt. Un test décrit n'est pas un test exécuté. La décision humaine ne passe jamais à true dans cet analyseur.

Ordre de revue : intégrité de structure, doublons/aliases, axes analytiques affectés par le matériau récent, pertinence des types. Le rapport retient toutes les propositions, sans plafond (D32), et indique le nombre différé, qui vaut 0 par construction ; plusieurs correctifs candidats peuvent coexister, chacun non appliqué. Les listes de détails sont bornées à vingt exemples, tout en conservant les comptes. Deux réparations infructueuses sur le même blocage arrêtent l'expérience ; les dépendances concernées restent à revalider.

Un texte identique ou un lien répété peut conduire à proposer un merge, un alias ou un tombstone réversible. Il faut d'abord vérifier sources, portée, dates et contre-exemple d'homonymie. Tout ancien ID, occurrence, localisateur et lien de provenance doit rester résolvable ; la dépréciation documente redirection, version et motif. **L'analyseur ne supprime rien et ne génère aucun merge appliqué.** Les deux occurrences d'une même cause peuvent partager une revue seulement si leur lien est établi ; la seule similarité lexicale ne suffit pas.

L'enrichissement des types suit la même règle : nommer une question utile, montrer les nœuds/liens qui justifient le changement, définir son sens et ses extrémités, tester un cas positif et un cas incompatible, puis soumettre la proposition. Aucun nombre arbitraire d'occurrences ne crée automatiquement un pilier ou un type.

## Limites opérationnelles

Le code est stdlib, local et sans accès réseau. Il écrit uniquement le rapport explicitement demandé à la CLI ; la fonction ne mute pas ses arguments. Aucun writer de graphe, ordonnanceur, apprentissage de modèle, automatisation GitHub ou promotion de connaissance n'est installé. La compilation des fiches en backlog et l'application d'un éventuel correctif restent des actes du coordinateur autorisé. Les rapports portant du corpus privé restent dans sa destination privée ; seules méthode et fixtures synthétiques entrent dans le dépôt public.
