# Báo cáo Day 7

## Dữ liệu và benchmark

- Nguồn, quyền sử dụng, số trang và số chunk: Đồ án tốt nghiệp "Xây dựng hệ thống phân tích và phát hiện lưu lượng truy cập ảo trong Digital Marketing dựa trên Machine Learning" (2026), `source_id` `doan-bot-traffic-2026`, tiếng Việt, dùng lại từ Day 6 (manifest Day 6 `data/manifest.json`; truy cập 2026-11-13; trích bằng pypdf 6.21.4, chuẩn hóa Unicode NFC). PDF có 89 trang vật lý; 69 trang nội dung được index (tr. 11–86, loại tr. 40–41 và 80–84 vì chỉ có hình/chú thích dưới 200 ký tự chữ). Index B của Day 6 (chia theo đoạn, tối đa 800 ký tự): 254 chunk. Quyền: học viên là tác giả và cho phép xử lý cục bộ cho mục đích học tập; PDF gốc không commit vì trang bìa có thông tin cá nhân. Ngày 2026-11-14 học viên (tác giả) cho phép gửi nội dung tài liệu lên API LLM bên ngoài để chạy agent (kiểm tra quyền theo RULES.md:6).
- Vector store, embedding model, phiên bản và số chiều: PostgreSQL 16.16 + pgvector 0.8.7 của Day 6 (Docker, container `day6_student_starter-postgres-1`, 127.0.0.1:55433), bảng `chunks`, tìm exact theo cosine (`score = 1 - distance`). Embedding `intfloat/multilingual-e5-base`, revision `d128750597153bb5987e10b1c3493a34e5a4502a`, 768 chiều, tiền tố `query: ` / `passage: `, vector chuẩn hóa; sentence-transformers 6.3.0, transformers 5.22.2, torch 2.15.0+cpu. Kết nối: `src/day6_link.py` dùng lại code truy xuất của Day 6 (DATABASE_URL đọc từ `.env` của Day 6, không chép sang repo này). Kiểm tra tương thích: embed lại 3 chunk của index B bằng đúng model và tiền tố cho cosine 1,0 với vector đã lưu (`starter/results/day6_check.json`).
- Agent model, cách chạy và phân chia dev/test: Agent gọi LLM qua cổng API bên thứ ba `https://api.xpiki.com/v1` (API tương thích OpenAI, xác thực Bearer; key do học viên cung cấp, lưu trong `.env` không commit); tên model chưa chốt (mốc 1:00–2:00). Giữ cách chia dev/test của Day 6: chia theo mục của đồ án, test lấy từ các mục 1.5.1, 2.2.2, 3.5, 3.19, 3.20 và Kết luận. Test Day 6 chỉ chạy sau khi đã chốt cấu hình và chưa dùng để chỉnh, nên dùng lại được (starter/README.md:43). Dev: 18 câu có đáp án + 2 câu thiếu bằng chứng; test: 6 + 2. Lệnh chuẩn bị dữ liệu: `src/README.md`.
- Cách xác định câu có/thiếu evidence và tiêu chí chấm: 24 câu có đáp án lấy từ benchmark Day 6 (Claude soạn nháp theo yêu cầu của học viên; evidence chép nguyên văn từ trang gold; evidence thay thế `alt_gold` cho q15, q16, q21). Evidence được ánh xạ sang đoạn nguyên văn trong chunk index B, so khớp bỏ qua hoa/thường, khoảng trắng và gạch nối như quy tắc kiểm chứng của Day 6; 21/27 evidence cần ánh xạ vì chunk giữ ký tự xuống dòng của PDF (đối chiếu trong `starter/data/converted/conversion_report.json`). Hit dùng nguyên định nghĩa của starter (evidence nằm trọn trong một chunk đúng nguồn và trang), áp dụng chung cho mọi phương pháp. 8 câu có filter chương (6 dev, 2 test) lấy từ chính câu hỏi ("Trong chương …"), không lấy từ gold. 4 câu thiếu bằng chứng (q25, q26 ở dev; q27, q28 ở test) do Claude soạn nháp cho Day 7, gần chủ đề tài liệu, cần học viên rà soát; cách kiểm tra (đọc mục liên quan, tìm từ khóa trên toàn bộ 254 chunk) ghi trong `absence_reason` của `data/day7_unanswerable.json`; kết luận chỉ áp dụng cho phần đã index. Câu thiếu bằng chứng không vào mẫu số của retrieval metrics. Tiêu chí chấm theo BENCHMARK.md: Hit@1, Evidence Hit@3, Context Evidence Rate; câu trả lời 0/1/2, citation hợp lệ, abstention.

