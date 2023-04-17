def EuclideanGCDIterative(a, b):
    """
    Compute GCD - greatest common divisor of two numbers a, b using Euclidean algorithm iterative method
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
            a, b = b, b - r


def EuclideanGCDRecursive(a, b):
    """
    Compute GCD - greatest common divisor of two numbers a, b using Euclidean algorithm recursive method
    :param a: first number
    :param b: second number
    :return: GCD of a, b
    :rtype: int
    """
    if a == 0:
        return b
    return EuclideanGCDRecursive(b % a, a)


first = 20
second = 30
print(EuclideanGCDIterative(first, second))
print(EuclideanGCDRecursive(first, second))
