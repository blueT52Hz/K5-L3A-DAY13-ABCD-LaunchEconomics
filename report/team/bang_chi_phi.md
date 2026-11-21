# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? 4.472 đ ÷ 274,7 đ ≈ **16,3 lần** (simulated). Phần lớn chi phí là giờ của nhân viên, không phải token.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại: 2.264.000 đ, chiếm 51,8%** tổng chi phí (simulated). Xem lại chiếm 40,7% (simulated), token 5,6%, tool 1,9%.

**Rà soát CP1 của Người gắn nhãn 1.** Người gắn nhãn 1 tính lại độc lập từ hai CSV, không dùng `mo_hinh`. Mọi số A2, A3, A4 khớp với bảng: tổng 4.373.585 đ, 978 việc thành công, 4.472 đ/việc; A3 khớp cả 4 loại; A4 ra 1.185 đ và 2.370 đ cố định mỗi việc. Mọi số dùng `phut_xem_lai_simulated` hoặc `phut_lam_lai_simulated` đều đã có nhãn `simulated`. Token, tool và số việc thành công đo từ trace nên không gắn nhãn.

**Đối chiếu A2 của Nguyễn Hoa Thanh Tùng (2A202603519).** Cộng cột `tool_calls` trên cả 1.624 lượt trong `logix_runs.csv`, kể cả lượt lỗi, được 5.600 lần gọi. Tính tay: 5.600 × 15 đ/lần = **84.000 đ**.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

**Cách tính.** Ghép hai CSV theo `request_id`, giữ nguyên ô trống trong `quyet_dinh_xem_lai`. Cộng chi phí token và tool của mọi lượt chạy và tiền xem lại, làm lại, rồi chia cho số yêu cầu có `ket_qua == 'thanh_cong'` trong từng loại. Tỷ lệ so với 12.000 đ dùng chi phí trợ lý mỗi việc thành công, chưa gồm chi phí cố định và chi phí xử lý thủ công các yêu cầu không thành công.

- Đề xuất pilot cho `noi_dia` và `hang_nang`. Loại `quoc_te` vì chỉ thành công 27,3% và tốn 22.515 đ/việc (simulated), gấp 1,88× mốc thủ công. Thử lại ít hiệu quả: tỷ lệ `ok` theo lượt giảm từ 45/150 (30,0%) xuống 12/105 (11,4%) rồi 2/93 (2,2%).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

**Cách tính.** Trong mẫu, phạm vi pilot có 982 yêu cầu và 900 việc thành công. Chi phí biến đổi là 3.072.513,274 đ ÷ 900 = 3.413,904 đ/việc (simulated). Dự phóng số việc thành công bằng sản lượng tháng toàn hệ thống × 900/1.200, rồi chia 40 triệu đ cho số việc đó để phân bổ chi phí cố định.

- Sau khi cộng chi phí cố định, chi phí mỗi việc thành công vẫn dưới 12.000 đ ở cả hai mức sản lượng. Khi giảm từ 45.000 xuống 22.500 yêu cầu/tháng, chi phí cố định mỗi việc tăng gấp đôi và tổng chi phí tăng từ 4.599 đ lên 5.784 đ/việc (simulated).

**Bàn giao CP1 của Nguyễn Hoa Thanh Tùng.** Sau khi ba phép thử A1 đạt, kết quả `mo_hinh` khớp với phép tính độc lập từ CSV: phí tool A2 là 84.000 đ, đủ bốn dòng A3 và cả hai mức sản lượng A4 khớp theo độ làm tròn trong bảng.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | **4.111 đ** |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Chi phí cả hệ thống bằng chi phí trợ lý cộng 12.000 đ cho mỗi yêu cầu không thành công.

- **Giới hạn 2 lượt** rẻ nhất cho công ty, **6.901.220 đ** (simulated). Giới hạn 1 lượt cho chi phí trợ lý mỗi việc thành công thấp nhất (**4.111 đ**, simulated), nhưng để lại thêm **85 yêu cầu** cho nhân viên xử lý so với giới hạn 2 lượt.

## B4 · Nếu phải xem lại tất cả

Trong 982 yêu cầu `noi_dia` và `hang_nang`, 948 yêu cầu có ít nhất một lượt `ok`, 48 ca phải làm lại và 900 yêu cầu thành công. Token và tool của mọi lượt chạy tốn 224.513 đ. Xem lại từng yêu cầu có gợi ý trong 5 phút tốn 9.480.000 đ (simulated). Dùng 9 phút làm lại theo đề và 15,3 phút làm lại trung bình trên toàn mẫu từ `phut_lam_lai_simulated`.

| Phút làm lại mỗi ca | Chi phí làm lại (simulated) | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) | Phút xem lại hòa vốn mỗi ca (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 9 phút | 864.000 đ | 11.743 đ | 0,98× | 5,12 |
| 15,3 phút (simulated) | 1.468.800 đ | 12.415 đ | 1,03× | 4,80 |

- Xem lại 100% gợi ý ở mức 5 phút/ca cho chi phí **11.743 đ/việc** nếu làm lại 9 phút và **12.415 đ/việc** nếu làm lại 15,3 phút (simulated).
- Pilot cần đo phút xem lại, phút làm lại và tỷ lệ xem lại có thể giảm mà vẫn đạt ngưỡng an toàn. Nếu vẫn xem lại 100% và mất 15,3 phút làm lại mỗi ca, thời gian xem lại cần ở khoảng **4,80 phút/ca** hoặc thấp hơn để hòa vốn (simulated).
