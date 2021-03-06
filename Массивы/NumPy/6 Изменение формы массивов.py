import numpy as np


a = np.arange(10)  # исходный массив
a.shape = 2, 5  # то же представление, но измененное
b = a.reshape(10)  # новое представление с другой переменной но теми же данными


a.shape = -1, 2  # делаем двумерный массив по 2 записи в строке, а -1 = столько строк, сколько получится (если возможно)
# print(a)

a.ravel()  # переделывает массив в одномерный (вектор)

# print(a)
a.resize(3, 3, refcheck=False)  # изменяет массив, несмотря на несоответствие кол-ва элементов
# print(a)
a.resize(3,5, refcheck=False)  # при увеличении, новые ячейки заполняются нулями
# print(a)


'''Транспонирование = переворот матрицы, когда строки превращаются в столбцы. Транспонирование создает лишь нвоое
представление, данные остаются старыми'''
a = np.array([(1,2,3), (4,5,6), (7,8,9)])
print(a)
b = a.T
print(b)


'''Вектор = массив размером в строчку, одномерный. Вектора нельзя транспонировать, в результате ничего не изменится.
Чтобы транспонировать вектор, нужно сначала создать вторую ось'''

print(f'\nx')
x = np.arange(10)
print(x)

x.shape = 1, -1
print('Теперь x имеет две оси, тут две квадратных скобки')
print(x)
x = x.T
print('Теперь это вектор-столбец')
print(x)