import pandas as pd

# =================================
# HELPER FUNCTIONS
# =================================
def letter_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_letter(n):
    return chr(n + ord('A'))

# =================================
# ENCRYPTION
# =================================
def encrypt(text, key):
    """
    Simple Block Cipher:
    - Block size = length of key
    - Each letter in block shifted by corresponding key letter (A=0..Z=25)
    """
    key = key.upper()
    block_size = len(key)
    dry_run = {"Block": [], "Plain Block": [], "Key Block": [], "Cipher Block": []}
    cipher_text = ""

    text_nospace = text.replace(" ", "").upper()
    for i in range(0, len(text_nospace), block_size):
        block = text_nospace[i:i+block_size]
        cipher_block = ""
        key_block = key[:len(block)]
        for t, k in zip(block, key_block):
            c_num = (letter_to_num(t) + letter_to_num(k)) % 26
            cipher_block += num_to_letter(c_num)
        cipher_text += cipher_block
        dry_run["Block"].append(i//block_size + 1)
        dry_run["Plain Block"].append(block)
        dry_run["Key Block"].append(key_block)
        dry_run["Cipher Block"].append(cipher_block)

    df = pd.DataFrame(dry_run)
    return df, cipher_text

# =================================
# DECRYPTION
# =================================
def decrypt(text, key):
    key = key.upper()
    block_size = len(key)
    dry_run = {"Block": [], "Cipher Block": [], "Key Block": [], "Plain Block": []}
    plain_text = ""

    text_nospace = text.replace(" ", "").upper()
    for i in range(0, len(text_nospace), block_size):
        block = text_nospace[i:i+block_size]
        key_block = key[:len(block)]
        plain_block = ""
        for c, k in zip(block, key_block):
            p_num = (letter_to_num(c) - letter_to_num(k)) % 26
            plain_block += num_to_letter(p_num)
        plain_text += plain_block
        dry_run["Block"].append(i//block_size + 1)
        dry_run["Cipher Block"].append(block)
        dry_run["Key Block"].append(key_block)
        dry_run["Plain Block"].append(plain_block)

    df = pd.DataFrame(dry_run)
    return df, plain_text
