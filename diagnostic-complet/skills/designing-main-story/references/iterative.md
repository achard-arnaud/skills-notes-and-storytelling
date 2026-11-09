# Mode `iterative` — réviser par delta

Commande : `python3 diagnostic-complet/writing.py iterative study.json revised.json --changed ID [ID ...] [--replacements remplacements.json] [--form-global] --expected-baseline-hash HASH`.

## Principe

Le delta d'abord : seul ce que la dépendance atteint est rouvert. Le reste est conservé octet pour octet, avec ses revues.

## Ordre des opérations

1. **Résoudre la baseline.** L'étude est choisie explicitement ; aucun canonique n'est deviné depuis un nom de fichier. Calculer son empreinte (`study_hash`) et la fournir en `--expected-baseline-hash` : un écart arrête l'opération.
2. **Désigner les IDs modifiés** (source, fragment, claim, paragraphe, encart).
3. **Calculer la clôture.** source, fragment, claim, puis paragraphes et encarts qui les consomment. `depends_on` va du dépendant vers sa dépendance ; supports, illustrates, contextualizes et causal_hypothesis vont de l'appui vers la cible ; contradictions et comparaisons restent des liens de revue.
4. **Appliquer des remplacements de prose** uniquement dans ce périmètre. Hors périmètre : refus.
5. **Invalider les seules revues affectées.** Un texte changé perd ses approbations `evidence` et `editorial` et reçoit le hash de son nouvel état. Une dépendance probatoire changée invalide `evidence` ; une règle de forme globale (`--form-global`) invalide `editorial` sur toute la zone ciblée.
6. **Rouvrir les encarts affectés** : retour à `candidate` quand leur prose, leur preuve ou leur placement est à revoir ; le texte antérieur reste conservé.
7. **Journaliser** : `writing_ledger` en ajout seul, avec hashes avant et après et `human_approval=false`.

## Règles de forme

- Un changement de mise en page ne rouvre pas le sourcing.
- Un claim infirmé rouvre la narration et les rendus qui le consomment.
- Une side story qui dépend d'un claim changé redevient `candidate` ; ses ponts et sa problématique sont à relire avec le nouveau tronc.

## Points de vigilance

- Une dépendance non résolue arrête le plan : ne pas poursuivre en la tolérant.
- La sortie du wrapper n'est pas une étude : utiliser sa clé `study` pour le rendu ou la révision suivante.
- Le module ne vérifie aucun fait et n'approuve rien.
