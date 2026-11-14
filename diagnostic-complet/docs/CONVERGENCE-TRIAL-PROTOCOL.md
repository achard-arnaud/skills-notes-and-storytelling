# Essai de convergence — protocole S3 / #297

Version 1, 14 novembre 2026. Candidat à exécuter sur un dossier réel après les
contrôles de S2 ; ce document ne constitue ni ce dossier ni sa recette.

## Décision et périmètre de preuve

Vérifier qu'une étude riche peut produire une analyse indépendante du récit,
alimenter une synthèse puis un brief, reprendre après la phase 2 et isoler les
descendants d'une correction, sans appauvrir le produit ou inventer une décision.
Le mandat de convergence est #294 ; capacités analytiques #295, consommateur #296,
essai réel #297. Les propriétaires historiques conservent leurs périmètres.

La recette mécanique, la substance analytique, la narration, le rendu réel et
l'acceptation de François ont des verdicts séparés. Un PASS de structure ou un
score agrégé ne compense jamais un mandat erroné ou une conclusion sans preuve.

## État au gel de ce protocole

| Élément | État et limite |
|---|---|
| S1 | A1–A4 livrés : contrat, intention/plan, question/méthode, adoption calculée sur mesures attribuées, plan d'impact |
| S2 | B1 livré : findings sélectionnés, dispositions des claims, liens tardifs, bootstrap writing et plan d'impact des consommateurs |
| Tests | Régression synthétique ; aucune mesure d'adoption réelle ni recette de texte d'entreprise |
| Reprise | Test dans un Python neuf avec `-I`, pièces phase2, demande phase3 et empreintes du moteur ; refus de données ou moteur modifiés |
| Main de référence observé | `2b3de4d4fc23455d21a76fdee8a81b98df66a098` ; à résoudre au démarrage de l'essai, sans déplacer le pin historique |
| Cible fonctionnelle observée | `67864080d1258e6ac32e6cfc52d3412b64af7d7e` après #312 ; le lot C1 ajoute seulement ce protocole et un test |
| Original Current AI | Rendu original non retrouvé selon le handoff ; attentes lecteur disponibles, aucun oracle pixel/texte inventé |
| Delos | Cas réel de régression envisagé ; les deux essais divergents ne sont pas une baseline satisfaisante |
| Cas de réserve | Entité distincte et mandat à figer **avant** sa recherche ; un second exemple de cohorte synthétique ne le remplace pas |

Les SHA du vrai essai seront consignés dans son reçu avant toute génération.
Leurs différences de capacité sont déclarées ; comparer les procédures à entrées
identiques, pas imposer une API absente au main ni lui retirer le droit de recherche.

## Admission du vrai essai

Avant toute recherche/génération comparative, enregistrer :

1. Demande utilisateur verbatim, retours du lecteur, audience, objet, périmètre,
   unités, date et caractère décisionnel ou exploratoire. Retrouver la pièce
   originale si elle est requise ; une reconstruction non validée reste une limite.
2. Deux références Git exactes et état des sources/méthodes/renderer. Préserver les
   flux main-only et les anciens essais ; aucun merge de branche expérimentale entière.
3. Même corpus autorisé, mêmes droits/outils de recherche, même budget déclaré,
   même support de livraison et même question pour les deux variantes. Journaliser
   les écarts d'accès réels, sans les attribuer au modèle ou à l'architecture.
4. Objet Delos précis ou cas substitué explicitement justifié ; réserver un autre
   cas indépendant avant la collecte. Ne pas choisir après les résultats.
5. Oracle de lecture : un lecteur explique public, tâche, parcours, mécanisme,
   composants/intégrations, disponibilité, logique de valeur, preuves et limites.
   Aucune décision de pilote, fonction support ou secteur ne peut être inventé.

Si une condition manque, qualifier l'action affectée et compléter les pièces ou
le protocole ; ne pas lancer une comparaison sous un mandat appauvri. La préparation
mécanique et les fixtures indépendantes restent possibles. Aucun GO routinier ni
nouveau scheduler n'est nécessaire pour ces préparations déjà autorisées.

## Corpus, provenance et couverture

Pour l'approfondissement demandé : 40–70 publications pertinentes, non un quota
rempli par des pages sans apport. Registre par entrée : URL canonique, éditeur,
origine, titre, date de publication si disponible, période observée, consultation,
question couverte, constat précis, périmètre, limite et statut de lecture.
Distinguer pages uniques et origines indépendantes ; regrouper copies, traductions
et reprises d'un communiqué. Préserver les recherches infructueuses et contradictions.
Une liste de 50 URL n'est pas une preuve de 50 publications lues et utiles.

