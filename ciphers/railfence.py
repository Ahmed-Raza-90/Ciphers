import pandas as pd

def _pad_letters(letters, depth):
    cycle = 2 * (depth - 1)
    if cycle == 0:
        return letters

    rem = len(letters) % cycle
    if rem != 0:
        letters += ["X"] * (cycle - rem)

    return letters

# ENCRYPTION WITH ZIGZAG TABLE
def encrypt_with_table(text, depth):
    if depth <= 1:
        return pd.DataFrame(), text

    letters = [c for c in text if c != " "]
    letters = _pad_letters(letters, depth)
    n = len(letters)
    table = [["" for _ in range(n)] for _ in range(depth)]
    row = 0
    direction = 1

    for col, ch in enumerate(letters):
        table[row][col] = ch

        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1

        row += direction

    cipher_letters = ""
    for r in range(depth):
        for c in range(n):
            if table[r][c]:
                cipher_letters += table[r][c]

    result = []
    idx = 0
    for ch in text:
        if ch == " ":
            result.append(" ")
        else:
            result.append(cipher_letters[idx])
            idx += 1

    while idx < len(cipher_letters):
        result.append(cipher_letters[idx])
        idx += 1

    df = pd.DataFrame(table)
    df.index = [f"Rail {i+1}" for i in range(depth)]

    return df, "".join(result)

# DECRYPTION WITH ZIGZAG TABLE
def decrypt_with_table(cipher, depth):
    if depth <= 1:
        return pd.DataFrame(), cipher

    letters = [c for c in cipher if c != " "]
    n = len(letters)

    table = [["" for _ in range(n)] for _ in range(depth)]

    row = 0
    direction = 1
    for col in range(n):
        table[row][col] = "*"

        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1

        row += direction

    idx = 0
    for r in range(depth):
        for c in range(n):
            if table[r][c] == "*":
                table[r][c] = letters[idx]
                idx += 1

    row = 0
    direction = 1
    plain_letters = []

    for col in range(n):
        plain_letters.append(table[row][col])

        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1

        row += direction

    result = []
    idx = 0
    for ch in cipher:
        if ch == " ":
            result.append(" ")
        else:
            result.append(plain_letters[idx])
            idx += 1

    final_text = "".join(result).rstrip("X")

    df = pd.DataFrame(table)
    df.index = [f"Rail {i+1}" for i in range(depth)]

    return df, final_text

def encrypt(text, depth):
    return encrypt_with_table(text, depth)[1]


def decrypt(text, depth):
    return decrypt_with_table(text, depth)[1]