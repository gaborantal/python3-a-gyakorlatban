#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import nose


def div(x, y):
    return x/y


class TestDiv(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(div(10, 2), 5)

    def test_0(self):
        with self.assertRaises(ZeroDivisionError):
            div(3, 0)

if __name__ == '__main__':
    nose.main()
