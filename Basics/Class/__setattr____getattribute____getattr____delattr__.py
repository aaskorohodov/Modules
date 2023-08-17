"""

__setattr__(self, key, value) - automatically called when the key property of the class changes;
__getattribute__(self, item) - automatically called when getting a class property named item;
__getattr__(self, item) - automatically called when a non-existent item property of the class is received;
__delattr__(self, item) - automatically called when the item property is deleted (it doesn't matter if item exists or
    not).


'Automatically called' == we can overwrite it or add new logic to it
For example:"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y, name):
        self.__x = x
        self.__y = y
        self.name = name

    def __setattr__(self, key, value):
        """Forbidding changing some exact property (key=any attribute)"""

        if key == 'z':
            raise AttributeError("Appropriate property!")
        else:
            '''Here you need to refer to the topmost object class, because there is a name change. If here
             inside __setattr__, try to do this "self.__x = value", then an infinite recursion will happen, because
             that "self.__x = value" will automatically call __setattr__ which will execute "self.__x = value"
             which... you get the idea'''

            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        """Same here, but deleting, instead of setting"""

        if item == 'stand_strong_ukraine':
            raise AttributeError(f'Property {self}.{item} can not deleted!')
        else:
            object.__delattr__(self, item)

    def __str__(self):
        """Making an Exception message look a bit nicer"""

        return self.name


a = Point(1, 2, 'Point A')
a.stand_strong_ukraine = True
del a.stand_strong_ukraine
