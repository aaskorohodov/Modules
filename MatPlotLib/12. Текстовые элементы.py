import numpy as np
import matplotlib.pyplot as plt
import matplotlib


'''
У каждой оси (объекта Axes) можно определять следующие текстовые элементы:
    title – заголовок для осей
    xlabel, ylabel – подписи для каждой из осей
    text – произвольная текстовая информация в области осей
    annotate – аннотация (текст со стрелкой)

Также, у окна в целом можно задавать такие текстовые элементы:
    subtitle – заголовок для фигуры (окна)
    figtext – размещение произвольной текстовой информации в области окна
'''


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
plt.figtext(0.05, 0.6, 'Текст в области окна', fontsize=24, color='r')
fig.suptitle('Заголовок окна')
ax.set_xlabel('Ox')
ax.set_ylabel('Oy')
ax.text(0.07, 0.7, 'Текст', bbox={'boxstyle': 'darrow', 'facecolor': '#AAAAFF'})

ax.text(0.05, 0.1, 'Произвольный текст в координатных осях')
ax.annotate('Аннотация', xy=(0.3, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})
plt.show()


'''
СВЫОЙСТВА ТЕКСТОВЫХ ПОЛЕЙ

alpha - степень прозрачности (число в диапазоне [0; 1])
backgroundcolor - цвет фона
color или c - цвет текста
fontfamily или family - тип шрифта
fontsize или size - размер шрифта
fontstyle или style - стиль шрифта: {'normal', 'italic', 'oblique'}
fontweight или weight - степень утолщения, число от 0 до 1000 или константы:
    'ultralight'
    'light'
    'normal'
    'regular'
    'book'
    'medium'
    'roman'
    'semibold'
    'demibold'
    'demi'
    'bold'
    'heavy'
    'extra bold'
    'black'
horizontalalignment или ha - выравнивание по горизонтали: {'center', 'right', 'left'}
label - текст заголовка
position - координаты текста (x, y)
rotation - поворот текста: вещественное число [0; 1] или константы {'vertical', 'horizontal'}
verticalalignment или va - выравнивание по вертикали: {'center', 'top', 'bottom', 'baseline', 'center_baseline'}
visible - отображение текста: True/False
x - координата x, вещественное число [0; 1]
y - координата y, вещественное число [0; 1]


Используется так:
    plt.figtext(0.05, 0.6, 'Текст в области окна', fontsize=24, color='r')
'''


# Bbox - дополнительное оформление

'''
boxstyle - вид рамки вокруг текста. Имеет параметры:
    circle
    darrow - стрелка в две стороны <-->
    larrow
    rarrow
    round - квадрат с закруглениями
    roundtooth - квадрат с окантовкой, типо как марка, зубчатая такая
    sawtooth - аналогично, только зубья больше
    square - просто квадрат (прямоугольник)
alpha - степень прозрачности фона
color - цвет фона с рамкой
edgecolor или ec - цвет рамки
facecolor или fc - цвет заливки
fill - использовать ли заливку: True/False
hatch - тип штриховки: {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
linestyle или ls - стиль линии границы: {'-', '--', '-.', ':', '', (offset, on-offseq), ...}
linewidth или lw - толщина рамки
'''

