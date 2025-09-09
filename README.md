Caesar Cipher Tool (Python)

A simple command-line tool for encryption and decryption using the classical Caesar Cipher technique.  
This project demonstrates substitution-based cryptography, where each character is shifted by a fixed number of positions within the alphabet.  

--------------------------------------------------
Project Summary
--------------------------------------------------
- Encrypt or decrypt messages using Caesar Cipher.
- User provides input text and shift value.
- Supports both encryption and decryption via command-line interface.
- Clean, modular implementation using a separate cipher.py file.

--------------------------------------------------
Features
--------------------------------------------------
- Interactive text-based interface.
- Choice of Encrypt (E) or Decrypt (D).
- User-defined shift value.
- Demonstrates modular coding and cryptography basics.

--------------------------------------------------
Software Requirements
--------------------------------------------------
- Python 3.8 or higher  
- No external libraries required (pure Python implementation).

--------------------------------------------------
Step-by-Step Implementation
--------------------------------------------------
1. Create project folder
   mkdir caesar_cipher
   cd caesar_cipher

2. Create cipher.py
   Paste the following code:
   ----------------------------------
   def encrypt(text, shift):
       result = ""
       for char in text:
           if char.isalpha():
               base = ord('A') if char.isupper() else ord('a')
               result += chr((ord(char) - base + shift) % 26 + base)
           else:
               result += char
       return result

   def decrypt(text, shift):
       return encrypt(text, -shift)
   ----------------------------------

3. Create main.py
   Paste the following code:
   ----------------------------------
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
   ----------------------------------

4. Run the program
   python main.py
   - Enter your text
   - Provide a shift value (example: 3)
   - Choose Encrypt (E) or Decrypt (D)

--------------------------------------------------
Theory - Caesar Cipher
--------------------------------------------------
The Caesar Cipher is a substitution cipher used in classical cryptography.  
Each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.  

Encryption: Shift each character forward by n.  
Decryption: Shift each character backward by n.  

This cipher is historically significant and forms the basis for understanding more complex cryptographic techniques. While not secure against modern cryptanalysis, it is widely used in education to introduce core principles of encryption, substitution, and modular arithmetic.

--------------------------------------------------
File Structure
--------------------------------------------------
caesar_cipher/
    cipher.py        Encryption and decryption logic
    main.py          CLI interface

--------------------------------------------------
Possible Extensions
--------------------------------------------------
- Add support for non-English alphabets.
- Implement brute-force attack (try all possible shifts).
- Add file-based encryption and decryption.
- Build a GUI version using Tkinter or PyQt.

--------------------------------------------------
License
--------------------------------------------------
This project is released under the MIT License.

--------------------------------------------------
