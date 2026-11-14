# Phiếu chấm tay agent-test-I2

Thang chấm (BENCHMARK.md §3):
- answer_grade với câu có đáp án: 0 = sai hoặc thiếu evidence; 1 = đúng một phần; 2 = đúng và đủ. Từ chối câu có đáp án chấm 0.
- citation_support: true khi đoạn được trích nằm trong context và thực sự hỗ trợ ý được trích; ID hợp lệ là chưa đủ.
- abstention_correct với câu thiếu bằng chứng: true khi agent thực sự từ chối, không thêm khẳng định vô căn cứ.
- context_score (chỉ test, ít nhất 5 câu có đáp án): 0 = không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.

## q19 · có đáp án · answered

- Câu hỏi: Hệ thống của đề tài ưu tiên phát hiện bot hợp lệ hay bot độc hại?
- Đáp án chuẩn: Bot độc hại (bad bot traffic).
- Evidence gold (tr. 23): Đề tài tập trung chủ yếu vào việc phát hiện bad bot traffic.
- Truy vấn (1): Hệ thống của đề tài ưu tiên phát hiện bot hợp lệ hay bot độc hại mục tiêu phân loại nhận diện bot độc hại bot hợp lệ
- Context cuối: B:doan-bot-traffic-2026:p79:534-1329, B:doan-bot-traffic-2026:p11:1655-2291, B:doan-bot-traffic-2026:p23:1304-2006

Câu trả lời của agent:

> Hệ thống ưu tiên phát hiện **bot độc hại (Bad Bot)**, dù vẫn phân loại được bot hợp lệ và bot độc hại. [B:doan-bot-traffic-2026:p23:1304-2006]

1. [B:doan-bot-traffic-2026:p23:1304-2006] (tr. 23): 1.5. Tổng quan về Machine Learning và phát hiện traffic bất thường 1.5.1. Khái niệm và phân loại Bot Traffic Hệ thống phát hiện bot traffic là một hệ thống phần mềm có khả năng phân tích hành vi truy cập của người dùng nhằm nhận diện và phân loại lưu lượng truy cập bất thường hoặc tự động (bot traffic). Theo nhiều nghiên cứu trong lĩnh vực Cybersecurity và Web Analytics, bot traffic có thể được phân loại theo nhiều tiêu chí khác nhau: - Theo mục đích hoạt động: Good Bot (bot hợp lệ như Googlebot, Bingbot phục vụ lập chỉ mục tìm kiếm) và Bad Bot (bot độc hại dùng để spam, click ảo quảng cáo, crawling trái phép hoặc tấn công hệ thống). Đề tài tập trung chủ yếu vào việc phát hiện bad bot traffic.

## q20 · có đáp án · answered

- Câu hỏi: Khi người dùng thật bị nghi là bot vì có hành vi bất thường nhưng hợp lệ, hệ thống nên xử lý thế nào?
- Đáp án chuẩn: Không tự động chặn ngay mà đưa vào danh sách nghi ngờ để quản trị viên kiểm tra thêm.
- Evidence gold (tr. 64): hệ thống không nên tự động chặn ngay mà nên đưa vào danh sách nghi ngờ để quản trị viên kiểm tra thêm
- Truy vấn (1): người dùng thật bị nghi là bot hành vi bất thường nhưng hợp lệ hệ thống xử lý thế nào xác minh bổ sung false positive
- Context cuối: B:doan-bot-traffic-2026:p64:0-662, B:doan-bot-traffic-2026:p64:663-1110, B:doan-bot-traffic-2026:p15:1861-2077

Câu trả lời của agent:

> Hệ thống không nên tự động chặn ngay. Thay vào đó, cần đưa người dùng vào danh sách nghi ngờ để quản trị viên kiểm tra thêm, đồng thời hiển thị mức độ tin cậy và các đặc trưng hành vi nổi bật để giảm nguy cơ xử lý nhầm [B:doan-bot-traffic-2026:p64:0-662].

