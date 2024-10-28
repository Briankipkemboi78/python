MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0  # Initialize profit variable


# Check the report
def check_resources():
    formatted_resources = "\n".join([
        f"water: {resources['water']}ml",
        f"milk: {resources['milk']}ml",
        f"coffee: {resources['coffee']}gm",
        f"profit: ${profit:.2f}"
    ])
    return formatted_resources


def drink_menu(drink_name):
    if drink_name in MENU:
        ingredients = MENU[drink_name]['ingredients']
        cost = MENU[drink_name]['cost']

        formatted_ingredients = "\n".join([
            f"water: {ingredients['water']}ml",
            f"milk: {ingredients.get('milk', 0)}ml",  # Use get to avoid KeyError
            f"coffee: {ingredients['coffee']}gm"
        ])

        return formatted_ingredients, cost


def process_coins(quarter, dimes, nickels, pennies):
    total = (
            (quarter * 0.25) +
            (dimes * 0.10) +
            (nickels * 0.05) +
            (pennies * 0.01)
    )
    return round(total, 2)  # Round to two decimal places


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True  # Return True only after all checks pass


# Check for correct Transaction
def is_transaction_correct(total_pay, drink_cost):
    if total_pay >= drink_cost:
        change = round(total_pay - drink_cost, 2)  # Calculate change
        print(f"Here is your ${change:.2f} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, you do not have enough money! The drink costs ${drink_cost:.2f}")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) \nOr type 'report' to get the resource report: \n")

    # Turn off the Coffee Machine
    if choice == "off":
        is_on = False

    # Print report
    elif choice == "report":
        print(check_resources())

    # Check if the drink is available in the menu
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            print("Please insert the coins!")
            quarter = int(input("How many quarters? \n"))
            dimes = int(input("How many dimes? \n"))
            nickels = int(input("How many nickels?\n"))
            pennies = int(input("How many pennies?\n"))

            payment = process_coins(quarter, dimes, nickels, pennies)
            if is_transaction_correct(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Sorry, that item is not available.")
