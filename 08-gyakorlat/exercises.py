#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce


# A feladat a reduce alkalmazasaval egy maximalus elemkivalasztast megirni
def max_elem_reduce(input_list):
    return None


def test(s, a, b):
    if a == b:
        print(s, 'OK')
    else:
        print('%s != %s' % (a, b))


def main():
    test('max_elem_reduce', max_elem_reduce([1,2,9,3,5,2,1,100]), 100)

if __name__ == '__main__':
    main()