1. [B:doan-bot-traffic-2026:p64:0-662] (tr. 64): là bot. Trường hợp này ảnh hưởng trực tiếp đến trải nghiệm người dùng và có thể khiến doanh nghiệp bỏ qua traffic hợp lệ. False negative xảy ra khi bot bị dự đoán là người dùng thật, làm dữ liệu thống kê tiếp tục bị nhiễu và ảnh hưởng đến quyết định marketing. Các false positive thường xuất hiện khi người dùng thật có hành vi bất thường nhưng hợp lệ, ví dụ tải lại trang liên tục, mở nhiều tab trong thời gian ngắn hoặc truy cập qua mạng có IP dùng chung. Trong trường hợp này, hệ thống không nên tự động chặn ngay mà nên đưa vào danh sách nghi ngờ để quản trị viên kiểm tra thêm. Việc hiển thị confidence và feature nổi bật giúp giảm rủi ro ra quyết định sai.

## q21 · có đáp án · answered

- Câu hỏi: Trong chương 3, mô hình Random Forest đạt Accuracy bao nhiêu trên tập kiểm thử? (filter {'chapter': 3})
- Đáp án chuẩn: Khoảng 93,85% (dự đoán đúng 1.877/2.000 mẫu).
- Evidence gold (tr. 75): mô hình dự đoán đúng 1.877/2.000 mẫu, tương ứng Accuracy khoảng 93,85%
- Evidence gold (tr. 77): Random Forest 93,85% 88,94% / 91,90%
- Truy vấn (1): Chương 3 mô hình Random Forest Accuracy trên tập kiểm thử đạt bao nhiêu phần trăm
- Context cuối: B:doan-bot-traffic-2026:p75:1103-1885, B:doan-bot-traffic-2026:p76:0-642, B:doan-bot-traffic-2026:p75:0-678

Câu trả lời của agent:

> Mô hình Random Forest đạt Accuracy **93,85%** trên tập kiểm thử. [B:doan-bot-traffic-2026:p75:1103-1885]

1. [B:doan-bot-traffic-2026:p75:1103-1885] (tr. 75): Bảng 3.18.Ma trận nhầm lẫn trên tập kiểm thử 2.000 session Thực tế / Dự đoán Dự đoán Real Dự đoán Bot Tổng Real traffic 1.298 72 1.370 Bot traffic 51 579 630 Tổng 1.349 651 2.000 Từ ma trận trên, mô hình dự đoán đúng 1.877/2.000 mẫu, tương ứng Accuracy khoảng 93,85%. Với lớp bot, Precision đạt khoảng 88,94%, nghĩa là trong các session bị đánh dấu là bot, phần lớn thực sự có hành vi bất thường. Recall của lớp bot đạt khoảng 91,90%, cho thấy mô hình phát hiện được đa số bot trong tập kiểm thử. F1-score của lớp bot đạt khoảng 90,40%, thể hiện sự cân bằng tương đối tốt giữa khả năng phát hiện bot và hạn chế cảnh báo nhầm. Bảng 3.19.Tổng hợp chỉ số đánh giá mô hình Random Forest Chỉ số Giá trị Ý nghĩa trong hệ thống Accuracy 93,85% Tỷ lệ dự đoán đúng tổng thể trên tập kiểm thử

## q22 · có đáp án · answered

- Câu hỏi: Trong chương 2, yêu cầu phi chức năng về hiệu năng quy định thời gian phản hồi API tối đa là bao lâu? (filter {'chapter': 2})
- Đáp án chuẩn: Không quá 2 giây đối với các request thông thường.
- Evidence gold (tr. 38): Thời gian phản hồi API≤2 giây đối với các request thông thường.
- Truy vấn (1): Chương 2 yêu cầu phi chức năng hiệu năng thời gian phản hồi API tối đa bao lâu
- Context cuối: B:doan-bot-traffic-2026:p38:0-535, B:doan-bot-traffic-2026:p53:0-328, B:doan-bot-traffic-2026:p56:0-797

Câu trả lời của agent:

> Thời gian phản hồi API tối đa là **2 giây** đối với các request thông thường. [B:doan-bot-traffic-2026:p38:0-535]

