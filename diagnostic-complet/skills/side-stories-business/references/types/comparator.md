# `[CMP]` Comparatif

Tag `CMP`, couleur ardoise. Source de vérité : `workflows/side-stories.workflow.json`, type `comparator`. Intègre l'anti-thèse de l'ancien `false_lead` quand elle prend la forme d'une comparaison.

## Rôle

Situer la cible, ou un cas, par rapport à **3 à 5 acteurs ou cas** sur **un critère commun**, avec les différences de conditions de départ.

## Choisir ce type quand

Le lecteur doit situer quelqu'un par rapport à d'autres sur une même dimension de décision. **Pas** quand un seul cas éclaire le passage (`illustration`), ni quand la comparaison suppose un classement de performances non sourcé.

## Format

Une table de **5 colonnes au plus** et **3 à 5 lignes**, une cellule remplie par colonne et par ligne, **180 mots au plus** autour. Champs de premier niveau obligatoires : `criterion`, `confounders` (liste non vide), `takeaway`.

1. Écrire le critère commun avant la table.
2. Remplir la table, une ligne par acteur ou cas.
3. Lister les facteurs de confusion et les différences de conditions de départ.
4. Conclure en une phrase qui renvoie au critère de décision.

## Squelette

```json
{
  "criterion": "<Critère commun de comparaison>",
  "confounders": ["<Différence de conditions de départ>", "<Facteur de confusion>"],
  "takeaway": "<Conclusion unique, liée au critère.>",
  "payload": {
    "table": {
      "columns": ["Acteur", "Centre de gravité", "Avantage", "Risque"],
      "rows": [
        ["<Acteur A>", "<...>", "<...>", "<...>"],
        ["<Acteur B>", "<...>", "<...>", "<...>"],
        ["<Acteur C>", "<...>", "<...>", "<...>"]
      ]
    }
  }
}
```

## Ligne éditoriale

- Le critère est commun, écrit avant la table et lié à une décision.
- Les différences de conditions de départ et les limites de transférabilité sont visibles.
- Pas de classement ni de notation (« intensité IA », disponibilité, ROI) sans source publique. Un archétype est à instruire, pas un verdict.
- Un benchmark de cas d'usage compare des cas décrits par des sources de même nature ; sinon le dire.

## Style indicatif

Neutre et symétrique : mêmes verbes, même niveau de détail par ligne. Le ton ne favorise aucun acteur.

## Exemples KB

- `EX-CMP-01` : trois archétypes d'acteurs et cinq concurrents nommés, à comparer sur quatre modèles de création de valeur (proximité et contrat, financement, exploitation, couche numérique). Le document source recommande de ne pas noter les acteurs sans preuves publiques : la table décrit, elle ne classe pas.
- `EX-CMP-02` : benchmark avec des cas d'usage d'acteurs. **À confirmer** : la demande du 2026-11-09 s'arrête à « avec les uses cases de » ; fournir la liste des acteurs.

Identifiants et statuts : `workflows/kb-examples.json`.
