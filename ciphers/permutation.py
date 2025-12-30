import pandas as pd

# =========================
# FLEXIBLE KEY PARSER
# =========================
def parse_key(key):
    if isinstance(key, str):
        key = key.strip()
        if key.startswith("[") and key.endswith("]"):
            key = key[1:-1]
        return [int(k.strip()) for k in key.split(",")]
    elif isinstance(key, list):
        return [int(k) for k in key]
    else:
        raise ValueError("Key must be a list or comma-separated string")

# =========================
# ENCRYPTION
# =========================
def encrypt(text, key):
    text = text.replace(" ", "").upper()
    key = parse_key(key)
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
        dry_run["Key"].append(key.copy())
        dry_run["Cipher Block"].append("".join(cipher_block))

    df = pd.DataFrame(dry_run)
    return df, cipher_text

# =========================
# DECRYPTION
# =========================
def decrypt(text, key):
    text = text.replace(" ", "").upper()
    key = parse_key(key)
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
        dry_run["Key"].append(key.copy())
        dry_run["Plain Block"].append("".join(plain_block))

    df = pd.DataFrame(dry_run)
    return df, plain_text.rstrip("X")