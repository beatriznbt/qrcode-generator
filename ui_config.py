import tkinter as tk

def create_ui():
    root = tk.Tk()
    root.title("QR Code Dinâmico")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")
    return root

def create_label(root):
    label = tk.Label(root, bg="#ffffff")
    label.pack(pady=20)
    return label

bold_font = ("Montserrat", 12, "bold")

def create_button(root, callback):
    button = tk.Button(root, text="Inserir link", command=callback, bg="#007bff", fg="#ffffff", font=bold_font)
    button.pack(pady=10)
    return button
