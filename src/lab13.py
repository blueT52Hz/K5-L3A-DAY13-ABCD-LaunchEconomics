"""Tính các bảng kiểm tra Lab 13 từ hai CSV giả lập. Chạy: python lab13.py."""

import math
import sys
from pathlib import Path
from statistics import NormalDist

import pandas as pd

BASELINE = 12_000
CO_DINH = 40_000_000
PHAM_VI = ("noi_dia", "hang_nang")


def ti_le_thanh_cong(p, k=None):
    return 1.0 if k is None else 1 - (1 - p) ** k


def so_lan_chay_ky_vong(p, k=None):
    return ti_le_thanh_cong(p, k) / p


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    ket_qua = (
        so_lan_chay_ky_vong(0.8, 2),
        so_lan_chay_ky_vong(0.8),
        he_so_chi_phi_moi_viec_thanh_cong(0.8, 3),
    )
    for tinh_duoc, dap_an in zip(ket_qua, (1.20, 1.25, 1.25)):
        assert math.isclose(tinh_duoc, dap_an, abs_tol=1e-9)
    return ket_qua


def doc_du_lieu():
    thu_muc = Path(__file__).resolve().parent
    return (
        pd.read_csv(thu_muc / "logix_runs.csv"),
        pd.read_csv(thu_muc / "logix_requests.csv", keep_default_na=False),
    )


def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính máy trên mọi lượt và nhân công theo yêu cầu còn trong giới hạn."""
    luot = runs[runs.request_id.isin(reqs.request_id)]
    yeu_cau = reqs
    if max_lan_chay is not None:
        luot = luot[luot.attempt.le(max_lan_chay)]
        yeu_cau = reqs[reqs.so_lan_chay.le(max_lan_chay)]
    token = (luot.tokens_in * gia_vao + luot.tokens_out * gia_ra) / 1000
    tool = luot.tool_calls * gia_tool
    xem_lai = yeu_cau.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam_lai = yeu_cau.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = int(yeu_cau.ket_qua.eq("thanh_cong").sum())
    return {
        "token": token.sum(), "tool": tool.sum(),
        "chay_lai": (token + tool)[luot.attempt.gt(1)].sum(),
        "xem_lai": xem_lai, "lam_lai": lam_lai, "tong": tong,
        "thanh_cong": thanh_cong, "so_luot": len(luot),
        "cps": tong / thanh_cong if thanh_cong else math.inf,
        "hoa_don": (token.sum() + tool.sum()) / len(reqs) if len(reqs) else math.nan,
    }


def chi_phi_co_dinh(ket_qua_pham_vi, tong_yeu_cau_mau, khoi_luong_thang):
    """Khối lượng đầu vào là toàn công ty. Phạm vi đã phản ánh trong tử số."""
    thanh_cong_thang = khoi_luong_thang * ket_qua_pham_vi["thanh_cong"] / tong_yeu_cau_mau
    co_dinh_moi_viec = CO_DINH / thanh_cong_thang
    return thanh_cong_thang, co_dinh_moi_viec, ket_qua_pham_vi["cps"] + co_dinh_moi_viec


def co_mau(p1, p2, alpha=0.05, power=0.80):
    z = NormalDist()
    p_tb = (p1 + p2) / 2
    goc = z.inv_cdf(1 - alpha / 2) * math.sqrt(2 * p_tb * (1 - p_tb))
    thay_the = z.inv_cdf(power) * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((goc + thay_the) / (p2 - p1)) ** 2)


def dinh_dang(n, le=0):
    return f"{n:,.{le}f}".translate(str.maketrans(".,", ",."))


def bang(cot, dong):
    kha_dung = [cot, ["---"] * len(cot), *dong]
    return "\n".join("| " + " | ".join(map(str, o)) + " |" for o in kha_dung)


def bao_cao_chi_phi(runs, reqs):
    so = dinh_dang
    thu = kiem_tra_dap_an_biet_truoc()
    goc = mo_hinh(runs, reqs)
    pilot = reqs[reqs.loai.isin(PHAM_VI)]
    trong_pham_vi = mo_hinh(runs, pilot)
    a2 = [
        ("Token", so(goc["token"]), "logix_runs.csv"),
        ("Tool", so(goc["tool"]), "logix_runs.csv"),
        ("Trong đó, lượt 2 và 3", so(goc["chay_lai"]), "Đã gồm trong token và tool"),
        ("Xem lại", so(goc["xem_lai"]), "simulated"),
        ("Làm lại", so(goc["lam_lai"]), "simulated"),
        ("Tổng chi phí", so(goc["tong"]), "simulated"),
        ("Số việc thành công", so(goc["thanh_cong"]), "ket_qua"),
        ("Chi phí mỗi việc thành công", so(goc["cps"]), "simulated"),
        ("Hóa đơn máy mỗi yêu cầu", so(goc["hoa_don"], 1), "Token và tool / số yêu cầu"),
    ]
    a3 = []
    for loai, yeu_cau in reqs.groupby("loai", sort=False):
        kq = mo_hinh(runs, yeu_cau)
        a3.append((loai, len(yeu_cau), so(100 * kq["thanh_cong"] / len(yeu_cau), 1) + "%",
                   so(kq["so_luot"] / len(yeu_cau), 2), so(kq["cps"]), so(kq["cps"] / BASELINE, 2) + "×"))
    quoc_te = reqs.loc[reqs.loai.eq("quoc_te"), "request_id"]
    quoc_te_runs = runs[runs.request_id.isin(quoc_te)]
    ok_tung_luot = quoc_te_runs.assign(ok=quoc_te_runs.status.eq("ok")).groupby("attempt").ok.mean()
    ok_quoc_te = " · ".join(so(ti_le * 100, 1) + "%" for ti_le in ok_tung_luot)

    a4 = []
    for khoi_luong in (45_000, 22_500):
        thanh_cong, co_dinh, tong = chi_phi_co_dinh(trong_pham_vi, len(reqs), khoi_luong)
        a4.append((so(khoi_luong), so(thanh_cong), so(co_dinh), so(tong), so(tong / BASELINE, 2) + "×"))
    thanh_cong_moi_yeu_cau = trong_pham_vi["thanh_cong"] / len(reqs)
    hoa_von = math.ceil(CO_DINH / (BASELINE - trong_pham_vi["cps"]) / thanh_cong_moi_yeu_cau)

    kich_ban = [
        ("Token ×2", {"gia_vao": 52, "gia_ra": 260}),
        ("Token ÷2", {"gia_vao": 13, "gia_ra": 65}),
        ("Xem lại ×2", {"he_so_xem_lai": 2}),
        ("Xem lại ÷2", {"he_so_xem_lai": 0.5}),
        ("Làm lại ×2", {"he_so_lam_lai": 2}),
        ("Làm lại ÷2", {"he_so_lam_lai": 0.5}),
        ("Lương +25%", {"luong_phut": 2500}),
        ("Tối đa 2 lượt", {"max_lan_chay": 2}),
        ("Tối đa 1 lượt", {"max_lan_chay": 1}),
        ("B2 · Token ×2 và xem lại ×2", {"gia_vao": 52, "gia_ra": 260, "he_so_xem_lai": 2}),
    ]
    b1 = []
    for ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        thay_doi = 100 * (cps / goc["cps"] - 1)
        dau = "+" if thay_doi > 0 else ""
        b1.append((ten, so(cps), f"{dau}{so(thay_doi, 1)}%"))
    b3 = []
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq["thanh_cong"]
        he_thong = kq["tong"] + BASELINE * khong_thanh_cong
        b3.append((k, so(kq["tong"]), khong_thanh_cong, so(he_thong), so(kq["cps"])))
    luot_pilot_ok = runs.status.eq("ok") & runs.request_id.isin(pilot.request_id)
    so_xem = runs.loc[luot_pilot_ok, "request_id"].nunique()
    so_lam_lai = int(pilot.ket_qua.eq("lam_lai").sum())
    tien_may = trong_pham_vi["token"] + trong_pham_vi["tool"]
    b4 = (tien_may + 2000 * (5 * so_xem + 9 * so_lam_lai)) / trong_pham_vi["thanh_cong"]

    return f"""# Bảng chi phí · Nhiệm vụ A và B

