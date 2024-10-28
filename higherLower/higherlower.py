import random
from game_data import data
from art import logo


# Create a function that generates a random account
def get_accounts():
    """ This function retrieves random account."""
    return random.choice(data)


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description} from {country}"


# Check the two random accounts and compare the number of followers
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    print(logo)

    score = 0
    game_should_continue = True
    account_a = get_accounts()
    account_b = get_accounts()

    while game_should_continue:
        account_a = account_b
        account_b = get_accounts()

        while account_a == account_b:
            account_b = get_accounts()

        print(f"Compare A: {format_data(account_a)}")
        print("vs")
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': \n").lower()
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']

        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry You are wrong! Final score {score}")


play_game()
