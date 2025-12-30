import pandas as pd

def letter_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_letter(n):
    return chr(n + ord('A'))

def generate_mapping(key):
    if not key or len(key) != 26:
        raise ValueError("Key must be 26 unique letters")
    key = key.upper()
    if len(set(key)) != 26:
        raise ValueError("Key letters must be unique")
    mapping = {chr(i + 65): key[i] for i in range(26)}
    reverse_mapping = {v: k for k, v in mapping.items()}
    return mapping, reverse_mapping

# ENCRYPTION
def encrypt(text, key):
    mapping, _ = generate_mapping(key)
    dry_run = {"Plain Char": [], "Cipher Char": []}
    cipher_text = ""
    for c in text:
        if c.isalpha():
            dry_run["Plain Char"].append(c.upper())
            dry_run["Cipher Char"].append(mapping[c.upper()])
            cipher_text += mapping[c.upper()]
        else:
            cipher_text += c
    df = pd.DataFrame(dry_run)
    return df, cipher_text

# DECRYPTION
def decrypt(text, key):
    _, reverse_mapping = generate_mapping(key)
    dry_run = {"Cipher Char": [], "Plain Char": []}
    plain_text = ""
    for c in text:
        if c.isalpha():
            dry_run["Cipher Char"].append(c.upper())
            dry_run["Plain Char"].append(reverse_mapping[c.upper()])
            plain_text += reverse_mapping[c.upper()]
        else:
            plain_text += c
    df = pd.DataFrame(dry_run)
    return df, plain_text