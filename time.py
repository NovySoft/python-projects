import sys
import time 
from tkinter import *

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text = current_time) 
    clock.after(200, times)

window = Tk()
window.title("Óra")
window.geometry("380x300")
clock = Label(window, font = ("times", 50, "bold"), bg = "orange")
clock.grid(column = 2, row = 2, padx = 100, pady = 25)
times()
lbl1 = Label(window,text = "Óra",font = "times 25 bold", bg = "blue")
lbl1.grid(column = 2, row = 0)

lbl2 = Label(window,text = "Óra      Perc    Másodperc",font = "times 15 bold", bg = "red")
lbl2.grid(column = 2, row = 3)

window.mainloop()
