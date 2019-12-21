from tkinter import *
from random import randint 
def dob():
    szöveg.delete(0.0, END)
    szöveg.insert(END, str(randint(1,9)))
ablak = Tk()
szöveg = Text(ablak, width=1, height=1)
gomb_A = Button(ablak, text='Nyomd meg!', command=dob)
szöveg.pack()
gomb_A.pack()
ablak.mainloop()