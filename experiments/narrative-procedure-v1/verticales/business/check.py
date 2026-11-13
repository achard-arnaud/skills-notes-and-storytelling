"""Contrôle des fixtures synthétiques. Exécuter depuis tout répertoire."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
def load(path):
    return json.loads((ROOT / path).read_text())
def check_trial(trial):
    errors = []
    if trial['threshold_cases'] * trial['assumed_saving_eur_per_case'] != trial['fixed_cost_eur']:
        errors.append('seuil économique incorrect')
    if trial['benefit_status'] != 'hypothesis':
        errors.append('économie fournisseur promue en résultat vérifié')
    return errors
def run():
    formats = load('manifest.json')['formats']
    for name, contract in formats.items():
        fixture = load(contract['fixture'])
        assert fixture['template'] == name
        assert fixture['expected']['blocks'] == contract['block_ids']
        assert list(fixture['sample_blocks']) == contract['block_ids']
        inputs = fixture['input']
        assert inputs['C3']['eligible_volume'] is None
        assert fixture['expected']['threshold_cases'] * inputs['C2']['saving_eur_per_case'] == inputs['C1']['launch_cost_eur']
    first = check_trial(load('trial-v1.json'))
    second = check_trial(load('trial-v2.json'))
    assert first == ['économie fournisseur promue en résultat vérifié'] and not second
    print(json.dumps({'fixtures':list(formats),'v1_errors':first,'v2_errors':second,'result':'PASS'},ensure_ascii=False))
if __name__ == '__main__':
    run()
