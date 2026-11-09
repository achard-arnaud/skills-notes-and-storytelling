# Veille académique : mini-wiki sourcé

Libellé affiché : **Veille académique** (code interne `VAC`, jamais montré au lecteur) ; couleur indigo. Source de vérité : `workflows/side-stories.workflow.json`, type `veille_academique`.

## Rôle

Installer **5 à 7 notions** sous forme de lexique, chacune en cinq blocs, avec une source explicite et un contre-point. Le lecteur sort de l'encart avec des termes définis et leur portée, puis revient au passage. Remplace l'ancien `method`.

## Choisir ce type quand

Le lecteur a besoin de notions définies, avec source, contre-exemple et lien avec le passage, avant de suivre un raisonnement. **Pas** quand il faut défendre une thèse avec des positions contrastées (`analytical_focus`) ou comparer des acteurs (`comparator`).

## Format

Un lexique de 5 à 7 entrées. Chaque entrée, 120 mots au plus (hors tableau ou schéma) :

| Champ | Contenu |
|---|---|
| `term` | La notion |
| `definition` | Définition sourcée ou thèse : `text`, `source` (`author`, `year`, `venue_or_url`), `evidence_level` |
| `example` | Exemple général ou illustration, hors cas |
| `in_practice` | En pratique dans le contexte immédiat : lien explicite avec le passage de la main story où l'encart est mobilisé |
| `contrast` | Comparatif ou anti-thèse rapide |
| `perspective` | Mise en perspective : `mode` parmi `table`, `schema`, `synthesis` ; une synthèse tient en 1 à 2 phrases |

Niveaux de preuve : `peer_reviewed`, `preprint`, `grey_literature`, `opinion`, `supplied` (matériau fourni, non vérifié dans l'ouvrage).

## Squelette

```json
{
  "payload": {
    "items": [
      {"term": "<Notion 1>",
       "definition": {"text": "<Définition sourcée.>", "source": {"author": "<Auteur>", "year": "<Année>", "venue_or_url": "<Revue ou URL>"}, "evidence_level": "supplied"},
       "example": "<Exemple général.>",
       "in_practice": "<Dans le passage SEC1, la notion sert à ...>",
       "contrast": "<Anti-thèse rapide.>",
       "perspective": {"mode": "synthesis", "content": "<Une ou deux phrases.>"}},
      {"term": "<Notion 2>", "definition": {"text": "<...>", "source": {"author": "<...>", "year": "<...>", "venue_or_url": "<...>"}, "evidence_level": "supplied"}, "example": "<...>", "in_practice": "<...>", "contrast": "<...>", "perspective": {"mode": "table", "content": "<tableau croisé>"}},
      {"term": "<Notion 3>", "definition": {"text": "<...>", "source": {"author": "<...>", "year": "<...>", "venue_or_url": "<...>"}, "evidence_level": "supplied"}, "example": "<...>", "in_practice": "<...>", "contrast": "<...>", "perspective": {"mode": "schema", "content": "<source du schéma>"}},
      {"term": "<Notion 4>", "definition": {"text": "<...>", "source": {"author": "<...>", "year": "<...>", "venue_or_url": "<...>"}, "evidence_level": "supplied"}, "example": "<...>", "in_practice": "<...>", "contrast": "<...>", "perspective": {"mode": "synthesis", "content": "<...>"}},
      {"term": "<Notion 5>", "definition": {"text": "<...>", "source": {"author": "<...>", "year": "<...>", "venue_or_url": "<...>"}, "evidence_level": "supplied"}, "example": "<...>", "in_practice": "<...>", "contrast": "<...>", "perspective": {"mode": "synthesis", "content": "<...>"}}
    ]
  }
}
```

## Ligne éditoriale

- Prudence sur les résultats : distinguer rapporté, reproduit et contesté.
- Dire le contexte de l'étude (taille, population, durée, conditions) avant toute extrapolation. `in_practice` est le **seul** lieu du transfert au cas.
- Le contre-point est obligatoire : une entrée sans anti-thèse est incomplète.
- Les préprints sont signalés comme tels ; une source non citable n'entre pas.
- Une définition issue d'une synthèse fournie reste `supplied` tant qu'elle n'a pas été retrouvée dans l'ouvrage avec sa page.

## Style indicatif

Registre encyclopédique : définitions en une phrase, termes stables d'une entrée à l'autre, pas de voix personnelle. La seule trace du contexte est `in_practice`.

## Métaprompt (brouillon)

```text
Tu rédiges une side story de type veille académique : lexique de <N> entrées (5 à 7) pour le passage <PASSAGE>.
Entrées : notions <NOTIONS>, sources citables <SOURCES>, problématique <PROBLEMATIQUE>.
Pour chaque notion : definition (text, source auteur/année/lieu, evidence_level), example hors cas,
in_practice qui cite le passage, contrast (anti-thèse rapide), perspective (table, schéma ou
synthèse de 1 à 2 phrases). 120 mots au plus par entrée.
Interdits : source non citable, extrapolation hors du contexte de l'étude, entrée sans contre-point.
Sortie : JSON payload.items uniquement.
Auto-contrôle : chaque définition renvoie-t-elle à une source présente dans le paquet ?
```

## Exemples KB

- `EX-VAC-01` : les quatre postures d'adoption de l'IA et leur arbitrage. Bon modèle d'entrée avec anti-thèse (« risque si appliquée seule »). Hypothèse d'arbitrage dans une synthèse fournie : niveau `supplied`.
- `EX-VAC-02` : cinq capacités de l'IA (perception, création, prédiction, raisonnement, agentique), principes TRICUS, seuil de 10 K$. **À ingérer** : le rapport a été fourni dans la conversation du 2026-11-09 et n'est pas dans la KB ; vérifier chaque définition dans l'ouvrage avant usage.

Identifiants et statuts : `workflows/kb-examples.json`.
