
# Exercise 1: Basic Math Operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else 'Cannot divide by 0'

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b

if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))
    print("Multiplication:", multiply(6, 7))
    print("Division:", divide(8, 2))
    print("Remainder:", remainder(10, 3))
    print("Power:", power(2, 5))