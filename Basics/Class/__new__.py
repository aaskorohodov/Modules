"""
The __new__ method is called before the class is instantiated.

1. first comes __new__
2. an instance is created
3. __init__ is called (if rewritten)

__new__ returns the address of the newly created object, if this is not done, then the object will be None.
It is not necessary to write this manually, since all classes in Python are inherited from the base object, which
already has __new__. Therefore, you can do this:"""


class Point:
    def __new__(cls, *args, **kwargs):
        print("Invoking __new__ for " + str(cls))
        return super().__new__(cls)


a = Point()

'''cls = reference to the current Point class, args and kwargs are not needed, but it is better to accept them, 
because __init__ can go further, which will require some variables, while when creating an instance (if it is 
created with variables, e.q: a = Point(1,2)) variables are passed to both __new__ and __init__.'''
