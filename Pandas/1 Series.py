import pandas as pd


print('''series похож на одномерный массив или питоновский список, но имеет индексы, как питоновский словарь.
При выводе, индекс находится слева, а элементы справа. Также при выводе в конце будет указан тип элементов, он может
быть разным, в зависимости от переданных объектов.''')
print()

my_series = pd.Series([5, 6, 7, 8, 9, 10])
print('Пример series my_series:')
print(my_series)
print()

print('my_series.index  Покажет индексы, которые есть в этом массиве')
print(my_series.index)
print()

print('my_series.values  Получим список элементов, в виде объекта numpy')
print(my_series.values)
print()

print('Доступ к элементам можно осуществить по индексам my_series[4]')
print(my_series[4])
print()

print("Но это фактически не индексы, а ключи. В примере выше эти индексы сформированы автоматически, поэтому они "
      "цифры. Но их можно задать руками, указав например буквы"
      "my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])"
      "my_series2['f']")
print()

my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2['f'])
print()


print("Вывод нескольких значений  my_series2[['a', 'b', 'f']]")
print(my_series2[['a', 'b', 'f']])
print()

print("Групповое присваивание my_series2[['a', 'b', 'f']] = 0")
my_series2[['a', 'b', 'f']] = 0
print(my_series2)
print()

print('Фильтрация  my_series2[my_series2 > 0] =>')
print(my_series2[my_series2 > 0])
print()

print("Операции математики  my_series2[my_series2 > 0] * 2 =>")
print(my_series2[my_series2 > 0] * 2)
print()

print("Работа, аналогично словарю  my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})")
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3)

print("Сам объект series обладает свойством name, которым можно задать всему массиву имя. Также имя можно задать "
      "индексам\n"
      "my_series3.name = 'numbers'\n"
      "my_series3.index.name = 'letters'\n")
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)
print()

print("Можно заменить все индексы сразу  \nmy_series3.index = ['A', 'B', 'C', 'D']\n"
      "Но при этом имя индексов теряется + список индексов должен совпадать по длине с массивом")
my_series3.index = ['A', 'B', 'C', 'D']
print(my_series3)