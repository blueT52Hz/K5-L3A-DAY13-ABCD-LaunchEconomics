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

- **Nhiệm vụ A (CP1 — Mô hình chi phí):** Đã hoàn thành A1 (1,20 · 1,25 · 1,25 — ĐẠT), mô hình `mo_hinh` cho A2 (4.472 đ/việc, simulated), tách 4 loại A3 (đề xuất pilot `noi_dia` + `hang_nang`, loại `quoc_te` vì chi phí 22.515 đ/việc, simulated) và phân bổ chi phí cố định A4 (4.599 đ và 5.784 đ/việc ở 45.000 và 22.500 yc/tháng, simulated). Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (CP2 — Độ nhạy):** Đã chạy đủ 9 kịch bản B1, xác định top 3 yếu tố nhạy nhất (số ca làm lại +51,8%/−25,9%, tỉ lệ xem lại +40,7%/−20,3%, lương nhân viên +23,1%, simulated), tính B3 (giới hạn 2 lượt rẻ nhất cả hệ thống: 6.901.220 đ, simulated) và B4 xem lại 100% (11.743 đ ở 9 phút; 12.415 đ ở 15,3 phút, hòa vốn ở 4,80 phút xem lại/ca, simulated). Đã cập nhật hồ sơ và nháp 3 luật dừng trong [pilot_plan.yaml](pilot_plan.yaml). Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3 — Phân loại lỗi):** Hai người gắn nhãn (Nguyễn Quang Duy và Khổng Tiến Dương) gắn độc lập 20 ca lỗi đạt đồng thuận 20/20 (100%) và hoàn tất bảng khắc phục 5 loại lỗi (mỗi dòng có event, ngưỡng, tần suất và vai trò phụ trách) trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Kế hoạch pilot):** Đã hoàn thiện [pilot_plan.yaml](pilot_plan.yaml) từ D1, D2 và tín hiệu an toàn của C: chia ngẫu nhiên theo nhân viên (`20 + 20` cụm, phân tầng 12 depot), `MDE = +6 điểm` (`859` quan sát hiệu dụng/nhóm, `DE = 6,96`, chấp nhận power `0,64` nếu hiệu ứng thật `+5 điểm`), rollout `[0.10, 0.25, 0.50, 0.50]` (kéo dài bậc 50% thành 2 tuần để đủ `≥ 5.980` yc/nhóm + `7` ngày theo dõi `mo_lai_trong_7_ngay`, `decision_date 2026-12-28`), 5 luật dừng đủ 4 vế và `rollback` trong 30 phút.
- **Nhiệm vụ E (CP5 — Chỉ số, rủi ro và hồ sơ launch v0):** Hoàn thành 3 chỉ số tính thử + 2 chỉ số đề xuất và 11 event có `trace_id` (E1), 3 dòng rủi ro kinh tế (E2) trong [chi_so.md](chi_so.md); tổng hợp thành hồ sơ một trang 7 mục kèm đề xuất **Go có điều kiện** trong [ho_so_launch_v0.md](ho_so_launch_v0.md). Phiếu duyệt chéo tại buổi lưu ở [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **Chi phí (A2–A4, simulated):** Toàn mẫu `4.472 đ/việc` (`0,37×` mốc `12.000 đ`; cả hệ thống gồm 222 yêu cầu không thành công là `5.865 đ/yc` = `0,49×`). Phạm vi pilot `noi_dia` + `hang_nang` gồm cố định 40 triệu đ/tháng là `4.599 đ/việc` (`0,38×`) ở 45.000 yc/tháng và `5.784 đ/việc` (`0,48×`) ở 22.500 yc/tháng; loại `quoc_te` (`22.515 đ/việc`, `1,88×`).
- **Độ nhạy (B1–B4, simulated):** Top 3 yếu tố nhạy nhất là số ca làm lại (`+51,8% / −25,9%`), tỉ lệ xem lại (`+40,7% / −20,3%`), lương nhân viên (`+23,1%`). Giới hạn 2 lượt tối ưu chi phí cả hệ thống (`6.901.220 đ`). Nếu xem lại 100% và làm lại 15,3 phút/ca, chi phí lên `12.415 đ/việc` (`1,03×`), ngưỡng hòa vốn xem lại khoảng `4,80 phút/ca`.
- **Lỗi (C):** Đồng thuận `20/20 (100%)` trên 20 ca lỗi Google PAIR; chốt 5 dòng khắc phục đo được qua event và vai trò phụ trách trong [bang_loi.md](bang_loi.md).
- **Kế hoạch pilot (D):** Chia ngẫu nhiên theo nhân viên (`20 + 20` cụm, phân tầng 12 depot), `MDE = +6 điểm` (`859` hiệu dụng/nhóm, `DE = 6,96`, `≥ 5.980` yc/nhóm), rollout `10% → 25% → 50%` (kéo dài bậc 50% thành 2 tuần) + 7 ngày theo dõi mở lại, `decision_date: 2026-12-28`, 5 luật dừng và rollback 30 phút.
- **Chỉ số & Rủi ro (E1–E2):** Đợt chạy thử đạt chỉ số chính `82,83%` (`92,26%` trong phạm vi pilot), bỏ qua gợi ý `27,12%` (`21,09%` trong pilot), mở lại 7 ngày `4,25%` (`3,97%` trong pilot; riêng `hang_nang` `8,23%`); 11 event có `trace_id` và 3 rủi ro kinh tế.
- **Đề xuất Gate 2a:** **Go có điều kiện** (chỉ mở pilot với 3 điều kiện về giới hạn 2 lượt + phạm vi, sửa lỗi hoàn trùng/cache bảng giá/validation trước ngày mở, và đo thật phút xem lại/làm lại + tách theo dõi `hang_nang`).
- **ABCD chấm LangChai:** **30/30**, đề xuất **Go có điều kiện** cho pilot nội địa và hàng nặng. [Phiếu ABCD chấm LangChai](phieu_cham.md)
- **Hội đồng LangChai chấm ABCD:** **25/30** (C6 **10/10**, C7 **5/10**, C8 **10/10**), đề xuất **Go có điều kiện**. Hội đồng yêu cầu gắn nhãn `simulated` cho cột Thay đổi (%) ở B1 và chốt luật dừng riêng cho hàng nặng trước khi mở pilot. Tỷ lệ mở lại của hàng nặng là **13/158 (8,23%)**, cao hơn tỷ lệ gộp **39/982 (3,97%)**. [Phiếu LangChai chấm ABCD](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/blob/079dd5f92c125d52097c2877e30433bd5a02a650/report/team/phieu_cham.md#L5-L12)
- **Cập nhật sau duyệt chéo:** Đã gắn nhãn `simulated` cho cột Thay đổi (%) ở B1 và bổ sung luật dừng riêng cho hàng nặng vào `pilot_plan.yaml`. Tính riêng tỷ lệ mở lại của hàng nặng trên các ca đã đủ 7 ngày theo dõi. Nếu vượt **6%** trong **3 ngày kiểm tra liên tiếp**, Giám đốc vận hành tạm dừng trợ lý cho hàng nặng trong vòng **30 phút** và chuyển các ca này về CSKH. [Gợi ý của hội đồng LangChai](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/blob/079dd5f92c125d52097c2877e30433bd5a02a650/report/team/phieu_cham.md#L10-L12)

## 5. Khó khăn và cách xử lý

- Dữ liệu thời gian xem lại/làm lại mang tính giả lập (`_simulated`), do đó mọi kết quả chi phí đều gắn nhãn `simulated`, đồng thời thiết kế event đo thật (`staff_review_decision.phut_xem_lai`, `staff_rework_completed.phut_lam_lai`) và luật dừng bám sát ngưỡng hòa vốn `4,80 phút/ca`.
- Chia theo depot chỉ có 6 cụm/nhóm (không đủ cỡ mẫu), còn bậc `50%` nếu chạy 1 tuần chỉ đạt tối đa ~`4.296–5.250` yc/nhóm (`< 5.980`). Nhóm chọn chia theo nhân viên (`20 + 20` cụm), nâng `MDE` lên `+6 điểm` (nêu rõ đánh đổi power `0,64` nếu hiệu ứng thật `+5 điểm`) và kéo dài bậc `50%` thành 2 tuần + 7 ngày theo dõi.
- Các lần làm việc song song phát sinh xung đột gộp trên file chung (`bang_loi.md`, `ho_so_launch_v0.md`, `pilot_plan.yaml`), được xử lý bằng cách `git pull --rebase` và đối chiếu lại toàn bộ số liệu sau mỗi checkpoint.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Mô hình chi phí dựa trên mẫu 1.200 yêu cầu và hai cột `_simulated`; dữ liệu chạy thử chưa có nhóm đối chứng nên chưa thể kết luận tác động nhân quả; chia theo nhân viên trong cùng depot còn nguy cơ tràn tác động nhẹ; hai bộ nhãn C đạt 100% khi dùng hỗ trợ AI nên cần xác nhận thêm trên dữ liệu thực.
- **Hướng cải thiện:** Bắt buộc dùng `staff_id` khóa quyền truy cập trợ lý và ghi log để kiểm soát tràn tác động; thay thế toàn bộ số `_simulated` bằng log event đo thật ngay từ tuần 1 pilot; bổ sung kiểm tra mẫu ngẫu nhiên hằng tuần (`audit_sample_checked`) và đối soát `refund_ledger_write` để bắt lỗi Ngầm và hoàn trùng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`)
