# Kísértetház
from random import randint
print('Kisértetház')
bátor_vagyok = True
pontszám = 0
while bátor_vagyok:
    szellem_ajtó = randint(1, 3)
    print('Három ajtó van előtted')
    print('Az egyik mögött szellem van.')
    print('Melyiket nyitod ki?')
    ajtó = input('1, 2 vagy 3?')
    ajtó_szám = int(ajtó)
    if ajtó_szám == szellem_ajtó:
        print('SZELLEM')
        bátor_vagyok = False
    else:
        print('Nincs szellem!')
        print('Lépj be a következő szobába!')
        pontszám = pontszám + 1
print('Menekülj!')
print('Vége a játéknak! Az elért pontszám:', pontszám)