## Retrieval và thử nghiệm

| Cấu hình | Phương pháp, top-k, filter, rerank, context budget | Giả thuyết / thay đổi | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Thời gian / chi phí |
|---|---|---|---|---|---|---|---|
| Baseline (B0) | Dense trên vector store Day 6 (chiến lược C: index B + filter chương do người dùng nêu), top-k 3, không rerank, context budget 800 ký tự (gồm tiêu đề), agent tối đa 4 lần search | Mặc định của starter, làm mốc so sánh | dev | 11/18 (61,1%) | 17/18 (94,4%) | 12/18 (66,7%) | Trung vị 9,6 s/câu (tối đa 26 s); 54 lượt gọi LLM; 105.662 ký tự input; 3.266 token output; khoảng $0,065 phần output (ước tính) |
| Phương pháp 2 (M2) | TF-IDF của starter trên cùng corpus, cùng filter, top-k 3, budget 800 ký tự, agent như B0 | Lexical: mạnh khi câu hỏi dùng đúng từ trong tài liệu | dev | 12/18 (66,7%) | 15/18 (83,3%) | 11/18 (61,1%) | Trung vị 9,9 s/câu (tối đa 29 s); 58 lượt gọi LLM; 114.399 ký tự input; 3.629 token output; khoảng $0,073 phần output |
| Phương pháp 3 (M3) | Hybrid RRF (dense C + TF-IDF, k = 60, 20 chunk mỗi danh sách), top-k 3, budget 800 ký tự | Gộp điểm mạnh của hai cách tìm | dev | 15/18 (83,3%) | 17/18 (94,4%) | 11/18 (61,1%) | Trung vị 10,6 s/câu (tối đa 28 s); 55 lượt gọi; 106.926 ký tự; 3.537 token; khoảng $0,071 |
| Cải thiện 1 (I1) | Như B0, context budget 3000 ký tự | Budget 800 loại evidence dài hoặc ở hạng 2–3 | dev | 11/18 (61,1%) | 17/18 (94,4%) | 15/18 (83,3%) | Trung vị 10,9 s/câu (tối đa 28 s); 42 lượt gọi; 108.463 ký tự; 2.805 token; khoảng $0,056 |
| Cải thiện 2 (I2) | Như I1, gộp context ưu tiên kết quả lượt search mới nhất | Kết quả lượt search mới không bị loại khi budget đầy | dev | 11/18 (61,1%) | 17/18 (94,4%) | 16/18 (88,9%) | Trung vị 9,7 s/câu (tối đa 14 s); 40 lượt gọi; 98.139 ký tự; 2.678 token; khoảng $0,054 |
| Cấu hình đã chọn (I2) | Dense C, top-k 3, budget 3000 ký tự, gộp context ưu tiên lượt search mới, tối đa 4 lần search | Chốt trên dev ngày 2026-11-14, chạy test một lần | test | 4/6 (66,7%) | 4/6 (66,7%) | 5/6 (83,3%) | Trung vị 10,8 s/câu (q27 có một lượt gọi LLM mất 206,5 s ở phía cổng API); 20 lượt gọi LLM; 57.016 ký tự input; 1.172 token output; khoảng $0,023 phần output |
| Baseline (B0) | Như B0 trên dev | Mốc so sánh, chạy test một lần | test | 4/6 (66,7%) | 4/6 (66,7%) | 2/6 (33,3%) | Trung vị 14,4 s/câu (tối đa 25 s); 25 lượt gọi; 48.894 ký tự; 1.333 token; khoảng $0,027 |

