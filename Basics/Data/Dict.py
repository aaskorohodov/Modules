"""
Dictionaries are a mutable and ordered data type, but the key must be an object of an immutable type:
- number
- string,
- tuple
The value can be any type of data.
"""


empty_dict = {}

not_empty_dict = {'a': 1, 'b': 2}

dict_created_with_a_build_in_function = dict(short='dict', long='dictionary')
dict_from_list_of_tuples = dict([(1, 1), (2, 4)])
dict_created_with_these_fancy_method = dict.fromkeys(['a', 'b'])
dict_created_with_that_fancy_method = dict.fromkeys(['a', 'b'], 100)  # All values will be 100, for each of 2 keys

d = {a: a ** 2 for a in range(7)}  # Creating with the help of generator
print(d)

# Helpful methods

'''copy() allows you to create a copy of the dictionary, while a normal assignment (dict1 = dict2) will only create a 
new reference, changing one object will change the other'''

a = d.copy()

'''get() returns a value from the dictionary by key, and if there is no value, it returns None, while the usual call
by type a[some_key] will raise an error if there is no such key. Also get can return something else if asked.'''

print(a.get('555', 'Ooops'))

'''The setdefault() method looks for a key, and if it doesn't exist, it creates a key with a value of None instead of 
raising an error. If the key exists, setdefault will return the value that matches it.'''

a.setdefault('555')
print(a)

'''We can set the default value, in case this key does not exists'''
a.setdefault('444', 'asd')
print(a)

'''keys, values, items do just what you expect. Note, if you write their result to a variable, change the dictionary and
call that variable again, the value in it will change:'''

keys = a.keys()
print(keys)
a['another_key'] = 'another_value'
print(keys)
