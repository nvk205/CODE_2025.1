so_nguyen = [15, 8, 22, 10, 5, 1]
# Tìm và in ra mục ở chỉ mục (index) 2.
# Thay đổi giá trị của mục cuối cùng thành 25.
# Sử dụng phương thức sort() để sắp xếp List theo thứ tự tăng dần.
# Cắt lát List để lấy ra 3 số đầu tiên.
print(so_nguyen[2])
so_nguyen.pop()
so_nguyen.append(25)
print(so_nguyen)
so_nguyen.sort()
print(so_nguyen)
print(so_nguyen[:3])
