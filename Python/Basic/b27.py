# Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
h = int(input("Nhap chieu cao cua tam giac: "))
print(' '*(h-1), end="")
print("*")
for i in range (1, h - 1):
    print(' '*(h-i-1), end = "")
    print("*", end ="")
    print(' '*(2*i-1), end = "")
    print("*", end = "")
    print()
print('*'*(2*h-1))