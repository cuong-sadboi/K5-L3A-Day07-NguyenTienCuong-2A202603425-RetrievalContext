# Phiếu chấm tay agent-test-B0

Thang chấm (BENCHMARK.md §3):
- answer_grade với câu có đáp án: 0 = sai hoặc thiếu evidence; 1 = đúng một phần; 2 = đúng và đủ. Từ chối câu có đáp án chấm 0.
- citation_support: true khi đoạn được trích nằm trong context và thực sự hỗ trợ ý được trích; ID hợp lệ là chưa đủ.
- abstention_correct với câu thiếu bằng chứng: true khi agent thực sự từ chối, không thêm khẳng định vô căn cứ.
- context_score (chỉ test, ít nhất 5 câu có đáp án): 0 = không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.

## q19 · có đáp án · abstain

- Câu hỏi: Hệ thống của đề tài ưu tiên phát hiện bot hợp lệ hay bot độc hại?
- Đáp án chuẩn: Bot độc hại (bad bot traffic).
- Evidence gold (tr. 23): Đề tài tập trung chủ yếu vào việc phát hiện bad bot traffic.
- Truy vấn (2): hệ thống ưu tiên phát hiện bot hợp lệ hay bot độc hại mục tiêu phát hiện phân loại bot độc hại | đề tài ưu tiên phát hiện bot độc hại, bot hợp lệ, bot tốt, bot xấu; mục tiêu nhận diện traffic bất thường và phân loại các loại bot
- Context cuối: B:doan-bot-traffic-2026:p20:1090-1729

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q20 · có đáp án · abstain

- Câu hỏi: Khi người dùng thật bị nghi là bot vì có hành vi bất thường nhưng hợp lệ, hệ thống nên xử lý thế nào?
- Đáp án chuẩn: Không tự động chặn ngay mà đưa vào danh sách nghi ngờ để quản trị viên kiểm tra thêm.
- Evidence gold (tr. 64): hệ thống không nên tự động chặn ngay mà nên đưa vào danh sách nghi ngờ để quản trị viên kiểm tra thêm
- Truy vấn (3): người dùng thật bị nghi là bot hành vi bất thường nhưng hợp lệ hệ thống xử lý thế nào xác minh nhầm false positive | cách xử lý người dùng hợp lệ bị hệ thống phát hiện nhầm là bot false positive cho phép xác minh bổ sung giảm chặn nhầm | quy trình xử lý false positive khi người dùng thật bị phát hiện là bot: cho phép xác minh bổ sung, thử thách CAPTCHA, đánh giá lại, giảm chặn nhầm hoặc không khóa tài khoản người dùng hợp lệ
- Context cuối: B:doan-bot-traffic-2026:p15:1861-2077

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q21 · có đáp án · abstain

- Câu hỏi: Trong chương 3, mô hình Random Forest đạt Accuracy bao nhiêu trên tập kiểm thử? (filter {'chapter': 3})
- Đáp án chuẩn: Khoảng 93,85% (dự đoán đúng 1.877/2.000 mẫu).
- Evidence gold (tr. 75): mô hình dự đoán đúng 1.877/2.000 mẫu, tương ứng Accuracy khoảng 93,85%
- Evidence gold (tr. 77): Random Forest 93,85% 88,94% / 91,90%
- Truy vấn (3): Chương 3 kết quả mô hình Random Forest Accuracy độ chính xác trên tập kiểm thử test set | Chương 3 bảng kết quả đánh giá Random Forest Accuracy tập kiểm thử test accuracy độ chính xác Random Forest đạt bao nhiêu phần trăm | Chương 3 bảng kết quả Random Forest Accuracy trên tập kiểm thử giá trị Accuracy test set phần trăm
- Context cuối: B:doan-bot-traffic-2026:p76:0-642

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q22 · có đáp án · answered

