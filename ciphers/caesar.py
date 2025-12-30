import pandas as pd

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# ENCRYPT
def encrypt_with_table(text, shift):
    rows = []

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            original_pos = ord(ch) - base
            shifted_pos = (original_pos + shift) % 26
            cipher_char = chr(shifted_pos + base)

            rows.append({
                "Plain Char": ch,
                "Plain Index": original_pos,
                "Shift": shift,
                "Cipher Index": shifted_pos,
                "Cipher Char": cipher_char
            })
        else:
            rows.append({
                "Plain Char": ch,
                "Plain Index": "-",
                "Shift": "-",
                "Cipher Index": "-",
                "Cipher Char": ch
            })

    return pd.DataFrame(rows)

# DECRYPT
def decrypt_with_table(text, shift):
    rows = []

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            cipher_pos = ord(ch) - base
            plain_pos = (cipher_pos - shift) % 26
            plain_char = chr(plain_pos + base)

            rows.append({
                "Cipher Char": ch,
                "Cipher Index": cipher_pos,
                "Shift": shift,
                "Plain Index": plain_pos,
                "Plain Char": plain_char
            })
        else:
            rows.append({
                "Cipher Char": ch,
                "Cipher Index": "-",
                "Shift": "-",
                "Plain Index": "-",
                "Plain Char": ch
            })

    return pd.DataFrame(rows)