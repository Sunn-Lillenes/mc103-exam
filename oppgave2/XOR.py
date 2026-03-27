#!/usr/bin/env python3


def xor_cipher(text, key):
    """XOR each character in 'text' with the integer 'key'."""
    output = []
    for ch in text:
        xored_code = ord(ch) ^ key
        output.append(chr(xored_code))
    return "".join(output)


def main():
    ciphertext = "Wkf#rvj`h#aqltm#el{#ivnsp#lufq#wkf#obyz#gld#bmg#ab`h-"

    # Brute force
    print("Brute force XOR keys 1-127:")
    common = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
    for key in range(1, 128):
        result = xor_cipher(ciphertext, key)
        score = sum(result.lower().count(word) for word in common)
        if score >= 2:
            print(f"  Key={key}: {result}")

    # Decrypt with found key.
    key = 3
    plaintext = xor_cipher(ciphertext, key)
    print("Ciphertext:", ciphertext)
    print("Key:", key)
    print("\nDecrypted plaintext:")
    print(plaintext)

    # Re-encrypt to verify.
    encrypted_again = xor_cipher(plaintext, key)
    print("\nEncrypting the plaintext again with the same key:")
    print(encrypted_again)
    print("\nShould match the original ciphertext:", encrypted_again == ciphertext)


if __name__ == "__main__":
    main()
