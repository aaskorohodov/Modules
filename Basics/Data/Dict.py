d = {}  # создание пустого словаря

d = {'a':1, 'b':2}  # не пустого словаря

d = dict(short='dict', long='dictionary')  # с помощью функции dict
d = dict([(1, 1), (2, 4)])
d = dict.fromkeys(['a', 'b'])  # с помощью метода fromkeys (в значениях будет None)
d = dict.fromkeys(['a', 'b'], 100)  # в значениях будет 100 для всех ключей

d = {a: a ** 2 for a in range(7)}  # с помощью генератора
print(d)