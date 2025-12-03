# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
n = int(input("Nhap so nguyen duong N: "))
while n <= 0:
    n = int(input("Khong thoa man! Nhap lai so nguyen duong N: "))
le = chan = 0
while n / 10 != 0:
    if n % 2 == 0:
        chan = chan + 1
        n = n // 10
    else:
        le = le + 1
        n = n // 10
print(le, chan)
