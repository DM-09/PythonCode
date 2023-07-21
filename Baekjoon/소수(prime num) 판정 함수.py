def isPrime(n):
    import math

    if n == 2: return True
    if math.factorial(n - 1) % n == n - 1: return True
    return False
