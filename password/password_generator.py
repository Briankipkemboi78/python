import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Generate your password!")
letters_nr = int(input("How many letter would you like in your password: \n"))
symbols_nr = int(input("How many symbols would your like?\n"))
numbers_nr = int(input("How many numbers would you like: \n"))


password_list = []
for char in range(0, letters_nr):
    random_char = random.choice(letters)
    password_list.append(random_char)
for sym in range(0, symbols_nr):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
for num in range(0, numbers_nr):
    random_number = random.choice(numbers)
    password_list.append(random_number)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
