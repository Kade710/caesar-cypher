from caesar.py import caesar_encrypt, caesar_decrypt
from rot13.py import rot13

def main():
    while True:
        print("\n=== Wise Crack ===")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt")
        print("3. Caesar Brute Force")
        print("4. ROT13")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Text: ")
            shift = int(input("Shift: "))
            print(caesar_encrypt(text, shift))

        elif choice == "2":
            text = input("Text: ")
            shift = int(input("Shift: "))
            print(caesar_decrypt(text, shift))

        elif choice == "3":
            text = input("Cyphertext: ")
            results = brute_force(text, shift)

            for shift, text in results:
                print(f"{shift}: {text}")

        elif choice == "4":
            text = input("Text: ")
            print(rot13(text))

        elif choice == "5":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()