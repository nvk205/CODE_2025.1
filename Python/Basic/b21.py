# Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)
ngay = int(input("Nhap ngay: "))
thang = int(input("Nhap thang: "))
# dem so thang co 30 hay 31 ngay va phai tru di 2 ngay cua thang 2

if thang != 9 and thang != 11:
    t30 = (thang - 1) // 2
elif thang == 9:
    t30 = 3
else:
    t30 = 4
if thang <= 7:
    t31 = thang // 2
else:
    t31 = (thang + 1) / 2
if thang > 2:
    print("So ngay tu dau nam: ", 30 * t30 + 31 * t31 + ngay - 2)
else:
    print("So ngay tu dau nam: ", 30 * t30 + 31 * t31 + ngay)
