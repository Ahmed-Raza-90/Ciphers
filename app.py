# # app.py
# import streamlit as st

# from ciphers.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
# from ciphers.playfair import encrypt as playfair_encrypt, decrypt as playfair_decrypt
# from ciphers.vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt, vigenere_encrypt_with_table, vigenere_decrypt_with_table
# from ciphers.railfence import encrypt as rail_encrypt, decrypt as rail_decrypt
# from ciphers.affine import encrypt as affine_encrypt, decrypt as affine_decrypt
# from ciphers.monoalpha import encrypt as mono_encrypt, decrypt as mono_decrypt
# import pandas as pd

# st.set_page_config(page_title="Classical Ciphers", layout="centered")
# st.title("Classical Ciphers Tool")
# st.write("Educational implementation of classical cryptography algorithms.")

# cipher = st.sidebar.selectbox(
#     "Select Cipher",
#     [
#         "Caesar Cipher",
#         "Playfair Cipher",
#         "Vigenere Cipher",
#         "Rail Fence Cipher",
#         "Affine Cipher",
#         "Monoalphabetic Cipher"
#     ]
# )

# mode = st.sidebar.radio("Mode", ["Encrypt", "Decrypt"])
# key = st.sidebar.text_input("Key")
# text = st.text_area("Enter Text")

# if st.button("Run"):
#     if not text:
#         st.error("Text is required")
#     elif cipher == "Vigenere Cipher" and (not key.isalpha()):
#         st.error("Key must be an alphabets")
#     else:
#         try:
#             if cipher == "Caesar Cipher":
#                 if not key.isdigit():
#                     st.error("Key must be a number")
#                 else:
#                     result = caesar_encrypt(text, int(key)) if mode == "Encrypt" else caesar_decrypt(text, int(key))

#             elif cipher == "Playfair Cipher":
#                 result = playfair_encrypt(text, key) if mode == "Encrypt" else playfair_decrypt(text, key)

#             elif cipher == "Vigenere Cipher":
#                 if mode == "Encrypt":
#                     # Show dry-run table + final cipher
#                     df = vigenere_encrypt_with_table(text, key)
#                     st.subheader("Vigenere Encryption Dry Run")
#                     st.dataframe(df, use_container_width=True)
#                     result = "".join(df["Cipher Text"])
#                 else:
#                     # Show decryption dry-run table + final plain text
#                     df = vigenere_decrypt_with_table(text, key)
#                     st.subheader("Vigenere Decryption Dry Run")
#                     st.dataframe(df, use_container_width=True)
#                     result = "".join(df["Plain Text"])

#             elif cipher == "Rail Fence Cipher":
#                 if not key.isdigit():
#                     st.error("Key must be a number")
#                 else:
#                     result = rail_encrypt(text, int(key)) if mode == "Encrypt" else rail_decrypt(text, int(key))

#             elif cipher == "Affine Cipher":
#                 result = affine_encrypt(text, key) if mode == "Encrypt" else affine_decrypt(text, key)

#             elif cipher == "Monoalphabetic Cipher":
#                 result = mono_encrypt(text, key) if mode == "Encrypt" else mono_decrypt(text, key)

#             st.subheader("Result")
#             st.code(result)
            
#         except Exception:
#             st.error("Invalid input or key")




# # app.py
# import streamlit as st
# import pandas as pd

# from ciphers.caesar import (
#     encrypt as caesar_encrypt,
#     decrypt as caesar_decrypt,
#     encrypt_with_table as caesar_encrypt_with_table,
#     decrypt_with_table as caesar_decrypt_with_table
# )

# from ciphers.playfair import encrypt as playfair_encrypt, decrypt as playfair_decrypt
# from ciphers.vigenere import (
#     encrypt as vigenere_encrypt,
#     decrypt as vigenere_decrypt,
#     vigenere_encrypt_with_table,
#     vigenere_decrypt_with_table
# )
# from ciphers.railfence import encrypt as rail_encrypt, decrypt as rail_decrypt
# from ciphers.affine import encrypt as affine_encrypt, decrypt as affine_decrypt
# from ciphers.monoalpha import encrypt as mono_encrypt, decrypt as mono_decrypt