Một cấu hình có thể đồng thời là phương pháp mới và cải thiện; giải thích rõ. Báo `n/N` và tỷ lệ, ghi đơn vị thời gian/chi phí, so sánh test sau khi chốt. Nêu hai lỗi dev, nguyên nhân, cách thử và lý do chọn cấu hình:

**Thiết kế thử nghiệm và tiêu chí chọn (chốt ngày 2026-11-14, sau khi chạy B0 và trước khi chạy M2, M3, I1, I2; chỉ dùng dev).** Mọi cấu hình dùng cùng corpus (index B, 254 chunk, xuất từ vector store Day 6), cùng câu hỏi, nhãn, filter chương và định nghĩa hit của starter; agent giống B0 (claude-opus-5-5, effort medium, tối đa 4 lần search, top-k 3), mỗi cấu hình chỉ đổi một yếu tố.

- M2 (phương pháp 2, lexical): TF-IDF của starter trên cùng corpus, cùng filter, budget 800 ký tự.
- M3 (phương pháp 3, hybrid): gộp dense C và TF-IDF bằng RRF (điểm = Σ 1/(k + thứ hạng), k = 60, lấy 20 chunk từ mỗi danh sách); chỉ dùng thứ hạng nên không cần chuẩn hóa điểm của hai retriever; budget 800 ký tự.
- I1 (cải thiện 1, đổi context budget): B0 với budget 3000 ký tự. Giả thuyết từ trace B0: budget 800 chỉ chứa được một chunk, nên q03, q05 (chunk gold đứng hạng 1 nhưng dài hơn budget) và q04, q08, q14, q17 (gold ở hạng 2–3) không có evidence trong context; 3000 ký tự đủ cho 3 chunk dài nhất của index B (tối đa 800 ký tự cộng khoảng 80 ký tự tiêu đề mỗi chunk), nên Context Evidence Rate sẽ tăng và số câu từ chối nhầm sẽ giảm, đổi lại tăng số ký tự input.
- I2 (cải thiện 2, chọn đoạn theo độ liên quan): I1 với thứ tự gộp context ưu tiên kết quả của lượt search mới nhất. Giả thuyết: khi agent tìm lại bằng truy vấn đã chỉnh, khung starter giữ chunk của lượt trước nên kết quả mới có thể bị loại khi budget đầy (starter/README.md:63); ưu tiên lượt mới giữ được evidence vừa tìm thấy.

Tiêu chí chọn, xét lần lượt; bằng nhau ở một bước thì xét bước sau, vẫn bằng thì chọn cấu hình đơn giản hơn:

1. Vẫn từ chối đúng 2/2 câu dev thiếu bằng chứng.
2. Context Evidence Rate của agent trên dev cao nhất; lấy 2 cấu hình dẫn đầu.
3. Chấm tay 2 cấu hình đó và B0: grounded answer trung bình cao hơn, rồi ít từ chối nhầm hơn.
4. Evidence Hit@3, rồi Hit@1, với câu hỏi gốc.
5. Thời gian trung vị mỗi câu, số lượt gọi LLM và chi phí thấp hơn.

**Kết quả trên dev và phân tích lỗi.** Bảng chi tiết từng câu ở `starter/results/compare-dev.md`.

