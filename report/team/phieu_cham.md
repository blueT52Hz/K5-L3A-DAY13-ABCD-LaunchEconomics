# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ABCD
- Nhóm được chấm: LangChai

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** cho `noi_dia` (2.695,64 đ; 0,225×) và `hang_nang` (8.220,73 đ; 0,685×, `simulated`) khớp bằng chứng: CPS gồm cố định 4.599,09–5.784,27 đ, B3 giới hạn 2 lượt còn 5.751,02 đ/yc (`simulated`). Nhóm nêu đủ số bất lợi: loại `quoc_te` (22.515,17 đ; 1,876×) và `doi_tac` (10.214,87 đ), xem lại 100% lên **12.414,50 đ/việc** (hòa vốn **4,80 phút** xem lại, `simulated`) và MDE 6 điểm làm power còn ~64% nếu tác động 5 điểm. Các điều kiện xử lý đều có vai trò và hạn kiểm tra (27–30/11/2026): Trưởng nhóm CSKH đo phút thật, Giám đốc vận hành kiểm 5.980 yc/nhóm, PM & Kỹ sư trưởng kiểm 20 ca nhãn, 5 khắc phục và ngưỡng 0 hoàn trùng. |
| C7 · Số giả lập và phạm vi | Thiếu nhãn và mở cho mọi yêu cầu | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Chi phí có phút giả lập được đánh dấu. Chọn nội địa (0,225×) và hàng nặng (0,685×); quốc tế ở 1,876× và đối tác ở 0,851×, có điều khoản riêng (simulated). [A3 của LangChai](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/blob/7e9731734fa3caa13868b85764eed071debbee62/report/team/bang_chi_phi.md#L28-L37) |
| C8 · Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có đối chứng đồng thời và phân ngẫu nhiên theo depot với 20 nhân viên mỗi nhóm. Thiết kế cho chênh lệch 6 điểm, cần 859 yêu cầu hiệu dụng mỗi nhóm và đặt mục tiêu 299 yêu cầu mỗi nhân viên. Bốn luật dừng nêu ngưỡng, thời hạn và vai trò có quyền xử lý. Giám đốc vận hành kiểm tra lưu lượng theo nhân viên trước khi mở pilot và chỉ chốt kết quả khi đủ mẫu, đủ thời gian theo dõi. [Kế hoạch pilot](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/blob/7e9731734fa3caa13868b85764eed071debbee62/report/team/pilot_plan.yaml#L26-L75) |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện cho pilot nội địa và hàng nặng.

**Lý do:** Chi phí biến đổi mỗi việc thành công của nội địa và hàng nặng lần lượt bằng 0,225× và 0,685× mốc tự làm (simulated). Xem lại 100% có thể đẩy chi phí lên 12.414,50 đ/việc (simulated), vượt mốc 12.000 đ. Trước khi mở pilot, Giám đốc vận hành xác nhận lưu lượng đủ để đạt 859 yêu cầu hiệu dụng mỗi nhóm và Kỹ sư trưởng kiểm thử chống hoàn trùng, đối soát thông báo với sổ cái. Trưởng nhóm CSKH đo phút xem lại từ tuần đầu và chỉ giảm mức xem lại khi đạt ngưỡng an toàn.

**Một câu hỏi cho đội trình:** Nếu tới ngày chốt kỳ đo mà một nhóm chưa đạt 859 yêu cầu hiệu dụng, đội sẽ xử lý thế nào?

**Câu trả lời dự thảo dựa trên kế hoạch LangChai:** Đến ngày chốt, chúng tôi tính lại cỡ mẫu hiệu dụng của từng nhóm theo số yêu cầu của từng nhân viên. Nếu một nhóm chưa đạt **859 yêu cầu hiệu dụng**, Giám đốc vận hành duyệt kéo dài kỳ thu mẫu theo tốc độ của nhóm có lưu lượng thấp hơn, giữ nguyên phân nhóm và tiếp tục áp dụng các luật dừng. Các ca cuối cần đủ cửa sổ **24 giờ để đóng và 7 ngày theo dõi mở lại sau khi đóng**. Nếu vẫn thiếu mẫu hoặc chưa đủ thời gian theo dõi, chúng tôi ghi **chưa đủ bằng chứng** và hoãn kết luận về hiệu quả. [Kế hoạch pilot LangChai](https://github.com/hoangnguyenai/K5-L3A-DAY13-LangChai-LaunchEconomics/blob/079dd5f92c125d52097c2877e30433bd5a02a650/report/team/pilot_plan.yaml#L51-L67)
