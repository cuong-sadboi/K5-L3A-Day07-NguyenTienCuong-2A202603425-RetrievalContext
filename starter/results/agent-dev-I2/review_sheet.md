# Phiếu chấm tay agent-dev-I2

Thang chấm (BENCHMARK.md §3):
- answer_grade với câu có đáp án: 0 = sai hoặc thiếu evidence; 1 = đúng một phần; 2 = đúng và đủ. Từ chối câu có đáp án chấm 0.
- citation_support: true khi đoạn được trích nằm trong context và thực sự hỗ trợ ý được trích; ID hợp lệ là chưa đủ.
- abstention_correct với câu thiếu bằng chứng: true khi agent thực sự từ chối, không thêm khẳng định vô căn cứ.
- context_score (chỉ test, ít nhất 5 câu có đáp án): 0 = không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.

## q01 · có đáp án · answered

- Câu hỏi: Theo báo cáo Bad Bot Report 2024 của Imperva, bot traffic chiếm khoảng bao nhiêu phần trăm tổng lưu lượng Internet toàn cầu?
- Đáp án chuẩn: Khoảng 49,6%.
- Evidence gold (tr. 15): bot traffic hiện chiếm khoảng 49,6% tổng lưu lượng Internet toàn cầu
- Truy vấn (1): Theo báo cáo Imperva Bad Bot Report 2024, bot traffic chiếm khoảng bao nhiêu phần trăm tổng lưu lượng Internet toàn cầu?
- Context cuối: B:doan-bot-traffic-2026:p15:665-1185, B:doan-bot-traffic-2026:p25:605-1384, B:doan-bot-traffic-2026:p24:1798-2469

Câu trả lời của agent:

> Theo báo cáo *Bad Bot Report 2024* của Imperva, bot traffic chiếm khoảng **49,6%** tổng lưu lượng Internet toàn cầu. [B:doan-bot-traffic-2026:p15:665-1185]

1. [B:doan-bot-traffic-2026:p15:665-1185] (tr. 15): 1.1.2. Hạn chế của các phương pháp phát hiện traffic truyền thống và động lực ứng dụng Machine Learning Mặc dù các hệ thống phân tích traffic truyền thống đã được sử dụng rộng rãi trong Digital Marketing, nhiều nghiên cứu và báo cáo thực tế cho thấy các phương pháp này vẫn tồn tại nhiều hạn chế. Theo báo cáo "Bad Bot Report 2024" của Imperva, bot traffic hiện chiếm khoảng 49,6% tổng lưu lượng Internet toàn cầu, trong đó phần lớn là các bot độc hại phục vụ cho spam, scraping dữ liệu, click fraud và tấn công tự động.

## q02 · có đáp án · answered

- Câu hỏi: Theo số liệu Cloudflare năm 2024 được trích dẫn, bao nhiêu phần bot độc hại có thể giả làm trình duyệt và hành vi người dùng?
- Đáp án chuẩn: Hơn 30% bot traffic độc hại.
- Evidence gold (tr. 15): Theo thống kê của Cloudflare năm 2024, hơn 30% bot traffic độc hại có khả năng giả lập trình duyệt và hành vi người dùng
- Truy vấn (1): số liệu Cloudflare năm 2024 tỷ lệ bot độc hại giả làm trình duyệt hành vi người dùng bao nhiêu phần
- Context cuối: B:doan-bot-traffic-2026:p15:1186-1860, B:doan-bot-traffic-2026:p15:665-1185, B:doan-bot-traffic-2026:p25:605-1384

Câu trả lời của agent:

> Hơn **30% bot độc hại** có khả năng giả lập trình duyệt và hành vi người dùng. [B:doan-bot-traffic-2026:p15:1186-1860]

1. [B:doan-bot-traffic-2026:p15:1186-1860] (tr. 15): Điều này cho thấy lưu lượng truy cập không còn hoàn toàn đến từ người dùng thật, gây ảnh hưởng nghiêm trọng đến độ chính xác của dữ liệu phân tích và hiệu quả của các chiến dịch Digital Marketing. [14] Phần lớn các hệ thống hiện nay hoạt động dựa trên phương pháp rule-based detection, sử dụng các luật cố định như chặn IP, giới hạn request hoặc kiểm tra user agent để phát hiện bot traffic. Tuy nhiên, các bot hiện đại ngày càng tinh vi và có khả năng mô phỏng hành vi người dùng thật. Theo thống kê của Cloudflare năm 2024, hơn 30% bot traffic độc hại có khả năng giả lập trình duyệt và hành vi người dùng, khiến nhiều hệ thống bảo vệ truyền thống khó phát hiện chính xác.

## q03 · có đáp án · answered

