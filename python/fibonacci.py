def FibonacciRecursive(n):
    """
    Fibonacci recursive algorithm
    :param n: how many times
    :return: n-th fibonacci progression element
    """
    if n <= 1:
        return n
    return FibonacciRecursive(n - 1) + FibonacciRecursive(n - 2)


def FibonacciIterative(n):
    """
    Fibonacci iterative algorithm
    :param n: iteration count
    :return: n element list of fibonacci progression
    """
    v = [0, 1]
    for i in range(2, n):
        v.append(v[i - 1] + v[-2])
    return v


print([FibonacciRecursive(k) for k in range(20)])
print(FibonacciIterative(20))
