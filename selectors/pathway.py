from tkinter import *
from tkcalendar import Calendar

# creating an object of tkinter

tkobj = Tk()

# setting up the geomentry

tkobj.geometry("400x400")
tkobj.title("Pathway picker")


choices = ['Pathway 1', 'Pathway 2']
variable = StringVar(tkobj)
variable.set('Pathway select')

w = OptionMenu(tkobj, variable, *choices)
w.pack(pady=20)
#starting the object
tkobj.mainloop()