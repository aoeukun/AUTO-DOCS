def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

limit = int(input("Generate Fibonacci sequence up to: "))
print(fibonacci(limit))