- Câu hỏi: Giải pháp Cloudflare Bot Management nhận diện bot dựa vào những yếu tố nào?
- Đáp án chuẩn: Fingerprint, IP reputation và AI.
- Evidence gold (tr. 18): Hệ thống có khả năng phát hiện bot dựa trên fingerprint, IP reputation và AI.
- Truy vấn (1): Cloudflare Bot Management nhận diện bot dựa vào những yếu tố nào các tín hiệu yếu tố phân tích hành vi trình duyệt thiết bị địa chỉ IP
- Context cuối: B:doan-bot-traffic-2026:p18:933-1705, B:doan-bot-traffic-2026:p30:0-611, B:doan-bot-traffic-2026:p27:0-718

Câu trả lời của agent:

> Cloudflare Bot Management nhận diện bot dựa trên: - **Fingerprint** của client. - **Uy tín địa chỉ IP (IP reputation)**. - **Trí tuệ nhân tạo (AI)** để phân tích và phát hiện bot. [B:doan-bot-traffic-2026:p18:933-1705]

1. [B:doan-bot-traffic-2026:p18:933-1705] (tr. 18): Cloudflare Bot Management – Là giải pháp chống bot chuyên nghiệp được nhiều doanh nghiệp lớn sử dụng. Hệ thống có khả năng phát hiện bot dựa trên fingerprint, IP reputation và AI. Theo Cloudflare, hệ thống của họ xử lý hàng chục triệu request mỗi giây trên toàn cầu. Tuy nhiên, chi phí triển khai tương đối cao, yêu cầu hạ tầng phức tạp và không phù hợp với phần lớn doanh nghiệp nhỏ hoặc các dự án nghiên cứu tại Việt Nam. Imperva Advanced Bot Protection – Đây là một trong những nền tảng bảo vệ website nổi tiếng trong lĩnh vực an ninh mạng. Hệ thống sử dụng AI để phát hiện bot traffic và các hành vi bất thường. Tuy nhiên, giải pháp này chủ yếu hướng đến các doanh nghiệp lớn với chi phí triển khai và vận hành cao, khó tiếp cận đối với các hệ thống quy mô nhỏ và vừa.

## q04 · có đáp án · answered

- Câu hỏi: Thế hệ hệ thống phát hiện bot giai đoạn 2010–2016 dựa trên hướng tiếp cận nào?
- Đáp án chuẩn: Phân tích hành vi và thống kê.
- Evidence gold (tr. 24): Thế hệ thứ hai (2010–2016) – Phân tích hành vi và thống kê
- Truy vấn (1): giai đoạn 2010–2016 thế hệ hệ thống phát hiện bot hướng tiếp cận nào phương pháp phát hiện bot
- Context cuối: B:doan-bot-traffic-2026:p24:298-673, B:doan-bot-traffic-2026:p24:1195-1797, B:doan-bot-traffic-2026:p24:674-1194

Câu trả lời của agent:

> Thế hệ hệ thống phát hiện bot giai đoạn 2010–2016 dựa trên **phân tích hành vi và phân tích thống kê**, như session, mẫu click, tỷ lệ thoát và thời gian truy cập để nhận diện hành vi bất thường.[B:doan-bot-traffic-2026:p24:1195-1797]

1. [B:doan-bot-traffic-2026:p24:1195-1797] (tr. 24): Khi lượng traffic website tăng mạnh cùng sự phát triển của Digital Marketing và quảng cáo trực tuyến, các hệ thống bot detection bắt đầu sử dụng behavioral analysis và statistical analysis. Google Analytics, Cloudflare và Akamai phát triển các cơ chế phân tích session, click pattern, bounce rate và thời gian truy cập để nhận diện hành vi bất thường. Giai đoạn này xuất hiện các kỹ thuật CAPTCHA và rate limiting nhằm giảm spam bot. Tuy nhiên, các phương pháp thống kê vẫn gặp khó khăn với các bot có khả năng mô phỏng hành vi người dùng thật. Thế hệ thứ ba (2016–2022) – Machine Learning và Big Data:

## q05 · có đáp án · answered

- Câu hỏi: Ở bước tiền xử lý của quy trình phát hiện bot bằng Machine Learning, những dữ liệu nào bị loại bỏ?
- Đáp án chuẩn: Request lỗi, dữ liệu trùng lặp hoặc dữ liệu không hợp lệ.
- Evidence gold (tr. 27): dữ liệu traffic được làm sạch nhằm loại bỏ request lỗi, dữ liệu trùng lặp hoặc dữ liệu không hợp lệ
- Truy vấn (1): bước tiền xử lý quy trình phát hiện bot bằng Machine Learning dữ liệu bị loại bỏ loại bỏ dữ liệu
- Context cuối: B:doan-bot-traffic-2026:p27:719-1519, B:doan-bot-traffic-2026:p54:1418-1716, B:doan-bot-traffic-2026:p27:1520-2225

Câu trả lời của agent:

> Ở bước tiền xử lý, hệ thống loại bỏ **các request lỗi, dữ liệu trùng lặp và dữ liệu không hợp lệ**. [B:doan-bot-traffic-2026:p27:719-1519]

