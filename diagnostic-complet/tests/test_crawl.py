import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import crawl  # noqa: E402

HOST = "www.example.test"


def page(title, body, links=()):
    anchors = "".join(f'<a href="{l}">l</a>' for l in links)
    return (f"<html><head><title>{title}</title><meta name='description' content='desc {title}'></head>"
            f"<body><nav>MENU</nav><main><h1>{title}</h1><p>{body}</p><ul><li>un</li><li>deux</li></ul>{anchors}</main>"
            f"<footer>FOOT</footer><script>var x=1;</script></body></html>").encode()


class FakeSite:
    def __init__(self, pages, robots="User-agent: *\nDisallow:\n", sitemap=None):
        self.pages, self.robots, self.sitemap, self.calls = pages, robots, sitemap or [], []

    def __call__(self, url, timeout=30):
        self.calls.append(url)
        if url.endswith("/robots.txt"):
            return 200, {"Content-Type": "text/plain"}, self.robots.encode(), url
        if url.endswith("sitemap_index.xml"):
            return 200, {}, b"<loc>https://%s/s1.xml</loc>" % HOST.encode(), url
        if url.endswith("/s1.xml"):
            return 200, {}, "".join(f"<loc>{u}</loc>" for u in self.sitemap).encode(), url
        if url in self.pages:
            return 200, {"Content-Type": "text/html"}, self.pages[url], url
        return 404, {}, b"", url


def make(tmp, site, **kw):
    sleeps = []
    c = crawl.Crawler(Path(tmp), HOST, fetch=site, delay=1.0, sleep=sleeps.append, **kw)
    return c, sleeps


class ExtractionTests(unittest.TestCase):
    def test_markdown_keeps_headings_lists_and_drops_boilerplate(self):
        md, title, links = crawl.html_to_markdown(page("Titre", "Corps", ["/a"]).decode(), "https://x/y")
        self.assertIn("# Titre", md)
        self.assertIn("- un", md)
        self.assertIn("Description: desc Titre", md)
        for noise in ("MENU", "FOOT", "var x"):
            self.assertNotIn(noise, md)
        self.assertEqual(title, "Titre")
        self.assertEqual(links, ["/a"])

    def test_normalize_drops_fragment_and_query_and_lowercases_host(self):
        self.assertEqual(crawl.normalize("HTTPS://WWW.Example.TEST//a//b?utm=1#f"), "https://www.example.test/a/b")

    def test_classification(self):
        self.assertEqual(crawl.classify_url("https://other.test/", HOST), "out_of_scope")
        self.assertEqual(crawl.classify_url(f"https://{HOST}/a.png", HOST), "ignored_asset")
        self.assertEqual(crawl.classify_url(f"https://{HOST}/a.pdf", HOST), "non_html")
        self.assertEqual(crawl.classify_url(f"https://{HOST}/a/", HOST), "page")


class CrawlTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def site(self, **kw):
        base = f"https://{HOST}"
        pages = {f"{base}/": page("Accueil", "x", ["/a/", "https://other.test/z", "/doc.pdf", "/img.png"]),
                 f"{base}/a/": page("A", "y", ["/b/"]),
                 f"{base}/b/": page("B", "z")}
        return FakeSite(pages, **kw)

    def test_follows_internal_links_only_and_lists_non_html(self):
        site = self.site()
        c, _ = make(self.tmp.name, site)
        c.load_robots()
        c.add(f"https://{HOST}/", "seed")
        report = c.run()
        self.assertEqual(report["pages_extracted"], 3)
        self.assertEqual(report["non_html_files"], 1)
        self.assertNotIn("https://other.test/z", site.calls)
        self.assertTrue(report["complete"])

    def test_robots_disallow_is_honoured(self):
        site = self.site(robots="User-agent: *\nDisallow: /a/\n")
        c, _ = make(self.tmp.name, site)
        c.load_robots()
        c.add(f"https://{HOST}/", "seed")
        report = c.run()
        self.assertEqual(report["robots_disallowed"], 1)
        self.assertNotIn(f"https://{HOST}/a/", site.calls)

    def test_rate_limit_sleep_after_each_page(self):
        c, sleeps = make(self.tmp.name, self.site())
        c.load_robots()
        c.add(f"https://{HOST}/", "seed")
        c.run()
        self.assertGreaterEqual(len(sleeps), 3)
        self.assertTrue(all(s == 1.0 for s in sleeps))

    def test_errors_are_recorded_not_hidden(self):
        base = f"https://{HOST}"
        site = FakeSite({f"{base}/": page("Accueil", "x", ["/missing/"])})
        c, _ = make(self.tmp.name, site)
        c.load_robots()
        c.add(f"{base}/", "seed")
        report = c.run()
        self.assertEqual(report["errors"], 1)
        self.assertEqual(report["pages_extracted"], 1)

    def test_resume_does_not_refetch_visited_pages(self):
        site = self.site()
        c, _ = make(self.tmp.name, site)
        c.load_robots()
        c.add(f"https://{HOST}/", "seed")
        c.run()
        first = len(site.calls)
        again, _ = make(self.tmp.name, site)
        again.load_robots()
        again.add(f"https://{HOST}/", "seed")
        again.run()
        self.assertEqual(len(site.calls) - first, 1)  # only robots.txt

    def test_sitemap_seeding_marks_origin(self):
        base = f"https://{HOST}"
        site = FakeSite({f"{base}/p1/": page("P1", "x")}, sitemap=[f"{base}/p1/"])
        c, _ = make(self.tmp.name, site)
        c.load_robots()
        c.seed_from_sitemaps(f"{base}/sitemap_index.xml")
        self.assertEqual(c.state["origin"][f"{base}/p1/"], "sitemap:s1.xml")

    def test_refuses_to_write_inside_the_public_repository(self):
        with self.assertRaises(ValueError):
            crawl.Crawler(crawl.PUBLIC_REPO / "diagnostic-complet" / "corpus", HOST)

    def test_extracted_text_is_written_to_markdown_files(self):
        c, _ = make(self.tmp.name, self.site())
        c.load_robots()
        c.add(f"https://{HOST}/a/", "seed")
        c.run()
        md = next((Path(self.tmp.name) / "pages").glob("*.md")).read_text(encoding="utf-8")
        self.assertIn("# A", md)


if __name__ == "__main__":
    unittest.main()
