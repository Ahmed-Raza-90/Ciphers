import pandas as pd

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# =============================
# BASIC HELPERS
# =============================
def clean_text(text):
    return "".join(c for c in text.upper() if c.isalpha())

def pad_text(text, size):
    while len(text) % size != 0:
        text += "X"
    return text

def mod_inverse(a, m=26):
    a %= m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Determinant has no modular inverse (invalid key)")

# =============================
# MATRIX MATH (NO NUMPY)
# =============================
def matrix_multiply(A, B):
    result = [[0] for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            result[i][0] += A[i][k] * B[k][0]
        result[i][0] %= 26
    return result

# ---------- 2x2 ----------
def det_2x2(m):
    return (m[0][0]*m[1][1] - m[0][1]*m[1][0]) % 26

def inv_2x2(m):
    det = det_2x2(m)
    det_inv = mod_inverse(det)
    inv = [
        [( m[1][1]*det_inv) % 26, (-m[0][1]*det_inv) % 26],
        [(-m[1][0]*det_inv) % 26, ( m[0][0]*det_inv) % 26]
    ]
    return det, det_inv, inv

# ---------- 3x3 ----------
def det_3x3(m):
    return (
        m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
      - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
      + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
    ) % 26

def inv_3x3(m):
    det = det_3x3(m)
    det_inv = mod_inverse(det)

    adj = [
        [
            (m[1][1]*m[2][2]-m[1][2]*m[2][1]),
            -(m[0][1]*m[2][2]-m[0][2]*m[2][1]),
            (m[0][1]*m[1][2]-m[0][2]*m[1][1])
        ],
        [
            -(m[1][0]*m[2][2]-m[1][2]*m[2][0]),
            (m[0][0]*m[2][2]-m[0][2]*m[2][0]),
            -(m[0][0]*m[1][2]-m[0][2]*m[1][0])
        ],
        [
            (m[1][0]*m[2][1]-m[1][1]*m[2][0]),
            -(m[0][0]*m[2][1]-m[0][1]*m[2][0]),
            (m[0][0]*m[1][1]-m[0][1]*m[1][0])
        ]
    ]

    inv = [[(adj[j][i] * det_inv) % 26 for i in range(3)] for j in range(3)]
    return det, det_inv, adj, inv

# =============================
# ENCRYPTION
# =============================
def hill_encrypt(text, key):
    size = len(key)
    text = pad_text(clean_text(text), size)

    rows = []
    result = ""

    for i in range(0, len(text), size):
        block = text[i:i+size]
        vec = [[ALPHABET.index(c)] for c in block]
        cipher_vec = matrix_multiply(key, vec)

        rows.append({
            "Plain Block": block,
            "Plain Numbers": [v[0] for v in vec],
            "Calculation": f"{key} x {[v[0] for v in vec]}",
            "Cipher Numbers": [v[0] for v in cipher_vec],
            "Cipher Block": "".join(ALPHABET[v[0]] for v in cipher_vec)
        })

        result += "".join(ALPHABET[v[0]] for v in cipher_vec)

    return pd.DataFrame(rows), result

# =============================
# DECRYPTION
# =============================
def hill_decrypt(text, key):
    size = len(key)
    text = pad_text(clean_text(text), size)

    if size == 2:
        _, _, inv_key = inv_2x2(key)
    else:
        _, _, _, inv_key = inv_3x3(key)

    rows = []
    result = ""

    for i in range(0, len(text), size):
        block = text[i:i+size]
        vec = [[ALPHABET.index(c)] for c in block]
        plain_vec = matrix_multiply(inv_key, vec)

        # Full calculation string
        calc_str = f"{inv_key} x {[v[0] for v in vec]} = {[v[0] for v in plain_vec]}"

        rows.append({
            "Cipher Block": block,
            "Cipher Numbers": [v[0] for v in vec],
            "Calculation": calc_str,
            "Plain Numbers": [v[0] for v in plain_vec],
            "Plain Block": "".join(ALPHABET[v[0]] for v in plain_vec)
        })

        result += "".join(ALPHABET[v[0]] for v in plain_vec)

    return pd.DataFrame(rows), result
