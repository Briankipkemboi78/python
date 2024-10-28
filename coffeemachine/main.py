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


# Check the report
def check_resources():
    formated_resources = "\n".join([
        f"water: {resources['water']}ml",
        f"milk: {resources['milk']}ml",
        f"coffee: {resources['coffee']}gm"
    ])
    money = 0

    return f"{formated_resources} \nmoney: ${money}"


def drink_menu(drink_name):
    if drink_name in MENU:
        ingredients = MENU[drink_name]['ingredients']
        cost = MENU[drink_name]['cost']

        formatted_ingredients = "\n".join([
            f"water: {ingredients['water']}ml",
            f"milk: {ingredients['milk']}ml",
            f"coffee: {ingredients['coffee']}gm"
        ])

        return f"{formatted_ingredients} \ncost: ${cost}"


check_report = input("Would you want to check the report: Type 'Report' \n").lower()

if check_report == "report":
    print(check_resources())

user_choice = input("What would you like? ('espresso', 'latte', 'cappuccino') \n")

if user_choice in MENU:
    print(drink_menu(user_choice))
    print("Please insert the coins!")
    quarter = input("How many quarters")
