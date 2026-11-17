from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/pedagogical-render.yml"
CONTRACT_PATH = "- 'templates/ai-enterprise-learning-six-page.md'"


class PedagogicalCiContractTests(unittest.TestCase):
    def test_active_template_triggers_render_on_pull_request_and_push(self):
        workflow = WORKFLOW.read_text()
        on_block = workflow.split("permissions:", 1)[0]
        pull_request = on_block.split("  pull_request:", 1)[1].split("  push:", 1)[0]
        push = on_block.split("  push:", 1)[1]

        self.assertIn(CONTRACT_PATH, pull_request)
        self.assertIn(CONTRACT_PATH, push)


if __name__ == "__main__":
    unittest.main()
