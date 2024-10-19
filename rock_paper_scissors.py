import random

options = ["Rock", "Paper", "Scissors"]

choices = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0, 2)
print(f"You chose: {options[choices]}")
print(f"Computer chose: {options[computer_choice]}")

if choices >= 3:
    print("You picked and invalid number. You lose")
elif choices == computer_choice:
    print("It's a draw")
elif choices == 0 and computer_choice == 1:
    print("You Lose")
elif choices == 0 and computer_choice == 2:
    print("You Win")
elif choices == 1 and computer_choice == 0:
    print("You Win")
elif choices == 1 and computer_choice == 2:
    print("You Lose")
elif choices == 2 and computer_choice == 0:
    print("You Lose")
elif choices == 2 and computer_choice == 1:
    print("You Win")
