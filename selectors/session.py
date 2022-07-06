from tkinter import *
from tkcalendar import Calendar

# creating an object of tkinter

tkobj = Tk()

# setting up the geomentry

tkobj.geometry("400x400")
tkobj.title("Session picker")


choices = ['session1','session2','session3','session4','session5','session6','session7','session8','session9','session10']
variable = StringVar(tkobj)
variable.set('Session Select')

w = OptionMenu(tkobj, variable, *choices)
w.pack(pady=20)
#starting the object
tkobj.mainloop()