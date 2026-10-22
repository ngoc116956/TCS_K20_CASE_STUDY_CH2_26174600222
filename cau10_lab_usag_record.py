from datetime import datetime

# Bước 1: Nhập các thông tin cơ bản từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
don_gia_kwh = float(input("Nhập đơn giá/kWh: "))

# Bước 2: Nhập dữ liệu thời gian để tính thời lượng
print("\n--- Nhập thời gian sử dụng ---")
nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))
ngay = int(input("Nhập ngày: "))

print(" Giờ bắt đầu:")
gio_bd = int(input("   Nhập giờ: "))
phut_bd = int(input("   Nhập phút: "))

print(" Giờ kết thúc:")
gio_kt = int(input("   Nhập giờ: "))
phut_kt = int(input("   Nhập phút: "))

# Tạo đối tượng datetime và tính thời lượng sử dụng
bat_dau = datetime(nam, thang, ngay, gio_bd, phut_bd)
ket_thuc = datetime(nam, thang, ngay, gio_kt, phut_kt)
thoi_luong = ket_thuc - bat_dau

# Chuyển đổi thời lượng ra tổng số phút để tính toán
so_phut = thoi_luong.total_seconds() / 60

# Bước 3: Tính toán điện năng và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Bước 4: Xuất kết quả định dạng ra màn hình
print("\n" + "="*20 + " KẾT QUẢ " + "="*20)
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Thời gian bắt đầu: {bat_dau.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Thời gian kết thúc: {ket_thuc.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Tổng thời gian sử dụng: {so_phut:.1f} phút")
print(f"Điện năng tiêu thụ: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí tiền điện: {chi_phi:.2f} VND")