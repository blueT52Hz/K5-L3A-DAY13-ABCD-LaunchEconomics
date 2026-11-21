# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu ở nhóm can thiệp mà nhân viên mở gợi ý của trợ lý | Số `refund_request_created` có `arm = can_thiep` và có `agent_suggestion_shown` cùng `trace_id`, chia số `refund_request_created` có `arm = can_thiep` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm mà khách không mở lại) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn trong mẫu kiểm tra của tuần | Không cần tính |

Cả ba chỉ số tính từ cột đo thật (`dong_trong_24h`, `mo_lai_trong_7_ngay`, `duoc_xem_lai`, `quyet_dinh_xem_lai`), không dùng cột `_simulated`. Người gắn nhãn 1 tính bằng pandas, đọc `logix_requests.csv` với `keep_default_na=False`.

**Trong phạm vi pilot `noi_dia` + `hang_nang` (982 yêu cầu):** chỉ số chính 92,26% (906/982) · bỏ qua gợi ý 21,09% (27/128) · mở lại trong 7 ngày **3,97% (39/982)**. Tỉ lệ mở lại theo loại: noi_dia 3,16% (26/824) · hang_nang 8,23% (13/158) · quoc_te 6,00% (9/150) · doi_tac 4,41% (3/68). Ngưỡng luật dừng an toàn trong `pilot_plan.yaml` phải đặt trên mức 3,97% hiện tại, nếu không pilot sẽ dừng ngay tuần đầu.

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, depot, loai, so_tien_vnd, arm (`can_thiep` / `doi_chung`), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (`ok` / `loi`), phien_ban_bang_gia, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (`giu` / `sua` / `bo`), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | ly_do (`het_3_lan_chay` / `ngoai_pham_vi` / `ngoai_du_lieu_12_thang`), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi tiền hoàn vào sổ |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, ly_do, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, trên mẫu ngẫu nhiên |
| `bank_transfer_failed` | Cổng ngân hàng | error_code (`invalid_account_number` / `input_validation_failed` / …), so_tien, trace_id | Khi ngân hàng từ chối lệnh chuyển tiền hoàn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính** (đóng trong 24 giờ, không mở lại trong 7 ngày): `ticket_closed` (lấy `closed_at − created_at` ≤ 24 giờ) và `ticket_reopened` (không có trong 7 ngày sau `closed_at`), chia số `refund_request_created`.
- **Dùng · bỏ qua gợi ý:** `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số `staff_review_decision`.
- **An toàn · lỗi lọt đến khách:** `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- **Dùng · tự đề xuất:** `refund_request_created` (lọc `arm = can_thiep`) và `agent_suggestion_shown`, nối với nhau qua `trace_id`.
- **An toàn · tự đề xuất:** `audit_sample_checked`. Ghi trùng tiền thì đối chiếu thêm `idempotency_key` trong `refund_ledger_write`.
- **Chi phí (dùng cho A và luật dừng chi phí):** `agent_run_completed` cho token và tool; `staff_review_decision.phut_xem_lai` và `staff_rework_completed.phut_lam_lai` thay cho hai cột `_simulated` sau tuần đầu pilot.
- Cả năm chỉ số đều tính được từ danh sách event, nên đều đo được.

**Đối chiếu với lỗi C và cửa sổ theo dõi D (chốt CP5):**

- **Lỗi C nào chỉ số nào bắt được.** Chỉ số an toàn "mở lại trong 7 ngày" (`ticket_reopened`) bắt được các ca khách nhận ra lỗi: ca 2 (hoàn thiếu, khách mở lại) và ca 18 (`ly_do = khieu_nai_thieu_tien`). Nó **không** bắt được lỗi Ngầm (ca 5, 17: không ai mở lại) và hoàn trùng (ca 20, khách không phàn nàn). Vì vậy cần thêm chỉ số an toàn tự đề xuất từ `audit_sample_checked` và đối soát `refund_ledger_write`. Bốn dòng còn lại trong `bang_loi.md` đều dùng event có trong bảng trên: ca 1 dùng `bank_transfer_failed`, ca 19 dùng `handoff_to_staff`, ca 17 dùng `audit_sample_checked` và `agent_run_completed.phien_ban_bang_gia`, ca 20 dùng `refund_ledger_write`.
- **Cửa sổ theo dõi.** Chỉ số chính và chỉ số an toàn cần 7 ngày sau `ticket_closed` mới chốt được một ca. Mỗi bậc rollout (10% → 25% → 50%) kéo dài một tuần, nên số đo cuối mỗi bậc chỉ gồm các ca đóng từ đủ 7 ngày trở lên. Luật dừng an toàn trong `pilot_plan.yaml` (vượt 6% trong 3 ngày kiểm tra liên tiếp) chỉ tính trên các ca đã đủ thời gian theo dõi. Mức hiện tại là 3,97% trong phạm vi pilot; riêng `hang_nang` là 8,23%, nên báo cáo tách riêng theo loại.
- **Thay số simulated.** Phút xem lại và phút làm lại trong A và B là số simulated. Từ tuần 1 của pilot, các số này được thay bằng `staff_review_decision.phut_xem_lai` và `staff_rework_completed.phut_lam_lai` đo thật.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
