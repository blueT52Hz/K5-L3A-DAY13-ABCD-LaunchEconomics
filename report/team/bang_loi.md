# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Quang Duy · Người gắn nhãn 2: Khổng Tiến Dương (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng (20/20).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_transfer_failed` có `error_code = invalid_account_number` hoặc `input_validation_failed`, tổng hợp hằng ngày. Ngưỡng: > 3% số yêu cầu hoàn tiền trong 24 giờ hoặc > 10 ca/ngày | Kiểm tra độ dài/định dạng số tài khoản ngay trên biểu mẫu trước khi tạo lệnh hoàn và hiển thị hướng dẫn sửa lỗi để khách nhập lại | Kỹ sư phụ trách agent hoàn phí |
| 20 | Hệ thống | Đối soát hằng ngày event `refund_ledger_write`: đếm số mã vận đơn có từ 2 lệnh hoàn trở lên trong 24 giờ. Ngưỡng: lớn hơn 0 ca/ngày thì báo động ngay | Lệnh hoàn bắt buộc có `idempotency_key` = mã vận đơn + loại hoàn phí; sổ cái từ chối lệnh trùng khoá. Khách gửi lại yêu cầu thì trợ lý trả trạng thái của yêu cầu cũ thay vì tạo lệnh mới. Thu hồi khoản hoàn thừa | Kỹ sư phụ trách agent hoàn phí |
| 18 | Ngữ cảnh | Event `ticket_reopened` trong 7 ngày có `ly_do = khieu_nai_thieu_tien` trên các ca đã tính đúng số tiền, tổng hợp hằng tuần. Ngưỡng: > 2% số ca đã đóng hoặc > 5 ca/tuần | Cập nhật mẫu phản hồi hiển thị rõ công thức tính (phí gốc, tỉ lệ hoàn theo chính sách, số tiền thực hoàn và kênh nhận tiền) | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` có `ly_do = ngoai_du_lieu_12_thang`, tổng hợp hằng tuần. Ngưỡng: tỉ lệ trên 2% số yêu cầu, hoặc có handoff mà `tom_tat` rỗng, hoặc nhân viên đóng sau handoff quá 24 giờ (từ `ticket_closed`) | Giữ cách xử lý hiện tại (nói rõ giới hạn, chuyển kèm tóm tắt). Kiểm tra tuổi đơn ngay bước đầu để chuyển trước khi gọi tool tra cứu, tránh tốn token, và báo khách thời gian xử lý dự kiến | Trưởng nhóm CSKH |
| 17 | Ngầm | Event `audit_sample_checked` hằng tuần trên 100 đơn chọn ngẫu nhiên: tỉ lệ đơn có `so_tien_da_hoan` khác `so_tien_dung`. Ngưỡng: trên 1% số đơn hoặc tổng lệch trên 200.000 đ/tuần. Thêm phiên bản bảng giá vào `agent_run_completed` và so với bản hiện hành mỗi ngày | Xoá bộ nhớ đệm bảng giá mỗi khi bảng giá đổi, ghi phiên bản bảng giá vào trace của mỗi lần chạy. Rà lại 212 đơn bị lệch và hoàn bù hoặc điều chỉnh | Kỹ sư phụ trách agent hoàn phí |
