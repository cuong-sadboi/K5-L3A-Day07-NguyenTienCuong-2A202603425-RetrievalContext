"""Gọi Claude thật qua Messages API bằng SDK `anthropic`, qua cổng API khai báo trong `.env`.

Cấu hình (`.env` của Day 7): LLM_BASE_URL (vd. https://api.xpiki.com/v1), LLM_API_KEY, LLM_MODEL.
Client luôn nhận `api_key` và `base_url` tường minh: khi có tham số tường minh, SDK không đọc các biến
môi trường ANTHROPIC_* (máy này có ANTHROPIC_AUTH_TOKEN / ANTHROPIC_BASE_URL của Claude Code, không
được gửi chúng tới cổng bên thứ ba). Key không bao giờ được in ra; lỗi được báo ra, không có phương án
giả lập (starter/README.md).

Cần SDK anthropic 2.8.0 (cài trong <DAY6_ROOT>/starter/.venv):
    <DAY6_ROOT>/starter/.venv/Scripts/python.exe src/llm_client.py --probe
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

# Giá Anthropic công bố (USD / 1 triệu token: input, output), theo bảng model trong tài liệu Claude API
# (cập nhật 2026-11-03). Cổng bên thứ ba có thể tính giá khác, nên chi phí trong trace là ước tính.
PRICES_PER_MTOK = {
    "claude-opus-5-5": (4.0, 20.0), "claude-opus-5": (5.0, 25.0), "claude-opus-4-8": (5.0, 25.0),
    "claude-sonnet-5": (2.0, 10.0), "claude-sonnet-4-6": (3.0, 15.0),
    "claude-haiku-5-5": (0.10, 0.50), "claude-haiku-4-5": (1.0, 5.0),
}


class LLMError(RuntimeError):
    """Thiếu cấu hình hoặc lỗi khi gọi nhà cung cấp LLM."""


def load_env(path: Path = ROOT / ".env") -> None:
    """Nạp KEY=VALUE từ `.env` vào môi trường (không ghi đè biến đã có, bỏ qua giá trị rỗng)."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if value and key not in os.environ:
            os.environ[key] = value


def make_client(timeout: float = 120.0, max_retries: int = 2):
    """Client SDK trỏ tới cổng trong `.env`; SDK tự thêm `/v1/messages` nên bỏ hậu tố `/v1` của base URL."""
    import anthropic

    load_env()
    base_url = os.environ.get("LLM_BASE_URL", "").rstrip("/")
    api_key = os.environ.get("LLM_API_KEY", "")
    if not base_url or not api_key:
        raise LLMError("Thiếu LLM_BASE_URL hoặc LLM_API_KEY trong .env")
    if base_url.endswith("/v1"):
        base_url = base_url[: -len("/v1")]
    return anthropic.Anthropic(api_key=api_key, base_url=base_url, timeout=timeout, max_retries=max_retries)


def configured_model() -> str:
    load_env()
    model = os.environ.get("LLM_MODEL", "")
    if not model:
        raise LLMError("Thiếu LLM_MODEL trong .env")
    return model


def usage_dict(usage: Any) -> dict[str, Any]:
    if usage is None:
        return {}
    return usage.to_dict() if hasattr(usage, "to_dict") else dict(usage)


def estimate_cost(model: str, usage: dict[str, Any]) -> float | None:
    """Chi phí ước tính theo giá công bố; token cache tính theo giá input (cận trên)."""
    price = PRICES_PER_MTOK.get(model)
    if price is None:
        return None
    input_tokens = sum(int(usage.get(key) or 0) for key in
                       ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    return round((input_tokens * price[0] + int(usage.get("output_tokens") or 0) * price[1]) / 1_000_000, 6)


PROBE_TOOL = {
    "name": "search",
    "description": "Tìm đoạn tài liệu liên quan tới truy vấn.",
    "input_schema": {"type": "object", "properties": {"query": {"type": "string"}},
                     "required": ["query"], "additionalProperties": False},
    "strict": True,
}


def _summary(response: Any, started: float) -> str:
    calls = [f"{b.name}({json.dumps(b.input, ensure_ascii=False)})" for b in response.content if b.type == "tool_use"]
    return (f"model={response.model} stop_reason={response.stop_reason} tool_use={calls or 'KHÔNG'} "
            f"usage={usage_dict(response.usage)} {round((time.perf_counter() - started) * 1000)} ms")


def main(argv: list[str] | None = None) -> None:
    import anthropic

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Thử gọi Claude qua cổng trong .env (Messages API)")
    parser.add_argument("--probe", action="store_true", help="thử tool use, effort và fallbacks")
    args = parser.parse_args(argv)
    client, model = make_client(), configured_model()
    print(f"base_url={client.base_url} model={model} auth_token_tu_env={client.auth_token is not None}")
    if not args.probe:
        return
    request = dict(model=model, max_tokens=16000, tools=[PROBE_TOOL],
                   tool_choice={"type": "auto", "disable_parallel_tool_use": True},
                   output_config={"effort": "medium"},
                   messages=[{"role": "user", "content": "Gọi tool search với query 'bot traffic'."}])
    for name, call in (("messages.create", lambda: client.messages.create(**request)),
                       ("beta + fallbacks=default", lambda: client.beta.messages.create(
                           betas=["server-side-fallback-2026-07-01"], fallbacks="default", **request))):
        started = time.perf_counter()
        try:
            print(f"[{name}] {_summary(call(), started)}")
        except anthropic.APIStatusError as error:
            print(f"[{name}] LỖI HTTP {error.status_code}: {str(error.message)[:300]}")
        except anthropic.APIConnectionError as error:
            print(f"[{name}] LỖI kết nối: {error}")


if __name__ == "__main__":
    main()
