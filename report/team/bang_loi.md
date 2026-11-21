# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Bản thực hành cá nhân dùng hai lượt AI độc lập. Mỗi lượt chỉ đọc đề học viên và trả đủ 20 nhãn. Hai bộ nhãn được so sau khi cả hai lượt đã chốt.

| Ca | Lượt AI 1 | Lượt AI 2 | Trùng | Nhãn thống nhất |
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

Hai lượt trùng **20/20 = 100%**, tính bằng số ca trùng chia 20. Mốc 80% tương ứng 16 ca. Bộ nhãn thống nhất khớp 20/20 ca với slide chữa.

## Quy tắc phân biệt ở các ca dễ nhầm

Hai lượt đồng thuận ở cả 20 ca. Ba ranh giới đáng lưu ý:

- **Ca 6 và 9.** Khách chọn sai mục hoặc nhập sai loại mã. Hai ca được gắn nhãn Do người dùng theo nguyên nhân khởi phát.
- **Ca 12 và 17.** Chi phí tăng hoặc số tiền lệch kéo dài mà vận hành không phát hiện. Hai ca được gắn nhãn Ngầm.
- **Ca 13 và 18.** Hoàn phí bảo hiểm nằm ngoài phạm vi nên ca 13 là Giới hạn hệ thống. Ca 18 hoàn đúng tiền nhưng thiếu cách tính khiến khách hiểu khác, nên là Ngữ cảnh.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các biện pháp được chọn từ nhãn thống nhất. Ngưỡng trong bảng là đề xuất cho pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_destination_validation_failed` khi số tài khoản không hợp lệ theo quy tắc ngân hàng đã chọn. Rà soát hằng ngày nếu có từ 5 lượt cùng mã lỗi độ dài. | Kiểm tra trước khi tạo lệnh hoàn và hướng dẫn khách đối chiếu số tài khoản. Chỉ ghi mã lỗi và `trace_id` vào sự kiện. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát `refund_ledger_written` theo khóa nghĩa vụ hoàn. Cảnh báo ngay khi có hai giao dịch thành công cho cùng một nghĩa vụ. | Dùng một khóa chống trùng cho cùng nghĩa vụ dù khách gửi lại. Nếu lệnh cũ đang chờ, tra trạng thái lệnh đó trước khi xử lý tiếp. | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Nối `ticket_reopened` có lý do chưa nhận tiền với giao dịch thành công vào ví. Rà lại mẫu thông báo từ 3 ca cùng lý do trong tuần. | Hiển thị rõ tiền hoàn vào ví LogiX trước khi khách xác nhận. Trong thông báo hoàn, ghi ví nhận tiền và cách xem số dư. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Ghi `unsupported_input_received` khi nhận tệp thoại. Rà luồng hỗ trợ khi có từ 10 yêu cầu khác nhau trong tuần. | Hiển thị lựa chọn nhập chữ hoặc chuyển nhân viên ngay khi nhận dạng tệp thoại, kèm mã yêu cầu để khách khỏi khai lại thông tin đã có. | Quản lý kênh hỗ trợ |
| 12 | Ngầm | Hằng tuần dùng `agent_run_completed` và kết quả đóng để so token mỗi việc thành công theo depot và loại yêu cầu. Rà soát nếu D05 vượt 1,5 lần trung vị các depot khác ở cùng loại trong hai tuần và có ít nhất 30 việc thành công mỗi tuần. | Kiểm tra trường thiếu trong phản hồi tra đơn của D05, bổ sung kiểm tra hợp đồng dữ liệu và chuyển nhân viên khi thiếu trường cần thiết để tránh gọi lặp. | Kỹ sư phụ trách tích hợp dữ liệu |
