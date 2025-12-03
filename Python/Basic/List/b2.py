inventory = ["Kiếm Sắt", "Áo Giáp Da", "Bình Thuốc HP", "Kiếm Sắt", "Mũ Vải"]
# Thực hiện các thao tác sau:
# Kiểm tra xem bạn có bao nhiêu "Kiếm Sắt" trong List.
# Thêm "Khiên Gỗ" vào cuối List.
# Xóa mục "Mũ Vải" khỏi List.
# Sử dụng vòng lặp for để in ra từng vật phẩm trong inventory.
print("Số lượng kiếm sắt: ", inventory.count("Kiếm Sắt"))
inventory.append("Khiên Gỗ")
inventory.remove("Mũ Vải")
print("Inventory List: ")
for dame in inventory:
    print(dame)
