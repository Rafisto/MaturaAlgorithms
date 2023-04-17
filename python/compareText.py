def compareText(s1, s2):
    """
    :param s1: string one
    :param s2: string two
    :return: true if strings are equal, else false
    """
    if s1 == s2:
        return True
    return False


print(compareText("abc", "abc"))
print(compareText("abc", "def"))
