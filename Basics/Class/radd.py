class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x} {self.y}]'

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_points(other)
        else:
            return self.add_point_tuple(other)

    def add_points(self, other):
        res = Point()
        res.x = self.x + other.num
        res.y = self.y + other.y
        return res

    def add_point_tuple(self, other):
        res = Point()
        res.x = self.x + other[0]
        res.y = self.y + other[1]
        return res

    def __radd__(self, other):
        """Gives the ability to add an object and a class, not just a class and an object.
        i.e. swaps the elements. Right Add"""

        return self.__add__(other)


a = Point(1, 1)
b = (3, 3)
print(b + a)
print(a + b)
