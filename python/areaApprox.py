def ApproxArea(f, a, b, n):
    """
    Approximate the area under the curve given by the function f, within range [a,b] and n sample trapezoids
    :param f: Function
    :param a: Start of range
    :param b: End of range
    :param n: Number X-axis of trapezoid splits
    :return: definite integral of a function f from a to b
    """
    delta_x = (b - a) / n

    total = 0
    for i in range(n):
        x = a + delta_x * i
        total += delta_x * (f(x) + f(x + delta_x)) / 2
    return total


def Func(x):
    return x ** 2


area = ApproxArea(Func, 0.0, 1.0, 100)
print(area)
