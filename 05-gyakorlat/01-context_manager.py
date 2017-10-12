#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://buildingskills.itmaybeahack.com/book/python-2.6/html/p03/p03c07_contexts.html
# https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers
# https://docs.python.org/3/library/contextlib.html
# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
# destruktor?! :'(
class File(object):

    def __init__(self, filename, mode):
        print('File context manager: __init__')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('File context manager: __enter__')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, exception_type, exception_value, traceback):
        print('File context manager: __exit__')
        self.open_file.close()


class WrongContextManager(object):
    def __init__(self, *args):
        print('Wrong context manager: __init__')

    def __enter__(self):
        print('Wrong context manager: __enter__')

if __name__ == '__main__':
    with File('foo.txt', 'w') as infile:
        infile.write('foo')

    # with WrongContextManager('Won\'t work') as wont_work:
    #     print(wont_work)
