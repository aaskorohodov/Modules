import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


matplotlib.use('TkAgg')


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25))
ax.plot(np.arange(0, 10, 0.5))

l1 = Line2D([1, 2, 3, 7], [1, 2, 3, 1])  # Просто ломаная линия
ax.add_line(l1)

x = np.arange(-2*np.pi, 2*np.pi, 0.1)  # Что-то по формуле
cos = Line2D(x, np.cos(x))
ax.add_line(cos)

# Готовые фигуры лежать тут
from matplotlib.patches import *
# Посмотреть все можно тут  https://matplotlib.org/stable/api/patches_api.html


rect = Rectangle((0, 0), 5, 7, facecolor='g')  # Расположение, высота-ширина, цвет
ax.add_patch(rect)

plt.show()

