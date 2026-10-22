# 5 & 6 tao bien chuan quy tac snake_case va chon kieu du lieu phu hop
ma_phien = "LABO26"  # kieu str ( chuoi ky tu)
ma_may = "PC12"      # kieu str ( chuoi ky tu)
cong_suat = 250.0    # kieu float ( so thap phan)
thoi_gian = 90       # kieu int ( so nguyen)
trang_thai = True    # kieu bool (dung/sai)
ghi_chu = None       # kieu nonetype ( bieu thi chua co ghi chu)

# 7 in tung gia tri va dung type() de kiem tra du lieu
print("Ma phien:", ma_phien, "->", type(ma_phien))
print("Ma may:", ma_may, "->", type(ma_may))
print("Cong suat:", cong_suat, "->", type(cong_suat))
print("Thoi gian:", thoi_gian, "->", type( thoi_gian))
print("Trang thai hoat dong:", trang_thai, "->", type(trang_thai))
print("GHi chu:", ghi_chu, "->", type(ghi_chu))
print("-" * 30) # vach ke phan tach dong de de nhin

# 8 thay doi thoi gain tu 90 thanh 120 bang phep gan lai va in ra gai tri moi
thoi_gian = 120
print("Thoi gian sau khi gan lai:", thoi_gian, "->", type(thoi_gian))