"""
map(func, iterable, ...)


def func(el1, el2):
    return '%s|%s' % (el1, el2)

list(map(func, [1, 2], [3, 4, 5]))   =>  ['1|3', '2|4']
"""
from typing import Iterable


def func(el1, el2):
    """Makes a string from 2 provided elements"""

    return '%s|%s' % (el1, el2)


'''What is happening here:

1. Map takes your function and argument(s) for this function. Arguments are expected to be iterables
2. Map turns into iterator, which on every iteration will feed one argument into that function
3. Map is used inside list(), which asks map to do its thing (feed 1 argument into its function), till there is no more
    arguments
*Note, that there is 2 lists, provided as arguments, and map does understand, that one list is bigger then the other,
    so it stops, when the shorter list is over, without raising an error.'''
print(list(map(func, [1, 2], [3, 4, 5])))


# Map returns an iterator, so it can be iterated over
a = map(func, [1, 2], [3, 4, 5])
print(next(a))
print(next(a))

'''The profit is that when you using map as an iterator (like the last example with "next"), the iterator only stores
one last used value, instead of saving all values inside memory. This makes memory usage not so big, when huge values 
need to be evaluated.'''


def func2(val):
    return str(val)


my_iterator = map(func2, range(100_000_000_000_000))  # At this point, map does NOT store this big list
'''If instead we would use this:
    my_iterator = map(func2, list(range(100_000_000_000_000)))

or even if we try to make this:
    list(range(100_000_000_000_000))
    
The error would be raised, because this is to huge for memory to store.'''


def iterator_user(iterator: Iterable[any]):
    """Makes iterations over provided iterable"""

    for item in iterator:
        print(f'Now only 1 value is stored in a memory. This value is {item}.')
        if item == '10':
            print('Now, we made what we wanted, and we can quit this cycle, without even using any of the next values.')
            break


iterator_user(my_iterator)
