"""

__setattr__(self, key, value) – автоматически вызывается при изменении свойства key класса;
__getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
__getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
__delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).


'Автоматически вызывается' = мы можем его переписать или дополнить, тогда при стандартном действии логика изменится.
Например:
"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y, name):
        self.__x = x
        self.__y = y
        self.name = name

    def __setattr__(self, key, value):
        """Тут запрещается изменять свойство (key=любой атрибут) на z"""
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            '''Тут нужно обратится к самому верхнему классу object, потому что там происходит смена имени. Если тут,
            внутри __setattr__, попробовать сделать так "self.__x = value", то случится бесконечная рекурсия, потому
            что "self.__x = value" будем автоматически вызывать __setattr__, который будет выполнять "self.__x = value",
            который...'''
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        """Тут """
        if item == 'x':
            raise AttributeError(f'Свойство {self}.{item} нельзя удалять, потому что тогда все сломается!')
        else:
            object.__delattr__(self, item)

    def __str__(self):
        """Для красоты, чтобы в ошибке была не белиберда"""
        return self.name


a = Point(1, 2, 'Точка_а')
a.x = 10
del a.x
