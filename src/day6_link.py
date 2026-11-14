"""Nối Day 7 với vector store và embedding model của Day 6 (GUIDE.md:5, starter/README.md:17).

Dùng lại nguyên code truy xuất của Day 6 (embedder e5 + PgVectorStore) để query embedding tương thích
với index. Code Day 6 được nạp dưới tên package `day6src`, vì Day 7 cũng có thư mục `src/`.

Cần thư viện của Day 6 (numpy, sentence-transformers, psycopg, pgvector), nên chạy bằng Python trong
`<DAY6_ROOT>/starter/.venv`. Vector store Day 6 phải đang chạy (container `day6_student_starter-postgres-1`).

    <DAY6_ROOT>/starter/.venv/Scripts/python.exe src/day6_link.py \
        --check-output starter/results/day6_check.json --export-output starter/data/day6/chunks_B.json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DAY6_ROOT = ROOT.parent / "K5-L3A-DAY06-NguyenTienCuong-2A202603425-DataIngestion"
PACKAGE = "day6src"
EXPORT_COLUMNS = ("chunk_id", "document_id", "source", "page", "chapter", "section", "section_title",
                  "char_start", "char_end", "content", "content_hash", "doc_sha256", "metadata", "model")


def day6_root() -> Path:
    """Thư mục repo Day 6; đổi bằng biến môi trường DAY6_ROOT nếu đặt ở chỗ khác."""
    return Path(os.environ.get("DAY6_ROOT") or DEFAULT_DAY6_ROOT).resolve()


def load_day6(root: Path | None = None):
    """Nạp package `starter/src` của Day 6 dưới tên `day6src` để không trùng với `src` của Day 7."""
    if PACKAGE in sys.modules:
        return sys.modules[PACKAGE]
    package_dir = (root or day6_root()) / "starter" / "src"
    init_file = package_dir / "__init__.py"
    if not init_file.exists():
        raise FileNotFoundError(f"Không thấy code Day 6 tại {package_dir}; đặt biến môi trường DAY6_ROOT.")
    spec = importlib.util.spec_from_file_location(PACKAGE, init_file, submodule_search_locations=[str(package_dir)])
    module = importlib.util.module_from_spec(spec)
    sys.modules[PACKAGE] = module
    spec.loader.exec_module(module)
    return module


def connect(root: Path | None = None):
    """Trả về (config, embedder, store) của Day 6. Lỗi kết nối được báo ra, không có phương án giả lập."""
    load_day6(root)
    from day6src import config, embeddings, indexing, store  # type: ignore[import-not-found]

    embedder = embeddings.create_embedder()
    db = store.PgVectorStore(indexing.database_url(), embedder.dimensions, embedder.model_name, config.VECTOR_TABLE)
    return config, embedder, db


def check(config, embedder, db, index: str, samples: int = 3) -> dict[str, Any]:
    """Ghi phiên bản model, số chiều, cách kết nối và kiểm tra embedding tương thích với index.

    Kiểm tra tương thích: embed lại vài chunk của index bằng đúng model và tiền tố "passage: " như lúc
    Day 6 tạo index; cosine với vector đang lưu phải xấp xỉ 1.
    """
    import numpy as np
    from psycopg import sql

    table = sql.Identifier(config.VECTOR_TABLE)
    with db.conn.cursor() as cursor:
        cursor.execute(sql.SQL("SELECT DISTINCT model FROM {} WHERE strategy = %s").format(table), (index,))
        models = sorted(row[0] for row in cursor.fetchall())
        cursor.execute(sql.SQL("SELECT chunk_id, content, embedding FROM {} WHERE strategy = %s ORDER BY chunk_id")
                       .format(table), (index,))
        rows = cursor.fetchall()
    if not rows:
        raise RuntimeError(f"Index {index} không có chunk nào trong vector store Day 6.")
    picks = [rows[round(i * (len(rows) - 1) / max(samples - 1, 1))] for i in range(samples)]
    fresh = embedder.embed_documents([row[1] for row in picks])
    stored = [row[2].to_numpy() if hasattr(row[2], "to_numpy") else np.asarray(row[2]) for row in picks]
    cosines = [round(float(np.dot(np.asarray(new), old)), 6) for new, old in zip(fresh, stored)]
    return {
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "day6_root": str(day6_root()),
        "connection": "DATABASE_URL đọc từ <DAY6_ROOT>/starter/.env qua code Day 6 (không chép vào Day 7)",
        "vector_store": {"backend": "PostgreSQL + pgvector", **db.server_info(), "table": config.VECTOR_TABLE,
                         "search": "exact, cosine distance <=>, score = 1 - distance"},
        "embedding": embedder.describe(),
        "indexes": {name: {"params": params, "rows": db.count(name), "fingerprint": db.fingerprint(name)}
                    for name, params in config.INDEXES.items()},
        "strategies": config.STRATEGIES,
        "compatibility": {
            "index": index,
            "models_in_index": models,
            "same_model": models == [embedder.model_name],
            "re_embedded_samples": [{"chunk_id": row[0], "cosine_with_stored": cos} for row, cos in zip(picks, cosines)],
            "min_cosine": min(cosines),
        },
    }


def export_chunks(config, db, index: str) -> list[dict[str, Any]]:
    """Mọi chunk của một index đúng như đang nằm trong vector store (không kèm vector), sắp theo chunk_id."""
    from psycopg import sql

    query = sql.SQL("SELECT {columns} FROM {table} WHERE strategy = %s ORDER BY chunk_id").format(
        columns=sql.SQL(", ").join(map(sql.Identifier, EXPORT_COLUMNS)), table=sql.Identifier(config.VECTOR_TABLE))
    with db.conn.cursor() as cursor:
        cursor.execute(query, (index,))
        return [dict(zip(EXPORT_COLUMNS, row)) for row in cursor.fetchall()]


def main(argv: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Kiểm tra kết nối vector store Day 6 và export chunk của một index")
    parser.add_argument("--index", default="B", help="index Day 6 dùng cho dense (mặc định B, index của chiến lược C)")
    parser.add_argument("--check-output", type=Path, required=True)
    parser.add_argument("--export-output", type=Path, required=True)
    args = parser.parse_args(argv)

    config, embedder, db = connect()
    with db:
        info = check(config, embedder, db, args.index)
        rows = export_chunks(config, db, args.index)
    info["export"] = {"index": args.index, "rows": len(rows), "path": args.export_output.as_posix()}
    for path, obj in ((args.check_output, info), (args.export_output, rows)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    emb = info["embedding"]
    print(json.dumps({"vector_store": info["vector_store"],
                      "embedding": {k: emb[k] for k in ("model", "revision", "dimensions", "query_prefix", "passage_prefix")},
                      "indexes": {k: v["rows"] for k, v in info["indexes"].items()},
                      "compatibility": info["compatibility"], "export": info["export"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
