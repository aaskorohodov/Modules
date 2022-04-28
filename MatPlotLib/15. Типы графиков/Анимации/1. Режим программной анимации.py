import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


'''
plt.show() не даст нам обновлять график в цикле, вернее даст, но чтобы шагнуть на следующую итерацию, нужно будет руками
закрыть окно. Поэтому есть встроенные инструменты.
'''

matplotlib.use('TkAgg')

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

plt.ion()  # Включаем интерактивный режим отображения данных

for delay in np.arange(0, np.pi, 0.1):
    y = np.cos(x + delay)

    plt.clf()   # Очищаем предыдущие данные
    plt.plot(x, y)  # Отображаем нужный график
    plt.draw()      # Рисуем
    plt.gcf().canvas.flush_events()  # И это тоже рисуем, хз, внутренние штуки matplotlib

    time.sleep(0.01)

plt.ioff()  # Выключаем интерактивный режим
plt.show()  # Чтобы окно не закрылось

'''
Но это медленно, потому что тут каждый раз рисуется окно и все с ним связанное. Можно менять только данные.
*интерактивный режим в этом случе надо ставить в самое начало, иначе не работает
'''
plt.ion()
fig, ax = plt.subplots()

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

line, = ax.plot(x, y)  # Сохраняем ссылку на объект, представляющий наш график

for delay in np.arange(0, 4 * np.pi, 0.1):
    y = np.cos(x + delay)  # Формируем нужное значение У на каждом шаге

    line.set_ydata(y)  # И обновляем только его

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)

plt.ioff()  # Выключаем интерактивный режим
plt.show()  # Чтобы окно не закрылось