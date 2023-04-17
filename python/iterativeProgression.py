def Progression(x):
    return x ** 2


def IterativeProgression(function, n):
    """
    Prints consecutive progression values from 1 to n
    :param function: Progression function
    :param n: element count
    :return: array of consecutive elements
    """
    res = []
    for i in range(1, n + 1):
        res.append(Progression(i))

    return res


print(IterativeProgression(Progression, 10))
