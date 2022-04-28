import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
img = Image.open('panda.jpeg')

ax.imshow(img)
plt.show()


fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

# Данные для цветовой (тепловой) карты
data = np.random.randint(0, 255, (10, 10))
ax.pcolormesh(data)
plt.show()

'''
x (первый аргумент) - Двумерный массив numpy в формате (M, N).
cmap - Используемая цветовая карта
edgecolors - Цвет границы вокруг каждой клетки цветовой сетки.
alpha - Степень прозрачности изображения.
shading - Схема заливки: {'flat', 'gouraud'}
snap - Привязка сетки к границам клеток (по умолчанию False)
'''

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

b = ax.pcolormesh(data, edgecolors='black', cmap='plasma')
fig.colorbar(b, ax=ax)  # Сбоку указатель-шкала (какому цвету какое значение)

plt.show()
