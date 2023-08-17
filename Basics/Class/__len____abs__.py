"""Initially, user-defined classes do not support len() and abs() methods, but they can be written manually,
using your own logic."""


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        """Calculates length of an object"""

        listed_coords = list(self.__coords)
        distance = listed_coords[-1] - listed_coords[0]
        if distance < 0:
            distance = abs(distance)
        return distance

    def __abs__(self):
        """Making a list of positive values from coords

        Note that map() can apply some method to all elements of iterable object. In this case, it is applied to
        all elements of a list and returns map-object, which we convert into list"""

        return list(map(abs, self.__coords))


p = Point(1, 5, -10)
print(len(p))
print(abs(p))