1. [B:doan-bot-traffic-2026:p27:719-1519] (tr. 27): 1.6.2. Quy trình hoạt động của hệ thống phát hiện bot traffic bằng Machine Learning Quy trình phát hiện bot traffic bằng Machine Learning được tổ chức thành hai giai đoạn chính, mỗi giai đoạn gồm nhiều bước xử lý tuần tự: Giai đoạn 1 – Thu thập và xử lý dữ liệu traffic (Data Processing). - Bước thứ nhất, Thu thập dữ liệu: hệ thống ghi nhận dữ liệu truy cập từ website thông qua access log, session tracking hoặc API tracking. Dữ liệu bao gồm: IP, user-agent, request URL, thời gian truy cập, thời gian giữa các request, session ID và hành vi người dùng trên website. - Bước thứ hai, Tiền xử lý dữ liệu (Preprocessing): dữ liệu traffic được làm sạch nhằm loại bỏ request lỗi, dữ liệu trùng lặp hoặc dữ liệu không hợp lệ. Sau đó hệ thống chuẩn hóa dữ liệu để phục vụ cho quá trình huấn luyện mô hình.

## q06 · có đáp án · answered

- Câu hỏi: Nhóm đặc trưng mô tả cách người dùng duyệt website gồm những chỉ số nào?
- Đáp án chuẩn: Số trang truy cập, thời gian ở lại website (session duration), chuỗi điều hướng giữa các trang và tỷ lệ thoát trang (bounce rate).
- Evidence gold (tr. 30): Đặc trưng về hành vi người dùng: số lượng trang truy cập, thời gian ở lại website (session duration), chuỗi điều hướng giữa các trang và tỷ lệ thoát trang (bounce rate).
- Truy vấn (1): nhóm đặc trưng mô tả cách người dùng duyệt website gồm những chỉ số nào các chỉ số hành vi duyệt website
- Context cuối: B:doan-bot-traffic-2026:p30:0-611, B:doan-bot-traffic-2026:p55:0-771, B:doan-bot-traffic-2026:p56:0-797

Câu trả lời của agent:

> Nhóm đặc trưng về hành vi duyệt website gồm: - Số lượng trang truy cập - Thời gian ở lại website (session duration) - Chuỗi điều hướng giữa các trang - Tỷ lệ thoát trang (bounce rate) [B:doan-bot-traffic-2026:p30:0-611]

1. [B:doan-bot-traffic-2026:p30:0-611] (tr. 30): request trên mỗi session, tốc độ gửi request, thời gian trung bình giữa hai request liên tiếp. Bot traffic thường có tần suất truy cập cao và đều bất thường so với người dùng thật. - Đặc trưng về hành vi người dùng: số lượng trang truy cập, thời gian ở lại website (session duration), chuỗi điều hướng giữa các trang và tỷ lệ thoát trang (bounce rate). Người dùng thật thường có hành vi duyệt web đa dạng hơn bot. - Đặc trưng về kỹ thuật: địa chỉ IP, user-agent, loại thiết bị, quốc gia truy cập, loại trình duyệt và hệ điều hành. Một số bot sử dụng user-agent giả hoặc thực hiện request từ nhiều IP bất thường.

## q07 · có đáp án · answered

- Câu hỏi: Trong chương 1, những bộ dữ liệu công khai nào được nêu để tham khảo và kiểm thử mô hình phát hiện bot? (filter {'chapter': 1})
- Đáp án chuẩn: CIC-IDS2017, Bot-IoT hoặc Web Server Log Dataset.
- Evidence gold (tr. 30): một số bộ dữ liệu nghiên cứu về bot detection như CIC-IDS2017, Bot-IoT hoặc Web Server Log Dataset
- Truy vấn (1): Chương 1 liệt kê những bộ dữ liệu công khai dùng để tham khảo và kiểm thử mô hình phát hiện bot
- Context cuối: B:doan-bot-traffic-2026:p27:719-1519, B:doan-bot-traffic-2026:p30:2133-2521, B:doan-bot-traffic-2026:p28:0-765

Câu trả lời của agent:

> Các bộ dữ liệu công khai được nêu là: - CIC-IDS2017 - Bot-IoT - Web Server Log Dataset [B:doan-bot-traffic-2026:p30:2133-2521]

1. [B:doan-bot-traffic-2026:p30:2133-2521] (tr. 30): - Dataset công khai: một số bộ dữ liệu nghiên cứu về bot detection như CIC-IDS2017, Bot-IoT hoặc Web Server Log Dataset được sử dụng để tham khảo và kiểm thử mô hình. Dữ liệu traffic thường có kích thước lớn và phát sinh liên tục theo thời gian thực. Vì vậy hệ thống cần cơ chế lưu trữ hiệu quả để phục vụ cho cả huấn luyện mô hình và phân tích realtime. Trong kiến trúc hệ thống đề xuất:

## q08 · có đáp án · answered

