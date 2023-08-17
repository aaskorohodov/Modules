"""
Descriptors are classes that at least have a __get__ method. The bottom line is that here we can take out in 1 place
a bunch of setters and getters that would otherwise need to be written under each attribute.
"""


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        """Checking that the passed argument is int. Will be called below in __set__"""

        if type(coord) != int:
            raise TypeError("Coordinate must be an integer!")

    def __set_name__(self, owner, name):
        """Name setter

        In this method, we form a local property with the name of the attribute by adding one underscore (as it is
        customary to do when defining descriptors). As a result, class instances will store names _x, _y, _z.
        The method is called automatically"""

        print('instance.name setter invoked')

        self.name = '_' + name

    def __get__(self, instance, owner):
        """ Getter

        self – link to the instance of that class (on which this method aws called)
        instance – link onto pt instance
        owner – link to Point3D (used automatically somewhere inside)
        """

        print('Getter invoked')

        return getattr(instance, self.name)
        # The same as 'return instance.__dict__[self.name]'

    def __set__(self, instance, value):
        """
        self – handle object reference (instance)
        instance – reference to the pt object from which the descriptor was accessed
        value – assigned value
        """
        self.verify_coord(value)
        setattr(instance, self.name, value)
        # Аналог
        # instance.__dict__[self.name] = value
        # print(f"__set__: {self.name} = {value}")


class Point3D:
    """Below, we simply return a reference to x,y,z, which will become instances of the descriptor class. In the
    descriptor class the __set_name__ method will automatically be called, much like __init__. In this method,
    instance's names will be created, it is not clear why, they are not used anywhere, and they are purple for us.
    Main, below"""

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        """Here on the left (where self.x) x is not just a letter, but an instance of Integer. That is, we assign an
        attribute to the name x, which (as it happens) is also an Integer instance. And to the right = is what we write
        there. Those you can take not xyz, but abc and write them on the right and nothing will change. Or you can
        write it not in self.x, but in self.a, and then pt.a will not be an instance of Integer, and we will not check
        if it belongs to int and do some other logic. Well, we will not limit actions with this attribute, but we can,
        if for example, if we do not write a delimiter in the Integer class, then we will not be able to delete it."""

        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
print(pt.z)
