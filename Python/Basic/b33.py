# Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
import math

a = int(input("Nhap so nguyen duong a: "))
if a < 2:
    print("Khong phai so nguyen to")
else:
    for i in range(2, round(math.sqrt(a)) + 1):
        if a % i == 0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")