- Lỗi 1, từ chối nhầm do context budget (q03, q05, q14; cả q04, q17). Ở B0, chunk gold của q03 và q05 đứng hạng 1 nhưng dài hơn budget 800 ký tự, q14 ở hạng 2, nên evidence không vào context và agent từ chối; tìm lại cũng không thêm được vì chunk của lượt đầu giữ chỗ. Sau khi tăng budget lên 3000 ký tự (I1), q03, q05, q14 đều được trả lời với evidence trong context; từ chối nhầm giảm từ 5/18 xuống 0/18, Context Evidence Rate tăng từ 12/18 lên 15/18, số lượt gọi LLM giảm từ 54 xuống 42 vì agent ít phải tìm lại.
- Lỗi 2, trả lời sai ý dù citation hợp lệ (q08). Ở B0, chunk gold tr. 60 đứng hạng 3 nên bị budget loại, agent trả lời bằng đoạn tr. 74 (mục 3.18: dữ liệu mô phỏng chia hai nhóm real/bot), không nêu nguồn dữ liệu nào; citation đúng ID nhưng câu trả lời không đúng câu hỏi. Ở I1 và I2, câu trả lời tốt hơn (log truy cập và dữ liệu mô phỏng, đoạn tr. 66) nhưng vẫn thiếu dataset.csv, vì truy vấn agent tự viết không lấy được tr. 60 trong top-3. Lỗi còn lại nằm ở retrieval, không phải ở budget.
- Lỗi 3, trả lời câu thiếu bằng chứng (M3, q25). Cấu hình hybrid trả lời "gần 50% lưu lượng Internet toàn cầu; tài liệu không nêu tỷ lệ riêng cho Việt Nam" kèm citation tr. 17 thay vì chỉ từ chối như prompt yêu cầu; `run_agent` vì vậy ghi là trả lời. Các cấu hình còn lại đều từ chối q25, nên đây là dao động của model trước context gần chủ đề, và M3 bị loại ở bước 1.
- M2 (TF-IDF) có Hit@1 cao hơn dense (12/18 so với 11/18) nhưng Evidence Hit@3 thấp hơn (15/18) và agent từ chối nhầm nhiều hơn (6/18). M3 (hybrid) có retrieval tốt nhất (Hit@1 15/18, MRR 0,88) nhưng với budget 800 Context Evidence Rate vẫn chỉ 11/18: thứ hạng tốt hơn không giúp được khi context chỉ chứa một chunk.
- I2 không kiểm chứng được giả thuyết của nó: trên dev cả 20 câu chỉ search một lần, nên thứ tự gộp context của nhiều lượt search chưa lần nào được dùng. Chênh lệch giữa I1 và I2 (q04 có evidence trong context ở I2, 40 so với 42 lượt gọi) đến từ khác biệt truy vấn giữa hai lần chạy của model, không phải từ thay đổi thứ tự.

**Áp tiêu chí chọn** (nhãn chấm tay ở bước 3 do Claude soạn nháp kèm lý do; học viên đọc phiếu và xác nhận ngày 2026-11-14; số liệu tính bằng `starter/agent_metrics.py`):

1. Loại M3 (từ chối đúng 1/2); B0, M2, I1, I2 đạt 2/2.
2. Context Evidence Rate: I2 16/18, I1 15/18, B0 12/18, M2 11/18; hai cấu hình dẫn đầu là I2 và I1.
3. Grounded answer trung bình: I2 1,89 (0/2/16), I1 1,83 (0/3/15), B0 1,33 (6/0/12); từ chối nhầm: I2 0/18, I1 0/18, B0 5/18. Chênh lệch I2 và I1 chỉ ở q04; nếu q04 của hai cấu hình được chấm như nhau thì hai cấu hình hòa ở bước 3 và 4, và I2 vẫn được chọn ở bước 5 (40 so với 42 lượt gọi, trung vị 9,7 so với 10,9 s/câu).

Cấu hình đã chốt (ngày 2026-11-14, trước khi chạy test): I2, gồm dense trên vector store Day 6 (chiến lược C), top-k 3, budget 3000 ký tự, gộp context ưu tiên lượt search mới nhất, tối đa 4 lần search, claude-opus-5-5 effort medium. Trên dev, I2 tương đương I1 cộng phần thứ tự gộp context, và phần này chỉ có tác dụng khi agent tìm từ hai lần trở lên.

