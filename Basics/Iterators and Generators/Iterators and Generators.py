"""
Generator - implements yield
An iterator is an object that supports the next() function to move to the next element in the collection.
An iterable is an object that allows you to iterate over its elements and can be converted to an iterator.

Iterators and generators only keep 1 object in memory, retrieving the next one as needed. Consequently,
you can create lists that would not fit into memory otherwise

a = list(range(1000000000000)) - will not fit into memory and will cause an error.
a = (x for x in range(1000000000000)) - will fit into memory and will work in cycles.

Generators differ from iterators in the way they are created (in parentheses):

mygenerator = (x*x for x in range(3))
mylist = [x*x for x in range(3)]
"""

lst = (x for x in range(1000000000))
x = range(110)

for i in x:
    '''Iterating over this iterable'''
    print(i, end=" ")
    if i > 100:
        break


for i in lst:
    '''I we try to continue, this iterator will keep going from the place where it stopped.'''
    print(i, end=" ")
    if i > 100:
        break

'''
Functions such as sum(), max(), min() work in generators, but such as lst[0], len() don't
'''