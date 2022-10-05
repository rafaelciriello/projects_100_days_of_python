#caesar cipher
from caesar_cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
print("Welcome to the Caesar Cipher.")
def caeser(start_text, shift_amount, cypher_direction):

    end_text = ""
    if cypher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter not in alphabet:
            new_letter = letter
            end_text += new_letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"The {cypher_direction} text is {end_text}.")

end_the_cipher = False

while not end_the_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caeser(start_text=text, shift_amount=shift, cypher_direction=direction)

    new_operation = input("Wold you like to continue? 'Y' or 'N': ").lower()
    if new_operation == "n":
        end_the_cipher = True
