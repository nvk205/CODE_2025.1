# Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
a = int(input("Nhap so nguyen duong a: "))
if a > 0:
    if a % 2 == 0:
        print("La so chan")
    else:
        print("La so le")
else:
    print("Khong phai so nguyen duong")
