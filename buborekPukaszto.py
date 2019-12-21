from tkinter import *
from time import sleep, time
from random import randint
from math import sqrt
MAGASSÁG = 500
SZÉLESSÉG = 800
ablak = Tk()
ablak.title('Buborékpukkasztó')
v = Canvas(ablak, width=SZÉLESSÉG, height=MAGASSÁG, bg='darkblue')
v.pack()
hajó_1 = v.create_polygon(7, 2, 7, 28, 30, 15, fill='red')
hajó_2 = v.create_oval(0, 0, 30, 30, outline='red')
HAJÓ_R = 15
KP_X = SZÉLESSÉG / 2
KP_Y = MAGASSÁG / 2
v.move(hajó_1, KP_X, KP_Y)
v.move(hajó_2, KP_X, KP_Y)
HAJÓ_SEB = 10
def hajót_mozgat(event):
    if event.keysym == 'Up':
        v.move(hajó_1, 0, -HAJÓ_SEB)
        v.move(hajó_2, 0, -HAJÓ_SEB)
    elif event.keysym == 'Down':
        v.move(hajó_1, 0, HAJÓ_SEB)
        v.move(hajó_2, 0, HAJÓ_SEB)
    elif event.keysym == 'Left':
        v.move(hajó_1, -HAJÓ_SEB, 0)
        v.move(hajó_2, -HAJÓ_SEB, 0)
    elif event. keysym == 'Right':
        v.move(hajó_1, HAJÓ_SEB, 0)
        v.move(hajó_2, HAJÓ_SEB, 0)
v.bind_all('<Key>', hajót_mozgat)
bub_id = list()
bub_r = list()
bub_seb = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SEB = 10
DIFF = 100
def buborékot_gyárt():
    x = SZÉLESSÉG + DIFF
    y = randint(0, MAGASSÁG)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = v.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_seb.append(randint(1, MAX_BUB_SEB))
def buborékot_mozgat():
    for i in range(len(bub_id)):
      v.move(bub_id[i], -bub_seb[i], 0)
def koord_kér(azonosító):
    poz = v.coords(azonosító)
    x = (poz[0] + poz[2])/2
    y = (poz[1] + poz[3])/2
    return x, y 
def bub_töröl(i):
    del bub_r[i]
    del bub_seb[i]
    v.delete(bub_id[i])
    del bub_id[i]
def bub_takarít():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = koord_kér(bub_id[i])
        if x < -DIFF:
             bub_töröl(i)
def távolság(id1, id2):
    x1, y1 = koord_kér(id1)
    x2, y2 = koord_kér(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
def ütközés():
    pontok = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if távolság(hajó_2, bub_id[bub]) < (HAJÓ_R + bub_r[bub]):
            pontok += (bub_r[bub] + bub_seb[bub])
            bub_töröl(bub)
    return pontok
v.create_text(50, 30, text='IDŐ', fill='white' )
v.create_text(150, 30, text='PONTSZÁM', fill='white' )
időszöveg = v.create_text(50, 50, fill='white' )
pontszöveg = v.create_text(150, 50, fill='white' )
def pontot_mutat(pontszám):
    v.itemconfig(pontszöveg, text=str(pontszám))
def időt_mutat(maradék_idő):
    v.itemconfig(időszöveg, text=str(maradék_idő))
BUB_VSZ = 10
IDŐLIMIT = 30
BÓNUSZPONT = 1000
pontszám = 0
bónusz = 0
vége = time() + IDŐLIMIT
BUB_VSZ = 10
pontszám = 0
 #FŐCIKLUS

while time() < vége:
    if randint(1, BUB_VSZ) == 1:
        buborékot_gyárt()
    buborékot_mozgat()
    bub_takarít()
    pontszám += ütközés()
    if (int(pontszám / BÓNUSZPONT)) > bónusz:
        bónusz += 1
        vége += IDŐLIMIT
    pontot_mutat(pontszám)
    időt_mutat(int(vége - time()))
    ablak.update()
    sleep(0.01)
v.create_text(KP_X, KP_Y, \
    text='GAME OVER', fill='white', font=('Helvetica',30))
v.create_text(KP_X, KP_Y + 30, \
    text='PONTSZÁM: '+ str(pontszám), fill='white')

