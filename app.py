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




# import streamlit as st
# import pandas as pd

# from ciphers.caesar import (
#     encrypt as caesar_encrypt,
#     decrypt as caesar_decrypt,
#     encrypt_with_table as caesar_encrypt_with_table,
#     decrypt_with_table as caesar_decrypt_with_table
# )
# from ciphers.playfair import (
#     encrypt as playfair_encrypt,
#     decrypt as playfair_decrypt,
#     encrypt_with_table as playfair_encrypt_with_table,
#     decrypt_with_table as playfair_decrypt_with_table
# )
# from ciphers.vigenere import (
#     encrypt as vigenere_encrypt,
#     decrypt as vigenere_decrypt,
#     vigenere_encrypt_with_table,
#     vigenere_decrypt_with_table
# )
# from ciphers.railfence import encrypt as rail_encrypt, decrypt as rail_decrypt
# from ciphers.affine import encrypt as affine_encrypt, decrypt as affine_decrypt
# from ciphers.monoalpha import encrypt as mono_encrypt, decrypt as mono_decrypt

# # =========================
# # STREAMLIT UI
# # =========================
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

# # =========================
# # RUN BUTTON
# # =========================
# if st.button("Run"):
#     if not text:
#         st.error("Text is required")
#     elif cipher == "Vigenere Cipher" and not key.isalpha():
#         st.error("Key must contain alphabets only")
#     else:
#         try:
#             # =========================
#             # CAESAR
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
#                 matrix, df, result = (playfair_encrypt_with_table if mode=="Encrypt" 
#                                       else playfair_decrypt_with_table)(text, key)
#                 st.subheader("5x5 Matrix")
#                 st.dataframe(matrix, use_container_width=True)
#                 st.subheader(f"Playfair {'Encryption' if mode=='Encrypt' else 'Decryption'} Dry Run")
#                 st.dataframe(df, use_container_width=True)

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

#         except Exception as e:
#             st.error(f"Invalid input or key: {e}")


















import streamlit as st
import pandas as pd

from ciphers.caesar import (
    encrypt_with_table as caesar_encrypt_with_table,
    decrypt_with_table as caesar_decrypt_with_table
)

from ciphers.playfair import (
    encrypt_with_table as playfair_encrypt_with_table,
    decrypt_with_table as playfair_decrypt_with_table
)

from ciphers.vigenere import (
    vigenere_encrypt_with_table,
    vigenere_decrypt_with_table
)

from ciphers.railfence import (
    encrypt_with_table as rail_encrypt_with_table,
    decrypt_with_table as rail_decrypt_with_table
)

from ciphers.affine import encrypt as affine_encrypt, decrypt as affine_decrypt
from ciphers.monoalpha import encrypt as mono_encrypt, decrypt as mono_decrypt
from ciphers.vernam import encrypt as vernam_encrypt, decrypt as vernam_decrypt
from ciphers.stream import encrypt as stream_encrypt, decrypt as stream_decrypt
from ciphers.blockcipher import encrypt as block_encrypt, decrypt as block_decrypt
from ciphers.columnar import encrypt as columnar_encrypt, decrypt as columnar_decrypt
from ciphers.permutation import encrypt as permutation_encrypt, decrypt as permutation_decrypt


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Classical Ciphers", layout="centered")
st.title("Classical Ciphers Tool")
st.write("Educational implementation of cryptography algorithms.")


cipher = st.sidebar.selectbox(
    "Select Cipher",
    [
        "Caesar Cipher",
        "Playfair Cipher",
        "Vigenere Cipher",
        "Rail Fence Cipher",
        "Affine Cipher",
        "Monoalphabetic Cipher",
        "Vernam Cipher",
        "Stream Cipher",
        "Block Cipher",
        "Columnar Cipher",
        "Permutation Cipher"
    ]
)

mode = st.sidebar.radio("Mode", ["Encrypt", "Decrypt"])
key = st.sidebar.text_input("Key")
text = st.text_area("Enter Text")


# =========================
# KEY HINTS
# =========================
if cipher == "Caesar Cipher":
    st.sidebar.info("Key: Number (shift value), e.g., 3")

elif cipher == "Playfair Cipher":
    st.sidebar.info("Key: Any word or phrase (letters only, J is replaced with I)")

elif cipher == "Vigenere Cipher":
    st.sidebar.info("Key: Letters only, repeated to match text length")

