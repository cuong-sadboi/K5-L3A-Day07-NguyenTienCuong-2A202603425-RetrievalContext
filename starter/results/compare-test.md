## Bảng so sánh

| Cấu hình | Retriever, budget, thứ tự context | Hit@1 | Evidence Hit@3 | MRR | Context Evidence (agent) | Từ chối nhầm | Từ chối câu thiếu bằng chứng | Lỗi | Lượt gọi LLM | Trung vị s/câu | Ký tự input | Token output | $ output (ước tính) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B0 | dense-C, 800 ký tự, arrival | 4/6 (66.7%) | 4/6 (66.7%) | 0.6667 | 2/6 (33.3%) | 3/6 (50.0%) | 2/2 | 0 | 25 | 14.4 | 48894 | 1333 | 0.0267 |
| I2 | dense-C, 3000 ký tự, latest-first | 4/6 (66.7%) | 4/6 (66.7%) | 0.6667 | 5/6 (83.3%) | 0/6 (0.0%) | 2/2 | 0 | 20 | 10.8 | 57016 | 1172 | 0.0234 |

## Từng câu

A = trả lời, R = từ chối, E = lỗi; + = context cuối có evidence gold; (n) = số lần search. Cột hạng gold: thứ hạng evidence trong top-3 với câu hỏi gốc của từng cấu hình (- = ngoài top-3).

| Câu | Loại | Hạng gold (câu hỏi gốc) | B0 | I2 |
|---|---|---|---|---|
| q19 | có đáp án | -/- | R (2) | A+ (1) |
| q20 | có đáp án | 1/1 | R (3) | A+ (1) |
| q21 | có đáp án | 1/1 | R (3) | A+ (1) |
| q22 | có đáp án | 1/1 | A+ (1) | A+ (1) |
| q23 | có đáp án | 1/1 | A+ (1) | A+ (1) |
| q24 | có đáp án | -/- | A (1) | A (1) |
| q27 | thiếu bằng chứng | -/- | R (4) | R (3) |
| q28 | thiếu bằng chứng | -/- | R (2) | R (3) |
