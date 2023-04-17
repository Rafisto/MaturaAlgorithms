import random


def naiveSearch(s, p):
    """
    Prints all occurrences (its start character) of a pattern in a text
    :param s: string
    :param p: pattern
    :return: None
    """
    n = len(s)
    m = len(p)
    for i in range(n - m):
        if p == s[i:i + m]:
            print(i)


def naiveSearchRes(s, p):
    """
    naiveSearch, but returns a result value
    :param s: string
    :param p: pattern
    :return: a string of length s pointing at the occurrences with the char (^), same length as the text
    """
    n = len(s)
    m = len(p)
    res = ""
    for i in range(n - m):
        if p == s[i:i + m]:
            res += "^"
        else:
            res += " "
    return res


charSet = ['A', 'B', 'C']
string = ''.join([charSet[random.randint(0, 2)] for i in range(100)])
pattern = ''.join([charSet[random.randint(0, 2)] for j in range(3)])

print(pattern)
print(string)
print(naiveSearchRes(string, pattern))
