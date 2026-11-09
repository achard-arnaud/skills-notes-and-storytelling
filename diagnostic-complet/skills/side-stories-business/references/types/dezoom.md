# `[DZ]` Dézoom

Tag `DZ`, couleur fuchsia. Source de vérité : `workflows/side-stories.workflow.json`, type `dezoom`. Harvesté de `zooming-geographic-scales` (échelles Z0 à Z4), transposé aux échelles business.

## Rôle

Changer d'échelle pour expliquer un mécanisme local, puis **revenir au local avec un gain explicite**. Échelles courantes : équipement, site, portefeuille, groupe, secteur.

## Choisir ce type quand

Une observation locale ne s'explique que par un mécanisme d'une autre échelle, et ce mécanisme n'est pas une étape de la chaîne causale du tronc. **Pas** quand le changement d'échelle est nécessaire à l'explication : il reste alors dans le tronc, même s'il change d'échelle.

## Format

Trois temps, **220 mots au plus**, un schéma ou une table de 5 colonnes au plus en option. Champs de premier niveau obligatoires : `scale_from`, `scale_to` (différentes), `mechanism`.

| Temps | Contenu |
|---|---|
| 1 | Le constat local, tel que le tronc l'a établi |
| 2 | Le canal de transmission vers l'échelle supérieure (nommé, jamais supposé) |
| 3 | Le retour local : ce que l'on peut maintenant observer ou décider |

## Squelette

```json
{
  "scale_from": "site",
  "scale_to": "portefeuille",
  "mechanism": "<canal de transmission nommé>",
  "payload": {
    "steps": [
      {"scale": "site", "statement": "<Constat local.>"},
      {"scale": "portefeuille", "statement": "<Canal de transmission et effet à cette échelle.>"},
      {"scale": "site", "statement": "<Gain local explicite.>"}
    ]
  }
}
```

## Ligne éditoriale

- Le mécanisme de transmission est nommé et sourcé. Une corrélation n'est pas un canal.
- Le retour explique quelque chose d'observable localement ; sinon c'est un commentaire détaché.
- Aucun chiffre sectoriel sans source ; un indicateur national n'est pas une mesure de la cible.
- Un dézoom ne remplace jamais une étape de la chaîne causale.

## Style indicatif

Trois paragraphes courts qui suivent les trois temps. Une phrase de transition par changement d'échelle. Conditionnel dès que le canal n'est qu'une hypothèse.

## Exemples KB

- `EX-DZ-01` : de l'installation à l'agrégateur, verrouillage fournisseur et couche d'orchestration indépendante. Bon modèle : le canal de transmission est l'accès aux données ; le retour est la capacité de lire un signal local avec son contexte de contrat. L'avantage d'orchestration reste une hypothèse.
- `EX-DZ-02` : investissements des concurrents dans l'IA. **Recherche requise** : la source existante ne donne que des noms et déclare ne pas sourcer les chiffres ; ne reprendre aucun montant.

Identifiants et statuts : `workflows/kb-examples.json`.
