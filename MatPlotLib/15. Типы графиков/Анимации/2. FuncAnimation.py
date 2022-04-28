import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation


'''
Для упрощения создания анимации в пакете matplotlib предусмотрено два специальных класса:
    FuncAnimation – создание анимации на основе функции;
    ArtistAnimation – создание покадровой анимации.

https://matplotlib.org/stable/api/animation_api.html

FuncAnimation работает на функции, т.е. генерирует себе каждый шаг анимации сама на лету.
ArtistAnimation делается из подготовленных заранее объектов, это полезно например для анимации в 3D, потому что
на отрисовку 3D-кадра уходим много времени.
'''


matplotlib.use('TkAgg')

fig, ax = plt.subplots()
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

line, = ax.plot(x, y)


def update_cos(frame, line, x):
    """
    frame - параметр, который меняется от кадра к кадру, в данном случае - это начальная фаза (угол)
    line - ссылка на объект Line2D
    x – аргументы косинусоиды
    """

    line.set_ydata(np.cos(x+frame))
    return [line]


phasa = np.arange(0, 4*np.pi, 0.1)  # Коллекция, которая будет перебираться на каждой итерации

animation = FuncAnimation(
    fig,                # фигура, где отображается анимация
    func=update_cos,    # функция обновления текущего кадра
    frames=phasa,       # параметр, меняющийся от кадра к кадру
    fargs=(line, x),    # дополнительные параметры для функции update_cos
    interval=30,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=False)       # зацикливать ли анимацию


plt.show()
