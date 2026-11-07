# Deux bootstraps de rédaction, un dispositif commun de composition

Audit source ciblé du 7 novembre 2026. Donneur : `achard-arnaud/tourisme-etude-historico-geographique`, commit **fb83e0e759d1fef78bbb2cca766fecbb23eda8d5**. Cible : module expérimental `diagnostic-complet/writing.py`. Cette passe livre les préparations et règles de conservation exécutables ; elle n'installe pas un générateur de prose ni un évaluateur sémantique automatique.

## Ce que le donneur contient réellement

| Source au commit épinglé | Mécanisme observé | Décision de transfert |
|---|---|---|
| `skills/storytelling-historical-travel/SKILL.md`, sections « one composition engine, two bootstraps » et « Shared composition layers » | Topologie lecteur → preuves → matériaux → tronc → revue indépendante/gel → qualification des encarts → placement → continuité | Conserver l'ordre des opérations ; aucune side story ne masque une transition faible du tronc |
| Même fichier, bootstraps `iterative` et `from_scratch` | Même moteur ; entrée fraîche sans ancien reader, entrée itérative avec canonique/journal | Deux fonctions d'entrée, pas deux vérités ni deux méthodes probatoires |
| `scripts/build_drafting_packets.py`, `ReadLedger`, `build_packet`, `build_packets` | Journal des lectures ; preuves et fragments par arc ; variantes de bootstrap ; manifeste contamination | Adapter vers entrées structurées et scope dérivé des IDs ; ne pas hériter de la structure historique ou des longueurs |
| `scripts/build_from_scratch_packets.py` | Wrapper de compatibilité autour du moteur partagé | Ne pas créer de second moteur divergent |
| `skills/editing-historical-travel-output/SKILL.md`, « Form-global storytelling changes » | Relecture complète de la zone sélectionnée, au-delà des seuls ajouts ; conservation des faits ; invalidation de la forme | Flag `form_global` étend aux paragraphes de la section sélectionnée ; l'évidence non touchée reste distincte de l'approbation éditoriale |
| `skills/storytelling-historical-travel/references/paragraph_review_checklist.md` | Revue indépendante liée au hash exact ; retour à false après réécriture ; piliers pertinents seulement | Réécriture invalide les flags de revue et produit une nouvelle empreinte ; le module n'auto-approuve rien |
| `scripts/from_scratch_review_contract.py` | Ledger all-false, référence aux claims et aux HIL, détection d'unités manquantes/périmées | Journal local des changements et règles de hash ; la signature stylistique Sarah n'est pas copiée dans François-Pro |

