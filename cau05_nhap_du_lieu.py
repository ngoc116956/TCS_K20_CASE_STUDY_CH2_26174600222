# 17 nhap thong tin cau hinh tu ban phim
print("--- NHAP THONG TIN CAU HINH THIET BI ---")
# dung inout() de nhan du lieu tu nguoi dung nhap vao
ma_thiet_bi = input("Nhap ma thiet bi: ")
cong_suat_str = input("Nhap con suat (W): ")
thoi_gian_str = input("Nhap thoi gian hoat dong (phut): ")
# 18 thuc hien ep kieu du lieu tu chuoi ( str) sang so thuc/so nguyen
# cong suat co the la so thap phan ne ep kieu float
cong_suat_thuc = float(cong_suat_str)
# thoi gain thg tinh bang phut nguyen nen ep kieu int
thoi_gian_nguyen = int(thoi_gian_str)
print("--- KET QUA SAU KHI EP KIEU ---")
#19 IN GIA TRI VA KIEM TRA KIEU DU LIEU SAU KHI CHUYEN DOI
print("Ma thiet bi:", ma_thiet_bi, "->", type(ma_thiet_bi))
print("Cong suat thuc (W):", cong_suat_thuc, "->", type(cong_suat_thuc))
print("Thoi gian nguyen (phut):", thoi_gian_nguyen, "->", type(thoi_gian_nguyen))
