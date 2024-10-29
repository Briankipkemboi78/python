from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        MenuItem[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino) \n Or Type 'report' to get the resource report: \n").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffe_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if drink and coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
