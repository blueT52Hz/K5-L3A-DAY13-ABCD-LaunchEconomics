# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: ABCD
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

- Đánh giá tính khả thi kinh tế (Launch Economics) và thiết kế kế hoạch pilot cho trợ lý hoàn phí LogiX-VN tại Gate 2a từ dữ liệu giả lập (1.200 yêu cầu, 1.624 lượt chạy).
- Tiếp cận theo 5 checkpoint (A–E): xây dựng mô hình chi phí mỗi việc thành công, phân tích độ nhạy, phân loại lỗi độc lập theo Google PAIR, thiết kế pilot có đối chứng và tổng hợp hồ sơ launch v0 để duyệt chéo.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **Nhiệm vụ A (CP1 — Mô hình chi phí):** Đã hoàn thành A1 (1,20 · 1,25 · 1,25 — ĐẠT), mô hình `mo_hinh` cho A2 (4.472 đ/việc, simulated), tách 4 loại A3 (đề xuất pilot `noi_dia` + `hang_nang`, loại `quoc_te` 22.515 đ/việc) và phân bổ chi phí cố định A4 (4.599 đ và 5.784 đ/việc ở 45.000 và 22.500 yc/tháng, simulated). Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (CP2 — Độ nhạy):** Đã chạy đủ 9 kịch bản B1, xác định top 3 yếu tố nhạy nhất (số ca làm lại +51,8%/−25,9%, tỉ lệ xem lại +40,7%/−20,3%, lương nhân viên +23,1%, simulated), tính B3 (giới hạn 2 lượt rẻ nhất cả hệ thống: 6.901.220 đ, simulated) và B4 xem lại 100% (11.743 đ ở 9 phút; 12.415 đ ở 15,3 phút, hòa vốn ở 4,80 phút xem lại/ca, simulated). Đã cập nhật hồ sơ và nháp 3 luật dừng trong [pilot_plan.yaml](pilot_plan.yaml). Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- *(Các nhiệm vụ C–E sẽ cập nhật sau các checkpoint tiếp theo.)*

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

...

## 5. Khó khăn và cách xử lý

...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

...

## 8. Tài liệu tham khảo

...
