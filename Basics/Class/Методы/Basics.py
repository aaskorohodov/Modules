'''Базовая работа с методами'''

class Point:
    x = 1; y = 1
    
    def setCoords(self, x, y):
        self.x = x
        self.y = y


pt = Point()
print(pt.__dict__)

# первый способ задать отрибуты экземпляру:
pt.x = 10
pt.y = 10
print(pt.__dict__)

# второй:
pt.setCoords(5, 5)
print(pt.__dict__)

# третий:
Point.setCoords(pt, 3, 3)
print(pt.__dict__)