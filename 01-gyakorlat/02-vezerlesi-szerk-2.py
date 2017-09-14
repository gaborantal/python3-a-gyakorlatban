"""
01-gyak: Vezérlési szerkezetek: for + while
"""

# ********************* FOR ****************
print("\n")
# 1.
for x in range(5):
    print(x)
print("\n")

# 2.
for x in range(-2, 5):
    print(x)
print("\n")

# 3.
for x in range(-2, 5, 3):
    print(x)
print("\n")

# 4.
szin_lista = ['kek', 'zold', 'piros', 'feher']
for szin in szin_lista:
    print(szin)
print("\n")

# 5.
for letter in 'Python':
   print('Current Letter :' + letter)
print("\n")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        print(n, 'is a prime number')
print("\n")

# ********************* WHILE ****************

"""
A klasszikus -lásd: C/C++- do-while szerkezet nincs Python-ban
"""
count = 0
while (count < 9):
    print('The count is:' + str(count))
    count = count + 1

count = 0
while count < 5:
    print(str(count) + " is  less than 5")
    count = count + 1
else:
    print(str(count) + " is not less than 5")


"""
'Hamis' do-while szerkezet:

while True:
    stuff()
    if fail_condition:
        break

vagy

stuff()
while not fail_condition:
    stuff()
"""