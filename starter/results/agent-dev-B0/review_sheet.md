# Phiếu chấm tay agent-dev-B0

Thang chấm (BENCHMARK.md §3):
- answer_grade với câu có đáp án: 0 = sai hoặc thiếu evidence; 1 = đúng một phần; 2 = đúng và đủ. Từ chối câu có đáp án chấm 0.
- citation_support: true khi đoạn được trích nằm trong context và thực sự hỗ trợ ý được trích; ID hợp lệ là chưa đủ.
- abstention_correct với câu thiếu bằng chứng: true khi agent thực sự từ chối, không thêm khẳng định vô căn cứ.
- context_score (chỉ test, ít nhất 5 câu có đáp án): 0 = không có evidence; 1 = có nhưng thiếu điều kiện hoặc nguồn; 2 = đủ evidence và nguồn.

## q01 · có đáp án · answered

- Câu hỏi: Theo báo cáo Bad Bot Report 2024 của Imperva, bot traffic chiếm khoảng bao nhiêu phần trăm tổng lưu lượng Internet toàn cầu?
- Đáp án chuẩn: Khoảng 49,6%.
- Evidence gold (tr. 15): bot traffic hiện chiếm khoảng 49,6% tổng lưu lượng Internet toàn cầu
- Truy vấn (1): Báo cáo Imperva Bad Bot Report 2024 bot traffic chiếm bao nhiêu phần trăm tổng lưu lượng Internet toàn cầu
- Context cuối: B:doan-bot-traffic-2026:p15:665-1185

Câu trả lời của agent:

> Bot traffic chiếm khoảng **49,6%** tổng lưu lượng Internet toàn cầu. [B:doan-bot-traffic-2026:p15:665-1185]

1. [B:doan-bot-traffic-2026:p15:665-1185] (tr. 15): 1.1.2. Hạn chế của các phương pháp phát hiện traffic truyền thống và động lực ứng dụng Machine Learning Mặc dù các hệ thống phân tích traffic truyền thống đã được sử dụng rộng rãi trong Digital Marketing, nhiều nghiên cứu và báo cáo thực tế cho thấy các phương pháp này vẫn tồn tại nhiều hạn chế. Theo báo cáo "Bad Bot Report 2024" của Imperva, bot traffic hiện chiếm khoảng 49,6% tổng lưu lượng Internet toàn cầu, trong đó phần lớn là các bot độc hại phục vụ cho spam, scraping dữ liệu, click fraud và tấn công tự động.

## q02 · có đáp án · answered

- Câu hỏi: Theo số liệu Cloudflare năm 2024 được trích dẫn, bao nhiêu phần bot độc hại có thể giả làm trình duyệt và hành vi người dùng?
- Đáp án chuẩn: Hơn 30% bot traffic độc hại.
- Evidence gold (tr. 15): Theo thống kê của Cloudflare năm 2024, hơn 30% bot traffic độc hại có khả năng giả lập trình duyệt và hành vi người dùng
- Truy vấn (1): Cloudflare năm 2024 tỷ lệ bot độc hại có thể giả làm trình duyệt và hành vi người dùng bao nhiêu phần trăm
- Context cuối: B:doan-bot-traffic-2026:p15:1186-1860

Câu trả lời của agent:

> Hơn **30%** lưu lượng bot độc hại có khả năng giả lập trình duyệt và hành vi người dùng. [B:doan-bot-traffic-2026:p15:1186-1860]

1. [B:doan-bot-traffic-2026:p15:1186-1860] (tr. 15): Điều này cho thấy lưu lượng truy cập không còn hoàn toàn đến từ người dùng thật, gây ảnh hưởng nghiêm trọng đến độ chính xác của dữ liệu phân tích và hiệu quả của các chiến dịch Digital Marketing. [14] Phần lớn các hệ thống hiện nay hoạt động dựa trên phương pháp rule-based detection, sử dụng các luật cố định như chặn IP, giới hạn request hoặc kiểm tra user agent để phát hiện bot traffic. Tuy nhiên, các bot hiện đại ngày càng tinh vi và có khả năng mô phỏng hành vi người dùng thật. Theo thống kê của Cloudflare năm 2024, hơn 30% bot traffic độc hại có khả năng giả lập trình duyệt và hành vi người dùng, khiến nhiều hệ thống bảo vệ truyền thống khó phát hiện chính xác.

