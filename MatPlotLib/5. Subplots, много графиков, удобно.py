import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

'''
    subplots(nrows, ncols)

дает ссылку на фигуру и список координатных осей:
'''

f, ax = plt.subplots(2, 2)
print(ax)

ax[0, 0].plot(np.arange(0, 5, 0.2))
ax[0, 0].grid()
ax[0, 1].plot(np.arange(5, 0, -0.2))
ax[0, 1].grid()

plt.show()
