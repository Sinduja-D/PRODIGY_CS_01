def caesar_cipher(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + key) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    msg = input("Enter your message: ")
    key = int(input("Enter the shift value: "))

    # Encrypting the message
    e_msg = caesar_cipher(msg, key)
    print(f"The Encrypted text is: {e_msg}")

    # Decrypting the message
    key = int(input("Enter the decryption shift value: "))
    d_msg = caesar_cipher(e_msg, -key)
    print(f"The Decrypted message is: {d_msg}")

if __name__ == "__main__":
    main()
