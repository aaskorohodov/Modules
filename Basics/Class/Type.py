"""
Type if a top-object, that creates other classes
"""

print(type(int))  # <class 'type'>
print(int.__mro__)  # (<class 'int'>, <class 'object'>)

'''Standard classes are inherited from object but are created by type, which is also a class'''

print(type(type))

'''type can create classes, which is inconvenient, but possible:

     type(<class name>, <tuple of parent classes>, <dictionary with attributes and their values>)

class name - it is what it is
tuple of parent classes - from where we will inherit the new class
a dictionary with attributes and their values - both attributes and methods can be passed here.
Methods can be written in advance and give a link to them here, or write as a lambda
'''

A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})  # А = ссылка на класс

asd = A()
print(asd.MAX_COORD)