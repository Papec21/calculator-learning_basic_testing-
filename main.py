def check_if_numbers(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            raise TypeError("Both inputs must be numbers")
    return num1, num2


def addition(num1, num2):
    num1, num2 = check_if_numbers(num1, num2)
    return num1 + num2


def subtraction(num1, num2):
    num1, num2 = check_if_numbers(num1, num2)
    return num1 - num2


def multiplication(num1, num2):
    num1, num2 = check_if_numbers(num1, num2)
    return num1 * num2


def division(num1, num2):
    num1, num2 = check_if_numbers(num1, num2)
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def calculator():
    print("Welcome to the calculator\n" "Choose an operation:\n" "1. Addition\n" "2. Subtraction\n" "3. Multiplication\n" "4. Division")

    operation = input("Enter the operation number: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    match operation:
        case '1':
            print(f"Result: {addition(num1, num2)}")
        case '2':
            print(f"Result: {subtraction(num1, num2)}")
        case '3':
            print(f"Result: {multiplication(num1, num2)}")
        case '4':
            try:
                print(f"Result: {division(num1, num2)}")
            except ValueError as e:
                print(f"Error: {e}")
        case _:
            print("Invalid operation choice.")

# calculator()
