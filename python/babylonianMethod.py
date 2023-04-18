def BabylonianMethod(n, e):
    """
    Approximate square root of n with accuracy e
    :param n: value to be calculated
    :param e: accuracy leve
    :return: approx. sqrt(n)
    """
    x = n
    y = 1
    while x - y > e:
        x = (x + y) / 2
        y = n / x
    return x


print(BabylonianMethod(n=9, e=0.01))
print(BabylonianMethod(n=16, e=0.01))
print(BabylonianMethod(n=17, e=0.01))
print(BabylonianMethod(n=2, e=0.0001))
