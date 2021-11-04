'''
map(func, iterable, ...)


def func(el1, el2):
    return '%s|%s' % (el1, el2)

list(map(func, [1, 2], [3, 4, 5]))   =>  ['1|3', '2|4']

'''

def func(el1, el2):
    return '%s|%s' % (el1, el2)

print(list(map(func, [1, 2], [3, 4, 5])))


'''map возвращает итератор, так что его можно перебирать'''
a = map(func, [1, 2], [3, 4, 5])
print(next(a))
print(next(a))