- Câu hỏi: Trong chương 3, dữ liệu thực nghiệm được lấy từ những nguồn nào? (filter {'chapter': 3})
- Đáp án chuẩn: Dữ liệu log thu thập từ request mẫu, dữ liệu đã tiền xử lý trong dataset.csv và dữ liệu mô phỏng trong synthetic_data.csv.
- Evidence gold (tr. 60): Dữ liệu thực nghiệm gồm dữ liệu log thu thập từ request mẫu, dữ liệu đã tiền xử lý trong dataset.csv và dữ liệu mô phỏng trong synthetic_data.csv.
- Truy vấn (1): Chương 3 dữ liệu thực nghiệm được lấy từ những nguồn nào nguồn dữ liệu thực nghiệm
- Context cuối: B:doan-bot-traffic-2026:p74:720-1272, B:doan-bot-traffic-2026:p73:1041-1834, B:doan-bot-traffic-2026:p66:1584-2091

Câu trả lời của agent:

> Dữ liệu thực nghiệm trong chương 3 được lấy từ hai nguồn chính: **log truy cập** và **dữ liệu mô phỏng** nhằm tạo ra hành vi của người dùng thật và bot [B:doan-bot-traffic-2026:p66:1584-2091].

1. [B:doan-bot-traffic-2026:p66:1584-2091] (tr. 66): 3.9. Phân tích dữ liệu đầu vào và chất lượng dataset Dữ liệu đầu vào quyết định trực tiếp đến độ tin cậy của mô hình phát hiện bot traffic. Trong đồ án, dữ liệu được hình thành từ log truy cập và dữ liệu mô phỏng nhằm tạo ra cả hai nhóm hành vi: người dùng thật và bot. Nhóm người dùng thật thường có thời gian phiên dài hơn, số trang truy cập đa dạng hơn và khoảng cách giữa các request không đều tuyệt đối. Ngược lại, nhóm bot thường có request lặp lại, tần suất cao hoặc user-agent chứa dấu hiệu crawler.

## q09 · có đáp án · answered

- Câu hỏi: Theo chương 1, MySQL được dùng để lưu những loại dữ liệu nào của hệ thống? (filter {'chapter': 1})
- Đáp án chuẩn: Dữ liệu traffic có cấu trúc như session, request log, thông tin người dùng và kết quả phân loại traffic.
- Evidence gold (tr. 31): MySQL được sử dụng để lưu trữ dữ liệu traffic có cấu trúc như session, request log, thông tin người dùng và kết quả phân loại traffic.
- Truy vấn (1): Chương 1 MySQL được sử dụng để lưu trữ những loại dữ liệu nào của hệ thống
- Context cuối: B:doan-bot-traffic-2026:p31:0-554, B:doan-bot-traffic-2026:p30:1383-2132, B:doan-bot-traffic-2026:p27:1520-2225

Câu trả lời của agent:

> Theo chương 1, MySQL được dùng để lưu trữ: - Dữ liệu session. - Request log. - Thông tin người dùng. - Kết quả phân loại traffic. [B:doan-bot-traffic-2026:p31:0-554]

1. [B:doan-bot-traffic-2026:p31:0-554] (tr. 31): - MySQL được sử dụng để lưu trữ dữ liệu traffic có cấu trúc như session, request log, thông tin người dùng và kết quả phân loại traffic. - MongoDB hoặc JSON log storage có thể được sử dụng cho dữ liệu log lớn, linh hoạt và thay đổi thường xuyên. - Dữ liệu sau khi thu thập sẽ được tiền xử lý và chuyển đổi thành feature dataset trước khi đưa vào pipeline Machine Learning. Ngoài việc lưu trữ, hệ thống còn cần hỗ trợ truy vấn nhanh theo thời gian, IP hoặc session để phục vụ dashboard giám sát và phân tích hành vi traffic bất thường theo thời gian thực.

## q10 · có đáp án · answered

- Câu hỏi: Trong chương 2, MySQL Database Service lưu những nhóm dữ liệu nào? (filter {'chapter': 2})
- Đáp án chuẩn: User data, traffic logs, detection results, system configuration và audit logs.
- Evidence gold (tr. 49): User data (admin, analyst, system user) - Traffic logs (request history) - Detection results (bot_score, label) - System configuration (rules, thresholds) - Audit logs
- Truy vấn (1): Chương 2 MySQL Database Service lưu những nhóm dữ liệu nào các nhóm dữ liệu được lưu trữ
- Context cuối: B:doan-bot-traffic-2026:p49:0-403, B:doan-bot-traffic-2026:p59:1348-1510, B:doan-bot-traffic-2026:p53:1402-2100

Câu trả lời của agent:

> MySQL Database Service lưu các nhóm dữ liệu: - Dữ liệu người dùng. - Nhật ký truy cập (traffic logs). - Kết quả phát hiện. - Cấu hình hệ thống. - Nhật ký kiểm toán (audit logs). [B:doan-bot-traffic-2026:p49:0-403]

1. [B:doan-bot-traffic-2026:p49:0-403] (tr. 49): 2.3.5. MySQL Database Service Hệ thống sử dụng MySQL để lưu trữ dữ liệu chính. Các nhóm dữ liệu: - User data (admin, analyst, system user) - Traffic logs (request history) - Detection results (bot_score, label) - System configuration (rules, thresholds) - Audit logs Thiết kế tối ưu: - Partition bảng traffic_logs theo ngày/tháng - Index theo IP, session_id, timestamp - Sử dụng read replica nếu tải lớn

