# Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)

a, b, c = list(map(float, input("Nhap 3 canh cua 1 tam giac: ").split()))
if a + b > c and a + c > b and b + c > a:
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        if a == b or a == c or b == c:
            print("Tam giac vuong can")
        else:
            print("La tam giac vuong")
    elif a == b == c:
        print("La tam giac deu")
    else:
        print("La tam giac thuong")
else:
    print("Khong phai ba canh cua mot tam giac")
