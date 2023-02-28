from add import add
from sub import subtract
from multiply import multiply
from divide import divide
from power import power
from rem import remainder

def solve(operation, a, b):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    elif operation == "^":
        return power(a, b)
    elif operation == "%":
        return remainder(a, b)
    else:
        raise ValueError("Invalid operation!")

operation = input("Enter operation (+, -, *, /, ^, %): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = solve(operation, a, b)
print(f"{a} {operation} {b} = {result}")