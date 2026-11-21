# Báo cáo cá nhân — Nguyễn Hoa Thanh Tùng

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoa Thanh Tùng
- MSSV: 2A202603519
- Email: chưa cung cấp
- Vai trong nhóm: Kiểm số, viết code tính B3–B4 và D1, phụ trách chấm C8 tại Gate 2a.

## 2. Phần việc phụ trách

- **CP1:** Kiểm tra cách đọc hai CSV, tính tay một khoản A2 và đối chiếu kết quả A3–A4.
- **CP2–CP3:** Tính B3 cho giới hạn 1/2/3 lượt, tính B4 với hai giả định phút làm lại và chuẩn bị D1.
- **CP4:** Bàn giao năm kết quả D1, phương án chia theo nhân viên và đánh đổi về cỡ mẫu.
- **CP5:** Rà E2, chi phí, phạm vi và cỡ mẫu trong kế hoạch pilot. Kiểm tra YAML và chấm C8 khi nhận hồ sơ nhóm được phân công.

## 3. Đóng góp cụ thể

- **A2–A4:** Đối chiếu 5.600 lượt gọi tool × 15 đ = **84.000 đ**. Bốn dòng A3 và hai kịch bản A4 khớp với `mo_hinh`. Trong phạm vi `noi_dia` và `hang_nang`, A4 cho **4.599 đ** và **5.784 đ** mỗi việc thành công ở hai mức sản lượng (simulated).
- **B3–B4:** Giới hạn 2 lượt có chi phí cả hệ thống thấp nhất trên mẫu (**6.901.220 đ**, simulated). Khi xem lại 100% gợi ý, chi phí là **11.743–12.415 đ/việc thành công** (simulated). Với 15,3 phút làm lại mỗi ca, ngưỡng hòa vốn khoảng **4,80 phút xem lại/ca** (simulated).
- **D1:** Tính đủ năm câu. Đề xuất 20 nhân viên mỗi nhóm, 299 yêu cầu/người, **5.980 yêu cầu thực tế mỗi nhóm** để đạt **859 quan sát hiệu dụng**. Power mục tiêu là 80% ở mức tăng 6 điểm phần trăm và khoảng 64% nếu mức tăng thật là 5 điểm phần trăm.
- **Rà CP5:** Đối chiếu ba dòng E2 với A4, B1, B3 và B4. Làm rõ phạm vi của từng kết quả chi phí, điều kiện an toàn trước khi giảm xem lại và cách dự phóng sản lượng toàn phạm vi từ cửa sổ 14 ngày. `yaml.safe_load` đọc được file, không còn dấu hỏi cần điền, và cả bốn luật dừng đủ bốn vế.
- **Điểm cần chốt trong hồ sơ:** Lịch đang cho một tuần ở bậc 50%. Ngay cả ở mức 1.500 yêu cầu/ngày và chia đều, một tuần chỉ có tối đa 5.250 yêu cầu mỗi nhóm, dưới 5.980. Cần thu đủ mẫu ở bậc 50% rồi dành thời gian theo dõi mở lại sau lần đóng. Khi so chi phí toàn hệ thống, 222 là số yêu cầu **không thành công**, gồm cả ca làm lại và ca chuyển nhân viên.
- **C8:** Chờ hồ sơ nhóm được phân công. Câu hỏi để dùng khi duyệt: Nhóm cần bao nhiêu ca đủ theo dõi ở mỗi nhánh, cần thu trong bao lâu và ai có quyền dừng nếu thiếu mẫu hoặc vượt ngưỡng an toàn?

## 4. Bằng chứng

- [Bảng chi phí A2–A4, B3–B4](bang_chi_phi.md)
- [Mã tính B3–B4 và D1](../../src/lab13.py)
- [Kết quả và bàn giao D1 trong YAML](pilot_plan.yaml)
- [Bảng rủi ro E2 đã đối chiếu](chi_so.md)

## 5. Công cụ AI đã dùng

Dùng ChatGPT (Codex) để hỗ trợ đọc yêu cầu, viết và rà mã tính toán, đối chiếu số liệu và soạn báo cáo. Kiểm tra lại bằng cách chạy `python -B lab13.py` từ `src/`, tính riêng từ hai CSV để đối chiếu, kiểm tra giới hạn cỡ mẫu và đọc YAML bằng `yaml.safe_load`.

## 6. Tự đánh giá

Phân biệt được chi phí trợ lý mỗi việc thành công và chi phí toàn hệ thống có phần xử lý thủ công. Việc rà D1 và lịch pilot cho thấy cần kiểm tra cả cỡ mẫu hiệu dụng lẫn số ca thực tế thu được trong kỳ đo.
