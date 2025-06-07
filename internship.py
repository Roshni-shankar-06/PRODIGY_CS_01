def caesar_cipher_encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            # Shift within uppercase or lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please type 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
