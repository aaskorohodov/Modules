import numpy as np


a = np.array([ 1,  2,  3, 10, 20, 30])

print(a.sum())    # 66
print(a.mean())   # 11.0  среднее арифметическое
print(a.max())    # 30
print(a.min())    # 1

# можно использовать на многоерных массивах:

a.resize(3, 2)
# [[ 1  2]
#  [ 3 10]
#  [20 30]]

a.sum()  # 66

# можно применять на конкретные оси:

print(a.sum(axis = 0))
# [24 42] – 24 по первой колонке, 42 по второй


'''Другие штуки (могут принимать как массивы, так и списки или просто числа):

np.abs(x)
Вычисление модуля от аргумента(ов)x; xможет быть числом, списком или массивом (модуль = без знака - минус)

np.amax(x)
Нахождение максимального значения от аргумента(ов)x (найдет максимальное значение в массиве)

np.amin(x)
Нахождение минимального значения от аргумента(ов)x

np.argmax(x)
Нахождение индекса максимального значения для x. (То есть вернет индекс самого большого числа)

np.argmin(x)
Нахождение индекса минимального значения дляx.

np.around(x)
Округление до ближайшего целого.

np.mean(x)
Вычисление среднего значения.

np.log(x)
Вычисление натурального логарифма.

np.log2(x)
Вычисление логарифма по основанию 2.

np.log10(x)
Вычисление логарифма по основанию 10.
'''