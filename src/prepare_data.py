"""Chuyển dữ liệu Day 6 sang định dạng Day 7 (data/README.md); chỉ dùng thư viện chuẩn.

Đầu vào:
  --chunks          chunk export từ vector store Day 6 (src/day6_link.py), JSON array
  --day6-questions  benchmark Day 6 (benchmark/questions.jsonl, mỗi dòng một câu có đáp án)
  --unanswerable    câu thiếu bằng chứng viết cho Day 7 (data/day7_unanswerable.json)
Đầu ra (--output, mặc định starter/data/converted như starter/README.md):
  chunks.json             id, text, source_id, source, page, metadata
  questions.json          câu có đáp án; mỗi evidence nằm trọn trong một chunk đúng nguồn và trang
  cases.json              mọi câu, có trường answerable, cho starter/agent_metrics.py
  conversion_report.json  đối chiếu evidence Day 6 với đoạn nguyên văn trong chunk

Evidence của Day 6 chép từ văn bản đã gộp dòng, còn chunk giữ ký tự xuống dòng của PDF, nên so khớp
nguyên văn thường trượt. Adapter tìm evidence trong các chunk đúng nguồn/trang khi bỏ qua hoa/thường,
khoảng trắng và gạch nối (cùng quy tắc kiểm chứng của Day 6), rồi ghi đoạn nguyên văn tương ứng trong
chunk làm evidence. Nhờ vậy `hit()` của starter/baseline.py dùng được nguyên định nghĩa so khớp.
"""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HYPHENS = frozenset("-\u00ad\u2010\u2011\u2012\u2013\u2014\u2015\u2212")  # gạch nối, soft hyphen, các loại dash
CHUNK_METADATA_KEYS = ("chapter", "section", "section_title", "char_start", "char_end", "content_hash", "doc_sha256")
UNANSWERABLE_KEYS = ("id", "split", "question", "answerable", "expected_behavior", "absence_reason")
MINIMUM = {"dev": {"answerable": 15, "unanswerable": 2}, "test": {"answerable": 5, "unanswerable": 2}}  # README.md:18


def _normalized(text: str) -> tuple[str, list[int]]:
    """Chuỗi để so khớp (chữ thường, bỏ khoảng trắng và gạch nối) kèm vị trí ký tự gốc của từng ký tự."""
    chars: list[str] = []
    positions: list[int] = []
    for index, char in enumerate(text):
        if char.isspace() or char in HYPHENS:
            continue
        for folded in char.casefold():
            chars.append(folded)
            positions.append(index)
    return "".join(chars), positions


def locate_evidence(text: str, evidence: str) -> str | None:
    """Đoạn nguyên văn trong `text` khớp `evidence` khi bỏ qua hoa/thường, khoảng trắng và gạch nối."""
    evidence = unicodedata.normalize("NFC", evidence)
    if evidence and evidence in text:
        return evidence
    haystack, positions = _normalized(text)
    needle, _ = _normalized(evidence)
    start = haystack.find(needle) if needle else -1
    if start < 0:
        return None
    return text[positions[start]: positions[start + len(needle) - 1] + 1]


def convert_chunk(row: dict[str, Any], index: str) -> dict[str, Any]:
    """Một dòng export của vector store Day 6 -> chunk Day 7 (data/README.md:5)."""
    metadata = {key: row[key] for key in CHUNK_METADATA_KEYS if row.get(key) is not None}
    metadata.update(row.get("metadata") or {})
    metadata["index"] = index
    return {"id": row["chunk_id"], "text": row["content"], "source_id": row["document_id"],
            "source": row["source"], "page": row["page"], "metadata": metadata}


def _gold_items(question: dict[str, Any]):
    yield "gold", question["gold_source_id"], question["gold_page"], question["evidence_quote"]
    for alt in question.get("alt_gold") or []:
        yield "alt_gold", alt.get("source_id", question["gold_source_id"]), alt["page"], alt["evidence_quote"]


def convert_answerable(question: dict[str, Any], chunks_by_page: dict) -> tuple[dict[str, Any], dict[str, Any]]:
    """Câu có đáp án Day 6 -> câu Day 7 (data/README.md:6); gold gồm evidence chính và evidence thay thế."""
    gold: list[dict[str, Any]] = []
    entries = []
    for kind, source_id, page, quote in _gold_items(question):
        matches = [(chunk["id"], span) for chunk in chunks_by_page.get((source_id, page), [])
                   if (span := locate_evidence(chunk["text"], quote)) is not None]
        if not matches:
            raise ValueError(f"{question['id']}: không tìm thấy evidence ({kind}) trong chunk nào của "
                             f"{source_id} trang {page}; cần sửa evidence hoặc ghi rõ evidence nằm ở nhiều chunk")
        spans = list(dict.fromkeys(span for _, span in matches))
        gold.extend({"source_id": source_id, "page": page, "evidence": span} for span in spans)
        entries.append({"kind": kind, "page": page, "day6_evidence": quote, "day7_evidence": spans,
                        "chunks": [chunk_id for chunk_id, _ in matches], "exact_in_day6": spans == [quote]})
    converted = {"id": question["id"], "split": question["split"], "question": question["question"],
                 "expected_answer": question["expected_answer"], "gold": gold}
    if question.get("filter"):
        converted["filter"] = question["filter"]
    return converted, {"id": question["id"], "split": question["split"], "evidence": entries}


