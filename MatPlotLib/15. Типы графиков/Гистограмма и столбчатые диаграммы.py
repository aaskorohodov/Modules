import matplotlib
import numpy as np
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

'''Гистограмма складывает числа, попавшие в какой-то столбик, в этот, собственно столбик. Т.е. каждый столбик это сумма
попавших туда чисел. ПО умолчанию разбивает график на 10 столбиков'''

y = np.random.normal(0, 2, 500)
ax.hist(y, 50)  # Передав сюда вторым аргументом число, получим другое количество столбиков
ax.grid()

plt.show()


'''Похожее делает функция bar. Ей первым аргументом передаются имена столбцов, а вторым их высоты. Столбики просто
строятся по очереди.'''
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = [f'H{i+1}' for i in range(10)]
y = np.random.randint(1, 5, len(x))
ax.bar(x, y)

plt.show()


'''bar ожно использовать аналогично hist, но тогда нужно сделать вот сколько действий'''
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

y = np.random.normal(0, 2, 500)
x = np.linspace(np.min(y), np.max(y), 10)  # Числа в заданном количестве, распределенный по заданному интервалу

# Считаем, сколько чисел попало в какой "столбик"
bars = [len(y[np.bitwise_and(y >= x[i], y < x[i+1])]) for i in range(len(x)-1)]
ax.bar(range(len(x)-1), bars)
plt.show()

# Для поворота бочком есть ax.barh()

'''
Функции bar() и barh() содержат ряд полезных параметров:

width - ширина столбцов (число или список)
bottom - начальное значение столбцов (по умолчанию 0)
align - выравнивание столбцов относительно риски: {'center',  'edge'} (по умолчанию 'center')
alpha - степень прозрачности (число от 0 до 1)
color - цвет столбцов
edgecolor - цвет границы
linewidth - толщина линии (вокруг столбца)
xerr, yerr - отображение величины погрешности (ошибки) для столбцов по горизонтали и по вертикали (число или список)
ecolor - цвет рисок линий погрешностей
log - True/False (включение/выключение логарифмического масштаба)
orientation - ориентация столбцов: {'vertical', 'horizontal'}


Пример:
'''

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = [f'H{i+1}' for i in range(10)]
y = np.random.randint(-20, 20, len(x))
ax.bar(x, y, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)
ax.grid()

plt.show()


'''Параметр width дает возможность делать так (ставить столбики рядом друг с другом, типо пары для сравнения):'''

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(10)
y1 = np.random.randint(3, 20, len(x))
y2 = np.random.randint(3, 20, len(x))
w = 0.3
ax.bar(x - w/2, y1, width=w)
ax.bar(x + w/2, y2, width=w)

plt.show()