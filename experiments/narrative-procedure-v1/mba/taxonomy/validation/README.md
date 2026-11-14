# Banc de recalcul synthétique

Exécuter `python replay.py` depuis ce dossier. Les 25 cas enregistrent entrées, résultat attendu, résultat obtenu et verdict dans receipt.json. Les oracles sont fixés à la main. Le banc fonctionne avec Python standard.

| Mesure | Convention testée | Exemple vérifiable |
|---|---|---|
| TCO | Dépense initiale + coûts nominaux sur deux périodes + sortie − valeur résiduelle | 100 + 30 + 40 + 10 − 20 = 160 € |
| ROI | (Bénéfices bruts − coût complet) / coût complet | (200 − 160) / 160 = 25 % |
| VAN et TRI | Flux initial immédiat, flux suivants à la fin de périodes égales | −100 + 55/1,1 + 60,5/1,1² = 0, soit un TRI de 10 % |
| Multiples | MOIC valeur totale / capital investi. EV/EBITDA sur une base cohérente de périmètre et de période | 360/120 = 3× et 900/150 = 6× |
| Payback | Premier retour à l’équilibre, flux uniformes dans la période de récupération, sans actualisation | −100, +40, +80 donnent 1,75 période |
| Seuil de rentabilité | Nombre entier de dossiers, arrondi supérieur du coût fixe / marge unitaire | 121/(13−5) donne 16 dossiers |
| RICE | Reach sur le même trimestre, impact sur échelle commune, confiance en fraction, effort en personnes-mois | 250×2×0,8/4 = 100 |
| TTV | Origine commune d’activation, événement de première valeur défini, durée à l’événement ou à la clôture du suivi. Kaplan–Meier, événements avant censures en cas d’égalité | Quatre entrants, valeur à J2 et J5, censures à J3 et J7. Probabilité de rester sans valeur à J2 = 0,75 puis à J5 = 0,375. Médiane = J5 |
| Adoption | Utilisateurs actifs distincts parmi les utilisateurs éligibles de la même cohorte et fenêtre, critère d’activité défini en amont | Deux utilisateurs actifs distincts parmi quatre donnent 50 % |

Un TRI unique est calculé uniquement pour un investissement conventionnel avec mise initiale négative et flux suivants positifs ou nuls. Les flux −100, +230, −132 admettent 10 % et 20 % ; le banc refuse une valeur unique. Une médiane TTV non atteinte ou un payback hors horizon renvoie une valeur indéterminée. La médiane Kaplan–Meier suppose une censure indépendante et demande un effectif à risque suffisant pour être interprétée. Comparer des scores RICE seulement à définitions et horizons identiques. La cohérence de périmètre, d’unité, de cohorte et la validité des hypothèses réelles restent à vérifier au stade de l’analyse.
