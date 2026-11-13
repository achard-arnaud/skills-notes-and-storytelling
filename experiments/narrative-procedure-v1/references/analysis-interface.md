# Une analyse spécialisée produit un input réutilisable
Appeler une compétence d’analyse seulement pour une question qui change le livrable ; sinon utiliser les résultats disponibles. PESTEL, Porter, VRIO/RIO, SWOT/TOWS, pricing et business model ont des finalités différentes. Clarifier « RIO » si la méthode visée n’est pas identifiable.
Un paquet contient : id, method, method_version, question, scope, as_of, input_claim_refs, findings (statement, status, claim_refs), counterevidence, unknowns et affects_blocks. Le schéma est contracts/analysis-result.schema.json.
Statuts : attributed_claim, inference, hypothesis, recommendation, unknown. Les faits vérifiés suivent le circuit du dépôt ; la skill rédactrice ne les promeut pas.
Pour SWOT→TOWS : conserver les facteurs S/W/O/T sourcés ; une option SO/WO/ST/WT référence ses facteurs et reste une recommandation ou hypothèse. Ne pas présenter une combinaison de facteurs comme une preuve de résultat.
Entrée nouvelle → calculer les blocs dépendants, les marquer à revoir ; préserver le reste. Un pointeur hors scope, une date incohérente ou une référence non résolue est un défaut à corriger, pas un espace à compléter par intuition.
Des dizaines de méthodes ne justifient pas des dizaines d’appels : choisir l’ensemble minimal, expliciter les dépendances et la condition d’arrêt. Les sorties analytiques restent indépendantes du format final.