## q03 · có đáp án · abstain

- Câu hỏi: Giải pháp Cloudflare Bot Management nhận diện bot dựa vào những yếu tố nào?
- Đáp án chuẩn: Fingerprint, IP reputation và AI.
- Evidence gold (tr. 18): Hệ thống có khả năng phát hiện bot dựa trên fingerprint, IP reputation và AI.
- Truy vấn (2): Cloudflare Bot Management nhận diện bot dựa vào những yếu tố nào, các tín hiệu và phương pháp phát hiện bot | Cloudflare Bot Management các yếu tố tín hiệu nhận diện bot: hành vi, fingerprint trình duyệt, địa chỉ IP, header, JavaScript, machine learning, điểm số bot score
- Context cuối: B:doan-bot-traffic-2026:p79:0-533

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q04 · có đáp án · abstain

- Câu hỏi: Thế hệ hệ thống phát hiện bot giai đoạn 2010–2016 dựa trên hướng tiếp cận nào?
- Đáp án chuẩn: Phân tích hành vi và thống kê.
- Evidence gold (tr. 24): Thế hệ thứ hai (2010–2016) – Phân tích hành vi và thống kê
- Truy vấn (3): Thế hệ hệ thống phát hiện bot trong giai đoạn 2010–2016 dựa trên hướng tiếp cận nào? Tìm các đoạn mô tả lịch sử, phân loại hoặc phương pháp phát hiện bot giai đoạn 2010 đến 2016. | Thế hệ thứ hai giai đoạn 2010–2016 hệ thống phát hiện bot traffic phương pháp tiếp cận machine learning học máy đặc trưng hành vi | Trong mục 1.5.2 Lịch sử phát triển hệ thống Bot Detection, tìm đoạn mô tả Thế hệ thứ hai (2010–2016), đặc biệt hướng tiếp cận, phương pháp hoặc đặc trưng dùng để phát hiện bot traffic.
- Context cuối: B:doan-bot-traffic-2026:p24:298-673

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q05 · có đáp án · abstain

- Câu hỏi: Ở bước tiền xử lý của quy trình phát hiện bot bằng Machine Learning, những dữ liệu nào bị loại bỏ?
- Đáp án chuẩn: Request lỗi, dữ liệu trùng lặp hoặc dữ liệu không hợp lệ.
- Evidence gold (tr. 27): dữ liệu traffic được làm sạch nhằm loại bỏ request lỗi, dữ liệu trùng lặp hoặc dữ liệu không hợp lệ
- Truy vấn (4): bước tiền xử lý quy trình phát hiện bot bằng Machine Learning dữ liệu bị loại bỏ loại bỏ dữ liệu | Trong bước làm sạch dữ liệu tiền xử lý của quy trình phát hiện bot bằng Machine Learning, hệ thống loại bỏ những bản ghi hoặc dữ liệu nào, ví dụ request lỗi, thiếu trường, trùng lặp, IP hoặc user-agent không hợp lệ? | Trong bước làm sạch dữ liệu của quy trình xử lý Machine Learning phát hiện bot, tài liệu nêu cụ thể những dữ liệu hoặc bản ghi nào bị loại bỏ, như request lỗi, bản ghi thiếu trường, dữ liệu trùng lặp, IP không hợp lệ, user-agent không hợp lệ hoặc giá trị bất thường? | Trong mục 2.6 Quy trình xử lý dữ liệu Machine Learning, bước làm sạch dữ liệu loại bỏ cụ thể những bản ghi nào: request lỗi, thiếu trường bắt buộc, trùng lặp, IP không hợp lệ, user-agent không hợp lệ, dữ liệu bất thường?
- Context cuối: B:doan-bot-traffic-2026:p54:1418-1716, B:doan-bot-traffic-2026:p52:799-1078

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q06 · có đáp án · answered