## q11 · có đáp án · answered

- Câu hỏi: Trong chương 2, kết quả phân loại traffic đầu ra của hệ thống gồm những nhãn nào? (filter {'chapter': 2})
- Đáp án chuẩn: Người dùng thật (real user), bot hợp lệ (good bot) hoặc bot bất thường (malicious bot).
- Evidence gold (tr. 35): Kết quả phân loại traffic gồm người dùng thật (real user), bot hợp lệ (good bot) hoặc bot bất thường (malicious bot)
- Truy vấn (1): Chương 2 kết quả phân loại traffic đầu ra của hệ thống gồm những nhãn nào các nhãn phân loại traffic
- Context cuối: B:doan-bot-traffic-2026:p35:1496-1925, B:doan-bot-traffic-2026:p43:1551-1864, B:doan-bot-traffic-2026:p54:0-799

Câu trả lời của agent:

> Kết quả phân loại traffic gồm các nhãn: - Người dùng thật (real user) - Bot hợp lệ (good bot) - Bot bất thường (malicious bot) [B:doan-bot-traffic-2026:p35:1496-1925]

1. [B:doan-bot-traffic-2026:p35:1496-1925] (tr. 35): - Các thông tin kỹ thuật như IP address, user-agent, HTTP method, request URL, response status và thời gian truy cập. Đầu ra của hệ thống: - Kết quả phân loại traffic gồm người dùng thật (real user), bot hợp lệ (good bot) hoặc bot bất thường (malicious bot); - Dashboard hiển thị thống kê traffic, session và cảnh báo các truy cập bất thường theo thời gian thực; - Báo cáo phân tích traffic phục vụ quản trị và giám sát hệ thống.

## q12 · có đáp án · answered

- Câu hỏi: Endpoint nào của Traffic Collection API dùng để thu thập dữ liệu request?
- Đáp án chuẩn: POST /v1/collect.
- Evidence gold (tr. 47): POST /v1/collect– Thu thập request data
- Truy vấn (1): Traffic Collection API endpoint thu thập dữ liệu request endpoint nào dùng để collect request data
- Context cuối: B:doan-bot-traffic-2026:p47:775-1333, B:doan-bot-traffic-2026:p52:1623-1832, B:doan-bot-traffic-2026:p31:1986-2358

Câu trả lời của agent:

> Endpoint dùng để thu thập dữ liệu request là **POST `/v1/collect`**. [B:doan-bot-traffic-2026:p47:775-1333]

1. [B:doan-bot-traffic-2026:p47:775-1333] (tr. 47): 2.3.3. Traffic Collection API (Golang RESTful API) Traffic Collection API được xây dựng bằng Golang nhằm đảm bảo hiệu năng cao trong việc thu thập request realtime. Chức năng chính: - Nhận toàn bộ HTTP requests từ client hoặc proxy layer. - Ghi nhận thông tin: IP, user-agent, headers, payload metadata. - Gán session_id và request_id cho từng request. - Forward dữ liệu sang AI/ML Service để phân tích. - Stream dữ liệu sang Kafka/queue (nếu mở rộng hệ thống). API chính: -POST /v1/collect– Thu thập request data -GET /v1/health– Kiểm tra trạng thái service

## q13 · có đáp án · answered

- Câu hỏi: Trong luồng phân tích, khi nào hệ thống ghi nhận một cảnh báo bot và lưu ở đâu?
- Đáp án chuẩn: Khi xác suất bot vượt ngưỡng cấu hình; cảnh báo được ghi vào bảng bot_detection_results và hiển thị trên dashboard.
- Evidence gold (tr. 53): Nếu xác suất bot vượt ngưỡng cấu hình, hệ thống ghi nhận cảnh báo vào bảng bot_detection_results và hiển thị trên dashboard.
- Truy vấn (1): luồng phân tích khi nào hệ thống ghi nhận cảnh báo bot và cảnh báo bot được lưu ở đâu
- Context cuối: B:doan-bot-traffic-2026:p53:329-836, B:doan-bot-traffic-2026:p50:0-252, B:doan-bot-traffic-2026:p44:0-644

Câu trả lời của agent:

> Hệ thống ghi nhận cảnh báo khi dữ liệu session đã đủ, được phân tích bằng AI và xác suất là bot vượt ngưỡng cấu hình. Cảnh báo được lưu trong bảng `bot_detection_results` và hiển thị trên dashboard. [B:doan-bot-traffic-2026:p53:329-836]

