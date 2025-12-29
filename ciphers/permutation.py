import pandas as pd

# =================================
# ENCRYPTION
# =================================
def encrypt(text, key):
    """
    Simple Permutation Cipher
    - key = list of indices showing new order
    Example: key = [3,1,2,0] means 0th char goes to 3rd, 1st to 1st, etc.
    """
    text = text.replace(" ", "").upper()
    key = [int(k) for k in key.split(",")]
    block_size = len(key)
    dry_run = {"Block": [], "Plain Block": [], "Key": [], "Cipher Block": []}
    cipher_text = ""

    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        if len(block) < block_size:
            block += "X"*(block_size-len(block))
        cipher_block = [""]*block_size
        for idx, k in enumerate(key):
            cipher_block[k] = block[idx]
        cipher_text += "".join(cipher_block)
        dry_run["Block"].append(i//block_size + 1)
        dry_run["Plain Block"].append(block)
        dry_run["Key"].append(key)
        dry_run["Cipher Block"].append("".join(cipher_block))

    df = pd.DataFrame(dry_run)
    return df, cipher_text

# =================================
# DECRYPTION
# =================================
def decrypt(text, key):
    text = text.replace(" ", "").upper()
    key = [int(k) for k in key.split(",")]
    block_size = len(key)
    dry_run = {"Block": [], "Cipher Block": [], "Key": [], "Plain Block": []}
    plain_text = ""

    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        plain_block = [""]*block_size
        for idx, k in enumerate(key):
            plain_block[idx] = block[k]
        plain_text += "".join(plain_block)
        dry_run["Block"].append(i//block_size + 1)
        dry_run["Cipher Block"].append(block)
        dry_run["Key"].append(key)
        dry_run["Plain Block"].append("".join(plain_block))

    df = pd.DataFrame(dry_run)
    return df, plain_text.rstrip("X")
