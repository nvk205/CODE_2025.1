# Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n
n = int(input("Nhap so n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum =", sum)
