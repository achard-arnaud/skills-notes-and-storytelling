# Veille entreprise : pitch d'entreprise

Libellé affiché : **Veille entreprise** (code interne `VCP`, jamais montré au lecteur) ; couleur cyan. Source de vérité : `workflows/side-stories.workflow.json`, type `veille_corporate_perso`.

## Rôle

Présenter une entreprise ou une offre en **10 à 15 lignes**, à partir de signaux publics, avec une **lecture personnelle signée** séparée des faits. Le format adapte `templates/one-pager.md` (réponse en tête, 3 à 5 faits décisifs, une comparaison éventuelle, une implication, sources compactes), sans en importer les autres exigences. La skill « pitch business » citée comme base n'est ni dans les skills synchronisés ni dans les dépôts accessibles : le métaprompt ci-dessous est une adaptation minimale à creuser.

## Choisir ce type quand

Le lecteur doit comprendre vite qui est cet acteur, ce qu'il vend, avec quelles preuves publiques, et ce que cela implique pour le récit. **Pas** quand il faut comparer plusieurs acteurs (`comparator`) ni instruire un mécanisme (`analytical_focus`).

## Format

Dix familles de lignes, une idée par ligne, 32 mots au plus par ligne, 10 à 15 lignes au total.

| Rôle de ligne | Nombre | Contenu |
|---|---|---|
| `headline` | 1, en tête | Qui, pour qui, quoi, en une phrase |
| `offer` | 1 à 2 | Ce que l'entreprise vend |
| `model` | 0 à 1 | Comment elle gagne de l'argent |
| `client_problem` | 1 | L'enjeu client adressé |
| `fact` | 3 à 5 | Fait public, avec `date` et `source` obligatoires |
| `differentiation` | 1 | Position dans la chaîne de valeur |
| `limit` | 1 au moins | Ce qui n'est pas prouvé ou reste inconnu |
| `personal_reading` | 1 | Lecture de l'auteur, signée, séparée des faits |
| `implication` | 1 au moins | Ce que cela change pour le passage ; nomme le passage |
| `sources` | 0 à 1 | Références compactes |

## Squelette

```json
{
  "payload": {
    "lines": [
      {"role": "headline", "text": "<Entreprise> vend <offre> à <client> pour <résultat>."},
      {"role": "offer", "text": "<Ce qu'elle propose, en une phrase.>"},
      {"role": "model", "text": "<Modèle économique déclaré.>"},
      {"role": "client_problem", "text": "<Enjeu client adressé.>"},
      {"role": "fact", "text": "<Fait public 1.>", "date": "AAAA-MM-JJ", "source": "<URL ou référence>"},
      {"role": "fact", "text": "<Fait public 2.>", "date": "AAAA-MM-JJ", "source": "<URL ou référence>"},
      {"role": "fact", "text": "<Fait public 3.>", "date": "AAAA-MM-JJ", "source": "<URL ou référence>"},
      {"role": "differentiation", "text": "<Position dans la chaîne de valeur.>"},
      {"role": "limit", "text": "<Ce qui n'est pas prouvé.>"},
      {"role": "personal_reading", "text": "Lecture de l'auteur : <opinion séparée des faits>."},
      {"role": "implication", "text": "<Ce que cela change pour le passage SEC1.>"},
      {"role": "sources", "text": "<Références compactes.>"}
    ]
  }
}
```

## Ligne éditoriale

- Le fait d'abord, l'opinion ensuite, jamais dans la même ligne.
- `personal_reading` est signée « lecture de l'auteur » : elle ne vaut ni position de l'entreprise ni verdict du rapport.
- Chaque fait est daté et sourcé par une source publique identifiable. Une page produit prouve l'offre, pas un déploiement, une intégration ni un ROI chez la cible.
- Aucun jugement sur des personnes ; aucun argument d'offre ou de fit fournisseur : le compte et l'offre restent séparés jusqu'au stade de fit.

## Style indicatif

Registre d'analyste : phrases courtes, verbes d'état, pas de superlatif. Les mots du fournisseur ne sont pas repris tels quels. Le conditionnel porte toute inférence.

## Métaprompt (brouillon, à creuser)

```text
Tu rédiges une side story de type veille entreprise, pitch de <ENTREPRISE> en 10 à 15 lignes.
Entrées : signaux publics datés et sourcés <SIGNAUX>, problématique <PROBLEMATIQUE>,
passage d'accueil <PASSAGE>, pont d'entrée <BRIDGE_IN>, pont de sortie <BRIDGE_OUT>.
Contraintes : une idée par ligne, 32 mots au plus ; ordre headline, offer, model,
client_problem, fact (3 à 5, chacun avec date et source), differentiation, limit,
personal_reading (signée), implication (nomme le passage), sources.
Interdits : fait sans source, opinion dans une ligne de fait, promesse de gain,
argument d'offre, jugement sur une personne.
Sortie : JSON payload.lines uniquement.
Auto-contrôle : relis tes lignes sans le paquet ; retrouves-tu la problématique et les
deux ponts ? Sinon réécris. Deux réparations au plus.
```

À creuser : variantes par taille d'acteur, règle de choix des 3 à 5 faits, gabarit de la ligne `model` quand le modèle économique n'est pas public.

## Exemples KB

- `EX-VCP-01` : pitch d'une offre de monitoring énergétique à partir de pages corporate. Regarder comment une page produit devient trois faits datés et une ligne `limit`.
- `EX-VCP-02` : fragments « Land & Scale » comme référence d'autorité. Le document source dit que ces étiquettes ne sont pas canoniques : retrouver la référence paginée avant de citer.
- `EX-VCP-03` : pitch et retour d'expérience « Ask for the moon » pour Framatome. **À collecter** : aucune source dans la KB ; l'idée (RAG agentique multimodal + KB à ontologie pour l'assistance à la maintenance sur site) reste une piste.

Identifiants et statuts : `workflows/kb-examples.json`.
