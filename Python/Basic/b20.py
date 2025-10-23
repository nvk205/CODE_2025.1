# Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
month = int(input("Nhap thang: "))
match month:
    case 1:
        print("31")
    case 2:
        print("28 or 29")
    case 3:
        print("31")
    case _:
        print("hjhj")
# luoi check nam nhuan chia het 4 nhung khong chia het 100 hoac chia het cho 400
