"""The reinforce-kb-loopback skill is a repository artifact: copies stay identical and every cited path exists (D31)."""
from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

REPO = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO / "diagnostic-complet" / "operational-skills" / "reinforce-kb-loopback"
DEPS = json.loads((SKILL_DIR / "dependencies.json").read_text(encoding="utf-8"))


def _existing(path: str) -> bool:
    return (REPO / path.split("::")[0]).exists()


class ReinforceSkillArtifactTests(unittest.TestCase):
    def test_mirrors_are_byte_identical_to_canonical(self):
        canonical = (REPO / DEPS["canonical"]).read_bytes()
        for mirror in DEPS["mirrors"]:
            self.assertTrue((REPO / mirror).exists(), mirror)
            self.assertEqual((REPO / mirror).read_bytes(), canonical, f"{mirror} drifted from canonical")

    def test_frontmatter_name_matches_folder(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"^---\nname: reinforce-kb-loopback\n")

    def test_every_dependency_path_exists(self):
        missing = []
        for group in DEPS["dependencies"].values():
            missing += [p for p in group if not _existing(p)]
        for case in DEPS["use_cases"]:
            for key in ("reads", "tests", "refusal_basis"):
                for entry in case.get(key, []):
                    # Only entries that name a repository path are checked; prose and placeholders are skipped.
                    if entry.startswith(("diagnostic-complet/", "contracts/")) and "<" not in entry:
                        if not _existing(entry.split(" (")[0]):
                            missing.append(entry)
            if "eval" in case:
                missing += [case["eval"]] if not _existing(case["eval"]) else []
        self.assertEqual(missing, [])

    def test_every_script_the_skill_runs_exists(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        scripts = set(re.findall(r"diagnostic-complet/[\w/.-]+\.py", text))
        self.assertTrue(scripts)
        self.assertEqual([s for s in scripts if not (REPO / s).exists()], [])

    def test_skill_no_longer_caps_proposals(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("au plus trois", text)
        self.assertNotIn("au plus une modification de type", text)

    def test_eval_cases_are_versioned(self):
        cases = sorted(p.name for p in (REPO / "diagnostic-complet/evals/reinforce-kb-loopback").iterdir() if p.is_dir())
        self.assertEqual(len(cases), 6)


if __name__ == "__main__":
    unittest.main()
