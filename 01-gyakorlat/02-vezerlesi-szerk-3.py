"""
01-gyak: Vezérlési szerkezetek: break, continue
"""

for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :' + letter)

print("\n")

for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter :' + letter)

print("\n")

for letter in 'Python':
    if letter == 'h':
        pass
        #print('This is pass block')
    print('Current Letter :' + letter)