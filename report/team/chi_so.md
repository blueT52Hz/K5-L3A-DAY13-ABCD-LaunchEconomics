# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0`, chia tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Bỏ qua gợi ý | Quyết định cuối là `sua` hoặc `bo`, chia số yêu cầu đã xem lại | 48/177 = 27,12% |
| An toàn | Mở lại trong 7 ngày | `mo_lai_trong_7_ngay = 1`, chia tổng số yêu cầu | 51/1.200 = 4,25%. Trong phạm vi pilot là 39/982 = 3,97%. |
| Dùng | Mở trợ lý | Số yêu cầu có lượt mở trợ lý trên số yêu cầu được bật trợ lý | Đo trong pilot |
| An toàn | Sai tiền qua đối soát mẫu | Số khoản chi lệch chính sách trên số khoản được kiểm tra ngẫu nhiên | Đo trong pilot |

Đây là các chỉ số của đợt chạy thử giả lập một nhóm. Đo mức tăng bằng đối chứng cùng kỳ trong pilot.

## Danh sách event

Mọi event có `event_id`, `trace_id`, `request_id` và thời điểm. Mỗi lượt chạy có thêm `run_id`. Giữ nguyên nhóm phân ban đầu khi tổng hợp.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hàng đợi CSKH | Loại, depot, nhân viên nhận đầu, nhóm phân, được bật trợ lý | Khi nhận và định tuyến |
| `assistant_opened` | Giao diện CSKH | Tài khoản và trạng thái được cấp quyền | Khi mở |
| `agent_run_completed` | Agent | Số lượt, token, tool, trạng thái | Sau mọi lượt |
| `staff_review_decision` | Giao diện CSKH | Giữ, sửa, bỏ, phút thao tác thật, mã phiên duyệt | Khi duyệt xong |
| `staff_rework_completed` | Giao diện CSKH | Phút thao tác thật, lý do, mã phiên | Khi làm lại xong |
| `ticket_closed` | Hệ thống ticket | Kết quả, nhân viên hay trợ lý, mã giao dịch | Khi đóng |
| `ticket_reopened` | Hệ thống ticket | Lý do và mã lần đóng | Khi mở lại |
| `refund_ledger_written` | Sổ cái | Mã giao dịch, khóa nghĩa vụ hoàn, số tiền, trạng thái | Khi ghi |
| `refund_notice_sent` | Dịch vụ thông báo | Mã giao dịch và trạng thái báo khách | Khi gửi |
| `refund_outcome_reconciled` | Dịch vụ đối soát | Số tiền đúng theo phiên bản chính sách, kết quả đối chiếu | Sau đối soát |
| `refund_audited` | Kế toán | Số tiền thực trả, số đúng và lý do lệch | Kiểm tra mẫu mỗi tuần |

Chỉ số chính nối sự kiện tạo, đóng và mở lại. Chỉ số an toàn mở lại dùng sự kiện mở lại trong 7 ngày từ lúc tạo để so hai nhóm trên cửa sổ bằng nhau. Cờ CSV chỉ dùng làm tham chiếu vì không có mốc thời gian. Chỉ số bỏ qua dùng quyết định xem lại cuối, và chỉ số mở trợ lý dùng sự kiện tạo cùng sự kiện mở. Chỉ số hoàn sai tiền dùng event kiểm tra mẫu.

Luật chi phí dùng token, tool, thời gian xem lại và làm lại đo thật. Số việc thành công dựa trên kết quả đóng theo luồng trợ lý, đủ theo dõi 7 ngày và đối soát khớp. Luật báo sai hoặc hoàn trùng đối chiếu thông báo với sổ cái theo mã giao dịch và khóa nghĩa vụ hoàn.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại gấp đôi | 6.787 đ mỗi việc, +51,8% (simulated) | Tỷ lệ ca làm lại tuần vượt 7% | Rà 20 trace và sửa nguyên nhân phổ biến | PM trợ lý hoàn phí |
| Duyệt 100% kéo dài | 11.743 đ mỗi việc trước cố định (simulated) | Tỷ lệ xem lại còn trên 50% ở cuối bậc 25% | Đo phút thao tác và chỉ giảm duyệt nội địa khi qua cổng | Trưởng nhóm CSKH |
| Khối lượng giảm còn một nửa | Cố định tăng từ 1.185 lên 2.370 đ mỗi việc trong dự phóng A4 (simulated) | Số việc thành công/tháng dưới 16.875 | Tính lại tổng chi phí gồm bàn giao trước khi mở rộng | Kế toán trưởng |
