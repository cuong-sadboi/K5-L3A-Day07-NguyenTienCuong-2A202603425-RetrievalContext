# Code

Đặt code của bạn tại đây hoặc mở rộng [starter](../starter/README.md). Khung agent chưa kết nối model và vector store thật.

## Mốc 1: nối Day 6 và chuẩn bị benchmark

Cần có repo Day 6 (mặc định nằm cạnh repo này; đặt chỗ khác thì khai báo biến môi trường `DAY6_ROOT`), môi trường Python `starter/.venv` của Day 6, và vector store Day 6 đang chạy:

```bash
docker start day6_student_starter-postgres-1
```

Nếu chưa có container, tạo lại trong `<DAY6_ROOT>/starter` với **đúng tên project** `docker compose -p day6_student_starter up -d`, rồi chạy indexing theo hướng dẫn của Day 6. Chạy `docker compose up` không kèm `-p` sẽ tạo một project khác với volume rỗng.

1. Kiểm tra kết nối, phiên bản model, số chiều, độ tương thích embedding và export chunk của index B (cần thư viện của Day 6):

```bash
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/day6_link.py --check-output starter/results/day6_check.json --export-output starter/data/day6/chunks_B.json
```

2. Chuyển chunk và benchmark sang định dạng của [data/README.md](../data/README.md) (chỉ thư viện chuẩn):

```bash
python src/prepare_data.py --chunks starter/data/day6/chunks_B.json --day6-questions <DAY6_ROOT>/benchmark/questions.jsonl --unanswerable data/day7_unanswerable.json --output starter/data/converted
```

3. Kiểm tra dữ liệu bằng baseline của starter trên dev, rồi chạy test:

```bash
python starter/baseline.py --chunks starter/data/converted/chunks.json --questions starter/data/converted/questions.json --split dev --output starter/results/dev-tfidf
python -m unittest discover -s tests -v
```

## Mốc 2: agent với model thật

Cần file `.env` ở thư mục gốc (sao chép từ `.env.example`, tự điền `LLM_API_KEY`; `.env` không được commit), SDK `anthropic` 2.8.0 trong venv Day 6 (`<DAY6_ROOT>/starter/.venv/Scripts/python.exe -m pip install anthropic==2.8.0`) và vector store Day 6 đang chạy.

```bash
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/llm_client.py --probe
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split dev --name B0 --output starter/results/agent-dev-B0
```

Mỗi lần chạy ghi `retrieval.json` (Hit@1, Evidence Hit@3, MRR với câu hỏi gốc), `traces.json` (từng tool call, kết quả, context, câu trả lời, citation, lỗi, thời gian, token) và `summary.json`. Tham số: `--strategy`, `--top-k`, `--budget`, `--max-searches`, `--effort`, `--no-fallbacks`, `--ids`, `--retrieval-only`. Chạy `--split test` phải kèm `--confirm-locked`, chỉ dùng sau khi đã chốt cấu hình và tiêu chí chọn (BENCHMARK.md:17).

## Mốc 3: thêm phương pháp, thử cấu hình trên dev, chấm tay

```bash
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split dev --name M2 --method tfidf --output starter/results/agent-dev-M2
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split dev --name M3 --method hybrid --output starter/results/agent-dev-M3
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split dev --name I1 --budget 3000 --output starter/results/agent-dev-I1
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split dev --name I2 --budget 3000 --order latest-first --output starter/results/agent-dev-I2
python src/review.py starter/results/agent-dev-B0
python starter/agent_metrics.py --cases starter/data/converted/cases.json --traces starter/results/agent-dev-B0/traces.json --reviews starter/results/agent-dev-B0/reviews.json --split dev --output starter/results/agent-dev-B0/agent_metrics.json
```

`review.py` ghi `review_sheet.md` và `reviews_template.json`; người chấm điền nhãn, lưu thành `reviews.json` rồi tổng hợp bằng `agent_metrics.py` của starter.

## Mốc 4: đánh giá test sau khi chốt cấu hình

Chạy baseline và cấu hình đã chốt trên test, mỗi cấu hình một lần:

```bash
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split test --name B0 --confirm-locked --output starter/results/agent-test-B0
<DAY6_ROOT>/starter/.venv/Scripts/python.exe src/agent.py --split test --name I2 --budget 3000 --order latest-first --confirm-locked --output starter/results/agent-test-I2
python src/compare.py starter/results/agent-test-B0 starter/results/agent-test-I2 --output starter/results/compare-test.md
python src/review.py starter/results/agent-test-B0 starter/results/agent-test-I2
```

Phiếu chấm test có thêm `context_score` (0/1/2) cho câu có đáp án (BENCHMARK.md:27). Sau khi có `reviews.json`, tổng hợp bằng `agent_metrics.py` với `--split test`.

| File | Nội dung |
|---|---|
| `src/retrievers.py` | TF-IDF của starter có filter, hybrid RRF (dense + TF-IDF) |
| `src/review.py` | Phiếu chấm tay và khung nhãn cho `agent_metrics.py`; không tự chấm |
| `src/llm_client.py` | Client SDK `anthropic` trỏ tới cổng trong `.env` (truyền `api_key`/`base_url` tường minh để không dùng biến `ANTHROPIC_*` của máy), giá công bố để ước tính chi phí |
| `src/agent.py` | Controller gọi Claude, dense retriever Day 6, chạy `run_agent` của starter, trace, metric tự động |
| `src/day6_link.py` | Nạp code Day 6 dưới tên `day6src`, kiểm tra kết nối và độ tương thích embedding, export chunk |
| `src/prepare_data.py` | Adapter Day 6 → Day 7; ánh xạ evidence sang đoạn nguyên văn trong chunk |
| `tests/test_agent.py`, `tests/test_retrievers.py`, `tests/test_review.py`, `tests/test_prepare_data.py` | Test bằng dữ liệu nhỏ và client/retriever giả, không gọi API |
| `data/day7_unanswerable.json` | 4 câu thiếu bằng chứng (2 dev, 2 test) kèm cách kiểm tra |
| `starter/data/converted/` | `chunks.json`, `questions.json`, `cases.json`, `conversion_report.json`; không được Git theo dõi, dùng `git add -f` nếu được phép chia sẻ (starter/README.md) |
