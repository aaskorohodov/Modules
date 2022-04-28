import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import ArtistAnimation


matplotlib.use('TkAgg')


# 3D-ось
fig = plt.figure(figsize=(10, 6))
ax_3d = fig.add_subplot(projection='3d')

# Координаты сетки
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)

# Список для изменяемого параметра и коллекция для хранения объектов Artist
phasa = np.arange(0, 2*np.pi, 0.1)
frames = []

# В цикле сформируем объекты Artist для последующей их анимации
for p in phasa:
    zgrid = np.sin(xgrid + p) * np.sin(ygrid) / (xgrid * ygrid)

    line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='b')
    frames.append([line])

animation = ArtistAnimation(
    fig,                # фигура, где отображается анимация
    frames,             # кадры
    interval=30,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)        # зацикливать ли анимацию

plt.show()
