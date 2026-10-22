#---- doan ma da sua loi----
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int( input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut /60/ 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kwh")
# comment mo ta loi da phat hien
#1 dong3 sai dau dong ngoac nhon '}' sua thanh ngoac don ')'
#2 dong5 bi loi typererror khi tinh toan sua bang cach them float() o dong2
#3 dong6 thua kys tu '")' o cuoi cau sua thanh xoa di
#4 dong7 thieu dau ngoac don')' them vao cuoi dong