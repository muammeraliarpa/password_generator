import random
import string
import tkinter as tk
from tkinter import ttk
import pyperclip

# Şifre oluşturmak için bir fonksiyon
def generate_password(length, use_letters, use_digits, use_punctuation):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    # Belirtilen uzunlukta rastgele bir şifre oluştur
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# "Şifre Oluştur" düğmesine tıklandığında çağrılacak fonksiyon
def generate_button_clicked():
    try:
        # Kullanıcının girdiği şifre uzunluğunu al
        length = int(length_entry.get())
        # Uzunluk negatif veya sıfıra eşitse hata mesajı göster ve işlemi sonlandır
        if length <= 0:
            result_label.config(text="Geçersiz uzunluk! Pozitif bir sayı girin.")
            return
        # Kullanıcının hangi karakter türlerini kullanmak istediğini al
        use_letters = letters_var.get()
        use_digits = digits_var.get()
        use_punctuation = punctuation_var.get()
        # Şifre oluştur ve sonucu ekrana yazdır
        password = generate_password(length, use_letters, use_digits, use_punctuation)
        result_label.config(text="Oluşturulan Şifre: " + password)
        # Oluşturulan şifreyi panoya kopyala
        pyperclip.copy(password)
    except ValueError:
        # Hata durumunda kullanıcıya uyarı ver
        result_label.config(text="Geçersiz giriş! Lütfen bir sayı girin.")

# Tkinter arayüzünü oluşturma
root = tk.Tk()
root.title("Şifre Oluşturucu")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

length_label = ttk.Label(mainframe, text="Şifre Uzunluğu:")
length_label.grid(column=0, row=0, sticky=tk.W)

length_entry = ttk.Entry(mainframe)
length_entry.grid(column=1, row=0)

letters_var = tk.BooleanVar()
letters_var.set(True)
letters_check = ttk.Checkbutton(mainframe, text="Harf", variable=letters_var)
letters_check.grid(column=0, row=1, sticky=tk.W)

digits_var = tk.BooleanVar()
digits_var.set(True)
digits_check = ttk.Checkbutton(mainframe, text="Rakam", variable=digits_var)
digits_check.grid(column=1, row=1, sticky=tk.W)

punctuation_var = tk.BooleanVar()
punctuation_var.set(True)
punctuation_check = ttk.Checkbutton(mainframe, text="Özel Karakter", variable=punctuation_var)
punctuation_check.grid(column=0, row=2, sticky=tk.W)

generate_button = ttk.Button(mainframe, text="Şifre Oluştur", command=generate_button_clicked)
generate_button.grid(column=0, row=3, columnspan=2)

result_label = ttk.Label(mainframe, text="")
result_label.grid(column=0, row=4, columnspan=2)

root.mainloop()
