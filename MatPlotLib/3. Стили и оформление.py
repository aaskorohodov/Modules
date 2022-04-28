import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# СТИЛИ ЛИНИИ

matplotlib.use('TkAgg')
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 5, 4, 2])
x2 = np.array([3, 4, 1, 2, 6])
y2 = np.array([1, 2, 3, 4, 5])

'''Если передать в plot третьем аргументом строку, то в ней можно указать тип линии. Всего есть:

    '-' Непрерывная линия (используется по умолчанию)
    '--' Штриховая линия
    '-.' Штрихпунктирная линия
    ':' Пунктирная линия
    'None' или ' ' Без рисования линии
'''

# plt.plot(x, y)
# plt.plot(x2, y2)
# plt.show()

'''plt.plot возвращает ссылку на объект Line2D, который можно настраивать'''

# lines = plt.plot(x, y, '--')
# print(lines)
# plt.setp(lines, linestyle='-.')
# plt.show()


# ЦВЕТ ЛИНИИ

'''
Цвета можно указывать буквами:
    'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'
Либо шестнадцатеричной записью:
    #0000CC

    lines = plt.plot(x, y, '--g', x2, y2, ':m') - передается вместе с типом линии
Еще можно передать с именованным параметром, который будет выбран над тем, что передано строкой:
    lines = plt.plot(x, y, '--g', x2, y2, ':m', color='r') - тут будет красным оба графика
Еще можно передать RGB и RGBA:
    lines = plt.plot(x, y, '--g', x2, y2, ':m', color=(0, 0, 0))
    lines = plt.plot(x, y, '--g', x2, y2, ':m', c=(0, 0, 0, 0.5))
*RGBA это с альфа-каналом, т.е. прозрачность

'''
# lines = plt.plot(x, y, '--', x2, y2, ':', c=(0, 0, 0, 0.1))
# plt.show()


# МАРКЕРЫ ТОЧЕК

'''
Тип записи как с цветом:
    plt.plot(x2, y2, ':o')

Значения:
'o' 'v' '^' '<' '>' '2' '3' '4' 's' 'p' '*' 'h' 'H' '+' 'x' 'D' 'd' '|' '_'

Если передаются, цвета, тип точки и тип линии, то можно передавать в любом порядке:
    lines = plt.plot(x, y, '-go', x2, y2, 's:m')
Можно передать в именованном параметре:
    lines = plt.plot(x, y, '-go', x2, y2, 's:m', marker='d')

Цвет маркера может отличаться от цвета линии, для этого есть markerfacecolor:
    lines = plt.plot(x, y, '-go', x2, y2, 's:m', marker='d', markerfacecolor='w')
'''


# ИМЕНОВАНЫЕ ПАРАМЕТРЫ

'''
Вроде все можно передавать через именованные параметры:
    plt.setp(lines[0], linestyle='-.', marker='s', markerfacecolor='b', linewidth=4)

Вот основные:

alpha - Степень прозрачности графика (значение от 0 до 1)
color или c - Цвет линии
dash_capstyle - Стиль штриховых конечных точек ['butt' | 'round' | 'projecting']
dash_joinstyle - Стиль штриховых соединительных точек ['miter' | 'round' | 'bevel']
data - Данные графика в формате (x, y), где x, y – массивы numpy
linestyle или ls - Стиль линии [ '-' | '--' | '-.' | ':' | 'steps' | ...]
linewidth или lw - Толщина линии (вещественное число)
marker - Маркер точек
markeredgecolor или mec - Цвет границ маркеров
markeredgewidth или mew - Толщина границы маркеров (вещественное число)
markerfacecolor или mfc - Цвет заливки маркеров
markersize или ms - Размер маркеров
solid_capstyle - Стиль конечных точек непрерывной линии ['butt' | 'round' | 'projecting']
solid_joinstyle - Стиль соединительных точек непрерывной линии ['miter' | 'round' | 'bevel']
visible - Показать/скрыть график [True | False]
xdata - Значения для оси абсцисс (массив numpy)
ydata - Значения для оси ординат (массив numpy)
'''


# ЗАЛИВКА

'''Формируем кривую линию-косинусоиду (как волна)'''
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)

'''Далее сделаем заливку. Автоматом (если ничего не передавать), заливаться будет область между 0 по Y (горизонт) и 
графиком'''
plt.fill_between(x, y)
plt.show()

'''Но горизонт можно изменить, например подняв до 0.5 по Y'''
plt.fill_between(x, y, 0.5)
plt.show()

'''Я не понял, что делает where, но вот так получается разноцветный график, потому что функция вызывается дважды'''
plt.fill_between(x, y, where=(y < 0), color='r', alpha=0.5)
plt.fill_between(x, y, where=(y > 0), color='g', alpha=0.5)
plt.show()