1. [B:doan-bot-traffic-2026:p38:0-535] (tr. 38): - Thống kê hiệu suất mô hình Machine Learning. 2.2.2. Yêu cầu phi chức năng Bên cạnh yêu cầu chức năng, hệ thống phát hiện bot traffic phải đáp ứng các yêu cầu phi chức năng sau: Hiệu năng Hệ thống phải có khả năng xử lý và ghi nhận traffic theo thời gian thực với độ trễ thấp. Thời gian phản hồi API≤2 giây đối với các request thông thường. Dashboard cập nhật dữ liệu traffic gần realtime nhằm hỗ trợ quản trị viên giám sát nhanh chóng. Hệ thống cần xử lý được nhiều request đồng thời mà không ảnh hưởng đáng kể đến hiệu năng website.

## q23 · có đáp án · answered

- Câu hỏi: So với cách phát hiện dựa trên luật, Random Forest xử lý thế nào một session có tần suất request không quá cao nhưng có các dấu hiệu khác đáng ngờ?
- Đáp án chuẩn: Kết hợp nhiều dấu hiệu yếu (interval đều, unique_pages thấp, error_rate cao) thành quyết định tổng thể nên vẫn có thể đánh dấu session đó là nghi ngờ.
- Evidence gold (tr. 77): Random Forest có thể kết hợp nhiều dấu hiệu yếu thành quyết định tổng thể, ví dụ một session không có RPM quá cao nhưng có interval đều, unique_pages thấp và error_rate cao vẫn có thể bị đánh dấu nghi ngờ.
- Truy vấn (1): Random Forest xử lý session tần suất request không cao nhưng có các dấu hiệu khác đáng ngờ so với phát hiện dựa trên luật
- Context cuối: B:doan-bot-traffic-2026:p77:0-538, B:doan-bot-traffic-2026:p77:960-1649, B:doan-bot-traffic-2026:p63:0-783

Câu trả lời của agent:

> So với rule-based chỉ phát hiện tốt các trường hợp rõ ràng như request quá dày hoặc User-Agent chứa chuỗi bot, Random Forest phân tích đồng thời nhiều đặc trưng. Vì vậy, một session dù không có RPM cao nhưng có khoảng cách request đều, ít trang truy cập và tỷ lệ lỗi cao vẫn có thể bị đánh dấu đáng ngờ [B:doan-bot-traffic-2026:p77:0-538].

1. [B:doan-bot-traffic-2026:p77:0-538] (tr. 77): Random Forest 93,85% 88,94% / 91,90% Ổn định nhất trong thử nghiệm, phù hợp làm mô hình chính So với rule-based baseline, Random Forest cải thiện rõ rệt khả năng phát hiện bot do phân tích đồng thời nhiều đặc trưng. Rule-based chỉ hiệu quả với các trường hợp rõ ràng như request quá dày hoặc user-agent chứa chuỗi bot. Trong khi đó, Random Forest có thể kết hợp nhiều dấu hiệu yếu thành quyết định tổng thể, ví dụ một session không có RPM quá cao nhưng có interval đều, unique_pages thấp và error_rate cao vẫn có thể bị đánh dấu nghi ngờ.

## q24 · có đáp án · answered

- Câu hỏi: Điểm yếu đầu tiên mà đồ án tự nhận về dữ liệu thực nghiệm là gì?
- Đáp án chuẩn: Dữ liệu thực nghiệm còn hạn chế về quy mô và độ đa dạng.
- Evidence gold (tr. 85): Hạn chế đầu tiên của đề tài là dữ liệu thực nghiệm còn hạn chế về quy mô và độ đa dạng.
- Truy vấn (1): điểm yếu đầu tiên đồ án tự nhận về dữ liệu thực nghiệm hạn chế dữ liệu thực nghiệm
- Context cuối: B:doan-bot-traffic-2026:p66:1236-1583, B:doan-bot-traffic-2026:p69:0-480, B:doan-bot-traffic-2026:p85:1651-2425

