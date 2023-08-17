"""A set is a mutable unordered data type. A set always contains only unique elements.
With it, you can remove duplicates in the list"""

lis = [1, 1, 1, 2, 3, 4, 5]
st = set(lis)
print(st)   # {1, 2, 3, 4, 5}


# Ways to create a set

my_set_1 = set()  # empty
my_set_2 = set('long string, that will be reduced to unique literals')
my_set_3 = set(lis)


# Operations with sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)     # {1, 2, 3, 4, 5, 6, 7, 8}

set4 = set1 | set2  # same as union, but with '|'
print(set4)     # {1, 2, 3, 4, 5, 6, 7, 8}
# generally, it all works like you would expect

# Helpful methods

# Метод add() добавляет элемент во множество:

set4.add('string')
print(set4)     # {1, 2, 3, 4, 5, 6, 7, 8, 'string'}

# The discard() allows to remove elements without raising an error if the element is not in the set:
set4.discard('string')  # {1, 2, 3, 4, 5, 6, 7, 8, 'string'} -> {1, 2, 3, 4, 5, 6, 7, 8}
set4.discard('element_that_is_not_in_this_set')  # {1, 2, 3, 4, 5, 6, 7, 8} -> {1, 2, 3, 4, 5, 6, 7, 8}
print(set4)     # {1, 2, 3, 4, 5, 6, 7, 8}
