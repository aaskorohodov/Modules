"""Methods can also be decorated, and the following shows that a decorator can be placed inside a class, even more so -
- inside the class, you can create a variable to which you can assign the result of the decorator's work. PyCharm
complains about errors but everything works great."""


def decor(decorated_method):
    """The decorator takes a method and returns a newly decorated function. It is important to remember that calling
    a method automatically passes the name of the class instance to itself, so the new function (wrapper) must take
    this name (self)."""

    def wrapper(self):
        lie = 3
        decorated_method(self, lie)
    return wrapper


class Luci:
    def __init__(self):
        self.age = 30

    @decor
    def how_old_are_you(self, lie):
        """This is not a very good example, since without decoration in how_old_are_you() you need to pass lie, and
        after decoration, it's already not needed (lie is declared in the decorator)."""

        print(f'I am {self.age - lie}')


luci = Luci()
luci.how_old_are_you()
