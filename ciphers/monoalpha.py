def encrypt(text, key):
    if len(key) != 26:
        raise ValueError
    key = key.lower()
    result = ""
    for c in text:
        if c.isalpha():
            result += key[ord(c.lower()) - 97]
        else:
            result += c
    return result


def decrypt(text, key):
    if len(key) != 26:
        raise ValueError
    key = key.lower()
    rev = {key[i]: chr(97+i) for i in range(26)}
    result = ""
    for c in text:
        if c.isalpha():
            result += rev[c]
        else:
            result += c
    return result
