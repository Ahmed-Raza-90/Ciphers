import pandas as pd

# =================================
# ENCRYPTION
# =================================
def encrypt(text, key):
    """
    Columnar Transposition Cipher
    """
    text = text.replace(" ", "").upper()
    key = key.upper()
    n_cols = len(key)
    n_rows = -(-len(text) // n_cols)  # ceiling division

    # Fill the grid row-wise
    grid = []
    idx = 0
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            if idx < len(text):
                row.append(text[idx])
                idx += 1
            else:
                row.append("X")  # padding
        grid.append(row)

    # Dry run table
    df = pd.DataFrame(grid, columns=list(key))
    
    # Read columns based on alphabetical order of key
    sorted_key = sorted([(k, i) for i, k in enumerate(key)], key=lambda x: x[0])
    cipher_text = ""
    for _, col_idx in sorted_key:
        for r in range(n_rows):
            cipher_text += grid[r][col_idx]

    return df, cipher_text

# =================================
# DECRYPTION
# =================================
def decrypt(text, key):
    text = text.replace(" ", "").upper()
    key = key.upper()
    n_cols = len(key)
    n_rows = -(-len(text) // n_cols)  # ceiling division

    # Determine column lengths
    sorted_key = sorted([(k, i) for i, k in enumerate(key)], key=lambda x: x[0])
    cols = {}
    idx = 0
    for _, col_idx in sorted_key:
        col_len = n_rows
        cols[col_idx] = list(text[idx:idx+col_len])
        idx += col_len

    # Reconstruct grid row-wise
    grid = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            row.append(cols[c][r])
        grid.append(row)

    df = pd.DataFrame(grid, columns=list(key))
    plain_text = "".join("".join(row) for row in grid).rstrip("X")
    return df, plain_text
