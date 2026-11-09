# Gate local équivalent à la CI désactivée

Les commits de passation portent `[skip ci]`. Ce gate reproduit, en local, les deux workflows du dépôt. Un PASS local n'est pas un PASS CI : il est déclaré comme tel dans les reçus (`ci: intentionally_not_run`).

## Environnement

Installer les dépendances du renderer hors dépôt :

```bash
python3 -m venv /tmp/gate-venv
/tmp/gate-venv/bin/pip install -r renderers/pedagogical/requirements.txt
```

Le navigateur Chromium est attendu sur `/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`. Ne pas lancer `playwright install`.

## Commandes

```bash
# 1. Contrôle des contrats racine (workflow skill-qa)
python3 scripts/validate_contracts.py

# 2. Tests pédagogiques avec navigateur (workflow pedagogical-render)
PEDAGOGICAL_BROWSER_TEST=1 NICE_CHROMIUM_PATH=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome \
  /tmp/gate-venv/bin/python -m unittest discover -s tests -p 'test_pedagogical*.py' -v

# 3. Rendu paysage et vérification (workflow pedagogical-render)
NICE_CHROMIUM_PATH=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome \
  /tmp/gate-venv/bin/python renderers/pedagogical/landscape.py learning/enterprise-ai/perception.sheet.json --out /tmp/pedagogical-render/perception
NICE_CHROMIUM_PATH=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome \
  /tmp/gate-venv/bin/python renderers/pedagogical/landscape.py learning/enterprise-ai/perception.sheet.json --out /tmp/pedagogical-render/perception --verify

# 4. Suite de passation (sous-projet)
python3 -m unittest discover -s diagnostic-complet/tests -v

# 5. QA visuelle du rendu HTML synthétique
python3 diagnostic-complet/render.py diagnostic-complet/fixtures/synthetic.json /tmp/study.html
```

Le contrôle 5 se lit ensuite dans un navigateur : scripts absents, aucun débordement horizontal à 390 px, aucune ressource externe.

## Résultats observés à `d29882b`

| Contrôle | Résultat |
|---|---|
| 1. `validate_contracts.py` | PASS — templates=10 modes=4 workflow=1.3.1 |
| 2. Tests pédagogiques (navigateur réel) | 13 tests, OK |
| 3. Rendu `perception` + `--verify` | rc=0, six pages PNG générées |
| 4. Suite passation | 105 tests, OK |
| 5. HTML synthétique | 0 erreur JavaScript ; 0 débordement à 1280 px et 390 px ; 0 ressource externe |

## Échec connu, hors passation

`python3 -m unittest discover -s tests -p 'test_*.py'` sans venv échoue à l'import (`ModuleNotFoundError: markdown`). Échec présent au commit de base `74a6354` ; le workflow CI installe les dépendances avant d'exécuter ces tests.
