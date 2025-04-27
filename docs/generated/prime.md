# Documentation for `prime.py`

```python
"""
This module provides a function to determine if a given number is prime.

It includes a function `is_prime(n)` that efficiently checks for primality and
demonstrates its usage by testing numbers from 1 to 20.
"""

def is_prime(n):
    """Check if a number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    This function efficiently checks for primality by iterating only up to the square root of the input number.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(10)
        False
        >>> is_prime(17)
        True
    """
    if n <= 1:
        # Numbers less than or equal to 1 are not prime.
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # Iterate from 2 up to the square root of n.
        # We only need to check divisors up to the square root of n.
        if n % i == 0:
            # If n is divisible by any number in this range, it's not prime.
            return False
    return True

# Test the function and print results for numbers 1 to 20
for num in range(1, 21):
    print(f"{num} is prime? {is_prime(num)}")
```