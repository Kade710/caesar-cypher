==========================
#Caesar-Encrypt
==========================

def caesar_encrypt(text, shift):
    result = ""

    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c

    return result

==========================
#Caesar-Decrypt
==========================

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

==========================
#Caesar-Brute-Force
==========================

def caesar_bruteforce(cipher):
    results = []

    cipher = cypher.upper()

    for shift in range (26):
        result = ""

        for c in cypher:
            if c.isalpha():
                base = ord('A')
                result += chr((ord(c) - base - shift) % 26 + base)
            else:
                result += c

        results.append((shift, result))

    return results