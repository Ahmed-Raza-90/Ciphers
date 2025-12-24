def mod_inverse(a, m):
    for i in range(1, m):
        if (a*i) % m == 1:
            return i
    raise ValueError


def encrypt(text, key):
    a, b = map(int, key.split(','))
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((a*(ord(c)-base)+b) % 26 + base)
        else:
            result += c
    return result


def decrypt(text, key):
    a, b = map(int, key.split(','))
    a_inv = mod_inverse(a, 26)
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((a_inv*((ord(c)-base)-b)) % 26 + base)
        else:
            result += c
    return result
