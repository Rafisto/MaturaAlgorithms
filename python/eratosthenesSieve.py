import math


def EratosthenesSieve(n):
    """
    An algorithm to find prime numbers from 2 to n
    :param n: number to generate
    :return: array of booleans, for which every true means an index of the number is prime
    """
    if n in [0, 1]:
        raise Exception("n should not be 1, nor 0")
    primes = [True for i in range(n)]
    primes[0] = primes[1] = False
    for i in range(2, math.isqrt(n)+1):
        if primes[i]:
            j = i ** 2
            while j < n:
                primes[j] = False
                j += i
    return primes


rng = EratosthenesSieve(1_000_000)
print(len([k for k in rng if k]))
print(', '.join([str(n) for n in range(len(rng)) if rng[n]]))
