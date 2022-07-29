from cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', '/', '<', '>', '?', ';', '\'', '\\', ':', '"', '|', '[', ']', '{', '}', '-', '=', '_', '+', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', '/',
            '<', '>', '?', ';', '\'', '\\', ':', '"', '|', '[', ']', '{', '}', '-', '=', '_', '+', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', '/', '<', '>', '?', ';', '\'', '\\', ':', '"', '|', '[', ']', '{', '}', '-', '=', '_', '+', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', ' ', ]
print(logo)

print("\nWelcome to Wayne's Encryption\n")

should_continue = True
while should_continue == True:

    def ceasar(start_text, shift_amount, cipher_direction):
        end_text = ""
        for characters in start_text:
            # if characters in alphabet:
            position = alphabet.index(characters)
            if cipher_direction == "encode":
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                new_position = position - shift_amount
                end_text += alphabet[new_position]
            # else:
            #end_text += characters
        print(f"Here's the {cipher_direction}d result: {end_text}")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    shift = shift % 59
    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("\nDo you want to run again? Yes or No?\n")
    if result == "no":
        should_continue = False
        print("Goodbye")


lists_1 = ["1", "2"]

position = lists_1.index("3")
print(position)
