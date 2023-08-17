"""An immutable ordered data type. Like a list, only immutable."""

my_tuple = tuple()

'''To make a tuple of 1 element, you need to use a comma, otherwise the result will be a string'''

my_tuple1 = ('some_thing',)
print(type(my_tuple1))  # tuple

my_tuple1 = ('some_thing')
print(type(my_tuple1))  # str
