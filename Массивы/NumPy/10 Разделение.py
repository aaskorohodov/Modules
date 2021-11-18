import numpy as np


a = np.arange(10)  # вектор
b, c = np.hsplit(a, 2)  # делим на 2 массива, указываем что делить и на сколько. Делить нужно, чтобы делилось
print(b.shape, c.shape)

# превращаем массив в вертикальный вектор, чтобы поделить его вертикально
a.shape = 10, -1
b, c = np.vsplit(a, 2)
print(b.shape, c.shape)



'''Произвольное разбиение массива'''
a = np.arange(18)
a.resize(3, 3, 2)
print(a.shape)

b = np.array_split(a, 2, axis=2)
print(type(b))
c = np.array_split(a, 3, axis=0)
print(c.shape)
d = np.array_split(a, 3, axis=1)
print(d.shape)