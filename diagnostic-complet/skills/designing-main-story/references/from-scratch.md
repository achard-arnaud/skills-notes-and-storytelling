# Mode `from-scratch` — repartir des preuves

Même moteur que l'itératif, entrée sans ancien lecteur. Commande : `python3 diagnostic-complet/writing.py from-scratch evidence-only.json prepared.json [--scaffold reader-topology.json]`.

## Ordre des opérations

1. **Entrée evidence-only** : identité, mandat, piliers, sources, fragments, claims, relations. Une étude qui contient déjà `sections` ou `side_stories` est refusée : une prose antérieure, même renommée, n'est pas une preuve.
2. **Topologie lecteur** (facultative) : si François a choisi un ordre, ne fournir que l'ordre, les titres, les IDs de claims et de piliers. Sans topologie, une seule section candidate cadrée par la question du mandat.
3. **Problème avant chronologie** (contrat repris du dépôt tourisme) : chaque section démarre d'un problème borné auquel le graphe peut répondre. Le problème est un cadre éditorial, pas une preuve ; il n'implique aucune réponse causale que le graphe ne soutient pas.
4. **Preuve avant conséquence** : scène ou constat, mécanisme local, conséquence locale, puis seulement dézoom vers un système plus large, puis retour. Ne jamais ouvrir par la conséquence abstraite pour recoller des faits en exemples.
5. **Tronc ou side story** : un fragment reste dans le tronc si le retirer casse l'explication (mobilisation, coalition, coût de gouvernance, flux, reproduction, changement de régime, mécanisme qui rend l'un d'eux possible). Sinon, c'est un candidat side story. Ne pas rétrograder un dézoom causal nécessaire en side story parce qu'il change d'échelle.
6. **Rédaction externe** : fragments et sources comme matériaux, claims comme contrôle, puis revue indépendante du tronc et gel. Ce module ne rédige aucun fait.
7. **Qualification des side stories** après gel du tronc : type, problématique, ponts (`side-stories-business`), puis vérification des retours et de l'insertion.

## Receipt à lire

`reader_prose_loaded=false` et état `scaffold_candidate_not_drafted`. Ce receipt porte sur les entrées acceptées : un fichier mal étiqueté ne peut pas être détecté par le script, donc vérifier à la main que l'entrée est bien evidence-only.

## Points de vigilance

- Les matériaux fournis ne sont pas des sources primaires vérifiées : leurs claims restent `supplied_claim` ou `hypothesis`.
- Une fiche fournisseur ne prouve ni déploiement, ni intégration, ni ROI chez la cible.
- Le compte (réalité de l'acheteur) et l'offre (vérité du vendeur) restent indépendants jusqu'à une étape de fit explicite.
