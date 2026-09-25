def add(x, y):
    """Add two numbers and return the result."""
    return x + y


def subtract(x, y):
    """Subtract y from x and return the result."""
    return x - y


def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y


def divide(x, y):
    """Divide x by y and return the result."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    """Main calculator interface."""
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit\n")

    while True:
        operation = input("Enter operation (or 'quit'): ").lower()

        if operation == 'quit':
            print("Goodbye!")
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.\n")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if operation == 'add':
                result = add(x, y)
            elif operation == 'subtract':
                result = subtract(x, y)
            elif operation == 'multiply':
                result = multiply(x, y)
            elif operation == 'divide':
                result = divide(x, y)

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    main()
