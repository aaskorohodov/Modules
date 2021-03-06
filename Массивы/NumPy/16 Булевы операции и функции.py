import numpy as np


a = np.array([1,2,3,10,20,30])
print(a > 5)  # [False False False  True  True  True]
print(a [a > 5] )  # [10 20 30]

'''Выше, a [a > 5] сначала создаем массив Тру/Фалс, затем сразу даем его в качестве индексов, получаем все значения,
больше 5. Аналогично есть:

a == b  Проверка на равенство
a != b  Проверка на неравенство
a > b   Проверка, что a больше b
a < b   Проверка, что a меньше b
a >= b  Проверка, что a больше или равно b
a <= b  Проверка, что a меньше или равно b

Еще есть аналог в виде функции:

greater(a, b) – выполняет сравнение a > b;
less(a, b) – выполняет сравнение a < b;
equal(a, b) – выполняет сравнение a == b.

np.array_equal(a, b) – возвращает True/False (одна значение, а не массив Тру/Фалс)
np.any(a > 5) – возвращает True, если хотя бы 1 элемент удовлетворяет условиям
np.all(a > 5) – тоже самое, только все элементы должны удовлетворять условию
'''