- Câu hỏi: Nhóm đặc trưng mô tả cách người dùng duyệt website gồm những chỉ số nào?
- Đáp án chuẩn: Số trang truy cập, thời gian ở lại website (session duration), chuỗi điều hướng giữa các trang và tỷ lệ thoát trang (bounce rate).
- Evidence gold (tr. 30): Đặc trưng về hành vi người dùng: số lượng trang truy cập, thời gian ở lại website (session duration), chuỗi điều hướng giữa các trang và tỷ lệ thoát trang (bounce rate).
- Truy vấn (1): nhóm đặc trưng mô tả cách người dùng duyệt website gồm những chỉ số nào; các chỉ số hành vi duyệt website, số trang, thời gian, lượt truy cập
- Context cuối: B:doan-bot-traffic-2026:p30:0-611

Câu trả lời của agent:

> Nhóm đặc trưng mô tả cách người dùng duyệt website gồm: - Số lượng trang truy cập - Thời gian ở lại website (session duration) - Chuỗi điều hướng giữa các trang - Tỷ lệ thoát trang (bounce rate) [B:doan-bot-traffic-2026:p30:0-611]

1. [B:doan-bot-traffic-2026:p30:0-611] (tr. 30): request trên mỗi session, tốc độ gửi request, thời gian trung bình giữa hai request liên tiếp. Bot traffic thường có tần suất truy cập cao và đều bất thường so với người dùng thật. - Đặc trưng về hành vi người dùng: số lượng trang truy cập, thời gian ở lại website (session duration), chuỗi điều hướng giữa các trang và tỷ lệ thoát trang (bounce rate). Người dùng thật thường có hành vi duyệt web đa dạng hơn bot. - Đặc trưng về kỹ thuật: địa chỉ IP, user-agent, loại thiết bị, quốc gia truy cập, loại trình duyệt và hệ điều hành. Một số bot sử dụng user-agent giả hoặc thực hiện request từ nhiều IP bất thường.

## q07 · có đáp án · answered

- Câu hỏi: Trong chương 1, những bộ dữ liệu công khai nào được nêu để tham khảo và kiểm thử mô hình phát hiện bot? (filter {'chapter': 1})
- Đáp án chuẩn: CIC-IDS2017, Bot-IoT hoặc Web Server Log Dataset.
- Evidence gold (tr. 30): một số bộ dữ liệu nghiên cứu về bot detection như CIC-IDS2017, Bot-IoT hoặc Web Server Log Dataset
- Truy vấn (1): Chương 1 liệt kê những bộ dữ liệu công khai dùng để tham khảo và kiểm thử mô hình phát hiện bot
- Context cuối: B:doan-bot-traffic-2026:p30:2133-2521

Câu trả lời của agent:

> Các bộ dữ liệu công khai được nêu là: **CIC-IDS2017, Bot-IoT và Web Server Log Dataset**. [B:doan-bot-traffic-2026:p30:2133-2521]

1. [B:doan-bot-traffic-2026:p30:2133-2521] (tr. 30): - Dataset công khai: một số bộ dữ liệu nghiên cứu về bot detection như CIC-IDS2017, Bot-IoT hoặc Web Server Log Dataset được sử dụng để tham khảo và kiểm thử mô hình. Dữ liệu traffic thường có kích thước lớn và phát sinh liên tục theo thời gian thực. Vì vậy hệ thống cần cơ chế lưu trữ hiệu quả để phục vụ cho cả huấn luyện mô hình và phân tích realtime. Trong kiến trúc hệ thống đề xuất:

## q08 · có đáp án · answered

- Câu hỏi: Trong chương 3, dữ liệu thực nghiệm được lấy từ những nguồn nào? (filter {'chapter': 3})
- Đáp án chuẩn: Dữ liệu log thu thập từ request mẫu, dữ liệu đã tiền xử lý trong dataset.csv và dữ liệu mô phỏng trong synthetic_data.csv.
- Evidence gold (tr. 60): Dữ liệu thực nghiệm gồm dữ liệu log thu thập từ request mẫu, dữ liệu đã tiền xử lý trong dataset.csv và dữ liệu mô phỏng trong synthetic_data.csv.
- Truy vấn (3): Chương 3 dữ liệu thực nghiệm được lấy từ những nguồn nào nguồn dữ liệu thực nghiệm | Chương 3 nguồn lấy dữ liệu thực nghiệm dataset real traffic bot traffic log website dữ liệu mô phỏng nguồn dữ liệu | Chương 3 mục dữ liệu thực nghiệm nguồn dữ liệu dataset được thu thập từ đâu log truy cập website dữ liệu thực tế mô phỏng real traffic bot traffic
- Context cuối: B:doan-bot-traffic-2026:p74:720-1272

