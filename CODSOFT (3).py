import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Invalid length. Please enter a positive integer.")
            return

        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Entry for password length
label_length = tk.Label(root, text="Enter password length:")
label_length.grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Button to generate and display password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