Số được tính bằng src/lab13.py trên dữ liệu giả lập của đề.

## A1 · Ba phép thử đáp án biết trước

Ba phép thử đáp án biết trước: ĐẠT ({' · '.join(so(x, 2) for x in thu)})

## A2 · Chi phí từ trace

{bang(("Khoản", "Giá trị (đ nếu là tiền)", "Nguồn hoặc nhãn"), a2)}

Chi phí mỗi việc thành công cao gấp {so(goc["cps"] / goc["hoa_don"], 1)} lần hóa đơn máy mỗi yêu cầu. Làm lại chiếm tỷ trọng lớn nhất, {so(100 * goc["lam_lai"] / goc["tong"], 1)}% (simulated).

## A3 · Tách theo loại

{bang(("Loại", "Yêu cầu", "Thành công", "Lượt/yêu cầu", "Đ/việc thành công (simulated)", "So với 12.000 đ (simulated)"), a3)}

Quốc tế tốn 22.515 đ/việc (simulated), đạt 27,3% việc thành công. Tỷ lệ lượt ok trong số ca đến từng lượt ({ok_quoc_te}) cho thấy lợi ích thấp ở lượt 2 và 3.

## A4 · Phân bổ 40 triệu đ chi phí cố định mỗi tháng

Hai dòng dự phóng từ 900 việc thành công nội địa và hàng nặng trên 1.200 yêu cầu toàn mẫu. Chi phí biến đổi trong phạm vi là {so(trong_pham_vi["tong"])} đ cho 900 việc thành công (simulated).

