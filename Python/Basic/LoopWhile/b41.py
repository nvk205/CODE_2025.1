# Nhap vao so nguyen duong N, kiem tra xem N = 2^k hay khong
import math

n = int(input("Nhap so nguyen duong N: "))
while n <= 0:
    n = int(input("Khong thoa man! Nhap lai so nguyen duong N: "))
if math.sqrt(n) == round(math.sqrt(n)):
    print(True)
else:
    print(False)
