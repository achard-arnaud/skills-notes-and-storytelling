# Du résultat analytique au bloc révisé

Choisir la route et le format dans [le registre](verticales/registry.json). Le manifeste de la verticale précise les blocs, le rôle qui en répond et le chemin de la fixture. Pour une question qui exige une analyse externe, conserver son identifiant, ses claims sources, ses limites et les blocs concernés. Un changement de résultat rouvre ces blocs et leur revue éditoriale.

| Route | Contrat | Observation qui rouvre la rédaction |
|---|---|---|
| Produit | [Manifeste produit](verticales/produit/manifest.json) | La capacité d’export chez l’acheteur reste inconnue ou le KPI arrive après la décision du pilote. |
| Business | [Manifeste business](verticales/business/manifest.json) | Le volume éligible ou la provenance du gain unitaire ne permet plus de soutenir la conclusion économique. |
| Technique | [Manifeste technique](verticales/technique/manifest.json) | Le résultat franchit le seuil d’invalidation ou le repli demandé dans le cas reste à éprouver. |
| Pédagogie | [Manifeste pédagogique](verticales/pedagogie/manifest.json) | Le corrigé contredit la règle de décision ou le réessai présente la même pièce sous un autre ID. |

## Paquet de reprise

Pour chaque étape achevée, conserver la version de la source, le couple route–format, le bloc, les références aux claims et analyses, le verdict observé et la prochaine action. À la reprise, vérifier la version des entrées et charger le seul manifeste utile. Une nouvelle preuve peut laisser le plan intact et invalider une seule conclusion. Le rédacteur décide ensuite si la correction de cette conclusion modifie le fil de lecture.

## Portée des essais

Les douze fixtures enregistrées conservent leurs IDs et chemins. Quatre fixtures contiennent aussi un scénario structuré avec deux mutations chacune. Les scénarios sont synthétiques. Le script compare_controls.py exécute les contrôles précédents sur des copies temporaires portant ces mutations puis applique le contrôle spécialisé. Les anciens contrôles ignorent le nouveau champ. Les huit mutations passent leur contrôle initial et déclenchent les huit alertes attendues avec le contrôle étendu. Cette mesure porte sur la couverture de ces décisions structurées. Elle ne mesure ni l’extraction de valeurs depuis la prose ni la qualité d’un texte libre.

Rejeu du corpus historique avec verticales/replay.py et du supplément fonctionnel avec verticales/functional_review.py. La comparaison appariée requiert verticales/compare_controls.py et le snapshot pédagogique épinglé.
