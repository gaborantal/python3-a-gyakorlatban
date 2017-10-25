#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        print('> setUp before a test')

    def tearDown(self):
        print('> tearDown after a test')

    def test_valid(self):
        self.assertTrue(utils.is_url('http://google.com'))

    def test_invalid(self):
        self._test_invalid_url('google')
        self._test_invalid_url(42)
        self._test_exc()

    def _test_invalid_url(self, url):
        self.assertFalse(utils.is_url(url))

    def _test_exc(self):
        with self.assertRaises(RuntimeError):
            self.assertFalse(utils.is_url('google', 12))

if __name__ == '__main__':
    unittest.main()
