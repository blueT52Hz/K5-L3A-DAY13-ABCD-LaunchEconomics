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
- **CP3 (Bước 5):** Gắn nhãn độc lập đủ 20 ca lỗi vào cột `Nhãn người 2` trong `report/team/bang_loi.md`.
- **CP4–CP5 (chuẩn bị sẵn):** Điền sẵn `rollback` và `simulated_inputs` trong `pilot_plan.yaml`; chuẩn bị sẵn khung kết quả, khó khăn, hạn chế và tài liệu tham khảo trong `group_report.md`. *(Sẽ cập nhật phần chốt số liệu CP3–CP5 sau khi nhóm hoàn tất.)*

## 4. Bằng chứng

- Các file đã cập nhật: `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/pilot_plan.yaml`, `report/team/bang_loi.md`.
- Commit CP1: `a897283`; Commit CP2: `1e6c757`.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI để hỗ trợ tổng hợp cấu trúc hồ sơ, đối chiếu số liệu từ `bang_chi_phi.md` / `src/lab13.py` và rà lỗi định dạng Markdown/YAML.
- Tự kiểm tra bằng cách chạy `cd src && python lab13.py`, kiểm tra `yaml.safe_load` trên `report/team/pilot_plan.yaml`, và đối chiếu từng con số với bảng A2–A4, B1–B4, cũng như rà nhãn `simulated` và quy tắc chỉ lập kế hoạch pilot.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ và đúng vai trò Người gắn nhãn 2 kiêm giữ hồ sơ ở CP1–CP2 và Bước 5 CP3; đang chờ đồng đội hoàn tất phần phụ thuộc để chốt CP3–CP5.