Giới hạn: mỗi cấu hình chỉ chạy một lần trên dev nên chưa đo được dao động giữa các lần chạy của model; dev chỉ có 18 câu có đáp án; chi phí chỉ ước tính được phần output vì cổng API không trả số token input.

## Agent và đánh giá

- Tool, số lượt gọi, điều kiện dừng, cách chọn context và xử lý lỗi: Agent dùng vòng lặp `run_agent` của starter với controller trong `src/agent.py`. Model `claude-opus-5-5` (effort `medium`, `max_tokens` 16000; thinking adaptive luôn bật ở model này, không gửi `temperature`) được gọi qua Messages API của cổng xpiki bằng SDK `anthropic` 2.8.0; bật `fallbacks: "default"` (beta `server-side-fallback-2026-07-01`) theo khuyến nghị của tài liệu Claude, model thực sự trả lời được ghi trong trace. Có một tool `search` (schema strict, `tool_choice` auto, tối đa một lời gọi mỗi lượt) gọi dense retrieval trên vector store Day 6 (chiến lược C). Mỗi lượt model nhận câu hỏi, số lần search còn lại, các truy vấn đã dùng và context đã gộp trong `<documents>`, không gửi lại toàn bộ lịch sử để budget context có hiệu lực. Điều kiện dừng: model trả lời mà không gọi tool, hoặc hết lượt search (lượt cuối không cung cấp tool nên model phải trả lời). Baseline B0 giữ mặc định của starter: tối đa 4 lần search, top-k 3, context budget 800 ký tự (tính cả tiêu đề nguồn), gộp context theo thứ tự đến và loại trùng (`pack_context`); lý do: dùng đúng khung starter làm mốc so sánh, còn budget và cách chọn context sẽ được thử ở các cấu hình cải thiện. Câu trả lời phải có citation `[ID]` nằm trong context, nếu không `run_agent` chuyển thành từ chối; khi thiếu bằng chứng, model được dặn trả lời đúng câu "Không đủ bằng chứng để trả lời." và không kèm citation. Nội dung tài liệu nằm trong `<documents>` và prompt nói rõ đó là dữ liệu, không phải chỉ dẫn. Lỗi model hoặc vector store được ghi `status: error` kèm thông báo (key bị che), không thay bằng kết quả giả; SDK tự thử lại tối đa 2 lần với lỗi mạng, 429 và 5xx. Chi phí: cổng không trả số token input thật (luôn báo `input_tokens` = 1) và không hỗ trợ `count_tokens` (404), nên trace ghi số ký tự input, số token output cổng báo và chi phí phần output ước tính theo giá công bố của `claude-opus-5-5` ($4 / $20 cho 1 triệu token input / output); chi phí thực đọc trên trang quản lý của cổng.

| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm |
|---|---|---|---|---|---|---|---|
| B0 / dev | 20/20 | Search: 1 lần ở 13 câu, 2 lần ở 2 câu, 3 lần ở 3 câu, 4 lần ở 2 câu (54 lượt gọi LLM) | 6/0/12, trung bình 1,33 | 13/13 | 13/13 câu trả lời | 2/2 | 5/18 (q03, q04, q05, q14, q17) |
| M2 / dev | 20/20 | 1 lần ở 11 câu, 2 lần ở 2, 3 lần ở 5, 4 lần ở 2 (58 lượt gọi) | Không chấm (không vào 2 cấu hình dẫn đầu ở bước 2) | Không chấm | 12/12 | 2/2 (theo trạng thái, chưa chấm tay) | 6/18 |
| M3 / dev | 20/20 | 1 lần ở 13 câu, 3 lần ở 6, 4 lần ở 1 (55 lượt gọi) | Không chấm (bị loại ở bước 1) | Không chấm | 15/15 | 1/2 (q25 bị trả lời) | 4/18 |
| I1 / dev | 20/20 | 1 lần ở 18 câu, 2 lần ở 2 (42 lượt gọi) | 0/3/15, trung bình 1,83 | 18/19 | 18/18 | 2/2 | 0/18 |
| I2 / dev | 20/20 | 1 lần ở cả 20 câu (40 lượt gọi) | 0/2/16, trung bình 1,89 | 17/19 | 18/18 | 2/2 | 0/18 |
| B0 / test | 8/8 | 1 lần ở 3 câu, 2 lần ở 2, 3 lần ở 2, 4 lần ở 1 (25 lượt gọi) | 3/1/2, trung bình 0,83 | 3/3 | 3/3 | 2/2 | 3/6 (q19, q20, q21) |
| I2 / test | 8/8 | 1 lần ở 6 câu có đáp án, 3 lần ở 2 câu thiếu bằng chứng (20 lượt gọi) | 0/0/6, trung bình 2,00 | 6/6 | 6/6 | 2/2 | 0/6 |

