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
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
