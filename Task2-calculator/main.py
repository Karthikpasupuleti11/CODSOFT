def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is one of the four options
    if choice in ['1', '2', '3', '4']:
        try:
            # Input two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} = {result}")

    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()