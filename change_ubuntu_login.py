#!/usr/bin/python3
# Author: Ramiz Muharemovic
# https://github.com/muharemovic
import os
import sys
import pip
import tkinter as tk
from tkinter import filedialog, messagebox
try:
    from PIL import Image, ImageTk

except:
    if not 'Pillow' in sys.modules.keys():
        pip.main(['install', 'Pillow'])
        messagebox.showinfo("info", "***Pillow installing, REOPEN APP***")

def apply_button():
    os.system("x-terminal-emulator -e glib-compile-schemas /usr/share/glib-2.0/schemas")
    a = messagebox.showinfo("info", "Please restart your Pc !")

def gui():
    root = tk.Tk()
    filename = tk.filedialog.askopenfilename(initialdir=os.path.expanduser('~/Pictures/'), title="Select file",
                                             filetypes=[("Image", "*.jpg"),("Image", "*.png")])
    with open('/usr/share/glib-2.0/schemas/10_unity_greeter_background.gschema.override', 'w') as f:
        f.write('[com.canonical.unity-greeter]\n'
                'draw-user-backgrounds=false\n'
                "background = '{}'".format(filename))
        f.close

    my_image = Image.open(filename)
    my_image = my_image.resize((300, 300))
    im = ImageTk.PhotoImage(my_image)
    panel = tk.Label(image=im)
    panel.pack()
    button = tk.Button(text="Apply", font=("Ubuntu", 12),command = apply_button  )
    button.pack()
    root.resizable(False, False)
    root.geometry("350x350")
    root.title("Login Screen Change")
    root.mainloop()
try:
    gui()
except NameError:
    print(" ")