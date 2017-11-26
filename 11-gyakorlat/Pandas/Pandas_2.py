#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

d1 = { 'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
       'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df1 = pd.DataFrame(d1)
df1['three']=pd.Series([10,20,30],index=['a','b','c'])
#print(df1)

df1['four']=df1['one']+df1['three']
#print(df1)


d2 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
      'three' : pd.Series([10,20,30], index=['a','b','c'])}

df2 = pd.DataFrame(d2)
#print (df2)
del df2['one']
#print (df2)
df2.pop('two')
df2['two'] = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
#print (df2)

#print(df2.loc['d'])
#print(df2.iloc[2])

df = df1.append(df2)
#print(df)
