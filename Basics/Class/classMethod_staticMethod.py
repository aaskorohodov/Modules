"""
@classmethod = метод, имеющий доступ только к атрибутам класса, но не его экземпляров
@staticmethod = метод, не имеющий доступ ни к атрибутам класса, ни к атрибутам экземпляров

Оба определяются внутри класса, путем постановки на метод соответствующего декоратора
"""


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        """Пример использования метода класса (он ниже). Обращение к нему идет через пространство имен класса,
        но эту строчку можно заменить на    if self.validate(x) and self.validate(y)    и будет работать аналогично."""
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
        else:
            self.x = 0
            self.y = 0

    def get_coord(self):
        return self.x, self.y

    @classmethod
    # cls = class, это ссылка на сам класс
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def do_smth():
        print('smth')


a = Vector(5, 101)
print(a.x, a.y)

# Можно звать метод на класс, а можно на экземпляр
print(Vector.validate(5))
print(a.validate(101))

# И так и эдак
a.do_smth()
Vector.do_smth()
