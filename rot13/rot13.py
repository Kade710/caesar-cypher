def rot13(text):
    result = ""

    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + 13) % 26 + base)
        else:
            result += c

    return result
