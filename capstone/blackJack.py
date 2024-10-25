import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

randon_numbers = random.sample(numbers, 2)
computers_choice = [random.choice(numbers)]
print(f"Your cards: {randon_numbers}")
print(f"Computer's first card: {computers_choice}")

def add(n1, n2):
    result = n1 + n2
    return result


next_card = input("Type 'y' to get another card, type 'n' to pass: \n")
if next_card == 'y':
    new_card = random.choice(numbers)
    computer_new_card = random.choice(numbers)
    randon_numbers.append(new_card)
    computers_choice.append(computer_new_card)
    print(f"Your cards are: {randon_numbers}")
    print(f"Computers cards are: {computers_choice}")
else:
    computer_new_card = random.choice(numbers)
    computers_choice.append(computer_new_card)
    print("You Passed")
    print(f"Your cards are: {randon_numbers}")
    print(f"Computers cards are: {computers_choice}")

