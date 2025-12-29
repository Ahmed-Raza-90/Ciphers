import pandas as pd

# =================================
# HELPER FUNCTIONS
# =================================
def letter_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_letter(n):
    return chr(n + ord('A'))

# =================================
# GENERATE KEY STREAM (repeating key)
# =================================
def generate_keystream(text, key):
    key = key.upper()
    keystream = ""
    key_index = 0
    for c in text:
        if c.isalpha():
            keystream += key[key_index % len(key)]
            key_index += 1
        else:
            keystream += c
    return keystream

# =================================
# ENCRYPTION
# =================================
def encrypt(text, key):
    keystream = generate_keystream(text, key)
    dry_run = {"Plain Char": [], "Key Char": [], "Cipher Char": []}
    cipher_text = ""
    
    for t, k in zip(text, keystream):
        if t.isalpha():
            t_num = letter_to_num(t)
            k_num = letter_to_num(k)
            c_num = (t_num + k_num) % 26
            c_char = num_to_letter(c_num)
            dry_run["Plain Char"].append(t.upper())
            dry_run["Key Char"].append(k)
            dry_run["Cipher Char"].append(c_char)
            cipher_text += c_char
        else:
            cipher_text += t
    
    df = pd.DataFrame(dry_run)
    return df, cipher_text

# =================================
# DECRYPTION
# =================================
def decrypt(text, key):
    keystream = generate_keystream(text, key)
    dry_run = {"Cipher Char": [], "Key Char": [], "Plain Char": []}
    plain_text = ""
    
    for c, k in zip(text, keystream):
        if c.isalpha():
            c_num = letter_to_num(c)
            k_num = letter_to_num(k)
            p_num = (c_num - k_num) % 26
            p_char = num_to_letter(p_num)
            dry_run["Cipher Char"].append(c)
            dry_run["Key Char"].append(k)
            dry_run["Plain Char"].append(p_char)
            plain_text += p_char
        else:
            plain_text += c
    
    df = pd.DataFrame(dry_run)
    return df, plain_text
