import random


def InsertionSort(array):
    """
    Insertion sort
    :param array: input array
    :return: sorted array
    """
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[i] < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = array[i]
    return array


print(InsertionSort([random.randint(0, 100) for i in range(20)]))
