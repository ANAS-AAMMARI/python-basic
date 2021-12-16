from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Hello")
string = "Hello Mr ANAS AAMMARI"
Label.config(text=string)
label = Label(root, font=("ds-digital", 40), background="orange", foreground= "black")
label.pack(anchor="center")
mainloop()
