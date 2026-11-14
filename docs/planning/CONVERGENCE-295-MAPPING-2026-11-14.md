# #295.M1 — Cartographie des contrats et fixture de compatibilité

14 novembre 2026. Base cible : `d904d8b4375f6112bc570dbbe128c6aa512f2561`.
Résultat : mapping documentaire contrôlé et fixture synthétique ; aucune migration
de runtime, de schéma canonique, d'enum ou de skill. #295 reste ouvert.

## Mandat et statut

Le [plan de convergence](CONVERGENCE-PLAN-2026-11-14.md) autorise comme repli S1
une « fixture de mapping et lacunes sans changement canonique ». Le
[handoff](HANDOFF-CONVERGENCE-2026-11-14.md) prévoit également le mapping
documentaire indépendant. Ce lot réalise ce repli, sans démarrer S2/S3 ni
réimplémenter diagnostic-complet. La restauration de dev et la préparation #298
sont déjà intégrées ; ne pas les refaire.

L'ADR-1007 reste **proposé**. Ce mapping n'enregistre pas son acceptation et ne
transforme pas les anciens SPEC_ONLY en autorisation d'implémentation. La
délégation permanente couvre ce travail documentaire : aucune approbation de
notification ni nouveau GO routinier n'est demandé.

## Versions réellement inspectées

Cible : le SHA de base ci-dessus. Donneur en lecture seule :
`75c8293de6984c6fac80e016528bdfa4ec019226`, sans merge de la branche d'essai.
Les huit blobs de source et leurs empreintes figurent dans le
[reçu](CONVERGENCE-295-MAPPING-RECEIPT-2026-11-14.json).

| Source cible | Autorité observée |
| --- | --- |
| `diagnostic-complet/docs/INTERFACES.md` | Étude v0, claims, relations, sections et frontières des modules |
| `diagnostic-complet/runtime.py` | Import, validation structurelle et projection du graphe de preuves |
| `diagnostic-complet/ontology/terminology.json` | Statuts des claims et politique des sources |
| `diagnostic-complet/context.py` | Board, sélection ready, paquets, checkpoints et invalidation des tâches descendantes |
| `diagnostic-complet/writing.py` | Préparation from-scratch et plan/application des révisions itératives |
| `docs/architecture/ADR-1007-study-workflow.md` | Proposition de frontière analyse avant récit ; statut inchangé |
| `docs/planning/CONVERGENCE-PLAN-2026-11-14.md` | S1/S2/S3 conditionnels et repli documentaire |

Source donneuse :
[`analysis-result.schema.json`](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/75c8293de6984c6fac80e016528bdfa4ec019226/experiments/narrative-procedure-v1/contracts/analysis-result.schema.json),
blob `b2303d0bd50e23a7c7a2ad7eb71b896fcacdc446`.
Ce schéma expérimental n'est pas le schéma canonique d'une étude v0.

## Mapping et écarts qui changent le prochain BUILD

| Élément | Existant et écart précis | Contrôle à prévoir dans S1 |
| --- | --- | --- |
| Intention produit | L'étude v0 porte `mandate.question`, `scope`, `audience`. Pas de contrat typé IntentBrief/AnalysisPlan constaté dans les interfaces inspectées. | Définir les champs et leur version sans fabriquer un mandat décisionnel ; préserver une étude legacy. |
| Question analytique | Le donneur possède déjà `question` en texte. `question_id` n'est pas accepté : `additionalProperties=false`. | Distinguer la question existante d'une identité analytique future ; ne pas annoncer une absence complète de question. |
| Moment du binding | `affects_blocks` est obligatoire et doit contenir au moins un élément. Même une liste vide est rejetée. | Prouver la compatibilité d'une analyse avant scaffold et la lecture de l'ancien binding ; pas de faux ID de bloc pour satisfaire le validateur. |
| Identités de preuves | `input_claim_refs` et `findings[].claim_refs` exigent des chaînes, pas la résolution dans l'étude. Les interfaces v0 utilisent `claims[].id`. | Résoudre les IDs dans la bonne étude et tester une référence absente/étrangère. Une validation JSON Schema seule ne le prouve pas. |
| Statuts | Le donneur admet `recommendation` dans un finding ; la terminologie des claims v0 ne l'admet pas. `verified_fact` existe côté étude, avec ses conditions probatoires, mais n'est pas un statut de finding donneur. | Garder analyse/recommandation distinctes des faits ; aucune conversion automatique en claim vérifié et aucun élargissement silencieux de l'enum. |
| Méthode et limites | `method`, `method_version`, `scope`, `as_of`, `counterevidence`, `unknowns` existent dans le donneur. Les deux derniers sont des listes de chaînes. | Conserver leurs valeurs et leur provenance ; ne pas transformer une contre-preuve textuelle en relation causale établie. |
| Scaffold et rédaction | `writing.prepare_from_scratch(evidence, reader_scaffold=None)` et les fonctions itératives existent déjà. `affects_blocks` ne définit pas à lui seul un mapping vers `sections[].id`. | Raccorder au consommateur existant dans S2, avec une table d'identités explicite ; aucun second moteur de rédaction. |
| Reprise et invalidation | `context.invalidate_descendants(board, changed_ids)` existe pour le DAG des tâches. `writing.plan_iterative` / `apply_iterative` gèrent les révisions. | Déclarer les liens des nouvelles analyses et prouver leur invalidation ciblée ; ne pas prétendre que ces nouveaux objets sont déjà couverts, ni réécrire les mécanismes existants. |

