import tkinter as tk
from tkinter import simpledialog
import threading
import time
import ui_config
from PIL import Image, ImageTk
import qrcode

def create_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

def update_qr_code(label):
    while True:
        global qr_data
        if qr_data:
            img = create_qr(qr_data)
            img = img.resize((300, 300), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk
        time.sleep(5)

def get_link():
    global qr_data
    qr_data = simpledialog.askstring("Entrada", "Digite o link para o QR Code:", parent=root)

def toggle_theme():
    global is_dark_theme
    is_dark_theme = not is_dark_theme
    update_theme()

def update_theme():
    if is_dark_theme:
        root.config(bg="#212121")
        label.config(bg="#212121", fg="#ffffff")
        insert_link_button.config(bg="#ffffff", fg="#212121")
        theme_button.config(bg="#ffffff", fg="#212121")
        theme_button.config(text="Tema claro")
    else:
        root.config(bg="#ffffff")
        label.config(bg="#ffffff", fg="#212121")
        insert_link_button.config(bg="#212121", fg="#ffffff")
        theme_button.config(bg="#212121", fg="#ffffff")
        theme_button.config(text="Tema escuro")

root = ui_config.create_ui()
label = ui_config.create_label(root)

insert_link_button = tk.Button(root, text="Inserir link", command=get_link)
insert_link_button.pack(pady=5)

theme_button = tk.Button(root, text="Tema escuro", command=toggle_theme)
theme_button.pack(pady=5)

qr_data = ""
is_dark_theme = False

thread = threading.Thread(target=update_qr_code, args=(label,))
thread.daemon = True
thread.start()

root.mainloop()