elif cipher == "Rail Fence Cipher":
    st.sidebar.info("Key: Number of rails, e.g., 3")

elif cipher == "Affine Cipher":
    st.sidebar.info("Key format: a,b (e.g., 5,8) | 'a' must be coprime with 26")

elif cipher == "Monoalphabetic Cipher":
    st.sidebar.info("Key: 26 unique letters (e.g., QWERTYUIOPASDFGHJKLZXCVBNM)")

elif cipher == "Vernam Cipher":
    st.sidebar.info("Key: Same length as text (letters only, spaces ignored)")

elif cipher == "Stream Cipher":
    st.sidebar.info("Key: Letters only, key repeats automatically")

elif cipher == "Block Cipher":
    st.sidebar.info("Key: Letters only, block size = key length")

elif cipher == "Columnar Cipher":
    st.sidebar.info("Key: Letters only, defines column order")

elif cipher == "Permutation Cipher":
    st.sidebar.info("Key: Comma-separated indices, e.g., 3,0,2,1")


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
            # CAESAR
            if cipher == "Caesar Cipher":
                if not key.isdigit():
                    st.error("Key must be a number")
                else:
                    shift = int(key)
                    df = caesar_encrypt_with_table(text, shift) if mode == "Encrypt" else caesar_decrypt_with_table(text, shift)
                    st.dataframe(df, use_container_width=True)
                    result = "".join(df["Cipher Char"] if mode == "Encrypt" else df["Plain Char"])

            # PLAYFAIR
            elif cipher == "Playfair Cipher":
                matrix, df, result = playfair_encrypt_with_table(text, key) if mode == "Encrypt" else playfair_decrypt_with_table(text, key)
                st.subheader("5x5 Matrix")
                st.dataframe(matrix, use_container_width=True)
                st.dataframe(df, use_container_width=True)

            # VIGENERE
            elif cipher == "Vigenere Cipher":
                df = vigenere_encrypt_with_table(text, key) if mode == "Encrypt" else vigenere_decrypt_with_table(text, key)
                st.dataframe(df, use_container_width=True)
                result = "".join(df["Cipher Text"] if mode == "Encrypt" else df["Plain Text"])

            # RAIL FENCE
            elif cipher == "Rail Fence Cipher":
                if not key.isdigit():
                    st.error("Key must be a number")
                else:
                    df, result = rail_encrypt_with_table(text, int(key)) if mode == "Encrypt" else rail_decrypt_with_table(text, int(key))
                    st.dataframe(df, use_container_width=True)

            # AFFINE
            elif cipher == "Affine Cipher":
                df, result = affine_encrypt(text, key) if mode == "Encrypt" else affine_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            # MONOALPHABETIC
            elif cipher == "Monoalphabetic Cipher":
                df, result = mono_encrypt(text, key) if mode == "Encrypt" else mono_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            # VERNAM
            elif cipher == "Vernam Cipher":
                df, result = vernam_encrypt(text, key) if mode == "Encrypt" else vernam_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            # STREAM
            elif cipher == "Stream Cipher":
                df, result = stream_encrypt(text, key) if mode == "Encrypt" else stream_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            # BLOCK
            elif cipher == "Block Cipher":
                df, result = block_encrypt(text, key) if mode == "Encrypt" else block_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            # COLUMNAR
            elif cipher == "Columnar Cipher":
                df, result = columnar_encrypt(text, key) if mode == "Encrypt" else columnar_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            # PERMUTATION
            elif cipher == "Permutation Cipher":
                df, result = permutation_encrypt(text, key) if mode == "Encrypt" else permutation_decrypt(text, key)
                st.dataframe(df, use_container_width=True)

            st.subheader("Result")
            st.code(result)

        except Exception as e:
            st.error(f"Invalid input or key: {e}")


# =========================
# FOOTER
# =========================
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    padding: 8px 0;
    font-size: 14px;
    color: white;
    border-top: 1px solid #555;
    background: #555;
    z-index: 999;
}
.footer img {
    width: 16px;
    vertical-align: middle;
}
</style>

<div class="footer">
    Made with ❤️ by
    <a href="https://github.com/Ahmed-Raza-90/" target="_blank" style="color:#000; text-decoration:none;">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
        Ahmed Raza
    </a>
</div>
""", unsafe_allow_html=True)