{bang(("Yêu cầu/tháng toàn công ty", "Việc thành công/tháng", "Cố định/việc (đ)", "Đ/việc gồm cố định (simulated)", "So với làm tay (simulated)"), a4)}

Cả hai mức khối lượng vẫn dưới 12.000 đ. Ngưỡng hòa vốn theo chi phí mỗi việc thành công là khoảng {so(hoa_von)} yêu cầu toàn công ty mỗi tháng, giả sử cơ cấu và hiệu suất giữ nguyên (simulated). Ngưỡng này chưa cộng phần nhân viên tiếp nhận.

## B1 và B2 · Độ nhạy

{bang(("Kịch bản", "Đ/việc thành công (simulated)", "So với A2 (simulated)"), b1)}

Ba yếu tố ảnh hưởng mạnh nhất trong các mức đã thử là làm lại, xem lại và lương nhân viên. Tác động của cặp bằng tổng tác động riêng khi số việc thành công giữ nguyên.

## B3 · Giới hạn chạy lại

{bang(("Giới hạn", "Trợ lý (đ, simulated)", "Không thành công", "Cả hệ thống (đ, simulated)", "Đ/việc thành công (simulated)"), b3)}

Hai lượt cho tổng chi phí hệ thống thấp nhất. Giới hạn một lượt làm giảm chi phí mỗi việc thành công nhưng có thêm {b3[0][2] - b3[1][2]} yêu cầu cần nhân viên xử lý.

## B4 · Xem lại 100% trong phạm vi

Với {so_xem} ca xem lại × 5 phút, {so_lam_lai} ca làm lại × 9 phút và {so(tien_may)} đ tiền máy, chi phí là {so(b4)} đ/việc, bằng {so(b4 / BASELINE, 2)}× làm tay, trước chi phí cố định (simulated). Pilot cần đo phút thật và kiểm tra khi nào có thể giảm duyệt an toàn.
"""


def bao_cao_co_mau():
    icc, m, c = 0.02, 75, 20
    n5, n6 = co_mau(0.70, 0.75), co_mau(0.70, 0.76)
    de = 1 + (m - 1) * icc
    n_cum = math.ceil(n5 * de)
    m6 = math.ceil(n6 * (1 - icc) / (c - n6 * icc))
    h5 = 2 * (math.asin(math.sqrt(0.75)) - math.asin(math.sqrt(0.70)))
    z = NormalDist()
    z_alpha, delta = z.inv_cdf(0.975), h5 * math.sqrt(n6 / 2)
    power5 = z.cdf(delta - z_alpha) + z.cdf(-delta - z_alpha)
    return "\n".join([
        "D1 · Cỡ mẫu",
        f"a. Chia theo yêu cầu: {n5} mỗi nhóm.",
        f"b. Chia theo nhân viên (m={m}): DE={de:.2f}, {n_cum} yêu cầu và {math.ceil(n_cum / m)} người mỗi nhóm.",
        f"c. Chia 20 nhân viên mỗi nhóm: hiệu dụng dưới {c / icc:.0f}.",
        f"d. Chia 6 depot mỗi nhóm: hiệu dụng dưới {6 / icc:.0f}.",
        f"e. Chênh 6 điểm: {n6} hiệu dụng mỗi nhóm, {m6} yêu cầu/người, DE={1 + (m6 - 1) * icc:.2f}.",
        f"Power tại chênh 5 điểm với {n6} mẫu hiệu dụng: {power5:.2f}.",
    ])


def bao_cao_chi_so(reqs):
    da_xem = reqs[reqs.duoc_xem_lai.eq(1)]
    pham_vi = reqs[reqs.loai.isin(PHAM_VI)]
    chi_so = [
        ("Đóng trong 24h và không mở lại", (reqs.dong_trong_24h.eq(1) & reqs.mo_lai_trong_7_ngay.eq(0)).sum(), len(reqs)),
        ("Sửa hoặc bỏ gợi ý", da_xem.quyet_dinh_xem_lai.isin(["sua", "bo"]).sum(), len(da_xem)),
        ("Mở lại", reqs.mo_lai_trong_7_ngay.sum(), len(reqs)),
        ("Mở lại trong phạm vi", pham_vi.mo_lai_trong_7_ngay.sum(), len(pham_vi)),
    ]
    return "E1 · Số liệu chạy thử giả lập\n" + "\n".join(
        f"{ten}: {dinh_dang(tu / mau * 100, 2)}% ({tu}/{mau})" for ten, tu, mau in chi_so
    )


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    runs, reqs = doc_du_lieu()
    print(bao_cao_chi_phi(runs, reqs))
    print(bao_cao_co_mau())
    print()
    print(bao_cao_chi_so(reqs))
