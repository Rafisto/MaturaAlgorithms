def RecursiveSquaringExponentiation(x, n):
    """
    Raise x to the power of n using squaring exponentiation principle:
    x^n is equal to:
    x * x ** 2 ** (n-1)/2  <==> if n is odd
    x ** 2 ** (n/2)        <==> if n is even
    :param x: power base
    :param n: power exponent
    :return: x^n
    """
    if n < 0:
        return RecursiveSquaringExponentiation(1 / x, -1 * n)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return RecursiveSquaringExponentiation(x * x, n // 2)
    elif n % 2 != 0:
        return x * RecursiveSquaringExponentiation(x * x, (n - 1) // 2)


print(RecursiveSquaringExponentiation(5, 5))
