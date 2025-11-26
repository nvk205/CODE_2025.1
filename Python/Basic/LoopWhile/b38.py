# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
n = int(input("Nhap so duong n: "))
count = 0
while n % 10 != 0:
    count = count + 1
    n = n // 10
print(count)
