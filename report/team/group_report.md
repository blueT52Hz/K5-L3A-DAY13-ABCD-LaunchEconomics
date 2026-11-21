# Báo cáo nhóm ABCD · L3A

## 1. Thông tin nhóm

Thành viên và đóng góp chờ nhóm xác nhận trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí và thiết kế pilot có đối chứng cho trợ lý hoàn phí LogiX-VN. Phân tích 1.624 lượt chạy và 1.200 yêu cầu giả lập. Chọn phạm vi theo chi phí, tỷ lệ thành công và khả năng kiểm soát rủi ro.

## 3. Giải pháp

- A và B. Cộng token, tool và phút nhân viên. So ba giới hạn chạy và phân bổ chi phí cố định ở hai mức khối lượng. [Bảng chi phí](bang_chi_phi.md)
- C. Bản thực hành cá nhân dùng hai lượt AI độc lập, đồng thuận 20/20 ca. Bảng có năm biện pháp khắc phục, mỗi loại lỗi một biện pháp. [Bảng lỗi](bang_loi.md)
- D. So cỡ mẫu theo yêu cầu, nhân viên và depot. Chọn ngẫu nhiên theo nhân viên với 20 cụm mỗi nhóm. [Kế hoạch pilot](pilot_plan.yaml)
- E. Tính ba chỉ số mẫu, đặc tả sự kiện và điều kiện mở bậc. [Chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md)

## 4. Kết quả

Chi phí biến đổi toàn mẫu là 4.472 đ mỗi việc thành công (simulated). Trong phạm vi pilot, A4 cho 4.599 đ mỗi việc tại 45.000 yêu cầu toàn công ty mỗi tháng và 5.784 đ tại nửa khối lượng, đã gồm cố định (simulated). Đề xuất Go có điều kiện cho nội địa và hàng nặng. Kết quả duyệt chéo chờ hội đồng thực tế.

## 5. Khó khăn và cách xử lý

Mã khởi đầu dừng ở lỗi `NotImplementedError` tại A1. Sau khi bổ sung các phép tính, lệnh `python lab13.py` trong `src/` cho 1,20 · 1,25 · 1,25. A4 được đối chiếu theo sản lượng thành công dự phóng. Cần chạy lại trên máy thứ hai theo checklist.

## 6. Tổng hợp đóng góp

Trợ lý AI hỗ trợ mã tính toán, nháp kỹ thuật và hai lượt gắn nhãn ở bản thực hành cá nhân. Thành viên xác nhận phần việc và bằng chứng trong [TEAM.md](../../TEAM.md). Mỗi người tạo [báo cáo cá nhân](MSSV_HoTen.md) theo tên quy định và ghi cách tự kiểm tra đầu ra.

## 7. Hạn chế và hướng cải thiện

Mẫu chạy thử chỉ có một nhóm và thời gian nhân viên là giả lập. Pilot cần thời gian thao tác thật, xác nhận lưu lượng từng người và chấp nhận MDE 6 điểm. Power ở mức tăng 5 điểm chỉ khoảng 0,64.

## 8. Tài liệu tham khảo

[Hướng dẫn buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) · [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Mã tính](../../src/lab13.py)