Liens source : [orchestrateur rédaction](https://github.com/achard-arnaud/tourisme-etude-historico-geographique/blob/fb83e0e759d1fef78bbb2cca766fecbb23eda8d5/skills/storytelling-historical-travel/SKILL.md), [builder partagé](https://github.com/achard-arnaud/tourisme-etude-historico-geographique/blob/fb83e0e759d1fef78bbb2cca766fecbb23eda8d5/scripts/build_drafting_packets.py), [édition](https://github.com/achard-arnaud/tourisme-etude-historico-geographique/blob/fb83e0e759d1fef78bbb2cca766fecbb23eda8d5/skills/editing-historical-travel-output/SKILL.md), [revue](https://github.com/achard-arnaud/tourisme-etude-historico-geographique/blob/fb83e0e759d1fef78bbb2cca766fecbb23eda8d5/skills/storytelling-historical-travel/references/paragraph_review_checklist.md).

## Relecture critique du donneur

Le principe est solide mais tout son code ne doit pas être importé tel quel.

- `_iterative_bootstrap` choisit `report_v3_full.md`, puis `report.md`, alors que l'orchestrateur demande de résoudre le canonique depuis un état explicite. La cible reçoit une étude explicitement sélectionnée ; elle ne devine aucun canonique depuis un nom de fichier.
- `build_packet` injecte le bootstrap canonique dans chaque paquet d'arc. La déduplication des chemins dans le read ledger ne mesure pas les copies du texte dans ces paquets. La cible délimite d'abord une closure d'IDs ; le module contexte demeure responsable du paquet physique et de son budget. Aucun gain de tokens n'est revendiqué sans mesure.
- Le garde-fou from-scratch du donneur repose notamment sur des chemins/suffixes. Il ne constitue pas une preuve sémantique qu'un texte renommé n'est jamais une ancienne prose. La cible exige une entrée **evidence-only**, refuse les conteneurs de prose et les types de source explicitement reader/canonical, et accepte seulement une topologie lecteur sans paragraphes.
- Certaines lectures de captures/intakes du donneur attrapent largement les exceptions et poursuivent. Cette tolérance ne prouve pas la complétude du corpus. La cible refuse les dépendances non résolues dans le plan itératif.
- Le mode source dit from-scratch interdit l'ancien reader mais accepte de la dette legacy explicitement typée. La cible n'active pas de bypass legacy ; les claims fournis gardent leur statut, sans promotion.

Ces différences sont des adaptations locales du sous-projet. Elles ne constituent pas une correction ou une certification du dépôt donneur.

## WF 1 — Repartir des preuves, sans ancien reader

API : `prepare_from_scratch(evidence, reader_scaffold=None)`.

1. Fournir un objet evidence-only : identité, mandat, piliers, sources, fragments, claims, relations. Une étude complète contenant `sections` ou `side_stories` est refusée.
2. Si un scaffold lecteur a été choisi explicitement, fournir seulement l'ordre, les titres, les IDs de claims et de piliers. Les paragraphes et champs non prévus sont refusés.
3. Préserver les sources, fragments, statuts et IDs de preuve sans les requalifier.
4. Produire les sections de scaffold avec paragraphes vides. Sans topologie fournie, créer une seule section candidate cadrée par la question du mandat ; ni huit chapitres ni classement alphabétique des preuves ne sont imposés.
5. Émettre le receipt `reader_prose_loaded=false` et l'état `scaffold_candidate_not_drafted`. Ce receipt porte sur les entrées acceptées ; un fichier mal étiqueté sémantiquement ne peut pas être détecté par le script.
6. La rédaction externe utilise les fragments/source comme matériaux, les claims comme contrôle, puis soumet le tronc à une revue indépendante. Ce module ne rédige pas de faits.
7. Après revue et gel du tronc, qualifier les side stories puis vérifier leurs retours et leur insertion. Les approbations humaines restent des événements explicites.

CLI : `python writing.py from-scratch evidence-only.json prepared.json --scaffold reader-topology.json`.

Le résultat contient `study` (scaffold candidat), `packet` (conditions du bootstrap et ordre de travail) et `ledger` (vide tant qu'aucun changement rédigé n'a été appliqué).

## WF 2 — Réviser par delta et dépendances

API : `plan_iterative(study, changed_ids, form_global=False)` puis `apply_iterative(study, changed_ids, replacements=None, form_global=False, expected_baseline_hash=...)`. Le dernier argument est obligatoire et nommé.

1. Désigner l'étude et les IDs modifiés. Le plan enregistre ID, version déclarée (ou inconnue), hash de contenu canonisé et état d'approbation déclaré ; revues factuelles et éditoriales sont comptées séparément, sans les transformer en accord humain. Avant application, comparer obligatoirement le hash de baseline attendu au contenu courant ; refuser une baseline périmée. Refuser aussi un ID inconnu, une identité dupliquée ou une référence de dépendance non résolue.
2. Calculer les impacts source → fragment → claim ; activer les relations pertinentes selon leur orientation. `depends_on` est orienté dépendant → dépendance ; supports/illustrates/contextualizes/causal_hypothesis vont de la proposition d'appui vers sa cible ; contradictions et comparaisons sont conservativement relues dans les deux sens.
3. Repérer les paragraphes utilisant les claims affectés et les encarts attachés aux claims/paragraphes concernés. Une section touchée ne déclenche pas automatiquement la réécriture de tous ses autres paragraphes.
4. En cas de `form_global`, élargir la revue éditoriale à tous les paragraphes des sections ciblées. La clôture de contexte doit alors charger ce span complet et ses seules transitions adjacentes utiles.
5. Accepter exclusivement des remplacements de prose non vide pour les paragraphes/encarts dans ce périmètre. Préserver exactement IDs, texte et métadonnées hors delta. Les sources, fragments, claims, relations et leurs statuts ne sont jamais modifiés par l'application de prose.
6. Pour un texte changé, remettre les approbations evidence/editorial à false et lier le nouvel état au SHA-256 exact du texte. Une revue périmée ou sans hash dans le scope est invalidée. Une dépendance probatoire changée invalide evidence ; un changement global de forme invalide editorial sans effacer une approbation factuelle valide et indépendante.
7. Remettre un encart affecté à l'état candidate lorsque sa prose, sa preuve ou son placement est à revoir. Le texte antérieur reste conservé tant qu'aucun remplacement n'est fourni.
8. Ajouter les changements au `writing_ledger`, en conservant les entrées précédentes, les hashes avant/après, les raisons et la revue antérieure. Les champs `human_approval=false` signalent que l'opération mécanique n'est pas une approbation.

CLI : `python writing.py iterative study.json revised.json --changed C-001 --replacements replacements.json --expected-baseline-hash <hash-du-plan>` ; option `--form-global` si la règle de forme s'applique à toute la zone. `study_hash(study)` calcule la même empreinte sans choisir de fichier canonique automatiquement.

Le résultat contient `study` révisée, `plan` de clôture et `ledger` des seuls changements de cette opération. La sortie wrapper n'est pas directement une étude : utiliser sa clé `study` pour le renderer ou la prochaine révision.

## Garanties, frontières et validations

Le module est stdlib, local et déterministe. Il ne fait aucun appel réseau, génération LLM, vérification de fait, promotion de claim ou approbation humaine. Il ne remplace ni le graphe probatoire complet, ni un jugement de style, ni la lecture sémantique de conservation.

Tests ciblés : `python -m unittest discover -s diagnostic-complet/tests -p test_writing.py -v` depuis la racine du dépôt. Les fixtures exercent refus de l'ancienne prose, scaffold indépendant, ordre éditorial explicite, closure orientée, conservation hors delta, état de revue lié au hash, revue globale bornée, retour d'encart, référence fantôme et ledger append-only.

Les matériaux d'entrée peuvent être fournis ou hypothétiques ; leur réemploi dans un workflow de rédaction ne les rend pas vérifiés. Les piliers corporate et industrie, ainsi que data et IA, restent distincts et ne deviennent pas des quotas de rédaction.
