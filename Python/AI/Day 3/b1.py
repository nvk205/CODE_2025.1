# Kiem tra so nguyen to
import math

n = int(input("Nhap so n: "))
m = round(math.sqrt(n))  # lam tron so
count = 0
for i in range(1, m):
    if n % i == 0:
        count = count + 1
if n == 1:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
