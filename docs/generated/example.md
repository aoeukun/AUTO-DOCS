# Documentation for `example.py`

# Checking Even or Odd
=====================

This Python program prompts the user to enter a number and then checks whether the number is even or odd.

### Execution

To execute this program, simply run the script. You will be prompted to enter a number. After entering a number, the program will print a message indicating whether the number is even or odd.

### Program Flow

Here's a step-by-step breakdown of the program's execution:

#### 1. User Input

The program asks the user to enter a number using the `input` function, which returns a string. This input is then converted to an integer using the `int` function.

```python
num = int(input("Enter a number: "))
```

#### 2. Checking Even or Odd

The program checks if the number is even or odd using the modulus operator (`%`). If the remainder of the division of the number by 2 is 0, the number is even; otherwise, it's odd.

```python
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```

### Notes

* This program does not handle non-numeric inputs. If the user enters a non-numeric value, the program will raise a `ValueError`.
* This program does not perform any error handling or validation for invalid inputs.
* The program assumes that the user will enter a whole number. If the user enters a decimal number, the program will treat it as an integer (truncating the decimal part).