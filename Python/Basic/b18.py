# Giải và biện luận phương trình ax + b = 0
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0 and b == 0:
    print("Phuong trinh vo so nghiem")
elif a == 0 and b != 0:
    print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh co nghiem x = ", -b / a)
