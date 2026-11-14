"""So sánh các cấu hình đã chạy trên cùng split: bảng số liệu và ma trận từng câu (phân tích lỗi trước/sau).

Chỉ đọc kết quả đã lưu (summary.json, retrieval.json, traces.json); không gọi LLM. Chỉ dùng thư viện chuẩn.
    python src/compare.py starter/results/agent-dev-B0 starter/results/agent-dev-M2 ... --output starter/results/compare-dev.md
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from agent import context_hit  # noqa: E402

DATA_DIR = ROOT / "starter" / "data" / "converted"


def pct(n: int, total: int) -> str:
    return f"{n}/{total} ({100 * n / total:.1f}%)" if total else "0/0"


def load(run: Path) -> dict[str, Any]:
    read = lambda name: json.loads((run / name).read_text(encoding="utf-8"))  # noqa: E731
    return {"name": run.name.replace("agent-dev-", "").replace("agent-test-", ""), "summary": read("summary.json"),
            "retrieval": read("retrieval.json"), "traces": read("traces.json")}


def table(runs: list[dict[str, Any]]) -> list[str]:
    lines = ["| Cấu hình | Retriever, budget, thứ tự context | Hit@1 | Evidence Hit@3 | MRR | Context Evidence (agent) | "
             "Từ chối nhầm | Từ chối câu thiếu bằng chứng | Lỗi | Lượt gọi LLM | Trung vị s/câu | Ký tự input | Token output | $ output (ước tính) |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for run in runs:
        s, r = run["summary"], run["retrieval"]["summary"]
        st = s["settings"]
        answerable = sum(s["answerable_status"].values())
        unanswerable = sum(s["unanswerable_status"].values())
        lines.append(
            f"| {run['name']} | {st['retriever']}, {st['budget']} ký tự, {st.get('order', 'arrival')} | {pct(r['hit1'], r['N'])} | "
            f"{pct(r['hit3'], r['N'])} | {r['mrr']} | {pct(s['context_evidence']['n'], s['context_evidence']['N'])} | "
            f"{pct(s['answerable_status'].get('abstain', 0), answerable)} | "
            f"{s['unanswerable_status'].get('abstain', 0)}/{unanswerable} | {len(s['errors'])} | {s['llm_calls']} | "
            f"{s['latency_ms']['median'] / 1000:.1f} | {s['input_chars']} | {s['output_tokens_reported']} | {s['output_cost_usd_est']} |")
    return lines


def matrix(runs: list[dict[str, Any]], questions: dict[str, dict[str, Any]]) -> list[str]:
    """Mỗi ô: trạng thái (A = trả lời, R = từ chối, E = lỗi), dấu + nếu context cuối có evidence gold, số lần search."""
    lines = ["| Câu | Loại | Hạng gold (câu hỏi gốc) | " + " | ".join(run["name"] for run in runs) + " |",
             "|---|---|---|" + "---|" * len(runs)]
    ids = [t["query_id"] for t in runs[0]["traces"]]
    for qid in ids:
        ranks = []
        cells = []
        for run in runs:
            row = next((x for x in run["retrieval"]["rows"] if x["query_id"] == qid), None)
            ranks.append(str(row["first_hit_rank"]) if row and row["first_hit_rank"] else "-")
            trace = next(t for t in run["traces"] if t["query_id"] == qid)
            status = {"answered": "A", "abstain": "R", "error": "E"}[trace["status"]]
            hit = "+" if qid in questions and trace["status"] != "error" and context_hit(trace, questions[qid]["gold"]) else ""
            cells.append(f"{status}{hit} ({trace['n_searches']})")
        kind = "có đáp án" if qid in questions else "thiếu bằng chứng"
        lines.append(f"| {qid} | {kind} | {'/'.join(ranks)} | " + " | ".join(cells) + " |")
    return lines


def main(argv: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="So sánh các lần chạy agent trên cùng split")
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    runs = [load(run) for run in args.runs]
    questions = {q["id"]: q for q in json.loads((DATA_DIR / "questions.json").read_text(encoding="utf-8"))}
    text = "\n".join(["## Bảng so sánh", "", *table(runs), "",
                      "## Từng câu", "",
                      "A = trả lời, R = từ chối, E = lỗi; + = context cuối có evidence gold; (n) = số lần search. "
                      "Cột hạng gold: thứ hạng evidence trong top-3 với câu hỏi gốc của từng cấu hình (- = ngoài top-3).", "",
                      *matrix(runs, questions)]) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
