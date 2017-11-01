#!/usr/bin/env python
# -*- coding: utf-8 -*-


# https://docs.python.org/3/library/typing.html
def say_hello(name: str) -> str:
    print('Hello', name)


def main():
    say_hello('Nagy Zsolt')
    say_hello(32)

if __name__ == '__main__':
    main()