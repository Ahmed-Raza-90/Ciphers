# 🔐 Ciphers Tool (Streamlit Cryptography Simulator)

This project is a Python-based Streamlit application that demonstrates multiple classical cryptography algorithms with full encryption and decryption support and step-by-step calculation tables.  
The purpose of this project is learning, not real-world security.

---

## 🎯 Project Objective

Most students learn cryptography by memorizing formulas without understanding what actually happens behind the scenes. This project focuses on visualizing the complete encryption and decryption process so users can clearly see how plaintext, keys, and mathematical operations produce ciphertext.

This tool is designed for:
- Cryptography and Information Security students
- University lab work and demonstrations
- Anyone who wants to understand classical ciphers properly

---

## 🧠 Implemented Ciphers

### Substitution Ciphers
- Caesar Cipher
- Monoalphabetic Cipher
- Affine Cipher

### Polyalphabetic Ciphers
- Vigenere Cipher
- Vernam Cipher
- Stream Cipher

### Transposition Ciphers
- Rail Fence Cipher
- Columnar Transposition Cipher
- Permutation Cipher
- Block Cipher

### Matrix-Based Cipher
- Hill Cipher (2x2 and 3x3 matrices)

### Digraph Cipher
- Playfair Cipher

Each cipher supports both encryption and decryption, along with step-by-step tables wherever logical.

---

## 🖥️ User Interface

- Built using Streamlit
- Sidebar-based cipher and mode selection
- Dynamic key input fields depending on selected cipher
- Step-by-step calculation tables displayed using Pandas
- Clear error messages for invalid keys or inputs

The interface is kept simple and focused on learning, not visuals.

---

## 📁 Project Structure

Ciphers/
│
├── app.py
├── README.md
├── requirements.txt
│
└── ciphers/
├── caesar.py
├── playfair.py
├── vigenere.py
├── railfence.py
├── affine.py
├── monoalpha.py
├── vernam.py
├── stream.py
├── blockcipher.py
├── columnar.py
├── permutation.py
└── hill.py


Each cipher is implemented in a separate module to keep the code clean and easy to understand.

---

## ⚙️ Installation

### Requirements
- Python 3.9 or higher
- pip package manager

### Install dependencies

pip install -r requirements.txt

Libraries used:
- streamlit
- pandas

---

## ▶️ Run the Application

From the project root directory, run:

python streamlit run app.py

The application will open automatically in your default web browser.

## 🧪 How to Use

1. Select a cipher from the sidebar
2. Choose Encrypt or Decrypt mode
3. Enter the input text
4. Enter the required key
5. Click the Run button

The application will display:
- A detailed calculation table
- The final encrypted or decrypted result

If the input or key is invalid, execution stops with an error message.

## 🔑 Key Formats

### Caesar Cipher
Only number like 3

### Playfair Cipher
Keyword
Letters only. J is automatically replaced with I.

### Vigenere / Stream / Block / Columnar
Key

### Rail Fence Cipher
Dept like 2,3

### Affine Cipher
a,b eg => 5,8
The value of `a` must be coprime with 26.

### Monoalphabetic Cipher
"QWERTYUIOPASDFGHJKLZXCVBNM"
Must contain exactly 26 unique letters.

### Vernam Cipher
KEY MATCHING TEXT
Key length must match the plaintext length (excluding spaces).

### Permutation Cipher
2,0,1

### Hill Cipher

- Matrix size: 2x2 or 3x3
- Values between 0 and 25
- Determinant must be invertible mod 26

Example (2x2 matrix):
3 3
2 5

## 🧮 Hill Cipher Details

- Plaintext is cleaned and padded with X if required
- Displays numeric vectors and matrix multiplication
- Shows intermediate and final results clearly
- Invalid key matrices are rejected immediately

This strict validation ensures correct cryptographic behavior.

## 📸 Screenshots

Create a folder named `screenshots` in the project root and add the following images:


---

## ⚠️ Disclaimer

This project is strictly for educational use.  
All implemented ciphers are cryptographically weak and should never be used for real-world data protection.


## 👤 Author

Ahmed Raza  
GitHub: https://github.com/Ahmed-Raza-90/

## 🚀 Future Improvements

- Frequency analysis tools
- Cipher attack demonstrations
- Modern cipher demonstrations (AES for learning only)
- Export step-by-step tables as CSV files

