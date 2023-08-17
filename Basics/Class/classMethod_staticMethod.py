"""
@classmethod = method that only accesses class attributes, not class instances
@staticmethod = method that does not have access to class or instance attributes

Both are defined inside the class by setting the appropriate decorator on the method.
"""


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        """An example of using a class method (it is below). It is accessed through the class namespace,
         but this line can be replaced with if self.validate(x) and self.validate(y) and will work similarly."""

        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
        else:
            self.x = 0
            self.y = 0

    def get_coord(self):
        return self.x, self.y

    @classmethod
    # cls = class, link to the class itself
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def do_something():
        print('Something is done. Great!')


a = Vector(5, 101)
print(a.x, a.y)

# classmethod can be called on class itself or ots instance
print(Vector.validate(5))
print(a.validate(101))

# Both works as well
a.do_something()
Vector.do_something()
