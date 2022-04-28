import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 3D-графики лежат в mpl_toolkits.mplot3d


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax_3d = Axes3D(fig)  # Или так: ax_3d = fig.add_subplot(projection='3d')

plt.show()

'''
После создания координатных осей мы можем в них строить двумерные и трехмерные графики с помощью того же самого набора функций:
    plot() – линейный 2D график в трех измерениях;
    step() – ступенчатый 2D график в трех измерениях;
    scatter() – точеный график 3D график.

Также нам становятся доступными следующие дополнительные функции:
    plot_wireframe() – построение каркасной поверхности в 3D;
    plot_surface() – построение непрерывной 3D поверхности.
'''

# Простой график
fig = plt.figure(figsize=(7, 4))
ax_3d = Axes3D(fig)

x = np.linspace(0, 10, 50)
z = np.cos(x)

# Подписываем оси, чтобы было понятно где какая
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

ax_3d.plot(x, x, z)

plt.show()



# Синусоида в плоскости

fig = plt.figure(figsize=(7, 4))
ax_3d = Axes3D(fig)

# Формируем координаты узлов в плоскости xy
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)

# Вычисляем значения синусоиды в этих узлах
zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

ax_3d.plot_wireframe(xgrid, ygrid, zgrid)

plt.show()


# Аналогично, но с другой поверхностью (не сетка а сплошная)
fig = plt.figure(figsize=(7, 4))
ax_3d = Axes3D(fig)
ax_3d.plot_surface(xgrid, ygrid, zgrid)
plt.show()

'''
x, y, z - 2D массивы для построения трехмерных графиков.
rcount, ccount - Максимальное число элементов каркаса по координатам x и y (по умолчанию 50).
rstride, cstride - Величина шага, с которым будут выбираться элементы из массивов x, y (параметры rstride, cstride
    и rcount, ccount – взаимоисключающие).
color - Цвет графика
cmap - Цветовая карта графика
'''


fig = plt.figure(figsize=(7, 4))
ax_3d = Axes3D(fig)
ax_3d.plot_surface(xgrid, ygrid, zgrid, rstride=5, cstride=5, cmap='plasma')
plt.show()


# Тоже самое, но точками
fig = plt.figure(figsize=(7, 4))
ax_3d = Axes3D(fig)
ax_3d.scatter(xgrid, ygrid, zgrid, s=1, color='g')
plt.show()
