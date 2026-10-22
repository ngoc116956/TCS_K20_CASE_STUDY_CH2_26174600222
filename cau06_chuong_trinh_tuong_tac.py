# b1 nhan du lieu nhap vao tu ban phim
ma_phien = input("Nhap ma phien: ")
may = input("Nhap ma may: ")
cong_suat = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut su dung: "))
don_gia = float(input("Nhap don gia/kwh: "))
# b2 tinh toan dien nang va chi phi
dien_nang_kwh = cong_suat * so_phut / 60
chi_phi = dien_nang_kwh * don_gia
# b3 in ket qua ra man hinh theo dung dinh dang mau
print(f"Ma phien: {ma_phien}")
print(f"May: {may}")
print(f"Dien nang: {dien_nang_kwh}")
print(f"Chi phi: {chi_phi}")
# chuyen doi cong suat va don ve so nguyen khi in dong cuoi de khop mau
cs_in = int(cong_suat) if cong_suat.is_integer() else cong_suat
dg_in = int(don_gia) if don_gia.is_integer() else don_gia
print(f"Ma thu voi: {ma_phien}, {may}, {cs_in}, {so_phut}, {dg_in}.")