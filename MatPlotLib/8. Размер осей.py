import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

'''Координатные оси на графике подстраиваются под размер графика. Можно изменить их'''

# Делаем фигуру
fig = plt.figure(figsize=(7, 4))
# Получаем ссылку на график, чтобы настроить ее (иначе можно было бы просто сделать plt.plot())
ax = fig.add_subplot()
# Делаем наш график
ax.plot(np.arange(1, 5, 0.25))
# Настраиваем размер
ax.set(xlim=(-5, 30), ylim=(-1, 6))

# Или можно так, аналогично, но методом специальным
# ax.set_xlim(-5, 30)
# ax.set_ylim(-1, 6)

# Или можно без ссылки ax, а просто на последний график с которым работали
# plt.xlim(-1, 20)
# plt.ylim(-1, 6)

# Можно ограничить не все, а что-то одно, для этого есть именованные параметры (xmin, xmax, ymin, ymax)
# ax.set_xlim(xmin = -1)
# ax.set_ylim(ymax = 4)

plt.show()
