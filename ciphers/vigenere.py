# vigenere.py
import pandas as pd

# =================================
# A–Z TABLE (A=0 … Z=25)
# =================================
def alphabet_table():
    return {chr(ord('A') + i): i for i in range(26)}
   

# =================================
# KEY GENERATION
# =================================
def generate_key(text, key):
    key = key.upper()
    new_key = ""
    j = 0
    for char in text:
        if char.isalpha():
            new_key += key[j % len(key)]
            j += 1
        else:
            new_key += char
    return new_key

# =================================
# BASIC ENCRYPT
# =================================
def encrypt(plaintext, key):
    table = alphabet_table()
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)

    cipher = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            total = (table[plaintext[i]] + table[key[i]]) % 26
            cipher += chr(total + ord('A'))
        else:
            cipher += plaintext[i]
    return cipher

# =================================
# BASIC DECRYPT
# =================================
def decrypt(ciphertext, key):
    table = alphabet_table()
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)

    plain = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            total = (table[ciphertext[i]] - table[key[i]]) % 26
            plain += chr(total + ord('A'))
        else:
            plain += ciphertext[i]
    return plain

# =================================
# ENCRYPT WITH FULL DRY RUN TABLE
# =================================
def vigenere_encrypt_with_table(plaintext, key):
    table = alphabet_table()
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)

    data = {
        "Plain Text": [],
        "Plain Value": [],
        "Key": [],
        "Key Value": [],
        "Sum": [],
        "Cipher Text": []
    }

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            p_val = table[plaintext[i]]
            k_val = table[key[i]]
            total = (p_val + k_val) % 26
            cipher_char = chr(total + ord('A'))
        else:
            p_val = k_val = total = "-"
            cipher_char = plaintext[i]

        data["Plain Text"].append(plaintext[i])
        data["Plain Value"].append(p_val)
        data["Key"].append(key[i])
        data["Key Value"].append(k_val)
        data["Sum"].append(total)
        data["Cipher Text"].append(cipher_char)

    return pd.DataFrame(data)


