# Bootstrap et rétro-analyse Current AI
14 novembre 2026. Lecture prête sur le périmètre vérifié. main épinglé à 7000c86a7e54cafc68c5bb5ada9aeed5df186aae ; candidat à 4827b03c6a49f6718496a8ce7218f44891b06a20. Audit documentaire, sans nouveau test de génération ni de rendu.

## Sources et limites
Demande et retours utilisateur visibles dans la conversation courante ; [brief rejoué](evals/current-ai/brief.md), [manifeste des sources](evals/current-ai/source-manifest.json), [trace A](evals/current-ai/A/process.json), [sortie A](evals/current-ai/A/two-pager.md), [sortie renforcée B2](evals/current-ai/B2/two-pager.md), SKILL.md et references/review.md candidats ; SKILL.md, references/workflow.md et templates/architecture-note.md de main au SHA ci-dessus.
La recherche des échanges antérieurs retourne des extraits d’anciennes réponses d’assistant. Ce matériau situe le dossier mais ne fournit ni conversation intégrale ni artefact original rendu. Les recherches de fichiers Current AI/Potluck n’ont pas identifié l’original. La reconstruction du résultat apprécié repose donc sur les retours utilisateur explicites ; les exemples ci-dessous sont des attentes reconstruites. Aucun chiffre historique repris comme fait actuel.

## Diagnostic des écarts
| Couche | Preuve localisée | Effet |
|---|---|---|
| Recherche du replay | brief Current AI, source unique et recherche externe interdite | Résumé de l’annonce, nombreuses inconnues ; pas de découverte du produit réel |
| Rendu du replay | brief et trace A, Markdown et pages logiques | Aperçus, widgets et architecture visuelle absents de l’évaluation |
| Cadrage | trace A et sorties A/B2, priorité Alpha puis cadrage de pilote | L’agent prépare un arbitrage que le corpus ne suffit pas à instruire |
| Main | workflow recherche → fragments → claims → scaffold ; architecture-note avec séquences métier détaillées | La méthode porte davantage de profondeur analytique que le replay n’en exploite |
| Main | smallest reversible step, lead with decision, clôture pilote sur certains formats | Le biais vers la recommandation existe également dans la baseline |
| Candidat actuel | huit finalités et recherche réintroduites, mais aucun lien vers le présent contrat avant cet audit | Correction du périmètre ; cible de richesse, combinaison business-produit et rendu encore sous-spécifiés |
| Contrôles | references/review.md exige objection/test dans la prose et vérification avant pilote | Contradiction avec le nouveau mandat descriptif si appliqué systématiquement |
| Validation | scores sur brief réécrit, fixtures de structure | Conformité locale récompensée sans comparaison au résultat réellement apprécié |

Le contraste entre le run aimé et les sorties est explicable par le changement d’entrées, de recherche, de mandat et de support. L’attribution causale à la seule skill main/candidate reste impossible avec ces essais. Une notation 10/10 sur ce dispositif ne constitue aucune preuve de transfert.

## Reconstruction de la logique appréciée
Les retours du demandeur nomment une narration orientée business case et produit, des produits liés à leur présentation, des use cases détaillés, une architecture fonctionnelle, un gap et des KPI, un récapitulatif et une navigation plaisante. Ils demandent en complément une signalétique société plus complète.

Hypothèse de progression à tester sur le dossier original lorsqu’il sera retrouvé :
1. Quelle ambition et quelle tension expliquent l’offre ?
2. Quels objets composent réellement le portefeuille et comment s’articulent-ils ?
3. Quel travail chaque produit permet-il et comment circule la valeur ?
4. Quelles preuves éclairent adoption, lacunes et maturité ?
5. Comment la stratégie, les moyens et la gouvernance soutiennent-ils le dispositif ?
6. Qu’a-t-on compris, que reste-t-il à instruire ?

Pour Current AI, la tension proposée est le passage d’un écosystème ouvert fragmenté à une expérience intégrée adoptée. Alpha, Router et Gap Map servent à examiner expérience utilisateur, accès aux modèles et orientation des contributions. La dépendance Router–Alpha est explicitée dans le brief ; une causalité automatique entre les trois objets demeure à démontrer. Ces noms appartiennent à la fixture, jamais à la procédure générale.

## Transférer le contexte
Appliquer le [contrat de contexte et de substance](references/business-product-context.md). La procédure commune orchestre la recherche et les analyses ; le profil business ou produit précise les questions. Un parcours combiné traite les deux objets et relie capacités, usages, valeur et moyens. La charte conserve les préférences de lecture confirmées pour ce projet. Les faits, pièces et relations de chaque entreprise demeurent dans le dossier d’entité. L’historique sert à retrouver preuves et corrections.

Une architecture de dossiers légère suffit : sources et claims par entité ; analyses réutilisables ; briefs par run ; sorties et retour humain ; références de méthode. Créer un fichier uniquement si le run l’utilise. Reprise et changement de format conservent le même socle de preuves avec sa date.

## Vérification nécessaire pour conclure à la transférabilité
Comparer main et candidat avec même demande verbatim, même paquet initial, même droit de recherche, même accès aux outils, même charte et même support. Évaluer séparément reconstruction de contexte, recherche, analyse et restitution. Le texte final doit permettre au lecteur d’expliquer le produit et la stratégie, de retracer un usage et de localiser les inconnues. Faire juger au demandeur substance et plaisir de lecture. Rapporter les défauts avant les métriques de coût.

Les 14 tests de contrats du lot précédent ne vérifient pas cette équivalence fonctionnelle. La cible de 40–70 publications approfondit le corpus ; la couverture des questions et l’indépendance des preuves doivent aussi être évaluées.
