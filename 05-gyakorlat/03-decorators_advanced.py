#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps


def debug(func):
    """Debug decorator

    Segitsegevel lehet debug infokat kiirni a hivott metodusokrol

    :param func: a metodus amit szeretnenk dekoralni
    """
    def decorated(*args, **kwargs):
        print("Called method", func.__name__)
        return func(*args, **kwargs)
    return decorated


def return_multiplier(*nums):
    def _outer_wrapper(wrapped_function):
        # @wraps(wrapped_function)
        def _wrapper(*args, **kwargs):

            result = wrapped_function(*args, **kwargs)

            for num in nums:
                result = result * num

            return result
        return _wrapper
    return _outer_wrapper


@debug
@return_multiplier(2, 3)
def func4():
    return 'Na'

print(func4())
