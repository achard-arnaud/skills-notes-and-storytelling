#!/usr/bin/env python3
"""Polite, resumable, single-host corporate crawler. Output is a PRIVATE corpus (never the public repo).

Respects robots.txt, identifies itself, rate-limits, stays on one host, checkpoints its frontier and
errors, and writes extracted Markdown plus raw bytes. It extracts text only; it makes no claim about
truth, authorship or completeness beyond the coverage report it writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from html.parser import HTMLParser
from pathlib import Path

PUBLIC_REPO = Path(__file__).resolve().parent.parent
USER_AGENT = "KBResearch/1.0 (private research crawler)"
SKIP_TAGS = {"script", "style", "noscript", "svg", "iframe", "form", "nav", "footer", "header", "template", "head"}
BLOCK_TAGS = {"p", "div", "section", "article", "li", "tr", "br", "blockquote", "ul", "ol", "table", "main"}
HEADINGS = {f"h{i}": "#" * i for i in range(1, 7)}
NON_HTML_EXT = {".pdf", ".docx", ".xlsx", ".pptx", ".zip", ".csv"}
IGNORED_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".css", ".js", ".woff", ".woff2",
               ".ttf", ".mp4", ".mp3", ".xml", ".json", ".rss"}
MAX_BYTES = 15 * 1024 * 1024


class _Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.description, self.links = "", "", []
        self.lines, self._buf, self._skip, self._heading, self._in_title = [], [], 0, None, False

    def _flush(self):
        text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
        self._buf = []
        if text:
            self.lines.append(f"{self._heading} {text}" if self._heading else text)
        self._heading = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "meta" and a.get("name") == "description":
            self.description = a.get("content") or ""
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in SKIP_TAGS:
            self._skip += 1
            return
        if self._skip:
            return
        if tag in HEADINGS:
            self._flush()
            self._heading = HEADINGS[tag]
        elif tag in BLOCK_TAGS:
            self._flush()
            if tag == "li":
                self._buf.append("- ")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in SKIP_TAGS and self._skip:
            self._skip -= 1
            return
        if not self._skip and (tag in HEADINGS or tag in BLOCK_TAGS):
            self._flush()

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if not self._skip:
            self._buf.append(data)

    def close(self):
        super().close()
        self._flush()


def html_to_markdown(html: str, url: str) -> tuple[str, str, list[str]]:
    parser = _Extractor()
    parser.feed(html)
    parser.close()
    title = re.sub(r"\s+", " ", parser.title).strip()
    body = [line for i, line in enumerate(parser.lines) if i == 0 or line != parser.lines[i - 1]]
    head = [f"# {title or url}", f"Source: {url}"]
    if parser.description.strip():
        head.append(f"Description: {parser.description.strip()}")
    blocks, previous = [], None
    for line in head + body:
        if previous is not None:
            blocks.append("\n" if line.startswith("- ") and previous.startswith("- ") else "\n\n")
        blocks.append(line)
        previous = line
    return "".join(blocks) + "\n", title, parser.links


def normalize(url: str, base: str | None = None) -> str:
    absolute = urllib.parse.urljoin(base or "", url.strip())
    parts = urllib.parse.urlsplit(absolute)
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    return urllib.parse.urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def classify_url(url: str, host: str) -> str:
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in {"http", "https"} or parts.netloc != host:
        return "out_of_scope"
    ext = Path(parts.path).suffix.lower()
    if ext in IGNORED_EXT:
        return "ignored_asset"
    if ext in NON_HTML_EXT:
        return "non_html"
    return "page"


def sitemap_urls(xml: str) -> list[str]:
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)


def http_fetch(url: str, timeout: int = 30):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, dict(response.headers), response.read(MAX_BYTES + 1), response.geturl()
    except urllib.error.HTTPError as error:
        return error.code, dict(error.headers or {}), b"", url
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return 0, {"error": str(error)}, b"", url


class Crawler:
    def __init__(self, out: Path, host: str, fetch=http_fetch, delay: float = 1.0, max_pages: int = 2000,
                 sleep=time.sleep, checkpoint_every: int = 10):
        resolved = Path(out).resolve()
        if resolved == PUBLIC_REPO or PUBLIC_REPO in resolved.parents:
            raise ValueError("private corpus must not be written inside the public repository")
        self.out, self.host, self.fetch, self.delay = Path(out), host, fetch, delay
        self.max_pages, self.sleep, self.checkpoint_every = max_pages, sleep, checkpoint_every
        (self.out / "raw").mkdir(parents=True, exist_ok=True)
        (self.out / "pages").mkdir(parents=True, exist_ok=True)
        self.state = {"queue": [], "visited": {}, "errors": [], "skipped": {}, "non_html": {}, "origin": {}}
        self.robots = urllib.robotparser.RobotFileParser()
        self._load_state()

    # --- state -----------------------------------------------------------------
    def _load_state(self):
        path = self.out / "state.json"
        if path.exists():
            self.state = json.loads(path.read_text(encoding="utf-8"))

    def checkpoint(self):
        (self.out / "state.json").write_text(json.dumps(self.state, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                             encoding="utf-8")

    # --- discovery ---------------------------------------------------------------
    def load_robots(self):
        status, _, body, _ = self.fetch(f"https://{self.host}/robots.txt")
        if status == 200:
            self.robots.parse(body.decode("utf-8", "replace").splitlines())
        else:
            self.robots.parse([])
        (self.out / "robots.txt").write_bytes(body if status == 200 else b"")
        return status

    def add(self, url: str, origin: str):
        url = normalize(url)
        kind = classify_url(url, self.host)
        if kind == "out_of_scope" or kind == "ignored_asset":
            self.state["skipped"][kind] = self.state["skipped"].get(kind, 0) + 1
            return
        if kind == "non_html":
            self.state["non_html"].setdefault(url, origin)
            return
        if url in self.state["visited"] or url in self.state["queue"]:
            return
        self.state["queue"].append(url)
        self.state["origin"][url] = origin

    def seed_from_sitemaps(self, index_url: str):
        status, _, body, _ = self.fetch(index_url)
        if status != 200:
            self.state["errors"].append({"url": index_url, "status": status, "stage": "sitemap_index"})
            return
        for child in sitemap_urls(body.decode("utf-8", "replace")):
            self.sleep(self.delay)
            st, _, xml, _ = self.fetch(child)
            if st != 200:
                self.state["errors"].append({"url": child, "status": st, "stage": "sitemap"})
                continue
            name = Path(urllib.parse.urlsplit(child).path).name
            for url in sitemap_urls(xml.decode("utf-8", "replace")):
                self.add(url, "sitemap:" + name)

    # --- crawl -------------------------------------------------------------------
    def fetch_page(self, url: str):
        if not self.robots.can_fetch(USER_AGENT, url):
            self.state["visited"][url] = {"status": "robots_disallowed"}
            return
        status, headers, body, final = self.fetch(url)
        if status == 0 or status >= 400:
            self.state["errors"].append({"url": url, "status": status, "stage": "page"})
            self.state["visited"][url] = {"status": status}
            return
        if classify_url(normalize(final), self.host) == "out_of_scope":
            self.state["visited"][url] = {"status": "redirect_out_of_scope", "final_url": final}
            return
        if len(body) > MAX_BYTES:
            self.state["errors"].append({"url": url, "status": "too_large", "stage": "page"})
            self.state["visited"][url] = {"status": "too_large"}
            return
        ctype = headers.get("Content-Type", headers.get("content-type", ""))
        digest = hashlib.sha256(body).hexdigest()
        if "html" not in ctype.lower() and body[:100].lstrip().lower().find(b"<html") < 0:
            (self.out / "raw" / f"{digest}.bin").write_bytes(body)
            self.state["non_html"][url] = {"content_type": ctype, "sha256": digest}
            self.state["visited"][url] = {"status": "non_html", "sha256": digest}
            return
        (self.out / "raw" / f"{digest}.html").write_bytes(body)
        markdown, title, links = html_to_markdown(body.decode("utf-8", "replace"), final)
        slug = hashlib.sha256(final.encode()).hexdigest()[:16]
        (self.out / "pages" / f"{slug}.md").write_text(markdown, encoding="utf-8")
        self.state["visited"][url] = {"status": status, "final_url": final, "title": title, "sha256": digest,
                                      "md": f"pages/{slug}.md", "bytes": len(body), "words": len(markdown.split())}
        for link in links:
            self.add(urllib.parse.urljoin(final, link), "link:" + url)

    def reextract(self) -> int:
        """Regenerate every page's Markdown from the stored raw HTML, without any request."""
        count = 0
        for url, info in self.state["visited"].items():
            if "md" not in info:
                continue
            raw = self.out / "raw" / f"{info['sha256']}.html"
            if not raw.exists():
                continue
            markdown, _, _ = html_to_markdown(raw.read_bytes().decode("utf-8", "replace"), info["final_url"])
            (self.out / info["md"]).write_text(markdown, encoding="utf-8")
            info["words"] = len(markdown.split())
            count += 1
        self.checkpoint()
        return count

    def run(self):
        done = 0
        while self.state["queue"] and done < self.max_pages:
            url = self.state["queue"].pop(0)
            if url in self.state["visited"]:
                continue
            self.fetch_page(url)
            done += 1
            if done % self.checkpoint_every == 0:
                self.checkpoint()
            self.sleep(self.delay)
        self.checkpoint()
        return self.coverage()

    def coverage(self) -> dict:
        visited = self.state["visited"]
        ok = [v for v in visited.values() if isinstance(v.get("status"), int) and v["status"] < 400]
        from_sitemap = sum(1 for u, o in self.state["origin"].items() if o.startswith("sitemap:"))
        in_sitemap_or_link = {"sitemap": from_sitemap,
                              "link_only": sum(1 for o in self.state["origin"].values() if o.startswith("link:"))}
        report = {"host": self.host, "pages_visited": len(visited), "pages_extracted": len([v for v in ok if "md" in v]),
                  "queue_remaining": len(self.state["queue"]), "errors": len(self.state["errors"]),
                  "robots_disallowed": sum(1 for v in visited.values() if v.get("status") == "robots_disallowed"),
                  "non_html_files": len(self.state["non_html"]), "skipped": self.state["skipped"],
                  "discovered_via": in_sitemap_or_link, "words_total": sum(v.get("words", 0) for v in visited.values()),
                  "complete": not self.state["queue"],
                  "limits": ["Text extraction only ; boilerplate (nav, footer, header, forms) is dropped.",
                             "Coverage is of reachable same-host HTML pages, not of the company's public footprint.",
                             "Non-HTML files are listed, not converted (see R2-09)."]}
        (self.out / "coverage.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--host", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--sitemap", help="sitemap index URL")
    parser.add_argument("--delay", type=float, default=1.0)
    parser.add_argument("--max-pages", type=int, default=2000)
    parser.add_argument("--reextract", action="store_true", help="rebuild Markdown from stored raw HTML; no requests")
    args = parser.parse_args(argv)
    crawler = Crawler(args.out, args.host, delay=args.delay, max_pages=args.max_pages)
    if args.reextract:
        print(json.dumps({"reextracted": crawler.reextract(), "coverage": crawler.coverage()}, ensure_ascii=False, indent=2))
        return 0
    print("robots:", crawler.load_robots())
    if args.sitemap and not crawler.state["queue"] and not crawler.state["visited"]:
        crawler.seed_from_sitemaps(args.sitemap)
        crawler.add(f"https://{args.host}/", "seed")
        crawler.checkpoint()
    print(json.dumps(crawler.run(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
