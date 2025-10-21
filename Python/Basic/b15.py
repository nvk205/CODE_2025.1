# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
a, b, c = list(map(float, input("Nhap 3 canh cua 1 tam giac: ").split()))
if a + b > c and a + c > b and b + c > a:
    print("La ba canh cua mot tam giac")
else:
    print("Khong phai ba canh cua mot tam giac")
