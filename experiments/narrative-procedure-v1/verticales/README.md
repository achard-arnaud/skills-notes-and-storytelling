# Second essai — quatre verticales, douze couples route–format

Le registre couvre les dix IDs du manifeste racine examiné et le three-pager candidat. Le two-pager dispose de deux fixtures, une produit et une business. La sélection utilise la route et le format. Le registre fournit une interface commune aux quatre manifestes spécialisés.

| Verticale | Couverture | Défaut discriminant et résultat |
|---|---|---|
| [Produit](produit/PROFILE.md) | Two-pager, opportunité ICP, three-pager candidat | Trois micro-essais corrigent respectivement la cadence, la faisabilité côté acheteur et la représentativité d’une extension. |
| [Business](business/PROFILE.md) | Six fixtures structurelles, un cas économique approfondi | Le contrôle détecte un gain fournisseur présenté comme vérifié. La décision corrigée dépend du volume éligible, du gain observé et du seuil économique. |
| [Technique](technique/profile.md) | Architecture et intégration, deux paires de mini-notes | Les témoins incomplets omettent le contre-test ou la posture d’intégration. Le rejeu retrouve les deux éléments en V2. |
| [Pédagogie](pedagogie/PROFILE.md) | Fiche Perception en six pages, révision de Transmettre | V1 et V2 passent le schéma. Seule V2 fournit les pièces, la correction et le réessai. Les cinq autres pages sont préservées. |

## Rejouer

Depuis ce dossier, exécuter `python replay.py --repo /chemin/vers/le/checkout` avec Python et jsonschema. Le checkout doit contenir le commit ca67c1ebe940f5a548b2fd76fc75a8f0f149087c. L’option `--snapshot` accepte aussi un dossier contenant les deux entrées pédagogiques aux chemins enregistrés dans son manifeste. Les trois autres essais utilisent uniquement les fichiers de leur profil. Le script signale un échec si un défaut prévu disparaît du témoin ou persiste dans sa correction. [Reçu consolidé](consolidated-receipt.json).

## Revue finale Skill Creator

1. **Déclencheur.** Une seule skill de composition sélectionne un profil selon l’objectif du lecteur et le format. Le frontmatter du point d’entrée révisé passe quick_validate.py.
2. **Chargement.** Une référence directe dans SKILL.md mène au [registre](registry.json). Chaque entrée donne le manifeste de scaffold, le profil, les fixtures et la commande de contrôle. Le tronc commun reste court.
3. **Responsabilités.** Les quatre dossiers isolés distinguent direction, rédaction, revue et livraison. Les méthodes analytiques interviennent quand une question le nécessite. Les rôles du manifeste peuvent être tenus séquentiellement par une personne ou un agent.
4. **Transfert.** Les comparables et le dossier de la PR sont examinés dans [la revue de sources](HARVEST.md) puis dans les revues propres aux verticales. Les références externes apportent des mécanismes à adapter.
5. **Corrections de consolidation.** Les agents ont employé différentes clés pour le catalogue local. Le registre les relie par des chemins explicites. Il préserve également les deux lectures possibles du two-pager. La couverture complète du catalogue est contrôlée distinctement du nombre de notes effectivement rédigées.
6. **Limite.** Ces essais utilisent des témoins et corrections synthétiques ou contrôlés. Les oracles de structure et de vocabulaire ont une portée étroite. La comparaison de qualité entre générations indépendantes, la validation par les utilisateurs et la pagination physique restent à instruire. Ce cycle ne mesure aucun gain de tokens.

Le prochain test discriminant consiste à donner à chaque profil un brief inédit, à masquer le résultat attendu et à faire lire le document seul à un représentant du public visé.

