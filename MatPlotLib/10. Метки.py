import numpy as np
import matplotlib.pyplot as plt
import matplotlib


'''Метки = цифры/буквы, которые на оси ХУ'''

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

# Самый простой способ скрыть метки
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.grid()
# plt.show()

# или можно отключить так:
# ax.xaxis.set_major_formatter(NullFormatter())


'''FormatStrFormatter'''

# Округляем до целого
# ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))

# Два знака после запятой, больше не надо
# ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# Два знака + надпись "у = "
# ax.yaxis.set_major_formatter(FormatStrFormatter('y = %.2f'))


'''Собственная функция для рисок'''

# ax.yaxis.set_major_formatter(FuncFormatter(formatOy))

'''
Тут formatOy это наша функция, придуманная нами, вот она:

def formatOy(x, pos):
    return f"[{x}]" if x < 0 else f"({x})"

В нее будет передаваться
    х = текущая риска, ее значение
    pos = номер риски, ее позиция
'''



'''FixedFormatter

Устанавливает любые метки. Ставит их сам, в порядке объявления. Например ниже мы сделаем FixedLocator, которые заставит
сделать риски в определенных местах, а потом передадим названия этих рисок:
    
    ax.xaxis.set_major_locator(FixedLocator([-3, -2, -1, 0, 1, 2, 3]))
    ax.xaxis.set_major_formatter(FixedFormatter(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
 
На графике будут буквы в местах, отмеченных этими цифрами по х
'''