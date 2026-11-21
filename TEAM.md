# Team

## Thông tin nhóm

- Tên nhóm: ABCD
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-ABCD-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/blueT52Hz/K5-L3A-DAY13-ABCD-LaunchEconomics`, nhánh `main` (cập nhật commit chốt ở CP5)

## Thành viên

| STT | Họ tên                | MSSV        | Email                 | GitHub        | Vai trò                                                                                                |
| --: | --------------------- | ----------- | --------------------- | ------------- | ------------------------------------------------------------------------------------------------------ |
|   1 | Vũ Trí Dũng           | 2A202603478 | dungvutri25@gmail.com | VuTriDung1123 | Người viết code (A1–A4, B1–B2, nháp D2, E2, chấm C6)                                                   |
|   2 | Nguyễn Hoa Thanh Tùng | 2A202603519 |                       |               | Người kiểm số & viết code (kiểm A2–A4, B3–B4, D1, chấm C8)                                             |
|   3 | Nguyễn Quang Duy      | 2A202603462 |                       |               | Người gắn nhãn 1 (rubric, gắn nhãn C, E1, chấm C7)                                                     |
|   4 | Khổng Tiến Dương      | 2A202603467 |                       |               | Người gắn nhãn 2, kiêm giữ hồ sơ (TEAM.md, gắn nhãn C, pilot_plan.yaml, hồ sơ launch, group_report.md) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Hai người (Số 1 và Số 2) cùng tham gia viết code và tính chi phí để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## Vũ Trí Dũng - 2A202603478 (Số 1)

### Phần việc phụ trách

- CP1: Cài môi trường, chạy thử `src/lab13.py`; hoàn thiện 3 hàm A1 và chạy 3 phép thử (1,20 · 1,25 · 1,25); viết `mo_hinh`, tính A2 và điền đủ 9 dòng.
- CP2: Chạy B1 đủ 9 kịch bản, B2 đổi một cặp yếu tố và xếp hạng 3 yếu tố nhạy nhất.
- CP3–CP4: Hoàn thiện B1–B2 nếu cần đối chiếu; nháp và chốt 5 câu D2 (đối chứng, ngẫu nhiên hóa, tràn tác động, chốt trước, số cụm).
- CP5: Viết E2 (ít nhất 2 rủi ro có số, dấu hiệu, hành động, vai trò); soát top 3 yếu tố nhạy và số bất lợi từ B4; chấm C6; chạy lại `python lab13.py` từ `src/` trên máy khác.

### Đóng góp cụ thể

- Viết `src/lab13.py` cho A1 (3 phép thử ĐẠT `1,20 · 1,25 · 1,25`), `mo_hinh` A2 (`4.472 đ/việc`, simulated), tách A3, B1 (9 kịch bản) và B2 (top 3 nhạy nhất).
- Chốt 5 câu D2 và `identifiability` trong `pilot_plan.yaml`; viết E2 (3 rủi ro kinh tế) trong `chi_so.md` và đối chiếu số bất lợi B4 trong `ho_so_launch_v0.md`.

### Bằng chứng

- [Báo cáo cá nhân Vũ Trí Dũng](report/team/2A202603478_VuTriDung.md) · [src/lab13.py](src/lab13.py) · [bang_chi_phi.md](report/team/bang_chi_phi.md) · [chi_so.md](report/team/chi_so.md)

## Nguyễn Hoa Thanh Tùng - 2A202603519 (Số 2)

### Phần việc phụ trách

- CP1: Kiểm tra cách đọc hai CSV, chuẩn bị phép tính tay; tính tay một số A2 từ CSV để đối chiếu; tính A3 cho 4 loại và A4 ở 2 mức sản lượng có chi phí cố định.
- CP2: Làm B3 cho giới hạn 1/2/3 lượt (gồm chi phí thủ công ca thất bại) và B4 xem lại 100% với hai giả định phút làm lại.
- CP3–CP4: Hoàn thiện B3–B4 nếu cần đối chiếu; tính đủ 5 phép tính cỡ mẫu D1; bàn giao kết quả D1, cách chia đề xuất và đánh đổi cỡ mẫu/power.
- CP5: Đối chiếu số E2 với B và kiểm tra nhất quán với kế hoạch pilot; soát phạm vi, chi phí và đánh đổi cỡ mẫu; chấm C8; kiểm tra kết quả, `yaml.safe_load` và hết dấu `?`.

### Đóng góp cụ thể

- Đối chiếu phí tool A2, rà A3–A4, viết và chạy B3–B4 cùng năm phép tính D1.
- Rà E2 với A4 và B, kiểm tra YAML và chỉ ra kỳ đo bậc 50% cần dài hơn một tuần để đủ mẫu.

### Bằng chứng

- [Báo cáo cá nhân Nguyễn Hoa Thanh Tùng](report/team/2A202603519_NguyenHoaThanhTung.md)

## Nguyễn Quang Duy - 2A202603462 (Số 3)

### Phần việc phụ trách

- CP1: Đọc rubric và tiêu chí của từng checkpoint; tính sớm 3 chỉ số E1 và tỷ lệ mở lại từ CSV; rà số liệu và yêu cầu gắn nhãn `simulated`.
- CP2: Nháp event và 2 chỉ số bổ sung cho E1.
- CP3–CP4: Gắn nhãn độc lập đủ 20 ca lỗi theo nguyên nhân gốc; tính đồng thuận, ghi quy tắc cho ca lệch, viết 3 dòng khắc phục và tổng hợp `bang_loi.md`; bàn giao tỷ lệ mở lại toàn mẫu và trong phạm vi pilot, đối chiếu tín hiệu an toàn từ C.
- CP5: Chốt E1 (3 chỉ số tính thử, thêm 1 chỉ số sử dụng, 1 chỉ số an toàn, ít nhất 6 event có `trace_id`); soát bằng chứng lỗi, chỉ số, event và nhãn `simulated`; chấm C7 và tổng hợp `phieu_cham.md`; rà đủ 6 file hồ sơ và tên file cá nhân.

### Đóng góp cụ thể

- Tính 3 chỉ số E1 trên toàn mẫu (`82,83% · 27,12% · 4,25%`) và phạm vi pilot (`92,26% · 21,09% · 3,97%`), đề xuất 2 chỉ số bổ sung và 11 event có `trace_id` trong `chi_so.md`.
- Gắn nhãn độc lập 20 ca lỗi (đồng thuận 20/20 = 100%), viết 3 dòng khắc phục (Ca 20, 19, 17) trong `bang_loi.md`; bàn giao tỉ lệ mở lại và tín hiệu an toàn cho D; điền Mục 4 `ho_so_launch_v0.md`.

### Bằng chứng

- [Báo cáo cá nhân Nguyễn Quang Duy](report/team/2A202603462_NguyenQuangDuy.md) · [bang_loi.md](report/team/bang_loi.md) · [chi_so.md](report/team/chi_so.md)

## Khổng Tiến Dương - 2A202603467 (Số 4)

### Phần việc phụ trách

- CP1: Điền vai và thông tin nhóm trong `TEAM.md`, mở khung hồ sơ launch và báo cáo nhóm; chuẩn bị khung YAML và các mục hồ sơ cần số từ A; nhận số A2–A4, điền chi phí và so sánh với nhân viên tự làm trong `ho_so_launch_v0.md`.
- CP2: Nhận top 3 và số B3/B4 để cập nhật hồ sơ và nháp luật dừng.
- CP3–CP4: Gắn nhãn độc lập cùng 20 ca lỗi theo nguyên nhân gốc; thống nhất ca lệch, viết 2 dòng khắc phục, đưa lỗi đáng lưu ý vào hồ sơ; chốt `pilot_plan.yaml` (ghi D1/D2 trong chú thích, điền rollout, rollback, ngày quyết định, kiểm tra `yaml.safe_load`).
- CP5: Nhận E1/E2 cập nhật hai mục chỉ số và rủi ro; gửi `ho_so_launch_v0.md` một trang, 7 mục (mỗi mục có số chính, trạng thái, vai trò phụ trách); trình hồ sơ nhóm và điều phối trả lời; chốt `group_report.md`, cập nhật đóng góp trong `TEAM.md`, điều phối commit/push và kiểm tra quyền xem repo.

### Đóng góp cụ thể

- Điền thông tin nhóm trong `TEAM.md`, dựng và cập nhật xuyên suốt `ho_so_launch_v0.md` (Mục 1, 3, 5, 6, 7 và đề xuất **Go có điều kiện**) và `group_report.md`.
- Gắn nhãn độc lập 20 ca lỗi (đồng thuận 20/20 = 100%) và viết 2 dòng khắc phục (Ca 1, Ca 18) trong `bang_loi.md`; chốt `pilot_plan.yaml` (scope, `staff`, MDE `+6 điểm`, kéo dài bậc 50% thành 2 tuần + 7 ngày theo dõi, `decision_date: 2026-12-28`, 4 luật dừng, rollback 30 phút).

### Bằng chứng

- [Báo cáo cá nhân Khổng Tiến Dương](report/team/2A202603467_KhongTienDuong.md) · [ho_so_launch_v0.md](report/team/ho_so_launch_v0.md) · [pilot_plan.yaml](report/team/pilot_plan.yaml) · [group_report.md](report/team/group_report.md)
