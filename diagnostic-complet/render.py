#!/usr/bin/env python3
"""Render a study as a local, self-contained reader; never promote its evidence."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
from urllib.parse import urlsplit
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sidestories  # noqa: E402


LABELS = {
    "supplied_claim": "Assertion fournie — à vérifier",
    "attributed_claim": "Assertion attribuée",
    "inference": "Inférence",
    "hypothesis": "Hypothèse",
    "verified_fact": "Fait déclaré vérifié — voir la preuve de revue",
    "unknown": "Inconnu",
}


def esc(value: object) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def anchor(value: object) -> str:
    """IDs are opaque to prevent attribute injection and preserve arbitrary input IDs."""
    return "item-" + hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:20]


def _link(value: str, known: set[str], label: str | None = None) -> str:
    if value not in known:
        return f'<span class="gap">Référence non résolue : {esc(label or value)}</span>'
    return f'<a href="#{anchor(value)}">{esc(label or value)}</a>'


def _pillars_attr(record: dict) -> str:
    return esc(json.dumps(record.get("pillar_ids", []), ensure_ascii=False))


def _diagram(value: object) -> str:
    if value is None:
        return ""
    return ('<details class="diagram"><summary>Diagramme Mermaid — source, sans moteur de rendu</summary>'
            f'<pre><code class="language-mermaid">{esc(value)}</code></pre></details>')


def _locator(value: object) -> str:
    text = str(value or "")
    # Never turn javascript:, data:, file:, or malformed URLs into active links.
    try:
        parsed = urlsplit(text)
    except ValueError:
        return f'<code>{esc(text)}</code>'
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return f'<a href="{esc(text)}" rel="noopener noreferrer">{esc(text)}</a>'
    return f'<code>{esc(text)}</code>'


def _tag_chip(kind) -> str:
    """Visible text tag first; color only reinforces it."""
    info = sidestories.tag_for(kind) if isinstance(kind, str) else None
    if not info:
        return ""
    return f'<span class="tag tag-{esc(info["tag"])}" title="{esc(info["label"])}">[{esc(info["tag"])}]</span> '


def render_study(study: dict) -> str:
    """Render supplied state without claiming semantic or human approval."""
    sections = study.get("sections", [])
    pillars = study.get("pillars", [])
    sources = study.get("sources", [])
    fragments = study.get("fragments", [])
    claims = study.get("claims", [])
    stories = study.get("side_stories", [])
    records = sections + pillars + sources + fragments + claims + stories
    records += [p for s in sections for p in s.get("paragraphs", [])]
    ids = [str(r["id"]) for r in records if r.get("id")]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate IDs cannot produce unambiguous reader anchors")
    known = set(ids)
    mandate = study.get("mandate", {})
    title = str(study.get("title") or study.get("id") or "Diagnostic business")
    options = '<option value="">Tous les piliers</option>' + "".join(
        f'<option value="{esc(p["id"])}">{esc(p.get("title", p["id"]))}</option>' for p in pillars
    )
    tabs = [("story", "Récit"), ("pillars", "Piliers"), ("evidence", "Preuves"), ("side-stories", "Side stories")]
    navigation = "".join(
        f'<button type="button" role="tab" id="tab-{key}" aria-controls="panel-{key}" '
        f'aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{label}</button>'
        for i, (key, label) in enumerate(tabs)
    )
    section_index = '<nav aria-label="Plan du récit"><ol>' + "".join(
        f'<li>{_link(s["id"], known, s.get("title", s["id"]))}</li>' for s in sections
    ) + '</ol></nav>'
    narrative = [section_index]
    for section in sections:
        paragraphs = []
        for p in section.get("paragraphs", []):
            review = p.get("review", {})
            state = "Revue déclarée complète" if review.get("evidence") and review.get("editorial") else "Revue incomplète"
            refs = " · ".join(_link(c, known) for c in p.get("claim_ids", []))
            paragraphs.append(f'<div id="{anchor(p["id"])}" class="paragraph filterable" data-pillars="{_pillars_attr(p)}">'
                              f'<p>{esc(p.get("text", ""))}</p><p class="meta">{state} · {refs}</p></div>')
        narrative.append(f'<section id="{anchor(section["id"])}" class="card filterable" data-pillars="{_pillars_attr(section)}">'
                         f'<h2>{esc(section.get("title", section["id"]))}</h2>{"".join(paragraphs)}'
                         f'{_diagram(section.get("mermaid"))}</section>')
    if not sections:
        narrative.append('<p class="gap">Le scaffold lecteur ne comporte pas encore de section.</p>')
    narrative.append(_diagram(study.get("mermaid")))
    pillar_view = ['<p>Axes analytiques candidats : ils éclairent le récit sans imposer son sommaire. '
                   'Leur présence ne constitue pas une validation humaine.</p>']
    for p in pillars:
        linked = [s for s in sections if p["id"] in s.get("pillar_ids", [])]
        links = " · ".join(_link(s["id"], known, s.get("title", s["id"])) for s in linked)
        pillar_view.append(f'<article id="{anchor(p["id"])}" class="card filterable" data-pillars="{esc(json.dumps([p["id"]]))}">'
                           f'<h2>{esc(p.get("title", p["id"]))}</h2><p>{esc(p.get("scope", ""))}</p>'
                           f'<p class="meta">{links or "Aucun passage rattaché pour le moment."}</p></article>')
    evidence = ['<h2>Assertions et hypothèses</h2>']
    for c in claims:
        status = LABELS.get(c.get("status"), "Statut inconnu")
        refs = " · ".join(_link(f, known) for f in c.get("fragment_ids", []))
        verification = c.get("verification", {})
        review_note = f'<p class="meta">Note de revue fournie : {esc(verification.get("note", ""))}</p>' if verification else ""
        evidence.append(f'<article id="{anchor(c["id"])}" class="card filterable" data-pillars="{_pillars_attr(c)}">'
                        f'<h3>{esc(c["id"])}</h3><p class="status">{esc(status)}</p><p>{esc(c.get("text", ""))}</p>'
                        f'<p>{refs or "Aucun fragment rattaché ; preuve à instruire."}</p>{review_note}</article>')
    evidence.append('<h2>Fragments</h2>')
    for f in fragments:
        evidence.append(f'<article id="{anchor(f["id"])}" class="card"><h3>{esc(f["id"])}</h3>'
                        f'<p>{esc(f.get("text", ""))}</p><p>{_link(f.get("source_id", ""), known)} · '
                        f'{esc(f.get("locator", ""))}</p></article>')
    evidence.append('<h2>Sources</h2>')
    for source in sources:
        evidence.append(f'<article id="{anchor(source["id"])}" class="card"><h3>{esc(source.get("title", source["id"]))}</h3>'
                        f'<p>Nature : {esc(source.get("kind", ""))} · Accès déclaré : {esc(source.get("access", "inconnu"))}</p>'
                        f'<p>{_locator(source.get("locator", ""))}</p></article>')
    side_view = ['<p>Encarts candidats ou stabilisés selon leur état déclaré. Le rendu ne les promeut pas.</p>']
    for s in stories:
        refs = " · ".join(_link(c, known) for c in s.get("claim_ids", []))
        return_link = _link(s["return_to"], known, "Retour au récit") if s.get("return_to") else '<span>Sans retour déclaré</span>'
        side_view.append(f'<article id="{anchor(s["id"])}" class="card filterable" data-pillars="{_pillars_attr(s)}">'
                         f'<h2>{esc(s.get("title", s["id"]))}</h2><p class="status">{_tag_chip(s.get("kind"))}{esc(s.get("state", "candidate"))} · {esc(s.get("kind", ""))}</p>'
                         f'<p>{esc(s.get("text", ""))}</p><dl><dt>Raison hors tronc</dt><dd>{esc(s.get("reason_outside", ""))}</dd>'
                         f'<dt>Apport au raisonnement</dt><dd>{esc(s.get("payoff", ""))}</dd></dl><p>{refs}</p><p>{return_link}</p></article>')
    panels = ["".join(narrative), "".join(pillar_view), "".join(evidence), "".join(side_view)]
    panel_html = "".join(f'<main role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}" tabindex="0"{(" hidden" if i else "")}>{panels[i]}</main>' for i, (key, _) in enumerate(tabs))
    return ('<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{CSS}{sidestories.tag_css()}</style></head><body><header>'
            '<p class="eyebrow">Diagnostic complet · espace expérimental</p>'
            f'<h1>{esc(title)}</h1><p>{esc(mandate.get("question", "Question à préciser"))}</p>'
            f'<p class="meta">Périmètre : {esc(mandate.get("scope", "À préciser"))} · Audience : {esc(mandate.get("audience", "À préciser"))}</p>'
            '<p class="notice">Les contenus et statuts ci-dessous sont ceux du dossier fourni. '
            'Cette projection ne vaut ni vérification des faits ni approbation éditoriale humaine.</p></header>'
            f'<nav role="tablist" aria-label="Vues du diagnostic">{navigation}</nav>'
            f'<div class="filter"><label for="pillar-filter">Filtrer par pilier analytique</label> <select id="pillar-filter">{options}</select>'
            '<p id="filter-state" aria-live="polite">Tous les piliers</p></div>'
            '<noscript><p>Le changement d’onglet et le filtre nécessitent JavaScript local. Aucune connexion réseau n’est utilisée.</p></noscript>'
            f'{panel_html}<script>{SCRIPT}</script></body></html>')


CSS = """
:root{font-family:system-ui,sans-serif;color:#17313d;background:#f5f7f8;line-height:1.6}
body{max-width:1080px;margin:auto;padding:24px}header{padding:24px;background:#fff;border-top:5px solid #136c78}
h1{font-size:2rem;line-height:1.2}h2{font-size:1.35rem}.eyebrow{color:#136c78;font-weight:700}
.meta{color:#425965;font-size:.9rem}.notice{border-left:4px solid #b47c18;padding:10px;background:#fff7e7}
[role=tablist]{display:flex;flex-wrap:wrap;gap:6px;margin:22px 0}button,select{font:inherit;padding:10px;border:1px solid #627b85;border-radius:5px;background:white;color:#17313d}
button[aria-selected=true]{background:#173f4c;color:white}button:focus-visible,a:focus-visible,select:focus-visible{outline:3px solid #bd6800;outline-offset:3px}
.filter{margin-bottom:20px}.card{background:white;padding:20px;margin:18px 0;border:1px solid #d1dfe3;border-radius:8px}
.status{font-weight:700;color:#795211}.tag{display:inline-block;padding:0 8px;border-radius:4px;font-weight:700;margin-right:6px}.gap{color:#8b3323}.paragraph p{white-space:pre-wrap}a{color:#075f80;text-underline-offset:3px}
pre{overflow:auto;padding:14px;background:#eaf0f2;white-space:pre-wrap}code{overflow-wrap:anywhere}dt{font-weight:700}dd{margin-left:0;margin-bottom:10px}[hidden]{display:none!important}
@media print{[role=tablist],.filter,noscript{display:none}[role=tabpanel][hidden],.filterable[hidden]{display:block!important}.card{break-inside:avoid}body{padding:0}}
"""


SCRIPT = """
(() => {
  const tabs = Array.from(document.querySelectorAll('[role=tab]'));
  function activate(tab, focus) {
    tabs.forEach(t => {
      const selected = t === tab;
      t.setAttribute('aria-selected', String(selected)); t.tabIndex = selected ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !selected;
    });
    if (focus) tab.focus();
  }
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => activate(tab, false));
    tab.addEventListener('keydown', e => {
      let target;
      if (e.key === 'ArrowRight') target = tabs[(i + 1) % tabs.length];
      if (e.key === 'ArrowLeft') target = tabs[(i + tabs.length - 1) % tabs.length];
      if (e.key === 'Home') target = tabs[0];
      if (e.key === 'End') target = tabs[tabs.length - 1];
      if (target) { e.preventDefault(); activate(target, true); }
    });
  });
  const filter = document.getElementById('pillar-filter');
  function applyFilter() {
    document.querySelectorAll('.filterable').forEach(card => {
      card.hidden = Boolean(filter.value) && !JSON.parse(card.dataset.pillars).includes(filter.value);
    });
    document.getElementById('filter-state').textContent = filter.options[filter.selectedIndex].text;
  }
  filter.addEventListener('change', applyFilter);
  function revealAnchor() {
    const target = document.getElementById(location.hash.slice(1));
    if (!target) return;
    filter.value = ''; applyFilter();
    const panel = target.closest('[role=tabpanel]');
    if (panel) activate(document.getElementById(panel.getAttribute('aria-labelledby')), false);
    target.scrollIntoView();
  }
  window.addEventListener('hashchange', revealAnchor);
  revealAnchor();
})();
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    study = json.loads(args.study.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_study(study), encoding="utf-8")
    print(f"HTML written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
