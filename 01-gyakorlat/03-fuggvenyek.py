#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
01-gyak: Függvények
"""
from math import cos
from math import pi

# ************* beépített függvények és modulok *************
nn = input('Írjon be valamilyen egész számot : ')
print(type(nn))
print(str(nn) + ' négyzete ' + str(int(nn)**2))

# from math import *
cos_x = cos(45)
print(cos_x)

sugar = 5
print("A kör területe: " + str(sugar**2 * pi))

szoveg = "Hello Mindenki"
print("A szöveg hossza: " + str(len(szoveg)))


# ************* sajat függvények *************
def kor_kerulete(sugar):
    print('A kör kerülete: 2 * r * PI')
    return 2 * sugar * pi


print(kor_kerulete(5))
print('\n')



# default ertek
def ember_adatai(nev, nem, eletkor=None):
    if eletkor:
        print(nev, nem, eletkor)
    else:
        print(nev, nem)

ember_adatai('John', 'ff', 20)
ember_adatai('Eva', 'n')
