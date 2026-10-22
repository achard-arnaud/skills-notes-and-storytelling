# React Workbench — prototype de démonstration uniquement

Ce prototype est **statique/client-side** : ne stocke aucun secret, ne lance pas la recherche, ne lit ni GitHub ni Obsidian, ne génère pas de Word/PDF/HTML/MD. Les boutons export sont désactivés pour ne pas faire passer une maquette pour un backend. Le bouton `Enregistrer overlay JSON` sauvegarde **une demande de démonstration**, pas un `RunOverlay` valide : les versions/SHA sont fictifs et le vrai validateurs devra les lier au manifest et au ToC versionné.

## Utilisation

```sh
npm install
npm run dev
npm run build
```

Dépendances proposées React 19 / Vite 6 / TypeScript 5 ; versions à geler via un lockfile au sprint de développement. Pas de build exécuté dans ce design sprint faute de dépendances installées.

## Ce que le prototype démontre

Sélection entreprise/produit/couple, liste de neuf templates illustrative, filtre business/product/technical, ToC consultable et réordonnable clavier, étoiles de profondeur, overlay sérialisé, état des fonctionnalités réellement absentes. Les listes de sections et certaines dimensions servent seulement à préfigurer l'UX et **ne sont pas des adaptations approuvées** du manifest `templates/manifest.json`. Aucun mouvement interdit par les contrats réels n'est encore vérifié; l'orchestrateur devra refuser les ordres incohérents.

Voir [spécification UX](../../docs/workbench-proposal/02-REACT-UX.md), [architecture](../../docs/workbench-proposal/01-ARCHITECTURE.md), [contrat proposé](../../contracts/workbench-run-overlay-v0.schema.json).
