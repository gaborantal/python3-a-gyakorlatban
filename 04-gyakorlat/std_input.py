#!/usr/bin/python

name = input('What is your name? ')
print("Hello "+name)

x=True
list_x = list()
while x:
    try:
        x = int(input())
    except ValueError:
        print('Invalid Number')
    list_x.append(x)
list_x.remove(list_x[len(list_x)-1])
print(list_x)
print("-----------------------")
result = input('operation: ')
print(eval(result))