Câu trả lời của agent:

> Dữ liệu thực nghiệm được tổng hợp theo hướng mô phỏng hoạt động thực tế của website, gồm hai nhóm: **real traffic** và **bot traffic**. [B:doan-bot-traffic-2026:p74:720-1272]

1. [B:doan-bot-traffic-2026:p74:720-1272] (tr. 74): 3.18. Bổ sung số liệu thực nghiệm và phân bố dataset Để đánh giá hệ thống rõ hơn, dữ liệu thực nghiệm được tổng hợp theo hướng mô phỏng gần với quá trình vận hành thực tế của một website digital marketing. Dataset gồm các session truy cập được gán nhãn thành hai nhóm: real traffic và bot traffic. Nhóm real traffic có đặc điểm request phân bố không đều, thời gian giữa các request thay đổi tự nhiên và số trang truy cập đa dạng. Nhóm bot traffic có xu hướng request nhanh, lặp lại endpoint, tỷ lệ lỗi cao hơn hoặc user-agent mang dấu hiệu tự động hóa.

## q09 · có đáp án · answered

- Câu hỏi: Theo chương 1, MySQL được dùng để lưu những loại dữ liệu nào của hệ thống? (filter {'chapter': 1})
- Đáp án chuẩn: Dữ liệu traffic có cấu trúc như session, request log, thông tin người dùng và kết quả phân loại traffic.
- Evidence gold (tr. 31): MySQL được sử dụng để lưu trữ dữ liệu traffic có cấu trúc như session, request log, thông tin người dùng và kết quả phân loại traffic.
- Truy vấn (1): Chương 1 MySQL được sử dụng để lưu trữ những loại dữ liệu nào của hệ thống
- Context cuối: B:doan-bot-traffic-2026:p31:0-554

Câu trả lời của agent:

> MySQL được dùng để lưu dữ liệu traffic có cấu trúc, gồm: session, request log, thông tin người dùng và kết quả phân loại traffic. [B:doan-bot-traffic-2026:p31:0-554]

1. [B:doan-bot-traffic-2026:p31:0-554] (tr. 31): - MySQL được sử dụng để lưu trữ dữ liệu traffic có cấu trúc như session, request log, thông tin người dùng và kết quả phân loại traffic. - MongoDB hoặc JSON log storage có thể được sử dụng cho dữ liệu log lớn, linh hoạt và thay đổi thường xuyên. - Dữ liệu sau khi thu thập sẽ được tiền xử lý và chuyển đổi thành feature dataset trước khi đưa vào pipeline Machine Learning. Ngoài việc lưu trữ, hệ thống còn cần hỗ trợ truy vấn nhanh theo thời gian, IP hoặc session để phục vụ dashboard giám sát và phân tích hành vi traffic bất thường theo thời gian thực.

## q10 · có đáp án · answered

- Câu hỏi: Trong chương 2, MySQL Database Service lưu những nhóm dữ liệu nào? (filter {'chapter': 2})
- Đáp án chuẩn: User data, traffic logs, detection results, system configuration và audit logs.
- Evidence gold (tr. 49): User data (admin, analyst, system user) - Traffic logs (request history) - Detection results (bot_score, label) - System configuration (rules, thresholds) - Audit logs
- Truy vấn (1): Chương 2 MySQL Database Service lưu những nhóm dữ liệu nào các nhóm dữ liệu được lưu trữ
- Context cuối: B:doan-bot-traffic-2026:p49:0-403, B:doan-bot-traffic-2026:p59:1348-1510

Câu trả lời của agent:

