#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ember():
    def __init__(self, nev, eletkor, szul_hely="Kecskemet"):
        self.nev = nev
        self.eletkor = eletkor
        self.szul_hely = szul_hely

ember = Ember("Kovacs Geza", 54, "Szeged")

print(dir(ember))
print(ember.__class__)
print(ember.__getattribute__("nev"))
print(getattr(ember, "nev"))
print("------------------------------------")
print(getattr(ember, "eletkor"))
setattr(ember, "eletkor", 30)
print(getattr(ember, "eletkor"))
print("------------------------------------")
ember.__init__("Toth Gabor", 20)
print(ember.nev, ember.szul_hely)
