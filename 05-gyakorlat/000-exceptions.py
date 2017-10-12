#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RantottaException(Exception):
    def __init__(self, hany_tojas):
        super(RantottaException, self).__init__()
        self.hany_tojas = hany_tojas

def rantotta_keszit(tojas):
    if tojas < 1:
        raise RantottaException(tojas)
    else:
        print('Nyami, kesz a rantotta %d tojasbol' % tojas)

def problems(a, b=0):
    if isinstance(a, int) and isinstance(b, int):
        return a/b
    else:
        raise Exception(a)


def main():
    print(problems(8, 2))
    # print(problems(10))
    # print(problems('Nagy baj van!'))

    try:
        problems(10)
    except ZeroDivisionError as zde:
        print('Nullaval nem osztunk, ejnye!')
        # raise  # Exception('Nullaval osztottunk!')
    except Exception as exc:
        print('Exception details:', exc)
    finally:
        print('Vege a veszelyes resznek! Huh!')

    tojasok = input('Hany tojasbol sutnel rantottat?')
    try:
        rantotta_keszit(int(tojasok))
    except RantottaException as re:
        print('%d tojasbol nem lehet rantottat sutni!' % re.hany_tojas)

if __name__ == '__main__':
    main()
