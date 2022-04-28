import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

'''Можно создать Figure так'''
# f, ax = plt.subplots(2, 2)
#
# ax[0, 0].plot(np.arange(0, 5, 0.2))
# ax[0, 0].grid()
# ax[0, 1].plot(np.arange(5, 0, -0.2))
# ax[0, 1].grid()

'''
Используя ссылку на объект Figure, можно устанавливать те или иные свойства для всего окна
'''

# f.set_size_inches(7, 4)     # размер 7 x 4 дюймов
# f.set_facecolor('m')        # цвет фона

'''Можно создать figure так'''

fig = plt.figure(figsize=(7, 4))
# plt.plot(np.arange(0, 5, 0.2))
# plt.show()

'''Можно отдельно создать координатную ось и положить в фигуру. '''
ax1 = fig.add_axes([0.0, 0, 1.0, 1.0])  # [pos_x, pos_y, width, height]
ax1.plot(np.arange(0, 5, 0.2))

plt.show()
