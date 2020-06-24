from tkinter import *
ablak = Tk()
def Agomb():
    print('Köszönöm!')
def Bgomb():
    print('Jaj! ez fájt!')
ablak = Tk()
gomb_A = Button(ablak, text='Nyomj meg!', command=Agomb)
gomb_B = Button(ablak, text='Ne nyomj meg!', comman=Bgomb)
gomb_A.pack()
gomb_B.pack()
ablak.mainloop()

