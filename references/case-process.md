# Cas isolés et appels contrôlés

Pour une nouvelle instance S3, fixer d’abord le [plan de routage](s3-operations.md#point-de-routage-obligatoire) et le conserver dans le dossier privé du cas. À ce stade, le moteur valide le contrat d’intake existant et les étapes. La validation mécanique du plan de domaine est suivie dans [#378](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/378).

Démarrer le moteur du projet :

```bash
python scripts/case_runtime.py check
python scripts/case_runtime.py init --case <case-id> --input intake.json
python scripts/case_runtime.py begin --case <case-id> --stage A0 --actor manual_agent
```

Le contrat d'intake est `contracts/case-artifacts.schema.json#/$defs/intake` : entity_id,
objective, constraints, cutoff, template_id, render_requested. Un template absent bloque.
Les cas RUN vont dans `data/cases/<case-id>/`, ignoré par Git ; les fixtures synthétiques
curatées vont dans `tests/`. Ne pas migrer les anciens dossiers par simple renommage.
La création exclusive refuse un identifiant existant et crée le graphe avant toute collecte.

`begin` émet un paquet de références avec les empreintes BUILD et celles des dépendances,
le contrat de sortie, le profil du template et le chemin exact du `result.json` attendu.
L'agent lit les sources et écrit cet artefact dans le dossier de la tentative ; le moteur
ne recherche pas le Web, ne sollicite aucun LLM et ne prétend pas observer les lectures
internes de l'hôte. `complete` contrôle les octets soumis, les schémas et les références.

| Étape | Entrée disponible | Artefact et contrôle |
| --- | --- | --- |
| A0 preuves | Intake | Captures locales, URL, date, locator, couverture de lecture |
| A1 modèle | A0 | Sources/fragments/claims en nodes ; edges typés et provenance |
| A2 structure | A0/A1 | Décision, objection, falsifier, sections et claim IDs |
| A3 rédaction | A1/A2 | Prose par section ; même mapping de claims que le scaffold |
| A4 revue | A0–A3 | Trois revues distinctes, et reçu PDF/QA si demandé |

```bash
python scripts/case_runtime.py complete --case <case-id> --stage A0
python scripts/case_runtime.py status --case <case-id>
python scripts/case_runtime.py invalidate --case <case-id> --stage A1 --reason "source corrigée"
```

Les anciennes tentatives restent présentes. L'invalidation suit le DAG du manifeste,
conserve les étapes amont et ne réépingle jamais silencieusement une nouvelle méthode.
Un changement de BUILD impose une nouvelle instance ou une migration explicitement
développée ; cette version n'offre pas de migration automatique de pins.

`state.json` est l'autorité de l'état et du journal `events` : séquence, date, étape,
tentative, acteur déclaré, résultat et empreintes. Écriture atomique et verrou local
évitent les mises à jour concurrentes perdues. Usage fournisseur et temps de lecture
restent inconnus si l'hôte ne les expose pas. Ce journal n'est pas une signature.

Le reçu A4 contrôle la présence et l'empreinte du PDF, ses pages physiques, `qa.json`
et les comptes QA. Il ne constitue ni une preuve de vérité des claims ni une
approbation métier. Les revues déclarées restent attribuées à leur auteur.

## Renforcement après incident

Utiliser `loopback --case <id> --proposal loopback/proposal.json` avec le contrat
`#/$defs/loopback`. Axes : architecture, bugfix, ci, runtime, skill. Le dispatch du
manifeste renvoie les questions et contrôles de l'axe. Relier l'observation à une preuve
locale hachée, à l'état exact, aux ADR concernés, à l'objectif/contraintes et à l'issue.
Choisir `no_change` ou une expérience avec hypothèse, falsifier, protocole, régression,
arrêt et rollback. Mesures : unité explicite, avant/après sourcés ou valeurs nulles.
Une estimation n'est pas une mesure observée.

Le validateur n'applique aucun correctif. Le BUILD autorisé corrige la première couche
fautive, exécute la régression et consigne les résultats dans l'issue et le reçu.
Revoir l'ADR si son hypothèse est invalidée ; renforcer l'implémentation si l'ADR reste
valide. La qualité d'une analyse n'est pas déduite d'une CI verte.

## Projection narrative S3

La note directe peut passer par [le sélecteur](../skills/selecting-narrative-schema/SKILL.md) sans créer de cas. Pour une étude complète, ajouter `"narrative_profile": "s3-narrative-v1"` à l’intake. Le moteur épingle le code, le profil et le guide. A2 réutilise les preuves A0/A1 à partir d’un fichier `request` local à sa tentative. Voir l'[exemple](../examples/narrative-selector-business.json) pour la forme de `request` ; le ledger de preuve vient du cas.

```bash
python scripts/case_runtime.py narrative --case mon-cas --stage A2 --request stages/A2/attempt-1/narrative.json
python scripts/case_runtime.py narrative --case mon-cas --stage A3 --section valeur
python scripts/case_runtime.py narrative --case mon-cas --stage A4 --findings stages/A4/attempt-1/findings.json
```

Exécuter chaque appel pendant sa tentative. À A2, ajouter `case_id`, `kind` et `narrative_ref` aux champs de scaffold retournés. Le résultat A4 référence le fichier des écarts (`narrative_review_ref`), en plus des trois revues. Un écart ouvert bloque A4 et renvoie à l’étape propriétaire. Un reçu mécanique vert ne change pas l’approbation humaine. Les encarts restent candidats. Les limites de couverture et les observations d’un auteur restent déclaratives.

## Rendu et mémo de décision

Si `render_requested=true`, A3 fournit le `payload_ref` dans sa tentative. Le moteur
valide le schéma et l'identité. Après `begin A4`, appeler `case_runtime.py render --case ID`.
Le moteur invoque l'adapter épinglé et contrôle le PDF, ses pages physiques et `qa.json`.
Recopier le reçu exact dans le résultat A4. Un profil sans adapter déclare le rendu indisponible.
Le contrôle des octets reste distinct de la revue de fond et de la lecture visuelle.

Pour une décision technique, ajouter `decision_type` à l’intake. A2 fournit `decision_memo_ref`
dans sa tentative. Le moteur valide le type et le verdict du scaffold, puis épingle le mémo et
ses preuves. Ce contrôle s’ajoute au contrôle narratif si les deux profils sont demandés.

## Contrat du manifeste lui-même

`contracts/case-process.schema.json` est consommé avant l'initialisation. Il décrit
les étapes, profils de template, adapters, références stables et axes de loopback.
Le moteur vérifie en plus que renderer et schéma de payload font partie des références
épinglées du profil et que ce schéma est valide. Une demande de rendu sans adapter
est refusée avant de créer le dossier du cas. La release commune couvre ce contrat.
