import pandas as pd

# =========================
# CREATE 5x5 MATRIX
# =========================
def create_matrix(key):
    key = key.lower().replace('j', 'i')
    used = []

    for c in key:
        if c.isalpha() and c not in used:
            used.append(c)

    for c in "abcdefghiklmnopqrstuvwxyz":
        if c not in used:
            used.append(c)

    return [used[i:i+5] for i in range(0, 25, 5)]


def matrix_dataframe(matrix):
    return pd.DataFrame(matrix, columns=["1", "2", "3", "4", "5"])


def find_pos(matrix, c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j


# =========================
# TEXT PREPARATION
# =========================
def prepare(text):
    text = text.lower().replace('j', 'i')
    text = ''.join(c for c in text if c.isalpha())

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'x'

        if a == b:
            result += a + 'x'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += 'x'

    return result


# =========================
# NORMAL ENCRYPT
# =========================
def encrypt(text, key):
    matrix = create_matrix(key)
    text = prepare(text)
    result = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i + 1])

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result


# =========================
# NORMAL DECRYPT
# =========================
def decrypt(text, key):
    matrix = create_matrix(key)
    result = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i + 1])

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result


# =========================
# ENCRYPT WITH DRY RUN
# =========================
def encrypt_with_table(text, key):
    matrix = create_matrix(key)
    prepared = prepare(text)

    rows = []
    cipher_text = ""

    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i + 1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            c_a = matrix[r1][(c1 + 1) % 5]
            c_b = matrix[r2][(c2 + 1) % 5]
            rule = "Same Row"
        elif c1 == c2:
            c_a = matrix[(r1 + 1) % 5][c1]
            c_b = matrix[(r2 + 1) % 5][c2]
            rule = "Same Column"
        else:
            c_a = matrix[r1][c2]
            c_b = matrix[r2][c1]
            rule = "Rectangle"

        pair = c_a + c_b
        cipher_text += pair
        rows.append([a + b, rule, pair])

    df = pd.DataFrame(rows, columns=["Plain Pair", "Rule", "Cipher Pair"])
    return matrix_dataframe(matrix), df, cipher_text


# =========================
# DECRYPT WITH DRY RUN
# =========================
def decrypt_with_table(text, key):
    matrix = create_matrix(key)

    rows = []
    plain_text = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            p_a = matrix[r1][(c1 - 1) % 5]
            p_b = matrix[r2][(c2 - 1) % 5]
            rule = "Same Row"
        elif c1 == c2:
            p_a = matrix[(r1 - 1) % 5][c1]
            p_b = matrix[(r2 - 1) % 5][c2]
            rule = "Same Column"
        else:
            p_a = matrix[r1][c2]
            p_b = matrix[r2][c1]
            rule = "Rectangle"

        pair = p_a + p_b
        plain_text += pair
        rows.append([a + b, rule, pair])

    df = pd.DataFrame(rows, columns=["Cipher Pair", "Rule", "Plain Pair"])
    return matrix_dataframe(matrix), df, plain_text
