# in tat ca cac so nguyen to nho hon n
import math

n = int(input("Nhap so n: "))
if n < 2:
    print("Khong co so nguyen to nao!")
else:
    for i in range(2, n + 1):
        prime = True
        for j in range(2, round(math.sqrt(i) + 1)):
            if i % j == 0:
                prime = False
        if prime:
            print(i)
