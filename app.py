import streamlit as st

from ciphers.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from ciphers.playfair import encrypt as playfair_encrypt, decrypt as playfair_decrypt
from ciphers.vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt
from ciphers.railfence import encrypt as rail_encrypt, decrypt as rail_decrypt
from ciphers.affine import encrypt as affine_encrypt, decrypt as affine_decrypt
from ciphers.monoalpha import encrypt as mono_encrypt, decrypt as mono_decrypt

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

if st.button("Run"):
    if not text:
        st.error("Text is required")
    else:
        try:
            if cipher == "Caesar Cipher":
                if not key.isdigit():
                    st.error("Key must be a number")
                else:
                    result = caesar_encrypt(text, int(key)) if mode == "Encrypt" else caesar_decrypt(text, int(key))

            elif cipher == "Playfair Cipher":
                result = playfair_encrypt(text, key) if mode == "Encrypt" else playfair_decrypt(text, key)

            elif cipher == "Vigenere Cipher":
                result = vigenere_encrypt(text, key) if mode == "Encrypt" else vigenere_decrypt(text, key)

            elif cipher == "Rail Fence Cipher":
                if not key.isdigit():
                    st.error("Key must be a number")
                else:
                    result = rail_encrypt(text, int(key)) if mode == "Encrypt" else rail_decrypt(text, int(key))

            elif cipher == "Affine Cipher":
                result = affine_encrypt(text, key) if mode == "Encrypt" else affine_decrypt(text, key)

            elif cipher == "Monoalphabetic Cipher":
                result = mono_encrypt(text, key) if mode == "Encrypt" else mono_decrypt(text, key)

            st.success("Result")
            st.code(result)

        except Exception:
            st.error("Invalid input or key")
