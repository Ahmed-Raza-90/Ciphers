import pandas as pd

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"No modular inverse for a={a} under mod {m}")

def letter_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_letter(n):
    return chr(n + ord('A'))

# ENCRYPTION
def encrypt(text, key):
    if not key or len(key.split(',')) != 2:
        raise ValueError("Key must be in format 'a,b' (e.g., 5,8)")
    a, b = map(int, key.split(','))
    if a % 2 == 0 or a % 13 == 0:
        raise ValueError("Key 'a' must be coprime with 26")
    
    dry_run = {"Plain Char": [], "Number": [], "Cipher Number": [], "Cipher Char": []}
    cipher_text = ""
    
    for c in text:
        if c.isalpha():
            x = letter_to_num(c)
            y = (a*x + b) % 26
            dry_run["Plain Char"].append(c.upper())
            dry_run["Number"].append(x)
            dry_run["Cipher Number"].append(y)
            dry_run["Cipher Char"].append(num_to_letter(y))
            cipher_text += num_to_letter(y)
        else:
            cipher_text += c
    
    df = pd.DataFrame(dry_run)
    return df, cipher_text

# DECRYPTION
def decrypt(text, key):
    if not key or len(key.split(',')) != 2:
        raise ValueError("Key must be in format 'a,b' (e.g., 5,8)")
    a, b = map(int, key.split(','))
    a_inv = mod_inverse(a, 26)
    
    dry_run = {"Cipher Char": [], "Cipher Number": [], "Plain Number": [], "Plain Char": []}
    plain_text = ""
    
    for c in text:
        if c.isalpha():
            y = letter_to_num(c)
            x = (a_inv * (y - b)) % 26
            dry_run["Cipher Char"].append(c.upper())
            dry_run["Cipher Number"].append(y)
            dry_run["Plain Number"].append(x)
            dry_run["Plain Char"].append(num_to_letter(x))
            plain_text += num_to_letter(x)
        else:
            plain_text += c
    
    df = pd.DataFrame(dry_run)
    return df, plain_text