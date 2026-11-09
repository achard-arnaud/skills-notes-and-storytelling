# Paquet de rendu d'une side story

Le rédacteur d'une side story ne lit pas l'étude entière. Il reçoit ce paquet, assemblé par le skill de pilier puis complété par `side-stories-business`. Un paquet incomplet bloque la rédaction : mieux vaut un refus clair qu'un encart sans question.

## Champs (définis dans `workflows/side-stories.workflow.json`, `renderer_packet`)

| Champ | Contenu | Origine |
|---|---|---|
| `kind` | Type canonique | Arbre de choix |
| `pillar_ids` | Piliers concernés | Skill de pilier |
| `parent_section_id`, `return_to` | Ancres de départ et de retour, qui doivent résoudre | Plan du tronc |
| `main_passage` | Identifiant du passage et une phrase de ce que le tronc vient d'établir | `designing-main-story` |
| `problematique` | Une seule question à laquelle l'encart répond | Skill de pilier (liste dans `pillar_routing`) |
| `bridge.in` | Phrase qui fait entrer depuis le tronc | Skill de pilier |
| `bridge.out` | Phrase qui ramène au tronc | Skill de pilier |
| `bridge.callback_to` | Ancre optionnelle vers une notion déjà éclairée | Plan du tronc |
| `reason_outside` | Pourquoi ce n'est pas dans le tronc | `side-stories-business` |
| `payoff` | Ce que le lecteur comprend en plus | `side-stories-business` |
| `claim_ids` | Claims mobilisés, avec leur statut | Étude |
| `format` | Compteurs, champs, longueurs du type | Workflow |
| `style` | Style indicatif du type | Fichier de référence du type |
| `forbidden` | Ce que l'encart ne peut pas affirmer | Statuts des claims |

## Pourquoi problématique et ponts sont obligatoires

La problématique donne un critère d'arrêt : tout ce qui n'aide pas à y répondre sort. Les ponts rendent l'encart lisible : sans pont d'entrée, il surgit ; sans pont de sortie, il ne rend rien au tronc. `runtime.py validate` les exige à partir de l'état `validated`, et les signale comme lacune pour un candidat.

## Mode auto-cohérence (section `self_consistency` du workflow)

1. **Reformuler.** Une passe indépendante, qui ne voit que le texte rédigé, écrit la problématique, le pont d'entrée et le pont de sortie qu'elle en déduit. Si elle ne retrouve pas ceux du paquet, le texte ne tient pas seul : réécrire, pas ajuster le paquet pour l'accorder.
2. **Tracer.** Chaque affirmation renvoie à un claim ou à une source du paquet. Une affirmation sans renvoi est retirée ou marquée hypothèse.
3. **Ne pas relever.** La mise en forme ne change aucun statut : un claim fourni reste fourni.
4. **Séparer.** Aucun fait du compte n'est mélangé à un argument d'offre.
5. **Contrôles mécaniques.** `runtime.py validate` vérifie compteurs, champs, longueurs et ancres.

Au plus deux réparations sur la même cause, puis l'encart est marqué bloqué avec la preuve et le travail indépendant continue (D10).

## Exemple de paquet (synthétique)

```json
{
  "kind": "dezoom",
  "pillar_ids": ["P-GOVERNANCE"],
  "parent_section_id": "SEC1",
  "return_to": "PAR1",
  "main_passage": "PAR1 : le tronc vient d'établir qu'un signal de sous-performance n'est exploitable que s'il arrive avec son contexte contractuel.",
  "problematique": "Pourquoi la dépendance à une interface fournisseur change-t-elle la capacité de contrôle d'un portefeuille ?",
  "bridge": {"in": "Ce qui vaut pour un site se joue autrement à l'échelle du portefeuille.", "out": "On revient au signal : sa lecture dépend de qui contrôle la donnée."},
  "reason_outside": "Le mécanisme est contractuel, pas opérationnel : il ne fait pas partie de la chaîne du signal.",
  "payoff": "Comprendre pourquoi un même signal vaut différemment selon les droits sur la donnée.",
  "claim_ids": ["C1"],
  "format": "3 temps, 220 mots au plus, scale_from, scale_to, mechanism",
  "style": "sobre, dense, conditionnel pour les hypothèses",
  "forbidden": ["aucun chiffre sectoriel sans source", "ne pas présenter l'avantage d'orchestration comme acquis"]
}
```
