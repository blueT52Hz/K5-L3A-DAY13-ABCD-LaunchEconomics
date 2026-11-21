# Bảng chi phí · Nhiệm vụ A và B

Số được tính bằng src/lab13.py trên dữ liệu giả lập của đề.

## A1 · Ba phép thử đáp án biết trước

Ba phép thử đáp án biết trước: ĐẠT (1,20 · 1,25 · 1,25)

## A2 · Chi phí từ trace

| Khoản | Giá trị (đ nếu là tiền) | Nguồn hoặc nhãn |
| --- | --- | --- |
| Token | 245.585 | logix_runs.csv |
| Tool | 84.000 | logix_runs.csv |
| Trong đó, lượt 2 và 3 | 93.804 | Đã gồm trong token và tool |
| Xem lại | 1.780.000 | simulated |
| Làm lại | 2.264.000 | simulated |
| Tổng chi phí | 4.373.585 | simulated |
| Số việc thành công | 978 | ket_qua |
| Chi phí mỗi việc thành công | 4.472 | simulated |
| Hóa đơn máy mỗi yêu cầu | 274,7 | Token và tool / số yêu cầu |

Chi phí mỗi việc thành công cao gấp 16,3 lần hóa đơn máy mỗi yêu cầu. Làm lại chiếm tỷ trọng lớn nhất, 51,8% (simulated).

## A3 · Tách theo loại

| Loại | Yêu cầu | Thành công | Lượt/yêu cầu | Đ/việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | --- | --- | --- | --- | --- |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

Quốc tế tốn 22.515 đ/việc (simulated), đạt 27,3% việc thành công. Tỷ lệ lượt ok trong số ca đến từng lượt (30,0% · 11,4% · 2,2%) cho thấy lợi ích thấp ở lượt 2 và 3.

## A4 · Phân bổ 40 triệu đ chi phí cố định mỗi tháng

Hai dòng dự phóng từ 900 việc thành công nội địa và hàng nặng trên 1.200 yêu cầu toàn mẫu. Chi phí biến đổi trong phạm vi là 3.072.513 đ cho 900 việc thành công (simulated).

| Yêu cầu/tháng toàn công ty | Việc thành công/tháng | Cố định/việc (đ) | Đ/việc gồm cố định (simulated) | So với làm tay (simulated) |
| --- | --- | --- | --- | --- |
| 45.000 | 33.750 | 1.185 | 4.599 | 0,38× |
| 22.500 | 16.875 | 2.370 | 5.784 | 0,48× |

Cả hai mức khối lượng vẫn dưới 12.000 đ. Ngưỡng hòa vốn theo chi phí mỗi việc thành công là khoảng 6.212 yêu cầu toàn công ty mỗi tháng, giả sử cơ cấu và hiệu suất giữ nguyên (simulated). Ngưỡng này chưa cộng phần nhân viên tiếp nhận.

## B1 và B2 · Độ nhạy

| Kịch bản | Đ/việc thành công (simulated) | So với A2 (simulated) |
| --- | --- | --- |
| Token ×2 | 4.723 | +5,6% |
| Token ÷2 | 4.346 | -2,8% |
| Xem lại ×2 | 6.292 | +40,7% |
| Xem lại ÷2 | 3.562 | -20,3% |
| Làm lại ×2 | 6.787 | +51,8% |
| Làm lại ÷2 | 3.315 | -25,9% |
| Lương +25% | 5.506 | +23,1% |
| Tối đa 2 lượt | 4.237 | -5,2% |
| Tối đa 1 lượt | 4.111 | -8,1% |
| B2 · Token ×2 và xem lại ×2 | 6.543 | +46,3% |

Ba yếu tố ảnh hưởng mạnh nhất trong các mức đã thử là làm lại, xem lại và lương nhân viên. Tác động của cặp bằng tổng tác động riêng khi số việc thành công giữ nguyên.

## B3 · Giới hạn chạy lại

| Giới hạn | Trợ lý (đ, simulated) | Không thành công | Cả hệ thống (đ, simulated) | Đ/việc thành công (simulated) |
| --- | --- | --- | --- | --- |
| 1 | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 | 4.373.585 | 222 | 7.037.585 | 4.472 |

Hai lượt cho tổng chi phí hệ thống thấp nhất. Giới hạn một lượt làm giảm chi phí mỗi việc thành công nhưng có thêm 85 yêu cầu cần nhân viên xử lý.

## B4 · Xem lại 100% trong phạm vi

Với 948 ca xem lại × 5 phút, 48 ca làm lại × 9 phút và 224.513 đ tiền máy, chi phí là 11.743 đ/việc, bằng 0,98× làm tay, trước chi phí cố định (simulated). Pilot cần đo phút thật và kiểm tra khi nào có thể giảm duyệt an toàn.
