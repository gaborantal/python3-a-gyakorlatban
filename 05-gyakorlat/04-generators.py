#!/usr/bin/env python
# -*- coding: utf-8 -*-


# generators are used to generate a series of values
# yield is like the return of generator functions
# The only other thing yield does is save the "state" of a generator function
# A generator is just a special type of iterator
# Like iterators, we can get the next value from a generator using next()
# for gets values by calling next() implicitly
# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def kiskutyak():
    for i in range(101):
        yield i+1
    yield 'Elfogytunk.. :('


def main():
    kiskutyak_generator = kiskutyak()
    for kiskutya in kiskutyak_generator:
        print(str(kiskutya) + '. kiskutya')

    # ajjaj
    print('next', next(kiskutyak_generator))

if __name__ == '__main__':
    main()