Câu trả lời của agent:

> Điểm yếu đầu tiên là dữ liệu thực nghiệm chưa đủ lớn và chưa phản ánh đầy đủ các kiểu bot tinh vi trong môi trường thực tế. [B:doan-bot-traffic-2026:p66:1236-1583]

1. [B:doan-bot-traffic-2026:p66:1236-1583] (tr. 66): Mặt hạn chế chính là dữ liệu thực nghiệm chưa đủ lớn và chưa phản ánh đầy đủ các kiểu bot tinh vi trong môi trường thực tế. Vì vậy, kết quả hiện tại nên được xem là cơ sở ban đầu. Để triển khai trong sản phẩm thật, hệ thống cần thu thập thêm dữ liệu, đánh giá trên traffic thực, bổ sung cơ chế giám sát drift và quy trình cập nhật mô hình định kỳ.

## q27 · thiếu bằng chứng · abstain

- Câu hỏi: Trong phần thực nghiệm so sánh mô hình, mô hình LSTM đạt F1-score bao nhiêu?
- Lý do thiếu bằng chứng: LSTM (cùng RNN, CNN, Transformer) chỉ được nhắc ở mục 1.3.3 (tr. 22) khi giới thiệu lý thuyết học sâu. Mục 3.20 (tr. 76–77) chỉ so sánh Random Forest với Logistic Regression, Decision Tree và Isolation Forest. Cách kiểm tra: tìm 'lstm', 'rnn', 'cnn', 'transformer', 'neural', 'mlp' trên 254 chunk index B: chỉ xuất hiện ở tr. 22, không có kết quả thực nghiệm của mô hình học sâu nào.
- Truy vấn (3): phần thực nghiệm so sánh các mô hình LSTM đạt F1-score bao nhiêu giá trị F1 score | Trong phần thực nghiệm so sánh mô hình, bảng kết quả có mô hình LSTM và chỉ số F1-score của LSTM là bao nhiêu | Trong phần thực nghiệm so sánh các mô hình, tìm bảng kết quả có mô hình LSTM và giá trị F1-score tương ứng của LSTM.
- Context cuối: B:doan-bot-traffic-2026:p23:702-1303, B:doan-bot-traffic-2026:p63:1284-1953, B:doan-bot-traffic-2026:p74:0-719

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q28 · thiếu bằng chứng · abstain

- Câu hỏi: Chi phí hạ tầng hằng tháng (tính bằng USD) để vận hành hệ thống trong đồ án là bao nhiêu?
- Lý do thiếu bằng chứng: Mục 3.23 (tr. 79) chỉ so sánh chi phí định tính (Bảng 3.23: hệ thống đề tài 'Thấp trong phạm vi demo', Cloudflare/Imperva 'Cao hơn, tùy gói dịch vụ'), không có con số. Các số liệu tiền tệ trong corpus chỉ là thiệt hại do ad fraud và bot trên toàn cầu (tr. 16, 26). Cách kiểm tra: đọc toàn văn mục 3.23 và tìm trên 254 chunk index B mọi con số kèm đơn vị tiền tệ (usd, đô, đồng, vnđ, triệu, nghìn, tỷ, $) cùng các từ 'máy chủ', 'vps', 'hosting', 'aws', 'azure', 'gcp', 'thuê': không có chi phí vận hành hệ thống.
- Truy vấn (3): chi phí hạ tầng hằng tháng USD vận hành hệ thống đồ án tổng chi phí hàng tháng | Bảng chi phí hạ tầng hàng tháng vận hành hệ thống USD máy chủ VPS cloud database frontend backend AI service tổng cộng mỗi tháng | chi phí vận hành triển khai hạ tầng hàng tháng bằng USD hệ thống đồ án VPS máy chủ cloud MySQL Docker Frontend Backend AI API tổng cộng USD/tháng
- Context cuối: B:doan-bot-traffic-2026:p60:1220-1969, B:doan-bot-traffic-2026:p62:1525-2204, B:doan-bot-traffic-2026:p33:0-733

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


