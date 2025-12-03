# slicing
danh_sach_so = [1, 5, 3, 6, 0, 9]
print(danh_sach_so[2:5])
print(danh_sach_so[-2:])
print(danh_sach_so[:])

# add items
fruits = ["cam", "quyt"]
fruits.append("xoai")  # them vao cuoi
print(fruits)
fruits.insert(1, "tao")  # them vao index = 1
print(fruits)
fruits.extend(["nho", "oi"])  # them list khac vao cuoi
print(fruits)

# removing items
fruits.remove("cam")  # xoa cam
print(fruits)
fruits.pop(1)  # xoa index = 1, khong co index thi xoa cuoi
print(fruits)
fruits.clear()  # xoa tat ca lam cho list rong
print(fruits)
del fruits  # xoa het ca chuoi

# sap xep
danh_sach_so.sort()  # tang dan
print(danh_sach_so)
danh_sach_so.sort(reverse=True)  # giam dan
print(danh_sach_so)
danh_sach_so.reverse()  # dao nguoc thu tu
print(danh_sach_so)
print(danh_sach_so.count(0))  # dem so luong 0
print(danh_sach_so.index(3))  # in index 3
