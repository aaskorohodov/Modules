import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, FixedLocator, MaxNLocator
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))


'''СКРЫВАЕМ РИСКИ СЕТКИ'''

# Делаем экземпляр нужного класса-сеткоскрывателя
lc = NullLocator()
# Рисуем сетку
ax.grid()
# Скрываем по нужной оси (тут по Х)
# ax.xaxis.set_major_locator(lc)
# set_major_locator = это крупная сетка, дефолтная. Еще есть мелкая, она... мельче и внутри крупной, типо ее еще делит

# plt.show()


'''ЧИСЛО РИСОК'''

# Задаем 10 штук для Y. Причем тут дно и потолок тоже считаются, т.е. будет не 10, а 8 (минус дно и потолок)
ax.yaxis.set_major_locator(LinearLocator(10))
# *но на каждую риску автоматом встанет число, ей соответствующе, что наверняка будет 1.5465468, что ебано
# plt.show()


'''ШАГ РИСОК'''

ax.xaxis.set_major_locator(MultipleLocator(base=3.5))
# plt.show()


'''РИСКИ ТАМ, ГДЕ СКАЖЕМ'''

ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))
# plt.show()

'''КРАСИВОЕ РАЗБИЕНИЕ'''

'''Тут устанавливается максимальное число рисок. Далее алгоритм попробует самостоятельно подобрать число рисок не более
заданного так, чтобы было красиво и без 3.65416161 или подобного'''
ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
# plt.show()



'''
set_minor_locator


Это мелкая сетка, она включается так:

    ax.minorticks_on()
    ax.grid(which='major') 
    ax.grid(which='minor')
    
Тут сначала указывается включить крупную, затем мелкую. Все тоже, что можно делать с крупной, можно делать и с мелкой.
'''

ax.minorticks_on()
ax.grid(which='major')
ax.grid(which='minor')
# plt.show()
