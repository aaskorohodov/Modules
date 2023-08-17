"""Below is an example of a decorator in which the local variable name does not disappear after the function is
executed, but is preserved in a variable. Thus, you can call the decorator once by passing it a value, and then access
the decorated function, in which some value will permanently be."""


def func(name):
    def inner_func():
        print('Hi', name)
    return inner_func


a = func('Masha')
b = func('Petia')

a()
b()


def adder(value):
    """Similarly, the adder function writes some value once, and then each call this value
     will be added to the passed arguments. Just another example."""

    def func2(var):
        print(value + var)
    return func2


a = adder(5)
a(5)
