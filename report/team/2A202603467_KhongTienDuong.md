# Báo cáo cá nhân — Khổng Tiến Dương - 2A202603467

## 1. Thông tin thành viên

- Họ tên: Khổng Tiến Dương
- MSSV: 2A202603467
- Email:
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (Số 4)

## 2. Phần việc phụ trách

- **CP1:** Điền vai và thông tin nhóm trong `TEAM.md`; mở khung hồ sơ launch (`report/team/ho_so_launch_v0.md`) và báo cáo nhóm (`report/team/group_report.md`); chuẩn bị khung `report/team/pilot_plan.yaml`; nhận số A2–A4 điền chi phí và so sánh với nhân viên tự làm.
- **CP2:** Nhận top 3 và số B3/B4 để cập nhật hồ sơ và nháp 3 luật dừng trong `report/team/pilot_plan.yaml`.
- **CP3:** Gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc; cùng thống nhất ca lệch, viết 2 dòng khắc phục và đưa lỗi đáng lưu ý vào hồ sơ.
- **CP4:** Chốt `report/team/pilot_plan.yaml` (ghi D1/D2 trong chú thích, điền rollout, rollback, ngày quyết định, kiểm tra `yaml.safe_load`).
- **CP5:** Nhận E1/E2 cập nhật hồ sơ; hoàn thiện `ho_so_launch_v0.md` một trang, 7 mục và đề xuất Gate 2a; trình bày và điều phối trả lời khi duyệt chéo; chốt `group_report.md`, cập nhật đóng góp trong `TEAM.md`.

## 3. Đóng góp cụ thể

- **CP1:** Cập nhật thông tin nhóm `ABCD`, lớp `L3A`, bảng phân công 4 thành viên trong `TEAM.md`; điền Mục 1 và Mục 3 trong `ho_so_launch_v0.md` từ số A2–A4; mở khung `group_report.md` và `pilot_plan.yaml` (trường `owner`, `scope`).
- **CP2:** Cập nhật tóm tắt Nhiệm vụ B trong `group_report.md` và đối chiếu Mục 7 + 3 luật dừng trong `pilot_plan.yaml`.
- **CP3:** Gắn nhãn độc lập đủ 20 ca lỗi vào cột `Nhãn người 2` trong `report/team/bang_loi.md` (đồng thuận 20/20 = 100% với Người gắn nhãn 1); viết 2 dòng khắc phục đo được cho Ca 1 (`Do người dùng`) và Ca 18 (`Ngữ cảnh`); cập nhật Mục 5 vào `ho_so_launch_v0.md`.
- **CP4:** Chốt `pilot_plan.yaml` từ D1, D2 và tín hiệu an toàn C (`assignment.unit = staff`, `mde = 0.06`, `n_per_arm = 859`, `design_effect = 6.96`, `clusters_per_arm = 20`, 4 luật dừng, `rollback` 30 phút); sửa lại lịch `rollout: [0.10, 0.25, 0.50, 0.50]` kéo dài bậc 50% thành 2 tuần để đủ `≥ 5.980` yêu cầu/nhóm + 7 ngày theo dõi `mo_lai_trong_7_ngay` và chốt `decision_date = 2026-12-28`; cập nhật Mục 6 của `ho_so_launch_v0.md`.
- **CP5:** Nhận kết quả E1–E2 từ `chi_so.md`, hoàn thiện Mục 7 và chốt đề xuất **Go có điều kiện** (kèm 3 điều kiện, người phụ trách, ngày kiểm tra) trong `ho_so_launch_v0.md`; hoàn thiện `group_report.md` và tổng hợp đóng góp 4 thành viên trong `TEAM.md`.

## 4. Bằng chứng

- Các file đã cập nhật: `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/pilot_plan.yaml`, `report/team/bang_loi.md`, `report/team/2A202603467_KhongTienDuong.md`.
- Các commit đã ghi nhận: `a897283` (CP1), `1e6c757` (CP2), `c50ccfa` (CP3 Bước 5 + khung CP4–CP5), `87980ea` (CP3 Bước 6), `ea74563` & `b2a5d53` (CP4).

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Antigravity / Gemini) để hỗ trợ dựng khung hồ sơ, gắn nhãn độc lập bộ 20 ca lỗi (theo đúng định nghĩa nguyên nhân gốc Google PAIR, không xem nhãn tham khảo trước), đối chiếu số liệu từ `bang_chi_phi.md` / `chi_so.md` / `src/lab13.py` và rà lỗi định dạng Markdown/YAML.
- Tự kiểm tra bằng cách chạy `cd src && python lab13.py`, chạy `yaml.safe_load` và kiểm tra không còn `?` ngoài chú thích trên `report/team/pilot_plan.yaml`, kiểm tra lại công thức thời gian thu mẫu ở bậc `50%` (`5.980 / 613,75 ≈ 9,74 ngày` → cần 2 tuần + 7 ngày theo dõi mở lại), rà nhãn `simulated` và kiểm tra không có từ cấm trong `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ vai trò Người gắn nhãn 2 kiêm giữ hồ sơ từ CP1 đến CP5, bảo đảm 6 file hồ sơ trong `report/team/` thống nhất số liệu và sẵn sàng cho phần trình bày, duyệt chéo tại buổi (`phieu_cham.md`).
