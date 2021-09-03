def decorator(func):
    def wrapper(*args, **kwargs):
        print('Decorated')
        func(*args, **kwargs)
    '''
    Это способ перебросить через декоратор имя функции и ее описание. Все просто и наглядно.
    '''
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@decorator
def my_func():
    '''
    My description here is.
    '''
    print('Funch, I am')


my_func()
print(my_func.__name__)
help(my_func)


'''
Ниже второй способ сделать тоже самое, только с использованием библиотеки functools.
'''


from functools import wraps


def decorator(func):
    @wraps(func)  # это декоратор, ему надо передать декорируемую функцию, остальное он сделает сам.
    def wrapper(*args, **kwargs):
        print('Decorated')
        func(*args, **kwargs)
    return wrapper


@decorator
def my_func():
    '''
    My description here is.
    '''
    print('Funch, I am')


my_func()
print(my_func.__name__)
help(my_func)