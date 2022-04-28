from matplotlib.gridspec import GridSpec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

# Создаем фигуру
fig = plt.figure(figsize=(7, 4))
# Разбиваем фигуру на столбцы/строки
gs = GridSpec(ncols=3, nrows=2, figure=fig)

'''Кладем разными способами графики в окно. Тут используются срезы numpy'''
ax1 = plt.subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))
ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))
ax3 = fig.add_subplot(gs[:, 2])
ax3.plot(np.random.random(10))

plt.show()
