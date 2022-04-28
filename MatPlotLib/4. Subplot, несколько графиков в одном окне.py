import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

'''
Для отрисовки нескольких графиков в одном окне используется функция subplot:

    subplot(nrows, ncols, index)

nrows, ncols – число строк и столбцов. Тут каждая ячейка будем своим графиком
index – куда в заданную как бы таблицу поставить текущий график
'''

# plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# plt.grid()  # будет только на последнем графике
# plt.show()

# можно так

# ax1 = plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# ax3 = plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# ax1.grid()
# ax2.grid()
# ax3.grid()
# plt.show()

'''
Можно сделать 2 сроки, первую разбить на 3, а вторую не разбивать и сделать там 1 большой график
'''

# ax1 = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
# ax2 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
# ax3 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
# ax4 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))
# plt.show()

'''Также можно указывать одно трехзначное число'''

ax1 = plt.subplot(131)
plt.plot(np.random.random(10))
ax2 = plt.subplot(132)
plt.plot(np.random.random(10))
ax3 = plt.subplot(133)
plt.plot(np.random.random(10))
plt.show()
