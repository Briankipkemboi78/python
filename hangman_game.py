import random

word_list = ["baboon", "mouse", "church"]

lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Guess the word: {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    user_guess = input("Please guess a letter \n").lower()

    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}")

    display = ""

    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"You are wrong: You have {lives} lives remaining")
        if lives == 0:
            game_over = True
            print("You lose! Game over")

    if "_" not in display:
        game_over = True
        print("You win")
