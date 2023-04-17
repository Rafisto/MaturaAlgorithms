import random


def BubbleSort(array):
    """
    Bubble sort
    :param array: input array
    :return: sorted array
    """
    sortd = False
    while not sortd:
        print(array)
        sortd = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sortd = False
                array[i], array[i + 1] = array[i + 1], array[i]
                break
    return array


print(BubbleSort([random.randint(0, 100) for i in range(20)]))
