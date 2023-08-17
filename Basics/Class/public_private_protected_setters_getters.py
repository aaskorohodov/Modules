"""
public, protected, private = access modes to class attributes and methods.

public = normal variables and methods, full access
protected = similar, but shows that this is kinds private (there is no protection)
private = direct access is closed (not even readable), but can be accessed inside the class

To change or read privates, you need to create methods that usually start with get and set, so they are called getters
and setters. The idea is that inside such a method you can do, for example, checking for the data type
(so that the string into a numeric attribute not written)
"""


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        # Here w can add some additional logic, for example check arguments types
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y
