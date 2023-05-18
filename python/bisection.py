def BisectionMethod(function, a, b, precision):
    """
    Prerequisites: f(x) continuous in [a,b], f(a)*f(b)<0
    :param function: f(x)
    :param a: range start
    :param b: range end
    :param precision: return approximation if < abs(a-b)
    :return: approximated root of a function f(x)
    """
    if function(a) * function(b) >= 0:
        raise Exception("The base condition not met: f(a)*f(b)<0")

    c = a
    while (b - a) >= precision:
        c = (a + b) / 2
        if function(c) == 0.0:
            break
        if function(c) * function(a) < 0:
            b = c
        else:
            a = c

    return c


def Function(x):
    return x ** 3 + 2 * x ** 2


start = -3
end = -1
print(BisectionMethod(Function, start, end, 0.01))
