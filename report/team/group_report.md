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
- **Nhiệm vụ C (CP3 — Phân loại lỗi):** Hai người gắn nhãn (Nguyễn Quang Duy và Khổng Tiến Dương) gắn độc lập 20 ca lỗi đạt đồng thuận 20/20 (100%) và hoàn tất bảng khắc phục 5 loại lỗi (mỗi dòng có event, ngưỡng, tần suất và vai trò phụ trách) trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Kế hoạch pilot):** Đã hoàn thiện [pilot_plan.yaml](pilot_plan.yaml) từ D1, D2 và tín hiệu an toàn của C: chia ngẫu nhiên theo nhân viên (`20 + 20` cụm, phân tầng 12 depot), `MDE = +6 điểm` (`859` quan sát hiệu dụng/nhóm, `DE = 6,96`, chấp nhận power `0,64` nếu hiệu ứng thật `+5 điểm`), rollout `[0.10, 0.25, 0.50]`, 4 luật dừng đủ 4 vế và `rollback` trong 30 phút.
- **Nhiệm vụ E (CP5 — Chỉ số, rủi ro và hồ sơ launch v0):** Đã cập nhật Mục 1, 2, 3, 7 trong [ho_so_launch_v0.md](ho_so_launch_v0.md); chờ [chi_so.md](chi_so.md) (E1, E2) và [phieu_cham.md](phieu_cham.md) để chốt đề xuất Gate 2a.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **Chi phí (A2–A4, simulated):** Toàn mẫu `4.472 đ/việc` (`0,37×` mốc `12.000 đ`); phạm vi pilot `noi_dia` + `hang_nang` gồm chi phí cố định 40 triệu đ/tháng là `4.599 đ/việc` (`0,38×`) ở 45.000 yc/tháng và `5.784 đ/việc` (`0,48×`) ở 22.500 yc/tháng; loại `quoc_te` (`22.515 đ/việc`, `1,88×`).
- **Độ nhạy (B1–B4, simulated):** Top 3 yếu tố nhạy nhất là số ca làm lại (`+51,8% / −25,9%`), tỉ lệ xem lại (`+40,7% / −20,3%`), lương nhân viên (`+23,1%`). Giới hạn 2 lượt tối ưu chi phí cả hệ thống (`6.901.220 đ`). Nếu xem lại 100% và làm lại 15,3 phút/ca, chi phí lên `12.415 đ/việc` (`1,03×`), ngưỡng hòa vốn xem lại khoảng `4,80 phút/ca`.
- **Lỗi, Pilot, Chỉ số & Duyệt chéo (C–E):** *[Chờ hoàn thiện CP3–CP5 để điền số liệu và đề xuất cuối Go / Go có điều kiện / No-go]*.

## 5. Khó khăn và cách xử lý

- Dữ liệu thời gian xem lại/làm lại mang tính giả lập (`_simulated`), do đó mọi kết quả chi phí đều phải gắn nhãn `simulated` và đặt luật dừng theo dõi sát thời gian xem lại thực tế trong pilot.
- *[Bổ sung thêm khó khăn/xử lý từ CP3–CP5 nếu có]*.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Mô hình chi phí hiện dựa trên mẫu 1.200 yêu cầu và hai cột `_simulated` (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`), chưa có dữ liệu đo thực tế từ đợt pilot có đối chứng.
- **Hướng cải thiện:** *[Bổ sung đánh đổi cỡ mẫu/power từ D1/D2 và hướng xử lý lỗi từ C sau khi chốt CP3–CP4]*.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`)
