"""__init__ handles initialization, it is called automatically when an instance of the class is created.
Since an instance can have local variables that are different from global variables (i.e., registered in the class),
using init can, for example, set local variables for each instance (attributes).

__del__ works in the opposite way, but is also called automatically when it is found that this instance
no one else refers. For example below, deletion occurs at the end of the program."""


class Point:
    def __init__(self, x=1, y=1):
        print(f'Instance created')
        self.x = x
        self.y = y

    def __del__(self):
        print('Instance deleted')

    def set_coords(self, x, y):
        self.x = x
        self.y = y


pt = Point(4, 5)
print(pt.__dict__)
print('asd')