# st.set_page_config(page_title="Classical Ciphers", layout="centered")
# st.title("Classical Ciphers Tool")
# st.write("Educational implementation of classical cryptography algorithms.")

# cipher = st.sidebar.selectbox(
#     "Select Cipher",
#     [
#         "Caesar Cipher",
#         "Playfair Cipher",
#         "Vigenere Cipher",
#         "Rail Fence Cipher",
#         "Affine Cipher",
#         "Monoalphabetic Cipher"
#     ]
# )

# mode = st.sidebar.radio("Mode", ["Encrypt", "Decrypt"])
# key = st.sidebar.text_input("Key")
# text = st.text_area("Enter Text")

# if st.button("Run"):
#     if not text:
#         st.error("Text is required")

#     elif cipher == "Vigenere Cipher" and not key.isalpha():
#         st.error("Key must contain alphabets only")

#     else:
#         try:
#             # =========================
#             # CAESAR CIPHER
#             # =========================
#             if cipher == "Caesar Cipher":
#                 if not key.isdigit():
#                     st.error("Key must be a number")
#                 else:
#                     shift = int(key)

#                     if mode == "Encrypt":
#                         df = caesar_encrypt_with_table(text, shift)
#                         st.subheader("Caesar Encryption Dry Run")
#                         st.dataframe(df, use_container_width=True)
#                         result = "".join(df["Cipher Char"])
#                     else:
#                         df = caesar_decrypt_with_table(text, shift)
#                         st.subheader("Caesar Decryption Dry Run")
#                         st.dataframe(df, use_container_width=True)
#                         result = "".join(df["Plain Char"])

#             # =========================
#             # PLAYFAIR
#             # =========================
#             elif cipher == "Playfair Cipher":
#                 result = playfair_encrypt(text, key) if mode == "Encrypt" else playfair_decrypt(text, key)

#             # =========================
#             # VIGENERE
#             # =========================
#             elif cipher == "Vigenere Cipher":
#                 if mode == "Encrypt":
#                     df = vigenere_encrypt_with_table(text, key)
#                     st.subheader("Vigenere Encryption Dry Run")
#                     st.dataframe(df, use_container_width=True)
#                     result = "".join(df["Cipher Text"])
#                 else:
#                     df = vigenere_decrypt_with_table(text, key)
#                     st.subheader("Vigenere Decryption Dry Run")
#                     st.dataframe(df, use_container_width=True)
#                     result = "".join(df["Plain Text"])

#             # =========================
#             # RAIL FENCE
#             # =========================
#             elif cipher == "Rail Fence Cipher":
#                 if not key.isdigit():
#                     st.error("Key must be a number")
#                 else:
#                     result = rail_encrypt(text, int(key)) if mode == "Encrypt" else rail_decrypt(text, int(key))

#             # =========================
#             # AFFINE
#             # =========================
#             elif cipher == "Affine Cipher":
#                 result = affine_encrypt(text, key) if mode == "Encrypt" else affine_decrypt(text, key)

#             # =========================
#             # MONOALPHABETIC
#             # =========================
#             elif cipher == "Monoalphabetic Cipher":
#                 result = mono_encrypt(text, key) if mode == "Encrypt" else mono_decrypt(text, key)

#             st.subheader("Result")
#             st.code(result)

#         except Exception:
#             st.error("Invalid input or key")




import streamlit as st
import pandas as pd

