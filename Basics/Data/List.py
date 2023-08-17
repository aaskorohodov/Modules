"""
Mutable and ordered data type
"""

lis = [1, 2, 3, 4, 5, 6]

'''Since the list is ordered, we can change its elements, like a dictionary:'''

lis[1] = 100

# Useful methods

lis = ['1', '2', '3']

a = '+'.join(lis)  # Combines into a single string, using '+' as delimiter
print(a)

lis.append('4')  # Appends elements at the end of the list

lis1 = [1, 2, 3, 4, 5]
lis2 = [10, 20, 30, 40, 50]

lis3 = lis2 + lis1

lis1.extend(lis2)  # Extends one list with the second. Unlike simple '+', the first list is changed

print(lis1.pop(-1))  # Deletes some element and returns it

lis_string = ['string1', 'string2']
lis_string.remove('string1')  # Removes element, without returning it. Note, that it requires the element, not index
print(lis_string)

print(lis1.index(30))  # Return an index, or raises an error

lis1.insert(0, 'first element')  # Inserts an element into requested position

# Inserting an element into the end:
lis1.insert(len(lis1), 'last element')
print(lis1)     # [..., 'last_element']
