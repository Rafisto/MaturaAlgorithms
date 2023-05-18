def GCD(a, b):
    """
    Compute GCD - greatest common divisor of two numbers a, b
    :param a: first number
    :param b: second number
    :return: GCD of a, b
    :rtype: int
    """
    while b != 1:
        r = a % b
        if r == 0:
            return b
        else:
            a, b = b, r
    return 1


def LCM(a, b):
    """
    Compute LCM - least common multiple of two numbers a, b
    Algorithm uses GCD defined previously
    :param a: first number
    :param b: second number
    :return: LCM of a, b
    :rtype: int
    """
    return (a * b) // GCD(a, b)


print(GCD(7, 8))
print(LCM(7, 8))
