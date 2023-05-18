def convertToDecimal(value, base):
    """
    Convert any base to decimal
    Constraints: same as builtin int()
    :param value: value to convert
    :param base: base of the number
    :return: decimal integer
    :rtype: int
    """
    return int(value, base)


def convertFromDecimalToAny(value, base):
    """
    Convert from decimal to any base
    :param value: value to convert
    :param base: base of the number
    :return: value in the desired base
    :rtype: int
    """
    remainder = []
    while value != 0:
        remainder.append(value % base)
        value = value // base
    return ''.join([str(r) for r in reversed(remainder)])


print(convertToDecimal("1000", 2))
print(convertFromDecimalToAny(8, 2))
