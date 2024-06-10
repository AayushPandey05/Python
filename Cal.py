import math
from queue import Queue

def add(q):
    operand1 = q.get()
    operand2 = q.get()
    result = operand1 + operand2
    q.put(result)
    print(f"Result: {result}")

def subtract(q):
    operand1 = q.get()
    operand2 = q.get()
    result = operand1 - operand2
    q.put(result)
    print(f"Result: {result}")

def multiply(q):
    operand1 = q.get()
    operand2 = q.get()
    result = operand1 * operand2
    q.put(result)
    print(f"Result: {result}")

def divide(q):
    operand1 = q.get()
    operand2 = q.get()
    if operand2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        result = operand1 / operand2
        q.put(result)
        print(f"Result: {result}")

def square(q):
    operand = q.get()
    result = operand ** 2
    q.put(result)
    print(f"Result: {result}")

def square_root(q):
    operand = q.get()
    if operand < 0:
        print("Error: Cannot calculate square root of a negative number")
    else:
        result = math.sqrt(operand)
        q.put(result)
        print(f"Result: {result}")

def sin(operand):
    result = math.sin(math.radians(operand))
    print(f"Result: {result}")

def cos(operand):
    result = math.cos(math.radians(operand))
    print(f"Result: {result}")

def tan(operand):
    result = math.tan(math.radians(operand))
    print(f"Result: {result}")

def asin(operand):
    if -1 <= operand <= 1:
        result = math.degrees(math.asin(operand))
        print(f"Result: {result}")
    else:
        print("Error: Invalid input for arcsine function")

def acos(operand):
    if -1 <= operand <= 1:
        result = math.degrees(math.acos(operand))
        print(f"Result: {result}")
    else:
        print("Error: Invalid input for arccosine function")

def atan(operand):
    result = math.degrees(math.atan(operand))
    print(f"Result: {result}")

def calculator():
    q = Queue()

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Square Root")
        print("7. Sin (in degrees)")
        print("8. Cos (in degrees)")
        print("9. Tan (in degrees)")
        print("10. Arcsin (in degrees)")
        print("11. Arccos (in degrees)")
        print("12. Arctan (in degrees)")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

        if choice in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'}:
            if choice in {'7', '8', '9', '10', '11', '12'}:
                operand = float(input("Enter operand: "))
                if choice == '7':
                    sin(operand)
                elif choice == '8':
                    cos(operand)
                elif choice == '9':
                    tan(operand)
                elif choice == '10':
                    asin(operand)
                elif choice == '11':
                    acos(operand)
                elif choice == '12':
                    atan(operand)
            else:
                operand1 = float(input("Enter operand 1: "))
                operand2 = float(input("Enter operand 2: "))
                q.put(operand1)
                q.put(operand2)
                if choice == '1':
                    add(q)
                elif choice == '2':
                    subtract(q)
                elif choice == '3':
                    multiply(q)
                elif choice == '4':
                    divide(q)
                elif choice == '5':
                    q.get()
                    square(q)
                elif choice == '6':
                    q.get()
                    square_root(q)
        elif choice == '13':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 13.")

if __name__ == "__main__":
    calculator()