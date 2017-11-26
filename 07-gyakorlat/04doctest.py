#!/usr/bin/env python
# -*- coding: utf-8 -*-

def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x


def concat(*args):
    """Return the square of x.

    >>> concat('sajt ', 'torta')
    'sajttorta'
    >>> concat(-2, 'a', 'b', 40.5, 'kiscica')
    '-2ab40.5kiscica'
    """
    s = ""
    for i in args:
        s += str(i).strip()

    return s

if __name__ == '__main__':
    import doctest
    doctest.testmod()
