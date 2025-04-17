# Documentation for `caculator.py`

```python
"""
This module implements a simple command-line calculator.

It provides basic arithmetic operations (addition, subtraction,
multiplication, and division) through a user-friendly interactive interface.
The user is prompted to choose an operation and then enter two numbers to
perform the calculation. The result is then displayed to the user.
"""

def add(x, y):
    """Add two numbers.

    This function takes two numbers as input and returns their sum.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """Subtract two numbers.

    This function takes two numbers as input and returns their difference (x - y).

    Args:
        x (float): The first number (minuend).
        y (float): The second number (subtrahend).

    Returns:
        float: The difference of x and y.
    """
    return x - y

def multiply(x, y):
    """Multiply two numbers.

    This function takes two numbers as input and returns their product.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """Divide two numbers.

    This function takes two numbers as input and returns their quotient (x / y).
    It handles division by zero by returning an error message.

    Args:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float or str: The quotient of x and y if y is not zero.
                      Returns "Error! Division by zero." if y is zero.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    """Run a simple command-line calculator.

    This function presents a menu of operations to the user, takes user input
    for the choice of operation and two numbers, performs the selected
    calculation using helper functions (add, subtract, multiply, divide),
    and displays the result. It also includes basic error handling for
    invalid input (non-numeric input and invalid operation choice).
    """
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ") # Prompt user to enter their choice of operation

    if choice in ('1', '2', '3', '4'): # Check if the user's choice is valid
        try:
            num1 = float(input("Enter first number: ")) # Get the first number from the user
            num2 = float(input("Enter second number: ")) # Get the second number from the user
        except ValueError: # Handle potential ValueError if user enters non-numeric input
            print("Invalid input. Please enter numeric values.")
            return # Exit the function if input is invalid

        if choice == '1': # Perform addition
            print(f"Result: {add(num1, num2)}")
        elif choice == '2': # Perform subtraction
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3': # Perform multiplication
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4': # Perform division
            print(f"Result: {divide(num1, num2)}")
    else: # Handle invalid operation choice
        print("Invalid choice")

if __name__ == "__main__":
    calculator() # Execute the calculator function when the script is run directly
```