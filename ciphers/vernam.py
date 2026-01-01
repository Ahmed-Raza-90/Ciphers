import pandas as pd

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def letter_to_num(c):
    return ord(c) - ord('A')

def num_to_letter(n):
    return chr((n % 26) + ord('A'))

def clean_text_and_key(text, key):
    clean_text = [c.upper() for c in text if c.isalpha()]
    clean_key = [c.upper() for c in key if c.isalpha()]

    if len(clean_text) != len(clean_key):
        raise ValueError("Key length must match number of letters in text")

    return clean_text, clean_key

def encrypt(text, key):
    plain, key_chars = clean_text_and_key(text, key)

    dry_run = {
        "Plain Char": [],
        "Key Char": [],
        "Plain Num": [],
        "Key Num": [],
        "Cipher Num": [],
        "Cipher Char": []
    }

    cipher_text = ""
    idx = 0

    for c in text:
        if c.isalpha():
            p = letter_to_num(plain[idx])
            k = letter_to_num(key_chars[idx])
            c_num = (p + k) % 26
            c_char = num_to_letter(c_num)

            dry_run["Plain Char"].append(plain[idx])
            dry_run["Key Char"].append(key_chars[idx])
            dry_run["Plain Num"].append(p)
            dry_run["Key Num"].append(k)
            dry_run["Cipher Num"].append(c_num)
            dry_run["Cipher Char"].append(c_char)

            cipher_text += c_char
            idx += 1
        else:
            cipher_text += c

    return pd.DataFrame(dry_run), cipher_text

def decrypt(text, key):
    cipher, key_chars = clean_text_and_key(text, key)

    dry_run = {
        "Cipher Char": [],
        "Key Char": [],
        "Cipher Num": [],
        "Key Num": [],
        "Plain Num": [],
        "Plain Char": []
    }

    plain_text = ""
    idx = 0

    for c in text:
        if c.isalpha():
            c_num = letter_to_num(cipher[idx])
            k = letter_to_num(key_chars[idx])
            p_num = (c_num - k) % 26
            p_char = num_to_letter(p_num)

            dry_run["Cipher Char"].append(cipher[idx])
            dry_run["Key Char"].append(key_chars[idx])
            dry_run["Cipher Num"].append(c_num)
            dry_run["Key Num"].append(k)
            dry_run["Plain Num"].append(p_num)
            dry_run["Plain Char"].append(p_char)

            plain_text += p_char
            idx += 1
        else:
            plain_text += c

    return pd.DataFrame(dry_run), plain_text
