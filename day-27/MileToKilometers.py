import tkinter
from tkinter import *


def convert():
    mil = float(mil_input.get())
    kilometer = round(1.609344 * mil)
    kilometers.config(text=kilometer)


window = Tk()

window.title("Mile to Kilometers Converter")
window.minsize(width=150, height=150)

# Button
button = Button(text="Convert", command=convert)
button.grid(column=1, row=3)

# input
mil_input = Entry(width=5)
mil_input.grid(column=1, row=0)

# kilometers
miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles = Label(text="is equal to")
miles.grid(column=0, row=1)
miles = Label(text="Km")
miles.grid(column=1, row=2)
kilometers = Label(text=0)
kilometers.grid(column=1, row=1)

window.mainloop()
