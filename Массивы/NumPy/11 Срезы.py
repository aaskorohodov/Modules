import numpy as np


a = np.arange(12)  # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

'''
Общий синтаксис аналогичен спискам:
<имя массива>[start:stop:step]
'''

b = a[2:4]  # array([2, 3])

'''
! Срезы возвращают представление, данные общие !
'''
b[0] = -100  # массив а тоже изменился


a[3:] # array([ 3,  4,  5,  6,  7,  8,  9, 10, 11])
a[:5] # array([ 100,    1, -100,    3,    4])
a[-5: -1] # array([ 7,  8,  9, 10])
a[:] # array([ 100,    1, -100,    3,    4,    5,    6,    7,    8,    9,   10,   11])
a[1:6:2] # array([1, 3, 5])
a[::2] # array([ 100, -100,    4,    6,    8,   10])
a[::-1] # array([  11,   10,    9,    8,    7,    6,    5,    4,    3, -100,  1,  100])


'''Срезу сразу можно что-то присваивать:'''

a[:4] = [-1, -2, -3, -4]  # присваивание списка
a[4::2] = np.array([10, 20, 30, 40])  # присваивание массива

'''Можно перебирать циклом:'''

for x in a:
     print(x, sep=' ', end=' ')