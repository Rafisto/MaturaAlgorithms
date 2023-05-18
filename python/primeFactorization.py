import math


def PrimeFactorization(n):
    """
    Decompose a number into a list of prime factors
    :param n: number to factorize
    :return: all factors of n in a list
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, math.isqrt(n), 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


print(PrimeFactorization(496))
print(PrimeFactorization(1*2*3*4*5*6*7*8*9*10))
