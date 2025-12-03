# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
n = int(input("Nhap so nguyen duong n: "))
chan = le = 0
while n / 10 != 0:
    if n % 2 == 0:
        chan = chan + 1
    else:
        le = le + 1
    n = n // 10
print(le, chan)
