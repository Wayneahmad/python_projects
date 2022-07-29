
from art import logo
import os

# add


def add(n1, n2):
    return n1 + n2

# subtract


def subtract(n1, n2):
    return n1 - n2

# multiply


def multiply(n1, n2):
    return n1 * n2

# divide


def divide(n1, n2):
    return n1 / n2


print(logo)
num1 = int(input("What's the first number?: "))
still_continue = True


while still_continue == True:
    os.system("clear")
    print(logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    for symbol in operations:
        print(symbol)
    operation_symbol = (input("Pick an operation?: "))
    num2 = int(input("What's the second number?: "))
    calculation = operations[operation_symbol]
    first_answer = calculation(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    num1 = first_answer

    result = input("do you want to make another calculation? Y or N\n").lower()

    if result == "y":
        continue
    else:
        os.system("clear")
        print("Goodbye")
        still_continue = False
