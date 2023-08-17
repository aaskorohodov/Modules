"""
@property makes it possible to work with private attributes as if they were normal. This is helpful in order to
limit only part of the functionality, for example, so that data can be written, but cannot be deleted.

property is defined as an attribute, which is given any name you want, and property itself accepts setters, getters, and
delimiters, (in that order) as arguments. property itself will call its first, second or third argument,
depending on the circumstances, will do what is needed and if there is a getter, then it will return what the getter
returns, and if there is - setter will call it.
"""


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

    # A complete analogue of what is above (PyCharm will warn you, but still works)
    # Link to the property
    # old = property()
    # Reference to itself, but with a built-in setter
    # old = old setter(set_old)
    # And the getter
    # old = old getter(get_old)


p = Person('Peter', 30)
d = Person('Dave', 15)
p.old = 35
print(p.old)
print(d.old)

# This will cause an error, because the property is private, it cannot be deleted, there is no delimiter
# del p.old


class Person:
    """The same thing, but with decorators"""

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # Getter MUST always go first
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


print('')
s = Person('Sam', 25)
print(s.old)
s.old = 35
print(s.old)
