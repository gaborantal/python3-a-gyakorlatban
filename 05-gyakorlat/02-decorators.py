#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Decorator tervezesi minta
# OOP tervezesi mintak koze tartozik
# Meglevo objektum funkcionalitasanak bovitese
# Emellett kozvetlenul nem befolyasolja a meglevo objektumot
# Annak tudta nelkul mukodik.


def first_decorator(func):
    def inner(x, y):
        print("< Before function call")
        func(x, y)
        print("< After function call")
    return inner


@first_decorator
def foo(x, y):
    print("The parameters were: ", x, y)


def foo2(x, y):
    print("The parameters were: ", x, y)

# Dekoralt funkcio meghivasa
foo("First run", 100)

# Dekoralas nelkuli funkcio meghivasa
method = foo2
method("Second run", 120)

# Kezzel alkalmazzuk a dekorator fuggvenyt
# Majd meghivjuk a dekoralt fuggvenyt
method = first_decorator(foo2)
method("Third run", 120)
