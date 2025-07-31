alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(text):
    enc_result = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            enc_result += alphabet[(alphabet.index(text[i]) + shift) % len(alphabet)]
        else:
            enc_result += text[i]
    print("\n🔐 Encrypted message:")
    print(enc_result)


def decryption(encrypted_texted):
    decr_result = ""
    for i in range(len(encrypted_texted)):
        if encrypted_texted[i] in alphabet:
            decr_result += alphabet[(alphabet.index(encrypted_texted[i]) - shift) % len(alphabet)]
        else:
            decr_result += encrypted_texted[i]
    print("\n🔓 Decrypted message:")
    print(decr_result)


def main():
    print("=" * 40)
    print("🔤 Caesar Cipher CLI Tool")
    print("=" * 40)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ").lower()
    text = input("Type your message:\n> ").lower()
    global shift
    shift = int(input("Type the shift number:\n> "))

    print("\nProcessing...\n")

    if direction == 'encode':
        encryption(text)
    elif direction == 'decode':
        decryption(text)
    else:
        print("⚠️  Enter a valid instruction (encode/decode)!")


if __name__ == "__main__":
    main()
