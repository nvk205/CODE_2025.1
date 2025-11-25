# Nhập vào số nguyên dương a, đếm số ước của a
a = int(input("Nhap so nguyen duong a: "))
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1
print(count)
