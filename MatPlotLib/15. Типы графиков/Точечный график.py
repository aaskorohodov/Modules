import matplotlib
import numpy as np
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

# Генерируем 500 рандомных точек
x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)

'''
Есть параметры для точек:

s - масштаб точек (число)
c или color - цвет точек
cmap - цветовая схема
alpha - степень прозрачности
linewidths - толщина граничной линии (вокруг точек)
edgecolor - цвет границы
marker - тип маркера
'''


ax.scatter(x, y, s=50, c='g', linewidths=1, marker='s', edgecolors='r')

plt.show()
