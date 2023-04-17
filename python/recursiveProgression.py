def Progression(x):
    return x ** 2


def RecursiveProgression(function, n, res):
    """
    Prints consecutive progression values from 0 to n
    :param function: Progression function
    :param n: element count
    :param res: result cache
    :return: array of consecutive elements
    """
    if len(res) == n:
        return res
    v = function(len(res) + 1)
    res.append(v)
    print(v)
    RecursiveProgression(function, n, res)


RecursiveProgression(Progression, 10, [])
