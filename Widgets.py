from tkinter import *
from datetime import date

window = Tk()
window.title("Widgets")
window.geometry("500x500")

lbl = Label(text = "Hi!", fg = "white",bg = "blue", height = 1, width = 500)

name_ent = Entry()
name_lbl = Label(text = "Full name", bg = "white")

def display():
    name = name_ent.get()
    message = "Welcome! Todays date is:"
    greet = "hello"+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height = 3)
btn = Button(text = "begin", command = display, height =1, bg = "blue", fg = "White")

lbl.pack()
name_lbl.pack()
name_ent.pack()
btn.pack()
text_box.pack()
