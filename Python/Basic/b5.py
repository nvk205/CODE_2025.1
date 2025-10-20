# Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
a = int(input("Nhap so nguyen a: "))
if 50 <= a and a <= 100 and a % 3 == 0:
    print("True")
else:
    print("False")
# or
print(50 <= a <= 100 and a % 3 == 0)  # clean
