import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


'''
Линии уровней, это что-то похожее на гео-карты, когда высоты указываются линиями. Их можно рисовать в 3D.
Для этого используются функции:
    contour() и contourf() – если данные по осям x, y, z представлены в виде двумерных массивов;
    tricontour() и tricontourf() – если данные для x, y, z представлены одномерными массивами.
'''

matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)

zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

ax_3d.contour(xgrid, ygrid, zgrid)

plt.show()


# Чтобы сделать в 2D, надо сначала сделать двумерную систему координат
fig, ax = plt.subplots(1, 2)

ax[0].contour(xgrid, ygrid, zgrid)
ax[1].contourf(xgrid, ygrid, zgrid)

plt.show()


# Теперь дорисуем к линиям числа
fig, ax = plt.subplots()

# Сохраняем ссылку и передаем её лейбл
c1 = ax.contour(xgrid, ygrid, zgrid)
ax.clabel(c1)  # Или так: c1.clabel()

plt.show()


# Зададим число линий, передав его в с1
fig, ax = plt.subplots()

c1 = ax.contour(xgrid, ygrid, zgrid, 15)
c1.clabel()

plt.show()

# Зададим значение, в котором хотим видеть линии (на карте это может быть определенная высота)
fig, ax = plt.subplots()
c1 = ax.contour(xgrid, ygrid, zgrid, [-0.5, -0.2, 0, 0.2, 0.5])
c1.clabel()

plt.show()


# Зададим цвета
fig, ax = plt.subplots()
c1 = ax.contour(xgrid, ygrid, zgrid, 15, colors=['g', 'b', 'r'])
c1.clabel()

plt.show()


# Зададим цвета через готовую цветовую карту, а также цвет для надписей и их формат
fig, ax = plt.subplots()
c1 = ax.contour(xgrid, ygrid, zgrid, cmap='plasma')
c1.clabel(colors='k', fmt='%.2f')

plt.show()


'''
Похожее, но с помощью функций tricontour() и tricontourf()
'''
fig, ax = plt.subplots()

# Делаем одномерные вектора
x = np.random.rand(100) * 4*np.pi - 2*np.pi
y = np.random.rand(100) * 4*np.pi - 2*np.pi

# Вычисляем значения синуса для этих чисел
z = np.sin(x) * np.sin(y) / (1+np.abs(x * y))

c1 = ax.tricontour(x, y, z, cmap='plasma')
c1.clabel(colors='k', fmt='%.2f')

plt.show()


# Аналогично, только не линии, а цельная поверхность
fig, ax = plt.subplots()
c1 = ax.tricontourf(x, y, z, cmap='plasma')
plt.show()
