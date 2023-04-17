def BinarySearch(array, left, right, x):
    """
    One of the fastest searching algorithms.
    Prerequisites: array order must be non-descending
    :param array: array that contains searched value x
    :param left: start of the search range
    :param right: end of the search range
    :param x: searched value
    :return: index of x in array
    """
    while left <= right:
        mid = left + (right - 1) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    raise Exception("Item not found")


a = [1, 2, 3, 5, 10, 20, 59, 940, 1490294, 19240192401294, 1924012940214910, 124019240124920419240]
v = 2
print(BinarySearch(a, 0, len(a) - 1, v))
