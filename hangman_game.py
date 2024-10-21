import random

word_list = ["baboon", "mouse", "church"]

chosen_word = random.choice(word_list)

print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Guess the word: {placeholder}")

user_guess = input("Please guess a letter \n").lower()

display = ""

for letter in chosen_word:
    if letter == user_guess:
        display += letter
    else:
        display += "_"
print(display)