import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import context


def board():
    return {"id": "demo", "base_sha": "abc", "tasks": [
        {"id": "a", "status": "completed", "depends_on": [], "issue_body": "do not load"},
        {"id": "b", "status": "planned", "depends_on": ["a"], "objective": "read one file"},
        {"id": "c", "status": "planned", "depends_on": ["b"]},
        {"id": "d", "status": "blocked", "depends_on": []}]}


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "one.md").write_text("énergie fiable\n", encoding="utf-8")
        (self.root / "other.md").write_text("Unrelated secret", encoding="utf-8")

    def packet(self, **kwargs):
        return context.build_packet(self.root, board(), "b", ["one.md"], **kwargs)

    def test_ready_respects_status_and_dependencies(self):
        self.assertEqual(context.ready_tasks(board()), ["b"])
        data = board()
        data["tasks"][0]["status"] = "awaiting_human"
        data["tasks"][1]["status"] = "ready"
        self.assertEqual(context.ready_tasks(data), [])

    def test_all_documented_states_accepted(self):
        for state in context.STATUSES:
            data = {"tasks": [{"id": "x", "status": state}]}
            self.assertTrue(context.validate_board(data)["ok"], state)
        self.assertFalse(context.validate_board([])["ok"])
        self.assertFalse(context.validate_board({"tasks": [{"id": "x", "status": []}]})["ok"])

    def test_cycle_unknown_and_duplicate_refused(self):
        data = board()
        data["tasks"][0]["depends_on"] = ["c"]
        self.assertFalse(context.validate_board(data)["ok"])
        data = board()
        data["tasks"][0]["depends_on"] = ["missing"]
        self.assertIn("missing dependency", context.validate_board(data)["errors"][0])
        data = board()
        data["tasks"].append(data["tasks"][0])
        self.assertFalse(context.validate_board(data)["ok"])

    def test_packet_is_bounded_and_does_not_carry_board(self):
        packet = self.packet()
        self.assertEqual(packet["budget"]["input_words"], 2)
        self.assertEqual(packet["budget"]["input_bytes"], len("énergie fiable\n".encode()))
        self.assertIsNone(packet["budget"]["token_count"])
        serialized = json.dumps(packet)
        self.assertNotIn("Unrelated secret", serialized)
        self.assertNotIn("do not load", serialized)
        self.assertEqual([x["path"] for x in packet["inputs"]], ["one.md"])

    def test_packet_carries_scope_acceptance_and_stop_without_claiming_lease(self):
        data = board()
        data["tasks"][1].update(outputs=["out/result.md"], acceptance=["review evidence"],
                                stop_condition="Stop after the review", status="ready")
        packet = context.build_packet(self.root, data, "b", ["one.md"], for_execution=True)
        self.assertEqual(packet["write_scope"], ["out/result.md"])
        self.assertEqual(packet["outputs"], ["out/result.md"])
        self.assertEqual(packet["acceptance"], ["review evidence"])
        self.assertEqual(packet["stop_condition"], "Stop after the review")
        self.assertTrue(packet["execution_ready"])
        self.assertEqual(packet["packet_mode"], "execution")
        self.assertTrue(any("No task lease" in limit for limit in packet["limits"]))
        snapshot = context.checkpoint(self.root, packet)
        self.assertEqual(snapshot["write_scope"], packet["write_scope"])

    def test_planned_packet_is_readable_but_not_executable(self):
        packet = self.packet()
        self.assertFalse(packet["execution_ready"])
        self.assertEqual(packet["packet_mode"], "planning")
        self.assertIn("two unsuccessful repairs", packet["stop_condition"])
        with self.assertRaisesRegex(ValueError, "task state is planned"):
            self.packet(for_execution=True)

    def test_execution_rejects_blocked_or_human_dependencies(self):
        for dep_state in ("blocked", "awaiting_human", "planned", "running"):
            data = board()
            data["tasks"][0]["status"] = dep_state
            data["tasks"][1]["status"] = "ready"
            packet = context.build_packet(self.root, data, "b", ["one.md"])
            self.assertFalse(packet["execution_ready"])
            self.assertTrue(any("dependency a" in item for item in packet["execution_blockers"]))
            with self.assertRaisesRegex(ValueError, "dependency a"):
                context.build_packet(self.root, data, "b", ["one.md"], for_execution=True)

    def test_execution_accepts_satisfied_dependencies_but_not_finished_task(self):
        for dep_state in context.SATISFIED:
            data = board()
            data["tasks"][0]["status"] = dep_state
            data["tasks"][1]["status"] = "ready"
            self.assertTrue(context.build_packet(self.root, data, "b", ["one.md"], for_execution=True)["execution_ready"])
        data["tasks"][1]["status"] = "verified"
        with self.assertRaisesRegex(ValueError, "task state is verified"):
            context.build_packet(self.root, data, "b", ["one.md"], for_execution=True)

    def test_budget_and_empty_input_refused(self):
        with self.assertRaisesRegex(ValueError, "budget exceeded"):
            self.packet(max_words=1)
        with self.assertRaisesRegex(ValueError, "at least one"):
            context.build_packet(self.root, board(), "b", [])

    def test_traversal_absolute_and_missing_refused(self):
        for path in ["../other.md", str(self.root / "one.md"), "absent.md"]:
            with self.assertRaises(ValueError, msg=path):
                context.build_packet(self.root, board(), "b", [path])

    def test_symlink_escape_refused(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "private.md"
            target.write_text("private")
            (self.root / "link.md").symlink_to(target)
            with self.assertRaisesRegex(ValueError, "outside root"):
                context.build_packet(self.root, board(), "b", ["link.md"])

    def test_duplicate_inputs_count_once(self):
        packet = context.build_packet(self.root, board(), "b", ["one.md", "./one.md"])
        self.assertEqual(len(packet["inputs"]), 1)
        self.assertEqual(packet["budget"]["input_words"], 2)

    def test_companion_must_be_explicit_and_counts_when_declared(self):
        (self.root / "instruction.md").write_text("Must read `other.md`.", encoding="utf-8")
        single = context.build_packet(self.root, board(), "b", ["instruction.md"])
        self.assertEqual(len(single["inputs"]), 1)
        self.assertIn("declared_inputs_only", single["context_coverage"])
        both = context.build_packet(self.root, board(), "b", ["instruction.md", "other.md"])
        self.assertEqual(both["budget"]["input_words"], single["budget"]["input_words"] + 2)

    def test_non_utf8_is_not_silently_replaced(self):
        (self.root / "binary.dat").write_bytes(b"\xff\xfe")
        with self.assertRaisesRegex(ValueError, "not UTF-8"):
            context.build_packet(self.root, board(), "b", ["binary.dat"])

    def test_checkpoint_refuses_changed_packet(self):
        packet = self.packet()
        (self.root / "one.md").write_text("changed", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "stale packet"):
            context.checkpoint(self.root, packet)

    def test_resume_detects_stale_missing_and_ref_changed(self):
        snapshot = context.checkpoint(self.root, self.packet(), "c", "Keep hypotheses unverified")
        self.assertTrue(context.validate_checkpoint(self.root, snapshot)["ok"])
        self.assertFalse(context.validate_checkpoint(self.root, snapshot, "different")["ok"])
        (self.root / "one.md").write_text("changed", encoding="utf-8")
        self.assertFalse(context.validate_checkpoint(self.root, snapshot)["ok"])
        (self.root / "one.md").unlink()
        self.assertFalse(context.validate_checkpoint(self.root, snapshot)["ok"])
        resume = context.resume_markdown(snapshot)
        self.assertIn("Prochaine tâche proposée : c", resume)
        self.assertIn("décision humaine", resume)
        self.assertNotIn("énergie fiable", resume)

    def test_invalidation_reopens_only_descendants_without_mutating_board(self):
        original = board()
        original["tasks"][1]["status"] = "verified"
        result = context.invalidate_descendants(original, ["b"])
        self.assertEqual(result["tasks"][1]["status"], "planned")
        self.assertEqual(result["tasks"][2]["invalidated_by"], ["b"])
        self.assertNotIn("invalidated_by", result["tasks"][0])
        self.assertNotIn("invalidated_by", result["tasks"][3])
        self.assertEqual(original["tasks"][1]["status"], "verified")

    def test_cli_packet_checkpoint_resume_and_failure_code(self):
        boardfile = self.root / "board.json"
        boardfile.write_text(json.dumps(board()))
        packetfile = self.root / "packet.json"
        snapshotfile = self.root / "checkpoint.json"
        resumefile = self.root / "RESUME.md"
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(context.main(["board", str(boardfile)]), 0)
            self.assertEqual(context.main(["packet", str(boardfile), "b", "--root", str(self.root),
                                           "--input", "one.md", "--output", str(packetfile)]), 0)
            self.assertEqual(context.main(["packet", str(boardfile), "b", "--root", str(self.root),
                                           "--input", "one.md", "--for-execution"]), 1)
            self.assertEqual(context.main(["checkpoint", str(packetfile), "--root", str(self.root),
                                           "--output", str(snapshotfile), "--resume", str(resumefile)]), 0)
            self.assertEqual(context.main(["resume-check", str(snapshotfile), "--root", str(self.root)]), 0)
            (self.root / "one.md").write_text("changed")
            self.assertEqual(context.main(["resume-check", str(snapshotfile), "--root", str(self.root)]), 1)
        self.assertTrue(resumefile.is_file())


if __name__ == "__main__":
    unittest.main()
