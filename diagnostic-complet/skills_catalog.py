#!/usr/bin/env python3
"""Twelve atomic operations as data: renders the public catalog and private SKILL.md drafts.

R2 reserves SKILL.md files to the personal environment: `drafts` refuses to write inside this
repository. `lint` checks a drafts directory (structure, existing commands, boundaries).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parent.parent
DIAG = Path(__file__).resolve().parent

SKILLS = [
 {"name": "source-convert", "module": "convert.py",
  "command": "python3 diagnostic-complet/convert.py FICHIERS --out DOSSIER_PRIVÉ",
  "trigger": "importe ces fichiers ; convertis ce PDF, DOCX, HTML ou ZIP en texte",
  "exclude": "la collecte web (corporate-crawl), l'atomisation (kb-ingest), toute édition du contenu",
  "inputs": "fichiers .md .txt .html .docx .pdf .zip", "outputs": "Markdown dans un dossier privé + rapport par statut avec empreintes",
  "steps": ["Lister les fichiers et leurs empreintes.", "Convertir ; lire le rapport par statut.", "Signaler converter_unavailable, no_text_layer, error, unsupported sans les masquer."],
  "forbid": ["inventer du texte pour un PDF sans couche texte", "extraire un ZIP sans garde de chemin ni de taille", "écrire hors du dossier privé"],
  "negative": "ZIP contenant ../escape.md : membre refusé, rien écrit hors du dossier."},
 {"name": "corporate-crawl", "module": "crawl.py",
  "command": "python3 diagnostic-complet/crawl.py --host HÔTE --out DOSSIER_PRIVÉ --sitemap URL_SITEMAP",
  "trigger": "scrape le site corporate ; complète la KB avec le site de l'entreprise",
  "exclude": "la conversion de fichiers, toute collecte hors de l'hôte déclaré, les sites authentifiés",
  "inputs": "un hôte, un sitemap, un dossier privé", "outputs": "pages Markdown, HTML brut, state.json (frontière, erreurs), coverage.json",
  "steps": ["Lire robots.txt ; s'arrêter si l'hôte est refusé.", "Semer depuis les sitemaps, suivre les liens du même hôte, une requête par seconde.", "Relire coverage.json : erreurs, non-HTML listés, file restante."],
  "forbid": ["ignorer robots.txt", "sortir de l'hôte", "écrire dans le dépôt public", "présenter la couverture comme exhaustive"],
  "negative": "Chemin interdit par robots.txt : non collecté et compté dans robots_disallowed."},
 {"name": "kb-ingest", "module": "kb.py",
  "command": "python3 diagnostic-complet/kb.py FICHIERS_MD --out KB_PRIVÉE --source-kind TYPE",
  "trigger": "atomise ces sources ; nourris la KB ; génère les nœuds",
  "exclude": "la conversion de formats (source-convert), la promotion de faits, la rédaction",
  "inputs": "Markdown ou texte extrait", "outputs": "sources, atomes dédupliqués avec occurrences et localisateurs, graphe documentaire",
  "steps": ["Ingérer en incrémental ; relire les compteurs et les erreurs.", "Vérifier que rien n'est inexpliqué (unexplained_non_whitespace_characters = 0).", "Conserver les occurrences répétées : elles portent la provenance."],
  "forbid": ["promouvoir un atome en fait", "fusionner des occurrences distinctes", "écrire sous un Git public sans déclaration explicite"],
  "negative": "Même texte dans deux sources : un atome, deux occurrences, aucune fusion de sources."},
 {"name": "ontology-check", "module": "ontology.py",
  "command": "python3 diagnostic-complet/ontology.py check | diff ancien nouveau | analyze graph.json",
  "trigger": "valide l'ontologie ; compare deux versions du référentiel ; classe ce graphe",
  "exclude": "tout changement de graphe, toute décision de seuil",
  "inputs": "référentiel JSON ou graph.json", "outputs": "validité, diff (breaking, revue humaine requise), classes, violations",
  "steps": ["Valider le référentiel.", "Comparer à la version précédente ; si human_review_required, arrêter avant tout reçu.", "Lire violations, non classés, hors ontologie."],
  "forbid": ["fixer un seuil", "corriger un graphe", "accepter une relation probatoire sans règle"],
  "negative": "Seuil sans decision_ref : référentiel refusé."},
 {"name": "reinforce-kb-loopback", "module": "reinforce.py",
  "command": "python3 diagnostic-complet/reinforce.py graph.json --recent-id ID --output reçu.json",
  "trigger": "revois la KB après cet apport ; reçu de renforcement du graphe",
  "exclude": "le diagnostic d'un run CV (run-loopback), la revue d'un A1 sans incident (challenge-a1-template)",
  "inputs": "graph.json, IDs récents explicites", "outputs": "un reçu : décision, toutes les propositions (sans plafond), déclencheurs, mesures",
  "steps": ["Lancer le reçu.", "Qualifier chaque constat : structurel, sémantique ou hypothèse.", "Poser les questions HIL, sans y répondre."],
  "forbid": ["fusionner, supprimer ou réaffecter un identifiant", "approuver un candidat", "traiter la densité comme un score"],
  "negative": "Aucun ID récent et graphe propre : no_change."},
 {"name": "evidence-import", "module": "runtime.py",
  "command": "python3 diagnostic-complet/runtime.py import|validate|graph",
  "trigger": "importe ces matériaux avec localisateurs ; valide références et statuts",
  "exclude": "l'atomisation en KB documentaire (kb-ingest), toute promotion épistémique",
  "inputs": "Markdown source", "outputs": "fragments localisés, claims importés comme supplied_claim, graphe probatoire",
  "steps": ["Importer avec localisateurs et empreintes.", "Valider références, statuts, liens, revues.", "Projeter le graphe."],
  "forbid": ["marquer un fait vérifié sans qualification déclarée", "déduire une cause"],
  "negative": "Fait vérifié sans revue déclarée : refusé."},
 {"name": "pillar-qualify", "module": "loopback.py",
  "command": "python3 diagnostic-complet/loopback.py graph.json --recent-id ID",
  "trigger": "qualifie ces nouveaux matériaux par pilier ; quels piliers sont touchés",
  "exclude": "la création d'un pilier par seuil, la décision éditoriale (HITL)",
  "inputs": "graph.json, IDs récents", "outputs": "couverture par pilier, matériaux non classés, revue proposée",
  "steps": ["Lire pillar_coverage et les non classés.", "Comparer au mandat ; garder industrie/corporate et data/IA distincts.", "Proposer retenir, réaffecter ou différer."],
  "forbid": ["créer un pilier parce qu'un seuil est franchi", "promouvoir une classification lexicale"],
  "negative": "Association par mots-clés : reste candidate."},
 {"name": "writing-fresh", "module": "writing.py",
  "command": "python3 diagnostic-complet/writing.py from-scratch",
  "trigger": "prépare un plan de rédaction depuis les preuves ; from-scratch",
  "exclude": "la révision d'un texte existant (writing-iterative), la génération de faits",
  "inputs": "scaffold et claims du graphe", "outputs": "topologie et plan sans prose",
  "steps": ["Refuser toute prose antérieure.", "Dériver le scaffold des preuves.", "Séparer tronc et encarts."],
  "forbid": ["rédiger des faits", "accepter une unité sans claim connu"],
  "negative": "Conteneur de prose antérieure fourni : refusé."},
 {"name": "writing-iterative", "module": "writing.py",
  "command": "python3 diagnostic-complet/writing.py iterative",
  "trigger": "révise ce texte à partir d'un delta ; mets à jour sans réécrire le reste",
  "exclude": "une nouvelle rédaction (writing-fresh)",
  "inputs": "baseline identifiée par empreinte, delta de sources", "outputs": "plan de révision, revues invalidées ciblées, journal append-only",
  "steps": ["Résoudre la baseline et son empreinte.", "Calculer la fermeture de dépendances du delta.", "Préserver le hors-delta ; invalider les seules revues affectées."],
  "forbid": ["remplacer hors delta", "ignorer une dépendance non résolue"],
  "negative": "Remplacement hors delta : rejeté."},
 {"name": "context-packet", "module": "context.py",
  "command": "python3 diagnostic-complet/context.py board|packet|checkpoint|resume-check",
  "trigger": "reprends le run ; paquet de contexte de cette tâche ; vérifie la fraîcheur",
  "exclude": "tout contrôle de la fenêtre du modèle (non prétendu)",
  "inputs": "board, tâche, entrées déclarées", "outputs": "paquet borné, checkpoint avec empreintes, refus si périmé",
  "steps": ["Valider le DAG et la tâche prête.", "Charger seulement les entrées déclarées.", "Refuser une entrée périmée."],
  "forbid": ["relire tout le dépôt par défaut", "prétendre purger la fenêtre"],
  "negative": "Entrée modifiée depuis le checkpoint : reprise refusée."},
 {"name": "reader-render", "module": "render.py",
  "command": "python3 diagnostic-complet/render.py ETUDE.json SORTIE.html",
  "trigger": "rends cette étude en HTML lecteur",
  "exclude": "la rédaction automatique, la promotion de preuves",
  "inputs": "étude JSON (récit, piliers, preuves, side stories)", "outputs": "HTML autonome sans ressource externe",
  "steps": ["Rendre.", "Vérifier erreurs JS, débordement à 390 et 1280 px, ressources externes.", "Rappeler que le rendu ne vaut pas validation."],
  "forbid": ["afficher un état humain non validé comme validé", "charger une ressource externe"],
  "negative": "Contenu injecté : échappé."},
 {"name": "graph1-project", "module": "project.py",
  "command": "python3 diagnostic-complet/project.py --graph1 CLONE --frozen-sha SHA --source kb=KB",
  "trigger": "publie la KB dans le namespace business de Graph1",
  "exclude": "toute modification du graphe de formation gelé",
  "inputs": "KB privée, clone Graph1, empreinte du graphe gelé", "outputs": "fichiers sous knowledge/business/, MANIFEST avec empreintes",
  "steps": ["Vérifier l'empreinte du graphe gelé ; refuser sinon.", "Écrire seulement sous le namespace, sans supprimer.", "Revérifier l'empreinte après écriture."],
  "forbid": ["écrire sous canonical/, build/, tests/, scripts/, docs/", "publier sans [skip ci] ni fast-forward", "forcer un push"],
  "negative": "Namespace hors knowledge/business/ : refusé."},
]


def catalog_markdown() -> str:
    lines = ["# Catalogue des douze opérations atomiques", "",
             "Généré par `skills_catalog.py catalog`. Les SKILL.md ne sont pas versionnés ici (mandat R2), sauf `reinforce-kb-loopback` (exception D31, `operational-skills/`) : `drafts` produit les autres hors dépôt, `lint` les contrôle.", "",
             "| # | Opération | Module | Déclencheur (exemples) | Exclut |", "|---|---|---|---|---|"]
    for i, s in enumerate(SKILLS, 1):
        lines.append(f"| {i} | `{s['name']}` | `{s['module']}` | {s['trigger']} | {s['exclude']} |")
    lines += ["", "## Contrat de chaque opération", ""]
    for s in SKILLS:
        lines += [f"### `{s['name']}`", "", f"- Commande : `{s['command']}`", f"- Entrées : {s['inputs']}", f"- Sorties : {s['outputs']}",
                  "- Interdits : " + " ; ".join(s["forbid"]), f"- Contre-exemple testé : {s['negative']}", ""]
    return "\n".join(lines).rstrip("\n") + "\n"


def draft_markdown(s: dict) -> str:
    description = (f"{s['trigger'][0].upper() + s['trigger'][1:]}. Opération atomique sur le module {s['module']}. "
                   f"Exclure {s['exclude']}.")
    steps = "\n".join(f"{i}. {t}" for i, t in enumerate(s["steps"], 1))
    forbid = "\n".join(f"- {t}" for t in s["forbid"])
    return (f"---\nname: {s['name']}\ndescription: {description}\n---\n\n# {s['name']}\n\n"
            f"## Entrées\n\n{s['inputs']}.\n\n## Commande\n\n`{s['command']}`\n\n## Étapes\n\n{steps}\n\n"
            f"## Sorties\n\n{s['outputs']}.\n\n## Interdits\n\n{forbid}\n\n## Contre-exemple\n\n{s['negative']}\n")


def lint(directory: Path) -> list[str]:
    errors = []
    names = {s["name"] for s in SKILLS}
    found = {p.name for p in Path(directory).iterdir() if p.is_dir()}
    for missing in sorted(names - found):
        errors.append(f"{missing}: missing")
    for extra in sorted(found - names):
        errors.append(f"{extra}: not in catalog")
    for name in sorted(names & found):
        path = Path(directory) / name / "SKILL.md"
        if not path.exists():
            errors.append(f"{name}: no SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        meta = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", text)
        if not meta or meta.group(1) != name:
            errors.append(f"{name}: bad frontmatter")
            continue
        if "Exclure" not in meta.group(2) or len(meta.group(2)) > 600:
            errors.append(f"{name}: description needs an exclusion and <=600 chars")
        for section in ("## Entrées", "## Étapes", "## Interdits", "## Contre-exemple"):
            if section not in text:
                errors.append(f"{name}: missing {section}")
        module = re.search(r"diagnostic-complet/(\w+)\.py", text)
        if not module or not (DIAG / f"{module.group(1)}.py").exists():
            errors.append(f"{name}: command does not name an existing module")
        if len(text.splitlines()) > 80:
            errors.append(f"{name}: longer than 80 lines")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("catalog")
    d = sub.add_parser("drafts")
    d.add_argument("--out", required=True, type=Path)
    l = sub.add_parser("lint")
    l.add_argument("directory", type=Path)
    args = parser.parse_args(argv)
    if args.command == "catalog":
        sys.stdout.write(catalog_markdown())
        return 0
    if args.command == "drafts":
        resolved = args.out.resolve()
        if resolved == REPO or REPO in resolved.parents:
            print("refused: SKILL.md files must not be written inside the public repository", file=sys.stderr)
            return 2
        for s in SKILLS:
            target = args.out / s["name"]
            target.mkdir(parents=True, exist_ok=True)
            (target / "SKILL.md").write_text(draft_markdown(s), encoding="utf-8")
        print(json.dumps({"drafts": len(SKILLS), "out": str(args.out)}))
        return 0
    errors = lint(args.directory)
    print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
