# Nhap vao so nguyen N, tinh tong cac chu so cua N
n = int(input("Nhap so nguyen duong N: "))
while n <= 0:
    n = int(input("Khong thoa man! Nhap lai so nguyen duong N: "))
Sum = 0
while n / 10 != 0:
    Sum = Sum + n % 10
    n = n // 10
print(Sum)
