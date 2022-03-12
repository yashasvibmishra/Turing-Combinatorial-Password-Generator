import random
import pyperclip
import string
from tkinter import *
from PIL import Image, ImageTk

def popmsg(final):
    popup = Tk()
    popup.config(bg='turquoise')
    popup.geometry('400x300')
    text = Text(popup,height=2, width=30)
    text.pack()
    text.insert(END,final)
    popup.mainloop()
def generate():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    ssymbols = ['!','@','%','^','&','*']
    password_length = slider.get()
    bucket = []
    final = []

    if lower_selected.get():
        for letter in lower:
            bucket.append(letter)

    if upper_selected.get():
        for letter in upper:
            bucket.append(letter)

    if numbers_selected.get():
        for number in numbers:
            bucket.append(number)

    if ssymbols_selected.get():
        for symbol in ssymbols:
            bucket.append(symbol)

    for i in range(password_length):
        final.append(random.choice(bucket))

    final = ''.join(final)
    pyperclip.copy(final)
    popmsg(''.join(final))
    print(''.join(final))  
root = Tk()
root.config(bg='turquoise')
root.geometry("300x300")
load= Image.open(r"C:\Users\KIIT\Desktop\main password generator\turing.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=100, y=100)


lower_selected = IntVar()
upper_selected = IntVar()
numbers_selected = IntVar()
ssymbols_selected = IntVar()

cb_lower = Checkbutton(root, text = "Lowercase", variable=lower_selected)
cb_upper = Checkbutton(root, text = "Uppercase", variable=upper_selected)
cb_numbers = Checkbutton(root, text = "Numbers", variable=numbers_selected)
cb_ssymbols = Checkbutton(root, text = "Special Symbols", variable=ssymbols_selected)

slider = Scale(root, from_=0, to=36, orient=HORIZONTAL)
btn_generatepw = Button(root,text="Create Pass",command=generate)

cb_lower.pack()
cb_upper.pack()
cb_numbers.pack()
cb_ssymbols.pack()
slider.pack()
btn_generatepw.pack()
# ---------------
# now we can directly paste this password into the password field of a website of choice
# ----------
mainloop()

