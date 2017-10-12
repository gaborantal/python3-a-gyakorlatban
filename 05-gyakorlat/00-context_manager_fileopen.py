#!/usr/bin/env python
# -*- coding: utf-8 -*-


def open_a_file_bad():
    fp = open('szoveg.txt', 'w')
    fp.write('Ez egy peldamondat. '*6)  # egymas utan hatszor beleirjuk a
                                        # fajlba a mondatunkat.
    # Ajjaj elfelejtettunk valamit!
    # fp.close()


def open_a_file_good():
    with open('szoveg.txt', 'w') as fp:
        fp.write('Ez egy peldamondat.\n'*50)
    # Ajjaj, nem felejtettunk el valamit?
    # Szerencsere nem, mert a context manager elvegzi helyettunk a bezarast.

if __name__ == '__main__':
    open_a_file_bad()
    open_a_file_good()
