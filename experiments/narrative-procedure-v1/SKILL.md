---
name: compose-decision-narrative
description: Composer ou réviser une note, un one/two/three-pager, une étude produit, une note business ou technique ou un support pédagogique depuis des preuves et analyses explicites. Sélectionner le contrat de format, diriger le scaffold, rédiger bloc par bloc, relire le récit et préparer sa livraison. Demander une analyse spécialisée quand elle manque.
---

# Compose Decision Narrative — candidat expérimental

Livrer une réponse utile au lecteur en conservant les preuves et le contexte. La procédure est commune ; les contrats de contenu, chartes et rendus se choisissent à la demande. Cette skill ne collecte pas automatiquement les sources et ne conduit pas tous les frameworks d’analyse.

## Cadrer et charger seulement ce qui sert
Identifier objectif du lecteur, décision ou acquis attendu, sujet/entités, scope, horizon, sources, mode neuf/itératif et support. En itératif, épingler la baseline et le delta avant de modifier le contenu. Distinguer information manquante bloquante et inconnue que le livrable peut rendre visible.
Lire [le routage](references/routing.md) pour choisir une route principale et le contrat de format. Lire seulement le template sélectionné et ses obligations. Les angles secondaires sont autorisés. Ne pas choisir les chapitres à partir des piliers d’analyse.
Lire [le contrat analytique](references/analysis-interface.md) seulement si une analyse spécialisée est requise, reçue ou modifiée. Les faits d’entreprise doivent garder date, scope et source ; un rapport précédent est un pointeur vers ses preuves.

## 1. Diriger le scaffold
Formuler une question centrale et une réponse calibrée au niveau de preuve. Pour l’apprentissage, préciser l’acquis démontrable. Nommer la tension utile sans dramatiser. Construire l’ordre des questions du lecteur, puis attribuer aux blocs : ID, question, action title ou titre pédagogique, payoff, claim_refs/analysis_refs, limites, objection matérielle, transition, rôle visuel et contrainte de format.
Lire [la charte rédactionnelle](references/editorial.md). Une thèse peut rester une hypothèse ; une liste de sujets n’est pas une démonstration.
Sortie : scaffold et liste de preuves manquantes. Si le raisonnement manque, ouvrir une demande analytique bornée ; ne pas remplir par une prose plausible.

## 2. Rédiger bloc par bloc
Rédiger chaque bloc depuis ses seules preuves/analyses. Préserver noms, unités, dates, scope, attributions, inconnues et contre-preuves. Une analyse externe reste distincte d’une preuve primaire.
Conserver une claim-map et les blocs hors delta. Ne pas changer la thèse en remplissant un bloc sans rouvrir le scaffold. Pour un cas d’usage, montrer acteur, tâche, parcours, valeur attendue, conditions, statut de démonstration et mesure pertinente.
Les cartes, tableaux, schémas et apartés servent le lecteur ; ils ne rehaussent aucun statut de preuve.
Sortie : blocs rédigés et claim-map ; marquer les gaps.

## 3. Relire à l’échelle du récit
Lire les titres seuls, puis les transitions et la conclusion. Vérifier réponse à la question, niveau de zoom, causalité, répétitions, contradictions, alignement sur la tension et absence de perte décisionnelle. Tester l’objection qui pourrait inverser la conclusion. Relire le découpage sous un critère commun, en déclarant les recouvrements réels.
Lire [les contrôles et retours](references/review.md). Rouvrir l’étape 1 pour une thèse ou structure défectueuse ; l’étape 2 pour une formulation, attribution ou omission locale. Réserver l’approbation humaine à son propriétaire réel.
Sortie : constats, corrections, périmètre rouvert et verdict explicite.

Avant de conclure la revue, écrire dans le livrable lui-même l’objection qui pourrait inverser la thèse et l’observation qui ferait changer la recommandation. Une réserve générale ou une mention PASS dans review.json ne suffit pas. Tester les titres seuls : chaque titre directeur porte une conclusion qualifiée ou un acquis attendu ; réserver les titres descriptifs aux repères qui le nécessitent.

## 4. Livrer et réactiver si nécessaire
Mapper les blocs au contrat choisi : longueur, ordre, sections, sources, liens, chartes et support. Vérifier le rendu si produit ; un Markdown à deux sections n’est pas deux pages physiques vérifiées. Ne pas réduire la police ni supprimer un risque critique pour tenir la pagination.
Un défaut de preuve retourne au paquet analytique/source ; un défaut d’ordre à 1 ; un défaut de texte à 2 ; un défaut de cohérence à 3 ; un défaut de rendu au renderer. Une réparation ciblée puis une vérification ; échec matériel persistant = REOPEN_TARGETED avec condition de reprise.
Livrer contenu, références et limites de validation réelles. Effectuer un loopback léger : observation, couche concernée, delta réutilisable ou NO_REUSABLE_DELTA. Aucun changement canonique automatique.

Le livrable diffusé seul reste compréhensible : résoudre les codes de source/claim dans une légende compacte ou conserver des attributions textuelles autonomes. Un cas proposé doit expliciter les capacités nécessaires encore non attestées, notamment accès et ingestion documentaire. Tester ce point avant de présenter un parcours comme immédiatement réalisable.

## Choisir le scaffold d’une verticale

Pour une note à plusieurs blocs ou une révision ciblée, ouvrir [le registre des quatre verticales](verticales/registry.json). Choisir le couple route et template, puis ouvrir le profil et le manifeste indiqués. Le manifeste attribue les blocs aux rôles et indique la fixture à rejouer après modification. Une tâche simple peut suivre directement le contrat de format. [Résultats du second essai et revue de consolidation](verticales/README.md).

## Ressources conditionnelles
- [Routage et formats](references/routing.md) : intention/format ou révision de format.
- [Charte rédactionnelle](references/editorial.md) : conception et rédaction.
- [Contrôles](references/review.md) : revue et sortie.
- [Interface d’analyse](references/analysis-interface.md) : import ou demande d’analyse.
- [Three-pager candidat](references/three-pager.md) : seulement si ce format est demandé.
- [Sources de méthode](references/sources.md) : audit ou approfondissement de la méthode.