Điểm context đọc tay cho 6 câu test có đáp án (BENCHMARK.md:27; 0 = không có evidence, 1 = có nhưng thiếu điều kiện hoặc nguồn, 2 = đủ evidence và nguồn): B0 0/1/2 = 3/1/2, I2 0/1/2 = 0/1/5. Lý do từng câu trong `reviews.json` (Claude soạn nháp, học viên xác nhận) của `starter/results/agent-test-B0/` và `agent-test-I2/`.

| Query ID | Loại câu | Tool call và kết quả | Câu trả lời và citation | Nhãn, lý do |
|---|---|---|---|---|
| q19 (I2, test) | Có đáp án | 1 search; context p79, p11, p23:1304-2006 (có evidence) | Ưu tiên phát hiện bot độc hại (Bad Bot) [p23:1304-2006] | 2, context 2: đoạn tr. 23 nêu đề tài tập trung vào bad bot traffic |
| q20 (I2, test) | Có đáp án | 1 search; context p64:0-662 (có evidence), p64:663-1110, p15 | Không tự động chặn ngay, đưa vào danh sách nghi ngờ để quản trị viên kiểm tra, hiển thị confidence và feature nổi bật [p64:0-662] | 2, context 2 |
| q21 (I2, test) | Có đáp án, filter chương 3 | 1 search; context p75:1103-1885 (có evidence), p76, p75:0-678 | Accuracy 93,85% [p75:1103-1885] | 2, context 2 |
| q22 (I2, test) | Có đáp án, filter chương 2 | 1 search; context p38:0-535 (có evidence), p53, p56 | Tối đa 2 giây với request thông thường [p38:0-535] | 2, context 2 |
| q23 (I2, test) | Có đáp án | 1 search; context p77:0-538 (có evidence), p77:960-1649, p63 | Random Forest kết hợp nhiều dấu hiệu yếu nên vẫn đánh dấu session đáng ngờ dù RPM không cao [p77:0-538] | 2, context 2 |
| q24 (I2, test) | Có đáp án | 1 search; context p66:1236-1583, p69, p85:1651-2425 (không có đoạn "hạn chế đầu tiên") | Dữ liệu thực nghiệm chưa đủ lớn và chưa phản ánh đầy đủ các kiểu bot tinh vi [p66:1236-1583] | 2, context 1: đúng nội dung, đoạn kết luận tr. 85 không có trong context |
| q27 (I2, test) | Thiếu bằng chứng | 3 search (LSTM, F1-score, bảng so sánh mô hình); context p23, p63, p74 | Không đủ bằng chứng để trả lời. | Từ chối đúng |
| q28 (I2, test) | Thiếu bằng chứng | 3 search (chi phí hạ tầng hằng tháng bằng USD); context p60, p62, p33 | Không đủ bằng chứng để trả lời. | Từ chối đúng |

