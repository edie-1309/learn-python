import random

random_integer = random.randint(1, 10)

user_input_number = input("Masukan tebakan angka: ");

if user_input_number == random_integer:
    print("Benar!")
else:
    print("Salah!, angka yang benar adalah: ", random_integer)