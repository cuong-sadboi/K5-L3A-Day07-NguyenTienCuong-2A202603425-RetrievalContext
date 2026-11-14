"""Kiểm tra retriever TF-IDF, hybrid RRF và thứ tự gộp context (src/retrievers.py, src/agent.py)."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "starter"))
from agent import run_agent_ordered
from agentic import run_agent
from retrievers import HybridRetriever, LexicalRetriever


def chunk(cid, text, chapter=1, page=1):
    return {"id": cid, "text": text, "source_id": "doc", "source": "doc.pdf", "page": page,
            "metadata": {"chapter": chapter} if chapter is not None else {}}


CHUNKS = [chunk("a", "Bot traffic chiếm gần một nửa lưu lượng Internet.", 1),
          chunk("b", "Bot traffic trong chương 3 được đo bằng dataset.", 3, 2),
          chunk("c", "Giao diện dashboard hiển thị biểu đồ.", None, 3)]


class Ranked:
    """Retriever giả trả danh sách đã xếp hạng sẵn."""
    name = "fake"

    def __init__(self, ids):
        self.ids = ids

    def search(self, query, *, filters, top_k):
        return [{**c, "rank": r, "score": 1.0} for r, c in
                enumerate([c for i in self.ids for c in CHUNKS if c["id"] == i][:top_k], start=1)]

    def close(self):
        pass


class LexicalTests(unittest.TestCase):
    def test_filter_and_ranks(self):
        retriever = LexicalRetriever(CHUNKS)
        all_hits = retriever.search("bot traffic", filters=None, top_k=3)
        self.assertEqual({c["id"] for c in all_hits}, {"a", "b"})
        self.assertEqual([c["rank"] for c in all_hits], [1, 2])
        only_ch3 = retriever.search("bot traffic", filters={"chapter": 3}, top_k=3)
        self.assertEqual([(c["id"], c["rank"]) for c in only_ch3], [("b", 1)])
        with self.assertRaises(ValueError):
            retriever.search("bot", filters={"year": 2025}, top_k=3)


class HybridTests(unittest.TestCase):
    def test_rrf_fuses_ranks(self):
        hybrid = HybridRetriever(Ranked(["a", "b", "c"]), Ranked(["b", "c"]), candidates=3, k=60)
        results = hybrid.search("q", filters=None, top_k=2)
        # b = 1/62 + 1/61 > c = 1/63 + 1/62 (có ở cả hai danh sách) > a = 1/61 (chỉ có ở danh sách dense)
        self.assertEqual([c["id"] for c in results], ["b", "c"])
        self.assertEqual(results[0]["source_ranks"], {"dense": 2, "lexical": 1})
        self.assertAlmostEqual(results[0]["score"], round(1 / 62 + 1 / 61, 6))


class Scripted:
    """Controller giả: search hai lần rồi trả lời trích dẫn chunk của lượt search thứ hai."""

    def __init__(self):
        self.step = 0

    def decide(self, question, history):
        self.step += 1
        if self.step <= 2:
            return {"action": "search", "query": str(self.step)}
        return {"action": "answer", "answer": "Trả lời [b]", "citations": ["b"]}


class Sequential:
    def __init__(self):
        self.i = 0

    def search(self, query, *, filters, top_k):
        self.i += 1
        return [CHUNKS[0]] if self.i == 1 else [CHUNKS[1]]


class OrderTests(unittest.TestCase):
    BUDGET = 90  # chỉ vừa một chunk kèm tiêu đề

    def test_arrival_matches_starter(self):
        starter = run_agent("q", Scripted(), Sequential(), budget=self.BUDGET)
        ours = run_agent_ordered("q", Scripted(), Sequential(), budget=self.BUDGET, order="arrival")
        self.assertEqual(ours, starter)
        self.assertEqual(ours["status"], "abstain")

    def test_latest_first_keeps_newest_search(self):
        result = run_agent_ordered("q", Scripted(), Sequential(), budget=self.BUDGET, order="latest-first")
        self.assertEqual(result["status"], "answered")
        self.assertEqual(result["events"][1]["context_ids"], ["b"])


if __name__ == "__main__":
    unittest.main()
