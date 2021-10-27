'''
В Python возможны следующие варианты доступа к данным:

<имя атрибута> (без одного или двух подчеркиваний вначале) – публичное свойство (public);
_<имя атрибута> (с одним подчеркиванием) – режим доступа protected (можно обращаться только внутри класса и во всех его дочерних классах)
__<имя атрибута> (с двумя подчеркиваниями) – режим доступа private (можно обращаться только внутри класса).

Если задать атрибуты так:
    self.__x = x; self.__y = y
то прочитать из так уже нельзя
    print( pt.__x )

Чтобы записывать и читать такие атрибуты, нужно задать соответствующие методы, обычно из начинают в set и get:
    def setCoords(self, x, y):
        self.__x = x
        self.__y = y

    def getCoords(self):
        return self.__x, self.__y

Кроме небольшой защиты от переписывания данных, такие методы могут и проверять, корректный ли тип данных передается:
    def setCoords(self, x, y):
        if (isinstance(x, int) or isinstance(x, float)) and \
            (isinstance(y, int) or isinstance(y, float)) :
            self.__x = x
            self.__y = y    else:
            print("Координаты должны быть числами")

Тут проверяется, что переданное значение является чилом
'''

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def setCoords(self, x, y):
        self.__x = x
        self.__y = y

    def getCoords(self):
        return self.__x, self.__y

pt = Point()
pt.setCoords(10, 20)

print( pt.getCoords() )