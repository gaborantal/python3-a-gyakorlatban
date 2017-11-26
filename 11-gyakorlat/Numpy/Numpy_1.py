#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

a1 = np.array([1, 2, 32, 14, 13, 23]) 
"""print(a1)
print(a1[2])
print(a1[3:])
print(a1[2:5])"""

a1 = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
"""print(a1)
print(a1[...,1] )
print(a1[1,...] )
print(a1[...,1:])"""


a2 = np.array([1, 2, 3, 4, 5], ndmin = 2) 
#print(a2)

a3 = np.array([[1, 2], [3, 4], [10,20]])
#print(a3)
#print(a3.shape)
a3.shape=(2,3)
#print(a3)

a4 = np.arange(12)
#print(a4)
a4 = np.arange(10,20,2)
#print(a4)
a4 = np.linspace(10,20,5) 

a5 = np.ones([2,2], dtype = int) 
#print(a5)

a6 = np.zeros([4,2], dtype = int) 
#print(a6)




a7 = np.arange(0,60,5)
a8 = a7.reshape(3,4)
   
#print(a8)
b = a8.T
#print(b )

"""
for x in np.nditer(b):
   print(x)


for x in np.nditer(a8, op_flags=['readwrite']):
   x[...]=2*x
print(a8)
"""