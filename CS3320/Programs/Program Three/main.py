import math
def mysine(x):
    result = 0
    for n in range(10):
        sign = (-1) ** n
        term = x ** (2 * n + 1) / math.factorial(2 * n + 1)
        result += sign * term
    return result
