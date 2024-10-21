print("Welcome to Ceaser Cypher!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Enter the shift number: \n"))


def encrypt(original_text, shift_number):
    encrypted_text = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += i
    print(f"Your encrypted message is: {encrypted_text}")


def decrypt(encrypted_text, shift_number):
    decrypted_text = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position - shift) % 26
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += i
    print(f"Your decrypted message is: {decrypted_text}")


if direction == "encode":
    encrypt(original_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_number=shift)
else:
    print("You have entered the wrong key!")