- Câu hỏi: Trong chương 2, yêu cầu phi chức năng về hiệu năng quy định thời gian phản hồi API tối đa là bao lâu? (filter {'chapter': 2})
- Đáp án chuẩn: Không quá 2 giây đối với các request thông thường.
- Evidence gold (tr. 38): Thời gian phản hồi API≤2 giây đối với các request thông thường.
- Truy vấn (1): Chương 2 yêu cầu phi chức năng hiệu năng thời gian phản hồi API tối đa bao lâu
- Context cuối: B:doan-bot-traffic-2026:p38:0-535

Câu trả lời của agent:

> Thời gian phản hồi API tối đa là **2 giây** đối với các request thông thường. [B:doan-bot-traffic-2026:p38:0-535]

1. [B:doan-bot-traffic-2026:p38:0-535] (tr. 38): - Thống kê hiệu suất mô hình Machine Learning. 2.2.2. Yêu cầu phi chức năng Bên cạnh yêu cầu chức năng, hệ thống phát hiện bot traffic phải đáp ứng các yêu cầu phi chức năng sau: Hiệu năng Hệ thống phải có khả năng xử lý và ghi nhận traffic theo thời gian thực với độ trễ thấp. Thời gian phản hồi API≤2 giây đối với các request thông thường. Dashboard cập nhật dữ liệu traffic gần realtime nhằm hỗ trợ quản trị viên giám sát nhanh chóng. Hệ thống cần xử lý được nhiều request đồng thời mà không ảnh hưởng đáng kể đến hiệu năng website.

## q23 · có đáp án · answered

- Câu hỏi: So với cách phát hiện dựa trên luật, Random Forest xử lý thế nào một session có tần suất request không quá cao nhưng có các dấu hiệu khác đáng ngờ?
- Đáp án chuẩn: Kết hợp nhiều dấu hiệu yếu (interval đều, unique_pages thấp, error_rate cao) thành quyết định tổng thể nên vẫn có thể đánh dấu session đó là nghi ngờ.
- Evidence gold (tr. 77): Random Forest có thể kết hợp nhiều dấu hiệu yếu thành quyết định tổng thể, ví dụ một session không có RPM quá cao nhưng có interval đều, unique_pages thấp và error_rate cao vẫn có thể bị đánh dấu nghi ngờ.
- Truy vấn (1): Random Forest xử lý session có tần suất request không quá cao nhưng có các dấu hiệu khác đáng ngờ, so với phương pháp phát hiện dựa trên luật
- Context cuối: B:doan-bot-traffic-2026:p77:0-538

Câu trả lời của agent:

> Random Forest không chỉ dựa vào ngưỡng tần suất request. Nó kết hợp đồng thời nhiều dấu hiệu yếu—như interval đều, `unique_pages` thấp và `error_rate` cao—nên vẫn có thể đánh dấu session là đáng ngờ dù RPM không quá cao. Ngược lại, rule-based chủ yếu hiệu quả với trường hợp rõ ràng như request quá dày hoặc User-Agent chứa chuỗi bot. [B:doan-bot-traffic-2026:p77:0-538]

1. [B:doan-bot-traffic-2026:p77:0-538] (tr. 77): Random Forest 93,85% 88,94% / 91,90% Ổn định nhất trong thử nghiệm, phù hợp làm mô hình chính So với rule-based baseline, Random Forest cải thiện rõ rệt khả năng phát hiện bot do phân tích đồng thời nhiều đặc trưng. Rule-based chỉ hiệu quả với các trường hợp rõ ràng như request quá dày hoặc user-agent chứa chuỗi bot. Trong khi đó, Random Forest có thể kết hợp nhiều dấu hiệu yếu thành quyết định tổng thể, ví dụ một session không có RPM quá cao nhưng có interval đều, unique_pages thấp và error_rate cao vẫn có thể bị đánh dấu nghi ngờ.

## q24 · có đáp án · answered

