from cipher import encrypt, decrypt

def main():
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    choice = input("Encrypt (E) or Decrypt (D)? ").upper()

    if choice == "E":
        print("Encrypted:", encrypt(text, shift))
    elif choice == "D":
        print("Decrypted:", decrypt(text, shift))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
