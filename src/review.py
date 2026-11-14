"""Tạo phiếu chấm tay cho một lần chạy agent (BENCHMARK.md §3); công cụ này không tự chấm.

Với mỗi câu, phiếu ghi câu hỏi, filter, đáp án chuẩn và evidence gold (hoặc lý do thiếu bằng chứng), trạng thái,
câu trả lời, nguyên văn từng đoạn được trích dẫn và context cuối. Kết quả trong thư mục của lần chạy:
  review_sheet.md         để đọc, đối chiếu và chấm
  reviews_template.json   khung nhãn cho starter/agent_metrics.py. Điền answer_grade (0/1/2) cho câu có đáp án,
                          citation_support (true/false cho từng citation), abstention_correct cho câu thiếu bằng
                          chứng và reason; lưu thành reviews.json rồi chạy agent_metrics.py.
Chỉ điền sẵn các nhãn mà docs quy định cứng: từ chối câu có đáp án chấm 0 (BENCHMARK.md:36); câu thiếu bằng
chứng mà agent không từ chối thì abstention_correct = false. Lần chạy lỗi không cần nhãn (starter/README.md §4).

    python src/review.py starter/results/agent-dev-B0 [starter/results/agent-dev-I1 ...]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "starter" / "data" / "converted"
GUIDE = [
    "Thang chấm (BENCHMARK.md §3):",
    "- answer_grade với câu có đáp án: 0 = sai hoặc thiếu evidence; 1 = đúng một phần; 2 = đúng và đủ. Từ chối câu có đáp án chấm 0.",
    "- citation_support: true khi đoạn được trích nằm trong context và thực sự hỗ trợ ý được trích; ID hợp lệ là chưa đủ.",
    "- abstention_correct với câu thiếu bằng chứng: true khi agent thực sự từ chối, không thêm khẳng định vô căn cứ.",
    "- context_score (chỉ test, ít nhất 5 câu có đáp án): 0 = không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.",
]


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def build(traces: list[dict[str, Any]], questions: list[dict[str, Any]], cases: list[dict[str, Any]],
          title: str = "") -> tuple[str, list[dict[str, Any]]]:
    question_by_id = {q["id"]: q for q in questions}
    case_by_id = {c["id"]: c for c in cases}
    lines = [f"# Phiếu chấm tay {title}".rstrip(), "", *GUIDE, ""]
    template: list[dict[str, Any]] = []
    for trace in traces:
        qid = trace["query_id"]
        case = case_by_id[qid]
        answerable = case["answerable"]
        chunks = {c["id"]: c for e in trace["events"] if e.get("event") == "search" for c in e["results"]}
        lines += [f"## {qid} · {'có đáp án' if answerable else 'thiếu bằng chứng'} · {trace['status']}", ""]
        lines.append(f"- Câu hỏi: {case['question']}" + (f" (filter {case['filter']})" if case.get("filter") else ""))
        if answerable:
            question = question_by_id[qid]
            lines.append(f"- Đáp án chuẩn: {question['expected_answer']}")
            lines += [f"- Evidence gold (tr. {g['page']}): {flat(g['evidence'])}" for g in question["gold"]]
        else:
            lines.append(f"- Lý do thiếu bằng chứng: {case['absence_reason']}")
        queries = [e["query"] for e in trace["events"] if e.get("event") == "search"]
        lines.append(f"- Truy vấn ({len(queries)}): " + " | ".join(queries))
        lines.append(f"- Context cuối: {', '.join(trace['final_context_ids']) or '(trống)'}")
        if trace["status"] == "error":
            lines.append(f"- Lỗi: {trace['error']}")
        lines += ["", "Câu trả lời của agent:", "", "> " + (flat(trace["answer"]) or "(trống)"), ""]
        for index, cid in enumerate(trace["citations"], start=1):
            chunk = chunks.get(cid)
            text = flat(chunk["text"]) if chunk else "(không thấy trong kết quả search)"
            lines.append(f"{index}. [{cid}] (tr. {chunk['page'] if chunk else '?'}): {text}")
        lines.append("")
        if trace["status"] == "error":
            continue
        label: dict[str, Any] = {"query_id": qid, "citation_support": [None] * len(trace["citations"]), "reason": ""}
        if answerable:
            label["answer_grade"] = None
            if trace["status"] == "abstain":
                label.update(answer_grade=0, reason="Từ chối câu có đáp án (BENCHMARK.md:36).")
            if case["split"] == "test":
                label["context_score"] = None
        else:
            label["abstention_correct"] = None
            if trace["status"] != "abstain":
                label.update(abstention_correct=False, reason="Agent không từ chối câu thiếu bằng chứng.")
        template.append(label)
    return "\n".join(lines) + "\n", template


def main(argv: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Tạo phiếu chấm tay cho các lần chạy agent")
    parser.add_argument("runs", nargs="+", type=Path, help="thư mục có traces.json")
    args = parser.parse_args(argv)
    questions = json.loads((DATA_DIR / "questions.json").read_text(encoding="utf-8"))
    cases = json.loads((DATA_DIR / "cases.json").read_text(encoding="utf-8"))
    for run in args.runs:
        traces = json.loads((run / "traces.json").read_text(encoding="utf-8"))
        sheet, template = build(traces, questions, cases, title=run.name)
        (run / "review_sheet.md").write_text(sheet, encoding="utf-8")
        (run / "reviews_template.json").write_text(json.dumps(template, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        todo = sum(v is None for label in template for v in [label.get("answer_grade", 0), label.get("abstention_correct", 0),
                                                            *label["citation_support"]])
        print(f"{run}: {len(template)} câu cần nhãn, {todo} ô chưa điền -> review_sheet.md, reviews_template.json")


if __name__ == "__main__":
    main()
