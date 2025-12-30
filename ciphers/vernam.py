import pandas as pd

def letter_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_letter(n):
    return chr(n + ord('A'))

def vernam_cipher(text, key):
    if not key or len(key) != len(text.replace(" ", "")):
        raise ValueError("Key length must match text length (excluding spaces)")

    dry_run = {"Plain Char": [], "Key Char": [], "Cipher Char": []}
    cipher_text = ""
    key_index = 0

    for c in text:
        if c.isalpha():
            t_num = letter_to_num(c)
            k_num = letter_to_num(key[key_index])
            cipher_num = t_num ^ k_num  
            cipher_char = num_to_letter(cipher_num)
            dry_run["Plain Char"].append(c.upper())
            dry_run["Key Char"].append(key[key_index].upper())
            dry_run["Cipher Char"].append(cipher_char)
            cipher_text += cipher_char
            key_index += 1
        else:
            cipher_text += c

    df = pd.DataFrame(dry_run)
    return df, cipher_text

def encrypt(text, key):
    return vernam_cipher(text, key)

def decrypt(text, key):
    return vernam_cipher(text, key)