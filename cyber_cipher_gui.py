# cyber_cipher_gui.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from cipher import encrypt, decrypt

class CyberCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberVault - Caesar Cipher")
        self.root.geometry("700x500")
        self.root.configure(bg="#0a0a1a")
        
        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#0a0a1a')
        self.style.configure('TLabel', background='#0a0a1a', foreground='#00ffcc', font=('Consolas', 10))
        self.style.configure('TButton', background='#003366', foreground='#00ffcc', font=('Consolas', 10))
        self.style.configure('TEntry', fieldbackground='#001a33', foreground='#00ffcc')
        self.style.configure('TScale', background='#0a0a1a', troughcolor='#001a33')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = tk.Label(main_frame, text="CYBERVAULT CAESAR CIPHER", 
                              font=("Courier New", 16, "bold"), 
                              fg="#00ffcc", bg="#0a0a1a")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Input section
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(input_frame, text="TEXT TO PROCESS:", font=("Consolas", 11, "bold")).grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.text_input = scrolledtext.ScrolledText(input_frame, width=50, height=6, 
                                                   bg="#001a33", fg="#00ffcc", 
                                                   insertbackground="#00ffcc",
                                                   font=("Consolas", 10))
        self.text_input.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        # Shift control
        shift_frame = ttk.Frame(main_frame)
        shift_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Label(shift_frame, text="SHIFT VALUE (0-25):", font=("Consolas", 11, "bold")).grid(row=0, column=0, sticky=tk.W)
        
        self.shift_var = tk.IntVar(value=3)
        shift_scale = ttk.Scale(shift_frame, from_=0, to=25, variable=self.shift_var)
        shift_scale.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        self.shift_label = ttk.Label(shift_frame, text="3", font=("Consolas", 12, "bold"))
        self.shift_label.grid(row=1, column=1, padx=(10, 0))
        
        # Update label when scale changes
        def update_shift_label(value):
            self.shift_label.config(text=str(int(float(value))))
        shift_scale.configure(command=update_shift_label)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(0, 15))
        
        encrypt_btn = ttk.Button(button_frame, text="ENCRYPT", command=self.encrypt_text)
        encrypt_btn.grid(row=0, column=0, padx=(0, 10))
        
        decrypt_btn = ttk.Button(button_frame, text="DECRYPT", command=self.decrypt_text)
        decrypt_btn.grid(row=0, column=1, padx=(0, 10))
        
        clear_btn = ttk.Button(button_frame, text="CLEAR", command=self.clear_text)
        clear_btn.grid(row=0, column=2, padx=(0, 10))
        
        # Output section
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(output_frame, text="RESULT:", font=("Consolas", 11, "bold")).grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.text_output = scrolledtext.ScrolledText(output_frame, width=50, height=6, 
                                                    bg="#001a33", fg="#00ffcc", 
                                                    state="disabled",
                                                    font=("Consolas", 10))
        self.text_output.grid(row=1, column=0, columnspan=2)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        shift_frame.columnconfigure(0, weight=1)
        
    def encrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to encrypt")
            return
            
        shift = self.shift_var.get()
        encrypted = encrypt(text, shift)
        
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert("1.0", encrypted)
        self.text_output.config(state="disabled")
        
    def decrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to decrypt")
            return
            
        shift = self.shift_var.get()
        decrypted = decrypt(text, shift)
        
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert("1.0", decrypted)
        self.text_output.config(state="disabled")
        
    def clear_text(self):
        self.text_input.delete("1.0", tk.END)
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberCipherApp(root)
    root.mainloop()