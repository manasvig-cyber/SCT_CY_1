# main.py - Modified to offer both interfaces
from cipher import encrypt, decrypt
import sys

def cli_interface():
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    choice = input("Encrypt (E) or Decrypt (D)? ").upper()

    if choice == "E":
        print("Encrypted:", encrypt(text, shift))
    elif choice == "D":
        print("Decrypted:", decrypt(text, shift))
    else:
        print("Invalid choice!")

def gui_interface():
    try:
        import tkinter as tk
        from enhanced_cipher import CyberCipherApp
        root = tk.Tk()
        app = CyberCipherApp(root)
        root.mainloop()
    except ImportError:
        print("GUI requires tkinter. Using CLI interface instead.")
        cli_interface()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        gui_interface()
    else:
        # Check if we're likely in a graphical environment
        try:
            # Try to import GUI components to see if they're available
            import tkinter
            response = input("GUI available. Use graphical interface? (Y/n): ").upper()
            if response != 'N':
                gui_interface()
            else:
                cli_interface()
        except ImportError:
            cli_interface()