1. [B:doan-bot-traffic-2026:p53:329-836] (tr. 53): 2.4.3. Luồng phân tích và cảnh báo bot traffic Backend lấy dữ liệu session đã đủ thông tin, tạo vector đặc trưng và gửi sang AI Service. AI Service nạp model đã huấn luyện, dự đoán nhãn và trả về xác suất bot. Nếu xác suất bot vượt ngưỡng cấu hình, hệ thống ghi nhận cảnh báo vào bảng bot_detection_results và hiển thị trên dashboard. Cảnh báo không chỉ gồm nhãn phân loại mà còn bao gồm các đặc trưng quan trọng như requests_per_minute, unique_pages và average_interval để người quản trị có cơ sở kiểm tra.

## q14 · có đáp án · answered

- Câu hỏi: Trường ip_address được thiết kế với kiểu dữ liệu nào và nhằm hỗ trợ điều gì?
- Đáp án chuẩn: VARCHAR(45), để hỗ trợ cả IPv4 và IPv6.
- Evidence gold (tr. 54): ip_address Địa chỉ IP truy cập VARCHAR(45) Hỗ trợ IPv4/IPv6
- Truy vấn (1): Trường ip_address được thiết kế với kiểu dữ liệu nào và nhằm hỗ trợ điều gì trong đồ án
- Context cuối: B:doan-bot-traffic-2026:p68:1453-1954, B:doan-bot-traffic-2026:p54:0-799, B:doan-bot-traffic-2026:p54:800-1417

Câu trả lời của agent:

> Trường `ip_address` được thiết kế với kiểu dữ liệu `VARCHAR(45)`, nhằm hỗ trợ lưu cả địa chỉ IPv4 và IPv6. [B:doan-bot-traffic-2026:p54:0-799]

1. [B:doan-bot-traffic-2026:p54:0-799] (tr. 54): Traffic log traffic_logs, sessions Lưu request, IP, user-agent, URL và thông tin phiên traffic_logs.session_id liên kết sessions.id Kết quả ML ml_features, bot_detection_results Lưu vector đặc trưng, nhãn dự đoán và xác suất bot ml_features.session_id liên kết bot_detection_results.session_id Cảnh báo/báo cáo alerts, reports Theo dõi IP/session đáng ngờ và báo cáo tổng hợp alerts.result_id liên kết bot_detection_results.id Bảng 2.12.Các trường dữ liệu traffic quan trọng Tên trường Ý nghĩa Kiểu dữ liệu gợi ý Ghi chú xử lý ip_address Địa chỉ IP truy cập VARCHAR(45) Hỗ trợ IPv4/IPv6 user_agent Chuỗi nhận dạng trình duyệt/bot TEXT Trích xuất browser, OS và dấu hiệu bot request_url URL được truy cập TEXT Dùng để phân tích đường dẫn bất thường timestamp Thời điểm request DATETIME Cần index theo

## q15 · có đáp án · answered

- Câu hỏi: Vì sao pipeline Machine Learning lưu dữ liệu thô tách biệt với kết quả dự đoán?
- Đáp án chuẩn: Dữ liệu thô phục vụ truy vết và huấn luyện lại, còn kết quả dự đoán phục vụ cảnh báo và báo cáo.
- Evidence gold (tr. 55): Dữ liệu thô phục vụ truy vết và huấn luyện lại, còn kết quả dự đoán phục vụ cảnh báo và báo cáo.
- Evidence gold (tr. 54): không ghi đè log gốc mà được lưu riêng nhằm bảo toàn dữ liệu thô cho quá trình huấn luyện lại sau này
- Truy vấn (1): pipeline Machine Learning vì sao lưu dữ liệu thô tách biệt với kết quả dự đoán mục đích lưu trữ dữ liệu raw prediction kết quả dự đoán
- Context cuối: B:doan-bot-traffic-2026:p55:772-1371, B:doan-bot-traffic-2026:p73:1041-1834, B:doan-bot-traffic-2026:p54:1418-1716

Câu trả lời của agent:

> Pipeline lưu dữ liệu thô tách biệt với kết quả dự đoán vì: - Dữ liệu thô cần được giữ lại để **truy vết và huấn luyện lại mô hình**. - Kết quả dự đoán phục vụ **cảnh báo và báo cáo**, có mục đích sử dụng khác với dữ liệu gốc. - Cách tách biệt giúp hệ thống **dễ kiểm tra, mở rộng**, phát hiện sai lệch khi kết quả bất thường và không làm mất dữ liệu gốc khi cập nhật mô hình. [B:doan-bot-traffic-2026:p55:772-1371] [B:doan-bot-traffic-2026:p73:1041-1834]

