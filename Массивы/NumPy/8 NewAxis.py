import numpy as np


a = np.arange(1, 10) # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

'''np.newaxis создает пустые оси.
Синтаксис: в квадратных скобках как бы указывается новое представление матрицы. В скобках указывается np.newaxis и :
np.newaxis = создай новую ось
: = сюда положи старые данные.
Это как бы визуально представление новой матрицы'''

b = a[np.newaxis, :]
print(b.shape)
c = a[np.newaxis, :, np.newaxis]
print(c.shape)
print(c)
print(c[0][3])