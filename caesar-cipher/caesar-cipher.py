cipher = input("Ciphertext: ").upper()

for shift in range (26):
    result = ""
    for c in cipher:
        if c.isalpha():
            result += chr((ord(c)-65-shift)%26+65)
        else:
            result += c
    print(f"Shift {shift}: {result}")