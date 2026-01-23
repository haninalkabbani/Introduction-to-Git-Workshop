def add(x, y):
    """
    Add two numbers together.

    Args:
        x (int | float): The first number to add
        y (int | float): The second number to add

    Returns:
        int | float: The sum of x and y
    """
    return x + y


def subtract(x, y):
    """
    Subtract the second number from the first.

    Args:
        x (int | float): The number to subtract from
        y (int | float): The number to subtract

    Returns:
        int | float: The difference of x and y
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers together.

    Args:
        x (int | float): The first number to multiply
        y (int | float): The second number to multiply

    Returns:
        int | float: The product of x and y
    """
    return x * y


def divide(x, y):
    """
    Divide the first number by the second.

    Args:
        x (int | float): The dividend
        y (int | float): The divisor

    Returns:
        float: The quotient of x divided by y

    Raises:
        ZeroDivisionError: If y is zero
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def calculate_and_display(x, y):
    """
    Perform basic arithmetic operations and display results.

    Args:
        x (int | float): The first number
        y (int | float): The second number
    """
    print(f"Numbers: x = {x}, y = {y}")
    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")

    try:
        result = divide(x, y)
        print(f"Division: {x} / {y} = {result}")
    except ZeroDivisionError as e:
        print(f"Division: {e}")


def get_number_input(prompt):
    """
    Get numeric input from user with automatic int/float conversion.

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        int | float: The numeric value entered by the user

    Raises:
        ValueError: If the input cannot be converted to a number
    """
    user_input = input(prompt)
    # Try to convert to int first, then float
    try:
        return int(user_input)
    except ValueError:
        return float(user_input)


def main():
    """
    Main function to demonstrate basic arithmetic operations.
    """
    # Get user input and convert to numeric types
    try:
        x = get_number_input("Enter the first number (x): ")
        y = get_number_input("Enter the second number (y): ")
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    print("=== Basic Calculator Demo ===")
    calculate_and_display(x, y)

if __name__ == "__main__":
    main()
