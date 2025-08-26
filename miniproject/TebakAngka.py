import random

random_integer = random.randint(1, 10)

user_input_number = input("Masukan tebakan angka: ");

if user_input_number == random_integer:
    print("Benar!")
elif not isinstance(user_input_number, int):
    print("Input harus angka!")
else:
    print("Salah!, angka yang benar adalah: ", random_integer)