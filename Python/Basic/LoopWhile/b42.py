# Nhap vao so N va tim so lon nhat trong day fibonaci be hon N
n = int(input("Nhap so tu nhien N: "))
while n <= 0:
    n = int(input("Khong thoa man! Nhap lai so nguyen duong N: "))
a = 1
b = 1
fi = a + b
while fi < n:
    a = b
    b = fi
    fi = a + b
print(b)
