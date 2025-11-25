# Nhập vào A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
A = float(input("Nhap A: "))
Sum = 0.0
n = 0
while Sum < A:
    n = n + 1
    Sum = Sum + 1 / n
print(Sum)
print(n - 1)