def check_unanswerable(question: dict[str, Any]) -> None:
    """Câu thiếu bằng chứng phải đúng schema data/README.md:7 và không có gold."""
    missing = [key for key in UNANSWERABLE_KEYS if key not in question]
    if missing:
        raise ValueError(f"{question.get('id')}: câu thiếu bằng chứng thiếu trường {missing}")
    if question["answerable"] is not False or question["expected_behavior"] != "search_and_abstain":
        raise ValueError(f"{question['id']}: cần answerable=false và expected_behavior='search_and_abstain'")
    if question["split"] not in ("dev", "test") or not str(question["absence_reason"]).strip():
        raise ValueError(f"{question['id']}: split hoặc absence_reason không hợp lệ")
    if "gold" in question or "expected_answer" in question:
        raise ValueError(f"{question['id']}: câu thiếu bằng chứng không được có gold hoặc expected_answer")


def to_case(question: dict[str, Any], answerable: bool) -> dict[str, Any]:
    """Case cho agent: không chứa gold hay đáp án chuẩn (data/README.md:9)."""
    case = {"id": question["id"], "split": question["split"], "question": question["question"],
            "answerable": answerable, "expected_behavior": "search_and_answer" if answerable else "search_and_abstain"}
    if question.get("filter"):
        case["filter"] = question["filter"]
    if not answerable:
        case["absence_reason"] = question["absence_reason"]
    return case


def build(raw_chunks: list[dict], day6_questions: list[dict], unanswerable: list[dict], index: str = "B") -> dict:
    chunks = [convert_chunk(row, index) for row in raw_chunks]
    if len({chunk["id"] for chunk in chunks}) != len(chunks):
        raise ValueError("chunk ID trùng")
    chunks_by_page: dict = defaultdict(list)
    for chunk in chunks:
        chunks_by_page[(chunk["source_id"], chunk["page"])].append(chunk)

    questions, cases, evidence_report = [], [], []
    for question in day6_questions:
        converted, entry = convert_answerable(question, chunks_by_page)
        questions.append(converted)
        evidence_report.append(entry)
        cases.append(to_case(converted, True))
    for question in unanswerable:
        check_unanswerable(question)
        cases.append(to_case(question, False))
    if len({case["id"] for case in cases}) != len(cases):
        raise ValueError("ID câu hỏi trùng")

    counts = {split: {"answerable": sum(c["split"] == split and c["answerable"] for c in cases),
                      "unanswerable": sum(c["split"] == split and not c["answerable"] for c in cases)}
              for split in ("dev", "test")}
    entries = [e for item in evidence_report for e in item["evidence"]]
    summary = {"index": index, "chunks": len(chunks), "counts": counts,
               "meets_minimum_README_md_18": all(counts[s][k] >= n for s, need in MINIMUM.items() for k, n in need.items()),
               "evidence_entries": len(entries), "evidence_exact_in_day6": sum(e["exact_in_day6"] for e in entries),
               "questions_with_filter": sum("filter" in q for q in questions)}
    return {"chunks": chunks, "questions": questions, "cases": cases,
            "report": {"summary": summary, "evidence": evidence_report}}


def main(argv: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Chuyển chunk và benchmark Day 6 sang định dạng Day 7")
    parser.add_argument("--chunks", type=Path, required=True)
    parser.add_argument("--day6-questions", type=Path, required=True)
    parser.add_argument("--unanswerable", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "starter" / "data" / "converted")
    parser.add_argument("--index", default="B")
    args = parser.parse_args(argv)

    raw_chunks = json.loads(args.chunks.read_text(encoding="utf-8"))
    day6_questions = [json.loads(line) for line in args.day6_questions.read_text(encoding="utf-8").splitlines()
                      if line.strip()]
    unanswerable = json.loads(args.unanswerable.read_text(encoding="utf-8"))
    result = build(raw_chunks, day6_questions, unanswerable, args.index)

    sys.path.insert(0, str(ROOT / "starter"))
    from baseline import validate  # kiểm tra theo đúng hợp đồng dữ liệu của starter

    validate(result["chunks"], result["questions"])
    args.output.mkdir(parents=True, exist_ok=True)
    for name, key in (("chunks.json", "chunks"), ("questions.json", "questions"), ("cases.json", "cases"),
                      ("conversion_report.json", "report")):
        (args.output / name).write_text(json.dumps(result[key], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["report"]["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
