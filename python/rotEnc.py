def encodeROT(message, base):
    """
    Caesar cipher, shift extended to every integer
    :param message: message to be encoded
    :param base: shift integer
    :return: encoded string
    """
    res = ""
    for c in message:
        res += chr((ord(c) - 97 + base) % 26 + 97)
    return res


def decodeROT(message, base):
    """
    Caesar decipher, unshift extended to every integer
    :param message: message to be decoded
    :param base: unshift integer
    :return: decode string
    """
    res = ""
    for c in message:
        res += chr((ord(c) - 97 - base) % 26 + 97)
    return res


print(encodeROT("qwertyuiopasdfgjklzxcvbnm", 13))
print(decodeROT("djreglhvbcnfqstwxymkpioaz", 13))
