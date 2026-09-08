def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def calculate(operation, a, b):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    result = operations.get(operation)(a, b)
    return result


print(calculate('add', 10, 5))
print(calculate('subtract', 10, 5))
print(calculate('multiply', 10, 5))
print(calculate('divide', 10, 5))
