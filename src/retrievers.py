"""Hai phương pháp retrieval thêm cho Day 7 (GUIDE.md:15–22); chỉ dùng thư viện chuẩn.

- LexicalRetriever: TF-IDF của starter (`baseline.TfidfIndex`) trên đúng corpus đã export từ vector store Day 6
  (`starter/data/converted/chunks.json`, index B), nên cùng corpus và phiên bản index với dense.
- HybridRetriever: gộp dense và lexical bằng Reciprocal Rank Fusion (RRF), chỉ dùng thứ hạng nên không cần
  chuẩn hóa điểm của hai retriever (GUIDE.md:22).

Cả hai áp dụng cùng filter do người dùng nêu (vd. {"chapter": 1}) như dense chiến lược C, để các phương pháp
chỉ khác nhau ở cách tìm và xếp hạng.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "starter") not in sys.path:
    sys.path.insert(0, str(ROOT / "starter"))
from baseline import TfidfIndex  # noqa: E402

# Khóa filter giống store.FILTER_COLUMNS của Day 6; document_id nằm ở trường source_id của chunk.
FILTER_FIELDS = {"chapter": ("metadata", "chapter"), "section": ("metadata", "section"),
                 "document_id": ("chunk", "source_id")}


def matches(chunk: dict[str, Any], filters: dict[str, Any] | None) -> bool:
    for key, value in (filters or {}).items():
        if key not in FILTER_FIELDS:
            raise ValueError(f"Filter {key!r} không được hỗ trợ; chỉ dùng: {', '.join(sorted(FILTER_FIELDS))}")
        place, field = FILTER_FIELDS[key]
        actual = chunk["metadata"].get(field) if place == "metadata" else chunk.get(field)
        if actual != value:
            return False
    return True


class LexicalRetriever:
    """TF-IDF của starter (tách từ theo `\\w+`, không dùng tách từ tiếng Việt), lọc theo filter rồi lấy top-k."""

    def __init__(self, chunks: list[dict[str, Any]]) -> None:
        self.index = TfidfIndex(chunks)
        self.name = "tfidf"
        self.calls: list[dict[str, Any]] = []

    def search(self, query: str, *, filters: dict[str, Any] | None, top_k: int) -> list[dict[str, Any]]:
        started = time.perf_counter()
        scored = [c for c in self.index.search(query, top_k=len(self.index.chunks)) if matches(c, filters)]
        results = [{**c, "score": round(c["score"], 6), "rank": rank, "method": self.name}
                   for rank, c in enumerate(scored[:top_k], start=1)]
        self.calls.append({"query": query, "applied_filter": filters or None, "n": len(results),
                           "latency_ms": round((time.perf_counter() - started) * 1000, 1)})
        return results

    def close(self) -> None:
        pass


class HybridRetriever:
    """RRF: điểm = Σ 1 / (k + thứ hạng) trên các danh sách dense và lexical, mỗi danh sách lấy `candidates` chunk."""

    def __init__(self, dense: Any, lexical: Any, *, candidates: int = 20, k: int = 60) -> None:
        self.dense, self.lexical = dense, lexical
        self.candidates, self.k = candidates, k
        self.name = f"hybrid-rrf({getattr(dense, 'name', 'dense')}+{getattr(lexical, 'name', 'lexical')})"
        self.calls: list[dict[str, Any]] = []

    def search(self, query: str, *, filters: dict[str, Any] | None, top_k: int) -> list[dict[str, Any]]:
        started = time.perf_counter()
        lists = {"dense": self.dense.search(query, filters=filters, top_k=self.candidates),
                 "lexical": self.lexical.search(query, filters=filters, top_k=self.candidates)}
        scores: dict[str, float] = {}
        chunks: dict[str, dict[str, Any]] = {}
        ranks: dict[str, dict[str, int]] = {}
        for source, results in lists.items():
            for chunk in results:
                scores[chunk["id"]] = scores.get(chunk["id"], 0.0) + 1 / (self.k + chunk["rank"])
                chunks.setdefault(chunk["id"], chunk)
                ranks.setdefault(chunk["id"], {})[source] = chunk["rank"]
        ordered = sorted(scores, key=lambda cid: (-scores[cid], cid))[:top_k]
        self.calls.append({"query": query, "applied_filter": filters or None, "n": len(ordered),
                           "candidates": {k: len(v) for k, v in lists.items()},
                           "latency_ms": round((time.perf_counter() - started) * 1000, 1)})
        return [{**chunks[cid], "score": round(scores[cid], 6), "rank": rank, "method": "hybrid-rrf",
                 "source_ranks": ranks[cid]} for rank, cid in enumerate(ordered, start=1)]

    def close(self) -> None:
        for retriever in (self.dense, self.lexical):
            retriever.close()
