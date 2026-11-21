"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def _kiem_tra_tham_so_a1(p, k):
    """Kiểm tra xác suất p trong (0, 1] và số lần chạy tối đa k >= 1 (nếu có)."""
    if not (0 < p <= 1):
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is not None and k < 1:
        raise ValueError('k phải >= 1')


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    _kiem_tra_tham_so_a1(p, k)
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    _kiem_tra_tham_so_a1(p, k)
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - chay_lai: chi phí token + tool của các lần chạy lại (attempt > 1).
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut × hệ số. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token_sum = float(tien_token.sum())
    tool_sum = float(tien_tool.sum())
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token_sum + tool_sum + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('nan')
    hoa_don_moi_yc = (token_sum + tool_sum) / len(reqs) if len(reqs) > 0 else float('nan')

    return {
        'token': token_sum,
        'tool': tool_sum,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
        'hoa_don_moi_yc': hoa_don_moi_yc,
    }


def bao_cao_gioi_han_chay_lai(runs, reqs):
    """B3: so sánh chi phí trợ lý và chi phí cả hệ thống theo giới hạn chạy."""
    print('\nB3 · Giới hạn chạy lại (simulated)')
    print('Giới hạn | Tổng trợ lý | Không thành công | Cả hệ thống | Đ/việc thành công')
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        chi_phi_he_thong = ket_qua['tong'] + BASELINE * khong_thanh_cong
        print(f"{gioi_han} | {ket_qua['tong']:,.0f} | {khong_thanh_cong:,} | "
              f"{chi_phi_he_thong:,.0f} | {ket_qua['cps']:,.0f}")


def bao_cao_xem_lai_toan_bo(runs, reqs):
    """B4: thay chi phí nhân công bằng kịch bản xem lại mọi gợi ý trong phạm vi pilot."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua = mo_hinh(runs, pham_vi)
    co_goi_y = runs['request_id'].isin(pham_vi['request_id']) & runs['status'].eq('ok')
    so_ca_xem_lai = runs.loc[co_goi_y, 'request_id'].nunique()
    so_ca_lam_lai = pham_vi['ket_qua'].eq('lam_lai').sum()
    phut_lam_lai_trung_binh = round(
        reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean(), 1
    )
    tien_token_tool = ket_qua['token'] + ket_qua['tool']
    tien_xem_lai = so_ca_xem_lai * 5 * LUONG_PHUT

    print('\nB4 · Xem lại 100% gợi ý trong phạm vi pilot (simulated)')
    print(f"{len(pham_vi)} yêu cầu | {so_ca_xem_lai} ca xem lại | "
          f"{so_ca_lam_lai} ca làm lại | {ket_qua['thanh_cong']} việc thành công")
    print(f'Token + tool: {tien_token_tool:,.0f} đ | Xem lại: {tien_xem_lai:,.0f} đ')
    for phut_lam_lai in (9, phut_lam_lai_trung_binh):
        tien_lam_lai = so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        tong_chi_phi = tien_token_tool + tien_xem_lai + tien_lam_lai
        cps = tong_chi_phi / ket_qua['thanh_cong']
        ngan_sach_xem_lai = BASELINE * ket_qua['thanh_cong'] - tien_token_tool - tien_lam_lai
        phut_hoa_von = ngan_sach_xem_lai / (so_ca_xem_lai * LUONG_PHUT)
        print(f'{phut_lam_lai:g} phút làm lại/ca | Tổng {tong_chi_phi:,.0f} đ | '
              f'{cps:,.0f} đ/việc thành công ({cps / BASELINE:.2f}×) | '
              f'Hòa vốn ở {phut_hoa_von:.2f} phút xem lại/ca')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(f"A1 (k=2, inf, cps_k3): "
          f"{so_lan_chay_ky_vong(0.8, 2):.2f} · "
          f"{so_lan_chay_ky_vong(0.8):.2f} · "
          f"{he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}")
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        fmt = ',.1f' if ten == 'hoa_don_moi_yc' else ',.0f'
        print(f'{ten:15s} {gia_tri:>14{fmt}}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · B1–B2: đổi từng yếu tố và một cặp yếu tố, ghi vào bảng độ nhạy.
    bao_cao_gioi_han_chay_lai(runs, reqs)
    bao_cao_xem_lai_toan_bo(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
