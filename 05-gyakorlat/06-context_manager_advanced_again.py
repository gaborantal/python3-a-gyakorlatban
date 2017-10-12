#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager, ContextDecorator
import time


class timed(ContextDecorator):
    def __init__(self, method_name):
        self.start = None
        self.end = None
        self.method_name = method_name

    def __enter__(self):
        self.start = time.time()
        print("Starting at {}".format(self.start))
        return self

    def __exit__(self, type, value, traceback):
        self.end = time.time()
        total = self.end - self.start
        print("Method '{}' ended at {} (total: {})".format(self.method_name,
                                                           self.end, total))


def main():
    with timed('for-range+sleep'):
        for i in range(100000):
            i = i*6
        time.sleep(2)
    complex_compute()


@timed('complex_compute')
def complex_compute():
    time.sleep(1)


if __name__ == '__main__':
    main()
