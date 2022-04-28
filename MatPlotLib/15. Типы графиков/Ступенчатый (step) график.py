import matplotlib
import numpy as np
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(0, 10)  # Готовим координаты. arange дает числа от 0 до 10 с шагом 1 (если иного не указано)
ax.step(x, x)         # Обязательно передаем координаты и для Х и для У, тут это одни и те же координаты
ax.grid()

ax.step(x, x, '-go')  # Можно указать цвет и маркеры, как для обычного графика

plt.show()

'''
Ступеньки на графике могут иметь первую ступеньку, либо сразу пойти вверх. Это можно настроить:
    ax.step(x, x, '-go', where='post')

Есть 3 варианта:
    pre - дефолтный, сразу вверх, потом ступеньки
    post - сначала первая ступенька (типо уровень земли)
    mid - сначала половина ступеньки, потом как обычно, а переданная координата уже будет не на изломе ступеньки, а
        как бы посередине ступени
'''

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
ax.step(x, x, '-go', where='post')
plt.show()

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
ax.step(x, x, '-go', where='mid')
plt.show()

'''
step умеет принимать несколько графиков в одном вызове и сразу отображать их. Т.е. можно вызвать step 2, 3, 4.. раза,
а можно один раз и скормить ей несколько данных, а при желании и несколько стилей:
'''
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
ax.step(x, x, '-go', x, np.cos(x), '--x', where='mid')
plt.show()
