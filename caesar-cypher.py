def caesar_bruteforce(cypher):
    results =[]

    cipher = cipher.upper()

    for shift in range (26):
        result = ""

        for c in cipher:
            if c.isalpha():
                result += chr((ord(c)-65-shift)%26+65)
            else:
                result += c
    
        results.append((shift, result))
    return results