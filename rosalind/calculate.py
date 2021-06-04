def fib_sequence(n, k):
    """
    Calculates the n-th element of a Fibonacci sequence
    """
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, b + a * k
    return b