- Câu hỏi: Điểm yếu đầu tiên mà đồ án tự nhận về dữ liệu thực nghiệm là gì?
- Đáp án chuẩn: Dữ liệu thực nghiệm còn hạn chế về quy mô và độ đa dạng.
- Evidence gold (tr. 85): Hạn chế đầu tiên của đề tài là dữ liệu thực nghiệm còn hạn chế về quy mô và độ đa dạng.
- Truy vấn (1): điểm yếu đầu tiên đồ án tự nhận về dữ liệu thực nghiệm hạn chế dữ liệu thực nghiệm
- Context cuối: B:doan-bot-traffic-2026:p66:1236-1583

Câu trả lời của agent:

> Điểm yếu đầu tiên là dữ liệu thực nghiệm chưa đủ lớn. [B:doan-bot-traffic-2026:p66:1236-1583]

1. [B:doan-bot-traffic-2026:p66:1236-1583] (tr. 66): Mặt hạn chế chính là dữ liệu thực nghiệm chưa đủ lớn và chưa phản ánh đầy đủ các kiểu bot tinh vi trong môi trường thực tế. Vì vậy, kết quả hiện tại nên được xem là cơ sở ban đầu. Để triển khai trong sản phẩm thật, hệ thống cần thu thập thêm dữ liệu, đánh giá trên traffic thực, bổ sung cơ chế giám sát drift và quy trình cập nhật mô hình định kỳ.

## q27 · thiếu bằng chứng · abstain

- Câu hỏi: Trong phần thực nghiệm so sánh mô hình, mô hình LSTM đạt F1-score bao nhiêu?
- Lý do thiếu bằng chứng: LSTM (cùng RNN, CNN, Transformer) chỉ được nhắc ở mục 1.3.3 (tr. 22) khi giới thiệu lý thuyết học sâu. Mục 3.20 (tr. 76–77) chỉ so sánh Random Forest với Logistic Regression, Decision Tree và Isolation Forest. Cách kiểm tra: tìm 'lstm', 'rnn', 'cnn', 'transformer', 'neural', 'mlp' trên 254 chunk index B: chỉ xuất hiện ở tr. 22, không có kết quả thực nghiệm của mô hình học sâu nào.
- Truy vấn (4): phần thực nghiệm so sánh mô hình LSTM F1-score đạt bao nhiêu giá trị F1 score | bảng so sánh mô hình thực nghiệm LSTM F1-score giá trị cụ thể Accuracy Precision Recall F1-score | "LSTM" "F1-score" bảng kết quả so sánh mô hình Accuracy Precision Recall | Trong phần thực nghiệm so sánh các mô hình, tìm bảng kết quả của mô hình LSTM và giá trị F1-score cụ thể; các chỉ số Accuracy Precision Recall F1-score của LSTM
- Context cuối: B:doan-bot-traffic-2026:p75:0-678

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q28 · thiếu bằng chứng · abstain

- Câu hỏi: Chi phí hạ tầng hằng tháng (tính bằng USD) để vận hành hệ thống trong đồ án là bao nhiêu?
- Lý do thiếu bằng chứng: Mục 3.23 (tr. 79) chỉ so sánh chi phí định tính (Bảng 3.23: hệ thống đề tài 'Thấp trong phạm vi demo', Cloudflare/Imperva 'Cao hơn, tùy gói dịch vụ'), không có con số. Các số liệu tiền tệ trong corpus chỉ là thiệt hại do ad fraud và bot trên toàn cầu (tr. 16, 26). Cách kiểm tra: đọc toàn văn mục 3.23 và tìm trên 254 chunk index B mọi con số kèm đơn vị tiền tệ (usd, đô, đồng, vnđ, triệu, nghìn, tỷ, $) cùng các từ 'máy chủ', 'vps', 'hosting', 'aws', 'azure', 'gcp', 'thuê': không có chi phí vận hành hệ thống.
- Truy vấn (2): chi phí hạ tầng hằng tháng tính bằng USD để vận hành hệ thống trong đồ án | chi phí hạ tầng hàng tháng USD vận hành hệ thống máy chủ cloud VPS database hosting đồ án số tiền cụ thể
- Context cuối: B:doan-bot-traffic-2026:p79:0-533

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


