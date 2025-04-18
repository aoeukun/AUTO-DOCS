def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
for num in range(1, 21):
    print(f"{num} is prime? {is_prime(num)}")
