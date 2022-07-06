import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkmacosx import Button

root = tk.Tk()
root.title("VAS Downloading Tool  version 0.1")
canvas = tk.Canvas(root,width = 600, height = 300)
canvas.grid(columnspan=3, rowspan=3)

#logo


logo = Image.open('vas.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)
photo = tk.PhotoImage(file = 'vas_icon.png')
root.wm_iconphoto(False, photo)
#instructions
instructions = tk.Label(root, text="Step 1: Generate the congifuration file for downloading Alexa data", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

#browse button
browse_text = tk.StringVar()
browse_btn = Button(root, textvariable=browse_text, font="Raleway", bg="#2CDA13", fg="white",width = 200)
browse_text.set("Enter Timestamp")
browse_btn.grid(column=1, row=3)




canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)



root.mainloop()