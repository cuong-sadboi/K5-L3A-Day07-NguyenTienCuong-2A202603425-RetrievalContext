"""Kiểm tra controller, runner và metric của src/agent.py bằng client/retriever giả (không gọi API thật)."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from agent import (ABSTAIN_TEXT, FALLBACK_BETA, ClaudeController, context_hit, retrieval_eval, run_case,
                   summarize, to_chunk)

MODEL = "claude-opus-5-5"
CHUNK = {"id": "B:doc:p1:0-40", "text": "Bot traffic chiếm 49,6% lưu lượng.", "source_id": "doc",
         "source": "doc.pdf", "page": 1, "metadata": {}, "score": 0.9, "rank": 1}
OTHER = {**CHUNK, "id": "B:doc:p2:0-30", "page": 2, "text": "Giao diện dashboard.", "rank": 1}
GOLD = [{"source_id": "doc", "page": 1, "evidence": "49,6%"}]
SETTINGS = {"name": "T", "max_searches": 2, "top_k": 3, "budget": 800}


def text_reply(text):
    return SimpleNamespace(content=[SimpleNamespace(type="text", text=text)], stop_reason="end_turn", model=MODEL,
                           usage=SimpleNamespace(to_dict=lambda: {"input_tokens": 1, "output_tokens": 10}),
                           _request_id="req_text")


def search_reply(query):
    block = SimpleNamespace(type="tool_use", name="search", input={"query": query}, id="toolu_1")
    return SimpleNamespace(content=[block], stop_reason="tool_use", model=MODEL,
                           usage=SimpleNamespace(to_dict=lambda: {"input_tokens": 1, "output_tokens": 10}),
                           _request_id="req_tool")


class FakeMessages:
    def __init__(self, replies):
        self.replies = iter(replies)
        self.requests = []

    def create(self, **kwargs):
        self.requests.append(kwargs)
        return next(self.replies)


class FakeClient:
    def __init__(self, replies):
        self.messages = FakeMessages(replies)
        self.beta = SimpleNamespace(messages=self.messages)


class FakeRetriever:
    def __init__(self, rows=None, error=None):
        self.rows, self.error, self.calls = rows or [], error, []

    def search(self, query, *, filters, top_k):
        if self.error:
            raise self.error
        self.calls.append((query, filters, top_k))
        return self.rows[:top_k]


class ControllerTests(unittest.TestCase):
    def test_first_turn_offers_search_with_supported_params(self):
        client = FakeClient([search_reply("bot traffic")])
        controller = ClaudeController(client, MODEL, max_searches=2)
        self.assertEqual(controller.decide("Bot chiếm bao nhiêu?", []), {"action": "search", "query": "bot traffic"})
        request = client.messages.requests[0]
        self.assertEqual(request["tools"][0]["name"], "search")
        self.assertEqual(request["tool_choice"], {"type": "auto", "disable_parallel_tool_use": True})
        self.assertEqual(request["output_config"], {"effort": "medium"})
        self.assertEqual((request["betas"], request["fallbacks"]), ([FALLBACK_BETA], "default"))
        self.assertNotIn("temperature", request)
        self.assertIn("Số lần search còn lại: 2", request["messages"][0]["content"])
        self.assertAlmostEqual(controller.calls[0]["output_cost_usd_est"], 10 * 20 / 1_000_000)

    def test_last_turn_without_tools_and_citations_only_chunk_ids(self):
        client = FakeClient([text_reply("Khoảng 49,6% [B:doc:p1:0-40], theo tài liệu tham khảo [17].")])
        controller = ClaudeController(client, MODEL, max_searches=2, fallbacks=False)
        history = [{"tool": "search", "queries": ["a", "b"], "context": "[B:doc:p1:0-40 | doc.pdf | page 1]\nBot",
                    "context_ids": ["B:doc:p1:0-40"]}]
        action = controller.decide("Bot chiếm bao nhiêu?", history)
        self.assertEqual(action["citations"], ["B:doc:p1:0-40"])
        request = client.messages.requests[0]
        self.assertNotIn("tools", request)
        self.assertNotIn("betas", request)
        self.assertIn("<documents>", request["messages"][0]["content"])
        self.assertIn("Đã hết lượt search", request["messages"][0]["content"])


class RunCaseTests(unittest.TestCase):
    def case(self, cid="q1"):
        return {"id": cid, "split": "dev", "question": "Bot chiếm bao nhiêu?", "filter": {"chapter": 1}}

    def test_answered_trace_has_fields_and_context_hit(self):
        controller = ClaudeController(FakeClient([search_reply("bot"), text_reply("49,6% [B:doc:p1:0-40]")]),
                                      MODEL, max_searches=2)
        retriever = FakeRetriever([CHUNK])
        trace = run_case(self.case(), controller, retriever, SETTINGS)
        self.assertEqual(trace["status"], "answered")
        self.assertEqual((trace["n_searches"], trace["n_llm_calls"], trace["output_tokens"]), (1, 2, 20))
        self.assertEqual(trace["final_context_ids"], [CHUNK["id"]])
        self.assertEqual(retriever.calls, [("bot", {"chapter": 1}, 3)])
        self.assertTrue(context_hit(trace, GOLD))

    def test_abstain_error_and_summary(self):
        abstain = run_case(self.case("q2"), ClaudeController(FakeClient([search_reply("x"), text_reply(ABSTAIN_TEXT)]),
                                                            MODEL, max_searches=2), FakeRetriever([OTHER]), SETTINGS)
        self.assertEqual(abstain["status"], "abstain")
        error = run_case(self.case("q3"), ClaudeController(FakeClient([search_reply("x")]), MODEL, max_searches=2),
                         FakeRetriever(error=ConnectionError("database unavailable")), SETTINGS)
        self.assertEqual(error["status"], "error")
        self.assertIn("ConnectionError", error["error"])
        summary = summarize([abstain, error], {"q2": GOLD, "q3": GOLD})
        self.assertEqual(summary["errors"], ["q3"])
        self.assertEqual(summary["tool_use"], {"n": 1, "N": 1})
        self.assertEqual(summary["context_evidence"], {"n": 0, "N": 2})


class RetrievalTests(unittest.TestCase):
    def test_hit_ranks_and_mrr(self):
        question = {"id": "q1", "question": "Bot?", "gold": GOLD}
        result = retrieval_eval(FakeRetriever([OTHER, CHUNK]), [question], top_k=3, budget=800)
        self.assertEqual(result["rows"][0]["first_hit_rank"], 2)
        self.assertEqual((result["summary"]["hit1"], result["summary"]["hit3"], result["summary"]["mrr"]), (0, 1, 0.5))

    def test_day6_row_mapping(self):
        row = {"rank": 1, "score": 0.8, "chunk_id": "B:doc:p1:0-40", "document_id": "doc", "source": "doc.pdf",
               "page": 1, "chapter": None, "section": "1.1", "section_title": "Mục", "char_start": 0,
               "char_end": 40, "text": "abc", "metadata": {}}
        chunk = to_chunk(row, "dense-C")
        self.assertEqual((chunk["id"], chunk["source_id"], chunk["method"]), ("B:doc:p1:0-40", "doc", "dense-C"))
        self.assertNotIn("chapter", chunk["metadata"])


if __name__ == "__main__":
    unittest.main()
