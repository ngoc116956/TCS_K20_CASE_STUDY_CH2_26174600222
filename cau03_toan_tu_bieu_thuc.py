# cho truoc cac bien ban dau
tong_phut = 135
cong_suat_w = 250

# 9 dung // va % de tinh so gio tron ven va so phut con lai
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print("So gio tron ven:", so_gio)
print("So phut con lai:", so_phut_du)

# 10 tao bien su_dung_lau nhan TRUE khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Su dung lau (>60 phut):", su_dung_lau, "->", type(su_dung_lau))

#11 tao bien du_lieu_hop_le nhan TRUE khi cong_suat_w > 0 va tong phut>0
du_lieu_hop_le = (cong_suat_w > 0)
print("Du lieu hop le:", du_lieu_hop_le, "->", type(du_lieu_hop_le))
print("-" * 30)
# 12 du doan roi kiem tra 2 bieu thuc toan hoc
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 +20) * 3
print("Ket qua bieu thuc 1 (100 + 20 * 3) =", bieu_thuc_1)
print("Ket qua bieu thuc 2 ((100 + 20) * 3) =", bieu_thuc_2)
# giai thich du doan yeu cau 12 
# bieu thuc 1 nhan chia  truoc cong tru sau
# bieu thuc 2 trong ngoac truoc ngoai ngoac sau