print("Welcome to Ceaser Cypher!")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_number, encode_or_decode):
    output_text = ""

    # If decoding, reverse the shift once here, not in every loop iteration
    if encode_or_decode == "decode":
        shift_number *= -1

    for i in original_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift_number) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += i  # Handle non-alphabet characters
    print(f"Your message is: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Enter the shift number: \n"))

    caesar(original_text=text, shift_number=shift, encode_or_decode=direction)

    opt = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if opt == 'no':
        should_continue = False
        print("Goodbye!")
