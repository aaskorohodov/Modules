import datetime

num = 123
some_str = 'hello'
print(f'{num=}')  # печатает имя переменной + знак равно + значение переменной
print(f'{num / 2 = }')  # операция внутри f-строки с красивым выводом
print(f'{some_str!r}')  # возвращает формальное представление объекта


more_num = 123.456
now = datetime.datetime.utcnow()
print(f'{more_num:.2f}') # округление до нужного числа знаков
print(f"{now:%Y %m %d}") # форматирование строки

