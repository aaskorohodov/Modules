def decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper description, it is"""

        print('Decorator logic')
        func(*args, **kwargs)

    # This is the way to path func's name and description through the decorator
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


@decorator
def my_func():
    """Func description, here is"""

    print('Func, I am')


my_func()
print(my_func.__name__)
help(my_func)


# The same way of doing this, but with functools
from functools import wraps


def decorator(func):
    @wraps(func)  # This is a decorator, it needs the function to be decorated, the rest it will do
    def wrapper(*args, **kwargs):
        print('Decorated')
        func(*args, **kwargs)
    return wrapper


@decorator
def my_func():
    """Description"""

    print('Func, I am')


my_func()
print(my_func.__name__)
help(my_func)
