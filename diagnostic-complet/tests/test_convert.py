import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import convert  # noqa: E402

DOCX_XML = ('<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
            '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Titre</w:t></w:r></w:p>'
            '<w:p><w:r><w:t>Un paragraphe.</w:t></w:r></w:p></w:body></w:document>')


def docx_bytes():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml", DOCX_XML)
    return buf.getvalue()


class ConvertTests(unittest.TestCase):
    def test_docx_headings_and_paragraphs(self):
        r = convert.convert_bytes("a.docx", docx_bytes())
        self.assertEqual(r["status"], "ok")
        self.assertIn("# Titre", r["markdown"])
        self.assertIn("Un paragraphe.", r["markdown"])

    def test_html_uses_the_shared_extractor(self):
        r = convert.convert_bytes("a.html", b"<html><head><title>T</title></head><body><h2>H</h2><p>x</p></body></html>")
        self.assertIn("## H", r["markdown"])

    def test_pdf_without_converter_is_reported_not_invented(self):
        with mock.patch.dict(sys.modules, {"pypdf": None}):
            r = convert.convert_bytes("a.pdf", b"%PDF-1.4")
        self.assertEqual(r["status"], "converter_unavailable")
        self.assertNotIn("markdown", r)

    def test_corrupt_docx_is_an_error_record_not_a_crash(self):
        r = convert.convert_bytes("bad.docx", b"not a zip")
        self.assertEqual(r["status"], "error")

    def test_unsupported_extension_is_listed(self):
        self.assertEqual(convert.convert_bytes("a.xyz", b"x")["status"], "unsupported")

    def test_zip_traversal_member_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            z = Path(tmp) / "evil.zip"
            with zipfile.ZipFile(z, "w") as arc:
                arc.writestr("../escape.md", "x")
                arc.writestr("ok.md", "# ok\n")
            records = convert.convert_file(z, Path(tmp) / "out")
        statuses = {r["source"].split("!")[1]: r["status"] for r in records}
        self.assertEqual(statuses["../escape.md"], "path_traversal_refused")
        self.assertEqual(statuses["ok.md"], "ok")
        self.assertFalse((Path(tmp) / "escape.md").exists())

    def test_output_name_is_content_addressed_and_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "n.md"
            src.write_text("# t\n", encoding="utf-8")
            a = convert.convert_file(src, Path(tmp) / "o")[0]["markdown_path"]
            b = convert.convert_file(src, Path(tmp) / "o")[0]["markdown_path"]
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
