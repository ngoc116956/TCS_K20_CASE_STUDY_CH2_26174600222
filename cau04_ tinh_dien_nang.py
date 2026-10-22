# cho truoc ca thong so ban dau 
cong_suat_w = 250 
so_phut = 90
dong_gia_kwh = 3000
# 13 tinh dien nang tieu thu va chi phi dien theo cong thuc de bai
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * dong_gia_kwh
# 14 in ca gia tri va kieu du lieu cua 2 ket qua
print("Dien nang tieu thu (kwh):", dien_nang_kwh, "->", type(dien_nang_kwh))
print("Chi phi dien (VND):", chi_phi, "->", type(chi_phi))
# 15 du doan ket qua (du doan ca 2 deu se co kieu so thuc float do cos phep/)
# ket qua tinh toan bang tay
# dien_nang = 250 * 90 / 60 /1000 = 0.375 kwh
# chi_phi = 0.375 * 3000 = 1125.0 VND

# 16 THAY SO PHUT BANG 60 VA CHAY LAI DE SO SANH
print("-" * 40)
so_phut = 60  # gan lai gia tri moi
# tinh toan lai theo so moi
dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * dong_gia_kwh
# in ket qua truong hop sau
print("--- KET QUA MOI VOI SO PHUT = 60 ---")
print("Dien nang tieu thu moi (kwh):", dien_nang_kwh_moi, "->", type(dien_nang_kwh_moi))
print("Chi phi dien moi (VND):", chi_phi_moi, "->", type(chi_phi_moi))