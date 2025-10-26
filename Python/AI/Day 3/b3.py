# Tinh luy thua theo 2 cach

n = int(input("Nhap n: "))
result1 = 1
i = 1

while i <= n:
    result1 = result1 * i
    i += 1
print(result1)

result2 = 1
for i in range(1, n + 1):
    result2 = result2 * i
print(result2)
