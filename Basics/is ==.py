"""
'==' checks if variables have the same value
'is' checks if the variables point to the same object (in memory)
"""

a = [1, 2, 3]
b = a
print(b is a)   # True
print(b == a)   # True


b = a[:]        # A way to copy list by slicing all of it
print(b is a)   # False
print(b == a)   # True


'''
An interesting feature is that None is a class, but exists in a single instance inside a given interpreter.
So, if several variables are None, then it is one object, because all that variables are pointing on a single memory 
cell.
'''

a = None
b = None
print(a == b)  # True
print(a is b)  # True

'''The same goes for True and False'''

a = True
b = True
print(a == b)  # True
print(a is b)  # True

a = False
b = False
print(a == b)  # True
print(a is b)  # True

'''All these, because the object is the same in memory. Take a look:'''
print(id(a))
print(id(b))
print(id(a) == id(b))
