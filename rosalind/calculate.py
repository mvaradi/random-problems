def fib_sequence(n, k):
    """
    Calculates the n-th element of a Fibonacci sequence
    """
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, b + a * k
    return(b)


"""
Explanation with n = 5, k = 3:

Fn = Fn-1 + Fn-2*3

F1 = 1
F2 = 1
F3 = 1+1*3 = 4
F4 = 4 + 1*3 = 7
F5 = 7 + 4*3 = 19
"""

# print(fib_sequence(5, 3))
#  19

# print(fib_sequence(30, 3))
# 20444528200