1. [B:doan-bot-traffic-2026:p55:772-1371] (tr. 55): Mô hình Random Forest được huấn luyện trên tập dữ liệu sau tiền xử lý. Khi có traffic mới, Backend tạo vector đặc trưng theo đúng thứ tự đã dùng lúc huấn luyện và gửi sang AI Service. AI Service trả về nhãn dự đoán, xác suất bot và confidence để lưu vào database và hiển thị trên dashboard. Một điểm quan trọng trong thiết kế pipeline là dữ liệu thô và kết quả dự đoán được lưu tách biệt. Dữ liệu thô phục vụ truy vết và huấn luyện lại, còn kết quả dự đoán phục vụ cảnh báo và báo cáo. Cách tách này giúp hệ thống dễ kiểm tra, dễ mở rộng và tránh làm mất nguồn dữ liệu gốc khi mô hình được cập nhật.
2. [B:doan-bot-traffic-2026:p73:1041-1834] (tr. 73): 3.17. Bài học rút ra từ quá trình thực nghiệm Quá trình thực nghiệm cho thấy việc xây dựng hệ thống phát hiện bot traffic không thể tách rời giữa kỹ thuật phần mềm và Machine Learning. Nếu chỉ có mô hình tốt nhưng pipeline dữ liệu thiếu ổn định, kết quả dự đoán sẽ không đáng tin cậy. Ngược lại, nếu hệ thống thu thập và lưu trữ dữ liệu tốt nhưng feature chưa phản ánh đúng hành vi truy cập, mô hình cũng khó phát hiện chính xác bot traffic. Bài học quan trọng nhất là cần thiết kế dữ liệu ngay từ đầu theo mục tiêu phân tích. Các trường như session_id, timestamp, request_url, user_agent và http_status phải được ghi nhất quán để có thể tính feature về sau. Ngoài ra, việc lưu riêng dữ liệu thô, dữ liệu feature và kết quả dự đoán giúp hệ thống dễ kiểm tra sai lệch khi có kết quả bất thường.

## q16 · có đáp án · answered

- Câu hỏi: Sau khi đăng nhập, người dùng dùng gì để gọi các API cần bảo vệ?
- Đáp án chuẩn: Access token được cấp sau khi đăng nhập.
- Evidence gold (tr. 57): Sau khi đăng nhập, người dùng nhận access token để gọi các API
- Evidence gold (tr. 49): JWT (access token + refresh token)
- Truy vấn (1): Sau khi đăng nhập, người dùng sử dụng gì để gọi các API cần bảo vệ? Cơ chế xác thực, token, JWT, Bearer token trong header khi truy cập API bảo vệ
- Context cuối: B:doan-bot-traffic-2026:p57:2606-2763, B:doan-bot-traffic-2026:p51:0-286, B:doan-bot-traffic-2026:p49:404-773

Câu trả lời của agent:

> Sau khi đăng nhập, người dùng dùng **JWT access token** để gọi các API cần bảo vệ. [B:doan-bot-traffic-2026:p57:2606-2763]

1. [B:doan-bot-traffic-2026:p57:2606-2763] (tr. 57): JWT được lựa chọn cho cơ chế xác thực vì phù hợp với mô hình web API tách frontend và backend. Sau khi đăng nhập, người dùng nhận access token để gọi các API

## q17 · có đáp án · answered

- Câu hỏi: Theo chương 1, nếu AI Service tạm thời gặp lỗi thì hệ thống theo kiến trúc Microservice vẫn hoạt động ra sao? (filter {'chapter': 1})
- Đáp án chuẩn: Vẫn tiếp tục thu thập log và lưu dữ liệu thô để phân tích lại sau; các thành phần còn lại không bị dừng toàn bộ.
- Evidence gold (tr. 32): nếu AI Service tạm thời gặp lỗi, hệ thống vẫn có thể tiếp tục thu thập log và lưu dữ liệu thô để phân tích lại sau; các thành phần còn lại không bị dừng toàn bộ
- Truy vấn (1): Chương 1 kiến trúc Microservice AI Service tạm thời gặp lỗi hệ thống vẫn hoạt động ra sao cơ chế chịu lỗi fallback circuit breaker
- Context cuối: B:doan-bot-traffic-2026:p33:734-1404, B:doan-bot-traffic-2026:p31:1337-1985, B:doan-bot-traffic-2026:p32:1705-1933

Câu trả lời của agent:

> Nếu AI Service tạm thời gặp sự cố, các service khác như Backend, Frontend, Dashboard hoặc API Gateway vẫn có thể tiếp tục hoạt động độc lập, vì hệ thống được thiết kế theo nguyên tắc “Design for Failure” và triển khai độc lập giữa các service. [B:doan-bot-traffic-2026:p31:1337-1985] Tuy nhiên, chức năng phát hiện bot do AI Service đảm nhiệm sẽ tạm thời bị gián đoạn.

1. [B:doan-bot-traffic-2026:p31:1337-1985] (tr. 31): - Triển khai độc lập (Independent Deployment) – cập nhật một service không ảnh hưởng đến các service khác; - Thiết kế cho sự thất bại (Design for Failure) – hệ thống phải hoạt động được ngay cả khi một service gặp sự cố. So sánh Monolithic vs Microservice: Trong kiến trúc Monolithic, toàn bộ ứng dụng là một khối thống nhất, dễ phát triển ở giai đoạn đầu nhưng khó mở rộng và bảo trì khi số lượng chức năng tăng. Microservice giải quyết vấn đề này bằng cách chia hệ thống thành các service nhỏ, mỗi service đảm nhiệm một nhóm chức năng riêng. Đối với hệ thống phân tích log và phát hiện traffic bất thường, kiến trúc Microservice được lựa chọn vì:

