import numpy as np


'''
np.expand_dims(a, axis) – добавление новой оси;
np.squeeze(a[, axis]) – удаление оси (без удаления элементов).
'''


x_test = np.arange(32).reshape(8, 2, 2)  # массив 8x2x2
x_test4 = np.expand_dims(x_test, axis=0)  # указываем добавить новую ось в самое начало (первая = 0)
# print(x_test)
# print(x_test.shape)

a = np.append(x_test4, x_test4, axis=0)  # добавляем элемент на первую ось. Указываем куда добавим (x_test) и что добавим

'''удаляем элемент, записывая результат в b. Указываем откуда удаляем (а), с какой оси (axis=0) и индекс элемента (0)'''
b = np.delete(a, 0, axis=0)
# print(b)

'''Добавляем последнюю ось'''
b = np.expand_dims(x_test4, axis=-1)
print(b)
print(b.shape)

'''Удаляем все оси, где 1 элемент'''
c = np.squeeze(b)
print(c.shape)