from ciphers.caesar import (
    encrypt as caesar_encrypt,
    decrypt as caesar_decrypt,
    encrypt_with_table as caesar_encrypt_with_table,
    decrypt_with_table as caesar_decrypt_with_table
)
from ciphers.playfair import (
    encrypt as playfair_encrypt,
    decrypt as playfair_decrypt,
    encrypt_with_table as playfair_encrypt_with_table,
    decrypt_with_table as playfair_decrypt_with_table
)
from ciphers.vigenere import (
    encrypt as vigenere_encrypt,
    decrypt as vigenere_decrypt,
    vigenere_encrypt_with_table,
    vigenere_decrypt_with_table
)
from ciphers.railfence import encrypt as rail_encrypt, decrypt as rail_decrypt
from ciphers.affine import encrypt as affine_encrypt, decrypt as affine_decrypt
from ciphers.monoalpha import encrypt as mono_encrypt, decrypt as mono_decrypt

# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Classical Ciphers", layout="centered")
st.title("Classical Ciphers Tool")
st.write("Educational implementation of classical cryptography algorithms.")

cipher = st.sidebar.selectbox(
    "Select Cipher",
    [
        "Caesar Cipher",
        "Playfair Cipher",
        "Vigenere Cipher",
        "Rail Fence Cipher",
        "Affine Cipher",
        "Monoalphabetic Cipher"
    ]
)

mode = st.sidebar.radio("Mode", ["Encrypt", "Decrypt"])
key = st.sidebar.text_input("Key")
text = st.text_area("Enter Text")

# =========================
# RUN BUTTON
# =========================
if st.button("Run"):
    if not text:
        st.error("Text is required")
    elif cipher == "Vigenere Cipher" and not key.isalpha():
        st.error("Key must contain alphabets only")
    else:
        try:
            # =========================
            # CAESAR
            # =========================
            if cipher == "Caesar Cipher":
                if not key.isdigit():
                    st.error("Key must be a number")
                else:
                    shift = int(key)
                    if mode == "Encrypt":
                        df = caesar_encrypt_with_table(text, shift)
                        st.subheader("Caesar Encryption Dry Run")
                        st.dataframe(df, use_container_width=True)
                        result = "".join(df["Cipher Char"])
                    else:
                        df = caesar_decrypt_with_table(text, shift)
                        st.subheader("Caesar Decryption Dry Run")
                        st.dataframe(df, use_container_width=True)
                        result = "".join(df["Plain Char"])

            # =========================
            # PLAYFAIR
            # =========================
            elif cipher == "Playfair Cipher":
                matrix, df, result = (playfair_encrypt_with_table if mode=="Encrypt" 
                                      else playfair_decrypt_with_table)(text, key)
                st.subheader("5x5 Matrix")
                st.dataframe(matrix, use_container_width=True)
                st.subheader(f"Playfair {'Encryption' if mode=='Encrypt' else 'Decryption'} Dry Run")
                st.dataframe(df, use_container_width=True)

            # =========================
            # VIGENERE
            # =========================
            elif cipher == "Vigenere Cipher":
                if mode == "Encrypt":
                    df = vigenere_encrypt_with_table(text, key)
                    st.subheader("Vigenere Encryption Dry Run")
                    st.dataframe(df, use_container_width=True)
                    result = "".join(df["Cipher Text"])
                else:
                    df = vigenere_decrypt_with_table(text, key)
                    st.subheader("Vigenere Decryption Dry Run")
                    st.dataframe(df, use_container_width=True)
                    result = "".join(df["Plain Text"])

            # =========================
            # RAIL FENCE
            # =========================
            elif cipher == "Rail Fence Cipher":
                if not key.isdigit():
                    st.error("Key must be a number")
                else:
                    result = rail_encrypt(text, int(key)) if mode == "Encrypt" else rail_decrypt(text, int(key))

            # =========================
            # AFFINE
            # =========================
            elif cipher == "Affine Cipher":
                result = affine_encrypt(text, key) if mode == "Encrypt" else affine_decrypt(text, key)

            # =========================
            # MONOALPHABETIC
            # =========================
            elif cipher == "Monoalphabetic Cipher":
                result = mono_encrypt(text, key) if mode == "Encrypt" else mono_decrypt(text, key)

            st.subheader("Result")
            st.code(result)

        except Exception as e:
            st.error(f"Invalid input or key: {e}")
