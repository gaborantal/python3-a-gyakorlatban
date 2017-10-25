#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_url(string, allowed=None):
    """
    Check if a string is a valid url.
    :param string: String to check.
    :param allowed: List of valid schemes ('http', 'https', 'ftp'...). Default to None (http is valid).
    :return: True if url, false otherwise
    :rtype: bool
    """
    if not isinstance(string, str):
        return False
    if not allowed:
        return string.startswith("http://")
    else:
        if not isinstance(allowed, list):
            raise RuntimeError('Allowed protocols is not a list')
        for allowed_start in allowed:
            if string.startswith('%s://' % allowed_start):
                return True
        return False


if __name__ == '__main__':
    print(is_url('http://google.com'))  # True
    print(is_url('http://google'))  # True
    print(is_url('ftp://google.com'))  # False
    print(is_url('ftp://google.com', ['http', 'ftp', 'https']))  # True
