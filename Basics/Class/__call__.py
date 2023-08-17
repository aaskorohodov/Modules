"""
__call__ is automatically called whenever there are parentheses () after the variable.
For example, when creating an instance of a class:
    c = Counter()

__call__ internally creates an object in memory, calls __init__ and returns a reference to the created object.
With his help we can turn, for example, class instances into callable objects:
"""


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("Method __call__ invoked")
        self.__counter += 1

        return self.__counter


c = Counter()
c()         # Method __call__ invoked
c()         # Method __call__ invoked
res = c()   # Method __call__ invoked
print(res)
