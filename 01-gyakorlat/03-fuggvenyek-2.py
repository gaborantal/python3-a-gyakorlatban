#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
01-gyak: Függvények: fgv neve, mint parameter + beagyazott fgv
"""

def osszead(a, b):
    return a+b

def kivon(a, b):
    return a-b

def negyzet(a, _):
    return a*a

def muvelet(muvelet_neve, par_1, par_2=None):
    eredmeny = muvelet_neve(par_1, par_2)
    print(eredmeny)

muvelet(negyzet, 2)
muvelet(kivon, 10, 3)

# *******************************

def szamologep(muveleti_jel, a, b):
    def _osszead():
        return a+b
    def _kivon():
        return a-b

    if muveleti_jel == "+":
        print( _osszead() )
    elif muveleti_jel == "-":
        print( _kivon())

szamologep("+", 10, 12)