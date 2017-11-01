#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def main():
    print(fib(50))

if __name__ == '__main__':
    main()
