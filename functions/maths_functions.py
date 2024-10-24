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



