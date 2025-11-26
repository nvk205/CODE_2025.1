# Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
# Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
a = []

while True:
    b = int(input("Nhap phan tu trong day: "))
    if b == -1:
        break
    else:
        a.append(b)
Max = max(a)
Min = min(a)
print("Max: ", Max)
print("Min: ", Min)