> MySQL Database Service lưu các nhóm dữ liệu: - Dữ liệu người dùng. - Nhật ký lưu lượng truy cập. - Kết quả phát hiện/phân loại. - Cấu hình hệ thống. - Nhật ký kiểm toán (audit logs). [B:doan-bot-traffic-2026:p49:0-403]

1. [B:doan-bot-traffic-2026:p49:0-403] (tr. 49): 2.3.5. MySQL Database Service Hệ thống sử dụng MySQL để lưu trữ dữ liệu chính. Các nhóm dữ liệu: - User data (admin, analyst, system user) - Traffic logs (request history) - Detection results (bot_score, label) - System configuration (rules, thresholds) - Audit logs Thiết kế tối ưu: - Partition bảng traffic_logs theo ngày/tháng - Index theo IP, session_id, timestamp - Sử dụng read replica nếu tải lớn

## q11 · có đáp án · answered

- Câu hỏi: Trong chương 2, kết quả phân loại traffic đầu ra của hệ thống gồm những nhãn nào? (filter {'chapter': 2})
- Đáp án chuẩn: Người dùng thật (real user), bot hợp lệ (good bot) hoặc bot bất thường (malicious bot).
- Evidence gold (tr. 35): Kết quả phân loại traffic gồm người dùng thật (real user), bot hợp lệ (good bot) hoặc bot bất thường (malicious bot)
- Truy vấn (1): Chương 2 kết quả phân loại traffic đầu ra của hệ thống gồm những nhãn nào các nhãn phân loại lưu lượng đầu ra
- Context cuối: B:doan-bot-traffic-2026:p35:1496-1925

Câu trả lời của agent:

> Kết quả phân loại traffic đầu ra của hệ thống gồm: **người dùng thật (real user), bot hợp lệ (good bot) và bot bất thường (malicious bot)**. [B:doan-bot-traffic-2026:p35:1496-1925]

1. [B:doan-bot-traffic-2026:p35:1496-1925] (tr. 35): - Các thông tin kỹ thuật như IP address, user-agent, HTTP method, request URL, response status và thời gian truy cập. Đầu ra của hệ thống: - Kết quả phân loại traffic gồm người dùng thật (real user), bot hợp lệ (good bot) hoặc bot bất thường (malicious bot); - Dashboard hiển thị thống kê traffic, session và cảnh báo các truy cập bất thường theo thời gian thực; - Báo cáo phân tích traffic phục vụ quản trị và giám sát hệ thống.

## q12 · có đáp án · answered

- Câu hỏi: Endpoint nào của Traffic Collection API dùng để thu thập dữ liệu request?
- Đáp án chuẩn: POST /v1/collect.
- Evidence gold (tr. 47): POST /v1/collect– Thu thập request data
- Truy vấn (1): Traffic Collection API endpoint dùng để thu thập dữ liệu request, tên endpoint hoặc đường dẫn API thu thập request
- Context cuối: B:doan-bot-traffic-2026:p47:775-1333

Câu trả lời của agent:

> Endpoint dùng để thu thập dữ liệu request là **POST `/v1/collect`**. [B:doan-bot-traffic-2026:p47:775-1333]

1. [B:doan-bot-traffic-2026:p47:775-1333] (tr. 47): 2.3.3. Traffic Collection API (Golang RESTful API) Traffic Collection API được xây dựng bằng Golang nhằm đảm bảo hiệu năng cao trong việc thu thập request realtime. Chức năng chính: - Nhận toàn bộ HTTP requests từ client hoặc proxy layer. - Ghi nhận thông tin: IP, user-agent, headers, payload metadata. - Gán session_id và request_id cho từng request. - Forward dữ liệu sang AI/ML Service để phân tích. - Stream dữ liệu sang Kafka/queue (nếu mở rộng hệ thống). API chính: -POST /v1/collect– Thu thập request data -GET /v1/health– Kiểm tra trạng thái service

## q13 · có đáp án · answered

