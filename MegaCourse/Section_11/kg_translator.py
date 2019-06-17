from tkinter import *

window = Tk()

def translate():
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    grams = float(entered_kgs.get())*1000
    pounds = float(entered_kgs.get())*2.20462
    ounces = float(entered_kgs.get())*35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


lb1 = Label(window, text="Kg")
lb1.grid(row=0, column=0)

entered_kgs = StringVar()
e1 = Entry(window, textvariable=entered_kgs)
e1.grid(row=0, column=1)

b1 = Button(window, text="Translate", command=translate)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=15)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=15)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=15)
t3.grid(row=1, column=2)

window.mainloop()