Le point bloquant démontré est le **binding trop précoce**, pas l'existence d'un
graphe d'analyse ou d'une question. L'extension compatible reste à définir et à
tester dans S1. Ce constat n'impose aucune nouvelle décision produit : traiter
les choix techniques réversibles selon les contrats, isoler seulement un vrai
arbitrage si les sources se contredisent.

## Fixture et vérifications effectuées

La [fixture](fixtures/convergence-295-mapping.json) contient uniquement des IDs,
une question et un constat synthétiques. Elle applique chaque mutation à un
payload de base, sans importer de corpus utilisateur.

| Cas | Résultat réellement observé contre le donneur épinglé |
| --- | --- |
| Binding legacy présent | Valide |
| Analyse sans `affects_blocks` | Rejet attendu : `required` |
| `affects_blocks=[]` | Rejet attendu : `minItems` |
| Ajout de `question_id` non déclaré | Rejet attendu : `additionalProperties` |
| Aucune référence de claim en entrée | Rejet attendu : `minItems` |
| Finding avec statut `verified_fact` | Rejet attendu : `enum` |
| Finding avec statut `recommendation` | Valide pour le donneur seulement |

Sept attentes de fixture passent ; la vérification distincte de la frontière des
statuts passe aussi. Les cinq rejets attendus démontrent les contraintes actuelles,
pas un correctif déjà implémenté. Contrôle effectué avec Python 3.12.14 et
`jsonschema.Draft202012Validator` avec vérification du format de date.

Reproduction après récupération du schéma donneur exact dans
`/tmp/analysis-result.schema.json` (vérifier son blob ci-dessus) :

```bash
python3 - /tmp/analysis-result.schema.json docs/planning/fixtures/convergence-295-mapping.json <<'PY'
import copy, json, sys
from jsonschema import Draft202012Validator, FormatChecker
schema, fixture = [json.load(open(p, encoding='utf-8')) for p in sys.argv[1:]]
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema, format_checker=FormatChecker())
for case in fixture['cases']:
    payload = copy.deepcopy(fixture['base_payload'])
    for field in case.get('remove_fields', []):
        payload.pop(field, None)
    payload.update(case.get('set_fields', {}))
    errors = list(validator.iter_errors(payload))
    assert (not errors) == case['expected_valid'], case['id']
    if 'expected_error' in case:
        expected = case['expected_error']
        assert any(e.validator == expected['validator'] and
                   (expected['field'] in e.message or expected['field'] in list(e.path))
                   for e in errors), case['id']
    print(case['id'], 'PASS')
PY
```

## Reprise bornée

1. Relire dev, les owners et ce mapping avant `feat/294-analysis-contracts`.
2. Définir un paquet S1 versionné : emplacement du contrat d'analyse, mapping des
   identités et statuts, migration legacy et comportement avant scaffold.
3. Ajouter les contre-tests sur références absentes, unknown/partial, absence de
   bloc et descendants touchés ; observer RED puis GREEN sur le runtime modifié.
4. Vérifier une analyse réellement consommée avant de déclarer S1 livré. La
   satisfaction du lecteur, la narration et le rendu restent des preuves séparées.

État de ce lot : **MAPPING_CHECKED**, prêt à relire en PR documentaire. État du
S1 runtime : **PLANNED_CONDITIONAL**, pas livré par cette fixture. Pas de tests
du runtime complet exécutés dans M1 ; pas de score de qualité métier, recherche
réelle, nouveau template, nouvelle skill, nouveau trigger ou changement d'ADR.
