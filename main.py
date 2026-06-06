from caesar import caesar_encrypt, caesar_decrypt, caesar_bruteforce
from rot13 import rot13


def main():
    while True:
        print("\n=== Wise Crack ===")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt")
        print("3. Caesar Brute Force")
        print("4. ROT13")
        print("5. Exit")

        choice = input("Choose: ")

        # Caesar Encrypt
        if choice == "1":
            text = input("Text: ")
            shift = int(input("Shift: "))
            print(caesar_encrypt(text, shift))

        # Caesar Decrypt
        elif choice == "2":
            cipher = input("Ciphertext: ")
            shift = int(input("Shift: "))
            print(caesar_decrypt(cipher, shift))

        # Caesar Brute Force
        elif choice == "3":
            cipher = input("Ciphertext: ")

            results = caesar_bruteforce(cipher)

            for shift, result in results:
                print(f"Shift {shift}: {result}")

        # ROT13
        elif choice == "4":
            text = input("Text: ")
            print(rot13(text))

        # Exit
        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()