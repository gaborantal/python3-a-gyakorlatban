#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.integrate as integrate
import scipy.special as special
import numpy as np

#  integrate a bessel function jv(2.5, x) along the interval [0, 4.5]
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
print(result)


# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
from scipy.integrate import dblquad
def I(n):
    return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)
print(I(4))

area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)
print(area)