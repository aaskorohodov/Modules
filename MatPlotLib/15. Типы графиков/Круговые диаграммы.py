import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

vals = [10, 40, 23, 30, 7]  # Значения необязательно должны быть в сумме = 100, хоть что можно, посчитает доли
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
ax.pie(vals, labels=labels)

plt.show()

'''
Полезные параметры:

labels - список подписей для долей
explode - список долей, выносимых из диаграммы
colors - цвета долей
autopct - формат числа величины доли внутри сегмента
pctdistance - расстояние от центра доли до текстовой метки
shadow - отображение тени у диаграммы
labeldistance - расстояние для текстовых метод долей (по умолчанию 1.1)
startangle - начальный угол поворота диаграммы (против часовой стрелки)
radius - радиус диаграммы
counterclock - порядок размещения долей на диаграмме (по часовой стрелки или против часовой) True/False
center - координата центра диаграммы (по умолчанию (0, 0))
frame - отображение рамки вокруг диаграммы (True/False)
wedgeprops - словарь дополнительных параметров (см. класс matplotlib.patches.Wedge)
'''

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

vals = [10, 40, 23, 30, 7]
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
exp = (0.1, 0.2, 0, 0, 0)
ax.pie(vals, labels=labels, autopct='%.2f', explode=exp, shadow=True)

plt.show()


# Другой пример:
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

vals = [10, 40, 23, 30, 7]
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
exp = (0.1, 0.2, 0, 0, 0)
ax.pie(vals, labels=labels, shadow=True, wedgeprops=dict(width=0.5))

plt.show()
