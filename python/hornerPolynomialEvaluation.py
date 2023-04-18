def EvaluatePolynomial(coefficients, x):
    """
    Let P be a polynomial with given coefficients
    This method evaluates P(x) with the least amount of separate multiplications
    :param coefficients: polynomial coefficients
    :param x: value at which P is calculated
    :return: P(x)
    """
    result = 0
    for i in range(len(coefficients)):
        result = result * x + coefficients[i]
    return result


print(EvaluatePolynomial([2, -6, 2, -1], 3))
