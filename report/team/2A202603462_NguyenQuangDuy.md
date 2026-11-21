# Báo cáo cá nhân — NguyenQuangDuy-2A202603462

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Duy
- MSSV: 2A202603462
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người gắn nhãn 1

## 2. Phần việc phụ trách

- **CP1:** Đọc rubric và điều kiện "Xong khi" của từng checkpoint. Tính sớm ba chỉ số E1 và tỉ lệ mở lại từ `logix_requests.csv`. Rà số A2–A4 và nhãn `simulated` trong `bang_chi_phi.md`.
- **CP2:** Nháp hai chỉ số E1 tự đề xuất và danh sách event có `trace_id`.
- **CP3:** Gắn nhãn 20 ca lỗi với vai người gắn nhãn 1, ghép hai bộ nhãn, tính đồng thuận, viết 3 dòng khắc phục (ca 20, 19, 17).
- **CP4:** Bàn giao tỉ lệ `mo_lai_trong_7_ngay` toàn mẫu và trong phạm vi pilot cho `pilot_plan.yaml`, đối chiếu tín hiệu an toàn từ C.
- **CP5:** Chốt E1 trong `chi_so.md`, soát bằng chứng lỗi, chỉ số, event và nhãn `simulated`, chấm C7 và tổng hợp `phieu_cham.md`, rà đủ 6 file hồ sơ và tên file cá nhân.

## 3. Đóng góp cụ thể

- Ba chỉ số E1 trong đợt chạy thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200). Trong phạm vi `noi_dia` + `hang_nang`: 92,26%, 21,09% và 3,97% (39/982). Riêng `hang_nang` mở lại 8,23%.
- Tính lại độc lập A2–A4 từ hai CSV, không dùng `mo_hinh`, và thấy khớp: 4.472 đ/việc (simulated), 978 việc thành công; A3 đủ 4 loại; A4 1.185 đ và 2.370 đ cố định mỗi việc. Điền hai câu hỏi A2: chi phí gấp 16,3 lần hoá đơn; làm lại chiếm 51,8% tổng chi phí (simulated).
- Đề xuất hai chỉ số (% yêu cầu ở nhóm can thiệp mà nhân viên mở gợi ý; % đơn lệch tiền qua kiểm tra mẫu hằng tuần) và 11 event có `trace_id`. Viết phần kiểm tra chéo chỉ số với event.
- Bảng lỗi: ghép hai bộ nhãn, đồng thuận 20/20 (100%). Viết 3 dòng khắc phục: ca 20 Hệ thống (khoá chống trùng), ca 19 Giới hạn hệ thống (handoff ngoài 12 tháng), ca 17 Ngầm (kiểm tra mẫu hằng tuần, phiên bản bảng giá).
- Bàn giao D: ngưỡng an toàn 6% cao hơn mức hiện tại 3,97%. Chỉ ra rằng tỉ lệ mở lại không bắt được lỗi Ngầm (ca 5, 17) và hoàn trùng (ca 20), và đề xuất thêm tín hiệu từ `audit_sample_checked` và `refund_ledger_write`.
- Điền mục 4 của `ho_so_launch_v0.md`.

## 4. Bằng chứng

- File: [chi_so.md](chi_so.md) (E1, event, kiểm tra chéo); [bang_loi.md](bang_loi.md) (cột nhãn người 1, đồng thuận, dòng ca 20, 19, 17); phần rà soát CP1 trong [bang_chi_phi.md](bang_chi_phi.md); chú thích tỉ lệ mở lại trong [pilot_plan.yaml](pilot_plan.yaml); mục 4 trong [ho_so_launch_v0.md](ho_so_launch_v0.md).
- Commit: `c03ad3d`, `f93bfaa`, `3ee7f09`, `b50e338` (ghép hai bộ nhãn), `5c977e9`, `98233f8`.

## 5. Công cụ AI đã dùng

- Claude Code (Claude): tính ba chỉ số E1 bằng pandas, tính lại độc lập A2–A4, gắn nhãn 20 ca lỗi (bộ nhãn người 1; Người 4 dùng một chatbot khác cho bộ nhãn người 2), nháp event, chỉ số tự đề xuất, dòng khắc phục, xử lý merge conflict ở `bang_loi.md` và soạn báo cáo này.
- Cách tự kiểm tra: đọc lại lý do gắn nhãn từng ca theo nguyên nhân gốc, không mở nhãn tham khảo trước khi khóa nhãn. Đối chiếu ba chỉ số E1 với số trong hướng dẫn (82,83% · 27,12% · 4,25%). So A2–A4 tính độc lập với số của `lab13.py`. Chạy `yaml.safe_load` sau khi sửa `pilot_plan.yaml`. Dùng `grep` để kiểm tra không còn từ cấm và đủ nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thành phần việc của người gắn nhãn 1 từ CP1 đến CP5. Ba chỉ số E1 khớp số đối chiếu. Đồng thuận nhãn 20/20.
- Hạn chế: hai bộ nhãn cùng được tạo với hỗ trợ của AI nên đồng thuận 100% không chứng minh mạnh được rằng định nghĩa rõ ràng. Phần chấm C7 phụ thuộc hồ sơ của nhóm được chấm.
