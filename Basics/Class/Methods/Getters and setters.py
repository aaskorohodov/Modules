"""
In Python, the following options for accessing data are possible:

<attribute_name> (without one or two underscores at the beginning) – public property (public);
_<attribute_name> (with single underscore) – protected access mode (can only be accessed within the class and in all its
    child classes)
__<attribute_name> (with two underscores) – private access mode (can only be accessed within the class).

If you set the attributes like this:
     self.__x = x
     self.__y = y
then it's impossible to read them:
     print(pt.__x)  -> raises an error

To write and read such attributes, you need to set the appropriate methods, usually their names start with 'set' and
'get':
     def setCoords(self, x, y):
         self.__x = x
         self.__y = y

     def getCoords(self):
         return self.__x, self.__y

In addition to a little protection against data rewriting, such methods can also check whether the correct data type
is being passed:
     def setCoords(self, x, y):
         if (isinstance(x, int) or isinstance(x, float)) and \
             (isinstance(y, int) or isinstance(y, float)) :
             self.__x = x
             self.__y = y else:
             print("Coordinates must be numbers")

This checks that the passed value is a number."""


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


pt = Point()
pt.set_coords(10, 20)

print(pt.get_coords())
try:
    print(pt.__x)   # Raises an error
except:
    print('Error was raised!')
