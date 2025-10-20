# Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
a, b = list(map(int, input("Nhap cac so nguyen a, b: ").split()))
print(a % 2 == 0 or b % 2 == 0)