## q18 · có đáp án · answered

- Câu hỏi: Khi kiểm tra tự động phát hiện dữ liệu bị lệch mạnh, hệ thống cần làm gì trước khi huấn luyện lại mô hình?
- Đáp án chuẩn: Cảnh báo để người phát triển kiểm tra trước khi dùng dữ liệu đó huấn luyện lại mô hình.
- Evidence gold (tr. 71): Khi phát hiện dữ liệu lệch mạnh, hệ thống cần cảnh báo để người phát triển kiểm tra trước khi dùng dữ liệu đó huấn luyện lại mô hình.
- Truy vấn (1): Khi kiểm tra tự động phát hiện dữ liệu bị lệch mạnh, hệ thống cần làm gì trước khi huấn luyện lại mô hình? Quy trình xử lý cảnh báo dữ liệu lệch, kiểm tra xác nhận và hành động trước retrain mô hình.
- Context cuối: B:doan-bot-traffic-2026:p71:985-1401, B:doan-bot-traffic-2026:p71:0-527, B:doan-bot-traffic-2026:p67:0-348

Câu trả lời của agent:

> Hệ thống cần cảnh báo để người phát triển kiểm tra dữ liệu trước khi sử dụng dữ liệu đó để huấn luyện lại mô hình. [B:doan-bot-traffic-2026:p71:985-1401]

1. [B:doan-bot-traffic-2026:p71:985-1401] (tr. 71): Biện pháp kiểm soát phù hợp là xây dựng các kiểm tra dữ liệu tự động trước khi huấn luyện mô hình. Các kiểm tra này bao gồm tỷ lệ thiếu dữ liệu, phân phối của từng feature, tỷ lệ nhãn bot/real, số lượng session quá ngắn, số request trùng lặp và sự thay đổi bất thường giữa các ngày. Khi phát hiện dữ liệu lệch mạnh, hệ thống cần cảnh báo để người phát triển kiểm tra trước khi dùng dữ liệu đó huấn luyện lại mô hình.

## q25 · thiếu bằng chứng · abstain

- Câu hỏi: Theo đồ án, bot traffic chiếm khoảng bao nhiêu phần trăm lưu lượng truy cập của các website tại Việt Nam?
- Lý do thiếu bằng chứng: Mục 1.1.3 (tr. 17) chỉ nêu số liệu Việt Nam về người dùng Internet (hơn 78 triệu, trên 79% dân số, DataReportal 2024) và nhận định doanh nghiệp Việt Nam còn thiếu giải pháp phát hiện bot; tỷ lệ bot traffic chỉ có ở mức toàn cầu (gần 50% ở tr. 17; 49,6% theo Imperva ở tr. 15). Cách kiểm tra: đọc toàn văn mục 1.1.3 và tìm mọi câu chứa 'Việt Nam' kèm '%' hoặc 'bot' trên 254 chunk index B: không có tỷ lệ bot traffic riêng cho Việt Nam.
- Truy vấn (1): bot traffic chiếm khoảng bao nhiêu phần trăm lưu lượng truy cập của các website tại Việt Nam
- Context cuối: B:doan-bot-traffic-2026:p17:1134-1770, B:doan-bot-traffic-2026:p17:584-1133, B:doan-bot-traffic-2026:p15:665-1185

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q26 · thiếu bằng chứng · abstain

- Câu hỏi: Đồ án nêu hệ thống phải tuân thủ văn bản pháp lý nào về bảo vệ dữ liệu cá nhân (ví dụ GDPR hoặc Nghị định 13/2023/NĐ-CP) khi lưu IP và user-agent của người truy cập?
- Lý do thiếu bằng chứng: Mục 3.11 (tr. 68–69) chỉ nêu biện pháp kỹ thuật (API key, phân quyền, RBAC, đặt AI Service trong mạng nội bộ, sao lưu định kỳ) và khuyến nghị chỉ dùng IP cho mục tiêu an ninh và phân tích traffic; không nêu văn bản pháp lý nào. Cách kiểm tra: đọc toàn văn mục 3.11 và tìm trên 254 chunk index B các từ 'GDPR', 'nghị định', '13/2023', 'dữ liệu cá nhân', 'pháp lý', 'tuân thủ', 'quyền riêng tư', 'privacy', 'consent', 'cookie': 0 kết quả; mọi lần xuất hiện 'luật' (18 chunk) đều mang nghĩa luật phát hiện (rule-based) hoặc luật phân tách của Decision Tree.
- Truy vấn (1): Đồ án nêu văn bản pháp lý về bảo vệ dữ liệu cá nhân khi hệ thống lưu địa chỉ IP và user-agent của người truy cập, GDPR, Nghị định 13/2023/NĐ-CP
- Context cuối: B:doan-bot-traffic-2026:p68:1453-1954, B:doan-bot-traffic-2026:p71:1402-2084, B:doan-bot-traffic-2026:p52:1079-1622

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


