# Comment garder le catalogue disponible pendant une panne du fournisseur ?

Cas synthétique.

## boundary

Le référentiel interne reste maître de l’identité des articles. [C1]

## flow

Proposition : importer chaque export dans une copie de lecture, vérifier son intégrité puis basculer la lecture. [C2]

## failure

Si la vérification échoue, conserver la dernière copie valide et informer le responsable catalogue. Proposition.

## alternative

Une lecture à la demande réduit le délai de mise à jour si une interface synchrone existe. Son existence reste à établir.

## countertest

Mesurer sur un pilote l’âge maximal accepté par les utilisateurs. Si cet âge est inférieur au cycle quotidien, rouvrir la décision. [C3]
