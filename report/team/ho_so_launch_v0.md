# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ABCD · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu A2: 4.472 đ/việc (simulated; hoá đơn token+tool 274,7 đ/yc). Phạm vi pilot `noi_dia` + `hang_nang` (A4, gồm 40 trđ cố định/tháng): 4.599 đ/việc ở 45.000 yc/tháng và 5.784 đ/việc ở 22.500 yc/tháng (simulated; biến đổi 3.414 đ/việc). Loại `quoc_te`: 22.515 đ/việc (simulated) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8% / −25,9%), 2. Tỉ lệ xem lại (+40,7% / −20,3%), 3. Lương nhân viên (+23,1% khi tăng 25%); token gấp đôi chỉ +5,6% (simulated) | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | Mốc thủ công: 12.000 đ/việc. Toàn mẫu A2: 0,37× tính riêng trợ lý (4.472 đ/việc), hoặc cả hệ thống gồm 222 ca chuyển nhân viên = 5.865 đ/yc = 0,49× (simulated). Theo loại A3: `noi_dia` 0,22× (2.696 đ), `hang_nang` 0,69× (8.221 đ), `doi_tac` 0,85× (10.215 đ), `quoc_te` 1,88× (22.515 đ) (simulated). Phạm vi pilot có cố định A4: 0,38× (45.000 yc) và 0,48× (22.500 yc) (simulated) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (1.200 yc): chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200). Phạm vi pilot: 92,26% · 21,09% · 3,97% (riêng `hang_nang` mở lại 8,23%). Thêm 2 chỉ số đề xuất (% nhân viên nhóm can thiệp mở gợi ý; % đơn lệch tiền qua kiểm tra mẫu tuần) và 11 event có `trace_id` (`chi_so.md`). Chưa có đối chứng nên chưa nói được trợ lý nâng chỉ số | Xong, có bằng chứng | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi: đồng thuận 20/20 (100%). Đáng lưu ý: lỗi Hệ thống (Ca 20: hoàn trùng, cần `idempotency_key`) và lỗi Ngầm (Ca 17: 212 đơn lệch bảng giá 9 ngày không ai mở lại); đã chốt 5 cách khắc phục đo được | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia theo nhân viên (20+20 cụm, phân tầng 12 depot), phạm vi `noi_dia` + `hang_nang`, MDE +6 điểm (n=859 hiệu dụng/nhóm, DE=6,96; power 0,64 nếu +5 điểm), rollout 10%→25%→50%, 4 luật dừng (an toàn 6%, chi phí biến đổi 8.000 đ, bỏ gợi ý 40%, kiểm tra ngầm/hoàn trùng), `decision_date` 2026-12-21 | Xong, có bằng chứng | Người giữ hồ sơ |
| 7 · Rủi ro kinh tế | B3: Trên 1.200 yêu cầu, giới hạn 2 lượt rẻ nhất cho cả hệ thống, 6.901.220 đ (simulated, gồm xử lý thủ công các ca không thành công). B4: Nếu xem lại 100% gợi ý trong phạm vi pilot, chi phí là 11.743–12.415 đ/việc thành công (simulated) so với mốc thủ công 12.000 đ. Với 15,3 phút làm lại mỗi ca (simulated), ngưỡng hòa vốn khoảng 4,80 phút xem lại/ca (simulated). | Giả lập | Người viết code |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
