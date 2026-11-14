"""Kiểm tra adapter Day 6 -> Day 7 (src/prepare_data.py); dữ liệu nhỏ, không cần vector store."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "starter"))
from baseline import hit, validate
from prepare_data import build, locate_evidence


def row(chunk_id, page, content, chapter=1):
    return {"chunk_id": chunk_id, "document_id": "doc", "source": "doc.pdf", "page": page, "chapter": chapter,
            "section": "1.1", "section_title": "Mục", "char_start": 0, "char_end": len(content),
            "content": content, "content_hash": "h", "doc_sha256": "v1", "metadata": {}, "model": "m"}


DAY6_QUESTION = {"id": "q1", "split": "dev", "type": "truc_tiep", "question": "Bot chiếm bao nhiêu?",
                 "expected_answer": "49,6%", "gold_source_id": "doc", "gold_page": 1,
                 "evidence_quote": "bot traffic chiếm 49,6% tổng lưu lượng",
                 "alt_gold": [{"source_id": "doc", "page": 2, "evidence_quote": "lưu lượng trực tuyến"}],
                 "filter": None}
UNANSWERABLE = {"id": "q2", "split": "dev", "question": "Tỷ lệ ở Việt Nam?", "answerable": False,
                "expected_behavior": "search_and_abstain", "absence_reason": "Không có số liệu riêng."}


class LocateEvidenceTests(unittest.TestCase):
    def test_returns_exact_span_across_newline_hyphen_and_case(self):
        text = "Hiện nay Bot\ntraffic chiếm 49,6% tổng\nlưu lượng; trực-\ntuyến"
        self.assertEqual(locate_evidence(text, "bot traffic chiếm 49,6% tổng lưu lượng"),
                         "Bot\ntraffic chiếm 49,6% tổng\nlưu lượng")
        self.assertEqual(locate_evidence(text, "trực tuyến"), "trực-\ntuyến")
        self.assertIsNone(locate_evidence(text, "50%"))
        self.assertIsNone(locate_evidence(text, "   "))


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.rows = [row("c1", 1, "Theo Imperva, bot\ntraffic chiếm 49,6% tổng lưu lượng Internet."),
                     row("c2", 2, "Mọi lưu lượng trực\ntuyến đều được ghi log.", chapter=None)]

    def test_schema_alt_gold_cases_and_starter_validation(self):
        result = build(self.rows, [DAY6_QUESTION], [UNANSWERABLE], "B")
        chunk = result["chunks"][0]
        self.assertEqual(set(chunk), {"id", "text", "source_id", "source", "page", "metadata"})
        self.assertEqual(chunk["metadata"]["index"], "B")
        self.assertNotIn("chapter", result["chunks"][1]["metadata"])
        question = result["questions"][0]
        self.assertEqual(len(question["gold"]), 2)
        self.assertNotIn("filter", question)
        self.assertTrue(hit(chunk, question["gold"]))
        validate(result["chunks"], result["questions"])
        cases = {c["id"]: c for c in result["cases"]}
        self.assertTrue(cases["q1"]["answerable"])
        self.assertNotIn("gold", cases["q1"])
        self.assertNotIn("expected_answer", cases["q1"])
        self.assertFalse(cases["q2"]["answerable"])
        self.assertEqual(cases["q2"]["expected_behavior"], "search_and_abstain")
        self.assertEqual(result["report"]["summary"]["counts"]["dev"], {"answerable": 1, "unanswerable": 1})
        self.assertFalse(result["report"]["summary"]["meets_minimum_README_md_18"])

    def test_evidence_must_be_on_gold_page(self):
        wrong_page = {**DAY6_QUESTION, "gold_page": 2, "alt_gold": []}
        with self.assertRaises(ValueError):
            build(self.rows, [wrong_page], [], "B")

    def test_unanswerable_schema_and_unique_ids(self):
        with self.assertRaises(ValueError):
            build(self.rows, [], [{k: v for k, v in UNANSWERABLE.items() if k != "absence_reason"}], "B")
        with self.assertRaises(ValueError):
            build(self.rows, [], [{**UNANSWERABLE, "gold": []}], "B")
        with self.assertRaises(ValueError):
            build(self.rows, [DAY6_QUESTION], [{**UNANSWERABLE, "id": "q1"}], "B")


if __name__ == "__main__":
    unittest.main()
