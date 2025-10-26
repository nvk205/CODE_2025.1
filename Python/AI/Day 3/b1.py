# Kiem tra so nguyen to
import math

n = int(input("Nhap so n: "))
m = round(math.sqrt(n)) + 1  # lam tron so
prime = True
for i in range(2, m):
    if n % i == 0:
        prime = False
if n < 2:
    prime = False
if prime:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
