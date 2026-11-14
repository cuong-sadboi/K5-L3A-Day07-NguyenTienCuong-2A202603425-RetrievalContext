"""Kiểm tra phiếu chấm tay (src/review.py): chỉ điền sẵn nhãn mà docs quy định cứng."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from review import build

CHUNK = {"id": "B:doc:p1:0-40", "text": "Bot traffic\nchiếm 49,6%.", "page": 1}
QUESTIONS = [{"id": "q1", "expected_answer": "49,6%", "gold": [{"source_id": "doc", "page": 1, "evidence": "49,6%"}]},
             {"id": "q2", "expected_answer": "x", "gold": [{"source_id": "doc", "page": 2, "evidence": "x"}]},
             {"id": "e1", "expected_answer": "y", "gold": [{"source_id": "doc", "page": 3, "evidence": "y"}]}]
CASES = [{"id": "q1", "split": "test", "question": "Bot?", "answerable": True},
         {"id": "q2", "split": "dev", "question": "X?", "answerable": True},
         {"id": "u1", "split": "dev", "question": "VN?", "answerable": False, "absence_reason": "Không có."},
         {"id": "u2", "split": "dev", "question": "Luật?", "answerable": False, "absence_reason": "Không có."},
         {"id": "e1", "split": "dev", "question": "Lỗi?", "answerable": True}]


def trace(qid, status, citations=(), answer=""):
    events = [{"event": "search", "query": "q", "results": [CHUNK], "context_ids": [CHUNK["id"]]}]
    return {"query_id": qid, "status": status, "answer": answer, "citations": list(citations),
            "events": events, "final_context_ids": [CHUNK["id"]], "error": "ConnectionError" if status == "error" else None}


class ReviewTests(unittest.TestCase):
    def test_template_prefills_only_fixed_rules(self):
        traces = [trace("q1", "answered", [CHUNK["id"]], "49,6% [B:doc:p1:0-40]"), trace("q2", "abstain"),
                  trace("u1", "abstain"), trace("u2", "answered", [CHUNK["id"]], "Có [B:doc:p1:0-40]"),
                  trace("e1", "error")]
        sheet, template = build(traces, QUESTIONS, CASES, title="T")
        labels = {label["query_id"]: label for label in template}
        self.assertNotIn("e1", labels)
        self.assertEqual((labels["q1"]["answer_grade"], labels["q1"]["citation_support"], labels["q1"]["context_score"]),
                         (None, [None], None))
        self.assertEqual(labels["q2"]["answer_grade"], 0)
        self.assertIsNone(labels["u1"]["abstention_correct"])
        self.assertIs(labels["u2"]["abstention_correct"], False)
        self.assertIn("Bot traffic chiếm 49,6%.", sheet)
        self.assertIn("Lỗi: ConnectionError", sheet)


if __name__ == "__main__":
    unittest.main()
