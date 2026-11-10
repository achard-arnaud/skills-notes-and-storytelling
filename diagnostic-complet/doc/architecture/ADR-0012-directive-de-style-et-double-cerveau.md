# ADR-0012 — Directive de style et définition du double cerveau

- **Statut** : accepté
- **Date** : 2026-11-10
- **Décisions liées** : D39 (directive de style), D40 (définition du double cerveau)
- **Tickets** : #291

## Contexte

François a fourni le 2026-11-09 un document de directives de rédaction (niveau direction) et a répondu « oui » le 2026-11-10 à son application. Il a aussi confirmé que le « double cerveau » cité correspond au jumeau numérique décrit comme un cerveau virtuel, et l'a défini : mémoire à long terme, connaissances (base de connaissances, gestion documentaire, wiki, etc.) et cycle de vie des skills.

## Décision

1. **D39 — directive de style.** Registre direct, factuel, analytique et didactique ; structure inductive avec listes, tableaux croisés et diagrammes ; phrases courtes ; jamais d'effet de balancement ni de double négation ; posture orientée décision. Elle vit dans `style_indicative` du workflow des side stories et dans les skills éditoriaux. `sidestories.style_gaps` contrôle les motifs mécaniques et les phrases de plus de 35 mots ; le résultat est une **lacune**, jamais une erreur : le style est un jugement éditorial.
2. **D40 — double cerveau.** La définition de François est ingérée dans la base privée comme source fournie, sans source externe. Elle alimente un candidat d'analyse approfondie. La lecture de l'agent (le « double » comme jumeau de l'organisation, séparé du modèle) reste à valider.

## Conséquences

- Les anciens textes des skills qui renvoyaient à une voix nominative sont remplacés par la directive.
- Le document de directives mentionne un client précis dans son dernier point ; seule la partie générale est reprise dans le dépôt public.
- Aucun contrôle automatique ne remplace la relecture humaine du style.