Constituer la couverture par question et par mécanisme : documentation/démonstration,
accès et tarification, clients/partenaires, historique/versions, entreprise/financement,
retours indépendants, alternatives et marché si pertinents. Une source vendeur
soutient une attribution, pas une mesure indépendante. En cas de pénurie, justifier
la couverture atteinte et la recherche effectuée ; ne pas abaisser silencieusement
la question ou déclarer une absence de preuve comme zéro.

Corpus réel, livrables, captures et journaux de RUN restent dans leur destination
privée ; ce dépôt public conserve seulement méthode, protocole et fixtures curatées.

## Parcours et checkpoint phase 2

1. Exécuter séparément recherche/qualification puis analyse sur les deux variantes.
   Chaque méthode activée conserve question, version, entrées, contre-preuves,
   unités/hypothèses, résultats, inconnues et condition d'arrêt.
2. Geler la fin de phase 2 : étude, brief, plan, enveloppe, sorties de méthode,
   catalogue/version, pièces de preuve et manifest des empreintes du moteur. Inclure
   les instructions applicables et dépendances déclarées ; ne pas charger toute la KB.
3. Utiliser `context.build_packet`, `checkpoint`, `resume_markdown` et
   `validate_checkpoint` existants. Conserver les seules pièces et la demande de la
   phase suivante. Une validation du checkpoint ne remplace pas les gates métier.
4. Arrêter le processus/session de travail. Reprendre dans un contexte neuf depuis
   ces pièces et leur code épinglé, sans accès à l'historique du chat comme entrée.
   Comparer empreintes de preuves/enveloppe, lacunes, méthode et résultat préparé.
5. Une pièce absente/modifiée ou un moteur différent refuse la reprise silencieuse.
   Requalifier explicitement REUSE/REFRESH/NEW et ses impacts ; pas de relance aveugle.

Le test `tests/test_convergence_replay.py` démontre seulement ce mécanisme sur la
fixture synthétique d'adoption : nominal et partial, processus neuf, empreintes
identiques, contre-tests source/moteur. Il n'évalue ni une vraie recherche ni le
raisonnement/narration d'un modèle après une nouvelle conversation humaine.

## Correction, synthèse et rendu

Introduire une correction de source matérielle et documenter l'ancien/nouveau
contenu. Sur la baseline, calculer les descendants claims → analyses → sections/
paragraphes par A3/B1. Conserver l'autre branche et les revues indépendantes.
Après correction, l'empreinte globale A1 doit être réconciliée explicitement : le
plan sélectif n'autorise pas une enveloppe périmée. Produire/réexaminer les résultats
affectés, reconstruire la synthèse puis le contexte et appliquer la revue prescrite.
Vérifier dans le résultat **appliqué**, et pas seulement le plan, que les flags et
approbations impactés ne subsistent pas à tort. Ce contrôle reste requis après B1.

La synthèse précède le brief. Chaque finding retenu est consommé ou écarté de façon
traçable ; chaque claim a sa disposition. Les vues produit/business peuvent changer
l'ordre et les titres en conservant les preuves et leurs statuts. Une réduction de
longueur ne doit pas effacer un fait matériel sans disposition explicite.

Rédiger et relire le texte seul, puis le support réellement livré : liens/ancres,
apercus datés légendés, lecture à largeur utile, absence de débordement et ressources
externes inattendues. Utiliser les capacités constatées au SHA, sans promettre un
renderer Mermaid, PDF ou widget absent. Les deux variantes ont le même support.

## Verdicts et condition de sortie

| Dimension | Preuve attendue | Responsable / statut initial |
|---|---|---|
| Technique | Commandes, SHA, empreintes, résultats et refus attendus | Agent, synthétique seulement jusqu'ici |
| Substance | Mécanismes, usages, preuves/contre-preuves, limites, mandat respecté | Revue indépendante, non exécutée sur le cas réel |
| Narration | Tension, enchaînement, compréhension autonome, faits matériels conservés | Revue indépendante, non exécutée sur le cas réel |
| Rendu | Support réel inspecté, liens et aperçus vérifiés | Non exécuté sur le cas réel |
| Reprise/correction | Pièces seules, refus du stale, descendants appliqués et indépendants conservés | Régression mécanique disponible ; essai réel à exécuter |
| Cas de réserve | Autre entité, mandat figé à l'avance, mêmes critères | Non sélectionné/exécuté |
| Acceptation finale | Retour de François distinct des tests/notes mécaniques | Non recueilli |

Reçu final : versions de toutes les entrées, périmètre réellement couvert,
exceptions, résultats défavorables conservés, main/dev/PR et CI exacts, coûts inconnus
étiquetés, propriétaire libéré, action suivante et condition précise. #295/#296/#297
restent ouverts tant que leurs critères et gates respectifs ne sont pas démontrés.
Aucune promotion `main` n'est autorisée par le seul PASS de la fixture ou de C1.
