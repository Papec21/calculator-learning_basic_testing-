from calculator_database import save_equation



def check_if_numbers(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            raise TypeError("Both inputs must be numbers")
    return num1, num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def calculator():
    print("Welcome to the calculator\n" "Choose an operation:\n" "1. Addition\n" "2. Subtraction\n" "3. Multiplication\n" "4. Division")

    choosed_operation = input("Enter the operation number: ")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        num1, num2 = check_if_numbers(num1, num2)
    except TypeError as e:
        print(f"Error: {e}")
        return

    match choosed_operation:
        case '1':
            operation = 'addition'
            result = addition(num1, num2)
            print(f"Result: {result}")
        case '2':
            operation = 'subtraction'
            result = subtraction(num1, num2)
            print(f"Result: {result}")
        case '3':
            operation = 'multiplication'
            result = multiplication(num1, num2)
            print(f"Result: {result}")
        case '4':
            operation = 'division'
            try:
                result = division(num1, num2)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        case _:
            print("Invalid operation choice.")

    save_equation(result, operation, num1, num2)


# calculator()
calculator()