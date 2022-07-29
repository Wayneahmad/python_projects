# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:

# password = ""

# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
# # print(password)
# for char in range(1, nr_symbols + 1):
#     random_symbols = random.choice(symbols)
#     password += random_symbols

# for char in range(1, nr_numbers + 1):
#     random_numbers = random.choice(numbers)
#     password += random_numbers
# print(password)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char
# print(password)
for char in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password_list += random_symbols

for char in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password_list += random_numbers

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
length = len(password)
print(f"Your password is {password}")


def my_function():

    print(f"\nYour password is {length} characters long")


my_function()
