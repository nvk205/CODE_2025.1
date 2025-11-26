# Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
a, b = list(map(int, input("Nhap so nguyen duong a, b: ").split()))
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i, end=" ")
