# nhap mot chuoi gom 3 so nguyen cach nhau boi dau phay va tinh tong 3 so
chuoi = input("Nhap 3 so nguyen: ")
a = chuoi.find(",")
b = chuoi.rfind(",")
s1 = int(chuoi[:a])
s2 = int(chuoi[a + 1 : b])
s3 = int(chuoi[b + 1 :])
sum = s1 + s2 + s3
print(sum)
