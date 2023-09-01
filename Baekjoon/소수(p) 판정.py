def isPrime(n):
    import math

    if n == 1: return False
    if n == 2: return True
    if math.factorial(n - 1) % n == n - 1: return True
    return False
# 윌슨의 정리

def isPrime(n):
    import math

    if n == 1: return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

# 제곱근 까지 브루트포스로 
