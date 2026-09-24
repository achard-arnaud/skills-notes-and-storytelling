# Template — Note stratégique de transformation d'un fonds (candidate v0.2)

## Décision et périmètre

Document de 5 à 7 pages pour les associés d'un fonds actif. Dimension primaire : business.
Il confronte les moteurs externes et le métier réel du fonds, puis propose une trajectoire
à trois à cinq ans. Ce n'est ni un diagnostic de maturité d'une participation, ni une
présentation de fournisseurs. `from-scratch` ou `iterative` selon la baseline disponible.

## Contrat des pages

1. **Thèse et arbitrage** : réponse d'emblée, lien exact avec la vocation et le périmètre
   du fonds, bénéfices différenciés pour GP, LP et participations, décision proposée.
2. **Pourquoi maintenant** : deux ou trois moteurs de marché sourcés, deux facteurs
   internes attestés, horizon 3–5 ans ; signaler toute exposition inférée.
3. **Forward deployment** : valeur de l'accompagnement avant/après acquisition, séquence
   digital → data → analytique/ML → IA → automatisation/robotique selon l'actif ;
   ownership CEO/COO/DSI, portefeuille de preuves, alternatives sans IA.
4. **Investment process** : origination, qualification, NDA/dataroom, diligence,
   comité, closing, suivi, exit ; friction, artefact, contrôle humain et métrique
   pour chaque maillon prioritaire. Distinguer GP, LP, fonds de fonds et banques.
5. **Économie et gouvernance** : EBITDA, croissance, cash, risque et capital investi
   sans doubles comptes ; services facturés et accords LP/GP/frais/offsets séparés ;
   confidentialité, permissions, origine des preuves et conformité.
6. **Trajectoire et rôle** : 0–90 jours, 12 mois, 3–5 ans ; propriétaires, gates,
   stop conditions, ressources et mandat durable, sans revendiquer une fonction déjà créée.
7. **Sources et limites** : références claim→source, date et périmètre ; contre-preuve,
   dépendances non vérifiées et questions de comité. Peut partager la page 6 si lisible.

## Gates

- Un cas marketing d'un cabinet ou fournisseur est attribué et ne devient jamais le ROI du fonds.
- Une étude sur la transmission n'est pas une prévision de dealflow éligible.
- Une opportunité de revenu du GP est distincte de la valeur économique du fonds et
  appelle revue des accords LP, de la tarification et des conflits d'intérêts.
- Le schéma d'organisation d'un pair ne prouve pas celui du fonds cible.
- Le rôle proposé explicite décision, responsabilité et relais des managers ; un agent
  ne devient jamais propriétaire d'un investissement ou d'une relation dirigeant.
- Toute revendication de compétence personnelle est appuyée par une expérience
  autorisée par le candidat ou reste formulation de positionnement à vérifier.

## Composition

Méthode primaire : pyramide (thèse → deux chaînes de valeur → économie → décision).
Insérer au plus deux side stories comparatives avec mécanisme et limite de transfert.
Garder les registres de fragments, claims et sources séparés de la maquette finale.
Une note candidate doit posséder une fixture qui teste ses sections et un contre-cas
sur le revenu de services avant promotion au statut validated.

## Kit d'output — adaptation de la grammaire Hivest

Les fichiers `strategic-fund-transformation/style.css`, `skeleton.html`,
`payload.schema.json` et `payload.example.json` constituent la nouvelle couche
présentation. Source d'inspiration : `Hivest-ptf-analysis`,
`renderers/three_pager_exec/exec_theme.css`,
`contracts/three-pager-exec.schema.json` et
`templates/THREE_PAGER_EXEC_v0.3.md`, consultés le 24/09/2026.
Leurs couleurs et rôles (navy = thèse, teal = conclusion, gold = point d'attention),
leur ligne de sources, leur pied « À retenir », la valeur canonique dans `figures`
et la traçabilité `lineage` sont réutilisés. Le format est ici A4 portrait,
5–7 pages ; les champs et le contenu trois pages / entreprise ont été remplacés
par sept slots de décision pour un fonds. Il ne s'agit pas d'une reproduction
pixel à pixel du rendu portefeuille.

Ordre des pages : `thesis`, `drivers`, `deployment`, `investment`, `economics`,
`roadmap`, `sources_limits` (la dernière peut être jointe à la sixième en restant
lisible). Ordre des preuves : sources → claims → figures canoniques → blocs →
payload → HTML/CSS → PDF/PNG → contrôle. Les renvois `{figure_key}` dans les textes
pointent exclusivement vers `figures` ; `src` y pointe vers une entrée `sources` ;
les `source_ids` de chaque bloc et page existent dans le même registre. Un calcul
requiert `calc`. Vérifier ces renvois au rendu, ainsi que l'unicité des pages,
les débordements, la lisibilité (plancher 9 pt), la cohérence des nombres et le
statut de preuve avant diffusion. Les figures vides de la fixture sont
intentionnelles. Le squelette est un contrat de slots, pas un moteur de rendu.

L'exemple complet de narration Hivest avec sommaire et trois processus se trouve
sous `examples/hivest-strategic-fund-transformation-2026-09-24.md` ; il est une
proposition sourcée, pas un diagnostic validé d'une participation. Le document
Greenfield cité comme [G1] correspond au fichier fourni `Best of Greenfield - S1
2026.pdf` : c'est **une seule source**, non deux documents indépendants. Ne pas
ajouter son PDF au dépôt.
