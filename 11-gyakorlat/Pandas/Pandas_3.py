#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
            'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
            'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df1 = pd.DataFrame(ipl_data)

g1 = df1.groupby('Team').groups
#print(g1)
g2 = df1.groupby(['Team','Year']).groups
#print(g2)

grouped = df1.groupby('Year')

"""
for name,group in grouped:
	print(name)
	print(group)
	print("\n")
"""
get_group = grouped.get_group(2014)
#print(get_group)


d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
     'Age':pd.Series([25,26,25,23,30,29,23]),
     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df2 = pd.DataFrame(d)
"""
for key,value in df2.iteritems():
	print(key,value)
print("\n")

for row_index,row in df2.iterrows():
	print(row)
print("\n")

for row in df2.itertuples():
	print(row)
print("\n")
"""

left = pd.DataFrame({'id':[1,2,3,4,5],
                     'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
                     'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({'id':[1,2,3,4,5],
                      'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
                      'subject_id':['sub2','sub4','sub3','sub6','sub5']})
"""
print(pd.merge(left,right,on='id'))
print("\n")
print(pd.merge(left,right,on=['id','subject_id']))
print("\n")
print(pd.concat([left,right]))
"""


df = pd.DataFrame({'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','David','Gasper','Betina','Andres']),
                   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
                   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])})
print(df.sum())
print("\n")
print(df.sum()['Age'])
print("\n")
print(df.sum(1))
print("\n")
print(df.max()['Age'])
# tovabbi opciok: count, sum, mean, median, mode, std, min, max, abs, prod, cumsum, cumprod
