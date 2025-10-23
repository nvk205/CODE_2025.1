# Giải và biện luận phương trình ax^2 + bx + c = 0
a, b, c = list(map(float, input("Nhap a, b, c: ").split()))
delta = b * b - 4 * a * c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem kep x = ", -b / (2 * a))
else:
    print(
        "Phuong trinh co hai nghiem: ", (-b + delta) / (2 * a), (-b - delta) / (2 * a)
    )
