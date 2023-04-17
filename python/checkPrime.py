from utils.measureTime import measureTime as time


def checkIfPrime(n):
    """
    :param n: an integer
    :return: is n prime?
    :rtype: bool
    """
    if n in [1, 0]:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def checkIfPrimeEfficient(n):
    """
    :param n: an integer
    :return: is n prime?
    :rtype: bool
    """
    if n in [1, 0]:
        return False
    if n <= 3:
        return True
    if n % 3 == 0 or n % 2 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# tests

print(time(checkIfPrime, [n for n in range(1_000_000)]))
print(time(checkIfPrimeEfficient, [n for n in range(1_000_000)]))
