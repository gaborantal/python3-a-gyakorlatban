"""
01-gyak: Vezérlési szerkezetek: if - else
"""

# ********************* IF ****************
x = 20

# 1.
if x < 10:
    print("x < 10")
print("\n")

# 2.
if x < 10:
    print("x < 10")
else:
    print("x >= 10")
print("\n")

# 3.
if x < 10:
    print("x < 10")
elif x < 20:
    print("10 <= x < 20")
elif x == 20:
    print("x == 20")
else:
    print("x > 20")
print("\n")

# 4.
if x < 10:
    print("x < 10")
elif x >= 10 and x < 20:
    print("10 <= x < 20")
elif x < 10 or x >= 20:
    print("Other")