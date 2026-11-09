# `[ILL]` Illustration

Tag `ILL`, couleur violette. Source de vérité : `workflows/side-stories.workflow.json`, type `illustration`. Regroupe `portrait`, `detour`, `also` et `object_focus`, dont les rôles se recouvraient.

## Rôle

Un cas d'usage, une citation de référence, un objet ou une personne qui **éclaire le passage sans ajouter de thèse**.

## Choisir ce type quand

Un exemple concret rend le passage lisible. **Pas** quand l'exemple porte une thèse (`analytical_focus`) ni quand il doit être comparé à d'autres (`comparator`).

## Format

Une forme parmi `use_case`, `quote`, `object`, `person`. **150 mots au plus** ; une citation tient en **40 mots** et porte `attributed_to`, `date`, `source`.

| Forme | Contenu |
|---|---|
| `use_case` | Besoin, action, résultat attendu. Le cadre « B-A-C » cité dans la demande n'est défini dans aucune source : cadre laissé libre jusqu'à confirmation |
| `quote` | Verbatim, daté, attribué, sourcé |
| `object` | Un équipement, un document ou une mesure, et ce qu'il éclaire |
| `person` | Un porteur du mécanisme, avec la borne de ce qu'on en dit |

## Squelette

```json
{
  "payload": {
    "form": "use_case",
    "text": "<Besoin, action, résultat attendu, en quelques phrases. Cas candidat, existence chez la cible à confirmer.>"
  }
}
```

Pour une citation :

```json
{
  "payload": {
    "form": "quote",
    "text": "<Citation verbatim, 40 mots au plus.>",
    "attributed_to": "<Nom, fonction>",
    "date": "AAAA-MM-JJ",
    "source": "<URL ou référence>"
  }
}
```

## Ligne éditoriale

- Une citation est **verbatim**, datée, attribuée et sourcée. Elle n'est jamais reconstituée ni paraphrasée entre guillemets.
- Un cas d'usage reste candidat tant que son existence chez la cible n'est pas confirmée.
- La contribution au passage et la borne sont explicites : pas d'anecdote gratuite.

## Style indicatif

Concret et bref. Une phrase pour situer, une pour l'apport, une pour la borne. Aucune émotion ajoutée.

## Exemples KB

- `EX-ILL-01` : IA multimodale au service des intervenants sur site (cas d'usage candidat, non confirmé comme cas de la cible). À rédiger au conditionnel.
- `EX-ILL-02` : citation de référence d'un dirigeant de l'industrie. **Recherche requise** : aucune citation dans la KB ; collecter la source avant de rédiger.

Identifiants et statuts : `workflows/kb-examples.json`.
