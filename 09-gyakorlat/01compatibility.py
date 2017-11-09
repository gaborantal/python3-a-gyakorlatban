#!/usr/bin/env python
# -*- coding: utf-8 -*-
import six


# Python2 vs Python3:
#  - http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#the-__future__-module
#  - https://docs.python.org/3.0/whatsnew/3.0.html
# Bovebben: https://pythonhosted.org/six/
def main():
    if six.PY2:
        print('Running on Python 2')
    elif six.PY34:
        print('Running on Python 3.4')
    elif six.PY3:
        print('Running on Python 3')

    print('An example: dicts')
    useless = {
        'use': 'less',
        'meaningoflife': 42
    }

    if six.PY2:
        for i in useless.iterkeys():
            print('a key in dict:', i)
    if six.PY3:
        for i in useless.keys():
            print('a key in dict:', i)

    # We can use six
    print('Using six')
    for i in six.iterkeys(useless):
        print('a key in dict:', i)

    print('3 / 2 =', 3 / 2)
    print('3 // 2 =', 3 // 2)
    print('3 / 2.0 =', 3 / 2.0)
    print('3 // 2.0 =', 3 // 2.0)

if __name__ == '__main__':
    main()
