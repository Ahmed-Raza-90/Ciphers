# vigenere_dryrun.py

# -------------------------------
# VIGENERE CIPHER WITH DRY RUN
# -------------------------------

def generate_key(text, key):
    key = key.lower()
    result = ""
    j = 0
    for c in text:
        if c.isalpha():
            result += key[j % len(key)]
            j += 1
        else:
            result += c
    return result

def encrypt(text, key, dry_run=False):
    if not key.isalpha():
        raise ValueError("Key must only contain letters")
    
    key = generate_key(text, key)
    result = ""
    
    if dry_run:
        print("\n--- Encryption Dry Run ---")
        print(f"{'Text':<10}{'Key':<10}{'Shift':<10}{'Result':<10}")
    
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i]) - ord('a')
            base = ord('A') if text[i].isupper() else ord('a')
            encrypted_char = chr((ord(text[i]) - base + shift) % 26 + base)
            result += encrypted_char
            if dry_run:
                print(f"{text[i]:<10}{key[i]:<10}{shift:<10}{encrypted_char:<10}")
        else:
            result += text[i]
            if dry_run:
                print(f"{text[i]:<10}{'-':<10}{'-':<10}{text[i]:<10}")
    return result

def decrypt(text, key, dry_run=False):
    if not key.isalpha():
        raise ValueError("Key must only contain letters")
    
    key = generate_key(text, key)
    result = ""
    
    if dry_run:
        print("\n--- Decryption Dry Run ---")
        print(f"{'Text':<10}{'Key':<10}{'Shift':<10}{'Result':<10}")
    
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i]) - ord('a')
            base = ord('A') if text[i].isupper() else ord('a')
            decrypted_char = chr((ord(text[i]) - base - shift) % 26 + base)
            result += decrypted_char
            if dry_run:
                print(f"{text[i]:<10}{key[i]:<10}{shift:<10}{decrypted_char:<10}")
        else:
            result += text[i]
            if dry_run:
                print(f"{text[i]:<10}{'-':<10}{'-':<10}{text[i]:<10}")
    return result

# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    while True:
        print("\n--- Vigenere Cipher Project ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter text: ")
            key = input("Enter key (letters only): ")
            dry = input("Do you want dry run? (y/n): ").lower() == 'y'
            encrypted = encrypt(text, key, dry_run=dry)
            print("\nFinal Encrypted Text:", encrypted)
        elif choice == "2":
            text = input("Enter text: ")
            key = input("Enter key (letters only): ")
            dry = input("Do you want dry run? (y/n): ").lower() == 'y'
            decrypted = decrypt(text, key, dry_run=dry)
            print("\nFinal Decrypted Text:", decrypted)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
