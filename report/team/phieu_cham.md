# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

## Phiếu duyệt chéo tại lớp

- Nhóm chấm: ABCD
- Nhóm được chấm: LangChai
- Điểm C6 / C7 / C8 và tổng: —
- Quyết định và lý do: —
- Câu hỏi và câu trả lời: —

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** cho pilot `noi_dia` (2.695,64 đ/việc; 0,225×) và `hang_nang` (8.220,73 đ/việc; 0,685×, `simulated`) khớp bằng chứng của nhóm: CPS gồm cố định đạt 4.599,09 đ (45.000 yc/tháng, 0,383×) và 5.784,27 đ (22.500 yc/tháng, 0,482×, `simulated`), cả hệ thống B3 giới hạn 2 lượt còn 5.751,02 đ/yc (`simulated`) < 12.000 đ, chỉ số chạy thử (82,83% đóng 24h không mở lại; 4,25% mở lại 7 ngày) chỉ ghi ở mức quan sát. Nhóm nêu đủ các con số bất lợi và cách xử lý theo vai trò, ngưỡng, ngày kiểm tra: (1) loại `quoc_te` (22.515,17 đ; 1,876×) và `doi_tac` (10.214,87 đ; 0,851×, điều khoản riêng, `simulated`); (2) làm lại gấp đôi +51,77%, xem lại gấp đôi +40,70%, lương +25% tăng 23,12% và xem lại 100% lên **12.414,50 đ/việc** (vượt 12.000 đ ở 15,30 phút làm lại/ca, `simulated`) → 30/11/2026 Trưởng nhóm CSKH bật đo phút thực tế, đối chiếu mốc hòa vốn **4,80 phút** xem lại (`simulated`) và chỉ giảm xem lại theo bậc khi đạt ngưỡng an toàn; (3) MDE 6 điểm khiến power giảm còn ~64% nếu tác động thật 5 điểm → 27/11/2026 Giám đốc vận hành kiểm lưu lượng 5.980 yc thô/nhóm trong 14 ngày (~427 yc/ngày/nhóm) và duyệt 20/20 cùng MDE 6 điểm; (4) 27/11/2026 PM trợ lý hoàn phí & Kỹ sư trưởng agent kiểm đủ 20 ca nhãn, 5 cách khắc phục và test gửi lại với ngưỡng 0 hoàn trùng, 0 thông báo thiếu sổ cái. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | ... | ... |
| C8 · Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | Có đối chứng đồng thời, chia ngẫu nhiên 20 nhân viên mỗi nhóm theo tầng depot và 4 luật dừng cụ thể. Thiết kế cần 859 yêu cầu hiệu dụng mỗi nhóm để phát hiện chênh lệch 6 điểm. Mức 5.980 yêu cầu thô mỗi nhóm trong 14 ngày dựa trên khoảng 299 yêu cầu mỗi nhân viên. Hồ sơ chưa có lưu lượng đủ điều kiện theo nhân viên để xác nhận kỳ đo đạt cỡ mẫu hiệu dụng, nên chưa đủ bằng chứng cho mức 10. [Kế hoạch pilot](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/blob/7e9731734fa3caa13868b85764eed071debbee62/report/team/pilot_plan.yaml#L26-L75) |
| **Tổng** | | | | **... / 30** | |

[Hồ sơ launch LangChai](ho_so_launch_v0.md)

| Tiêu chí                      | 0 điểm                            | 5 điểm                               | 10 điểm                                                                        |         Điểm | Lý do (có số)                                                                                                                                                                                                                                   |
| ----------------------------- | --------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------ | -----------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C6 · Đề xuất khớp bằng chứng  | Mâu thuẫn với số của chính nhóm   | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý                                      |           10 | Go có điều kiện phù hợp với chi phí biến đổi thấp ở phạm vi chọn và rủi ro xem lại 100% có thể lên 12.414,50 đ/việc (simulated). Điều kiện mở pilot yêu cầu đo phút thực tế và xét ngưỡng an toàn trước khi giảm xem lại. [B4](bang_chi_phi.md) |
| C7 · Số giả lập và phạm vi    | Thiếu nhãn và mở cho mọi yêu cầu  | Có nhãn hoặc có thu hẹp phạm vi      | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số                        |              |                                                                                                                                                                                                                                                 |
| C8 · Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung     | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng |              |                                                                                                                                                                                                                                                 |
| **Tổng chấm thử**             |                                   |                                      |                                                                                | **... / 30** |                                                                                                                                                                                                                                                 |

**Đề xuất chấm thử:**

**Lý do:**

**Câu hỏi luyện bảo vệ:** Nếu tới ngày chốt kỳ đo mà một nhóm chưa đạt 859 yêu cầu hiệu dụng, đội sẽ xử lý thế nào?

**Trả lời dự kiến:** Kiểm lại cỡ mẫu hiệu dụng dựa trên phân bố yêu cầu theo nhân viên. Nếu còn thiếu, Giám đốc vận hành duyệt kéo dài kỳ đo, giữ phân nhóm và theo dõi đủ 7 ngày sau khi đóng yêu cầu trước khi kết luận.
