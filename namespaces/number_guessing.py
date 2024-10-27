import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 an 100")

    EASY = 10
    HARD = 5

    guess_number = random.randint(1, 100)

    is_game_over = False
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = EASY if difficulty == 'easy' else HARD

    while attempts > 0 and not is_game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")

        user_guess = int(input("Make a guess: "))

        if user_guess > guess_number:
            print("Too High!")
        elif user_guess < guess_number:
            print("Too Low")
        else:
            print(f"Congrats! You guessed the number {guess_number} correctly.")
            is_game_over = True

        attempts -= 1

        if attempts == 0:
            print(f"You've run out of attempts. The number was {guess_number}. Better luck next time!")
            is_game_over = True
        else:
            print("Guess Again")


number_guessing_game()