- Đường dẫn trace, nhãn, lệnh chạy, thời gian và chi phí: mỗi cấu hình dev ở `starter/results/agent-dev-<tên>/` (B0, M2, M3, I1, I2; gồm `traces.json`, `summary.json`, `retrieval.json`, `run.log`); bảng so sánh `starter/results/compare-dev.md`; test ở `starter/results/agent-test-B0/` và `agent-test-I2/` (thêm `review_sheet.md`, nhãn và điểm context), bảng `starter/results/compare-test.md`; phiếu chấm tay `review_sheet.md`, nhãn `reviews.json` (Claude soạn nháp, học viên xác nhận) và số liệu `agent_metrics.json` trong thư mục B0, I1, I2; lệnh chạy trong `src/README.md`. Retrieval dense C trên dev (Hit@1 11/18, Hit@3 17/18) trùng số của Day 6.
- Kết quả trước/sau, ví dụ lỗi, đánh đổi và giới hạn: Trên test, I2 so với B0: Context Evidence Rate 2/6 lên 5/6, từ chối nhầm 3/6 xuống 0/6, grounded answer trung bình 0,83 lên 2,00; cả hai từ chối đúng 2/2 câu thiếu bằng chứng; retrieval với câu hỏi gốc như nhau (Hit@1 4/6, Hit@3 4/6) vì cùng dense C. Xu hướng giống dev: lỗi chính của B0 là budget 800 ký tự loại evidence (q19, q20, q21 bị từ chối dù có đáp án). Đánh đổi: I2 gửi nhiều ký tự input hơn (57.016 so với 48.894) nhưng ít lượt gọi LLM hơn (20 so với 25), thời gian trung vị thấp hơn (10,8 so với 14,4 s/câu) và chi phí output ước tính thấp hơn ($0,023 so với $0,027); một lượt gọi LLM của I2 ở q27 mất 206,5 s ở phía cổng API (truy xuất chỉ 1,4 s), nên thời gian tối đa của I2 là 223 s. Ví dụ để trình bày: câu trả lời có bằng chứng là I2 q21 (Accuracy 93,85% [p75:1103-1885]); câu thiếu bằng chứng là I2 q27 (tìm 3 lần với LSTM, F1-score rồi từ chối); lỗi là B0 q08 trên dev (trả lời sai ý bằng đoạn tr. 74 dù citation hợp lệ về ID) và M3 q25 trên dev (trả lời câu thiếu bằng chứng). Giới hạn: test nhỏ (6 câu có đáp án, 2 câu thiếu bằng chứng) và mỗi cấu hình chỉ chạy một lần nên chưa đo được dao động của model; thứ tự gộp context của I2 không được dùng trên dev và trên test chỉ xảy ra ở 2 câu thiếu bằng chứng; nhãn chấm tay do Claude soạn nháp, học viên xác nhận; chi phí chỉ ước tính phần output vì cổng không trả số token input; README benchmark của Day 6 ghi rủi ro chủ đề gần nhau giữa dev và test (q04, q18 với q23; q08 với q24).

## Thử thách nâng cao (nếu thực hiện)

Không thực hiện (đồ án dùng làm corpus chỉ có 89 trang, chưa đủ 100 trang).

- Tài liệu, nguồn, quyền sử dụng, số trang và phiên bản:
- Cách xử lý text, bảng, ảnh, biểu đồ; phạm vi index và phần chưa xử lý:
- Cách chia benchmark, schema evidence, model và cấu hình đã chốt trên dev:

| Nhóm test | Đạt / tổng | Tỷ lệ | Lỗi / nhận xét |
|---|---|---|---|
| Bảng | | | |
| Ảnh, sơ đồ | | | |
| Biểu đồ | | | |
| Multi-hop | | | |
| Text | | | |
| Thiếu bằng chứng | | | |
| **Toàn bộ** | | | |

- Trace, nhãn và evidence từng câu; thời gian, chi phí, lỗi hệ thống:
- Giới hạn, cách tái lập và đường dẫn benchmark:
