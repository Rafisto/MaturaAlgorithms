import random


def InsertionSort(array):
    """
    Insertion sort
    :param array: input array
    :return: sorted array
    """
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and array[i] < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


v = [random.randint(0, 100) for i in range(20)]
print(v)
print(InsertionSort(v))