- Câu hỏi: Trong luồng phân tích, khi nào hệ thống ghi nhận một cảnh báo bot và lưu ở đâu?
- Đáp án chuẩn: Khi xác suất bot vượt ngưỡng cấu hình; cảnh báo được ghi vào bảng bot_detection_results và hiển thị trên dashboard.
- Evidence gold (tr. 53): Nếu xác suất bot vượt ngưỡng cấu hình, hệ thống ghi nhận cảnh báo vào bảng bot_detection_results và hiển thị trên dashboard.
- Truy vấn (1): luồng phân tích khi nào hệ thống ghi nhận cảnh báo bot cảnh báo bot được lưu ở đâu
- Context cuối: B:doan-bot-traffic-2026:p53:329-836

Câu trả lời của agent:

> Khi xác suất bot vượt ngưỡng cấu hình, hệ thống ghi nhận cảnh báo vào bảng `bot_detection_results` và hiển thị trên dashboard. Cảnh báo gồm nhãn phân loại cùng các đặc trưng như `requests_per_minute`, `unique_pages` và `average_interval`. [B:doan-bot-traffic-2026:p53:329-836]

1. [B:doan-bot-traffic-2026:p53:329-836] (tr. 53): 2.4.3. Luồng phân tích và cảnh báo bot traffic Backend lấy dữ liệu session đã đủ thông tin, tạo vector đặc trưng và gửi sang AI Service. AI Service nạp model đã huấn luyện, dự đoán nhãn và trả về xác suất bot. Nếu xác suất bot vượt ngưỡng cấu hình, hệ thống ghi nhận cảnh báo vào bảng bot_detection_results và hiển thị trên dashboard. Cảnh báo không chỉ gồm nhãn phân loại mà còn bao gồm các đặc trưng quan trọng như requests_per_minute, unique_pages và average_interval để người quản trị có cơ sở kiểm tra.

## q14 · có đáp án · abstain

- Câu hỏi: Trường ip_address được thiết kế với kiểu dữ liệu nào và nhằm hỗ trợ điều gì?
- Đáp án chuẩn: VARCHAR(45), để hỗ trợ cả IPv4 và IPv6.
- Evidence gold (tr. 54): ip_address Địa chỉ IP truy cập VARCHAR(45) Hỗ trợ IPv4/IPv6
- Truy vấn (4): trường ip_address kiểu dữ liệu được thiết kế nhằm hỗ trợ chức năng gì trong cơ sở dữ liệu | Trong thiết kế cơ sở dữ liệu, trường ip_address thuộc bảng nào, được khai báo kiểu dữ liệu gì (ví dụ VARCHAR, VARBINARY, INET6) và mục đích hỗ trợ lưu trữ, tra cứu hoặc phát hiện địa chỉ IP như thế nào? | ip_address kiểu dữ liệu bảng lưu địa chỉ IP phát hiện bot traffic tra cứu địa chỉ IP thiết kế cơ sở dữ liệu | ip_address được khai báo kiểu dữ liệu gì trong bảng cơ sở dữ liệu, mục đích lưu trữ tra cứu phát hiện địa chỉ IP hoặc bot traffic
- Context cuối: B:doan-bot-traffic-2026:p53:1402-2100

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q15 · có đáp án · answered

- Câu hỏi: Vì sao pipeline Machine Learning lưu dữ liệu thô tách biệt với kết quả dự đoán?
- Đáp án chuẩn: Dữ liệu thô phục vụ truy vết và huấn luyện lại, còn kết quả dự đoán phục vụ cảnh báo và báo cáo.
- Evidence gold (tr. 55): Dữ liệu thô phục vụ truy vết và huấn luyện lại, còn kết quả dự đoán phục vụ cảnh báo và báo cáo.
- Evidence gold (tr. 54): không ghi đè log gốc mà được lưu riêng nhằm bảo toàn dữ liệu thô cho quá trình huấn luyện lại sau này
- Truy vấn (1): pipeline Machine Learning vì sao lưu dữ liệu thô tách biệt với kết quả dự đoán mục đích lưu trữ dữ liệu raw prediction kết quả dự đoán
- Context cuối: B:doan-bot-traffic-2026:p55:772-1371

Câu trả lời của agent:

> Pipeline lưu tách biệt vì: - Dữ liệu thô dùng để truy vết và huấn luyện lại mô hình. - Kết quả dự đoán dùng cho cảnh báo và báo cáo. - Cách tách này giúp dễ kiểm tra, dễ mở rộng và bảo toàn dữ liệu gốc khi cập nhật mô hình. [B:doan-bot-traffic-2026:p55:772-1371]

