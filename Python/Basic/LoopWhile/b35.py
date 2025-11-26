# Nhập n
# Cho S(k) = 1 + 2 + 3 + … + k
# Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
n = int(input("Nhap so nguyen n: "))
k = 0
Sum = 0
while Sum < n:
    k = k + 1
    Sum = Sum + k
print(k - 1)
