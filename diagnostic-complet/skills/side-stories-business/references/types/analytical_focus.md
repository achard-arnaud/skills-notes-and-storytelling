# `[FOC]` Focus analytique

Tag `FOC`, couleur marine. Source de vérité : `workflows/side-stories.workflow.json`, type `analytical_focus`. Harvesté de `composing-side-stories` (dépôt tourisme) et de sa grammaire visuelle inspirée de `two-pager-nice`. Intègre l'ancien `false_lead` : une fausse piste est une position contrastée examinée puis écartée.

## Rôle

Traiter en une ou deux pages un mécanisme qui compte pour la décision mais qui est trop étroit pour une section du tronc.

## Choisir ce type quand

Le mécanisme appelle une thèse, deux positions défendables et un enseignement. **Pas** quand le contenu est un exemple (`illustration`) ou une définition (`veille_academique`).

## Format

**450 mots au plus**. Structure fixe dans `payload.analysis` :

| Champ | Contenu |
|---|---|
| `core_question` | La question centrale |
| `thesis` | La thèse retenue |
| `positions` | Au moins deux positions contrastées, chacune avec sa réserve (`position`, `caveat`) |
| `mechanisms` | Au moins un mécanisme, avec `evidence_status` parmi `verified`, `vendor_claim`, `inference`, `hypothesis`, `unknown` |
| `takeaway` | L'enseignement, qui nomme la décision du tronc concernée |

Grammaire visuelle (si rendu en page) : A4 paysage, question en tête, cartes de contraste, bandeau de mécanisme, tables de 5 colonnes au plus, schéma avant paragraphe faible.

## Squelette

```json
{
  "payload": {
    "analysis": {
      "core_question": "<Question centrale>",
      "thesis": "<Thèse retenue>",
      "positions": [
        {"position": "<Position A>", "caveat": "<Réserve A>"},
        {"position": "<Position B>", "caveat": "<Réserve B>"}
      ],
      "mechanisms": [
        {"mechanism": "<Mécanisme causal>", "evidence_status": "inference"}
      ],
      "takeaway": "<Enseignement, lié à la décision du tronc.>"
    }
  }
}
```

## Ligne éditoriale

- La thèse est contredite par au moins une position défendable avant d'être retenue.
- Chaque mécanisme porte un statut de preuve ; la présentation ne le relève jamais.
- Un schéma passe avant un paragraphe faible. Les tables ont 5 colonnes au plus.
- Un focus ne remplace pas une section : s'il porte la chaîne causale, il retourne dans le tronc.

## Style indicatif

Argumentatif, sobre : question, thèse, objections, mécanisme, enseignement. Chaque objection reçoit sa réponse ou sa réserve.

## Exemples KB

- `EX-FOC-01` : pourquoi un actif sous-performe, diagnostic à six causes, et intelligence distribuée contre intervention située. Grille de diagnostic générique, pas un incident de la cible.
- `EX-FOC-02` : « double cerveau ». **À collecter** : notion citée le 2026-11-09, absente de la KB et non définie ; fournir une définition et une source avant instruction.
- `EX-FOC-03` : retour d'expérience de cabinets sur les moteurs de l'IA dans les énergies renouvelables ou les certificats d'économies d'énergie. **Recherche requise** ; niveau de preuve `grey_literature`.

Identifiants et statuts : `workflows/kb-examples.json`.
