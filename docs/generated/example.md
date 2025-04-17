# Documentation for `example.py`

```python
"""
This script determines whether a given number is even or odd.

It prompts the user to enter an integer and then uses the modulo operator
to check for divisibility by 2. Based on the result, it prints whether
the number is even or odd to the console.
"""

# Ask the user to enter a number and convert it to an integer.
num = int(input("Enter a number: "))

# Check if the number is even by using the modulo operator (%).
# If the remainder of the division by 2 is 0, the number is even.
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
```