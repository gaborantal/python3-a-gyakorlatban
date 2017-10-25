#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mock
import random
import unittest


def coin_flip():
    return 'fej' if random.random() > 0.5 else 'iras'


def game(choice):
    coin = coin_flip()
    if coin == choice:
        return "won"
    else:
        return "lost"


def welcome(obj):
    print('~~~~~WELCOME~~~~~')
    obj.hello()
    print('~~~~~Have a great time!~~~~~')


class TestGame(unittest.TestCase):

    @mock.patch('random.random', return_value=0.8)
    def test_play_win(self, mock_random):
        returned_value = game('fej')
        self.assertEqual(returned_value, 'won')

    @mock.patch('random.random')
    def test_play_lose(self, mock_random):
        mock_random.return_value = 0.1
        returned_value = game('fej')
        self.assertEqual(returned_value, 'lost')

    def test_welcome(self):
        useless = mock.MagicMock()
        with mock.patch('sys.stdout') as stdout_mock:
            welcome(useless)
        useless.hello.assert_called()

if __name__ == '__main__':
    unittest.main()
