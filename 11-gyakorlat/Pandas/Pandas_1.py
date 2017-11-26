#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

str = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', '1234','SteveSmith'])
#print(str.str.upper())
"""
tovabbi opciok:
   lower, upper, len, strip, split, cat, get_dummies, contains, replace, repeat, count, startswith,
   endswith, find, findall, swapcase, islower, isupper, isnumeric,
"""

#Series: one-dimensional labeled array
s1 = pd.Series(['a','b','c','d'])
#print(s1)

s2 = pd.Series(['a','b','c','d'],index=[100,101,102,103])
#print(s2)

data2 = {'a' : 0., 'b' : 1., 'c' : 2.}
s3 = pd.Series(data2)
#print(s3)

s4 = pd.Series(data2,index=['b','c','d','a'])
"""print(s4)
print(s4[:3])
print(s4['a'])
print(s4.axes)
print(s4.empty)
print(s4.size)
print(s4.values)
print(s4.head(2)) # v.o: print(s[:2])
print(s4.tail(2)) # v.o: print(s[-2:])"""


#Data: two-dimensional data structure
data3 = [1,2,3,4,5]
df1 = pd.DataFrame(data3)
#print(df1)

data4 = [['Alex',10],['Bob',12],['Clarke',13]]
df2 = pd.DataFrame(data4,columns=['Name','Age'])
#print(df2)

data5 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],
         'Age':[28,34,29,42]}
df3 = pd.DataFrame(data5)
#print(df3)


data6 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],
         'Age':[28,34,29,42]}
df4 = pd.DataFrame(data6, index=['rank1','rank2','rank3','rank4'])
#print(df4)

data6 = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
         'Age':pd.Series([25,26,25,23,30,29,23]),
         'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df5 = pd.DataFrame(data6)
"""print(df5.axes)
print(df5.shape)
print(df5.values)
print(df5.T)"""
