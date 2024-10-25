def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return f"n1 must be greater than n2"


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 > n1:
        return n1 / n2
    else:
        return f"n2 must be greater than n1"


operand = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

want_to_continue = True
first_number = int(input("Enter the first digit: \n"))
for symbol in operand:
    print(symbol)

while want_to_continue:
    operation = input("Enter the operation to carry out: \n")
    second_number = int(input("Enter the second digit: \n"))

    if operation in operand:
        result = operand[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

    else:
        print("Invalid operation")

    to_continue = input("Do you want to continue, Type y for 'yes', n for 'no' \n")
    if to_continue == 'y':
        first_number = result

    else:
        print("Exiting the Calculator!")
        want_to_continue = False
