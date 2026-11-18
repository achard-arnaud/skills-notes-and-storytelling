# IA en entreprise — fiches pédagogiques

Le pilote **Perception** est repris en profondeur, en six pages A4 paysage. Le contenu canonique est [perception.sheet.json](perception.sheet.json); [perception.md](perception.md) est sa projection de lecture. Les cinq autres modules conservent leur version candidate précédente et seront repris après fermeture de cette boucle.

Le manifeste rend cette frontière exploitable : Perception est le seul module `active_canonical`, avec une sheet paysage et une projection Markdown. Les cinq autres modules sont `legacy_candidate`, sans sheet active ni certification de rendu. Leur Markdown reste une source candidate historique et ne vaut pas compatibilité avec le contrat paysage courant. Le champ `template_source_commit` conserve le pin de la baseline candidate historique ; il ne désigne pas le BUILD actif et ne certifie aucun des cinq modules non migrés.

Le [catalogue](USE_CASE_CATALOG.md) répartit les 70 situations fournies, conserve leurs IDs et conditions, et pointe vers `use-cases.catalog.json`. Les deux pièces jointes identiques ne sont comptées qu’une fois. Une dominante est proposée; une tâche peut garder plusieurs contributions et une alternative sans IA.

Suivre [la skill](../../skills/pedagogical-ai-learning/SKILL.md) et [le contrat actif unique](../../contracts/pedagogical-sheet.schema.json). Structure dans `renderers/pedagogical/landscape.py` et `landscape.html`; design dans `landscape.css`. Les anciens contrats portrait ne sont pas requis pour ce pilote.

```bash
python renderers/pedagogical/landscape.py learning/enterprise-ai/perception.sheet.json --out build/perception
```

Les passages utiles du livre et les sources primaires des histoires ont été lus pour ce tour. Les TOWS, méthodes d’animation, choix de cas et étoiles sont des adaptations pédagogiques. Aucun gain local n’est promis. Le détail des 17 piliers reste absent : l’ancrage niveau 2 est proposé sans numéro inventé. Le statut reste candidat jusqu’à validation pédagogique.