1. [B:doan-bot-traffic-2026:p55:772-1371] (tr. 55): Mô hình Random Forest được huấn luyện trên tập dữ liệu sau tiền xử lý. Khi có traffic mới, Backend tạo vector đặc trưng theo đúng thứ tự đã dùng lúc huấn luyện và gửi sang AI Service. AI Service trả về nhãn dự đoán, xác suất bot và confidence để lưu vào database và hiển thị trên dashboard. Một điểm quan trọng trong thiết kế pipeline là dữ liệu thô và kết quả dự đoán được lưu tách biệt. Dữ liệu thô phục vụ truy vết và huấn luyện lại, còn kết quả dự đoán phục vụ cảnh báo và báo cáo. Cách tách này giúp hệ thống dễ kiểm tra, dễ mở rộng và tránh làm mất nguồn dữ liệu gốc khi mô hình được cập nhật.

## q16 · có đáp án · answered

- Câu hỏi: Sau khi đăng nhập, người dùng dùng gì để gọi các API cần bảo vệ?
- Đáp án chuẩn: Access token được cấp sau khi đăng nhập.
- Evidence gold (tr. 57): Sau khi đăng nhập, người dùng nhận access token để gọi các API
- Evidence gold (tr. 49): JWT (access token + refresh token)
- Truy vấn (1): Sau khi đăng nhập, người dùng sử dụng gì để gọi các API cần bảo vệ? Cơ chế xác thực, token, JWT, access token trong header Authorization
- Context cuối: B:doan-bot-traffic-2026:p57:2606-2763, B:doan-bot-traffic-2026:p49:404-773

Câu trả lời của agent:

> Sau khi đăng nhập, người dùng sử dụng **access token (JWT)** để gọi các API cần bảo vệ. [B:doan-bot-traffic-2026:p57:2606-2763]

1. [B:doan-bot-traffic-2026:p57:2606-2763] (tr. 57): JWT được lựa chọn cho cơ chế xác thực vì phù hợp với mô hình web API tách frontend và backend. Sau khi đăng nhập, người dùng nhận access token để gọi các API

## q17 · có đáp án · abstain

- Câu hỏi: Theo chương 1, nếu AI Service tạm thời gặp lỗi thì hệ thống theo kiến trúc Microservice vẫn hoạt động ra sao? (filter {'chapter': 1})
- Đáp án chuẩn: Vẫn tiếp tục thu thập log và lưu dữ liệu thô để phân tích lại sau; các thành phần còn lại không bị dừng toàn bộ.
- Evidence gold (tr. 32): nếu AI Service tạm thời gặp lỗi, hệ thống vẫn có thể tiếp tục thu thập log và lưu dữ liệu thô để phân tích lại sau; các thành phần còn lại không bị dừng toàn bộ
- Truy vấn (3): Chương 1 kiến trúc Microservice AI Service tạm thời gặp lỗi hệ thống vẫn hoạt động ra sao cơ chế dự phòng xử lý lỗi | Chương 1 khi AI Service gặp lỗi tạm thời Microservice các service khác vẫn hoạt động độc lập cơ chế cô lập lỗi dự phòng | Chương 1 AI Service bị lỗi tạm thời hệ thống Microservice xử lý như thế nào các service khác hoạt động độc lập cô lập lỗi fallback retry circuit breaker
- Context cuối: B:doan-bot-traffic-2026:p33:734-1404

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q18 · có đáp án · answered

- Câu hỏi: Khi kiểm tra tự động phát hiện dữ liệu bị lệch mạnh, hệ thống cần làm gì trước khi huấn luyện lại mô hình?
- Đáp án chuẩn: Cảnh báo để người phát triển kiểm tra trước khi dùng dữ liệu đó huấn luyện lại mô hình.
- Evidence gold (tr. 71): Khi phát hiện dữ liệu lệch mạnh, hệ thống cần cảnh báo để người phát triển kiểm tra trước khi dùng dữ liệu đó huấn luyện lại mô hình.
- Truy vấn (1): kiểm tra tự động phát hiện dữ liệu bị lệch mạnh hệ thống cần làm gì trước khi huấn luyện lại mô hình
- Context cuối: B:doan-bot-traffic-2026:p71:985-1401

