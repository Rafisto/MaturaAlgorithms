import time


def measureTime(method, cases):
    start = time.time()
    for case in cases:
        method(case)
    end = time.time()
    return end - start
