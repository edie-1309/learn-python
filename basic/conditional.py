# operator yang digunakan untuk melakukan suatu pengkondisian, seperti membandingkan dua nilai.

# operator perbandingan, persamaan
# print(2 == 3)

# operator perbandingan, pertidaksamaan
# print(2 != 4)

# kurang dari
# print(2 < 3)

# lebih dari
# print(4 > 2)

# kurang dari atau sama dengan, 
# print(5 <= 5)

# lebih dari atau sama dengan
# print(5 >= 6)

# conditional statement (operator percabangan), dan ini berkaitan dengan operator pengkondisian
# if, else, elif
# nilai_pertama = 3.5
# nilai_kedua = 3.2

# if nilai_pertama < nilai_kedua:
#     print("nilai pertama lebih kecil dari nilai kedua")
# elif nilai_pertama > nilai_kedua:
#     print("nilai pertama lebih besar dari nilai kedua")
# else:
#     print("nilai pertama sama dengan nilai kedua")
# contoh lain
username_system = "admin"
password_system = "admin123"

input_username = input("masukkan username: ")
input_password = input("masukkan password: ")

if input_username == username_system and input_password == password_system:
    print("kredesial sesuai, anda berhasil login")
else:
    print("kredesial tidak sesuai, silahkan coba lagi")