Câu trả lời của agent:

> Khi phát hiện dữ liệu lệch mạnh, hệ thống cần cảnh báo để người phát triển kiểm tra trước khi sử dụng dữ liệu huấn luyện lại mô hình. [B:doan-bot-traffic-2026:p71:985-1401]

1. [B:doan-bot-traffic-2026:p71:985-1401] (tr. 71): Biện pháp kiểm soát phù hợp là xây dựng các kiểm tra dữ liệu tự động trước khi huấn luyện mô hình. Các kiểm tra này bao gồm tỷ lệ thiếu dữ liệu, phân phối của từng feature, tỷ lệ nhãn bot/real, số lượng session quá ngắn, số request trùng lặp và sự thay đổi bất thường giữa các ngày. Khi phát hiện dữ liệu lệch mạnh, hệ thống cần cảnh báo để người phát triển kiểm tra trước khi dùng dữ liệu đó huấn luyện lại mô hình.

## q25 · thiếu bằng chứng · abstain

- Câu hỏi: Theo đồ án, bot traffic chiếm khoảng bao nhiêu phần trăm lưu lượng truy cập của các website tại Việt Nam?
- Lý do thiếu bằng chứng: Mục 1.1.3 (tr. 17) chỉ nêu số liệu Việt Nam về người dùng Internet (hơn 78 triệu, trên 79% dân số, DataReportal 2024) và nhận định doanh nghiệp Việt Nam còn thiếu giải pháp phát hiện bot; tỷ lệ bot traffic chỉ có ở mức toàn cầu (gần 50% ở tr. 17; 49,6% theo Imperva ở tr. 15). Cách kiểm tra: đọc toàn văn mục 1.1.3 và tìm mọi câu chứa 'Việt Nam' kèm '%' hoặc 'bot' trên 254 chunk index B: không có tỷ lệ bot traffic riêng cho Việt Nam.
- Truy vấn (1): bot traffic chiếm khoảng bao nhiêu phần trăm lưu lượng truy cập của các website tại Việt Nam
- Context cuối: B:doan-bot-traffic-2026:p17:1134-1770

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


## q26 · thiếu bằng chứng · abstain

- Câu hỏi: Đồ án nêu hệ thống phải tuân thủ văn bản pháp lý nào về bảo vệ dữ liệu cá nhân (ví dụ GDPR hoặc Nghị định 13/2023/NĐ-CP) khi lưu IP và user-agent của người truy cập?
- Lý do thiếu bằng chứng: Mục 3.11 (tr. 68–69) chỉ nêu biện pháp kỹ thuật (API key, phân quyền, RBAC, đặt AI Service trong mạng nội bộ, sao lưu định kỳ) và khuyến nghị chỉ dùng IP cho mục tiêu an ninh và phân tích traffic; không nêu văn bản pháp lý nào. Cách kiểm tra: đọc toàn văn mục 3.11 và tìm trên 254 chunk index B các từ 'GDPR', 'nghị định', '13/2023', 'dữ liệu cá nhân', 'pháp lý', 'tuân thủ', 'quyền riêng tư', 'privacy', 'consent', 'cookie': 0 kết quả; mọi lần xuất hiện 'luật' (18 chunk) đều mang nghĩa luật phát hiện (rule-based) hoặc luật phân tách của Decision Tree.
- Truy vấn (2): Đồ án nêu yêu cầu tuân thủ văn bản pháp lý về bảo vệ dữ liệu cá nhân khi lưu địa chỉ IP và user-agent của người truy cập, GDPR, Nghị định 13/2023/NĐ-CP | Trong đồ án có nêu GDPR, Nghị định 13/2023/NĐ-CP, Luật bảo vệ dữ liệu cá nhân, hoặc văn bản pháp lý nào khi thu thập/lưu địa chỉ IP và user-agent không?
- Context cuối: B:doan-bot-traffic-2026:p68:1453-1954

Câu trả lời của agent:

> Không đủ bằng chứng để trả lời.


