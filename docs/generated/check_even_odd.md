# Documentation for `check_even_odd.py`

```python
"""
This script determines whether a given number is even or odd.

It prompts the user to enter an integer and then uses the modulo operator
to check for divisibility by 2. The result is printed to the console,
indicating whether the input number is even or odd.
"""

# Ask the user for a number and convert it to an integer.
num = int(input("Enter a number: "))

# Check if the number is even or odd using the modulo operator (%).
# If the remainder of the division by 2 is 0, the number is even.
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```