# Nhập vào số nguyên dương a, in ra bảng cửu chương của a
a = int(input("Nhap so nguyen duong a: "))
while a <= 0:
    a = int(input("Nhap lai so nguyen duong a: "))
for i in range (1, 11):
    print(a, "*", i, "=", a*i)