import matplotlib
import numpy as np
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')             # Первый вариант, как указать имена для легенды
ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')
# ax.legend(['1', '2'])                                          # Второй вариант, он отменит первый
# line1, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')  # Третий вариант, указываем имя тут...
# line2, = ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')   # ... а ниже переименовываем это имя...
# ax.legend((line2, line1), ['Линия 2', 'Линия 1'])              # ... вот тут. Херота получается, но так можно

'''
Расположение легенды можно указать с помощью loc. У него есть:
    ['best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right',
    'lower center', 'upper center', 'center']
'''

# ax.legend(['1', '2'], loc='upper right')

'''
Можно указать положение легенда координатами цифрами, где первая по Х, вторая по У. Цифра от 0 до 1:
    ax.legend(['1', '2'], bbox_to_anchor=(0.5, 0.7))
'''

'''
Для оформления текста в легенде есть:
    fontsize - Размер шрифта, число или строка:
        'xx-small'
        'x-small'
        'small'
        'medium'
        'large'
        'x-large'
        'xx-large'
    frameon - Отображать ли рамку у легенды (True/False, по умолчанию включено)
    framealpha - Прозрачность рамки (вещественное число или None)
    facecolor - Цвет заливки
    edgecolor - Цвет рамки
    title - Текст заголовка, либо значение None
    title_fontsize - Размер шрифта для заголовка
'''

ax.legend(['1', '2'],
          loc='center',
          fontsize='xx-large',
          facecolor='m',
          edgecolor='g',
          title='title',
          title_fontsize='xx-large')

plt.show()
