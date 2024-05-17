import numpy as np

def add(x, y):
    return np.add(x, y)

def subtract(x, y):
    return np.subtract(x, y)

def multiply(x, y):
    return np.multiply(x, y)

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    else:
        return np.divide(x, y)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
