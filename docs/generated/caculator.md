# Documentation for `caculator.py`

```python
"""
A simple command-line calculator program.

This script defines basic arithmetic operations (add, subtract, multiply, divide)
and a main calculator function that takes user input to perform these operations.
It prompts the user to select an operation and enter two numbers, then displays the result.
Handles potential division by zero errors and invalid input gracefully.
"""
def add(x, y):
    """Calculate the sum of two numbers.

    This function takes two numerical arguments and returns their sum.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y


def subtract(x, y):
    """Calculate the difference between two numbers.

    This function subtracts the second number (y) from the first number (x).

    Args:
        x (float): The first number (minuend).
        y (float): The second number (subtrahend).

    Returns:
        float: The difference of x and y (x - y).
    """
    return x - y


def multiply(x, y):
    """Calculate the product of two numbers.

    This function multiplies two numerical arguments and returns their product.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y


def divide(x, y):
    """Calculate the quotient of two numbers.

    This function divides the first number (x) by the second number (y).
    It handles division by zero by returning an error message.

    Args:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float or str: The quotient of x and y if y is not zero.
                      Returns an error message string "Error! Division by zero." if y is zero.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    """Run the simple calculator program.

    This function presents a menu of operations to the user, takes user input
    for the choice of operation and two numbers, performs the selected calculation,
    and then prints the result to the console. It also includes error handling
    for invalid input types and operation choices.
    """
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ") # Get user's choice of operation

    if choice in ('1', '2', '3', '4'): # Check if the choice is valid
        try:
            num1 = float(input("Enter first number: ")) # Get the first number from the user and convert to float
            num2 = float(input("Enter second number: ")) # Get the second number from the user and convert to float
        except ValueError:
            print("Invalid input. Please enter numeric values.") # Handle non-numeric input
            return # Exit the function if input is invalid

        if choice == '1': # Perform addition
            print(f"Result: {add(num1, num2)}")
        elif choice == '2': # Perform subtraction
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3': # Perform multiplication
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4': # Perform division
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice") # Handle invalid operation choice

if __name__ == "__main__":
    calculator() # Execute the calculator function when the script is run directly
```